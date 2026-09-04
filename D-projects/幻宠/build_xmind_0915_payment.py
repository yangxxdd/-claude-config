# -*- coding: utf-8 -*-
"""生成 幻宠 9/15-9/18 第二阶段付费测试 camp 架构脑图 (.xmind)"""
import json
import uuid
import zipfile

OUT = r"D:\claude-projects\projects\幻宠\Palkie广告架构-付费测试-9.15-9.18.xmind"


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
OLD_MATERIALS = [  # 6月确认复用的优秀素材
    "V-帕萌战斗-雪地竞品",
    "V-帕萌战斗-群殴打鸡",
    "V-抓宠战斗",
    "P-抓宠经营-幽飘",
    "P-抓宠经营-超梦",
    "V-抓宠经营-捕捞竞品",
    "P-宠物展示-合3D",
    "P-宠物展示-二阶进化",
]
NEW_MATERIALS = [  # 新制作脚本素材
    "P-宠物展示-融合恶搞",
    "P-宠物展示-融合炫酷",
    "P-宠物展示-融合擦边",
    "V-幽飘法庭剧情",
    "V-宠物展示-蹭超能勇士变身",
    "V-宠物展示-宠物进化蹭数码宝贝",
    "V-抓宠经营-砸蛋",
    "V-抓宠经营-售卖帕基改片头重口味",
]


# ---------- C1: PH 拉低价格 ----------
camp1 = topic("广告系列1 · PALKIE-FB-Android-INSTALL-PH-拉低价格", "s-camp", [
    topic("[参数] D1开启 · ABO · 2 adset · 6,000量 @$1 = $6,000", "s-param"),
    topic("Adset · 旧素材组（3,000量 @$1）", "s-group",
          [creative(x) for x in OLD_MATERIALS]),
    topic("Adset · 新制作脚本组（3,000量 @$1）", "s-group",
          [creative(x) for x in NEW_MATERIALS]),
])

# ---------- C2: MX/BR/ID 拉低价格 ----------
camp2 = topic("广告系列2 · PALKIE-FB-Android-INSTALL-MX/BR/ID-拉低价格", "s-camp", [
    topic("[参数] D1开启 · ABO · 2 adset · 1,000量 @$1 = $1,000 · 三国混跑", "s-param"),
    topic("Adset · 旧素材组（500量 @$1）", "s-group",
          [creative(x) for x in OLD_MATERIALS]),
    topic("Adset · 新制作脚本组（500量 @$1）", "s-group",
          [creative(x) for x in NEW_MATERIALS]),
])

# ---------- C3: US Install 测付费率 ----------
camp3 = topic("广告系列3 · PALKIE-FB-Android-INSTALL-US-测付费率", "s-camp", [
    topic("[参数] D1开启 · 1 adset · 1,000量 @$5 = $5,000 · 一阶段优胜素材", "s-param"),
    topic("Adset · 一阶段优胜素材-XX（1个adset）", "s-group", [
        topic("优胜素材 · 待 9/8-9/11 一阶段筛选", "s-placeholder"),
    ]),
])

# ---------- C4: US AEO 付费 ----------
camp4 = topic("广告系列4 · PALKIE-FB-Android-AEO-US-付费", "s-camp", [
    topic("[参数] D2开启 · 1 adset · 1,000量 @$20 = $20,000 · 积累数据后开", "s-param"),
    topic("Adset · aeo付费-XX（1个adset）", "s-group", [
        topic("优胜素材 · 待 9/8-9/11 一阶段筛选", "s-placeholder"),
    ]),
])

# ---------- US 下总览标注 + 各 camp ----------
overview = [
    topic("[总览] Meta Ads · 9/15-9/18 · 第二阶段付费测试 · 4天", "s-param"),
    topic("[预算] 总 $37,000 · 审批上限 $45,000 · 预估 $32,000 · 余 $5,000", "s-param"),
    topic("[KPI] 测付费率(C3) + 测付费上限(C4) · 拉低单价(C1+C2)", "s-param"),
    topic("[量级] 4 camp 合计 9,000 · 预估花费 $32,000", "s-param"),
]

us = topic("US", "s-lv1", overview + [camp1, camp2, camp3, camp4])
android = topic("Android", "s-lv1", [us])

root = topic("Palkie付费测试广告架构 9/15-9/18", "s-center", [android])
root["structureClass"] = "org.xmind.ui.logic.right"

# ---------- sheet / content ----------
sheet_id = tid("sheet")
content = [{
    "id": sheet_id,
    "class": "sheet",
    "title": "Palkie付费测试 9/15-9/18",
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


def count(topics):
    n = 0
    for t in topics:
        n += 1
        if "children" in t:
            n += count(t["children"]["attached"])
    return n


print("总节点数:", count([root]))
print("输出文件:", OUT)
