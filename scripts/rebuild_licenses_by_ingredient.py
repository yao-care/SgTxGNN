"""SG 依成分重建證據包的許可證紀錄（2026-11-06，用戶核准；全程不用 AI；做法比照 Za／Us）。

原收集器依 DrugBank 對照或成分字串比對 HSA 註冊產品、截 20 筆，結果有三種問題：
- 部分紀錄：182 個證據包 total_matches 大於紀錄數（acetaminophen 112 張只存 20 張），張數只能寫「至少」；
- 漏收：頁名是 HSA 成分欄的片段（「4.56MG DONEPEZIL FREE BASE」「TO METFORMIN HYDROCHLORIDE」），比對時帶著劑量與字首；
- 正文依當時的空結果寫了「Singapore 查無註冊」，跟現在的概覽矛盾。

1. 來源：HSA 已註冊治療產品（data.gov.sg 資料集 d_767279312753558cbf19d48344577084，免金鑰；先 GET poll-download 取下載網址）。
   每張許可證（LicenceNo）一列，Activeingredients 以「&&」分隔多個成分，常見「X 鹽 劑量 eqv Y」的寫法。
   資料集只列現行註冊產品、沒有狀態欄：在列＝有效（證據包 status 空白，reviewer 視為有效）。
   重建前重新下載，存 data/raw/sg_hsa_registered_products.csv（--skip-download 用已存的檔）。
2. 比對（成分名先拿掉括號內容、劑量、藥典字樣（B.P.／USP／Ph. Eur.）、micronized、free base 等，拼字統一 sulphate→sulfate、
   besilate→besylate、HCl→hydrochloride；「X eqv Y」的 X、Y 都算）：
   - 頁名有「eqv」：用 eqv 後面的有效部分（moiety），去鹽類比對（ALECTINIB HYDROCHLORIDE … EQV. ALECTINIB → alectinib）。
   - 頁名本身帶鹽類（memantine hydrochloride、potassium bicarbonate）：只收同一個鹽（去掉水合物字樣後相同）。
   - 其他：去鹽類比對；同義名（acetaminophen＝paracetamol、albuterol＝salbutamol…）與「-ic acid」＝「-ate」視為同一成分。
   - 產品成分含本藥就收（含複方產品，與原收集器相同）。本站沒有複方頁。
3. 寫回證據包 tfda：records＝全部比對到的許可證（單方產品排前面），total_matches＝張數（不再截斷，不再是部分紀錄）；
   原紀錄整批換掉。比對結果是空的、但原紀錄有許可證號仍在 HSA 現行清單 → 不改這個證據包、列進報告（疑似比對漏掉，要人看）。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--skip-download] [--dry-run] [--report out.tsv] [頁 ...]
"""
import csv
import io
import json
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data/raw"
CSV_FILE = RAW / "sg_hsa_registered_products.csv"
DATASET = "d_767279312753558cbf19d48344577084"

SALT = (r"hydrochloride|hydrobromide|besylate|maleate|mesylate|tartrate|bitartrate|fumarate|hemifumarate|succinate|ethylsuccinate|"
        r"citrate|acetate|diacetate|dipropionate|propionate|valerate|butyrate|phosphate|sulfate|nitrate|lactate|gluconate|palmitate|"
        r"sodium|potassium|calcium|magnesium|disodium|dipotassium|cilexetil|axetil|medoxomil|dihydrochloride|bromide|chloride|iodide|"
        r"tosylate|edisylate|pamoate|embonate|stearate|oleate|mandelate|camsylate|xinafoate|furoate|aceponate|hyclate|trometamol|tromethamine|"
        r"meglumine|dimeglumine|olamine|erbumine|benzathine|esylate|napadisilate|hemisulfate|bisulfate|isethionate|dimesylate|mononitrate|acetonide|hexacetonide|"
        r"monosodium|trisodium|decanoate|enanthate|cypionate|undecanoate|oxalate|diphosphate|mesilate|dihydrogen|hydrogen|"
        r"butylbromide|methylbromide|n butylbromide|pivalate|fosamil|alafenamide|disoproxil|dipivoxil|etexilate|bromide")
HYD = (r"hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|heptahydrate|sesquihydrate|hemihydrate|"
       r"hemipentahydrate|anhydrous|hydrous|anhydrate")
SALT_RX = re.compile(r"\b(" + SALT + "|" + HYD + r")\b")
HYD_RX = re.compile(r"\b(" + HYD + r")\b")
# 藥典、粒徑、劑型描述等不是成分的字樣
NOISE = re.compile(r"\b(b ?p|u ?s ?p|ph ?eur|eur|jp|micronized|micronised|micronized|non micronised|ultramicronized|sterile|"
                   r"free base|base|basis|powder|granulation|granules|coated|dried|gel|solution [a-z]|bag [a-z]|to|of|equivalent|"
                   r"eqv|equiv|eq|corresponding|ce|in|small|large|chamber|compartment|concentrate|form|crystalline|amorphous|or|ml|mg|mcg|iu|dose|doses|actuation|vial|inh|w v|w w|v v)\b")
DOSE = re.compile(r"\d+(?:[.,]\d+)?\s*(?:mg|mcg|µg|ug|g|ml|iu|i u|units?|u|mmol|meq|%|ppm|kbq|mbq|gbq)(?![a-z])(?:\s*/\s*(?:\d+(?:[.,]\d+)?\s*)?[a-z]+)*|\b\d+(?:[.,]\d+)?\b")
SPELL = [(r"\bsulphate\b", "sulfate"), (r"\bbesilate\b", "besylate"), (r"\btosilate\b", "tosylate"), (r"\bmesilate\b", "mesylate"),
         (r"\besilate\b", "esylate"), (r"\bhcl\b", "hydrochloride"), (r"\bhbr\b", "hydrobromide"), (r"\baluminium\b", "aluminum"),
         (r"\bcaesium\b", "cesium"), (r"\bsulph", "sulf"), (r"\bphenobarbitone\b", "phenobarbital"), (r"\boestr", "estr"),
         (r"\bhyoscine n butylbromide\b", "hyoscine butylbromide"), (r"\bfrusemide\b", "furosemide"), (r"\blignocaine\b", "lidocaine"),
         (r"\bthyroxine\b", "levothyroxine"), (r"\bcyclosporin\b", "ciclosporin"), (r"\bcyclosporine\b", "ciclosporin"),
         (r"\b2 ?hcl\b", "dihydrochloride"), (r"\bn butylbromide\b", "butylbromide"), (r"^(?:d|l|dl)\s+", "")]
# 同一個成分的不同名稱統一成一個（整字取代；HSA 多用英國名，頁名多用美國名或 DrugBank 名）
CANON = [(r"\bsalbutamol\b", "albuterol"), (r"\blevosalbutamol\b", "levalbuterol"), (r"\bparacetamol\b", "acetaminophen"),
         (r"\badrenaline\b", "epinephrine"), (r"\bnoradrenaline\b", "norepinephrine"), (r"\bscopolamine\b", "hyoscine"),
         (r"\bbutylscopolamine\b", "hyoscine butylbromide"), (r"\bglyburide\b", "glibenclamide"), (r"\bmeperidine\b", "pethidine"),
         (r"\brifampin\b", "rifampicin"), (r"\bleuprolide\b", "leuprorelin"), (r"\bsomatotropin\b", "somatropin"),
         (r"\bamoxycillin\b", "amoxicillin"), (r"\bdextrose\b", "glucose"), (r"\b(?:carbon activated|charcoal activated|activated carbon)\b", "activated charcoal"),
         (r"\bacetylsalicylic acid\b", "aspirin"), (r"\bglyceryl trinitrate\b", "nitroglycerin"), (r"\bfolinic acid\b", "leucovorin"),
         (r"\bcalcium folinate\b", "leucovorin calcium"), (r"\bcholecalciferol\b", "colecalciferol"), (r"\bcephalexin\b", "cefalexin"),
         (r"\bcefazolin\b", "cefazolin"), (r"\bethinylestradiol\b", "ethinyl estradiol"), (r"\bphytomenadione\b", "phytonadione"),
         (r"\blidocaine\b", "lidocaine"), (r"\bsulfamethoxazole\b", "sulfamethoxazole"), (r"\bbenzylpenicillin\b", "penicillin g"),
         (r"\baciclovir\b", "acyclovir"), (r"\bbenztropine\b", "benzatropine"), (r"\bguaiphenesin\b", "guaifenesin"),
         (r"\bruxolinitib\b", "ruxolitinib"), (r"\bvitamin a\b", "retinol"), (r"\bvitamin c\b", "ascorbic acid"),
         (r"\bvitamin b1\b", "thiamine"), (r"\bvitamin b6\b", "pyridoxine"), (r"\bvitamin b12\b", "cyanocobalamin"),
         (r"\bcarbonyldiamide\b", "urea")]
GREEK = {"alfa", "alpha", "beta", "gamma", "delta"}
SPLIT_EQV = re.compile(r"\b(?:eqv|equv|equiv|eq|equivalent|corresponding|corresponds|as)\b\.?\s*(?:to\b)?", re.I)
# 比對結果確認為空的頁（原紀錄是別的成分的產品；要附依據）
CONFIRMED_EMPTY = {"gallium_nitrate": "原紀錄是 Ga-67 citrate、Ge-68/Ga-68 chloride 放射性藥品；HSA 現行清單沒有 gallium nitrate",
                   "alpha-tocopherol_acetate": "原紀錄是 Cernevit（DL-alpha-tocopherol）；HSA 現行清單沒有 alpha-tocopherol acetate（另有 alpha tocopheryl acid succinate）",
                   "prochlorperazine_mesylate": "原紀錄是 prochlorperazine maleate 錠；HSA 現行清單沒有 mesylate"}


def norm(x):
    t = str(x or "").lower()
    t = re.sub(r"\((?![^()]*\)).*$", " ", t)  # 沒有收尾的括號：括號以後都拿掉（Glyceryl trinitrate(GTN in 2% Glucose）
    while re.search(r"\([^()]*\)|\[[^\[\]]*\]", t):
        t = re.sub(r"\([^()]*\)|\[[^\[\]]*\]", " ", t)
    t = t.replace("(", " ").replace(")", " ").replace("@", " ")
    t = DOSE.sub(" ", t)
    t = " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())
    for a, b in SPELL:
        t = re.sub(a, b, t)
    for a, b in CANON:
        t = re.sub(a, b, t)
    t = " ".join(NOISE.sub(" ", t).split())
    return t


def nohyd(t):
    return " ".join(HYD_RX.sub(" ", t).split()) or t


def base(t):
    s = " ".join(SALT_RX.sub(" ", t).split())
    return s or nohyd(t)  # 整個名字都是鹽類字（sodium chloride、magnesium sulfate）→ 保留原名


def acid_ate(t):
    out = {t}
    if t.endswith("ic acid"):
        out.add(t[:-7] + "ate")
    elif t.endswith("ate") and " " not in t:
        out.add(t[:-3] + "ic acid")
    return out


def saltwords(t):
    return frozenset(SALT_RX.findall(nohyd(t)))


def parts(s):
    """「X 鹽 劑量 eqv Y」→ [X, Y]（各自正規化，空的拿掉）；整個字串包在括號裡時先拿掉外層括號"""
    s = str(s or "").strip()
    if re.fullmatch(r"\([^()]*\)", s):
        s = s[1:-1]
    return [p for p in (norm(x) for x in SPLIT_EQV.split(str(s or ""))) if len(p) >= 3]


def product_keys(ing):
    """HSA 一個成分 → {(去鹽鍵, 鹽類字集合)}；「X, 說明」另取逗號前的 X（Cetuximab, chimeric antibody）"""
    ps = parts(ing) + parts(ing.split(",")[0]) + [q for g in re.findall(r"\(([^()]*)\)", ing) for q in parts(g)]  # 括號內的別名（CARBONYLDIAMIDE (UREA)）
    out = set()
    for p in ps:
        b = base(p)
        out.add((b, saltwords(p) if b != nohyd(p) else frozenset()))
        w = b.split()
        if len(w) > 1 and w[-1] in GREEK:  # follitropin beta → 也算 follitropin
            out.add((" ".join(w[:-1]), frozenset()))
    return out


def page_terms(inn):
    """頁 → (比對方式, 鍵集合)"""
    ps = parts(inn)
    if not ps:
        return "none", set()
    if len(ps) > 1:  # 頁名帶 eqv：用有效部分去鹽類比
        return "base", {base(ps[-1])}
    p = ps[0]
    if base(p) != nohyd(p):  # 頁名本身帶鹽類：只收同一個鹽（產品的鹽類字包含頁名的鹽類字：hydrocortisone sodium succinate 算 hydrocortisone succinate）
        return "salt", {(base(p), saltwords(p))}
    return "base", {base(p)}


def _get(url, **kw):
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=180, **kw)
            r.raise_for_status()
            return r
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def load_hsa(download):
    if download:
        d = _get(f"https://api-open.data.gov.sg/v1/public/api/datasets/{DATASET}/poll-download", headers={"Accept": "application/json"}).json()
        if d.get("code") != 0:
            raise SystemExit(f"取得下載網址失敗：{d.get('errorMsg')}")
        RAW.mkdir(parents=True, exist_ok=True)
        CSV_FILE.write_bytes(_get(d["data"]["url"]).content)
    rows = list(csv.DictReader(io.StringIO(CSV_FILE.read_bytes().decode("utf-8-sig"))))
    if not rows or "LicenceNo" not in rows[0] or "Activeingredients" not in rows[0]:
        raise SystemExit(f"HSA 欄位改變：{list(rows[0])[:6] if rows else '空檔'}")
    if len(rows) < 5000:
        raise SystemExit(f"HSA 只解析出 {len(rows)} 筆，疑似格式改變")
    return rows


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    rows = load_hsa("--skip-download" not in argv)
    prods = {}
    by_base = {}
    for r in rows:
        lid = (r.get("LicenceNo") or "").strip()
        ings = [i.strip() for i in (r.get("Activeingredients") or "").split("&&") if i.strip()]
        if not lid or not ings:
            continue
        prods[lid] = {"r": r, "ings": ings}
        for i in ings:
            for b_, sw in product_keys(i):
                by_base.setdefault(b_, set()).add((lid, sw))
    current = set(prods)
    out, held, n_changed, n_found, n_empty = [], [], 0, 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        inn = (b.get("drug") or {}).get("inn") or page.replace("_", " ")
        mode, terms = page_terms(inn)
        hit = set()
        for t in terms:
            if mode == "salt":
                hit |= {lid for lid, sw in by_base.get(t[0], set()) if t[1] <= sw}
            else:
                hit |= {lid for lid, _ in by_base.get(t, set())}
                # 「-ic acid」＝「-ate」只認鹽（sodium valproate、mycophenolate sodium），不認酯類前驅藥（fenofibrate、mycophenolate mofetil）
                for v in acid_ate(t) - {t}:
                    hit |= {lid for lid, sw in by_base.get(v, set()) if sw}
        terms = {" ".join(sorted(t[1])) + ":" + t[0] if isinstance(t, tuple) else t for t in terms}
        old_ids = sorted({str(r.get("license_id") or "").strip() for r in reg.get("records") or []} - {""})
        old_cur = sorted(set(old_ids) & current)
        if not hit and old_cur and page not in CONFIRMED_EMPTY:
            held.append(page)
            out.append(f"{page}\t{mode}:{'|'.join(sorted(terms))}\t{reg.get('total_matches')}\t{len(old_ids)}\t-\tHELD\t{';'.join(old_cur[:10])}\t")
            continue
        recs = []
        for lid in sorted(hit, key=lambda k: (len(prods[k]["ings"]), k)):
            r = prods[lid]["r"]
            recs.append({"license_id": lid, "brand_name_zh": r.get("Productname") or "", "brand_name_en": r.get("Productname") or "",
                         "ingredients": "&&".join(prods[lid]["ings"]), "indication": "", "dosage_form": r.get("Dosageform") or "",
                         "manufacturer": r.get("Manufacturer") or "", "license_holder": r.get("Licenseholder") or "",
                         "approval_date": r.get("Approvaldate") or "", "expiry_date": "", "status": "",
                         "forensic_classification": r.get("Forensicclassification") or "", "atc_code": r.get("ATCCode") or "",
                         "route_of_administration": r.get("RouteofAdministration") or "", "strength": r.get("Strength") or "",
                         "kind": "single" if len(prods[lid]["ings"]) == 1 else "combo",
                         "source": "HSA registered therapeutic products (data.gov.sg)"})
        new = dict(reg, found=bool(recs), records=recs, total_matches=len(recs),
                   rebuilt="2026-11-06 by ingredient (HSA registered therapeutic products, data.gov.sg)")
        new_ids = [r["license_id"] for r in recs]
        dropped = sorted(set(old_ids) - set(new_ids))
        out.append(f"{page}\t{mode}:{'|'.join(sorted(terms))}\t{reg.get('total_matches')}\t{len(old_ids)}\t{len(new_ids)}\t"
                   f"{len(dropped)}\t{';'.join(dropped[:15])}\t{';'.join(sorted(set(new_ids) - set(old_ids))[:15])}")
        n_found += bool(recs)
        n_empty += not recs
        if new != reg:
            n_changed += 1
            b["tfda"] = new
            if not dry:
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tmatch\told_total_matches\told_records\tnew_records\tdropped\tdropped_ids\tadded_ids\n" + "\n".join(out) + "\n",
                             encoding="utf-8")
    print(f"HSA 現行註冊 {len(prods)} 張；改 {n_changed} 個證據包（有紀錄 {n_found}、查無 {n_empty}、比對落空但原許可證仍在列而保留 {len(held)}）")
    if held:
        print("保留（要人看）：" + ", ".join(held[:30]))


if __name__ == "__main__":
    main(sys.argv[1:])
