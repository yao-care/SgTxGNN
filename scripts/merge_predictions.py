#!/usr/bin/env python3
"""合併 KG 和 DL 預測結果，並過濾已知適應症

此腳本會：
1. 載入 DrugBank 的已知適應症（indication relations）
2. 載入 KG 預測（repurposing_candidates.csv）
3. 載入 DL 預測（txgnn_checkpoint.csv）
4. 過濾掉已經是已知適應症的預測
5. 合併並輸出 unified_predictions.csv

使用方法:
    uv run python scripts/merge_predictions.py
"""

from pathlib import Path
from typing import Dict, Set

import pandas as pd


def load_existing_indications(relations_path: Path) -> Dict[str, Set[str]]:
    """載入 DrugBank 已知適應症

    Args:
        relations_path: drug_disease_relations.csv 路徑

    Returns:
        {drug_name_upper: {disease_name_lower, ...}}
    """
    df = pd.read_csv(relations_path)

    # 只取 indication 關係（已批准適應症）
    indications = df[df["relation"] == "indication"]

    drug_diseases: Dict[str, Set[str]] = {}
    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"].lower()

        if drug not in drug_diseases:
            drug_diseases[drug] = set()
        drug_diseases[drug].add(disease)

    return drug_diseases


def is_existing_indication(
    drug_name: str,
    disease_name: str,
    existing_indications: Dict[str, Set[str]]
) -> bool:
    """檢查是否為已知適應症

    使用子字串匹配來處理名稱變體
    """
    drug_upper = drug_name.upper()
    disease_lower = disease_name.lower()

    existing_diseases = existing_indications.get(drug_upper, set())

    # 完全匹配
    if disease_lower in existing_diseases:
        return True

    # 子字串匹配（處理 "hypertension" vs "hypertensive disorder" 等）
    for existing_d in existing_diseases:
        if existing_d in disease_lower or disease_lower in existing_d:
            return True

    return False


def main():
    print("=" * 60)
    print("合併預測結果並過濾已知適應症")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent

    # 1. 載入已知適應症
    print("步驟 1: 載入 DrugBank 已知適應症...")
    relations_path = base_dir / "data" / "external" / "drug_disease_relations.csv"
    existing_indications = load_existing_indications(relations_path)

    total_indications = sum(len(diseases) for diseases in existing_indications.values())
    print(f"  藥物數: {len(existing_indications)}")
    print(f"  已知適應症數: {total_indications}")
    print()

    # 2. 載入 KG 預測（靶點相似性方法）
    print("步驟 2: 載入 KG 預測...")
    kg_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"
    kg_results = []

    if kg_path.exists():
        kg_df = pd.read_csv(kg_path)
        print(f"  原始 KG 預測數: {len(kg_df)}")

        # KG 預測已經在生成時過濾了已知適應症
        # 但仍做額外檢查以確保一致性
        filtered_count = 0
        for _, row in kg_df.iterrows():
            drug_name = row.get("ingredient", "")
            disease_name = row.get("potential_indication", "")
            similarity_score = row.get("similarity_score", None)

            if not is_existing_indication(drug_name, disease_name, existing_indications):
                kg_results.append({
                    "drugbank_id": row["drugbank_id"],
                    "drug_name": drug_name,
                    "ingredient": drug_name,
                    "disease_name": disease_name,
                    "score": similarity_score,  # 使用靶點相似度分數
                    "source": "KG",
                    "license_id": row.get("license_id", ""),
                    "brand_name": row.get("brand_name", ""),
                    "similar_drug": row.get("similar_drug", ""),
                })
            else:
                filtered_count += 1

        print(f"  額外過濾已知適應症: {filtered_count}")
        print(f"  保留的新適應症候選: {len(kg_results)}")
    else:
        print("  警告: repurposing_candidates.csv 不存在")
    print()

    # 3. 載入 DL 預測
    print("步驟 3: 載入 DL 預測...")
    dl_path = base_dir / "data" / "processed" / "txgnn_checkpoint.csv"
    dl_results = []

    if dl_path.exists():
        dl_df = pd.read_csv(dl_path)
        print(f"  原始 DL 預測數: {len(dl_df)}")

        # 載入藥品映射以取得 license_id 和 brand_name
        drug_mapping_path = base_dir / "data" / "processed" / "drug_mapping.csv"
        drug_info = {}
        if drug_mapping_path.exists():
            dm_df = pd.read_csv(drug_mapping_path)
            for _, row in dm_df.iterrows():
                db_id = row.get("drugbank_id")
                if pd.notna(db_id):
                    if db_id not in drug_info:
                        drug_info[db_id] = {
                            "license_id": row.get("license_id", ""),
                            "brand_name": row.get("brand_name", ""),
                            "ingredient": row.get("normalized_ingredient", ""),
                        }

        # 過濾已知適應症
        filtered_count = 0
        for _, row in dl_df.iterrows():
            drug_name = row.get("drug_name", "")
            disease_name = row.get("disease_name", "")
            drugbank_id = row.get("drugbank_id", "")
            score = row.get("txgnn_score", None)

            if not is_existing_indication(drug_name, disease_name, existing_indications):
                info = drug_info.get(drugbank_id, {})
                dl_results.append({
                    "drugbank_id": drugbank_id,
                    "drug_name": drug_name,
                    "ingredient": info.get("ingredient", drug_name),
                    "disease_name": disease_name,
                    "score": score,
                    "source": "DL",
                    "license_id": info.get("license_id", ""),
                    "brand_name": info.get("brand_name", ""),
                })
            else:
                filtered_count += 1

        print(f"  過濾掉已知適應症: {filtered_count}")
        print(f"  保留的新適應症候選: {len(dl_results)}")
    else:
        print("  警告: txgnn_checkpoint.csv 不存在")
    print()

    # 4. 合併結果
    print("步驟 4: 合併 KG 和 DL 預測...")

    # 建立 (drugbank_id, disease_name) -> result 的映射
    merged: Dict[tuple, dict] = {}

    # 先加入 KG 結果
    for result in kg_results:
        key = (result["drugbank_id"], result["disease_name"].lower())
        merged[key] = result.copy()

    # 再加入 DL 結果，如果重複則標記為 KG+DL
    for result in dl_results:
        key = (result["drugbank_id"], result["disease_name"].lower())
        if key in merged:
            # 兩種方法都預測，更新為 KG+DL
            merged[key]["source"] = "KG+DL"
            merged[key]["score"] = result["score"]  # 使用 DL 的分數
        else:
            merged[key] = result.copy()

    # 轉換為 DataFrame
    unified_df = pd.DataFrame(list(merged.values()))

    # 統計
    if len(unified_df) > 0:
        source_counts = unified_df["source"].value_counts()
        print(f"  KG only: {source_counts.get('KG', 0)}")
        print(f"  DL only: {source_counts.get('DL', 0)}")
        print(f"  KG+DL (雙重驗證): {source_counts.get('KG+DL', 0)}")
        print(f"  總計: {len(unified_df)}")
    print()

    # 5. 儲存結果
    print("步驟 5: 儲存結果...")
    output_path = base_dir / "data" / "processed" / "unified_predictions.csv"
    unified_df.to_csv(output_path, index=False)
    print(f"  輸出: {output_path}")

    print()
    print("=" * 60)
    print("完成！")
    print("=" * 60)

    # 顯示範例
    if len(unified_df) > 0:
        print()
        print("範例預測（前 10 個）：")
        sample = unified_df.head(10)[["drug_name", "disease_name", "source", "score"]]
        print(sample.to_string(index=False))


if __name__ == "__main__":
    main()
