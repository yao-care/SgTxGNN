"""SG（HSA 已註冊治療產品，data.gov.sg）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：data.gov.sg 資料集 d_767279312753558cbf19d48344577084（免金鑰；先 GET poll-download 取下載網址，沿用站上 process_fda_data.py）。
只列現行註冊產品、沒有狀態欄：在列不改紀錄（證據包 status 原本空白，reviewer 視為有效），
新清單查不到的 licence_no 保留原狀態、列在 summary（不推定為撤銷）。證據包 license_id＝licence_no（例 SIN00095P）。
"""
import csv
import io
import time

import requests

RAW_FILE = "raw/sg_hsa_licences.json"
# 2026-10-30 實測證據包 4,481 張對得上 93.8%（其餘已不在 HSA 現行清單，保留原狀態並列在 summary）；涵蓋門檻 90%。
COVER_MIN = 0.90
DATASET = "d_767279312753558cbf19d48344577084"


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


def fetch():
    d = _get(f"https://api-open.data.gov.sg/v1/public/api/datasets/{DATASET}/poll-download", headers={"Accept": "application/json"}).json()
    if d.get("code") != 0:
        raise RuntimeError(f"取得下載網址失敗：{d.get('errorMsg')}")
    rows = csv.DictReader(io.StringIO(_get(d["data"]["url"]).content.decode("utf-8-sig")))
    if "LicenceNo" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變：{rows.fieldnames}")
    return [{"licence": (x["LicenceNo"] or "").strip()} for x in rows if x.get("LicenceNo")]


def validate(new, old):
    p = []
    if len(new) < 5000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["licence"]: "listed" for r in new}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    return False  # 在列不改紀錄；只用來確認仍在列，查不到的列在 summary
