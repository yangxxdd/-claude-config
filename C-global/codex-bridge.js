const http = require('http');
const https = require('https');

const PORT = process.env.CODEX_BRIDGE_PORT || 3457;
const TARGET_HOST = process.env.CODEX_BRIDGE_TARGET || 'api.deepseek.com';
const TARGET_PATH = '/v1/chat/completions';
const DEFAULT_API_KEY = process.env.DEEPSEEK_API_KEY || '';

let idCounter = 0;
function uid() {
  return `${Date.now().toString(36)}${(++idCounter).toString(36)}${Math.random().toString(36).slice(2, 6)}`;
}

function log(...args) {
  console.log(`[${new Date().toISOString()}]`, ...args);
}

// ── Request: Responses API → Chat Completions ──────────────────────

function extractText(content) {
  if (!content) return '';
  if (typeof content === 'string') return content;
  if (Array.isArray(content)) {
    return content
      .filter(c => c.type === 'input_text' || c.type === 'output_text' || c.type === 'text')
      .map(c => c.text || '')
      .join('');
  }
  return '';
}

function convertInputToMessages(input, instructions) {
  const messages = [];

  if (instructions) {
    messages.push({ role: 'system', content: instructions });
  }

  if (!input || !Array.isArray(input)) return messages;

  for (const item of input) {
    // User / system input
    if (item.role === 'user' || item.role === 'system') {
      const text = extractText(item.content);
      messages.push({ role: 'user', content: text });
      continue;
    }

    // Assistant output (text)
    if (item.role === 'assistant') {
      const text = extractText(item.content);
      if (text) {
        messages.push({ role: 'assistant', content: text });
      }
      continue;
    }

    // Function call (assistant tool use from previous turn)
    if (item.type === 'function_call') {
      messages.push({
        role: 'assistant',
        content: null,
        tool_calls: [{
          id: item.call_id || item.id,
          type: 'function',
          function: {
            name: item.name,
            arguments: item.arguments
          }
        }]
      });
      continue;
    }

    // Function call output (tool result)
    if (item.type === 'function_call_output') {
      messages.push({
        role: 'tool',
        tool_call_id: item.call_id,
        content: item.output || ''
      });
      continue;
    }

    // Skip reasoning / unknown item types
  }

  return messages;
}

function convertTools(tools) {
  if (!tools || !Array.isArray(tools)) return undefined;
  const result = tools
    .filter(t => t.type === 'function')
    .map(t => ({
      type: 'function',
      function: {
        name: t.name,
        description: t.description || '',
        parameters: t.parameters || {}
      }
    }));
  return result.length ? result : undefined;
}

// ── Response: Chat Completions → Responses API (non-streaming) ─────

function buildSyncResponse(chatResp, model) {
  const respId = 'resp_' + uid();
  const choice = chatResp.choices?.[0];
  const message = choice?.message || {};
  const output = [];

  if (message.content) {
    output.push({
      id: 'msg_' + uid(),
      type: 'message',
      role: 'assistant',
      status: 'completed',
      content: [{ type: 'output_text', text: message.content }]
    });
  }

  if (message.tool_calls) {
    for (const tc of message.tool_calls) {
      output.push({
        id: 'fc_' + uid(),
        type: 'function_call',
        call_id: tc.id,
        name: tc.function.name,
        arguments: tc.function.arguments,
        status: 'completed'
      });
    }
  }

  return {
    id: respId,
    object: 'response',
    status: 'completed',
    model: model,
    output: output,
    usage: chatResp.usage ? {
      input_tokens: chatResp.usage.prompt_tokens || 0,
      output_tokens: chatResp.usage.completion_tokens || 0,
      total_tokens: chatResp.usage.total_tokens || 0
    } : null
  };
}

// ── SSE helpers ────────────────────────────────────────────────────

function sse(res, event, data) {
  res.write(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`);
}

// ── Response: Chat Completions SSE → Responses API SSE ─────────────

function handleStream(res, upstreamRes, model) {
  const respId = 'resp_' + uid();
  const msgId = 'msg_' + uid();

  sse(res, 'response.created', {
    type: 'response.created',
    response: { id: respId, object: 'response', status: 'in_progress', model: model, output: [] }
  });

  sse(res, 'response.in_progress', {
    type: 'response.in_progress',
    response: { id: respId, object: 'response', status: 'in_progress', model: model, output: [] }
  });

  sse(res, 'response.output_item.added', {
    type: 'response.output_item.added',
    output_index: 0,
    item: { id: msgId, type: 'message', role: 'assistant', status: 'in_progress', content: [] }
  });

  sse(res, 'response.content_part.added', {
    type: 'response.content_part.added',
    item_id: msgId, output_index: 0, content_index: 0,
    part: { type: 'output_text', text: '' }
  });

  let fullText = '';
  let finishReason = null;
  let inputTokens = 0;
  const toolCalls = {};   // index → { id, name, arguments }
  let hasText = false;

  let buf = '';
  upstreamRes.on('data', chunk => {
    buf += chunk.toString();
    const lines = buf.split('\n');
    buf = lines.pop();

    for (const line of lines) {
      if (!line.trim() || line.startsWith(':')) continue;
      if (!line.startsWith('data: ')) continue;

      const payload = line.slice(6).trim();
      if (payload === '[DONE]') continue;

      let parsed;
      try { parsed = JSON.parse(payload); } catch (_) { continue; }

      const choice = parsed.choices?.[0];
      if (!choice) continue;

      const delta = choice.delta || {};
      if (choice.finish_reason) finishReason = choice.finish_reason;
      if (parsed.usage) {
        inputTokens = parsed.usage.prompt_tokens || inputTokens;
      }

      // ── text content ──
      if (delta.content) {
        hasText = true;
        fullText += delta.content;
        sse(res, 'response.content_part.delta', {
          type: 'response.content_part.delta',
          item_id: msgId, output_index: 0, content_index: 0,
          delta: { type: 'text_delta', text: delta.content }
        });
      }

      // ── tool calls ──
      if (delta.tool_calls) {
        for (const tc of delta.tool_calls) {
          const idx = tc.index;
          if (!toolCalls[idx]) toolCalls[idx] = { id: '', name: '', arguments: '' };
          if (tc.id) toolCalls[idx].id = tc.id;
          if (tc.function?.name) toolCalls[idx].name = tc.function.name;
          if (tc.function?.arguments) toolCalls[idx].arguments += tc.function.arguments;
        }
      }
    }
  });

  upstreamRes.on('end', () => {
    // End text content part
    sse(res, 'response.content_part.done', {
      type: 'response.content_part.done',
      item_id: msgId, output_index: 0, content_index: 0,
      part: { type: 'output_text', text: fullText }
    });

    // End message output item
    sse(res, 'response.output_item.done', {
      type: 'response.output_item.done',
      output_index: 0,
      item: {
        id: msgId, type: 'message', role: 'assistant', status: 'completed',
        content: hasText ? [{ type: 'output_text', text: fullText }] : []
      }
    });

    // Emit function_call output items
    let outIdx = 1;
    const tcIndices = Object.keys(toolCalls).sort((a, b) => a - b);
    for (const idx of tcIndices) {
      const tc = toolCalls[idx];
      const fcId = 'fc_' + uid();

      sse(res, 'response.output_item.added', {
        type: 'response.output_item.added',
        output_index: outIdx,
        item: { id: fcId, type: 'function_call', call_id: tc.id, name: tc.name, arguments: tc.arguments, status: 'in_progress' }
      });

      sse(res, 'response.output_item.done', {
        type: 'response.output_item.done',
        output_index: outIdx,
        item: { id: fcId, type: 'function_call', call_id: tc.id, name: tc.name, arguments: tc.arguments, status: 'completed' }
      });

      outIdx++;
    }

    // Final event
    const outTokens = fullText.length;
    sse(res, 'response.completed', {
      type: 'response.completed',
      response: {
        id: respId, object: 'response', status: 'completed', model: model, output: [],
        usage: {
          input_tokens: inputTokens || 0,
          output_tokens: outTokens,
          total_tokens: (inputTokens || 0) + outTokens
        }
      }
    });

    res.end();
  });

  upstreamRes.on('error', (err) => {
    log('Stream error:', err.message);
    if (!res.headersSent) res.statusCode = 502;
    res.end();
  });
}

// ── Main server ────────────────────────────────────────────────────

const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization, x-api-key');

  if (req.method === 'OPTIONS') { res.statusCode = 204; res.end(); return; }

  // GET /v1/models
  if (req.method === 'GET' && (req.url === '/v1/models' || req.url.startsWith('/v1/models?'))) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({
      object: 'list',
      data: [{
        id: 'deepseek-chat',
        object: 'model',
        owned_by: 'deepseek',
        context_window: 131072,
        max_context_window: 131072
      }]
    }));
    return;
  }

  // POST /v1/responses
  if (req.method === 'POST' && req.url === '/v1/responses') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      let parsed;
      try { parsed = JSON.parse(body); } catch (e) {
        res.statusCode = 400;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({ error: { message: 'Invalid JSON' } }));
        return;
      }
      handleResponses(req, res, parsed);
    });
    return;
  }

  // 404
  res.statusCode = 404;
  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify({ error: { message: 'Not found' } }));
});

function handleResponses(req, res, body) {
  const model = body.model || 'deepseek-chat';
  const stream = body.stream === true;

  log(`${stream ? 'STREAM' : 'SYNC'} model=${model}`);

  const authHdr = req.headers['authorization'] || req.headers['x-api-key'] || '';
  const apiKey = authHdr.replace(/^Bearer\s+/i, '') || DEFAULT_API_KEY;

  const chatBody = {
    model: 'deepseek-chat',
    messages: convertInputToMessages(body.input, body.instructions),
    max_tokens: body.max_output_tokens || 8192,
    temperature: body.temperature ?? 0.7,
    stream: stream
  };

  if (body.top_p !== undefined) chatBody.top_p = body.top_p;

  const tools = convertTools(body.tools);
  if (tools) chatBody.tools = tools;

  const payload = JSON.stringify(chatBody);

  log('→', JSON.stringify({
    model: chatBody.model,
    msgs: chatBody.messages.length,
    tools: chatBody.tools?.length || 0,
    stream: chatBody.stream,
    firstMsg: chatBody.messages[0]?.content?.slice(0, 100),
    lastMsg: chatBody.messages[chatBody.messages.length - 1]?.content?.slice(0, 100),
    payloadLen: payload.length
  }));

  const upstreamReq = https.request({
    hostname: TARGET_HOST,
    port: 443,
    path: TARGET_PATH,
    method: 'POST',
    timeout: 120000,
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(payload),
      'Authorization': `Bearer ${apiKey}`,
      'Accept': stream ? 'text/event-stream' : 'application/json'
    }
  }, (upstreamRes) => {
    if (upstreamRes.statusCode >= 400) {
      let errData = '';
      upstreamRes.on('data', c => errData += c);
      upstreamRes.on('end', () => {
        log('Upstream error:', upstreamRes.statusCode, errData.slice(0, 1000));
        log('Request payload (first 2000 chars):', payload.slice(0, 2000));
        res.statusCode = upstreamRes.statusCode;
        res.setHeader('Content-Type', 'application/json');
        res.end(errData);
      });
      return;
    }

    if (stream) {
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/event-stream');
      res.setHeader('Cache-Control', 'no-cache');
      res.setHeader('Connection', 'keep-alive');
      handleStream(res, upstreamRes, model);
    } else {
      let data = '';
      upstreamRes.on('data', c => data += c);
      upstreamRes.on('end', () => {
        try {
          const chatResp = JSON.parse(data);
          res.setHeader('Content-Type', 'application/json');
          res.end(JSON.stringify(buildSyncResponse(chatResp, model)));
        } catch (e) {
          log('Parse error:', e.message);
          res.statusCode = 500;
          res.setHeader('Content-Type', 'application/json');
          res.end(JSON.stringify({ error: { message: 'Failed to parse upstream' } }));
        }
      });
    }
  });

  upstreamReq.on('error', (err) => {
    log('Upstream request error:', err.message);
    if (!res.headersSent) {
      res.statusCode = 502;
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify({ error: { message: err.message } }));
    }
  });

  upstreamReq.write(payload);
  upstreamReq.end();
}

server.listen(PORT, () => {
  log(`Codex Bridge running on http://localhost:${PORT}`);
  log(`Target: https://${TARGET_HOST}${TARGET_PATH}`);
  if (!DEFAULT_API_KEY) log('WARNING: DEEPSEEK_API_KEY not set — relying on Codex Authorization header');
});

process.on('SIGINT', () => {
  log('Shutting down...');
  server.close(() => process.exit(0));
});
