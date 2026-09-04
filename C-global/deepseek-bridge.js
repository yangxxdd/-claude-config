const http = require('http');
const https = require('https');

const PORT = process.env.DEEPSEEK_BRIDGE_PORT || 3456;
const TARGET = 'api.deepseek.com';

function log(...args) {
  console.log(`[${new Date().toISOString()}]`, ...args);
}

function convertMessages(body) {
  const messages = [];

  if (body.system) {
    messages.push({ role: 'user', content: `[System] ${body.system}` });
  }

  if (body.messages && Array.isArray(body.messages)) {
    for (const msg of body.messages) {
      if (msg.role === 'system') {
        messages.push({ role: 'user', content: `[System] ${msg.content}` });
      } else {
        messages.push({ role: msg.role, content: msg.content });
      }
    }
  }

  return messages;
}

function convertResponse(openaiBody, originalModel) {
  const choice = openaiBody.choices && openaiBody.choices[0];
  const content = (choice && choice.message && choice.message.content) || '';

  return {
    id: openaiBody.id || `msg_${Date.now()}`,
    type: 'message',
    role: 'assistant',
    model: originalModel,
    content: [{ type: 'text', text: content }],
    stop_reason: choice && choice.finish_reason === 'stop' ? 'end_turn' : null,
    usage: openaiBody.usage || { input_tokens: 0, output_tokens: 0 }
  };
}

function sendSSE(res, event, dataObj) {
  const data = JSON.stringify(dataObj);
  res.write(`event: ${event}\ndata: ${data}\n\n`);
}

function handleRequest(req, res, bodyStr) {
  try {
    const body = JSON.parse(bodyStr);
    log(`${req.method} ${req.url} model=${body.model || '?'} stream=${body.stream || false}`);

    const isStream = body.stream === true;

    const openaiBody = {
      model: body.model === 'claude-sonnet-4' || body.model === 'sonnet'
        ? 'deepseek-chat'
        : (body.model || 'deepseek-chat'),
      messages: convertMessages(body),
      max_tokens: body.max_tokens || 4096,
      temperature: body.temperature ?? 0.7,
      stream: isStream
    };

    if (body.top_p !== undefined) openaiBody.top_p = body.top_p;
    if (body.stop !== undefined) openaiBody.stop = body.stop;

    const requestOptions = {
      hostname: TARGET,
      port: 443,
      path: '/v1/chat/completions',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': req.headers.authorization || `Bearer ${process.env.DEEPSEEK_API_KEY || ''}`,
        'Accept': isStream ? 'text/event-stream' : 'application/json'
      }
    };

    if (!isStream) {
      const proxyReq = https.request(requestOptions, (proxyRes) => {
        let data = '';
        proxyRes.on('data', chunk => data += chunk);
        proxyRes.on('end', () => {
          res.statusCode = proxyRes.statusCode;
          res.setHeader('Content-Type', 'application/json');

          if (proxyRes.statusCode >= 200 && proxyRes.statusCode < 300) {
            try {
              const openaiResp = JSON.parse(data);
              const anthropicResp = convertResponse(openaiResp, body.model);
              res.end(JSON.stringify(anthropicResp));
            } catch (e) {
              res.end(data);
            }
          } else {
            res.end(data);
          }
        });
      });

      proxyReq.on('error', (err) => {
        log('Request error:', err.message);
        res.statusCode = 502;
        res.end(JSON.stringify({ error: err.message }));
      });

      proxyReq.write(JSON.stringify(openaiBody));
      proxyReq.end();
      return;
    }

    // Streaming
    const proxyReq = https.request(requestOptions, (proxyRes) => {
      if (proxyRes.statusCode < 200 || proxyRes.statusCode >= 300) {
        let errorData = '';
        proxyRes.on('data', chunk => errorData += chunk);
        proxyRes.on('end', () => {
          res.statusCode = proxyRes.statusCode;
          res.setHeader('Content-Type', 'application/json');
          log('Upstream error:', proxyRes.statusCode, errorData.slice(0, 500));
          res.end(errorData || JSON.stringify({ error: `Upstream returned ${proxyRes.statusCode}` }));
        });
        return;
      }

      res.statusCode = proxyRes.statusCode;
      res.setHeader('Content-Type', 'text/event-stream');
      res.setHeader('Cache-Control', 'no-cache');
      res.setHeader('Connection', 'keep-alive');

      const msgId = `msg_${Date.now()}`;
      let streamEnded = false;
      let outputTokens = 0;

      sendSSE(res, 'message_start', {
        type: 'message_start',
        message: {
          id: msgId,
          type: 'message',
          role: 'assistant',
          model: body.model,
          content: [],
          stop_reason: null,
          usage: { input_tokens: 0, output_tokens: 0 }
        }
      });

      sendSSE(res, 'content_block_start', {
        type: 'content_block_start',
        index: 0,
        content_block: { type: 'text', text: '' }
      });

      let buffer = '';
      proxyRes.on('data', chunk => {
        buffer += chunk;
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
          if (!line.trim() || line.startsWith(':')) continue;
          if (!line.startsWith('data: ')) continue;

          const dataStr = line.slice(6).trim();
          if (dataStr === '[DONE]') {
            if (!streamEnded) {
              streamEnded = true;
              sendSSE(res, 'content_block_stop', { type: 'content_block_stop', index: 0 });
              sendSSE(res, 'message_delta', {
                type: 'message_delta',
                delta: {
                  stop_reason: 'end_turn',
                  stop_sequence: null,
                  usage: { output_tokens: outputTokens }
                }
              });
              sendSSE(res, 'message_stop', { type: 'message_stop' });
            }
            continue;
          }

          try {
            const parsed = JSON.parse(dataStr);
            const choice = parsed.choices && parsed.choices[0];
            const delta = choice && choice.delta;

            if (delta && delta.content) {
              outputTokens += 1; // approximate
              sendSSE(res, 'content_block_delta', {
                type: 'content_block_delta',
                index: 0,
                delta: { type: 'text_delta', text: delta.content }
              });
            }

            // DeepSeek may send finish_reason in the last delta chunk before [DONE]
            if (choice && choice.finish_reason && !streamEnded) {
              streamEnded = true;
              sendSSE(res, 'content_block_stop', { type: 'content_block_stop', index: 0 });
              sendSSE(res, 'message_delta', {
                type: 'message_delta',
                delta: {
                  stop_reason: 'end_turn',
                  stop_sequence: null,
                  usage: { output_tokens: outputTokens }
                }
              });
              sendSSE(res, 'message_stop', { type: 'message_stop' });
            }
          } catch (e) {
            // ignore malformed lines
          }
        }
      });

      proxyRes.on('end', () => {
        if (!streamEnded) {
          streamEnded = true;
          sendSSE(res, 'content_block_stop', { type: 'content_block_stop', index: 0 });
          sendSSE(res, 'message_delta', {
            type: 'message_delta',
            delta: {
              stop_reason: 'end_turn',
              stop_sequence: null,
              usage: { output_tokens: outputTokens }
            }
          });
          sendSSE(res, 'message_stop', { type: 'message_stop' });
        }
        res.end();
      });
    });

    proxyReq.on('error', (err) => {
      log('Stream error:', err.message);
      res.statusCode = 502;
      res.end();
    });

    log('-> DeepSeek body:', JSON.stringify(openaiBody).slice(0, 500));
    proxyReq.write(JSON.stringify(openaiBody));
    proxyReq.end();

  } catch (err) {
    log('Error:', err.message);
    res.statusCode = 500;
    res.end(JSON.stringify({ error: err.message }));
  }
}

const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') {
    res.statusCode = 204;
    res.end();
    return;
  }

  let body = '';
  req.on('data', chunk => body += chunk);
  req.on('end', () => handleRequest(req, res, body));
});

server.listen(PORT, () => {
  log(`DeepSeek bridge running on http://localhost:${PORT}`);
  log(`Target: https://${TARGET}`);
});

process.on('SIGINT', () => {
  log('Shutting down...');
  server.close(() => process.exit(0));
});
