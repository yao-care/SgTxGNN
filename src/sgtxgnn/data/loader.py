"""HSA 藥品資料載入與過濾 - Singapore 版本"""

import json
from pathlib import Path
from typing import Optional

import pandas as pd
import yaml


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 HSA 藥品資料

    Args:
        filepath: JSON 檔案路徑，預設為 data/raw/sg_hsa_drugs.json

    Returns:
        包含所有藥品的 DataFrame

    Raises:
        FileNotFoundError: 找不到資料檔案時，提供下載指引
    """
    config = load_field_config()

    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "raw" / "sg_hsa_drugs.json"

    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到藥品資料: {filepath}\n"
            f"請先執行以下步驟：\n"
            f"1. 執行: uv run python scripts/process_fda_data.py\n"
            f"   (會自動從 data.gov.sg API 下載資料)\n"
            f"或手動下載：\n"
            f"  https://data.gov.sg/datasets/d_767279312753558cbf19d48344577084/view"
        )

    with open(filepath, "r", encoding=config.get("encoding", "utf-8")) as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """過濾有效藥品

    HSA 資料只包含已註冊產品，無需過濾狀態。
    主要過濾有主成分的藥品（TxGNN 需要）。

    Args:
        df: 原始藥品 DataFrame

    Returns:
        僅包含有主成分的藥品 DataFrame
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]

    active = df.copy()

    # 過濾有主成分的藥品（TxGNN 需要）
    ingredients_field = field_mapping.get("ingredients", "")
    if ingredients_field and ingredients_field in df.columns:
        active = active[active[ingredients_field].notna() & (active[ingredients_field] != "")]

    # 重設索引
    active = active.reset_index(drop=True)

    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """取得藥品資料摘要統計

    Args:
        df: 藥品 DataFrame

    Returns:
        摘要統計字典
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]

    ingredients_field = field_mapping.get("ingredients", "")
    dosage_form_field = field_mapping.get("dosage_form", "")
    forensic_field = field_mapping.get("forensic_classification", "")
    atc_field = field_mapping.get("atc_code", "")

    summary = {"total_count": len(df)}

    if ingredients_field and ingredients_field in df.columns:
        summary["with_ingredient"] = df[ingredients_field].notna().sum()
        summary["unique_ingredients"] = df[ingredients_field].nunique()

    if dosage_form_field and dosage_form_field in df.columns:
        summary["dosage_forms"] = df[dosage_form_field].value_counts().head(10).to_dict()

    if forensic_field and forensic_field in df.columns:
        summary["forensic_classification"] = df[forensic_field].value_counts().to_dict()

    if atc_field and atc_field in df.columns:
        # 統計 ATC 第一層分類
        atc_first = df[atc_field].dropna().str[0].value_counts()
        summary["atc_categories"] = atc_first.to_dict()

    return summary
