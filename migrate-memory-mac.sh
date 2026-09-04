#!/bin/bash
# 记忆迁移脚本（Mac 版）
# 把 GitHub 仓库里按 Windows 路径存的记忆，搬到 Mac 的正确位置。
# 用法：bash migrate-memory-mac.sh
set -e

TMP="/tmp/cc-migrate"
U=$(whoami)

echo "=== 迁移项目记忆文件 ==="

# 克隆仓库（公开，无需 token）
rm -rf "$TMP"
git clone https://github.com/yangxxdd/-claude-config.git "$TMP" >/dev/null 2>&1

# 路径转义对照：
#   Windows: D:\claude-projects\projects\GTS  -> D--claude-projects-projects-GTS
#   Mac:     /Users/$U/claude-projects/projects/GTS -> -Users-$U-claude-projects-projects-GTS
PREFIX="-Users-$U-claude-projects-projects"
PROJ_BASE="$HOME/claude-projects/claude-config/projects"

# ---- GTS 记忆 ----
GTS_SRC="$TMP/D-config/projects/D--claude-projects-projects-GTS/memory"
if [ -d "$GTS_SRC" ]; then
  GTS_DST="$PROJ_BASE/${PREFIX}-GTS/memory"
  mkdir -p "$GTS_DST"
  cp "$GTS_SRC"/*.md "$GTS_DST/"
  echo "① GTS 记忆：$(ls "$GTS_DST" | wc -l | tr -d ' ') 个 -> $GTS_DST"
fi

# ---- 幻宠记忆（中文"幻宠"在 Claude 转义规则下会变成 ---，与 Windows 一致）----
HUAN_SRC="$TMP/D-config/projects/D--claude-projects-projects---/memory"
if [ -d "$HUAN_SRC" ]; then
  HUAN_DST="$PROJ_BASE/${PREFIX}---/memory"
  mkdir -p "$HUAN_DST"
  cp "$HUAN_SRC"/*.md "$HUAN_DST/"
  echo "② 幻宠记忆：$(ls "$HUAN_DST" | wc -l | tr -d ' ') 个 -> $HUAN_DST"
fi

# ---- 兜底：把 C-global 里 cwd=D:\claude-projects 产生的幻宠记忆也并进去 ----
EXTRA_SRC="$TMP/C-global/projects/D--claude-projects/memory"
if [ -d "$EXTRA_SRC" ]; then
  EXTRA_DST="$PROJ_BASE/${PREFIX}---/memory"
  mkdir -p "$EXTRA_DST"
  cp "$EXTRA_SRC"/*.md "$EXTRA_DST/" 2>/dev/null || true
  echo "③ 补充幻宠记忆（来自 C 盘全局）已并入 $EXTRA_DST"
fi

rm -rf "$TMP"

echo ""
echo "=== 迁移完成 ==="
echo "注意：Claude Code 按'启动时的当前目录'读记忆。"
echo "只有用 start-GTS.command / start-幻宠.command 启动，才会读到对应记忆。"
echo ""
echo "⚠️ 核对方法：启动某项目后，若记忆没加载，运行："
echo "   ls ~/claude-projects/claude-config/projects/"
echo "   看实际生成的目录名是否与本脚本假设一致（中文名可能转义不同），"
echo "   不一致就把对应 memory 目录整体改名即可。"
