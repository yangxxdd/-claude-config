---
name: guangdada-playwright
description: 广大大平台 Playwright 操作注意事项——两个搜索框的区别
metadata: 
  node_type: memory
  type: reference
  originSessionId: 87ac973d-a7e4-4d73-8af2-7707de1dac24
---

## 广大大有两个搜索框

1. **顶部搜索框**（header）：placeholder "搜索 创意 广告主 关键词" → 跳转到"全局搜索"页面。**这个不能用！** 搜出来的不是广告素材，是全局索引。
2. **页面中间的素材筛选区**：placeholder "搜索广告主、文案、包名等关键词" → 这才是**展示广告素材筛选**的正确搜索框。旁边有"综合"下拉、"Top创意"按钮、游戏分类等筛选条件。

**每次在广大大搜索素材，必须用第 2 个搜索框（素材筛选区），不能用顶部那个。**

## 其他操作要点
- Playwright 已配置持久化 Chrome Profile：`C:/Users/yangxd/.claude/chrome-profile`
- 登录态已保存，不需要重新登录
- 搜索结果页面可能很大（100K+ 字符），截图比读 snapshot 更有效
- DeepSeek 模型看不到截图，搜索结果需要用户肉眼筛选后把链接发给我
