---
name: claude-dual-config-sync
description: D盘项目 bat 启动走独立配置目录，sync-model.js 负责与 cc switch 主配置同步模型
metadata: 
  node_type: memory
  type: project
  originSessionId: e85eb6d5-7864-4d44-96d9-988d2cdc28b7
  modified: 2026-08-03T08:08:52.987Z
---

用户环境有两套 Claude 配置（2026-08-03 确定为有意设计，勿合并）：

- **主配置**：`C:\Users\yangxd\.claude\settings.json` — cc switch 切换模型时改写这里
- **D盘项目配置**：`D:\claude-projects\claude-config\settings.json` — 三个项目 bat（start-GTS/幻宠/日常.bat）通过 `set CLAUDE_CONFIG_DIR` 指向它，会话/记忆按项目目录隔离存储

**同步机制**：每个 bat 启动前执行 `node D:\claude-projects\sync-model.js`，把主配置的 env 块（模型/接口/token）合并进 D 盘配置。曾发现 D 盘 env 写死 deepseek 导致 cc switch 失效，已通过此脚本解决。D 盘原配置备份在 `settings.json.bak-20260803`。

**Why**: settings.json 的 env 块优先级高于 /model 和 cc switch；两套配置目录互不读取，必须靠脚本桥接。

**How to apply**: 用户反映"bat 启动模型不对/cc switch 没生效"时，先对比两个 settings.json 的 env 块，再检查 sync-model.js 是否被 bat 调用。修改任一配置时注意另一边是否需要同步。
