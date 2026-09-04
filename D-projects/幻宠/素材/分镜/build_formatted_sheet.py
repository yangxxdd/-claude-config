# -*- coding: utf-8 -*-
"""Build formatted PET COURT sheet matching UA script style"""

import json, subprocess, sys, os

TOKEN = "LbOEwi3q5ivsAMkA45JcJbtXnac"
SHEET_ID = "XXTIdQ"
NUM_COLS = 14  # A-N

# Styles
GRAY_BG = "rgb(216,216,216)"
HDR_STYLE = {
    "background_color": GRAY_BG,
    "font_weight": "bold",
    "font_size": 13,
    "horizontal_alignment": "center",
    "vertical_alignment": "middle",
}
NORMAL_STYLE = {
    "font_size": 13,
    "vertical_alignment": "middle",
}
TITLE_STYLE = {
    "background_color": GRAY_BG,
    "font_weight": "bold",
    "font_size": 13,
    "vertical_alignment": "middle",
}

def hdr(v):
    """Gray header label cell"""
    return {"value": v, "cell_styles": dict(HDR_STYLE)}

def val(v, wrap=True):
    """Normal value cell"""
    s = dict(NORMAL_STYLE)
    if wrap:
        s["wrap_text"] = True
    return {"value": v, "cell_styles": s}

def title(v):
    """Storyboard title cell (gray bg)"""
    return {"value": v, "cell_styles": dict(TITLE_STYLE)}

def empty():
    return {"value": "", "cell_styles": dict(NORMAL_STYLE)}

def pad(row, n=NUM_COLS):
    while len(row) < n:
        row.append(empty())
    return row[:n]

rows = []

# ===== ROW 1: Project Header =====
rows.append(pad([
    hdr("需求人"), val("孔祥建（投放/UA）"),
    hdr("核心卖点"), val("宠物抚养权法庭parody · 三层反转 · 机制punchline"),
    hdr("目标受众"), val("美国18-45岁SLG玩家"),
    hdr("视频尺寸"), val("720*1280"),
    hdr("视频时长"), val("~50s（可剪30s/15s版）"),
    hdr("参考图"), val("本地: 分镜参考素材/（15组AI已生成）"),
    hdr("备注"), val("咒语: Everyone's catchable. | CTA双版AB测试 | 合规: AIGC标注+结尾Dramatization声明"),
]))

# ===== ROW 2: Audio/Sub-header =====
rows.append(pad([
    hdr("口播要求"), val("英文配音+英文字幕（75%静音用户对策：关键信息全部字幕覆盖）"),
    hdr("BGM"), val("法庭真人秀风铜管stinger→悬疑弦乐铺底→轻快上扬收尾（原创罐头授权，禁sound-alike）"),
    hdr("音效/特效"), val("法槌x3 + 捕捉吸入(buzhuo1/游戏原声) + 读条(buzhuo2/游戏原声) + 闭合震动+原创确认音(battle_win变调或音效库)"),
    hdr("参考视频"), val("竞品: Last Asylum_Plague(吸血鬼城镇BGM参考) / Guns of Glory_Lost Island(角色造型) / Game of Vampires_Twilight Sun(交互格式)"),
    hdr("资产警示"), val("幽飘模型目录含'宝可梦'字样→进制作前必须核实来源；Logo需向发行/美术索取"),
]))

# ===== 5 STORYBOARDS =====
storyboards = [
    ("分镜一：开场钩子 + 幽飘登场", "S0-S2（~9s）",
     """【制作】AI(法庭场景+法官) + AE(片头包装) + DCC(幽飘FBX渲染) → 本镜为Pipeline Test镜头

【画面】
① 首帧即法庭全景：深木色调+金色法徽（原创，嵌捕捉球剪影替代鹰徽）+ 大字钩子覆盖全屏
   字幕条: CASE #4847 — Thompson v. Thompson
   大字钩子: They agree on everything... except ONE.
② 法官(50+女性，灰白短发，黑法官袍+白领——主动避开Sheindlin特征)看卷宗抬眼
   台词: "The Thompsons are divorcing. House, car, money — settled. They agree on EVERYTHING... except one thing."
③ 镜头缓缓推向当事人席——幽飘端坐大木椅上，戴小领结，眼神无辜，耳朵轻抖。人类夫妻站两边讲台。
   无台词。观众席窃语渐起+滑稽高音弦乐。

【参考图】本地 美式法庭全景(带法徽).png + 法庭片头包装(法徽+字幕条).png + 法官定妆参考图.png + 幽飘(可爱生物)参考.png
【资产】幽飘模型 Y:/.../木少女一阶10111/mod_10111_high.fbx | 立绘: 帕基截图/11【幽飘】10111WoodGril.png"""),

    ("分镜二：法庭对决（妻控诉 → 夫反击）", "S3-S6（~12s）",
     """【制作】AI(妻子+丈夫+群演) → 人类角色全部AI生成，配音+口型同步两步走

【画面】
① 妻子站起(ice-cold冷怒，不哭闹！)，砸名牌字幕条: KAREN THOMPSON — Plaintiff
   台词: "Your Honor — he used her as FUSION FODDER. I HATCHED her. I was there for her first evolution... and he tried to feed her to a FUSION MACHINE."
   背景观众低声惊呼
② 观众席大妈捂嘴倒吸凉气。整齐倒吸气声
③ 丈夫拍桌而起(委屈爆发)，砸名牌字幕条: DOUG THOMPSON — Defendant
   台词: "I was THERE when she evolved! THREE A.M.! Where were YOU?! Oh, right — BOOK CLUB."
   观众爆笑+拍腿声
★ 孵化/进化/融合=三个真实游戏机制（弃用虚构的喂食+刷新率）。全片最地道一句(本地化原话): THREE A.M. + BOOK CLUB

【参考图】本地 妻子(Karen Thompson)定妆.png + 丈夫(Doug Thompson)定妆.png + 法庭观众席反应(多样性).png"""),

    ("分镜三：法官裁决 + 选择悬念", "S7-S10（~11s）",
     """【制作】AI(法官) + DCC(幽飘) + AE(屏幕文字)

【画面】
① 法官连敲法槌，全场安静，看向幽飘
   台词: "ENOUGH. I have ONE ruling... the creature CHOOSES."
   槌声后骤静，低音提琴紧张铺底
② 三方特写快切: 妻子期待脸→丈夫咽口水→幽飘面无表情
   屏幕文字: Who will it choose?  心跳声渐强
③ 幽飘跳下椅子，小短腿走向法庭中央（正常速度，不用慢镜头！）。放大脚步声+滑稽配乐
④ 幽飘抬头看妻子(特写)→转头看丈夫(特写)→停顿半秒。音乐戛然抽空，只剩环境底噪

★ v3关键修改: 'This court has'改第一人称'I have'; S8-S10原10s无台词压至6s+屏幕文字(静音用户对策)

【参考图】本地 法官正面特写(法槌时刻).png + 幽飘正面面部特写.png + 幽飘走向法庭中央(全身).png"""),

    ("分镜四：收服法官 + 法警补刀（全片高潮）", "S11-S13（~12s）",
     """【制作】DCC(幽飘转身+举球) + AE(球道具+吸入光效+法官消散粒子+读条UI+球体震动) + AI(法警+单人反应特写)

【画面】
① 幽飘转身——0.3s身体遮挡帧中捕捉球出现于爪中——继续转身对准法官席
   全场凝固拆为2-3个单人反应特写快切(规避多角色同框AI脸漂移)
   所有音乐抽空+球体机械轻响
② 光束从球中卷出→包裹法官(卡通光效，不做痛苦挣扎)→吸入球中(AI冻结帧+AE粒子消散)→读条UI闪现→球体闭合震动一次
   音效: buzhuo1(吸入)→buzhuo2(读条)→闭合+原创确认音(battle_win变调或音效库)
③ 死寂中法警缓缓站起，面无表情，从腰带解下自己的捕捉球
   台词: "...Everyone's catchable." (停顿一拍) "Court's adjourned."
   法警低音独白+尾音鼓点。全片记忆点。

★ v3核心修改: ①弃用晃三下+叮(任天堂trade dress)→游戏真实收服(吸入+读条); ②遮挡剪辑替代掏球(无资产+穿模); ③法官消散必须有空景; ④Court's adjourned回收法庭格式叠笑点

【参考图】本地 捕捉球道具设计参考.png + 法庭空景(无法官).png + 法警(Bailiff)定妆.png
【音效资产】Y:/.../Audios/audio_sfx_buzhuo1.mp3 + audio_sfx_buzhuo2.mp3 + audio_sfx_battle_win.mp3"""),

    ("分镜五：结尾卡 + CTA", "S14-S15（~5s）",
     """【制作】AE(字幕动效+结尾卡) + 游戏UI截图

【画面】
① 硬切黑屏，白色打字机字体逐行砸出（每行配打字机敲击声）
   字幕: Catch pets. Catch feelings. Catch... everyone.（末行everyone稍大）
② 游戏捕捉界面UI定格1.5s（看得清这是手游）→ Logo + 下载按钮 + CTA
   CTA A版: Who Will You Catch First?
   CTA B版: Your SSR Is Waiting — Play Free
   底部全程小字: Dramatization. Not actual gameplay footage.

★ v3修改: UI露出从0.5s→1.5s(低于识别阈值修正); 原Catch bosses/everything无机制支撑→改玩笑语气; CTA双版AB测试; 免责声明=FTC减责+平台申诉筹码

【资产】UI/C_宠物捕捉.psd（2.08GB，提前预留提取时间）| Logo: 需向发行/美术索取正式文件（不在图标发行PNG12.3/里）
【参考图】本地 结尾黑屏字幕风格参考.png"""),
]

for sbtitle, timing, content in storyboards:
    # Title row: A=title gray bg, B-N=merged with timing
    rows.append(pad([title(sbtitle), val(timing)]))
    # Content row: A=empty, B-N=merged with full content
    rows.append(pad([empty(), val(content)]))

# ===== Write to JSON =====
json_path = "feishu_formatted.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

range_end = len(rows)
range_str = f"A1:N{range_end}"
print(f"Total rows: {range_end}")
print(f"Range: {range_str}")
print(f"JSON: {json_path}")

# Write cells
result = subprocess.run([
    "lark-cli", "sheets", "+cells-set",
    "--spreadsheet-token", TOKEN,
    "--sheet-id", SHEET_ID,
    "--range", range_str,
    "--cells", f"@{json_path}",
    "--format", "json"
], capture_output=True, text=True, cwd=r"D:\claude-projects\projects\幻宠\素材\分镜")
print("Write:", result.stdout[:300] if result.stdout else result.stderr[:300])

# ===== Apply Merges =====
# Merge plan: storyboard title rows = B-N merged; content rows = B-N merged
merges = []
for i, (sbtitle, timing, content) in enumerate(storyboards):
    title_row = 3 + i * 2  # rows 3,5,7,9,11
    content_row = title_row + 1  # rows 4,6,8,10,12
    # Merge title row B-N
    merges.append(f"B{title_row}:N{title_row}")
    # Merge content row B-N
    merges.append(f"B{content_row}:N{content_row}")

# Also merge header rows where needed
merges.append("D1:G1")   # 核心卖点描述
merges.append("B2:D2")   # 口播要求
merges.append("D2:F2")   # BGM描述
merges.append("H2:J2")   # 音效
merges.append("K2:L2")   # 参考视频

for m in merges:
    r = subprocess.run([
        "lark-cli", "sheets", "+cells-merge",
        "--spreadsheet-token", TOKEN,
        "--sheet-id", SHEET_ID,
        "--range", m,
        "--format", "json"
    ], capture_output=True, text=True, cwd=r"D:\claude-projects\projects\幻宠\素材\分镜")
    ok = "ok" if "ok" in (r.stdout[:100] if r.stdout else "") else f"FAIL({r.stderr[:100] if r.stderr else ''})"
    print(f"  Merge {m}: {ok}")

print("\nDONE! Sheet ID:", SHEET_ID)
print("URL: https://my.feishu.cn/wiki/LbOEwi3q5ivsAMkA45JcJbtXnac")
