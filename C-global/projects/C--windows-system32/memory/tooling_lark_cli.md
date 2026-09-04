---
name: lark-cli 工具避坑指南
description: lark-cli v1.0.26 的正确用法、常见错误和workaround，尤其是docs +update/+create的markdown支持
type: reference
originSessionId: a16f26ab-7427-49f0-bcdd-93494eadf471
---
## 版本：1.0.36（2026/05/21 升级），原 1.0.26→1.0.36 一次成功

## 文档创建
```bash
# 正确（必须 --doc-format markdown，不是 --markdown=true）
lark-cli docs +create --api-version v2 --title "标题" --doc-format markdown --content "@file.md"

# 错误 → 空白文档
lark-cli docs +create --api-version v2 --title "标题" --markdown=true --content "@file.md"
```

## 文档更新
```bash
# 正确
lark-cli docs +update --api-version v2 --doc "<url>" --command overwrite --doc-format markdown --content "@file.md"

# 错误 → 空白文档
lark-cli docs +update --api-version v2 --doc "<url>" --command overwrite --mode markdown --content "@file.md"

# 错误 → --command is required
lark-cli docs +update --api-version v2 --doc "<url>" --mode overwrite --doc-format markdown --content "@file.md"
```

## Sheet读取（不需要--api-version）
```bash
lark-cli sheets +read --spreadsheet-token "<token>" --sheet-id "<id>" --value-render-option "FormattedValue"
```
- 不加 `--value-render-option "FormattedValue"` 会返回公式（如 D3/E3）而非实际值

## 文档局部读取
```bash
# 按标题读取
lark-cli docs +fetch --api-version v2 --doc "<url>" --scope section --start-block-id "<block_id>"

# doc-format markdown 导出
lark-cli docs +fetch --api-version v2 --doc "<url>" --scope full --doc-format markdown
```

**Why:** lark-cli 1.0.26 的 markdown 转换有严重bug——错误flag会导致文档内容全部丢失变成空白。原文档可通过飞书web版本历史恢复。

**How to apply:** 操作飞书文档时严格使用 `--doc-format markdown` + `--command overwrite` 组合，不要用 `--markdown=true` 或 `--mode` flag。每次操作前先确保文档已备份或可恢复。

## 1.0.36 注意事项
- **`docs +search` 迁移到 `drive +search`**：原命令不再可用，需改脚本
- **overwrite 会先警告**（含 whiteboard/file block 的文档）：降低误覆盖风险
- **新 `markdown` 域**：`markdown +create/+diff/+patch`，可探索替代部分 docs markdown 流程
- **推荐 `lark-cli update` 而非 `npm install -g`** 做后续升级
