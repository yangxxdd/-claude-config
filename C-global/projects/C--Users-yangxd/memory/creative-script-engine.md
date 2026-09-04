---
name: creative-script-engine
description: 素材脚本创意引擎——每次写素材脚本必须遵循的强制 SOP
metadata: 
  node_type: memory
  type: project
  originSessionId: 87ac973d-a7e4-4d73-8af2-7707de1dac24
---

用户是投放，周期性为幻宠（宝可梦题材）和 GTS（黑帮题材）写素材脚本。

## 强制流程（每次必循，不可跳过）
1. **Step 0**: 定位游戏 → 读 asset_index.json 确认物料&资产（角色/场景/UI）。成品素材只看不引用。
2. **Step 1**: 找参考（强制！只找外部竞品）→ WebSearch 搜索竞品广告 + 跨品类参考。**不拿自己成品当参考**，除非用户明确说"在之前基础上延伸"。
3. **Step 2**: 创意提案（2-3 方案，轻量确认）→ 含 AI/AE/UE 分工 + 原因 + 参考来源
4. **Step 3**: 用户确认后 → 生成完整分镜 Excel 表（每个镜头配资产路径 + 制作方式 + 原因）
5. **Step 4**: 质量自检（Hook 公式/冲突/资产引用/时长/CTA）

## AI/AE/UE 决策框架
- **AI 生成**: 游戏里不存在的新角色/融合体/概念图；视频前贴吸睛画面；剧情插画。不可用于连续动画或 UI。
- **AE 合成**: 现有图层素材组合+动效；UI 弹窗/数值/转场；竞品复刻（替换素材+改尾贴）；2D 特效。不可用于 3D 场景。
- **UE 渲染**: 3D 场景+摄像机漫游；角色 3D 动画；需要高质量实时光影。仅在必须用 3D 时使用。
- **优先级**: AE+AI 优先 → UE 仅在必须 3D 时 → 必须标注原因

## 钩子公式（行业验证）
- 震惊虐待：对可爱生物施加暴力/危机 → Palmon Survival 式
- 反差打脸：被嘲笑→反转证明强大
- 禁忌悬念：警告/禁忌→好奇心驱动
- 竞技压迫：多人淘汰/生死局
- 沙雕搞笑：拟人化卖萌/意外事故

## 资产库
- GTS: `Y:\市场运营部\友蜜\黑帮题材`
- 幻宠: `Y:\市场运营部\友蜜\幻想宠物`
- 索引: `C:\Users\yangxd\.claude\projects\C--Users-yangxd\asset_index.json`
- 引擎文档: `C:\Users\yangxd\.claude\projects\C--Users-yangxd\素材脚本创意引擎.md`
