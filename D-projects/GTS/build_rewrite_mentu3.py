# -*- coding: utf-8 -*-
"""重写门徒群像：一排站 → 金字塔式阵型"""
import csv

rows = [
[7, "P-门徒群像-集结展示(收集欲)", "1080×1080", "好奇(这些门徒是谁)+视觉冲击(阵型排面)",
"二次元游戏角色群像立绘，全身景别(群像占画面70%)，金字塔式阵型构图：SSR门徒绯夜(和服蛇纹)居中最前最突出，气场最强(C位主角)；其余门徒按稀有度向两侧后方错落——西装打手(精瘦凶悍)在左后、机车党(皮衣墨镜)在左后更远处、神枪手(风衣狙击枪)在右后，形成V字扇形阵型，有前后纵深和主次关系，不是一字排开。游戏UI元素——顶部'门徒'标题框，每个门徒脚下稀有度标识(SSR/SR/R)，底部'十连招募'发光按钮。每个门徒登场光效(稀有度越高越强)。低角度仰视，压迫感。背景暗色黑帮都市夜景霓虹(虚化)。",
"二次元游戏角色群像立绘，全身，群像占画面百分之七十，金字塔式阵型构图：一位穿和服有蛇纹刺青的冷艳女性门徒(SSR)居中最前最突出，气场最强，是C位主角；其余门徒按稀有度向两侧后方错落——左边稍后是精瘦凶悍的西装打手，再靠后是穿皮衣戴墨镜的机车党，右边稍后是披风衣扛狙击枪的神枪手，形成V字扇形阵型，有前后纵深和主次关系，不是一字排开。游戏UI元素：顶部一个'门徒'标题框，每个门徒脚下有稀有度标识(SSR、SR、R)，底部一个发光'十连招募'按钮。每个门徒有登场光效，稀有度越高的门徒光效越强。低角度仰视群像构图，压迫感十足。背景是暗色黑帮都市夜景霓虹，虚化处理。游戏卡面质感，戏剧化打光，除SSR、SR、R、十连招募外不要其他任何文字。",
"Anime game character group art, full-body, the group occupying 70% of the frame, pyramid formation composition: a coldly beautiful kimono-clad female disciple with snake tattoos (SSR) stands in the center front, most prominent and commanding, the C-position lead; the other disciples fall back to the sides by rarity — a lean fierce thug in a suit on the left slightly behind, a leather-jacket sunglasses biker further back, a trench-coat sniper with a rifle on the right slightly behind — forming a V-shaped fan formation with front-to-back depth and clear hierarchy, NOT a flat straight line. Game UI elements: a 'Disciples' title box at the top, rarity badges (SSR, SR, R) under each disciple's feet, a glowing '10x Recruit' button at the bottom. Each disciple has an entrance light effect, stronger for higher rarity. Low-angle group composition with oppressive presence. Background is a dark mafia city neon night scene, blurred. Game card art quality, dramatic lighting, no other text except SSR, SR, R and 10x Recruit.",
"门徒群像 + 招募表演素材 + 门徒抽卡UI"],
]

with open("D:/claude-projects/projects/GTS/rewrite_mentu3.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)
print("重写行数:", len(rows))
print("done")
