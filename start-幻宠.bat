@echo off
chcp 65001 > nul
set CLAUDE_CONFIG_DIR=D:\claude-projects\claude-config
node "D:\claude-projects\sync-model.js"
cd /d D:\claude-projects\projects\幻宠
claude
