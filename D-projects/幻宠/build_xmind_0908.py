# -*- coding: utf-8 -*-
"""生成 幻宠 9/8-9/11 次留/3留测试 camp 架构脑图 (.xmind)"""
import json
import uuid
import zipfile

OUT = r"D:\claude-projects\projects\幻宠\Palkie广告架构-9.8-9.11.xmind"


def tid(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:10]}"


def topic(title, style_id, children=None):
    t = {"id": tid("topic"), "class": "topic", "title": title, "style": {"id": style_id}}
    if children:
        t["children"] = {"attached": children}
    return t


def creative(title):
    return topic(title, "s-creative")


# ---------- 素材清单 ----------
C1_CREATIVES = [
    "P-宠物展示-融合恶搞",
    "P-宠物展示-融合炫酷",
    "P-宠物展示-融合擦边",
    "V-幽飘法庭剧情",
    "V-宠物展示-蹭超能勇士变身",
    "V-宠物展示-宠物进化蹭数码宝贝",
    "V-抓宠经营-砸蛋",
    "V-抓宠经营-售卖帕基改片头重口味",
]
C1_POKEMON = ["宝可梦图片1", "宝可梦图片2", "宝可梦视频1"]
C2_CREATIVES = ["P-宠物展示-合成3D", "P-抓宠经营-超梦", "V-宠物展示-宠物合成"]
C3_BATTLE = ["V-帕萌战斗-雪地竞品", "V-帕萌战斗-群殴打鸡", "V-抓宠战斗", "P-抓宠经营-幽飘"]
C3_SHOW = ["P-抓宠经营-超梦", "V-抓宠经营-捕捞竞品", "P-宠物展示-合3D", "P-宠物展示-二阶进化"]

# ---------- 4 个广告系列 ----------
camp1 = topic("广告系列1 · PALKIE-FB-Android-INSTALL-US-新素材方向", "s-camp", [
    topic("[参数] D1开启 · ABO · 11素材 @$5 · 550量=$2,750", "s-param"),
    topic("旧商店五图（8 adset · 每adset 50量=$250）", "s-group",
          [creative(x) for x in C1_CREATIVES]),
    topic("测宝可梦素材（3 adset · 每adset 50量=$250）", "s-group",
          [creative(x) for x in C1_POKEMON]),
])

camp2 = topic("广告系列2 · PALKIE-FB-Android-INSTALL-US-商店图AB", "s-camp", [
    topic("[参数] D1开启 · ABO · 200量 @$5 = $1,000 · 素材相同仅商店五图不同", "s-param"),
    topic("新商店图（1 adset）", "s-group", [creative(x) for x in C2_CREATIVES]),
    topic("旧商店图（1 adset）", "s-group", [creative(x) for x in C2_CREATIVES]),
])

camp3 = topic("广告系列3 · PALKIE-FB-Android-INSTALL-US-主买量", "s-camp", [
    topic("[参数] D1开启 · CBO · 700量 @$5 = $3,500 · 老素材（上次测试验证）", "s-param"),
    topic("Adset 战斗方向", "s-group", [creative(x) for x in C3_BATTLE]),
    topic("Adset 宠物展示方向", "s-group", [creative(x) for x in C3_SHOW]),
])

camp4 = topic("广告系列4 · PALKIE-FB-Android-AEO-US-留存", "s-camp", [
    topic("[参数] D2开启 · AEO（aeo留存）· 700量 @$8 = $5,600 · 1 adset", "s-param"),
    topic("Adset aeo留存-XX（1个adset）", "s-group", [
        topic("优胜素材 · 待D1筛选（取自 C1/C2/C3 优胜）", "s-placeholder"),
    ]),
])

# ---------- US 下总览标注 + 各 camp ----------
overview = [
    topic("[总览] Meta Ads · 9/8-9/11 · KPI: 次留(D1)/3留(D3) · 单服 2,000人", "s-param"),
    topic("[预算] 总 $13,000 · 审批上限 $15,000 · 预留空间", "s-param"),
    topic("[量级] 4 camp 合计 2,150 · 预估花费 $12,850 · 超单服2,000需注意", "s-param"),
]

us = topic("US", "s-lv1", overview + [camp1, camp2, camp3, camp4])
android = topic("Android", "s-lv1", [us])

root = topic("Palkie广告架构 9/8-9/11", "s-center", [android])
root["structureClass"] = "org.xmind.ui.logic.right"

# ---------- sheet / content ----------
sheet_id = tid("sheet")
content = [{
    "id": sheet_id,
    "class": "sheet",
    "title": "Palkie广告架构 9/8-9/11",
    "coreVersion": "3.0",
    "rev": 1,
    "rootTopic": root,
}]

styles = [
    {"id": "s-center", "type": "topic", "properties": {
        "fo:color": "#FFFFFF", "fo:font-size": "18pt", "fo:font-weight": "bold",
        "svg:fill": "#2E75B6", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-lv1", "type": "topic", "properties": {
        "fo:color": "#1F1F1F", "fo:font-size": "13pt", "fo:font-weight": "bold",
        "svg:fill": "#BFBFBF", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-camp", "type": "topic", "properties": {
        "fo:color": "#1F1F1F", "fo:font-size": "12pt", "fo:font-weight": "bold",
        "svg:fill": "#D9D9D9", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-group", "type": "topic", "properties": {
        "fo:color": "#1F1F1F", "fo:font-size": "11pt", "fo:font-weight": "bold",
        "svg:fill": "#EDEDED", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-param", "type": "topic", "properties": {
        "fo:color": "#C55A11", "fo:font-size": "10pt", "fo:font-style": "italic",
        "svg:fill": "#FDEBD0", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-creative", "type": "topic", "properties": {
        "fo:color": "#1F1F1F", "fo:font-size": "10pt",
        "svg:fill": "#FFFFFF", "shape-class": "org.xmind.topicShape.roundedRect"}},
    {"id": "s-placeholder", "type": "topic", "properties": {
        "fo:color": "#808080", "fo:font-size": "10pt", "fo:font-style": "italic",
        "svg:fill": "#FAFAFA", "shape-class": "org.xmind.topicShape.roundedRect"}},
]

metadata = {
    "creator": {"name": "XMind", "version": "23.11.6538"},
    "metadata": [{"metadata-id": "default", "o:default-rev": 1}],
}

manifest = {
    "file-entries": [
        {"full-path": "content.json", "media-type": "application/json"},
        {"full-path": "metadata.json", "media-type": "application/json"},
        {"full-path": "styles.json", "media-type": "application/json"},
    ]
}

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for name, obj in [("content.json", content), ("metadata.json", metadata),
                      ("styles.json", styles), ("manifest.json", manifest)]:
        data = json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8")
        z.writestr(name, data)

# ---------- 校验 ----------
with zipfile.ZipFile(OUT, "r") as z:
    names = z.namelist()
    for name in ["content.json", "metadata.json", "styles.json", "manifest.json"]:
        assert name in names, f"missing {name}"
        json.loads(z.read(name).decode("utf-8"))
    print("zip entries:", names)
    print("valid json: OK")

# 统计节点
def count(topics):
    n = 0
    for t in topics:
        n += 1
        if "children" in t:
            n += count(t["children"]["attached"])
    return n

print("总节点数:", count([root]))
print("输出文件:", OUT)
