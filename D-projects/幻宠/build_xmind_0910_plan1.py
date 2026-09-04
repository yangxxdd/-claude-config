# -*- coding: utf-8 -*-
"""生成 幻宠 9/10-9/12 方案一（不开AEO）广告架构脑图 (.xmind)"""
import json
import uuid
import zipfile

OUT = r"D:\claude-projects\projects\幻宠\Palkie广告架构-方案一-9.10-9.12.xmind"


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
# 6月确认素材
CONFIRM_8 = {
    "战斗": ["V-帕萌战斗-雪地竞品", "V-帕萌战斗-群殴打鸡", "V-抓宠战斗", "P-抓宠经营-幽飘"],
    "宠物展示": ["P-抓宠经营-超梦", "V-抓宠经营-捕捞竞品", "P-宠物展示-合成 3D", "P-宠物展示-二阶进化"],
}
ITER_5 = ["P-宠物展示-二阶进化-迭代", "P-抓宠经营-皮卡丘", "P-抓宠经营-耿鬼", "P-宠物展示-合成 3D迭代", "V-宠物展示-宠物融合迭代"]
NEW_8_MAIN = ["P-宠物展示-融合恶搞", "P-宠物展示-融合炫酷", "P-宠物展示-融合擦边", "V-幽飘法庭剧情",
              "V-宠物展示-蹭超能勇士变身", "V-抓宠经营-砸蛋", "V-抓宠经营-售卖帕基改片头重口味"]
NEW_8_NEWACCT = ["V-宠物展示-宠物进化蹭数码宝贝"]  # 侵权BGM -> 新户
POKEMON_3 = ["宝可梦图片1", "宝可梦图片2", "宝可梦视频1"]
SHOP_4 = ["P-宠物展示-合成 3D", "P-抓宠经营-超梦", "V-宠物展示-宠物合成", "V-抓宠战斗"]

# ---------- 美国 (3 camp) ----------
us_c1 = topic("Camp1 · INSTALL-US-留存测试 (1,000量@$5=$5,000)", "s-camp", [
    topic("[参数] 8确认素材拆2组adset · 5迭代仅替补不跑", "s-param"),
    topic("Adset · 战斗方向", "s-group", [creative(x) for x in CONFIRM_8["战斗"]]),
    topic("Adset · 宠物展示方向", "s-group", [creative(x) for x in CONFIRM_8["宠物展示"]]),
    topic("Adset · 5迭代储备(不跑)", "s-group", [creative(x) for x in ITER_5]),
])

us_c2 = topic("Camp2 · INSTALL-US-商店图验证 (450量@$5=$2,250)", "s-camp", [
    topic("[参数] 4素材×新/旧商店图各1adset · 每adset 225量", "s-param"),
    topic("Adset · 新商店图(225量)", "s-group", [creative(x) for x in SHOP_4]),
    topic("Adset · 旧商店图(225量)", "s-group", [creative(x) for x in SHOP_4]),
])

us_c3_main = topic("Camp3 · INSTALL-US-素材方向验证-主户 (350量@$5=$1,750)", "s-camp", [
    topic("[参数] 7新脚本素材 · 每素材50量", "s-param"),
    topic("Adset · 7新脚本素材(每素材50量)", "s-group", [creative(x) for x in NEW_8_MAIN]),
])

us_c3_new = topic("Camp3-新户 · INSTALL-素材方向验证-新户 (200量@$5=$1,000)", "s-camp", [
    topic("[参数] 新账户单独camp · 宝可梦3+侵权BGM素材 · 每素材50量 · IP风险隔离", "s-param"),
    topic("Adset · 宝可梦3+蹭数码宝贝(每素材50量)", "s-group",
          [creative(x) for x in POKEMON_3 + NEW_8_NEWACCT]),
])

# ---------- 菲律宾 (2 camp) ----------
ph_c1 = topic("Camp4 · INSTALL-PH-商店图验证 (1,000量@$1=$1,000)", "s-camp", [
    topic("[参数] 同4素材×新/旧商店图2adset · 领导:美国450量太少,PH陪玩顺带测", "s-param"),
    topic("Adset · 新商店图(500量)", "s-group", [creative(x) for x in SHOP_4]),
    topic("Adset · 旧商店图(500量)", "s-group", [creative(x) for x in SHOP_4]),
])

ph_c2 = topic("Camp5 · INSTALL-PH-方向验证 (1,000量@$1=$1,000)", "s-camp", [
    topic("[参数] 3adset = 6月优秀/迭代/新方向素材", "s-param"),
    topic("Adset · 6月测试优秀素材组", "s-group", [creative(x) for x in CONFIRM_8["战斗"] + CONFIRM_8["宠物展示"]]),
    topic("Adset · 6月优秀迭代组", "s-group", [creative(x) for x in ITER_5]),
    topic("Adset · 新方向素材组", "s-group", [creative(x) for x in NEW_8_MAIN]),
])

# ---------- T3 (1 camp) ----------
t3_c1 = topic("Camp6 · INSTALL-T3(MX/ID/BR)-方向验证 (1,000量@$1=$1,000)", "s-camp", [
    topic("[参数] 3adset = 6月优秀/迭代/新方向素材", "s-param"),
    topic("Adset · 6月测试优秀素材组", "s-group", [creative(x) for x in CONFIRM_8["战斗"] + CONFIRM_8["宠物展示"]]),
    topic("Adset · 6月优秀迭代组", "s-group", [creative(x) for x in ITER_5]),
    topic("Adset · 新方向素材组", "s-group", [creative(x) for x in NEW_8_MAIN]),
])

# ---------- 总览 ----------
overview = [
    topic("[总览] Meta Ads · Android · 9/10-9/12(3天) · 不开AEO · 测留存(次留/3留/7留)", "s-param"),
    topic("[预算] 总 $13,000 · 5,000量", "s-param"),
    topic("[分日] 9/10 1500量/$3,900 · 9/11 1800量/$4,600 · 9/12 1700量/$4,500", "s-param"),
    topic("[国家] 美国($5) + 菲律宾($1) + T3=MX/ID/BR($1)", "s-param"),
]

us = topic("美国 · 2,000量/$10,000", "s-lv1", [us_c1, us_c2, us_c3_main, us_c3_new])
ph = topic("菲律宾 · 2,000量/$2,000", "s-lv1", [ph_c1, ph_c2])
t3 = topic("T3(MX/ID/BR) · 1,000量/$1,000", "s-lv1", [t3_c1])
android = topic("Android", "s-lv1", overview + [us, ph, t3])

root = topic("Palkie广告架构-方案一(不开AEO) 9/10-9/12", "s-center", [android])
root["structureClass"] = "org.xmind.ui.logic.right"

# ---------- sheet / content ----------
sheet_id = tid("sheet")
content = [{
    "id": sheet_id,
    "class": "sheet",
    "title": "Palkie广告架构-方案一 9/10-9/12",
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
