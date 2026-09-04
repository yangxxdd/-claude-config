# 05-B 提示词 V2（单场景叙事：胜利成果融入场景）

## 核心改动（V1 → V2）
- V1 问题：战利品/变色是"右上角贴片"，与前景人物脱节，元素堆叠
- V2 方案：把"结果"写成**一个连贯场景中的动作**——领袖站在刚占领的街区，战利品在脚下，小弟在搬运，钥匙在手中
- 三层分离：场景层（街区+人物+战利品在真实空间）/ 特效层（街区边界黄光作为"占领"的视觉反馈）/ UI层（边缘）
- 结果不再是一个角标，而是"这个街区被我们赢了"的完整叙事画面

## AI提示词-EN (V2)
Create a Google Play store featured image (1080x1920 vertical) for a mafia SLG mobile game called GTS. Theme: bring your crew, take the block - the victorious RESULT of winning a gang fight. Style: American comic realism with bright crime-comedy energy, neon-noir accent, consistent with the previous GTS store images (warm action foreground on purple-blue city background, realistic materials, cinematic lighting). NOT cute/chibi, NOT flat cartoon. Violence implied, NOT gory. No realistic celebrity faces. Do not copy GTA or Peaky Blinders logos, fonts, or exact costumes.

[SCENE - A SINGLE COHERENT MOMENT] The female cowgirl disciple-leader stands at the entrance of a just-captured city block, the center of the frame. She has just won the fight. Behind her, the block now belongs to her crew: her followers are carrying loot - bundles of cash, a golden territory key, resource crates - out of the captured buildings toward a growing pile at her feet. One follower hoists a cash bundle, another drags a crate. The key she just claimed is in her own hand, held up triumphantly.

[THE RESULT - PART OF THE SCENE] The captured territory is shown as a real place, not a UI marker: the buildings behind her are now lit in her crew's warm yellow light (a subtle glow marking "ours now"), the street edge transitions from neutral gray to warm gold where her crew controls it. The loot is physically on the ground and being carried - it belongs to the moment, in proper spatial relation to the characters.

[FOREGROUND] The leader is front and center, larger, holding the golden key up, confident victorious pose, her crew around her. The battle aftermath is visible but light: scattered smoke from the fight receding behind, no gore.

[BACKGROUND] The captured block stretches back with depth - buildings, street, the enemy has fallen back; distant city in purple-blue ambient tone, warm gold where her crew's territory begins.

[UI] Standard mobile SLG store screenshot UI, fully integrated: top resource bar (pink diamond +3K, silver coin +200K, gold bar +500K+, gear settings, envelope mail, dark-bg white-text rounded chips); top-left circular player avatar with purple border, nickname, pink star level 30, purple fist power number; top-right top-down city minimap with castle base icon; left vertical buttons ACTIVITY / PASS / STARTER with red notification dots; right vertical buttons RANKING / SHOP / OPSS / BAG; bottom-center large title "BRING YOUR CREW. TAKE THE BLOCK." in white bold sans-serif uppercase on a dark backdrop, occupying the bottom 15-20%.

[STYLE] Bright, readable at thumbnail size: the victory result must be obvious in 3 seconds at 180px. The leader holding the key + her crew carrying loot + the captured block glowing behind = one coherent story. NOT a UI marker pasted in a corner - the result is a real place and real people. Warm gold on purple-blue, American comic realism. Realistic gameplay visuals at least 60%.

[RESTRICTIONS] Do NOT show a loot pile floating in a corner disconnected from the scene. Do NOT show a single-person duel or hero-portrait poster. Avoid gore, blood, corpses. Do not let the action replace the identity hero image. No marijuana or drugs. No realistic celebrity faces. Do not copy GTA/Peaky Blinders logos, fonts, or costumes.

## AI提示词-中文 (V2)
为GTS黑帮SLG游戏生成一张Google Play商店图（1080×1920竖屏），主题：带上你的人，拿下这条街——赢得帮派战斗后的胜利成果。风格：美漫写实×明亮犯罪喜剧×霓虹点缀，与GTS之前商店图连贯（暖色动作前景+紫蓝城市背景、真实材质、电影级布光）；绝不是Q版萌系、不是扁平卡通。暴力只暗示、不血腥。不用真实明星脸。不复制GTA/浴血黑帮的Logo、字体、服装。

[场景·单一连贯时刻] 女牛仔门徒领袖站在一个刚被占领的街区入口，位于画面中央。她刚刚打赢了这场战斗。在她身后，街区现在属于她的帮派：她的小弟们正把战利品——成捆现金、一把金色地盘钥匙、资源箱——从被占领的建筑里搬出来，堆向她在脚下的一个越来越大的战利品堆。一个小弟扛着一捆现金，另一个拖着一个箱子。她刚夺得的钥匙握在自己手中，得意地举起。

[结果·场景的一部分] 被占领的领土展示为一个真实的地方，而不是UI标记：她身后的建筑现在亮着她帮派的暖黄色灯光（微光标注"现在归我们"），街道边缘在她帮派控制的地方从中性灰过渡到暖金色。战利品物理地在地上、被人搬运——它属于这个时刻，与人物有正确的空间关系。

[前景] 领袖位于画面中央靠前、更大，举起金色钥匙，自信的胜利姿态，帮派成员围在她身边。战斗的余波可见但轻微：战斗退去后散落的烟雾，无血腥。

[背景] 被占领的街区向纵深延伸——建筑、街道，敌人已退却；远处城市是紫蓝环境色调，她帮派领土开始的地方是暖金色。

[UI] 完整集成手游SLG商店截图UI：顶部资源条（粉钻+3K/银币+200K/金币+500K+/齿轮设置/信封邮件，黑底白字圆角芯片）；左上角圆形玩家头像（紫色描边）+昵称+粉色星星等级30+紫色拳头战斗力数字；右上角俯视城市小地图+城堡据点图标；左侧竖排按钮ACTIVITY/PASS/STARTER（红色通知点）；右侧RANKING/SHOP/OPSS/BAG；底部居中大字标题"BRING YOUR CREW. TAKE THE BLOCK."，白色粗体无衬线全大写，深色底衬，占底部15-20%。

[风格] 明亮、缩略图可读：胜利结果必须在180px缩略图下3秒内看懂。领袖举钥匙+小弟搬运战利品+被占领街区在身后发光=一个连贯的故事。不是贴在角落的UI标记——结果是真实的地方和真实的人。暖金+紫蓝，美漫写实。真实玩法画面至少60%。

[禁区] 不要展示与场景脱节的漂浮在角落的战利品堆。不要展示单人决斗或英雄立绘海报。避免血腥、鲜血、尸体。不要让动作图替代身份首图。不出现大麻/毒品。不用真实明星脸。不复制GTA/浴血黑帮的Logo、字体、服装。
