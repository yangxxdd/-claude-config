#!/bin/bash
# Claude Code 配置部署脚本（Mac 版）—— 对应 Windows 桌面的 download.ps1
# 用法：在 Mac 终端运行  bash deploy-mac.sh
set -e

REPO_URL="https://github.com/yangxxdd/-claude-config.git"
CDRIVE="$HOME/.claude"
DDIR="$HOME/claude-projects"
TMP="/tmp/claude-sync-download"

echo "============================================"
echo "  Claude Code - Deploy from GitHub (Mac)"
echo "============================================"

# 0. 检查 git
if ! command -v git >/dev/null 2>&1; then
  echo "[错误] 未安装 git。请先安装：xcode-select --install"
  exit 1
fi
echo "[Check] git: OK"

# 1. 备份现有配置
BACKUP="$HOME/.claude-backup-$(date +%Y%m%d-%H%M%S)"
if [ -d "$CDRIVE" ]; then cp -R "$CDRIVE" "$BACKUP"; echo "[备份] $BACKUP"; fi

# 2. 克隆
rm -rf "$TMP"
git clone "$REPO_URL" "$TMP"
echo "[Clone] done"

# 3. 输入 API Key
read -p "DeepSeek API Key (sk- 开头，回车跳过): " APIKEY
echo ""

# 4. 部署全局配置
mkdir -p "$CDRIVE"
cp -R "$TMP/C-global/." "$CDRIVE/"
echo "[部署] 全局配置 -> $CDRIVE"

# 4.5 迁移全局记忆（主配置，路径确定）
U=$(whoami)
GLOBAL_MEM="$CDRIVE/projects/-Users-$U/memory"
mkdir -p "$GLOBAL_MEM"
if [ -d "$TMP/C-global/projects/C--Users-yangxd/memory" ]; then
  cp "$TMP"/C-global/projects/C--Users-yangxd/memory/*.md "$GLOBAL_MEM/"
  echo "[记忆] 全局记忆 $(ls "$GLOBAL_MEM" | wc -l | tr -d ' ') 个 -> $GLOBAL_MEM"
fi

# 5. 部署项目目录（D 盘等价）
mkdir -p "$DDIR/shared" "$DDIR/claude-config" "$DDIR/projects"
[ -d "$TMP/D-shared/skills" ]  && cp -R "$TMP/D-shared/skills"  "$DDIR/shared/skills"
[ -d "$TMP/D-shared/plugins" ] && cp -R "$TMP/D-shared/plugins" "$DDIR/shared/plugins"
cp -R "$TMP/D-config/." "$DDIR/claude-config/"
for d in "$TMP"/D-projects/*/; do
  name=$(basename "$d")
  cp -R "$d" "$DDIR/projects/$name"
done
for f in "$TMP"/*; do
  [ -f "$f" ] || continue
  base=$(basename "$f")
  case "$base" in
    start-*|upload*|download*|sync-model*|CLAUDE*) cp "$f" "$DDIR/" ;;
  esac
done
echo "[部署] 项目目录 -> $DDIR"

# 6. 建软链（替代 Windows junction）
ln -sfn "$DDIR/shared/skills"   "$CDRIVE/skills"
ln -sfn "$DDIR/shared/plugins"  "$CDRIVE/plugins"
ln -sfn "$DDIR/shared/skills"   "$DDIR/claude-config/skills"
ln -sfn "$DDIR/shared/plugins"  "$DDIR/claude-config/plugins"
echo "[软链] skills/plugins 已链接到 shared"

# 7. 展开模板生成真实配置
expand() {
  [ -f "$1" ] || return
  sed -e "s|{{DEEPSEEK_API_KEY}}|$APIKEY|g" \
      -e "s|{{USER_HOME}}|$HOME|g" \
      -e "s|%USERPROFILE%|$HOME|g" \
      -e "s|{{D_DRIVE}}|$DDIR|g" \
      "$1" > "$2"
  echo "  生成 $(basename "$2")"
}

expand "$CDRIVE/CLAUDE.md.template"                  "$CDRIVE/CLAUDE.md"
expand "$TMP/C-global/settings.template.json"        "$CDRIVE/settings.json"
expand "$TMP/C-global/mcp.template.json"             "$CDRIVE/mcp.json"
expand "$TMP/C-global/.mcp.template.json"            "$CDRIVE/.mcp.json"
[ -f "$TMP/D-config/settings.json" ]      && expand "$TMP/D-config/settings.json"      "$DDIR/claude-config/settings.json"
[ -f "$TMP/D-config/mcp.json" ]           && expand "$TMP/D-config/mcp.json"           "$DDIR/claude-config/mcp.json"
[ -f "$TMP/D-config/.mcp.json" ]          && expand "$TMP/D-config/.mcp.json"          "$DDIR/claude-config/.mcp.json"
[ -f "$TMP/D-config/CLAUDE.md.template" ] && expand "$TMP/D-config/CLAUDE.md.template" "$DDIR/claude-config/CLAUDE.md"

# 8. 启动脚本赋可执行权限
chmod +x "$DDIR"/start-*.command 2>/dev/null || true

# 9. 跳过首次登录向导（走 DeepSeek 接口，无需 Anthropic 登录）
printf '{"hasCompletedOnboarding": true}' > "$HOME/.claude.json"

rm -rf "$TMP"
echo ""
echo "============================================"
echo "  部署完成！"
echo "============================================"
echo "  全局配置 -> $CDRIVE"
echo "  项目配置 -> $DDIR"
echo "  启动项目：双击 ~/claude-projects/start-GTS.command 等"
