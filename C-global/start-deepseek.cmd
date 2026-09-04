@echo off
chcp 65001 >nul
cd /d "%USERPROFILE%\.claude"

if "%DEEPSEEK_API_KEY%"=="" (
  echo [错误] 环境变量 DEEPSEEK_API_KEY 未设置
  echo 请先执行: setx DEEPSEEK_API_KEY "sk-你的DeepSeek密钥"
  echo 然后重新打开终端再运行此脚本。
  pause
  exit /b 1
)

echo [1/3] 检查代理是否已在运行...
netstat -ano | findstr ":3456" >nul
if %errorlevel% equ 0 (
  echo     代理已在运行，跳过启动
) else (
  echo [2/3] 启动 DeepSeek 本地代理...
  start /min "DeepSeek Bridge" node "%USERPROFILE%\.claude\deepseek-bridge.js"
  timeout /t 2 /nobreak >nul
)

echo [3/3] 启动 Claude Code (DeepSeek 模式)...
claude --settings "%USERPROFILE%\.claude\settings-deepseek.json"
