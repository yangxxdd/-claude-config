# 素材脚本引擎 — 交接文档

## 你现在要做什么

用户是投放，需要为下次测试准备素材脚本。**三个需求待完成：**

1. **宝可梦融合素材 ×3** — 新融合方式，强化融合表现力。Step 2 提案已出（3个方案），等用户选方向进 Step 3。
2. **抓宠玩法素材 ×20** — 20 种不同的抓宠工具/物理手段（精灵球、弹弓、套索、捕网等），不是叙事套路。
3. **魔法+宠物融合 ×1** — AI 向素材。

## 引擎 SOP（必须按这个走）

完整引擎：`C:\Users\yangxd\.claude\projects\C--Users-yangxd\素材脚本创意引擎.md`

```
Step 0: 定位游戏 → 读 asset_index.json
Step 1: 找参考（外部竞品，不拿自己成品当参考）
  1d: 参考适配分析（B级改编四问）
Step 2: 创意提案（2-3 方案，含 AI/AE/UE 分工+原因+参考来源）
Step 3: 用户确认 → 完整分镜Excel（每镜配资产路径+制作方式+原因）
Step 4: 质量自检
```

## 资产库

- 幻宠：`Y:\市场运营部\友蜜\幻想宠物`（需要先挂载 `Y:` 到 `\\192.168.0.172\部门文件`）
- GTS：`Y:\市场运营部\友蜜\黑帮题材`
- 索引：`C:\Users\yangxd\.claude\projects\C--Users-yangxd\asset_index.json`

挂载 NAS 的命令（如果 Y: 没挂）：
```powershell
$enc = [System.Text.Encoding]::GetEncoding('gb2312')
$bytes = [byte[]]@(0xb2, 0xbf, 0xc3, 0xc5, 0xce, 0xc4, 0xbc, 0xfe)
$shareName = $enc.GetString($bytes)
net use Y: "\\192.168.0.172\$shareName"
```

## 宝可梦融合 3 个方案（Step 2 已出）

详见上一轮对话的提案。三个方案概要：

| 方案 | 钩子 | 核心 | AI用量 |
|------|------|------|--------|
| 1 天崩开局 | 反差打脸 | 融合失败被嘲笑→废料逆袭成神宠 | 3图 |
| 2 肢解车间 | 工业恐怖 | 暗黑车间解剖重组→极致美感融合体 | 2图 |
| 3 反向驯服 | 身份反转 | 宠物反向融合训练师→人宠合一 | 1图 |

等待用户确认方案方向，然后进 Step 3 出完整分镜 Excel。

## 行业调研（已完成的参考知识）

- **Palmon Survival 公式**：虐待钩子→恢复进化→战力展示。4线投放：震惊/救援/生产率/AAA战斗
- **Merge 赛道 5 段结构**：抓眼开头→展示冲突→解决方案→节奏推进→CTA
- **2 秒法则**：前 2 秒必须有极端设定阻止滑动
- **钩子公式**：震惊虐待 / 反差打脸 / 禁忌悬念 / 竞技压迫 / 沙雕搞笑

## AI/AE/UE 决策框架

- **AI**：新角色/融合体/概念图、前贴吸睛画面、剧情插画。不可做连续动画或 UI。
- **AE**：现有素材组合+动效、UI/数值/转场、竞品复刻（换素材+改尾贴）、2D特效。不可做 3D 场景。
- **UE**：3D 场景+摄像机、角色 3D 动画。仅在必须用 3D 时使用。优先级最低。

## 记忆文件

- 引擎 SOP：`C:\Users\yangxd\.claude\projects\C--Users-yangxd\memory\creative-script-engine.md`
- 广大大操作注意：`C:\Users\yangxd\.claude\projects\C--Users-yangxd\memory\guangdada-playwright.md`
- 临时文件清理：`C:\Users\yangxd\.claude\projects\C--Users-yangxd\memory\temp-file-cleanup.md`

## 用户偏好

- 先提案再脚本，不要一步出完整脚本
- 每个镜头必须标资产引用或"需新做"
- AI/AE/UE 每个决策必须有原因，不是拍脑袋
- 时长必须符合实际制作能力
- 不要拿用户自己的成品素材当创意参考
- 临时文件（截图/抽帧/中间产物）分析完必须删除
