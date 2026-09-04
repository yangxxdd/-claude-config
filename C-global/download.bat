@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ============================================
echo   Claude Code 配置 — 从 GitHub 下载
echo ============================================
echo.

REM ==========================================
REM 步骤 0：检查 Git 是否安装
REM ==========================================
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [错误] 没有找到 Git！
    echo 请先去 https://git-scm.com/download/win 下载安装 Git
    echo 安装后重新运行本脚本
    pause
    exit /b 1
)
echo [检查] Git 已安装
echo.

REM ==========================================
REM 步骤 1：输入 GitHub 仓库地址
REM ==========================================
echo [1/6] 请输入你的 GitHub 仓库地址
echo.
echo 格式示例：https://github.com/yangxd/claude-config.git
echo.
set /p REPO_URL="仓库地址: "
if "%REPO_URL%"=="" (
    echo 未输入地址，退出
    pause
    exit /b 1
)
echo.

REM ==========================================
REM 步骤 2：备份现有配置
REM ==========================================
echo [2/6] 检查现有配置...
set CLAUDE_DIR=%USERPROFILE%\.claude
set BACKUP_DIR=%USERPROFILE%\.claude-backup-%date:~0,4%%date:~5,2%%date:~8,2%-%time:~0,2%%time:~3,2%%time:~6,2%
set BACKUP_DIR=%BACKUP_DIR: =0%

if exist "%CLAUDE_DIR%" (
    echo 发现已有 .claude 目录，备份到:
    echo %BACKUP_DIR%
    xcopy "%CLAUDE_DIR%" "%BACKUP_DIR%" /E /I /Q /H 2>nul
    echo 备份完成
) else (
    echo 当前没有 .claude 目录，无需备份
)
echo.

REM ==========================================
REM 步骤 3：克隆仓库到临时目录
REM ==========================================
echo [3/6] 从 GitHub 下载配置...
set TEMP_DIR=%TEMP%\claude-config-temp
if exist "%TEMP_DIR%" rmdir /S /Q "%TEMP_DIR%"

git clone "%REPO_URL%" "%TEMP_DIR%" 2>nul
if %errorlevel% neq 0 (
    echo.
    echo [错误] 克隆失败！请检查：
    echo   1. 仓库地址是否正确
    echo   2. 仓库是否为私有（需要先在 GitHub 上登录或配置 SSH Key）
    echo   3. 网络是否正常
    pause
    exit /b 1
)
echo 下载完成
echo.

REM ==========================================
REM 步骤 4：输入 API Key
REM ==========================================
echo [4/6] 配置 API Key
echo.
echo 请输入你的 DeepSeek API Key（sk- 开头，在 DeepSeek 后台获取）：
echo （直接回车则跳过，之后可以手动修改配置文件）
echo.
set /p API_KEY="API Key: "
echo.

REM ==========================================
REM 步骤 5：生成配置文件
REM ==========================================
echo [5/6] 生成配置文件...

REM 获取当前用户的实际 Home 路径
set HOME_PATH=C:/Users/%USERNAME%
echo   你的用户目录: %HOME_PATH%

REM --- 生成 settings.json ---
if exist "%TEMP_DIR%\settings.template.json" (
    copy "%TEMP_DIR%\settings.template.json" "%CLAUDE_DIR%\settings.json" /Y >nul
    if not "%API_KEY%"=="" (
        powershell -Command "(Get-Content '%CLAUDE_DIR%\settings.json' -Raw) -replace '{{DEEPSEEK_API_KEY}}', '%API_KEY%' | Set-Content '%CLAUDE_DIR%\settings.json' -Encoding UTF8"
    )
    powershell -Command "(Get-Content '%CLAUDE_DIR%\settings.json' -Raw) -replace '%%USERPROFILE%%', '%HOME_PATH%' | Set-Content '%CLAUDE_DIR%\settings.json' -Encoding UTF8"
    echo   settings.json — 已生成
)

REM --- 生成 mcp.json ---
if exist "%TEMP_DIR%\mcp.template.json" (
    copy "%TEMP_DIR%\mcp.template.json" "%CLAUDE_DIR%\mcp.json" /Y >nul
    if not "%API_KEY%"=="" (
        powershell -Command "(Get-Content '%CLAUDE_DIR%\mcp.json' -Raw) -replace '{{DEEPSEEK_API_KEY}}', '%API_KEY%' | Set-Content '%CLAUDE_DIR%\mcp.json' -Encoding UTF8"
    )
    powershell -Command "(Get-Content '%CLAUDE_DIR%\mcp.json' -Raw) -replace '%%USERPROFILE%%', '%HOME_PATH%' | Set-Content '%CLAUDE_DIR%\mcp.json' -Encoding UTF8"
    echo   mcp.json — 已生成
)

REM --- 生成 .mcp.json ---
if exist "%TEMP_DIR%\.mcp.template.json" (
    copy "%TEMP_DIR%\.mcp.template.json" "%CLAUDE_DIR%\.mcp.json" /Y >nul
    if not "%API_KEY%"=="" (
        powershell -Command "(Get-Content '%CLAUDE_DIR%\.mcp.json' -Raw) -replace '{{DEEPSEEK_API_KEY}}', '%API_KEY%' | Set-Content '%CLAUDE_DIR%\.mcp.json' -Encoding UTF8"
    )
    echo   .mcp.json — 已生成
)

REM --- 生成 CLAUDE.md ---
if exist "%TEMP_DIR%\CLAUDE.md.template" (
    copy "%TEMP_DIR%\CLAUDE.md.template" "%CLAUDE_DIR%\CLAUDE.md" /Y >nul
    powershell -Command "(Get-Content '%CLAUDE_DIR%\CLAUDE.md' -Raw) -replace '{{USER_HOME}}', '%HOME_PATH%' | Set-Content '%CLAUDE_DIR%\CLAUDE.md' -Encoding UTF8"
    echo   CLAUDE.md — 已生成
)

echo.

REM ==========================================
REM 步骤 6：复制其他所有文件
REM ==========================================
echo [6/6] 复制其余配置...
REM 复制除了模板对应的实际文件之外的所有内容
xcopy "%TEMP_DIR%\*" "%CLAUDE_DIR%\" /E /Y /Q /EXCLUDE:"%TEMP_DIR%\.gitignore-exclude" 2>nul
REM 如果上面的排除失败了，直接覆盖（反正 settings 等已经生成了）
xcopy "%TEMP_DIR%\projects" "%CLAUDE_DIR%\projects\" /E /Y /Q 2>nul
xcopy "%TEMP_DIR%\skills" "%CLAUDE_DIR%\skills\" /E /Y /Q 2>nul
xcopy "%TEMP_DIR%\plugins" "%CLAUDE_DIR%\plugins\" /E /Y /Q 2>nul

REM 复制根目录文件（.gitignore, CREDENTIALS.md, start-*.cmd 等）
for %%f in ("%TEMP_DIR%\*.*") do (
    copy "%%f" "%CLAUDE_DIR%\" /Y >nul 2>nul
)

echo 复制完成
echo.

REM ==========================================
REM 清理
REM ==========================================
rmdir /S /Q "%TEMP_DIR%"

echo ============================================
echo   配置下载完成！
echo ============================================
echo.
echo 下一步：
echo   1. 打开新的终端，输入 claude 启动
echo   2. 飞书登录：lark-cli auth login
echo   3. Qwen Vision：如需使用，复制 qwen-vision-mcp 目录到家
echo.
echo 如果遇到问题，你的旧配置备份在：
echo   %BACKUP_DIR%
echo.
pause
