# -*- coding: utf-8 -*-
"""GTS 视频需求重写版 v2 —— 视频6条 + 放量分镜2条，模块/内容/参考格式"""
import csv

h2 = ["模块", "内容", "参考/备注"]

rows = []

def add(mod, content, ref=""):
    rows.append([mod, content, ref])

# ============ 视频 6 条 ============
add("━━ 视频① V-招募表演-门徒迭代（试点）━━", "", "")
add("创意标准", "悬念(谁上场)+欲望(绯夜日式角色)", "")
add("要求(源素材+改动点·优化)", "基于7月 V-招募表演 迭代：把登场门徒换成新立绘'绯夜'（首充门徒/日式情人+蛇纹刺青），前3秒先给绯夜剪影+蛇纹特写立悬念，再做登场表演变体（不同登场动作/灯光节奏/BGM），结尾保留招募钩子。AI制作，可剪30s/15s版。", "")
add("吸睛逻辑", "公式=门徒表演→招募结果（7月 Install D1 39.58% 全局最高）；钩子=绯夜剪影悬念；商业化=抽卡暗示", "")
add("文案(英文配音)", "Fresh blood. The family grows. One seat open. Who steps up?", "")
add("参考", "7月 V-招募表演 + 绯夜立绘", "")
add("", "", "")

add("━━ 视频② V-卧底暴露（试点）━━", "", "")
add("创意标准", "好奇/悬念（身份反转）", "")
add("要求(源素材+改动点·优化)", "命运反转公式换剧本（贴黑帮幻想）：警方卧底身份暴露，被黑帮围堵羞辱，前3秒立起'他被围堵、身份将揭穿'的紧张悬念，亮明真正身份绝地反杀。AI制作。", "")
add("吸睛逻辑", "身份反转的戏剧冲突；结局留白；贴黑帮幻想（卧底/背叛是黑帮经典元素）", "")
add("文案(英文配音)", "Undercover for years. Tonight the mask comes off. You wanted a gangster? Here I am.", "")
add("参考", "7月 V-晋级失败被捕", "")
add("", "", "")

add("━━ 视频③ V-鸡公打丧尸（谨慎试点）━━", "", "")
add("创意标准", "情绪/好笑（反差萌）", "")
add("要求(源素材+改动点·优化)", "基于 V-鸡公大侠 恶搞公式（'打X升级'）换对象为打丧尸，必须保留'鸡'这个核心反差元素（鸡打丧尸的违和喜感）；修正7月短板——结尾补复仇反转（原'收集金币'改'逆袭打脸'）。AI制作。", "")
add("吸睛逻辑", "恶搞反差（鸡打丧尸）；修正已知短板=叙事弧线断（7月数据复盘结论）", "")
add("文案(英文配音)", "A nobody. A chicken. And an army of zombies. Guess who wins.", "")
add("参考", "7月 V-鸡公大侠", "")
add("", "", "")

add("━━ 视频④ V-打丧尸枪战（谨慎试点）━━", "", "")
add("创意标准", "代入/想玩（玩法实录）", "")
add("要求(源素材+改动点·优化)", "前期成长目标演示：UE录屏打丧尸枪战实机，前3秒直接给枪战爽点（不是空镜），等级/装备成长字幕包装（LEVEL UP/+EQUIPMENT），验证丧尸/枪战题材吸量。低成本试点1条。", "")
add("吸睛逻辑", "前期目标方向（制作人储备方向）；玩家对枪战行为接受度高（新手调研）", "")
add("文案(英文配音)", "Day one: a rusty pistol. Day seven: the city remembers your name. 字幕条: LEVEL UP / +EQUIPMENT", "")
add("参考", "打丧尸玩法实机+受击特效", "")
add("", "", "")

add("━━ 视频⑤ V-擦边酒吧（谨慎试点）━━", "", "")
add("创意标准", "欲望（性暗示/禁忌）", "")
add("要求(源素材+改动点·优化)", "危险暧昧氛围素材：黑帮酒吧/夜店场景，霓虹+暗光+暧昧，前3秒用'若隐若现'的暧昧剪影立禁忌感（参考浴血黑帮入会仪式氛围）。试探性1条。⚠️Meta平台合规风险前置评估。", "")
add("吸睛逻辑", "禁忌感/窥探欲（浴血黑帮已验证的氛围吸量点）", "")
add("文案(英文配音)", "The best deals happen after midnight. Come inside.", "")
add("参考", "浴血黑帮氛围 + 酒吧喝酒动作", "")
add("", "", "")

add("━━ 视频⑥ V-模拟经营复测（放量·复测）━━", "", "")
add("创意标准", "代入/想玩（经营实录）", "")
add("要求(源素材+改动点·优化)", "模拟经营清洁复测（合并经营闭环演示）：基于7月 V-模拟经营 素材，新版重新录制并严格对齐实际玩法（升级→产出→回报可视化），经营成长线从破败小店到街区垄断完整演示。投放端固定FB版位（排除AN）、固定商店页（五图AB定稿后）、原版vs新版单变量对比。UE录屏+字幕包装。", "")
add("吸睛逻辑", "7月翻车根因=素材承诺未兑现（CVR腰斩-64.8%、25-44岁CVR从36-38%跌到12%）；本轮兑现经营反馈=修复素材与产品承接断层", "")
add("文案(英文配音)", "Build it. Run it. Own the block. 字幕条: UPGRADE → PRODUCTION → PROFIT", "")
add("参考", "7月 V-模拟经营原版/新版", "")
add("", "", "")

# ============ 分镜① 门徒收服（放量）============
add("━━ 分镜① V-门徒收服（放量）━━", "", "")
add("创意标准", "悬念(独子被绑)+欲望(收服权力)+视觉冲击(街头火并)", "")
add("核心卖点", "黑帮题材承诺（浴血公式）+ 门徒收服（商业化钩子）", "")
add("概述(剧情线)", "汤米·卡索独子被秃鹫帮当街羞辱绑走→熄雪茄拨电话集结门徒→街头火并碾压对方→对方老大跪地，'跪下，或者加入'收服为门徒→黑屏CTA", "")
add("角色定位", "汤米·卡索：45+意裔黑帮大佬，复古三件套+金表+雪茄，银灰鬓角（避开明星脸，AI原创）；秃鹫帮老大：40+光头彪悍皮夹克；门徒群像：西装打手/机车党/神枪手三类", "")

add("分镜一 开场+冲突 S0-S2(~9s)", "【强化点】前3秒立起'独子被绑'情感钩子。①首帧暗光酒吧全景，大字钩子 They took his son. ②汤米背身望窗外 ③秃鹫帮叫嚣信号弹划夜。制作=AI+AE(霓虹/字幕)", "参考浴血黑帮氛围")
add("　AI提示词(中)", "昏暗的复古黑帮酒吧内部，深色木质吧台和琥珀色暖光，雪茄烟雾缭绕，窗外是夜晚霓虹街景，一位穿复古三件套西装、银灰鬓角的黑帮大佬背身站在窗前，1940年代黑帮电影氛围，低调深沉的光影，电影剧照质感，不要任何文字。", "")
add("　AI提示词(英)", "Dim vintage mafia bar interior, dark wooden counter and amber warm light, swirling cigar smoke, night neon street view outside the window, a mafia boss in a vintage three-piece suit with silver-gray temples standing with his back to the window, 1940s gangster film atmosphere, low-key deep lighting, cinematic still quality, no text.", "")

add("分镜二 集结门徒 S3-S5(~10s)", "①汤米熄雪茄掏老式电话 ONE CALL ②门徒快切登场(3-4名风格各异) ③门徒大军集结压迫感。制作=AI(群像)+AE(集结BGM)", "复用招募表演公式")
add("　AI提示词(中)", "夜晚城市街道，一群纪律严明的黑帮门徒在酒吧门口集结列队，前排是穿笔挺黑西装的打手，旁边是骑着机车的皮衣墨镜党，还有披着风衣的狙击手，霓虹灯和车灯照亮街道，压迫感十足的低角度群像构图，电影感打光，不要任何文字。", "")
add("　AI提示词(英)", "Night city street, a group of disciplined mafia disciples assembling in formation outside the bar, front row of thugs in crisp black suits, leather-jacket sunglasses bikers on motorcycles beside them, a sniper in a trench coat, neon lights and headlights illuminating the street, oppressive low-angle group composition, cinematic lighting, no text.", "")

add("分镜三 街头火并 S6-S9(~12s)", "①西装大军碾压秃鹫地盘枪火爆炸 ②汤米缓步入场不奔跑(大佬气场) ③霓虹招牌被夺 THE EAST SIDE IS OURS。制作=AI+UE可替换+AE光效", "参考爽感战斗/浴血火并")
add("　AI提示词(中)", "夜晚城市街头的帮派枪战火并场面，穿黑西装的帮派大军端着枪推进，枪口火光和爆炸火花四溅，一名气场强大的黑帮大佬不慌不忙地走在战场中央，身后是燃烧的霓虹招牌，电影感动作大场面，高速摄影瞬间，高对比打光，不要任何文字。", "")
add("　AI提示词(英)", "Night city street gang gunfight scene, an army of black-suited gangsters advancing with guns, muzzle flashes and explosions sparking everywhere, a commanding mafia boss walking calmly through the center of the battlefield, burning neon signs behind him, cinematic action spectacle, high-speed photography moment, high-contrast lighting, no text.", "")

add("分镜四 收服结局 S10-S12(~10s)", "①秃鹫老大按跪在地 ②汤米俯视停顿 KNEEL. OR JOIN. ③收服动画(招募UI) PULL FOR MORE。制作=AI+AE(收服光效/UI)", "参考门徒招募UI")
add("　AI提示词(中)", "硝烟散去后的街头，一位败下阵来的光头黑帮老大被按住跪在地上，穿着西装的黑帮大佬居高临下俯视着他，俯视视角戏剧化打光，画面有权力感和仪式感，漫画电影风格，不要任何文字。", "")
add("　AI提示词(英)", "Street after the smoke clears, a defeated bald gang boss pinned down on his knees, a suited mafia boss looking down at him from above, high-angle dramatic lighting, a sense of power and ritual, comic-cinematic style, no text.", "")

add("分镜五 结尾卡 S13-S14(~4s)", "①黑屏打字机字幕 Run the city. / Recruit the family. ②Logo+商店/抽卡角标。制作=AE(字幕动效+结尾卡)", "参考7月结尾卡")
add("", "", "")

# ============ 分镜② 门徒抽卡（放量）============
add("━━ 分镜② V-门徒抽卡（放量）━━", "", "")
add("创意标准", "悬念(抽不抽)+欲望(抽卡赌博)", "")
add("核心卖点", "门徒抽卡（商业化核心），目标链：抽卡前知道想抽谁→抽到知道为什么值钱→抽到后知道用在哪", "")
add("概述(剧情线)", "主角攒十连钻石站招募台前犹豫→按下金光爆SSR'绯夜'→面板数据+人物背景塑造'为什么值钱'→上阵/经营/合体技展示'用在哪'→养成承诺→CTA", "")
add("角色定位", "绯夜Himena：日式女性门徒，深色和服+蛇纹刺青，冷艳（严格按立绘物料）；主角：年轻黑帮新秀休闲西装", "首充门徒/日式情人")

add("分镜一 招募台+犹豫 S0-S2(~8s)", "【强化点】前3秒立起'抽不抽'悬念。①招募界面钻石跳动 10 PULLS READY ②手指悬停特写颤抖 ③咬牙按下白光大爆。制作=UE(界面)+AE(数字动画)", "门徒招募UI录屏")
add("　AI提示词(中)", "手机游戏招募界面，主角站在神秘招募台前，屏幕上的钻石货币数字在跳动，按钮散发着紫色金色的光芒，气氛充满悬念和期待，二次元游戏UI风格，竖屏构图，不要任何文字。", "")
add("　AI提示词(英)", "Mobile game recruitment interface, the protagonist standing before a mysterious summoning platform, diamond currency numbers ticking on screen, a button glowing with purple and gold light, an atmosphere of suspense and anticipation, anime game UI style, vertical composition, no text.", "")

add("分镜二 十连抽卡 S3-S5(~10s)", "①十连卡面快速翻动 ②金光定格SSR剪影 S RARE—绯夜 ③屏幕震动抽出。制作=UE(抽卡动画)+AE(金光粒子)", "门徒抽卡动画录屏")
add("　AI提示词(中)", "二次元抽卡游戏的金光爆发瞬间，一张SSR卡牌在耀眼的金色光芒中缓缓浮现，卡面上是剪影轮廓，周围是飞舞的金色粒子特效，屏幕震动感，戏剧化的金光渲染，游戏UI风格，不要任何文字。", "")
add("　AI提示词(英)", "Golden light explosion moment in an anime gacha game, an SSR card slowly emerging from dazzling golden light, a silhouette on the card face, golden particle effects swirling around, screen-shake sensation, dramatic golden rendering, game UI style, no text.", "")

add("分镜三 为什么值钱 S6-S8(~10s)", "①绯夜华丽登场 HIMENA—SR THE ACE ②稀有度+面板数据快闪 TOP TIER STATS ③人物背景一句(旧蛇组王牌弃暗投明)。制作=AI(立绘)+AE(稀有度框/面板)", "首充门徒立绘")
add("　AI提示词(中)", "二次元游戏角色立绘，一位冷艳的日式风格黑帮女性门徒，身穿优雅深色和服，手臂和肩颈有若隐若现的蛇纹刺青，自信从容的站姿，SSR金色稀有度框围绕，戏剧化电影打光，精致人物细节，背景是暗色黑帮都市夜景霓虹，竖版构图，游戏卡面质感，不要任何文字。", "")
add("　AI提示词(英)", "Anime game character art, a coldly beautiful Japanese-style mafia female disciple in an elegant dark kimono, faint snake tattoos on her arms and shoulders, confident poised stance, framed by an SSR gold rarity border, dramatic cinematic lighting, exquisite detail, dark mafia city neon night background, vertical composition, game card art quality, no text.", "")

add("分镜四 用在哪 S9-S11(~12s)", "①上阵战斗大招 SHE FIGHTS ②经营加成收益上升 SHE EARNS ③养成升级武器拉满 SHE GROWS。制作=UE(实机)+AI(过场)+AE(字幕)", "爽感战斗+经营素材")
add("　AI提示词(中)", "二次元黑帮题材战斗演出，一位和服女性门徒释放强力大招，能量光效和技能特效在周围爆发，身后是城市夜景，电影感战斗构图，动作张力十足，不要任何文字。", "")
add("　AI提示词(英)", "Anime mafia-themed battle scene, a kimono-clad female disciple unleashing a powerful ultimate move, energy light and skill effects erupting around her, city nightscape behind her, cinematic battle composition, full of dynamic tension, no text.", "")

add("分镜五 结尾卡 S12-S13(~5s)", "①黑屏打字机 Pull for power. / She's waiting. ②Logo+招募/抽卡角标。制作=AE(字幕动效+结尾卡)", "参考7月结尾卡")

with open("D:/claude-projects/projects/GTS/rewrite_video_v2.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows([h2] + rows)
print("视频分镜 sheet 行数:", len(rows) + 1)
print("done video")
