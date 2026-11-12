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
程式區塊標記（2026-11-12 起，本站查核機制，比照 UsTxGNN）：程式產生的表格（連同表下的 SHOW 句，或 NONE_LINE）前後各一行
「<!-- licenses:begin -->」「<!-- licenses:end -->」（前後空行），讓查核紀錄、刪句工具與 gate 分得出哪些字是程式寫的；
區塊內容由 block_for 決定（重排、補標記、快照共用；列數依原表列數，所以快照存全部可列的列、gate 比前 N 列）；
--mark-existing 只替表頭＝HEAD 的現有程式表補標記、不改內容；carry_block 給 sync_notes_to_docs.py 重寫整頁時移植舊頁的程式區塊；
program_rows 給 scripts/build_license_snapshot.py。gate（scripts/check_seo_docs.py）依 snapshots/sg_licenses.json.gz 檢查程式表
（src/sgtxgnn/regulatory/licenses.py）。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--dry-run] [--mark-existing] [頁 ...]
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
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
MAX_ROWS = 20


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


def block_for(recs, n=None):
    """程式區塊的內容（不含標記）：n 列的表＋（總數較多時）SHOW 句；n 預設 min(5, 總數)；沒有任何註冊時是 NONE_LINE 一句"""
    rows = table_rows(recs)
    if not rows:
        return [NONE_LINE]
    n = min(5, len(rows)) if n is None else n
    return HEAD + rows[:n] + (["", SHOW.format(n=n, m=len(rows))] if len(rows) > n else [])


def strip_marks(lines):
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def program_rows(tf, fc=None):
    """快照用：(程式表最多可列的列, None)；頁面的列數依原表列數（5～20），gate 比前 N 列；SHOW 句的 N 隨頁不同，不比"""
    rows = table_rows(tf.get("records") or [])
    return rows[:MAX_ROWS], None


def _bounds(lines):
    a = lines.index(SEC) + 1
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def _is_prog_text(l):
    return bool(SHOW_RX.match(l.strip()))


def mark_existing(lines):
    """表頭＝HEAD 的現有程式表（連同緊接的 SHOW 句）或 NONE_LINE 補上標記，內容一字不改"""
    if BEGIN in lines or SEC not in lines:
        return lines
    a, b = _bounds(lines)
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        if NONE_LINE in lines[a:b]:
            k = lines.index(NONE_LINE, a)
            return lines[:k] + wrap([NONE_LINE]) + lines[k + 1:]
        return lines
    x = y = tb[0]
    if lines[x].strip() != HEAD[0]:
        return lines
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    blk, k = lines[x:y + 1], y + 1
    while k < b and not lines[k].strip():
        k += 1
    if k < b and _is_prog_text(lines[k]):
        blk, y = blk + ["", lines[k]], k
    return lines[:x] + wrap(blk) + lines[y + 1:]


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁的市場段落，取代新頁模型寫的第一張表（連同表下程式文字）；
    新頁段落沒有表時接在標題下。舊頁沒有程式區塊就原樣回傳新頁。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    if SEC not in lines:
        return new_text
    a, b = _bounds(lines)
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        rest = [l for l in lines[y + 1:b] if not _is_prog_text(l)]
        out = lines[:x] + blk + rest + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def process(text, recs, partial=False):
    lines = strip_marks(text.split("\n"))
    if SEC not in lines:
        return None
    a = lines.index(SEC) + 1
    b = next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        rows = table_rows(recs)
        if rows or not any(l.strip() == NONE_LINE for l in lines[a:b]):
            lines = lines[:a] + [""] + wrap(block_for(recs)) + [""] + lines[a:]
        else:  # 已有 NONE_LINE：補標記（不重複加句）
            k = lines.index(NONE_LINE, a)
            lines = lines[:k] + wrap([NONE_LINE]) + lines[k + 1:]
        t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
        return t2 if t2 != text else None
    x, y = tb[0], tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and (partial or l.strip() != PART_NOTE)]
    rows = table_rows(recs)
    out = lines[:x] + wrap(block_for(recs, min(MAX_ROWS, max(y - x - 1, min(5, len(rows)))))) + [""] + rest + lines[b:]
    if out[x - 1].strip():
        out.insert(x, "")
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return t2 if t2 != text else None


def main(argv):
    if "--mark-existing" in argv:
        n = 0
        for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
            raw = page.read_bytes().decode("utf-8")
            if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
                continue
            crlf = "\r\n" in raw[:500]
            t = raw.replace("\r\n", "\n")
            new = re.sub(r"\n{3,}", "\n\n", "\n".join(mark_existing(t.split("\n"))))
            if BEGIN in new and BEGIN not in t:  # 只寫入真的補了標記的頁
                n += 1
                if "--dry-run" not in argv:
                    page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
        print(f"程式區塊標記：補上 {n} 頁")
        return
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
