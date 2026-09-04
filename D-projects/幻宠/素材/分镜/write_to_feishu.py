# -*- coding: utf-8 -*-
"""Prepare PET COURT storyboard data and write to Feishu spreadsheet"""

import json, subprocess, sys, io

TOKEN = "LbOEwi3q5ivsAMkA45JcJbtXnac"
SHEET_ID = "WE2gvc"

# ========================================
# Build cell data in UA script format
# ========================================

NUM_COLS = 14

def pad_row(cells, n=NUM_COLS):
    """Ensure row has exactly n cells"""
    while len(cells) < n:
        cells.append({"value": ""})
    return cells[:n]

rows = []

# --- Row 1: Project header ---
rows.append(pad_row([
    {"value": "需求人"},
    {"value": "孔祥建（投放/UA）"},
    {"value": "核心卖点"},
    {"value": "宠物抚养权法庭parody + 三层反转 + 机制punchline"},
    {"value": "目标受众"},
    {"value": "美国18-45岁SLG玩家"},
    {"value": "视频尺寸"},
    {"value": "720*1280"},
    {"value": "视频时长"},
    {"value": "50s（可剪30s/15s短版）"},
    {"value": "参考图"},
    {"value": "本地: 分镜参考素材/（15组AI参考图已生成）"},
    {"value": "备注"},
    {"value": "咒语: Everyone's catchable. | CTA双版AB测试"},
]))

# --- Row 2: Audio/sub-header ---
rows.append(pad_row([
    {"value": "口播要求"},
    {"value": "英文配音+英文字幕（75%静音用户对策：关键信息全部字幕覆盖）"},
    {"value": "BGM"},
    {"value": "法庭真人秀风铜管stinger→悬疑弦乐铺底→轻快上扬收尾（原创罐头授权，禁sound-alike）"},
    {"value": "音效/特效要求"},
    {"value": "法槌x3 + 捕捉吸入(buzhuo1/游戏原声) + 读条(buzhuo2/游戏原声) + 闭合震动+原创确认音(battle_win变调或音效库)"},
    {"value": "备注"},
    {"value": "合规：AIGC标注/结尾Dramatization声明/法官避开Sheindlin特征/文档禁出现'Judge Judy''Pokémon'"},
]))

# --- Storyboards (S0-S15 = 16 scenes) ---
storyboards = [
    ("分镜一 S0 首帧钩子（3s）",
     "DCC(幽飘FBX) + AE(片头包装)\n"
     "首帧即法庭全景: 深木色调+金色法徽（原创设计，嵌捕捉球剪影替代传统鹰徽）+字幕条\n"
     "中央大字钩子: They agree on everything... except ONE.\n"
     "字幕条: CASE #4847 — Thompson v. Thompson\n"
     "制作原因: 75%静音用户刷feed，黑屏钩子无效。首帧必须有画面+文字双钩子。法徽原创=品牌记忆点\n"
     "参考: 本地 美式法庭全景(带法徽).png + 法庭片头包装(法徽+字幕条).png"),

    ("分镜二 S1 法官开场（3s）",
     "AI(法官表演)\n"
     "法官(50+女性，灰白短发，犀利眼神，黑法官袍+白领——主动避开Sheindlin签名特征)看着卷宗抬眼\n"
     "台词: 'The Thompsons are divorcing. House, car, money — settled. They agree on EVERYTHING... except one thing.'\n"
     "制作原因: 排比句强化真人秀开场腔; except one thing悬念钩子\n"
     "参考: 本地 法官定妆参考图.png"),

    ("分镜三 S2 幽飘登场（3s）",
     "DCC(幽飘FBX渲染→领结AE贴合) + AE(合成进AI场景+接触阴影+统一胶片LUT)\n"
     "镜头缓缓推向当事人席——幽飘端坐大木椅上，戴小领结，眼神无辜，耳朵轻抖\n"
     "人类夫妻站立场边讲台（符合法庭秀格式）\n"
     "无台词。观众席窃语渐起+滑稽高音弦乐\n"
     "★本镜头为Pipeline Test镜头，先做通再批量\n"
     "资产: 幽飘模型 Y:/.../木少女一阶10111/mod_10111_high.fbx | 立绘: 帕基截图/11【幽飘】10111WoodGril.png\n"
     "参考: 本地 幽飘(可爱生物)参考.png"),

    ("分镜四 S3 妻子控诉（6s）",
     "AI(妻子表演——ice-cold冷怒毒舌，不哭闹)\n"
     "妻子(30+，精致海军蓝西装，深发低马尾)首次开口，砸名牌字幕条\n"
     "字幕条: KAREN THOMPSON — Plaintiff\n"
     "台词: 'Your Honor — he used her as FUSION FODDER. I HATCHED her. I was there for her first evolution... and he tried to feed her to a FUSION MACHINE.'\n"
     "★v3重写: 原COMMON berries+0.01% spawn rate虚构了游戏不存在的机制，改为孵化+进化+融合三个真实机制\n"
     "参考: 本地 妻子(Karen Thompson)定妆.png"),

    ("分镜五 S4 观众反应（1s）",
     "AI(群演)\n观众席大妈捂嘴倒吸凉气。整齐倒吸气声\n无台词\n"
     "制作原因: 反应镜头是真人秀节奏的呼吸点\n参考: 本地 法庭观众席反应(多样性).png"),

    ("分镜六 S5 丈夫反击（5s）",
     "AI(丈夫表演——委屈爆发，拍桌而起)\n"
     "丈夫(30+，格子衫+卷袖，松开领带)首次开口，砸名牌字幕条\n"
     "字幕条: DOUG THOMPSON — Defendant\n"
     "台词: 'I was THERE when she evolved! THREE A.M.! Where were YOU?! Oh, right — BOOK CLUB.'\n"
     "拍桌+观众爆笑。全片最地道一句(本地化原话)\n"
     "参考: 本地 丈夫(Doug Thompson)定妆.png"),

    ("分镜七 S6 观众爆笑（1s）",
     "AI(群演)\n观众爆笑，一人拍腿。观众爆笑+拍腿声\n"
     "制作原因: OHHHH起哄偏另一档节目风格，爆笑更贴法庭秀"),

    ("分镜八 S7 法官裁决（5s）",
     "AI(法官)\n法官连敲法槌，全场安静，法官看向下方幽飘\n"
     "台词: 'ENOUGH. I have ONE ruling... the creature CHOOSES.'\n"
     "槌声后全场骤静，低音提琴紧张铺底起\n"
     "★v3改: 原This court has不是法官说话方式，改第一人称I have\n"
     "参考: 本地 法官正面特写(法槌时刻).png"),

    ("分镜九 S8 三方特写快切（2s）",
     "AI(人类特写) + DCC(幽飘特写) + AE(屏幕文字)\n"
     "妻子期待脸→丈夫咽口水→幽飘面无表情。心跳声渐强\n"
     "屏幕文字: Who will it choose?\n"
     "★v3压缩: S8-S10原10s无台词压至6s，加屏幕文字留驻静音用户"),

    ("分镜十 S9 幽飘走向法庭中央（2s）",
     "DCC(幽飘move动作，速度可调) + AE(合成)\n"
     "幽飘跳下椅子，小短腿走向法庭中央。放大脚步声+滑稽配乐点\n"
     "★v3: 砍慢镜头(付费流量大忌)，正常速度\n"
     "参考: 本地 幽飘走向法庭中央(全身).png"),

    ("分镜十一 S10 抉择瞬间（2s）",
     "DCC(幽飘头部动画，idle基础上手K转头) + AE\n"
     "幽飘抬头看妻子(特写)→转头看丈夫(特写)→停顿半秒\n"
     "音乐戛然抽空，只剩环境底噪\n"
     "参考: 本地 幽飘正面面部特写.png"),

    ("分镜十二 S11 掏球转身（4s）",
     "DCC(幽飘转身，手K举球转身而非掏球) + AE(球道具+合成) + AI(单人反应特写x3)\n"
     "幽飘转身——0.3s身体遮挡帧中捕捉球出现于爪中——继续转身对准法官席\n"
     "全场凝固拆为2-3个单人反应特写快切(规避多角色同框脸漂移)\n"
     "★v3改: 无掏球动作且小短腿掏背后必穿模，遮挡剪辑是影视魔术标准cheat\n"
     "参考: 本地 捕捉球道具设计参考.png"),

    ("分镜十三 S12 收服法官（4s）",
     "AE(吸入光效+法官消散粒子+读条UI+球体震动) + AI(法官冻结帧)\n"
     "光束从球中卷出→包裹法官→吸入球中(AI冻结帧+AE粒子消散)→读条UI闪现→球体闭合震动一次\n"
     "★v3核心修改: 弃用晃三下+叮(任天堂trade dress高风险)，改用游戏真实收服表现(吸入+读条)\n"
     "音效: buzhuo1→buzhuo2→原创确认音 | 场景生成阶段必须同步输出无法官空景\n"
     "参考: 本地 法庭空景(无法官).png"),

    ("分镜十四 S13 法警补刀（4s）",
     "AI(法警) + AE(球道具)\n"
     "死寂中法警缓缓站起，面无表情，从腰带解下自己的捕捉球\n"
     "台词: '...Everyone's catchable.' (停顿一拍) 'Court's adjourned.'\n"
     "法警低音独白+尾音低沉鼓点。deadpan补刀=全片记忆点\n"
     "★v3新增: Court's adjourned回收法庭格式再叠一层笑点\n"
     "参考: 本地 法警(Bailiff)定妆.png"),

    ("分镜十五 S14 黑屏字幕（2s）",
     "AE(字幕动效)\n硬切黑屏，白色打字机字体逐行砸出\n"
     "字幕: Catch pets. Catch feelings. Catch... everyone.\n"
     "每行字幕配打字机敲击声\n"
     "★v3改: 原Catch bosses/everything无机制支撑，改玩笑语气+callback法官被收\n"
     "参考: 本地 结尾黑屏字幕风格参考.png"),

    ("分镜十六 S15 结尾卡（3s）",
     "AE(结尾卡) + 游戏UI截图\n"
     "0-1.5s: 游戏捕捉界面UI定格(看得清这是手游)\n"
     "1.5-3s: Logo+下载按钮+CTA\n"
     "CTA A版: Who Will You Catch First? / B版: Your SSR Is Waiting — Play Free\n"
     "底部小字: Dramatization. Not actual gameplay footage.\n"
     "★v3改: UI露出从0.5s延长到1.5s(低于识别阈值); CTA双版AB测试\n"
     "资产: UI/C_宠物捕捉.psd + Logo需向发行/美术索取"),
]

for title, content in storyboards:
    rows.append(pad_row([{"value": title}]))
    rows.append(pad_row([{"value": content}]))

# ========================================
# Write to Feishu
# ========================================
range_end = len(rows)
range_str = f"A1:N{range_end}"

# Save cells as JSON file for lark-cli
json_path = r"D:\claude-projects\projects\幻宠\素材\分镜\feishu_cells.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

print(f"Prepared {len(rows)} rows for range {range_str}")
print(f"JSON saved to: {json_path}")

# Write using lark-cli
cmd = [
    "lark-cli", "sheets", "+cells-set",
    "--spreadsheet-token", TOKEN,
    "--sheet-id", SHEET_ID,
    "--range", range_str,
    "--cells", f"@{json_path}",
    "--format", "json"
]

print("Writing to Feishu...")
result = subprocess.run(cmd, capture_output=True, text=True)

print("STDOUT:", result.stdout[:500] if result.stdout else "")
if result.stderr:
    print("STDERR:", result.stderr[:500])
print("Return code:", result.returncode)
