import json

tables = ["material","daily","finance","issue","conclusion"]
for name in tables:
    fl = json.load(open(f"sync_dump/fields_{name}.json", encoding="utf-8"))
    rl = json.load(open(f"sync_dump/recs_{name}.json", encoding="utf-8"))
    fmap = {}
    for f in fl["data"]["fields"]:
        fmap[f["id"]] = (f["name"], f["type"], f.get("multiple", False))
    d = rl["data"]
    fids = d.get("field_id_list", [])
    recids = d.get("record_id_list", [])
    rows = d.get("data", [])
    out = []
    for rid, row in zip(recids, rows):
        rec = {}
        for fid, val in zip(fids, row):
            nm, typ, mult = fmap.get(fid, (fid, "?", False))
            if typ in ("formula", "auto_number"):
                continue
            if val is None:
                rec[nm] = None
            elif typ == "select":
                if isinstance(val, list):
                    rec[nm] = val[0] if (len(val)==1 and not mult) else val
                else:
                    rec[nm] = val
            elif typ == "datetime":
                s = str(val).replace("T"," ").split(".")[0]
                rec[nm] = s
            else:
                rec[nm] = val
        out.append({"record_id": rid, "fields": rec})
    json.dump(out, open(f"sync_dump/norm_{name}.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"=== {name}: {len(out)} records ===")
    for r in out:
        print(r["record_id"], "=>", json.dumps(r["fields"], ensure_ascii=False))
