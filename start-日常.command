#!/bin/bash
# 日常项目启动脚本（Mac 版）—— 对应 Windows 的 start-日常.bat
export CLAUDE_CONFIG_DIR="$HOME/claude-projects/claude-config"
node "$HOME/claude-projects/sync-model.js"
cd "$HOME/claude-projects/projects/日常" || exit 1
exec claude
