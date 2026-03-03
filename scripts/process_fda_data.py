#!/usr/bin/env python3
"""處理新加坡 HSA 藥品資料

從 data.gov.sg API 下載 HSA 已註冊藥品資料並轉換為 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    https://data.gov.sg/datasets/d_767279312753558cbf19d48344577084/view

產生檔案:
    data/raw/sg_hsa_drugs.json
"""

import json
import time
from pathlib import Path

import pandas as pd
import requests
import yaml


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_csv(config: dict, output_path: Path) -> Path:
    """從 data.gov.sg 下載 CSV 檔案

    Args:
        config: 欄位映射設定
        output_path: 輸出 CSV 檔案路徑

    Returns:
        下載的檔案路徑
    """
    print("取得下載連結...")
    resource_id = config["data_source"]["resource_id"]
    poll_url = f"https://api-open.data.gov.sg/v1/public/api/datasets/{resource_id}/poll-download"

    response = requests.get(poll_url, headers={"Accept": "application/json"}, timeout=30)
    response.raise_for_status()

    data = response.json()
    if data.get("code") != 0:
        raise ValueError(f"取得下載連結失敗: {data.get('errorMsg')}")

    download_url = data["data"]["url"]
    print(f"下載中...")

    # 下載 CSV
    csv_response = requests.get(download_url, timeout=120)
    csv_response.raise_for_status()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(csv_response.content)

    print(f"已下載: {output_path} ({output_path.stat().st_size / 1024 / 1024:.2f} MB)")
    return output_path


def load_csv_data(csv_path: Path) -> list:
    """從 CSV 檔案載入資料

    Args:
        csv_path: CSV 檔案路徑

    Returns:
        藥品資料列表
    """
    print(f"讀取 CSV: {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"載入 {len(df)} 筆記錄")

    # 轉換為字典列表
    records = df.to_dict(orient="records")
    return records


def fetch_hsa_data(config: dict) -> list:
    """從 data.gov.sg API 下載 HSA 藥品資料

    Args:
        config: 欄位映射設定

    Returns:
        藥品資料列表
    """
    api_endpoint = config["data_source"]["api_endpoint"]
    resource_id = config["data_source"]["resource_id"]

    all_records = []
    limit = 1000  # 每次請求的筆數
    offset = 0

    print(f"API 端點: {api_endpoint}")
    print(f"Resource ID: {resource_id}")
    print()

    while True:
        url = f"{api_endpoint}?resource_id={resource_id}&limit={limit}&offset={offset}"
        print(f"下載中... offset={offset}")

        # 重試邏輯處理 429 錯誤
        max_retries = 3
        for attempt in range(max_retries):
            response = requests.get(url, timeout=60)

            if response.status_code == 429:
                wait_time = 5 * (attempt + 1)
                print(f"  速率限制，等待 {wait_time} 秒後重試...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()
            break
        else:
            raise Exception(f"超過最大重試次數: {url}")

        data = response.json()

        if not data.get("success"):
            raise ValueError(f"API 請求失敗: {data.get('error', 'Unknown error')}")

        result = data.get("result", {})
        records = result.get("records", [])

        if not records:
            break

        all_records.extend(records)
        offset += limit

        # 檢查是否已取得所有資料
        total = result.get("total", 0)
        if offset >= total:
            break

        # 請求間延遲避免速率限制
        time.sleep(1)

    print(f"總共下載 {len(all_records)} 筆藥品資料")
    return all_records


def clean_record(record: dict) -> dict:
    """清理單筆記錄

    移除 API 回傳的系統欄位，保留藥品資料欄位。

    Args:
        record: 原始記錄

    Returns:
        清理後的記錄
    """
    # 移除系統欄位
    system_fields = ["_id", "_full_count"]
    return {k: v for k, v in record.items() if k not in system_fields}


def process_hsa_data(records: list, output_path: Path) -> Path:
    """處理並儲存 HSA 藥品資料

    Args:
        records: 原始資料列表
        output_path: 輸出檔案路徑

    Returns:
        輸出檔案路徑
    """
    # 清理記錄
    cleaned = [clean_record(r) for r in records]

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 儲存 JSON
    print(f"儲存至: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

    return output_path


def print_summary(records: list):
    """印出資料摘要"""
    print()
    print("=" * 40)
    print("資料摘要")
    print("=" * 40)
    print(f"總藥品數: {len(records)}")

    # 統計有主成分的藥品
    with_ingredients = sum(1 for r in records if r.get("active_ingredients"))
    print(f"有主成分: {with_ingredients} ({with_ingredients/len(records)*100:.1f}%)")

    # 統計 Forensic Classification
    forensic = {}
    for r in records:
        fc = r.get("forensic_classification", "Unknown")
        if pd.isna(fc):
            fc = "Unknown"
        forensic[fc] = forensic.get(fc, 0) + 1

    print()
    print("Forensic Classification:")
    for fc, count in sorted(forensic.items(), key=lambda x: -x[1]):
        print(f"  {fc}: {count}")

    # 統計 ATC 分類
    atc_first = {}
    for r in records:
        atc = r.get("atc_code", "")
        if atc and not pd.isna(atc):
            first = str(atc)[0] if atc else "Unknown"
            atc_first[first] = atc_first.get(first, 0) + 1

    if atc_first:
        print()
        print("ATC 第一層分類:")
        for atc, count in sorted(atc_first.items(), key=lambda x: -x[1]):
            print(f"  {atc}: {count}")


def main():
    print("=" * 60)
    print("處理新加坡 HSA 藥品資料")
    print("=" * 60)
    print()

    # 載入設定
    config = load_config()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    csv_path = raw_dir / "sg_hsa_drugs.csv"
    output_path = raw_dir / "sg_hsa_drugs.json"

    # 優先使用本地 CSV，否則下載
    if csv_path.exists():
        print(f"使用本地 CSV: {csv_path}")
        records = load_csv_data(csv_path)
    else:
        print("本地 CSV 不存在，從 API 下載...")
        download_csv(config, csv_path)
        records = load_csv_data(csv_path)

    # 處理並儲存
    process_hsa_data(records, output_path)

    # 印出摘要
    print_summary(records)

    print()
    print("=" * 60)
    print("完成！")
    print("=" * 60)
    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
