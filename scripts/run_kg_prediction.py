#!/usr/bin/env python3
"""執行知識圖譜方法預測 - Singapore HSA 版本

使用 TxGNN 知識圖譜進行老藥新用預測。

KG 預測策略（藥物相似性方法）：
1. 載入藥物-蛋白質靶點關係
2. 對於每個 HSA 藥物，找出具有相似靶點的其他藥物
3. 使用相似藥物的適應症作為潛在新適應症
4. 排除該藥物的已知適應症

使用方法:
    uv run python scripts/run_kg_prediction.py

前置條件:
    1. 已執行 process_fda_data.py
    2. 已執行 prepare_external_data.py

產生檔案:
    data/processed/repurposing_candidates.csv
"""

from pathlib import Path
from typing import Dict, Set, List, Tuple

import pandas as pd
import yaml

from sgtxgnn.data.loader import load_fda_drugs, filter_active_drugs
from sgtxgnn.mapping.drugbank_mapper import (
    load_drugbank_vocab,
    map_fda_drugs_to_drugbank,
    get_mapping_stats,
)
from sgtxgnn.mapping.disease_mapper import (
    load_disease_vocab,
    map_fda_drugs_to_diseases,
    get_mapping_stats as get_disease_mapping_stats,
)


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_drug_targets(kg_path: Path) -> Dict[str, Set[str]]:
    """載入藥物-蛋白質靶點關係

    Args:
        kg_path: kg.csv 路徑

    Returns:
        {drugbank_id: {protein_id, ...}}
    """
    df = pd.read_csv(kg_path)

    # 篩選 drug_protein 關係
    drug_protein = df[df["relation"] == "drug_protein"]

    drug_targets: Dict[str, Set[str]] = {}
    for _, row in drug_protein.iterrows():
        drug_id = str(row["x_id"])
        protein_id = str(row["y_id"])

        if drug_id not in drug_targets:
            drug_targets[drug_id] = set()
        drug_targets[drug_id].add(protein_id)

    return drug_targets


def load_existing_indications(relations_path: Path) -> Tuple[Dict[str, Set[str]], Dict[str, Set[str]]]:
    """載入已知適應症

    Args:
        relations_path: drug_disease_relations.csv 路徑

    Returns:
        (drug_to_diseases, disease_to_drugs)
        drug_to_diseases: {drug_name_upper: {disease_name_lower, ...}}
        disease_to_drugs: {disease_name_lower: {drug_name_upper, ...}}
    """
    df = pd.read_csv(relations_path)
    indications = df[df["relation"] == "indication"]

    drug_to_diseases: Dict[str, Set[str]] = {}
    disease_to_drugs: Dict[str, Set[str]] = {}

    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"].lower()

        if drug not in drug_to_diseases:
            drug_to_diseases[drug] = set()
        drug_to_diseases[drug].add(disease)

        if disease not in disease_to_drugs:
            disease_to_drugs[disease] = set()
        disease_to_drugs[disease].add(drug)

    return drug_to_diseases, disease_to_drugs


def calculate_target_similarity(
    targets1: Set[str],
    targets2: Set[str]
) -> float:
    """計算兩個藥物的靶點相似度（Jaccard 係數）"""
    if not targets1 or not targets2:
        return 0.0
    intersection = len(targets1 & targets2)
    union = len(targets1 | targets2)
    return intersection / union if union > 0 else 0.0


def find_similar_drugs(
    query_drug: str,
    query_targets: Set[str],
    all_drug_targets: Dict[str, Set[str]],
    min_similarity: float = 0.3,
    top_k: int = 10
) -> List[Tuple[str, float]]:
    """找出與查詢藥物相似的其他藥物

    Args:
        query_drug: 查詢藥物的 DrugBank ID
        query_targets: 查詢藥物的靶點集合
        all_drug_targets: 所有藥物的靶點映射
        min_similarity: 最小相似度門檻
        top_k: 返回前 k 個相似藥物

    Returns:
        [(drug_id, similarity), ...]
    """
    similarities = []
    for drug_id, targets in all_drug_targets.items():
        if drug_id == query_drug:
            continue
        sim = calculate_target_similarity(query_targets, targets)
        if sim >= min_similarity:
            similarities.append((drug_id, sim))

    # 按相似度排序
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_k]


def main():
    print("=" * 60)
    print("執行知識圖譜方法預測 - Singapore HSA")
    print("（藥物靶點相似性方法）")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    config = load_field_config()
    field_mapping = config["field_mapping"]

    # 1. 載入藥品資料
    print("步驟 1/7: 載入藥品資料...")
    fda_df = load_fda_drugs()
    active_df = filter_active_drugs(fda_df)
    print(f"  總藥品數: {len(fda_df)}")
    print(f"  有效藥品數: {len(active_df)}")
    print()

    # 2. DrugBank 映射
    print("步驟 2/7: 執行 DrugBank 映射...")
    drugbank_df = load_drugbank_vocab()
    drug_mapping = map_fda_drugs_to_drugbank(
        active_df,
        drugbank_df,
        ingredient_field=field_mapping["ingredients"],
        license_field=field_mapping["license_id"],
        brand_field=field_mapping["brand_name_en"],
    )
    drug_stats = get_mapping_stats(drug_mapping)
    print(f"  總成分數: {drug_stats['total_ingredients']}")
    print(f"  映射成功: {drug_stats['mapped_ingredients']} ({drug_stats['mapping_rate']*100:.1f}%)")
    print(f"  獨特 DrugBank ID: {drug_stats['unique_drugbank_ids']}")
    print()

    # 3. 疾病映射（ATC 代碼推斷）
    print("步驟 3/7: 執行疾病映射...")
    disease_df = load_disease_vocab()
    indication_mapping = map_fda_drugs_to_diseases(
        active_df,
        disease_df,
        atc_field=field_mapping["atc_code"],
        license_field=field_mapping["license_id"],
        brand_field=field_mapping["brand_name_en"],
    )
    disease_stats = get_disease_mapping_stats(indication_mapping)
    print(f"  總映射數: {disease_stats['total_mappings']}")
    print()

    # 4. 載入藥物靶點關係
    print("步驟 4/7: 載入藥物-蛋白質靶點關係...")
    kg_path = base_dir / "data" / "kg.csv"
    drug_targets = load_drug_targets(kg_path)
    print(f"  有靶點資訊的藥物數: {len(drug_targets)}")
    print()

    # 5. 載入已知適應症
    print("步驟 5/7: 載入已知適應症（用於排除）...")
    relations_path = base_dir / "data" / "external" / "drug_disease_relations.csv"
    drug_to_diseases, disease_to_drugs = load_existing_indications(relations_path)
    print(f"  已知藥物-疾病對: {sum(len(d) for d in drug_to_diseases.values())}")
    print()

    # 6. 基於靶點相似性尋找老藥新用候選
    print("步驟 6/7: 尋找老藥新用候選...")

    # 取得成功映射的 HSA 藥物
    valid_drugs = drug_mapping[drug_mapping["drugbank_id"].notna()].copy()
    unique_drugbank_ids = valid_drugs["drugbank_id"].unique()

    # 建立 drugbank_id -> drug info 映射
    drug_info: Dict[str, dict] = {}
    for _, row in valid_drugs.iterrows():
        db_id = row["drugbank_id"]
        if db_id not in drug_info:
            drug_info[db_id] = {
                "license_id": row.get("license_id", ""),
                "brand_name": row.get("brand_name", ""),
                "ingredient": row.get("normalized_ingredient", ""),
            }

    candidates = []
    drugs_with_targets = 0
    drugs_with_similar = 0

    for db_id in unique_drugbank_ids:
        # 檢查是否有靶點資訊
        if db_id not in drug_targets:
            continue
        drugs_with_targets += 1

        query_targets = drug_targets[db_id]
        info = drug_info[db_id]
        drug_name = info["ingredient"].upper()

        # 找出相似藥物
        similar_drugs = find_similar_drugs(
            db_id, query_targets, drug_targets,
            min_similarity=0.3, top_k=10
        )

        if not similar_drugs:
            continue
        drugs_with_similar += 1

        # 取得查詢藥物的已知適應症
        existing_diseases = drug_to_diseases.get(drug_name, set())

        # 收集相似藥物的適應症作為候選
        for similar_drug_id, similarity in similar_drugs:
            # 取得相似藥物的名稱
            similar_drug_name = drugbank_df[
                drugbank_df["drugbank_id"] == similar_drug_id
            ]["drug_name_upper"].values

            if len(similar_drug_name) == 0:
                continue
            similar_drug_name = similar_drug_name[0]

            # 取得相似藥物的適應症
            similar_indications = drug_to_diseases.get(similar_drug_name, set())

            for disease in similar_indications:
                # 排除已知適應症
                if disease in existing_diseases:
                    continue

                # 檢查是否為子字串匹配
                is_existing = any(
                    e in disease or disease in e
                    for e in existing_diseases
                )
                if is_existing:
                    continue

                candidates.append({
                    "license_id": info["license_id"],
                    "brand_name": info["brand_name"],
                    "ingredient": drug_name,
                    "drugbank_id": db_id,
                    "potential_indication": disease,
                    "similar_drug": similar_drug_name,
                    "similarity_score": similarity,
                    "source": "KG (target similarity)",
                })

    print(f"  HSA 藥物有靶點資訊: {drugs_with_targets}")
    print(f"  HSA 藥物有相似藥物: {drugs_with_similar}")
    print(f"  原始候選數: {len(candidates)}")

    # 去重
    candidates_df = pd.DataFrame(candidates)
    if len(candidates_df) > 0:
        # 保留最高相似度的記錄
        candidates_df = candidates_df.sort_values("similarity_score", ascending=False)
        candidates_df = candidates_df.drop_duplicates(
            subset=["license_id", "ingredient", "potential_indication"],
            keep="first"
        )
    print(f"  去重後候選數: {len(candidates_df)}")
    print()

    # 7. 儲存結果
    print("步驟 7/7: 儲存結果...")
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 儲存候選
    candidates_path = output_dir / "repurposing_candidates.csv"
    candidates_df.to_csv(candidates_path, index=False)
    print(f"  候選結果: {candidates_path}")

    # 儲存藥物映射
    drug_mapping_path = output_dir / "drug_mapping.csv"
    drug_mapping.to_csv(drug_mapping_path, index=False)
    print(f"  藥物映射: {drug_mapping_path}")

    # 儲存疾病映射
    disease_mapping_path = output_dir / "disease_mapping.csv"
    indication_mapping.to_csv(disease_mapping_path, index=False)
    print(f"  疾病映射: {disease_mapping_path}")

    print()
    print("=" * 60)
    print("完成！")
    print("=" * 60)
    print()
    print("統計摘要:")
    print(f"  HSA 藥品數: {len(active_df)}")
    print(f"  DrugBank 映射率: {drug_stats['mapping_rate']*100:.1f}%")
    print(f"  KG 老藥新用候選數: {len(candidates_df)}")

    if len(candidates_df) > 0:
        print()
        print("前 5 個候選（按相似度排序）:")
        top5 = candidates_df.head(5)[["ingredient", "potential_indication", "similar_drug", "similarity_score"]]
        for _, row in top5.iterrows():
            print(f"  {row['ingredient']} → {row['potential_indication']}")
            print(f"    (相似於 {row['similar_drug']}, 相似度: {row['similarity_score']:.2f})")

    print()
    print("下一步: 合併 KG 和 DL 預測")
    print("  uv run python scripts/merge_predictions.py")


if __name__ == "__main__":
    main()
