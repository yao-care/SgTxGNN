#!/usr/bin/env python3
"""SgTxGNN 的下載檔產生器（2026-11-06 起；本站自己的，不與他站共用）。

產生 2 份檔（網址沿用 2026-03 初始 commit 的檔）：

  docs/data/drugs.csv            公開藥物頁上的每一筆預測新適應症（藥–病配對），一列一筆
  docs/data/drugs-by-level.json  公開藥物頁依頁首等級分組＋配對統計＋高分配對（/evidence-high/、/evidence-medium/、
                                 /evidence-low/ 的 JS 讀它）

2026-03 的舊檔是當時 data/processed 的全量 KG＋DL 配對（含沒有公開頁的藥、含 KG 已知用途），之後沒更新，
公開藥物頁裡 264 個藥不在檔內。這裡改成只讀網站現行內容，不讀 data/，不手寫藥品資料：

  - 只收公開藥物頁（docs/_drugs/*.md，排除 noindex 頁與轉址頁）。藥＝front matter title，等級＝front matter
    evidence_level（頁首等級，沒寫當 L5），預測適應症數＝front matter indication_count，網址＝該頁網址。
  - 配對（disease_name、score、該筆的等級）讀 docs/data/search-index.json（由藥物頁預測表產生；每藥筆數＝indication_count）。
    score 由百分比換成 0–1。這些都是 TxGNN 深度學習模型的分數，已知用途（KG 的 indication／off-label 與許可證適應症）
    已在藥物頁排除，所以 source 一律是 DL；公開資料沒有 KG 已知用途的配對，這份檔不再收 KG、KG+DL 列。
  - drugbank_id：本站 docs/_drugs/db*.md 的 DrugBank ID 轉址頁（/drugs/dbXXXXX/ → 藥物頁）；剛好一個 ID 轉到該頁時才填，否則留空。
  - drugs-by-level.json：levels 依頁首等級分組（L1…L5、N/A），每藥一筆，筆數＝docs/_data/drug_stats.json；
    counts 是藥數與配對數；high_score 是分數 > 0.99 的配對中最高的 100 筆（分數高到低、同分依藥名與病名；總數在 counts.high_score）。
    generated 只在其他內容有變時更新成當天日期。

內容沒變就不改寫檔案。藥物頁改等級、改 noindex、search-index.json 重產之後要重跑；scripts/check_seo_docs.py 第 14 項會擋過期的檔。

用法：python3 scripts/generate_download_data.py            # 產生（有變才寫）
      python3 scripts/generate_download_data.py --check    # 只比對，有不同就 exit 1
"""
import csv
import io
import json
import re
import sys
from datetime import date
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

CSV_REL = "data/drugs.csv"
BY_LEVEL_REL = "data/drugs-by-level.json"
CSV_FIELDS = ["drugbank_id", "drug_name", "disease_name", "score", "source"]
LEVEL_ORDER = ["L1", "L2", "L3", "L4", "L5", "N/A"]
HIGH_SCORE = 0.99
HIGH_SCORE_LIST = 100  # 舊檔也只列前 100 筆；總數在 counts.high_score
NOTE = ("Built from the public drug pages of this site (noindex and redirect pages excluded). levels: drugs grouped by the "
        "evidence level shown at the top of each drug page. Pairs: the predicted new indications listed on those pages "
        "(docs/data/search-index.json), scored by the TxGNN deep learning model (source DL); known uses are excluded on the "
        "drug pages, so this file has no KG or KG+DL rows. high_score: the 100 highest-scoring pairs with score > 0.99 (total in counts.high_score). Scores are ranking "
        "values, not probabilities. Research use only; predictions require clinical validation.")


def front_matter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    out = {}
    for line in text[3:end if end >= 0 else None].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def jekyll_slugify(s):
    return re.sub(r"[\W_]+", "-", s).strip("-").lower()


def norm(p):
    return "/" if p in ("", "/") else p.rstrip("/") + "/"


def is_redirect(text, fm):
    return 'http-equiv="refresh"' in text or fm.get("layout") == "id_redirect" or bool(fm.get("redirect_to"))


def load(docs=DOCS):
    """回傳 (公開藥物 list, DrugBank ID 對照, search-index 以 slug 為鍵)。"""
    drugs, db_by_url = [], {}
    for f in sorted((docs / "_drugs").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        fm = front_matter(text)
        if is_redirect(text, fm):
            m = re.match(r"^db\d{5}$", f.stem, re.I)
            t = re.search(r'http-equiv="refresh"\s+content="\d+;\s*url=([^"]+)"', text)
            if m and t:
                db_by_url.setdefault(norm(t.group(1)), []).append(f.stem.upper())
            continue
        if fm.get("noindex", "").lower() == "true":
            continue
        slug = jekyll_slugify(fm.get("slug") or f.stem)
        try:
            count = int(fm.get("indication_count") or 0)
        except ValueError:
            count = 0
        drugs.append({"stem": f.stem, "slug": slug, "url": norm(fm.get("permalink") or f"/drugs/{slug}/"),
                      "name": fm.get("title", f.stem), "level": fm.get("evidence_level") or "L5", "count": count})
    index = json.loads((docs / "data" / "search-index.json").read_text(encoding="utf-8"))
    by_slug = {d.get("slug"): d for d in index.get("drugs", [])}
    return drugs, db_by_url, by_slug


def build(docs=DOCS):
    """回傳 ({docs 相對路徑: 內容}, warnings)。drugs-by-level.json 的內容是 dict（generated 另外處理）。"""
    drugs, db_by_url, by_slug = load(docs)
    warnings, pairs, levels = [], [], {}
    for d in drugs:
        ids = sorted(set(db_by_url.get(d["url"], [])))
        dbid = ids[0] if len(ids) == 1 else ""
        entry = by_slug.get(d["slug"])
        inds = (entry or {}).get("indications") or []
        if entry is None:
            warnings.append(f"{d['stem']}：search-index.json 沒有 {d['slug']}")
        elif len(inds) != d["count"]:
            warnings.append(f"{d['stem']}：search-index.json {len(inds)} 筆預測，頁面 indication_count {d['count']}")
        drug_pairs = []
        for ind in inds:
            score = round(float(ind["score"]) / 100, 4) if ind.get("score") not in (None, "") else None
            drug_pairs.append({"drugbank_id": dbid, "drug_name": d["name"], "disease_name": ind.get("name", ""),
                               "score": score, "source": "DL", "indication_level": ind.get("level", ""), "url": d["url"]})
        pairs += drug_pairs
        top = max(drug_pairs, key=lambda p: p["score"] or 0) if drug_pairs else None
        levels.setdefault(d["level"], []).append({
            "drug_name": d["name"], "drugbank_id": dbid, "evidence_level": d["level"],
            "indication_count": d["count"],
            "top_indication": top["disease_name"] if top else "",
            "top_score": top["score"] if top else None,
            "url": d["url"],
        })
    ordered = {lv: levels[lv] for lv in LEVEL_ORDER + sorted(set(levels) - set(LEVEL_ORDER)) if lv in levels}
    high = sorted((p for p in pairs if p["score"] is not None and p["score"] > HIGH_SCORE),
                  key=lambda p: (-p["score"], p["drug_name"].lower(), p["disease_name"].lower()))
    by_level = {
        "generated": "",
        "note": NOTE,
        "counts": {
            "drugs": len(drugs),
            **{lv: len(v) for lv, v in ordered.items()},
            "total": len(pairs), "dl": len(pairs), "high_score": len(high),
        },
        "levels": ordered,
        "high_score": [{k: p[k] for k in ("drugbank_id", "drug_name", "disease_name", "score", "source", "url")} for p in high[:HIGH_SCORE_LIST]],
    }
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=CSV_FIELDS, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for p in pairs:
        w.writerow({**p, "score": "" if p["score"] is None else f"{p['score']:.4f}"})
    return {CSV_REL: buf.getvalue().encode("utf-8"), BY_LEVEL_REL: by_level}, warnings


def dump_by_level(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8") + b"\n"


def stale_files(files, docs=DOCS):
    """與現有檔不同的檔（drugs-by-level.json 不比 generated）。"""
    out = []
    for rel, data in files.items():
        path = docs / rel
        if not path.exists():
            out.append(rel)
        elif isinstance(data, dict):
            try:
                cur = json.loads(path.read_text(encoding="utf-8"))
            except ValueError:
                out.append(rel)
                continue
            if not isinstance(cur, dict) or {**cur, "generated": ""} != data or not cur.get("generated"):
                out.append(rel)
            elif path.read_bytes() != dump_by_level({**data, "generated": cur["generated"]}):
                out.append(rel)
        elif path.read_bytes() != data:
            out.append(rel)
    return out


def main():
    check = "--check" in sys.argv[1:]
    files, warnings = build()
    for w in warnings:
        print(f"⚠ {w}")
    changed = stale_files(files)
    if not check:
        for rel in changed:
            data = files[rel]
            if isinstance(data, dict):
                data = dump_by_level({**data, "generated": date.today().isoformat()})
            (DOCS / rel).write_bytes(data)
    c = files[BY_LEVEL_REL]["counts"]
    print(f"公開藥物頁 {c['drugs']} 個；等級 { {k: v for k, v in c.items() if k in LEVEL_ORDER} }；"
          f"配對 {c['total']} 筆、分數 > {HIGH_SCORE} 的 {c['high_score']} 筆")
    if check:
        if changed:
            print("與產生器輸出不同：" + "、".join(changed))
            sys.exit(1)
        print("下載檔與產生器輸出相同")
    else:
        print(("已更新：" + "、".join(changed)) if changed else "內容沒變，沒有改寫檔案")


if __name__ == "__main__":
    main()
