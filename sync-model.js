// 启动前同步模型配置（跨平台：Windows / macOS / Linux）：
// 把 cc switch 管理的主配置（~/.claude/settings.json）中的 env 块
// 合并进项目共享配置（$CLAUDE_CONFIG_DIR/settings.json），
// 使项目启动的 Claude 跟随 cc switch 当前选择的模型/接口/token。
// 同步失败不阻断启动，仅提示。

const fs = require('fs');
const os = require('os');
const path = require('path');

// 主配置固定在家目录；项目配置取自 CLAUDE_CONFIG_DIR 环境变量
const SRC = path.join(os.homedir(), '.claude', 'settings.json');
const DST = process.env.CLAUDE_CONFIG_DIR
  ? path.join(process.env.CLAUDE_CONFIG_DIR, 'settings.json')
  : path.join(os.homedir(), '.claude', 'settings.json');

try {
  const src = JSON.parse(fs.readFileSync(SRC, 'utf8'));
  const dst = JSON.parse(fs.readFileSync(DST, 'utf8'));

  if (!src.env || Object.keys(src.env).length === 0) {
    console.log('[sync-model] 主配置没有 env 块，跳过同步');
    process.exit(0);
  }

  dst.env = { ...(dst.env || {}), ...src.env };
  fs.writeFileSync(DST, JSON.stringify(dst, null, 2) + '\n', 'utf8');

  const model = src.env.ANTHROPIC_MODEL || '(未指定模型)';
  const base = src.env.ANTHROPIC_BASE_URL || 'Anthropic 官方接口';
  console.log(`[sync-model] 已同步 -> 模型: ${model} | 接口: ${base}`);
} catch (e) {
  console.log('[sync-model] 同步失败（不影响启动）: ' + e.message);
}
