---
name: office-tool-selection-rules
description: OfficeCLI vs 现有 docx/xlsx/pdf skill 的选择规则，确保功能重叠时自动选对工具
metadata: 
  node_type: memory
  type: project
  originSessionId: 04e7f9cf-a459-4d10-85ef-59f8ac9f99de
---

# Office 工具选择决策规则

存在功能重叠时，按以下优先级自动选择。**禁止在有重叠的场景下随机选或两个都试。**

## 一、按文件格式第一层路由

| 文件格式 | 使用工具 | 原因 |
|---------|---------|------|
| `.pptx` / PowerPoint | **OfficeCLI MCP** (`mcp__officecli_*`) | 唯一选择，无替代 |
| `.pdf` | **pdf skill** | OfficeCLI 不处理 PDF，无冲突 |
| `.docx` / Word | 见第二节 | 有重叠 |
| `.xlsx` / `.xlsm` | 见第三节 | 有重叠 |
| `.csv` / `.tsv` | **xlsx skill** 为主 | OfficeCLI 对 CSV 支持有限 |
| 飞书文档/知识库 URL | **lark-doc / lark-wiki** | 不同生态，无冲突 |
| 企业微信文档/表格 URL | **wecomcli-doc / wecomcli-smartsheet** | 不同生态，无冲突 |

## 二、.docx 任务决策树

```
是模板合并（{{key}} 批量填充）？
  → Yes: OfficeCLI（merge 命令，现有 skill 做不到）
  → No: 继续

需要可视化预览（AI 要"看到"渲染效果）？
  → Yes: OfficeCLI（内置 HTML 渲染引擎，view html/screenshot/watch）
  → No: 继续

涉及公式/水印/表单域/OLE/脚注/内容控件/复杂域？
  → Yes: OfficeCLI（这些元素现有 skill 不支持或支持很差）
  → No: 继续

是 Markdown → docx 转换？
  → Yes: docx skill（现有成熟流程）
  → No: 继续

是查看/编辑修订跟踪（Track Changes）？
  → Yes: docx skill（对此场景更成熟）
  → No: 继续

简单读写/格式调整？
  → 优先 OfficeCLI（路径式操作更精确），docx skill 备用
```

## 三、.xlsx/.xlsm 任务决策树

```
需要数据透视表？
  → Yes: OfficeCLI（一条命令生成，含切片器/日期分组/计算字段）
  → No: 继续

需要公式自动求值（写 =SUM() 立刻看到结果）？
  → Yes: OfficeCLI（350+ 函数内置求值引擎）
  → No: 继续

需要高级图表（帕累托图/箱线图/迷你图/对数轴）？
  → Yes: OfficeCLI
  → No: 继续

是数据清洗（畸形行/错位表头/脏数据）？
  → Yes: xlsx skill（数据处理能力更强）
  → No: 继续

是 CSV/TSV 导入导出/格式转换？
  → Yes: xlsx skill（对此场景更成熟）
  → No: 继续

需要条件格式/数据验证/自动筛选？
  → Yes: OfficeCLI（更全面）
  → No: 继续

简单单元格读写/基础图表/格式调整？
  → 优先 OfficeCLI，xlsx skill 备用
```

## 四、强制规则

1. **不要两个都调**：如果功能重叠，按规则选一个，不要"先用 A 试试不行再用 B"。除非第一个确实报错/不支持。
2. **不要中途切换**：如果已经用某个工具开始处理一个文件，继续用同一个工具完成，不要混用。
3. **pdf/wecomcli/lark 永远不受影响**：这些生态和 OfficeCLI 零重叠，该用啥用啥。
4. **新任务默认优先 OfficeCLI**：对于 docx/xlsx/pptx 本地文件操作，OfficeCLI 是更现代、更 AI-native 的选择。只在上述明确标注 xlsx/docx skill 更强的场景用旧 skill。

**Why:** 用户安装了 OfficeCLI 后，docx/xlsx/pptx 都有了更强的工具，但也保留了旧 skill。需要明确规则防止选择混乱。
**How to apply:** 每次处理 Office 文件前，先查此表。遇到不在表中的场景，优先 OfficeCLI。
