$ErrorActionPreference = "Stop"
Set-Location "$env:USERPROFILE\.claude"

Write-Host "============================================"
Write-Host "  Claude Code - Upload to GitHub"
Write-Host "============================================"
Write-Host ""

# 1. Init git if needed
if (-not (Test-Path ".git")) {
    Write-Host "[1/4] Init git repo..."
    git init
} else {
    Write-Host "[1/4] Git repo ready"
}
Write-Host ""

# 2. Update CLAUDE.md template
Write-Host "[2/4] Updating CLAUDE.md template..."
if (Test-Path "CLAUDE.md") {
    $content = Get-Content "CLAUDE.md" -Raw -Encoding UTF8
    $content = $content -replace [regex]::Escape("C:/Users/yangxd"), "{{USER_HOME}}"
    Set-Content "CLAUDE.md.template" -Value $content -Encoding UTF8
    Write-Host "  Done"
}
Write-Host ""

# 3. Commit
Write-Host "[3/4] Committing..."
git add -A
git commit -m "Update: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
Write-Host "  Done"
Write-Host ""

# 4. Push
Write-Host "[4/4] Pushing to GitHub..."
$output = & git push origin master 2>&1 | Out-String
if ($LASTEXITCODE -eq 0) {
    Write-Host "Push succeeded!"
} else {
    Write-Host $output
    Write-Host "Push may have failed. Check output above."
    Write-Host ""
    Write-Host "If authentication failed, generate new token:"
    Write-Host "  https://github.com/settings/tokens"
}
Write-Host ""
Write-Host "Done! Press Enter to close."
Read-Host
