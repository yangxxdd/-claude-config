# -*- coding: utf-8 -*-
"""生成 幻宠 9/17-9/19 方案一（不开AEO）广告架构脑图 (.xmind)
变化点：美国从「2组adset」改为「1 camp · ABO · 3组adset(40%/40%/20%)」；菲律宾不变。
迭代/新方向素材用占位符（优秀迭代 / 新方向），不列具体名（部分在制作中）。
"""
import json
import uuid
import zipfile

OUT = r"D:\claude-projects\projects\幻宠\Palkie广告架构-方案一(不开AEO) 917-919-更新.xmind"


def tid(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:10]}"


def topic(title, children=None):
    t = {"id": tid("topic"), "title": title}
    if children:
        t["children"] = {"attached": children}
    return t


# ---------- 美国 · 老素材（来自 2.6 确认8） ----------
US_OLD_VIDEO = ["V-抓宠战斗", "V-抓宠经营-捕捞竞品", "V-帕萌战斗-雪地竞品", "V-帕萌战斗-群殴打鸡"]
US_OLD_IMAGE = ["P-宠物展示-合成 3D", "P-宠物展示-二阶进化", "P-抓宠经营-超梦", "P-抓宠经营-幽飘"]

# ---------- 美国 · Camp1（唯一变化点：ABO 3组） ----------
us_c1 = topic("Camp1 · INSTALL-US-留存测试 (1,000量@$5=$5,000)", [
    topic("[参数] ABO · 3组adset · 预算40%/40%/20%"),
    topic("Adset 1 · 老素材视频组 (40%=$2,000)", [
        *[topic(x) for x in US_OLD_VIDEO],
        topic("优秀迭代视频 ×4（好方向迭代·缩减时长版）"),
    ]),
    topic("Adset 2 · 视频组 (40%=$2,000 · 共8条)", [
        topic("新方向视频"),
        topic("剩余优秀迭代视频"),
    ]),
    topic("Adset 3 · 图片组 (20%=$1,000 · ≤8条)", [
        *[topic(x) for x in US_OLD_IMAGE],
        topic("新方向图片 / 优秀迭代图片"),
    ]),
])

# ---------- 菲律宾（不变，沿用旧结构） ----------
PH_SHOP_4 = ["P-宠物展示-合成 3D", "P-抓宠经营-超梦", "V-宠物展示-宠物合成", "V-抓宠战斗"]

ph_c4 = topic("Camp4 · INSTALL-PH-商店图验证 (1,000量@$0.6=$600)", [
    topic("Adset · 新商店图(500量)", [topic(x) for x in PH_SHOP_4]),
    topic("Adset · 旧商店图(500量)", [topic(x) for x in PH_SHOP_4]),
])

PH_CONFIRM_8 = [
    "V-帕萌战斗-雪地竞品", "V-帕萌战斗-群殴打鸡", "V-抓宠战斗", "P-抓宠经营-幽飘",
    "P-抓宠经营-超梦", "V-抓宠经营-捕捞竞品", "P-宠物展示-合成 3D", "P-宠物展示-二阶进化",
]
PH_ITER_5 = ["P-宠物展示-二阶进化-迭代", "P-抓宠经营-皮卡丘", "P-抓宠经营-耿鬼",
             "P-宠物展示-合成 3D迭代", "V-宠物展示-宠物融合迭代"]
PH_NEW_7 = ["P-宠物展示-融合恶搞", "P-宠物展示-融合炫酷", "P-宠物展示-融合擦边",
            "V-幽飘法庭剧情", "V-宠物展示-蹭超能勇士变身", "V-抓宠经营-砸蛋",
            "V-抓宠经营-售卖帕基改片头重口味"]

ph_c5 = topic("Camp5 · INSTALL-PH-方向验证 (3,000量@$0.6=$1800)", [
    topic("[参数] 3adset = 6月优秀/迭代/新方向素材"),
    topic("Adset · 6月测试优秀素材组", [topic(x) for x in PH_CONFIRM_8]),
    topic("Adset · 6月优秀迭代组", [topic(x) for x in PH_ITER_5]),
    topic("Adset · 新方向素材组", [topic(x) for x in PH_NEW_7]),
])

# ---------- 总览 ----------
overview = [
    topic("[总览] Meta Ads · Android · 9/17-9/19(3天) · 不开AEO · 测留存(次留/3留/7留)"),
    topic("[预算] 总 $7400 · 5,000量"),
    topic("[分日] 9/17 1500量/$2220 · 9/18 1500量/$2220 · 9/19 2000量/$2960"),
    topic("[国家] 美国($5) + 菲律宾($0.6)"),
]

us = topic("美国 · 1,000量/$5,000", [us_c1])
ph = topic("菲律宾 · 4,000量/$2400", [ph_c4, ph_c5])
android = topic("Android", overview + [us, ph])

root = topic("Palkie广告架构-方案一(不开AEO) 9/17-9/19", [android])
root["class"] = "topic"
root["structureClass"] = "org.xmind.ui.logic.right"

# ---------- sheet / content（新版 XMind JSON 格式） ----------
sheet = {
    "id": tid("sheet"),
    "revisionId": str(uuid.uuid4()),
    "class": "sheet",
    "rootTopic": root,
    "title": "Palkie广告架构-方案一 9/17-9/19",
    "arrangeableLayerOrder": [root["id"]],
    "zones": [],
    "theme": {},
}
content = [sheet]

metadata = {
    "dataStructureVersion": "3",
    "creator": {"name": "Vana", "version": "26.04.01341"},
    "layoutEngineVersion": "5",
}
manifest = {
    "file-entries": {
        "content.json": {},
        "metadata.json": {},
    }
}

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for name, obj in [("content.json", content), ("metadata.json", metadata),
                      ("manifest.json", manifest)]:
        data = json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8")
        z.writestr(name, data)

# ---------- 校验 ----------
with zipfile.ZipFile(OUT, "r") as z:
    names = z.namelist()
    for name in ["content.json", "metadata.json", "manifest.json"]:
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
