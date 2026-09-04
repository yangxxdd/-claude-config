import json
tables = ["material","daily","finance","issue","conclusion"]
for n in tables:
    copy = json.load(open(f"sync_dump/fields_{n}.json",encoding="utf-8"))["data"]["fields"]
    formal = json.load(open(f"sync_dump/formal_fields_{n}.json",encoding="utf-8"))["data"]["fields"]
    cnames = {f["name"]:f["type"] for f in copy}
    fnames = {f["name"]:f["type"] for f in formal}
    only_copy = set(cnames)-set(fnames)
    only_formal = set(fnames)-set(cnames)
    type_diff = {k:(cnames[k],fnames[k]) for k in cnames.keys()&fnames.keys() if cnames[k]!=fnames[k]}
    print(f"=== {n}: copy={len(cnames)} formal={len(fnames)} ===")
    if only_copy: print("  缺(只在copy):", sorted(only_copy))
    if only_formal: print("  多(只在formal):", sorted(only_formal))
    if type_diff: print("  类型不同:", type_diff)
    if not only_copy and not only_formal and not type_diff: print("  ✓ 字段名+类型完全一致")
