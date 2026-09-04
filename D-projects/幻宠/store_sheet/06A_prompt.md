# 06-A 提示词（犯罪地图全美扩张·芝加哥事件密度）

## 方向定位
- P1 定向 | 中文：从一个街区，到统一全美 | 英文：FROM ONE BLOCK TO ALL AMERICA.
- 制作人意图：双重叙事=微观(城市犯罪实时分布)+宏观(全国势力扩张)；地图绑定事件/攻城/路线/占领结果
- 场景：前景放大芝加哥犯罪地图，火并/抢劫/招募事件针正在发生；背景拉远到美国版图，黄色势力扩张
- A/B：A版以芝加哥事件密度为主
- 禁区：避免纯卫星地图/纯城市名/无动作旗帜；不用现实警务App Logo/UI；不展示无法到达区域
- 参考：06-研发参考-犯罪地图A(Citizen实时犯罪图) + 06-研发参考-犯罪地图B(战略扩张图) + 5-大世界.jpg(UI基准)

## AI提示词-EN
Create a Google Play store featured image (1080x1920 vertical) for a mafia SLG mobile game called GTS. Theme: from one block to all America - Chicago crime map with dense live events. Style: American comic realism with neon-noir crime-city energy, consistent with the previous GTS store images (dark map data on purple-blue glow, glowing event markers, realistic materials, cinematic lighting). NOT cute/chibi, NOT flat cartoon. Keep violence implied, not gory. No realistic celebrity faces. Do not copy GTA or Peaky Blinders logos, fonts, or exact costumes.

[FOREGROUND - THE LIVE CRIME MAP] A large zoomed-in Chicago city map fills the lower two-thirds of the frame, drawn in dark blue-black street-grid style with glowing details. The map is ALIVE with crime events: pulsing red markers for shootouts, orange for robberies, yellow for recruitment - each with small icons, actively happening, with motion trails. This is a real-time crime map where things are currently occurring, not a static satellite view.

[THE EXPANSION - BACKGROUND] Behind/above the Chicago map, the view pulls back to the USA map outline. The yellow faction spreads from one block to three cities and points toward the whole nation, with marching-route animation trails and a few territory-color patches (yellow yours, red/blue rivals). The connection between the local events and the national expansion is visible.

[ANCHOR ACTION] One small but real battle scene is anchored somewhere on the map as the ground-truth focal point - showing that the events on the map correspond to actual gameplay (a small street fight with tiny figures, muzzle flashes), not just icons.

[UI] Standard mobile SLG store screenshot UI, fully integrated: top resource bar (pink diamond +3K, silver coin +200K, gold bar +500K+, gear settings, envelope mail, dark-bg white-text rounded chips); top-left circular player avatar with purple border, nickname, pink star level 30, purple fist power number; top-right top-down city minimap with castle base icon; left vertical buttons ACTIVITY / PASS / STARTER with red notification dots; right vertical buttons RANKING / SHOP / OPSS / BAG; bottom-center large title "FROM ONE BLOCK TO ALL AMERICA." in white bold sans-serif uppercase on a dark backdrop, occupying the bottom 15-20%.

[STYLE] Bright-readable data-map look: the live crime events and the national expansion must be obvious in 3 seconds at 180px. The map shows ACTION happening now (events + routes + one battle), NOT a static satellite map or a list of city names. Dark map base with glowing red/yellow event markers on purple-blue, American comic realism. Realistic gameplay visuals at least 60%.

[RESTRICTIONS] Do NOT make it a pure satellite map, pure city-name labels, or action-less flags. Do NOT copy real police-app logos or UI elements (no real-world emergency app branding); borrow only the "event density" expression. Do NOT show unreachable areas. No realistic celebrity faces. Do not copy GTA/Peaky Blinders logos, fonts, or costumes.

## AI提示词-中文
为GTS黑帮SLG游戏生成一张Google Play商店图（1080×1920竖屏），主题：从一个街区，到统一全美——芝加哥犯罪地图密集实时事件。风格：美漫写实×霓虹黑色城市感，与GTS之前商店图连贯（深色地图数据+紫蓝辉光、发光事件标记、真实材质、电影级布光）；绝不是Q版萌系、不是扁平卡通。暴力只暗示、不血腥。不用真实明星脸。不复制GTA/浴血黑帮的Logo、字体、服装。

[前景·实时犯罪地图] 一张放大的芝加哥城市地图铺满画面下三分之二，深蓝黑街区网格风格带发光细节。地图充满活力：火并的红色脉动标记、抢劫的橙色标记、招募的黄色标记——每个带小图标，正在发生，有运动轨迹。这是实时犯罪地图，有正在发生的事情，不是静态卫星图。

[扩张·背景] 在/高于芝加哥地图后方，视野拉远到美国版图轮廓。黄色势力从一个街区扩展到三座城市并指向全国，带有行军路线动画轨迹和几块势力色块（黄色=你方，红/蓝=对手）。局部事件和全国扩张之间的联系清晰可见。

[锚点动作] 地图某处锚定一个小而真实的战斗场景作为落地焦点——显示地图上的事件对应实际玩法（一场小人物的街头战斗，枪口火光），不只是图标。

[UI] 完整集成手游SLG商店截图UI：顶部资源条（粉钻+3K/银币+200K/金币+500K+/齿轮设置/信封邮件，黑底白字圆角芯片）；左上角圆形玩家头像（紫色描边）+昵称+粉色星星等级30+紫色拳头战斗力数字；右上角俯视城市小地图+城堡据点图标；左侧竖排按钮ACTIVITY/PASS/STARTER（红色通知点）；右侧RANKING/SHOP/OPSS/BAG；底部居中大字标题"FROM ONE BLOCK TO ALL AMERICA."，白色粗体无衬线全大写，深色底衬，占底部15-20%。

[风格] 明亮可读的数据地图感：实时犯罪事件和全国扩张必须在180px缩略图下3秒内看懂。地图显示"现在正在发生的动作"（事件+路线+一处战斗），不是静态卫星图或城市名清单。深色地图底+红/黄发光事件标记+紫蓝，美漫写实。真实玩法画面至少60%。

[禁区] 不要做成纯卫星地图、纯城市名标注或无动作的旗帜。不要复制现实警务App的Logo或UI元素（不用现实紧急应用品牌）；只借鉴"事件密度"的表达。不展示无法到达的区域。不用真实明星脸。不复制GTA/浴血黑帮的Logo、字体、服装。
