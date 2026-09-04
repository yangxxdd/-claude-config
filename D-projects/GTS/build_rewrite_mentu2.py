# -*- coding: utf-8 -*-
"""重做 2 条门徒立绘脚本，补景别/UI游戏感/背景/特效四要素"""
import csv

rows = [
[6, "P-门徒立绘-绯夜单卡(首充·商业化)", "1080×1080", "欲望(日式情人)+视觉冲击",
"二次元游戏角色立绘，半身胸像景别(主体占画面60-70%)：冷艳的日式黑帮女性门徒'绯夜'，深色和服+若隐若现蛇纹刺青，手持折扇，正面略仰视构图凸显气场。游戏UI元素齐全——SSR金色稀有度框围绕，顶部标注SSR，左下角'首充'角标，右下角'获取'发光按钮，底部钻石货币图标。角色周身金色粒子流光特效，SSR框金色光效。背景暗色黑帮都市夜景霓虹(虚化，不抢主体)。",
"二次元游戏角色立绘，半身胸像，主体占画面百分之六十到七十，一位冷艳的日式黑帮女性门徒，身穿优雅深色和服，手臂肩颈有若隐若现的蛇纹刺青，手持精致折扇，正面略仰视构图，气场强大。游戏UI界面元素：SSR金色稀有度框围绕角色，顶部用简洁标准字体标注SSR，左下角一个红色'首充'角标，右下角一个发光'获取'按钮，底部有钻石货币图标。角色周身有金色粒子流光特效，SSR框带金色光效。背景是暗色黑帮都市夜景霓虹，虚化处理，不抢主体。竖版构图，游戏卡面插画质感，戏剧化电影打光，精致人物细节，除SSR、首充、获取外不要其他任何文字。",
"Anime game character art, half-body portrait, subject occupying 60-70% of the frame, a coldly beautiful Japanese-style mafia female disciple in an elegant dark kimono, faint snake tattoos on her arms and shoulders, holding a delicate folding fan, slightly low-angle front composition exuding authority. Game UI elements: a gold SSR rarity frame around the character, the rarity text 'SSR' in a clean standard font at the top, a red 'First Recharge' badge at the bottom-left, a glowing 'Recruit' button at the bottom-right, and diamond currency icons at the bottom. Golden particle flow effects around the character, gold glow on the SSR frame. Background is a dark mafia city neon night scene, blurred, not stealing focus from the subject. Vertical composition, game card art quality, dramatic cinematic lighting, exquisite detail, no other text except SSR, First Recharge and Recruit.",
"首充门徒/日式情人立绘 + 门徒抽卡UI"],

[7, "P-门徒群像-集结展示(收集欲)", "1080×1080", "好奇(这些门徒是谁)+视觉冲击(排面)",
"二次元游戏角色群像立绘，全身景别(群像占画面70%)：一排风格各异的黑帮门徒并肩而立——西装打手(精瘦凶悍)、机车党(皮衣墨镜)、神枪手(风衣狙击枪)、绯夜(和服蛇纹)，居中者气场最强，站姿端正体现纪律感。游戏UI元素——顶部'门徒'标题框，每个门徒脚下稀有度标识(SSR/SR/R)，底部'十连招募'发光按钮。每个门徒有登场光效(稀有度越高光效越强)，集结气场光。低角度仰视群像构图，压迫感。背景暗色黑帮都市夜景霓虹(虚化)。",
"二次元游戏角色群像立绘，全身，群像占画面百分之七十，一排风格各异的黑帮门徒并肩而立：左边精瘦凶悍的西装打手，旁边穿皮衣戴墨镜的机车党，再旁边披风衣扛狙击枪的神枪手，最右边穿和服有蛇纹刺青的冷艳女性门徒，站姿端正体现纪律感，居中者气场最强。游戏UI元素：顶部一个'门徒'标题框，每个门徒脚下有稀有度标识(SSR、SR、R)，底部一个发光'十连招募'按钮。每个门徒有登场光效，稀有度越高的门徒光效越强。低角度仰视群像构图，压迫感十足。背景是暗色黑帮都市夜景霓虹，虚化处理。游戏卡面质感，戏剧化打光，除SSR、SR、R、十连招募外不要其他任何文字。",
"Anime game character group art, full-body, the group occupying 70% of the frame, a row of distinct mafia disciples standing side by side: a lean fierce thug in a suit on the left, a leather-jacket sunglasses biker, a trench-coat sniper with a rifle, and a coldly beautiful kimono-clad female disciple with snake tattoos on the right, upright disciplined stances, the central figure most dominant. Game UI elements: a 'Disciples' title box at the top, rarity badges (SSR, SR, R) under each disciple's feet, a glowing '10x Recruit' button at the bottom. Each disciple has an entrance light effect, stronger for higher rarity. Low-angle group composition with oppressive presence. Background is a dark mafia city neon night scene, blurred. Game card art quality, dramatic lighting, no other text except SSR, SR, R and 10x Recruit.",
"门徒群像 + 招募表演素材 + 门徒抽卡UI"],
]

with open("D:/claude-projects/projects/GTS/rewrite_mentu2.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)
print("重做行数:", len(rows))
print("done")
