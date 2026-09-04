# -*- coding: utf-8 -*-
import json, uuid, zipfile, io

def nid():
    return str(uuid.uuid4())

def build_topic(title, children=None):
    t = {"id": nid(), "title": title}
    if children:
        t["children"] = {"attached": [build_topic(c, cc) for c, cc in children]}
    return t

def build_sheet(title, root_children):
    sid = nid()
    sheet = {
        "id": sid,
        "revisionId": nid(),
        "class": "sheet",
        "title": title,
        "rootTopic": {
            "id": nid(),
            "class": "topic",
            "title": title,
            "titleUnedited": False,
            "structureClass": "org.xmind.ui.map.clockwise",
            "children": {"attached": [build_topic(c, cc) for c, cc in root_children]},
        },
    }
    return sid, sheet

# ============ Sheet 1: 方案A 纯留存 ============
sheetA_title = "GTS广告架构 · 方案A 纯留存（9/17-9/19）"
sheetA_children = [
    ("Android", [
        ("美国", [
            ("Camp1 · INSTALL-US 视频主导量（CBO $4,050 · 保留AN）", [
                ("黑帮入会/氛围：V-浴血黑帮 + V-浴血黑帮-叙事迭代", None),
                ("角色展示/招募：V-招募表演 + V-立绘展示-斩神片头", None),
                ("复仇逆袭：V-晋级失败被捕 + V-无厘头擦边", None),
                ("战斗：V-玩法展示-打丧尸 + V-鸡公大侠", None),
            ]),
            ("Camp2 · INSTALL-US 图片主导量（CBO $2,700 · 保留AN）", [
                ("角色展示：P-门徒立绘-单人 + P-门徒立绘-多人", None),
                ("美漫分镜：P-美漫分镜 + 帮派火并 + 地盘争夺", None),
                ("幽默经营：P-炸鸡店 + P-披萨店 + P-炸鸡店迭代", None),
                ("擦边/命运反转：P-黑帮经营-擦边 + P-美漫分镜-角色升级", None),
            ]),
            ("Camp3 · INSTALL-US 清洁复测（ABO $750 · 剔除AN）", [
                ("V-模拟经营原版（4月明星/7月翻车）", None),
                ("V-爽感战斗（D1异常排查）", None),
                ("V-特殊设备视角（D3复现）", None),
            ]),
        ]),
    ]),
]

# ============ Sheet 2: 方案B 留存+付费 ============
sheetB_title = "GTS广告架构 · 方案B 留存+付费（9/17-9/20）"
sheetB_children = [
    ("Android", [
        ("美国", [
            ("Camp1 · INSTALL-US 主导量（CBO $2,250 · 保留AN）", [
                ("黑帮入会/氛围：V-浴血黑帮 + V-浴血黑帮-叙事迭代", None),
                ("角色展示/招募：V-招募表演 + V-斩神片头 + P-门徒立绘×2", None),
                ("命运反转/美漫：V-晋级失败 + P-美漫-角色升级 + P-美漫分镜 + 帮派火并 + 地盘争夺", None),
                ("幽默经营：P-炸鸡店 + P-披萨店 + P-炸鸡店迭代", None),
                ("战斗：V-玩法展示-打丧尸 + V-鸡公大侠", None),
                ("擦边：V-无厘头擦边 + P-黑帮经营-擦边", None),
            ]),
            ("Camp2 · AEO付费-US（CBO $6,000 · Day2-4 开启）", [
                ("素材 Day1 美国 Install 数据动态筛出（3-4 支）", [
                    ("筛选：CPI≤$4.0 + 量级≥30 DNU", None),
                    ("方向付费潜力：经营/角色/氛围 > 战斗/恶搞/擦边", None),
                    ("图片也可入选（不预判）", None),
                ]),
            ]),
            ("Camp3 · INSTALL-US 清洁复测（ABO $750 · 剔除AN）", [
                ("V-模拟经营原版（4月明星/7月翻车）", None),
                ("V-爽感战斗（D1异常排查）", None),
                ("V-特殊设备视角（D3复现）", None),
            ]),
        ]),
        ("菲律宾", [
            ("Camp4 · INSTALL-PH 陪玩（CBO $750 · 保留AN）", [
                ("4 组陪玩", [
                    ("主力素材（复用赢家）", None),
                    ("新素材探索", None),
                    ("图片低成本组", None),
                    ("备选组", None),
                ]),
            ]),
        ]),
    ]),
]

sidA, sheetA = build_sheet(sheetA_title, sheetA_children)
sidB, sheetB = build_sheet(sheetB_title, sheetB_children)

content = [sheetA, sheetB]

metadata = {
    "dataStructureVersion": "3",
    "creator": {"name": "Claude", "version": "1.0.0"},
    "activeSheetId": sidA,
    "layoutEngineVersion": "5",
}

manifest = {
    "file-entries": {
        "content.json": {},
        "metadata.json": {},
    }
}

def enc(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8")

out = r"D:\claude-projects\projects\GTS\GTS广告架构-9月测试.xmind"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("content.json", enc(content))
    z.writestr("metadata.json", enc(metadata))
    z.writestr("manifest.json", enc(manifest))

print("WROTE", out)
