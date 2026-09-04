#!/bin/bash
# GTS 项目启动脚本（Mac 版）—— 对应 Windows 的 start-GTS.bat
export CLAUDE_CONFIG_DIR="$HOME/claude-projects/claude-config"
node "$HOME/claude-projects/sync-model.js"
cd "$HOME/claude-projects/projects/GTS" || exit 1
exec claude
