# -*- coding: utf-8 -*-
"""为方向 02-10 生成中英双语 AI 提示词"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from directions_base import DIRECTIONS

# 统一的 UI 段落（所有方向通用，沿用 GTS 真实 UI 体系）
UI_EN = """[UI] Standard mobile SLG store screenshot UI, fully integrated: top resource bar (pink diamond +3K, silver coin +200K, gold bar +500K+, gear settings, envelope mail, dark-bg white-text rounded chips); top-left circular player avatar with purple border, nickname, pink star level 30, purple fist power number; top-right top-down city minimap with castle base icon; left vertical buttons ACTIVITY / PASS / STARTER with red notification dots; right vertical buttons RANKING / SHOP / OPSS / BAG; bottom-center large title in white bold sans-serif uppercase on a dark backdrop, occupying the bottom 15-20%."""

UI_ZH = """[UI] 完整集成手游SLG商店截图UI：顶部资源条（粉钻+3K/银币+200K/金币+500K+/齿轮设置/信封邮件，黑底白字圆角芯片）；左上角圆形玩家头像（紫色描边）+昵称+粉色星星等级30+紫色拳头战斗力数字；右上角俯视城市小地图+城堡据点图标；左侧竖排按钮ACTIVITY/PASS/STARTER（红色通知点）；右侧RANKING/SHOP/OPSS/BAG；底部居中大字标题（白色粗体无衬线全大写，深色底衬，占底部15-20%）。"""

# 统一的风格前缀（所有方向共用，保证整套商店图风格一致）
STYLE_EN = """in the style of American comic realism with neon-noir crime city energy (like Batman: Arkham / Watch Dogs game art), bright crime-comedy mood, warm golden/orange/red foreground contrasting with cool purple-blue night background, cinematic lighting, realistic materials, NOT cute/chibi, NOT flat cartoon. Keep violence implied, not gory. No realistic celebrity faces. Do not copy GTA or Peaky Blinders logos, fonts, or exact costumes."""

STYLE_ZH = """风格：美漫写实（类似《蝙蝠侠：阿卡姆》《看门狗》游戏美术）× 明亮犯罪喜剧 × 霓虹黑色城市氛围；暖金/橙红前景 vs 冷紫蓝夜晚背景、电影级布光、真实材质；绝不是Q版萌系、不是扁平卡通。暴力只暗示、不血腥。不用真实明星脸。不复制GTA/浴血黑帮的Logo、字体、服装。"""

# 每个方向的具体画面描述（EN/ZH），基于 producer_intent + scene
SCENES = {
"02": {
  "en": """[FOREGROUND] A confident disciple or the cowgirl hero stands at the center of a bright sunlit city intersection, arms crossed, deciding which way to go next. Around her, three real gameplay events unfold as small vignettes: collecting protection money from a shopkeeper, recruiting a new disciple from a crowd, and a small street shootout between rival crews. A bright yellow route line connects the three events across the pavement, and a red circular event pin marks each spot. [MIDGROUND] A vibrant American city in daytime: classic cars, palm trees, crosswalks, shopfronts, pedestrians - a lively, safe-looking city that secretly hides criminal opportunities. [BACKGROUND] The city extends into the distance with skyline silhouettes under a clear blue sky with soft clouds; a few warm neon signs hint at the night that will come.""",
  "zh": """[前景] 一位自信的门徒或女牛仔主角站在明亮的午后城市十字路口中央，双臂交叉，决定下一步往哪走。她周围有3个真实玩法事件作为小场景展开：向店主收保护费、从人群中招募新门徒、两个敌对帮派间的街头交火。一条亮黄色路线穿过路面串联三个事件，每个点位钉着红色圆形事件针。[中景] 明亮的美式城市日景：经典汽车、棕榈树、斑马线、店铺门面、行人——一个看似安全热闹的城市，实则暗藏犯罪机会。[背景] 城市向远处延伸，天际线剪影映在晴朗的蓝天白云下；几处暖色霓虹招牌暗示夜晚将至。"""
},
"03-A": {
  "en": """[FOREGROUND-LEFT] A finger drags a thick stack of dollar bills from the bottom-left corner, a green glowing money trail arcing into the center. [CENTER] The glowing green cash trajectory flows into a locked room/building; the lock breaks with a crack effect and the room lights up. [FOREGROUND-RIGHT] The unlocked room pops out a production result - stacks of cash, resources, and an output panel. The causal chain reads left-to-right in one glance: drag cash -> unlock -> production. [BACKGROUND] A clean modern building interior with a purple-blue ambient tone; the behavior is the subject, not the UI.""",
  "zh": """[左前景] 一根手指从左下角拖动一叠厚厚的美钞，一道绿色发光钞票轨迹弧形飞向画面中央。[中景] 绿色钞票轨迹流入一间锁着的房间/建筑；锁随着破裂特效打开，房间点亮。[右前景] 解锁的房间弹出产业产出——成堆现金、资源和一个产出面板。三段因果一眼从左读到右：拖现金→解锁→产出。[背景] 干净现代的建筑室内，紫蓝环境色调；主体是行为动作，不是UI。"""
},
"03-B": {
  "en": """[FOREGROUND-LEFT] A finger drags a thick stack of dollar bills from the bottom-left corner, a green glowing money trail arcing into the center. [CENTER] The glowing green cash trajectory flows into a locked outdoor street-industry building; the lock breaks and the block lights up. [FOREGROUND-RIGHT] The unlocked street block pops out production - cash, resources, and an output panel. Same three-stage causal chain as version A but with the unlock target being an outdoor street industry instead of an indoor room. [BACKGROUND] A modern city block exterior with purple-blue ambient tone.""",
  "zh": """[左前景] 一根手指从左下角拖动一叠厚厚的美钞，一道绿色发光钞票轨迹弧形飞向画面中央。[中景] 绿色钞票轨迹流入一座锁着的室外街区产业建筑；锁破裂，街区点亮。[右前景] 解锁的街区弹出产出——现金、资源和产出面板。三段因果与A版一致，但解锁对象从室内房间改为室外街区产业。[背景] 现代城市街区外观，紫蓝环境色调。"""
},
"04-A": {
  "en": """[CENTER] A street band / a musical disciple performs at the center of a graffiti park, playing an electric guitar, energy waves radiating outward. [OUTER RING] Citizens gather from all sides, shown in three stages of transformation: normal passersby -> curious onlookers drawn in -> converts joining as a row of new disciples (crowd growing from 3 to 12 people). [BACKGROUND] A bright graffiti park: colorful spray-paint murals, a skateboard half-pipe, fried chicken bucket stickers on the walls, urban playfulness. Crowd density and numbers are the focus of this version.""",
  "zh": """[中心] 涂鸦公园中央，一支街头乐队/一名演奏门徒在弹电吉他，能量波向外扩散。[外圈] 市民从四面八方聚拢，以三段轮廓变化呈现：普通路人→被吸引的围观者→加入列队的新小弟（人群从3人增长到12人）。[背景] 明亮的涂鸦公园：彩色喷绘涂鸦墙、滑板坡道、墙上的炸鸡桶贴纸，充满城市活力。本版重点是人群数量变化。"""
},
"04-B": {
  "en": """[CENTER] A street band / a musical disciple performs at the center of a graffiti park. [FOCUS] One distinctive disciple is drawn in by the music and joins a three-person lineup - a single-character transformation shown clearly: playing -> attracting -> the disciple joining the team. The crowd around is secondary; the featured disciple is the clear focus. [BACKGROUND] A bright graffiti park: colorful spray-paint murals, a skateboard half-pipe, fried chicken bucket stickers on the walls.""",
  "zh": """[中心] 涂鸦公园中央，街头乐队/演奏门徒在表演。[焦点] 一名特色门徒被音乐吸引，加入三人阵容——清晰展示单体转化：演奏→吸引→门徒入队。周围人群是次要的，特色门徒是明确焦点。[背景] 明亮的涂鸦公园：彩色喷绘涂鸦墙、滑板坡道、墙上炸鸡桶贴纸。"""
},
"05-A": {
  "en": """[FOREGROUND] A battle-ready disciple stands at the bottom third of the frame, leading 6-10 followers behind him in a large street battle. [MIDGROUND] A chaotic but lively gang fight at a city crossroads or mansion entrance: cover positions, bullet trails, cars, muzzle flashes - the scale of the fight is the focus of this version. [FOREGROUND-RIGHT] The contested block turns from gray to yellow in the upper right, with cash and a territory key dropping down. Gritty but not gory - no blood close-ups.""",
  "zh": """[前景] 一名战斗型门徒站在画面下三分之一处，率领身后6-10名小弟进行大规模街头火并。[中景] 城市十字路口或豪宅门前混乱但热闹的帮派火并：掩体、弹道、车辆、枪口火光——本版重点是战斗规模。[右上] 争夺中的街区从灰色变为黄色，掉落现金和地盘钥匙。硬朗但不血腥——无鲜血特写。"""
},
"05-B": {
  "en": """[FOREGROUND] A battle-ready disciple leads 6-10 followers in a street battle at a city crossroads (battle slightly reduced in this version). [FOREGROUND-RIGHT EMPHASIS] The contested block turns from gray to yellow with a LARGER, more prominent color-change area, and MORE loot dropping: cash, territory keys, and supplies raining down as the visual focus. The result layer is amplified over the fight scale. Gritty but not gory - no blood close-ups.""",
  "zh": """[前景] 战斗型门徒率6-10名小弟在城市十字路口火并（本版战斗略缩小）。[右上强化] 争夺中的街区从灰色变黄色，变色面积更大更醒目，更多战利品掉落：现金、地盘钥匙、物资如雨落下作为视觉焦点。结果层放大优先于战斗规模。硬朗但不血腥——无鲜血特写。"""
},
"06-A": {
  "en": """[FOREGROUND] A large zoomed-in Chicago crime map fills the lower frame: event pins for shootouts, robberies, and recruitment are actively happening, with pulsing red markers. [BACKGROUND] The view pulls back to the full USA map outline; the yellow faction spreads from one block to three cities and points toward the whole nation, with marching-route animation trails. One real battle scene is anchored in the foreground as the ground-truth focal point. This version emphasizes Chicago event density.""",
  "zh": """[前景] 放大的芝加哥犯罪地图铺满下半画面：火并、抢劫、招募的事件针正在发生，红色标记脉动。[背景] 视野拉远到美国版图轮廓；黄色势力从一个街区扩展到三座城市并指向全国，带有行军路线动画残影。前景锚定一处真实战斗作为落地焦点。本版强调芝加哥事件密度。"""
},
"06-B": {
  "en": """[FOREGROUND] One real battle scene is anchored at the bottom as the ground-truth focal point. [BACKGROUND EMPHASIS] The USA map outline fills most of the frame; the yellow faction covers a LARGER area spanning multiple cities with prominent city labels and marching routes - the nationwide expansion is the focus of this version. Event pins on Chicago remain but are secondary to the national map spread.""",
  "zh": """[前景] 底部锚定一处真实战斗作为落地焦点。[背景强化] 美国版图轮廓铺满大部分画面；黄色势力覆盖更大的面积、横跨多座城市，城市标注和行军路线醒目——本版重点是全国版图扩张。芝加哥事件针保留但作为次要。"""
},
"07-A": {
  "en": """[CENTER] A small energetic Jack Russell terrier is the visual hero: tiny body, lively expressive face, strong contrast against the burly gang disciples. It playfully bites an enemy's trouser leg or snatches a mission item, while the disciple and followers seize the moment to attack. A toppled fried chicken bucket adds a humorous secondary detail. [MIDGROUND] A night city street battle scene with gang disciples. [MOOD] Comedic contrast - the cute little dog disrupting a serious fight.""",
  "zh": """[中心] 一只活泼的小型杰克罗素梗犬是视觉主角：体型小、表情生动、与壮硕的黑帮门徒形成强烈反差。它调皮地咬住敌人的裤脚或叼走任务物品，门徒与小弟趁机进攻。一个被撞翻的炸鸡桶作为幽默次细节。[中景] 夜晚城市街头的帮派战斗场景。[氛围] 喜剧反差——可爱小狗打乱一场严肃的战斗。"""
},
"07-B": {
  "en": """[CENTER] A large powerful German Shepherd is the visual hero: bigger, fiercer, more combat-ready than the Jack Russell version. It lunges at the enemy with impactful force, the disciple and followers attacking behind it. Less comedic, more about combat power. [MIDGROUND] A night city street battle scene with gang disciples. [MOOD] The shepherd reads as a real combat asset, not a joke.""",
  "zh": """[中心] 一只大型强壮的德国牧羊犬是视觉主角：比杰克罗素版更大、更凶猛、更有战斗力。它扑向敌人充满冲击力，门徒与小弟在其后进攻。喜剧感减弱，更强调战力。[中景] 夜晚城市街头帮派战斗场景。[氛围] 德牧是真实的战斗力量，不是笑点。"""
},
"08-A": {
  "en": """[UPPER-LEFT] A loved one is injured and trapped in a crime scene (surrounded and hurt, NOT bound or exposed), in distress. [CENTER] A finger taps a rescue action button, a red countdown timer glowing urgently. [LOWER-RIGHT] Disciples and followers storm into the block to fight. A yellow route line strengthens the urgency. Three-part narrative: crisis -> tap to rescue -> consequence. This version emphasizes rescue urgency (countdown + finger guide).""",
  "zh": """[左上] 心爱之人受伤被困在犯罪现场（被围困受伤，不是束缚/暴露），处境危急。[中央] 手指点按救援按钮，红色倒计时紧急闪烁。[右下] 门徒与小弟冲入街区战斗。一条黄色路线强化紧迫感。三段叙事：危机→点击救援→后果。本版强调救援紧迫（倒计时+手指引导）。"""
},
"08-B": {
  "en": """[UPPER-LEFT] A loved one is injured and trapped (surrounded and hurt, NOT bound or exposed), smaller and secondary. [LOWER-RIGHT MAIN] The revenge battle dominates: disciples and followers in a large firefight, the rescue crisis smaller, the war the main visual. Red countdown and yellow route remain but the vengeance firefight is the hero shot. Three-part narrative kept, but consequence layer amplified.""",
  "zh": """[左上] 心爱之人受伤被困（被围困受伤，不是束缚/暴露），占比缩小作为次要。[右下主视觉] 复仇火并主导画面：门徒与小弟大规模交火，救援危机缩小，复仇战争成为主视觉。红色倒计时和黄色路线保留，但复仇火并是主角。三段叙事保留，后果层放大。"""
},
"09-A": {
  "en": """[CENTER] The cowgirl hero (Icon/first-charge anchor) stands centered as the anchor, with one different-role disciple on each side. Above each are ultra-short role labels: FIRE / BUSINESS / SUPPORT. [BELOW] Below the three characters, the same team shows a combined-attack result in a block firefight - a finishing combo. [STYLE] Three distinct characters with clear roles, comic hero energy. This version groups by faction/archetype combination.""",
  "zh": """[中央] 女牛仔主角（Icon/首充锚点）居中作为锚点，左右各一名不同定位的门徒。每人上方有极短的角色标签：FIRE(火力)/BUSINESS(生意)/SUPPORT(支援)。[下方] 三名角色下方，同一队伍在街区火并中展示合击结果——终结连招。[风格] 三名角色定位清晰、个性鲜明，美漫英雄气质。本版按阵营/定位组合。"""
},
"09-B": {
  "en": """[CENTER] The cowgirl hero stands centered, with one different-role disciple on each side. Role labels change to: PROSPECTING / MANAGEMENT / COMBAT (gameplay-task oriented). [BELOW] Below the three characters, the combined-attack result shows three task-completion scenes (opening / running business / fighting). Same layout as version A but roles are gameplay-task based.""",
  "zh": """[中央] 女牛仔主角居中，左右各一名不同定位的门徒。角色标签改为：开荒/经营/战斗（按玩法任务定位）。[下方] 三人下方，合击结果展示三种任务完成场景（开荒/经营/火并）。布局与A版一致，但角色按玩法任务组合。"""
},
"10-A": {
  "en": """[LEFT] A level-1 mansion/property in its early state. [CENTER] A stack of cash is being poured in, pulling an upgrade progress bar. [RIGHT] The completed mansion: pool, car fleet, and security guards visibly added, same camera angle as the left for a clear before/after contrast. Construction light effects and particles emphasize the transformation. Same-lens before/after read is the core of this image. This version upgrades the mansion.""",
  "zh": """[左侧] 一级豪宅/产业的初始状态。[中央] 一叠现金投入，拉动升级进度条。[右侧] 完成态豪宅：泳池、车队、安保人员明显增加，与左侧同镜头角度形成清晰的before/after对比。施工光效和粒子强化转变。同镜头before/after是本图核心。本版升级对象是豪宅。"""
},
"10-B": {
  "en": """[LEFT] A level-1 fried chicken shop in its early state. [CENTER] A stack of cash is being poured in, pulling an upgrade progress bar. [RIGHT] The max-level fried chicken chain: neon sign, expanded scale, more customers - same camera angle as the left for a clear before/after contrast. This version upgrades the fried chicken shop/industry instead of the mansion. Construction light effects emphasize the transformation.""",
  "zh": """[左侧] 一级炸鸡店的初始状态。[中央] 一叠现金投入，拉动升级进度条。[右侧] 满级炸鸡连锁：霓虹招牌、规模扩大、顾客更多——与左侧同镜头角度形成before/after对比。本版升级对象是炸鸡店/产业而非豪宅。施工光效强化转变。"""
},
}


# 英文主题描述（供 Gemini 理解，不直接用中文）
EN_THEME = {
  "02": "run the city your way - a casual crime playground",
  "03-A": "put cash to work - submit cash to unlock an industry (room unlock)",
  "03-B": "put cash to work - submit cash to unlock an industry (street block unlock)",
  "04-A": "draw a crowd, build a crew - street band recruiting disciples in a graffiti park (crowd focus)",
  "04-B": "draw a crowd, build a crew - a featured disciple joins the lineup in a graffiti park (recruit focus)",
  "05-A": "bring your crew, take the block - gang shootout scale",
  "05-B": "bring your crew, take the block - gang shootout result and loot",
  "06-A": "from one block to all America - Chicago crime map event density",
  "06-B": "from one block to all America - nationwide map expansion",
  "07-A": "even the dog works for the family - Jack Russell terrier comedic combat",
  "07-B": "even the dog works for the family - German Shepherd combat power",
  "08-A": "save her, start a war - rescue urgency",
  "08-B": "save her, start a war - revenge firefight",
  "09-A": "build a crew for every hustle - three-disciple lineup by faction/archetype",
  "09-B": "build a crew for every hustle - three-disciple lineup by gameplay task",
  "10-A": "turn cash into power - mansion upgrade before/after",
  "10-B": "turn cash into power - fried chicken shop upgrade before/after",
}


def build_prompt(code):
    d = DIRECTIONS[code]
    scene = SCENES[code]
    title = d["en"]
    en_theme = EN_THEME[code]
    en_prompt = (
        f"Create a Google Play store featured image (1080x1920 vertical) for a mafia SLG mobile game called GTS. "
        f"Theme: {en_theme}. {STYLE_EN}\n\n"
        f"{scene['en']}\n\n"
        f"{UI_EN.replace('bottom-center large title in white bold sans-serif uppercase on a dark backdrop, occupying the bottom 15-20%.', f'bottom-center large title \\\"{title}\\\" in white bold sans-serif uppercase on a dark backdrop, occupying the bottom 15-20%.')}"
    )
    zh_prompt = (
        f"为GTS黑帮SLG游戏生成一张Google Play商店图（1080×1920竖屏），主题：{d['subject']}。{STYLE_ZH}\n\n"
        f"{scene['zh']}\n\n"
        f"{UI_ZH.replace('底部居中大字标题（白色粗体无衬线全大写，深色底衬，占底部15-20%）', f'底部居中大字标题\\\"{title}\\\"（白色粗体无衬线全大写，深色底衬，占底部15-20%）')}"
    )
    return zh_prompt, en_prompt


if __name__ == "__main__":
    for code in ["02", "03-A", "04-A", "05-A", "06-A", "07-A", "08-A", "09-A", "10-A"]:
        zh, en = build_prompt(code)
        print(f"===== {code} ===== 中文{len(zh)}字 英文{len(en)}字")
