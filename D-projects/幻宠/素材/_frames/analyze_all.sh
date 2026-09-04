#!/bin/bash
FRAMES_DIR="D:/claude-projects/projects/幻宠/素材/_frames"
PYTHON="C:/Users/yangxd/qwen-vision-mcp/analyze.py"
QUESTION="请详细描述这个视频截图：画面内容、风格、文字/UI、传达的信息。请用中文回答，控制在200字以内。"

FILES=(
  "V-帕萌战斗-出狱打鸡"
  "V-帕萌战斗-合成狙击"
  "V-帕萌战斗-群殴打鸡"
  "V-帕萌战斗-杀宠复刻"
  "V-帕萌战斗-雪地竞品"
  "V-天灾重建-长版"
  "V-抓宠经营-捕捞竞品"
  "V-抓宠经营-狐狸"
  "V-抓宠经营-虐待"
  "V-抓宠经营-售卖帕基"
  "V-抓宠经营-拯救可达鸭"
  "V-抓宠战斗"
)

for name in "${FILES[@]}"; do
  for pct in 20 50 80; do
    frame="${FRAMES_DIR}/${name}_${pct}.jpg"
    echo "=== ANALYZING: ${name}_${pct}.jpg ==="
    python "$PYTHON" "$frame" "$QUESTION" 2>&1
    echo "=== END ${name}_${pct}.jpg ==="
    echo ""
  done
done
