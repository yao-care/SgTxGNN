#!/usr/bin/env python3
"""執行知識圖譜方法預測 - Singapore HSA 版本

使用 TxGNN 知識圖譜進行老藥新用預測。

使用方法:
    uv run python scripts/run_kg_prediction.py

前置條件:
    1. 已執行 process_fda_data.py
    2. 已執行 prepare_external_data.py

產生檔案:
    data/processed/repurposing_candidates.csv
"""

from pathlib import Path

import pandas as pd
import yaml

from txgnn.data.loader import load_fda_drugs, filter_active_drugs
from txgnn.mapping.drugbank_mapper import (
    load_drugbank_vocab,
    map_fda_drugs_to_drugbank,
    get_mapping_stats,
)
from txgnn.mapping.disease_mapper import (
    load_disease_vocab,
    map_fda_drugs_to_diseases,
    get_mapping_stats as get_disease_mapping_stats,
)
from txgnn.predict.repurposing import (
    load_drug_disease_relations,
    find_repurposing_candidates,
    generate_repurposing_report,
)


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    print("=" * 60)
    print("執行知識圖譜方法預測 - Singapore HSA")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    config = load_field_config()
    field_mapping = config["field_mapping"]

    # 1. 載入藥品資料
    print("步驟 1/6: 載入藥品資料...")
    fda_df = load_fda_drugs()
    active_df = filter_active_drugs(fda_df)
    print(f"  總藥品數: {len(fda_df)}")
    print(f"  有效藥品數（有成分）: {len(active_df)}")
    print()

    # 2. DrugBank 映射
    print("步驟 2/6: 執行 DrugBank 映射...")
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

    # 3. 疾病映射（使用 ATC 代碼推斷）
    print("步驟 3/6: 執行疾病映射（ATC 代碼推斷）...")
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
    print(f"  獨特藥品: {disease_stats['unique_drugs']}")
    print(f"  獨特疾病: {disease_stats['unique_diseases']}")
    print()

    # 4. 載入 TxGNN 藥物-疾病關係
    print("步驟 4/6: 載入 TxGNN 知識圖譜...")
    relations_df = load_drug_disease_relations()
    print(f"  藥物-疾病關係數: {len(relations_df)}")
    print()

    # 5. 尋找老藥新用候選
    print("步驟 5/6: 尋找老藥新用候選...")
    candidates = find_repurposing_candidates(
        drug_mapping,
        indication_mapping,
        relations_df,
        region="sg",
    )
    report = generate_repurposing_report(candidates)
    print(f"  候選數: {report['total_candidates']}")
    print(f"  獨特藥物: {report['unique_drugs']}")
    print(f"  獨特疾病: {report['unique_diseases']}")
    print()

    if report['top_diseases']:
        print("  前 5 個最常見的潛在新適應症:")
        for disease, count in list(report['top_diseases'].items())[:5]:
            print(f"    - {disease}: {count}")
        print()

    # 6. 儲存結果
    print("步驟 6/6: 儲存結果...")
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 儲存候選
    candidates_path = output_dir / "repurposing_candidates.csv"
    candidates.to_csv(candidates_path, index=False)
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
    print(f"  老藥新用候選數: {report['total_candidates']}")
    print()
    print("下一步: 生成 FHIR 資源")
    print("  uv run python scripts/generate_fhir_resources.py")


if __name__ == "__main__":
    main()
