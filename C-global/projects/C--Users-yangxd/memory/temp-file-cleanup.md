---
name: temp-file-cleanup
description: 每次分析产生的临时截图、抽帧、中间文件必须删除，只保留用户需要的最终参考
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87ac973d-a7e4-4d73-8af2-7707de1dac24
---

## 规则
- 视频抽帧 → 分析完后删除所有临时帧
- Playwright 截图 → 分析完后删除，只保留用户明确需要的参考
- 任何中间产物（临时 JSON、meta 文件等）→ 用完即删
- **保留的**：用户确认的参考素材链接/文件、最终脚本产出

**Why:** 用户之前积累了大量无用的中间截图和分析文件，占用空间且混乱。
**How to apply:** 每次分析流程结束时，执行清理脚本删除临时目录和文件。在分析报告中只保留结论，不保留中间产物。
