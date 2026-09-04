$ErrorActionPreference = "Stop"

Write-Host "============================================"  -ForegroundColor Cyan
Write-Host "  Claude Code - Sync to GitHub" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# ============================================
# Config
# ============================================
$RepoUrl  = "https://github.com/yangxxdd/-claude-config.git"
$CDrive   = "$env:USERPROFILE\.claude"
$DDrive   = "D:\claude-projects"
$TempDir  = "$env:TEMP\claude-sync-" + (Get-Date -Format "HHmmss")
$Username = $env:USERNAME

# ============================================
# 1. Prepare temp staging area
# ============================================
Write-Host "[1/5] Preparing staging area..." -ForegroundColor Yellow
if (Test-Path $TempDir) { Remove-Item -Recurse -Force $TempDir }
New-Item -ItemType Directory -Path "$TempDir\C-global" -Force | Out-Null
New-Item -ItemType Directory -Path "$TempDir\D-shared" -Force | Out-Null
New-Item -ItemType Directory -Path "$TempDir\D-config" -Force | Out-Null
New-Item -ItemType Directory -Path "$TempDir\D-projects" -Force | Out-Null
Write-Host "  Done"
Write-Host ""

# ============================================
# 2. Stage C: drive global config
# ============================================
Write-Host "[2/5] Staging C: drive global config..." -ForegroundColor Yellow

# Copy root files (excluding sensitive ones)
$cFileExclude = @('settings.json','settings.local.json','settings-deepseek.json','mcp.json','.mcp.json','.credentials.json','CLAUDE.md','history.jsonl','bridge.log')
Get-ChildItem "$CDrive\*" -File -ErrorAction SilentlyContinue | ForEach-Object {
    if ($_.Name -notin $cFileExclude -and $_.Name -notmatch '\.bak$') {
        $dest = "$TempDir\C-global\$($_.Name)"
        Copy-Item $_.FullName $dest -Force
    }
}

# Copy subdirectories (excluding gitignored ones)
$cExclude = @('telemetry','temp','cache','file-history','shell-snapshots','backups','paste-cache','downloads','sessions','session-env','tasks','skills','plugins','skills.bak','plugins.bak','chrome-profile','playwright-profile','venv','.venv','node_modules','__pycache__')
Get-ChildItem "$CDrive\*" -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    if ($_.Name -notin $cExclude) {
        $dest = "$TempDir\C-global\$($_.Name)"
        Copy-Item $_.FullName $dest -Recurse -Force -ErrorAction SilentlyContinue
    }
}

# Generate CLAUDE.md template (replace C:/Users/<user> with placeholder)
$claudeMdPath = "$CDrive\CLAUDE.md"
if (Test-Path $claudeMdPath) {
    $content = Get-Content $claudeMdPath -Raw -Encoding UTF8
    $content = $content -replace [regex]::Escape("C:/Users/$Username"), "{{USER_HOME}}"
    Set-Content "$TempDir\C-global\CLAUDE.md.template" -Value $content -Encoding UTF8
}

# Strip session transcripts (contain API keys) and temp data
Write-Host "  Stripping session data..."
Get-ChildItem "$TempDir\C-global" -Recurse -Filter "*.jsonl" -File -ErrorAction SilentlyContinue | Remove-Item -Force
Get-ChildItem "$TempDir\C-global" -Recurse -Directory -Filter "tool-results" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
Get-ChildItem "$TempDir\C-global" -Recurse -Directory -Filter "subagents" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
Get-ChildItem "$TempDir\C-global" -Recurse -Directory -Filter "session-env" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force

Write-Host "  Done ($((Get-ChildItem $TempDir\C-global -Recurse).Count) items)"
Write-Host ""

# ============================================
# 3. Stage D: drive shared (skills + plugins)
# ============================================
Write-Host "[3/5] Staging D: drive shared (skills + plugins)..." -ForegroundColor Yellow

if (Test-Path "$DDrive\shared\skills") {
    Copy-Item "$DDrive\shared\skills" "$TempDir\D-shared\skills" -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "  skills: $((Get-ChildItem "$TempDir\D-shared\skills" -Directory).Count) items"
}
if (Test-Path "$DDrive\shared\plugins") {
    Copy-Item "$DDrive\shared\plugins" "$TempDir\D-shared\plugins" -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "  plugins: $((Get-ChildItem "$TempDir\D-shared\plugins" -Directory).Count) items"
}
Write-Host ""

# ============================================
# 4. Stage D: drive config + projects
# ============================================
Write-Host "[4/5] Staging D: drive config + projects..." -ForegroundColor Yellow

# D-config (exclude skills/plugins junctions)
$dConfigExclude = @('skills','plugins','skills.bak','plugins.bak','telemetry','temp','cache','sessions','tasks','file-history','shell-snapshots','backups','downloads','session-env','paste-cache','chrome-profile','playwright-profile','venv','.venv','node_modules','__pycache__')
if (Test-Path "$DDrive\claude-config") {
    Get-ChildItem "$DDrive\claude-config\*" -ErrorAction SilentlyContinue | ForEach-Object {
        if ($_.Name -notin $dConfigExclude -and $_.Name -notmatch '\.bak') {
            $dest = "$TempDir\D-config\$($_.Name)"
            if ($_.PSIsContainer) {
                Copy-Item $_.FullName $dest -Recurse -Force -ErrorAction SilentlyContinue
            } else {
                Copy-Item $_.FullName $dest -Force
            }
        }
    }
}

# Generate D-config CLAUDE.md template
$dClaudeMdPath = "$DDrive\claude-config\CLAUDE.md"
if (Test-Path $dClaudeMdPath) {
    $content = Get-Content $dClaudeMdPath -Raw -Encoding UTF8
    $content = $content -replace [regex]::Escape("C:/Users/$Username"), "{{USER_HOME}}"
    $content = $content -replace [regex]::Escape("D:\claude-projects"), "{{D_DRIVE}}"
    Set-Content "$TempDir\D-config\CLAUDE.md.template" -Value $content -Encoding UTF8
}

# Sanitize D-config settings files (replace API keys)
$ApiKeyPattern = 'sk-[a-zA-Z0-9]{20,}'
@("settings.json","mcp.json",".mcp.json") | ForEach-Object {
    $file = "$TempDir\D-config\$_"
    if (Test-Path $file) {
        $content = Get-Content $file -Raw -Encoding UTF8
        $content = $content -replace $ApiKeyPattern, "{{DEEPSEEK_API_KEY}}"
        Set-Content $file -Value $content -Encoding UTF8
    }
}

Write-Host "  D-config: $((Get-ChildItem $TempDir\D-config -Recurse).Count) items"

# D-projects (GTS, 幻宠, 日常)
if (Test-Path "$DDrive\projects") {
    Copy-Item "$DDrive\projects\*" "$TempDir\D-projects\" -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "  D-projects: $((Get-ChildItem $TempDir\D-projects -Directory).Count) projects"
}

# Root files (CLAUDE.md, start-*.bat, upload scripts)
Get-ChildItem "$DDrive\*" -File -ErrorAction SilentlyContinue | ForEach-Object {
    Copy-Item $_.FullName "$TempDir\" -Force
}
Write-Host "  Root files copied"

Write-Host ""

# ============================================
# 4.5. Global cleanup — strip ALL session data
# ============================================
Write-Host "[Clean] Removing session transcripts (contain API keys)..." -ForegroundColor Yellow
$allJsonl = Get-ChildItem "$TempDir" -Recurse -Filter "*.jsonl" -File -ErrorAction SilentlyContinue
$allJsonl | Remove-Item -Force
Write-Host "  Removed $($allJsonl.Count) .jsonl files"

$cleanDirs = @('tool-results','subagents','session-env','sessions','tasks','telemetry','temp','cache','downloads','paste-cache','shell-snapshots','file-history','backups','session-env','playwright-mcp')
foreach ($dir in $cleanDirs) {
    $items = Get-ChildItem "$TempDir" -Recurse -Directory -Filter $dir -ErrorAction SilentlyContinue
    foreach ($item in $items) { Remove-Item $item.FullName -Recurse -Force -ErrorAction SilentlyContinue }
}
Write-Host "  Cleaned session data directories"

# 删除超过 50MB 的大文件（GitHub 单文件硬限制 100MB；素材视频/大 PPT 不入 Git，源文件仍在 D 盘）
$bigFiles = Get-ChildItem "$TempDir" -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.Length -gt 50MB }
foreach ($f in $bigFiles) {
    Write-Host "  跳过 $( [math]::Round($f.Length/1MB,1) )MB 大文件: $($f.Name)"
    Remove-Item $f.FullName -Force -ErrorAction SilentlyContinue
}
Write-Host ""

# ============================================
# 5. Commit and push
# ============================================
Write-Host "[5/5] Pushing to GitHub..." -ForegroundColor Yellow

Set-Location $TempDir

# git 是外部命令，其 stderr 的换行符 warning 在 PowerShell 5.1 + ErrorActionPreference=Stop 下
# 会被误判为 NativeCommandError 导致脚本中断，这里临时放宽为 Continue
$ErrorActionPreference = "Continue"

# Init git if needed
if (-not (Test-Path ".git")) {
    git init
    git remote add origin $RepoUrl
}

git add -A
git commit -m "Sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm')" --allow-empty

$output = & git push -u origin master --force 2>&1 | Out-String
if ($LASTEXITCODE -eq 0) {
    Write-Host "  Push succeeded!" -ForegroundColor Green
} else {
    # Check if it actually worked (git sometimes outputs to stderr)
    if ($output -match "master -> master") {
        Write-Host "  Push succeeded!" -ForegroundColor Green
    } else {
        Write-Host "  Push may have failed. Output:" -ForegroundColor Red
        Write-Host $output
    }
}

# Cleanup
Set-Location $CDrive
Remove-Item -Recurse -Force $TempDir -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "Done! Press Enter to close." -ForegroundColor Green
Read-Host
