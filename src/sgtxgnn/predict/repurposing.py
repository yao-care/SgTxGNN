"""老藥新用預測 - 基於 TxGNN 知識圖譜

支援台灣 TFDA 和新加坡 HSA 資料格式。
"""

from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd


# 欄位名稱對照（支援不同地區）
FIELD_NAMES = {
    "tw": {
        "license_id": "許可證字號",
        "brand_name": "中文品名",
        "ingredient": "標準化成分",
        "disease": "disease_name",
        "new_indication": "潛在新適應症",
    },
    "sg": {
        "license_id": "license_id",
        "brand_name": "brand_name",
        "ingredient": "normalized_ingredient",
        "disease": "disease_name",
        "new_indication": "potential_indication",
    },
}


def load_drug_disease_relations(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 藥物-疾病關係

    Args:
        filepath: CSV 檔案路徑

    Returns:
        藥物-疾病關係 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drug_disease_relations.csv"

    return pd.read_csv(filepath)


def build_drug_indication_map(relations_df: pd.DataFrame) -> Dict[str, Set[str]]:
    """建立藥物 -> 已知適應症集合的映射（用於過濾）

    Args:
        relations_df: 藥物-疾病關係 DataFrame

    Returns:
        {drug_name: {disease1, disease2, ...}} - 已批准/已知的適應症
    """
    # 只取 indication（已批准適應症）- 這些需要被排除
    indications = relations_df[relations_df["relation"] == "indication"]

    drug_map = {}
    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"].lower()  # 統一小寫以便比較

        if drug not in drug_map:
            drug_map[drug] = set()
        drug_map[drug].add(disease)

    return drug_map


def build_all_diseases_set(relations_df: pd.DataFrame) -> Set[str]:
    """取得所有疾病名稱集合

    Args:
        relations_df: 藥物-疾病關係 DataFrame

    Returns:
        所有疾病名稱的集合
    """
    diseases = set()
    for _, row in relations_df.iterrows():
        disease = row["y_name"]
        if pd.notna(disease):
            diseases.add(disease)
    return diseases


def find_repurposing_candidates(
    drug_mapping_df: pd.DataFrame,
    indication_mapping_df: pd.DataFrame,
    relations_df: Optional[pd.DataFrame] = None,
    region: str = "sg",
) -> pd.DataFrame:
    """找出老藥新用候選

    比較藥品的現有適應症與 TxGNN 知識圖譜中的適應症，
    找出可能的新適應症。

    Args:
        drug_mapping_df: 藥品 DrugBank 映射結果
        indication_mapping_df: 適應症疾病映射結果
        relations_df: TxGNN 藥物-疾病關係
        region: 地區代碼 ("tw" 或 "sg")

    Returns:
        老藥新用候選 DataFrame
    """
    if relations_df is None:
        relations_df = load_drug_disease_relations()

    # 取得欄位名稱
    fields = FIELD_NAMES.get(region, FIELD_NAMES["sg"])
    license_col = fields["license_id"]
    brand_col = fields["brand_name"]
    ingredient_col = fields["ingredient"]
    disease_col = fields["disease"]
    new_indication_col = fields["new_indication"]

    # 建立 TxGNN 藥物適應症映射
    kg_drug_map = build_drug_indication_map(relations_df)

    # 建立藥品的現有適應症（向量化操作）
    if disease_col in indication_mapping_df.columns:
        diseases_df = indication_mapping_df[
            indication_mapping_df[disease_col].notna()
        ][[license_col, disease_col]].copy()
        diseases_df["disease_lower"] = diseases_df[disease_col].str.lower()
        drug_diseases = diseases_df.groupby(license_col)["disease_lower"].apply(set).to_dict()
    else:
        drug_diseases = {}

    # 建立藥品資訊索引（向量化）
    # 處理不同欄位名稱
    drugbank_col = "drugbank_id"
    valid_drugs = drug_mapping_df[drug_mapping_df[drugbank_col].notna()].copy()

    if len(valid_drugs) == 0:
        return pd.DataFrame()

    # 取得唯一的 (許可證, 藥物成分) 組合
    unique_cols = [license_col, ingredient_col, brand_col, drugbank_col]
    existing_cols = [c for c in unique_cols if c in valid_drugs.columns]
    unique_pairs = valid_drugs[existing_cols].drop_duplicates()

    candidates = []

    for _, row in unique_pairs.iterrows():
        license_no = row[license_col]
        drug_name = row[ingredient_col]

        # 查詢 TxGNN 中該藥物的所有適應症
        kg_diseases = kg_drug_map.get(drug_name, set())
        if not kg_diseases:
            continue

        # 取得現有適應症
        existing_diseases = drug_diseases.get(license_no, set())

        # 找出潛在新適應症
        for disease in kg_diseases:
            disease_lower = disease.lower()

            # 快速檢查是否已存在
            is_new = all(
                exist_d not in disease_lower and disease_lower not in exist_d
                for exist_d in existing_diseases
            )

            if is_new:
                candidates.append({
                    "license_id": license_no,
                    "brand_name": row.get(brand_col, ""),
                    "ingredient": drug_name,
                    "drugbank_id": row[drugbank_col],
                    "potential_indication": disease,
                    "source": "TxGNN Knowledge Graph",
                })

    result_df = pd.DataFrame(candidates)

    # 去重
    if len(result_df) > 0:
        # First: remove exact duplicates per license
        result_df = result_df.drop_duplicates(
            subset=["license_id", "ingredient", "potential_indication"]
        )

        # Second: for DL prediction efficiency, keep only unique (drugbank_id, disease) pairs
        # This prevents redundant DL predictions for the same drug-disease combination
        # We keep the first occurrence (arbitrary license_id as representative)
        result_df = result_df.drop_duplicates(
            subset=["drugbank_id", "potential_indication"],
            keep="first"
        )

    return result_df


def generate_repurposing_report(candidates_df: pd.DataFrame) -> dict:
    """生成老藥新用報告統計

    Args:
        candidates_df: 候選藥物 DataFrame

    Returns:
        統計報告字典
    """
    if len(candidates_df) == 0:
        return {
            "total_candidates": 0,
            "unique_drugs": 0,
            "unique_diseases": 0,
            "top_diseases": [],
            "top_drugs": [],
        }

    # 支援不同欄位名稱
    ingredient_col = "ingredient" if "ingredient" in candidates_df.columns else "藥物成分"
    indication_col = "potential_indication" if "potential_indication" in candidates_df.columns else "潛在新適應症"

    unique_drugs = candidates_df[ingredient_col].nunique()
    unique_diseases = candidates_df[indication_col].nunique()

    # 最常見的潛在新適應症
    top_diseases = candidates_df[indication_col].value_counts().head(10).to_dict()

    # 最多潛在新適應症的藥物
    drug_counts = candidates_df.groupby(ingredient_col)[indication_col].nunique()
    top_drugs = drug_counts.sort_values(ascending=False).head(10).to_dict()

    return {
        "total_candidates": len(candidates_df),
        "unique_drugs": unique_drugs,
        "unique_diseases": unique_diseases,
        "top_diseases": top_diseases,
        "top_drugs": top_drugs,
    }
