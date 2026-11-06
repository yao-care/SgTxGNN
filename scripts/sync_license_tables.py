"""依成分重建後，把藥物頁「## Singapore Market Information」段落的許可證表換成程式產生的表（2026-11-06，用戶核准；全程不用 AI）。

前置：scripts/rebuild_licenses_by_ingredient.py 已重建 data/bundles（HSA 現行註冊，全部有效）。
- 段落裡原有的表（不論原欄位）換成「| Licence | Product | Dosage form | Status |」（本站 240 頁原本就是這個寫法），
  單方產品在前；列數＝原表列數與 min(5, 總數) 取大（最多 20）；總數多於列數時表後加一句「Showing N of M HSA registrations.」。
  HSA 清單只有現行註冊，Status 一律 Valid。
- 新資料沒有任何註冊時拿掉表，改一句「No registration was found in the HSA listing of registered therapeutic products used for this report.」
- 表後 known_use_pages 寫的「Only part of the licence list is held in the data; the list may be incomplete.」（原本是部分紀錄才加）：
  重建後的紀錄是完整清單（total_matches＝紀錄數），這句跟事實矛盾，一併拿掉；仍是部分紀錄的證據包保留。
- 段落裡沒有表的頁（矛盾句刪完只剩標題，例 ganirelix、palivizumab；或舊頁只有文字）：在標題下補程式產生的表（min(5, 總數) 列，
  總數較多時加「Showing N of M HSA registrations.」）；沒有任何註冊時補「No registration was found …」句（已有就不重複）。
  比照 Uk、NZ、Ph 的同名程式（2026-11-06 用戶決定）。表以外的文字不動（跟新事實矛盾的句子由 tools/txgnn/.claude/delete_license_sentences.py 處理）。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--dry-run] [頁 ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = "## Singapore Market Information"
HEAD = ["| Licence | Product | Dosage form | Status |", "|------|------|------|------|"]
NONE_LINE = "No registration was found in the HSA listing of registered therapeutic products used for this report."
SHOW = "Showing {n} of {m} HSA registrations."
SHOW_RX = re.compile(r"^Showing \d+ of \d+ HSA registrations\.$")
PART_NOTE = "Only part of the licence list is held in the data; the list may be incomplete."


def cell(x):
    return str(x or "").replace("|", "/").replace("\n", " ").strip()


def table_rows(recs):
    seen, rows = set(), []
    for r in sorted(recs, key=lambda r: (r.get("kind") == "combo", str(r.get("license_id")))):
        k = r.get("license_id")
        if not k or k in seen:
            continue
        seen.add(k)
        rows.append(f"| {k} | {cell(r.get('brand_name_en'))[:70]} | {cell(r.get('dosage_form')) or 'Not recorded'} | Valid |")
    return rows


def process(text, recs, partial=False):
    lines = text.split("\n")
    if SEC not in lines:
        return None
    a = lines.index(SEC) + 1
    b = next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        rows = table_rows(recs)
        if rows:
            n = min(5, len(rows))
            block = HEAD + rows[:n] + (["", SHOW.format(n=n, m=len(rows))] if len(rows) > n else [])
        elif not any(l.strip() == NONE_LINE for l in lines[a:b]):
            block = [NONE_LINE]
        else:
            return None
        t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:a] + [""] + block + [""] + lines[a:]))
        return t2 if t2 != text else None
    x, y = tb[0], tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and (partial or l.strip() != PART_NOTE)]
    rows = table_rows(recs)
    if rows:
        n = min(20, max(y - x - 1, min(5, len(rows))))
        block = HEAD + rows[:n]
        if len(rows) > n:
            block += ["", SHOW.format(n=n, m=len(rows))]
    else:
        block = [NONE_LINE]
    out = lines[:x] + block + rest + lines[b:]
    if out[x - 1].strip():
        out.insert(x, "")
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return t2 if t2 != text else None


def main(argv):
    dry = "--dry-run" in argv
    only = {a for a in argv if not a.startswith("--")}
    n = 0
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        bf = ROOT / "data/bundles" / page.stem / "drug_bundle.json"
        if not bf.exists():
            bf = ROOT / "data/bundles" / page.stem.replace("-", "_") / "drug_bundle.json"
        if not bf.exists():
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        crlf = "\r\n" in raw[:500]
        reg = json.loads(bf.read_text(encoding="utf-8")).get("tfda") or {}
        recs = reg.get("records") or []
        new = process(raw.replace("\r\n", "\n"), recs, int(reg.get("total_matches") or 0) > len(recs))
        if new is None:
            continue
        n += 1
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    print(f"許可證表改 {n} 頁")


if __name__ == "__main__":
    main(sys.argv[1:])
