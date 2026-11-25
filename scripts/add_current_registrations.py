"""SG 每週補收 HSA 現行清單有、證據包還沒有的本藥許可證（2026-11-25，用戶第五輪決定；全程不用 AI）。

證據包 tfda.records 是 2026-11-06 scripts/rebuild_licenses_by_ingredient.py 依成分重建的（當時 HSA 清單 5,511 張，不截斷）；
之後每週排程（license_adapter）只確認號碼仍在列、不收新註冊，所以 11-06 之後才核准的本藥許可證不會進證據包。
這支照同一套重建規則（rebuild_licenses_by_ingredient 的 index／match／record，比對規則不放寬）重算每個證據包對到的現行許可證，
證據包裡還沒有的補一筆（欄位同重建；source 註明 HSA 清單下載日與規則、added＝補收日），total_matches 加上補收筆數。
只加不刪（不在現行清單的舊紀錄照舊保留，由 license_adapter 列在 summary）、可重複執行；重建比對落空的頁不會有東西可補。
records 本來就不截斷（重建後不是部分紀錄），所以沒有筆數上限。
用法（repo 根目錄）：python3 scripts/add_current_registrations.py [--skip-download] [--dry-run] [--report out.tsv]
每週排程（.github/workflows/license-refresh.yml）在 license_refresh 前跑（下載最新清單）；有補收就照常發新 Release。
"""
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rebuild_licenses_by_ingredient as rb  # noqa: E402


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    rows = rb.load_hsa("--skip-download" not in argv)
    prods, by_base = rb.index(rows)
    today = dt.date.today().isoformat()
    src_date = dt.date.fromtimestamp(rb.CSV_FILE.stat().st_mtime).isoformat()
    source = f"HSA registered therapeutic products (data.gov.sg, downloaded {src_date}); matched by ingredient, same rule as the 2026-11-06 rebuild"
    out, n_b, n_r = [], 0, 0
    for f in sorted(rb.BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        recs = list(reg.get("records") or [])
        have = {str(r.get("license_id") or "").strip() for r in recs}
        _, _, hit = rb.match(b, page, by_base)
        add = sorted(hit - have, key=lambda k: (len(prods[k]["ings"]), k))
        if not add:
            continue
        new = []
        for lid in add:
            r = rb.record(prods, lid)
            r["source"] = source
            r["added"] = today
            new.append(r)
        reg = dict(reg, records=recs + new, found=True, total_matches=int(reg.get("total_matches") or len(recs)) + len(new))
        b["tfda"] = reg
        n_b += 1
        n_r += len(new)
        out.append(f"{page}\t{len(new)}\t" + ";".join(f"{r['license_id']} {r['brand_name_en']}" for r in new))
        if not dry:
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tadded\tlicences\n" + "\n".join(out) + "\n", encoding="utf-8")
    print(f"HSA 現行註冊 {len(prods)} 張；補收 {n_b} 個證據包 {n_r} 筆" + ("（dry-run，未寫檔）" if dry else ""))
    for line in out:
        print("  " + line)


if __name__ == "__main__":
    main(sys.argv[1:])
