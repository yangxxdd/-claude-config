import json, subprocess, sys

COPY = "NldXb92j7ayS4ks3FCCcT1FcnAw"
tables = {
    "material": "tbl1emyBpEthQGXD",
    "daily": "tbl8USRMn8xmPH7E",
    "finance": "tblaEa2UNhJauEOw",
    "issue": "tblfBbAVlnEyHNBc",
    "conclusion": "tblQbhCdiSJxSAM2",
}

def cli(*args):
    r = subprocess.run(["lark-cli","base"]+list(args), capture_output=True, text=True, encoding="utf-8")
    return json.loads(r.stdout)

for name, tid in tables.items():
    # field-list
    fl = cli("+field-list","--base-token",COPY,"--table-id",tid,"--limit","200")
    fmap = {}  # id -> (name, type, multiple)
    for f in fl["data"]["fields"]:
        fmap[f["id"]] = (f["name"], f["type"], f.get("multiple", False))
    # record-list
    rl = cli("+record-list","--base-token",COPY,"--table-id",tid,"--limit","200","--format","json")
    d = rl["data"]
    fids = d.get("field_id_list", [])
    ftypes = d.get("field_type_list", [])
    recids = d.get("record_id_list", [])
    rows = d.get("data", [])
    out = []
    for rid, row in zip(recids, rows):
        rec = {}
        for fid, ftype, val in zip(fids, ftypes, row):
            nm, typ, mult = fmap.get(fid, (fid, "?", False))
            if typ == "formula" or typ == "auto_number":
                continue
            if val is None:
                rec[nm] = None
            elif typ == "select":
                if isinstance(val, list):
                    rec[nm] = val[0] if (len(val)==1 and not mult) else val
                else:
                    rec[nm] = val
            elif typ == "datetime":
                # val like "2026-07-09T00:00:00.000+08:00"
                s = str(val)
                s = s.replace("T"," ").split(".")[0]
                rec[nm] = s
            elif typ == "number":
                rec[nm] = val  # already number or string
            else:
                rec[nm] = val
        out.append({"record_id": rid, "fields": rec})
    with open(f"sync_dump/norm_{name}.json","w",encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"=== {name} ({tid}) ===")
    for r in out:
        print(r["record_id"], "=>", json.dumps(r["fields"], ensure_ascii=False))
