"""DrugBank 映射模組"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

from .normalizer import (
    extract_ingredients,
    get_all_synonyms,
    generate_name_variants,
    normalize_british_spelling,
    normalize_ingredient,
)


def load_drugbank_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 DrugBank 詞彙表

    Args:
        filepath: CSV 檔案路徑，預設為 data/external/drugbank_vocab.csv

    Returns:
        DrugBank 詞彙表 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drugbank_vocab.csv"

    return pd.read_csv(filepath)


def build_name_index(drugbank_df: pd.DataFrame) -> Dict[str, str]:
    """建立名稱索引（名稱 -> DrugBank ID）

    Args:
        drugbank_df: DrugBank 詞彙表

    Returns:
        名稱到 ID 的對照字典
    """
    index = {}

    for _, row in drugbank_df.iterrows():
        name_upper = row["drug_name_upper"]
        drugbank_id = row["drugbank_id"]

        # 完整名稱
        index[name_upper] = drugbank_id

        # 移除常見鹽類後綴，建立別名
        # 例如 "METFORMIN HCL" -> "METFORMIN"
        salt_suffixes = [
            " HCL", " HYDROCHLORIDE", " SODIUM", " POTASSIUM",
            " SULFATE", " SULPHATE", " MALEATE", " ACETATE",
            " CITRATE", " PHOSPHATE", " BROMIDE", " CHLORIDE",
            " TARTRATE", " FUMARATE", " SUCCINATE", " MESYLATE",
            " BESYLATE", " CALCIUM", " MAGNESIUM", " NITRATE",
            " LACTATE", " GLUCONATE", " DISODIUM", " MONOHYDRATE",
            " DIHYDRATE", " TRIHYDRATE", " ANHYDROUS",
            " DIPROPIONATE", " PROPIONATE", " ACETONIDE",
            " VALERATE", " BUTYRATE", " HEXAHYDRATE",
        ]

        for suffix in salt_suffixes:
            if name_upper.endswith(suffix):
                base_name = name_upper[:-len(suffix)].strip()
                if base_name and base_name not in index:
                    index[base_name] = drugbank_id

    # 添加常見同義詞對照
    synonym_map = {
        # 維生素
        "NIACINAMIDE": "NICOTINAMIDE",
        "NICOTINIC ACID": "NIACIN",
        "PYRIDOXINE": "VITAMIN B6",
        "THIAMINE": "VITAMIN B1",
        "RIBOFLAVIN": "VITAMIN B2",
        "CYANOCOBALAMIN": "VITAMIN B12",
        "ASCORBIC ACID": "VITAMIN C",
        "TOCOPHEROL": "VITAMIN E",
        "RETINOL": "VITAMIN A",
        "CHOLECALCIFEROL": "VITAMIN D3",
        "ERGOCALCIFEROL": "VITAMIN D2",
        "PHYTONADIONE": "VITAMIN K1",
        # 常見藥物別名（美式→DrugBank 名稱）
        "ACETYLSALICYLIC ACID": "ASPIRIN",
        "PARACETAMOL": "ACETAMINOPHEN",
        "ADRENALINE": "EPINEPHRINE",
        "NORADRENALINE": "NOREPINEPHRINE",
        "LIGNOCAINE": "LIDOCAINE",
        "FRUSEMIDE": "FUROSEMIDE",
        "ALBUTEROL": "SALBUTAMOL",  # DrugBank 使用 SALBUTAMOL
        "ALBUTEROL SULFATE": "SALBUTAMOL",
        "ACYCLOVIR": "ACICLOVIR",  # DrugBank 可能使用不同名稱
        "FLUOROURACIL": "FLUOROURACIL",
        "CYCLOSPORINE": "CICLOSPORIN",
        "RIFAMPIN": "RIFAMPICIN",
        # L- 前綴處理
        "L-MENTHOL": "LEVOMENTHOL",
        "MENTHOL": "LEVOMENTHOL",
        "DL-MENTHOL": "RACEMENTHOL",
        "L-ADRENALINE": "EPINEPHRINE",
        # 水合物/無水
        "CAFFEINE ANHYDROUS": "CAFFEINE",
        "DEXTROSE MONOHYDRATE": "GLUCOSE",
        "DEXTROSE": "GLUCOSE",
        "GLUCOSE MONOHYDRATE": "GLUCOSE",
        "HYDROUS DEXTROSE": "GLUCOSE",
        "DEXTROSE HYDROUS": "GLUCOSE",
        # 鋁化合物
        "ALUMINUM HYDROXIDE": "ALUMINIUM HYDROXIDE",
        "ALUMINUM HYDROXIDE GEL": "ALUMINIUM HYDROXIDE",
        "ALUMINUM HYDROXIDE GEL DRIED": "ALUMINIUM HYDROXIDE",
        # 常見縮寫
        "5-FU": "FLUOROURACIL",
        "5-FLUOROURACIL": "FLUOROURACIL",
        # ===== 新加坡 HSA 常見名稱 =====
        # 英式→DrugBank
        "AMOXYCILLIN": "AMOXICILLIN",
        "GUAIPHENESIN": "GUAIFENESIN",
        "SULPHAMETHOXAZOLE": "SULFAMETHOXAZOLE",
        # INN → DrugBank
        "GLIBENCLAMIDE": "GLYBURIDE",
        "SOMATROPIN": "SOMATOTROPIN",
        # HYOSCINE 系列 → SCOPOLAMINE
        "HYOSCINE": "SCOPOLAMINE",
        "HYOSCINE N-BUTYLBROMIDE": "BUTYLSCOPOLAMINE",
        "HYOSCINE BUTYLBROMIDE": "BUTYLSCOPOLAMINE",
        "SCOPOLAMINE BUTYLBROMIDE": "BUTYLSCOPOLAMINE",
        # 鹽類 → 基本形式
        "SODIUM VALPROATE": "VALPROIC ACID",
        "VALPROATE SODIUM": "VALPROIC ACID",
        "SODIUM FUSIDATE": "FUSIDIC ACID",
        "FUSIDIC ACID SODIUM": "FUSIDIC ACID",
        # 前驅藥/酯類 → 基本形式
        "OLMESARTAN MEDOXOMIL": "OLMESARTAN",
        "CANDESARTAN CILEXETIL": "CANDESARTAN",
        "FOSINOPRIL SODIUM": "FOSINOPRIL",
        "LISINOPRIL DIHYDRATE": "LISINOPRIL",
        # Cetirizine 變體
        "CETIRIZINE DIHYDROCHLORIDE": "CETIRIZINE",
        "CETIRIZINE 2HCL": "CETIRIZINE",
        "CETIRIZINE HCL": "CETIRIZINE",
        "LEVOCETIRIZINE DIHYDROCHLORIDE": "LEVOCETIRIZINE",
        "LEVOCETIRIZINE 2HCL": "LEVOCETIRIZINE",
        # Amfetamine 類
        "LISDEXAMFETAMINE DIMESYLATE": "LISDEXAMFETAMINE",
        "LISDEXAMPHETAMINE DIMESYLATE": "LISDEXAMFETAMINE",
        "LISDEXAMPHETAMINE MESILATE": "LISDEXAMFETAMINE",
        # Follitropin 類
        "FOLLITROPIN ALFA": "FOLLITROPIN",
        "FOLLITROPIN BETA": "FOLLITROPIN",
        # 特殊名稱/詞序
        "CARBON ACTIVATED": "ACTIVATED CHARCOAL",
        "ACTIVATED CARBON": "ACTIVATED CHARCOAL",
        "CHARCOAL ACTIVATED": "ACTIVATED CHARCOAL",
        "COAL TAR SOLUTION": "COAL TAR",
        "COAL TAR PREPARED": "COAL TAR",
        # 尿素
        "CARBONYLDIAMIDE": "UREA",
        "CARBAMIDE": "UREA",
        # 其他常見
        "TRIMETAZIDINE DIHYDROCHLORIDE": "TRIMETAZIDINE",
        "LEUPRORELIN ACETATE": "LEUPROLIDE",
        "LEUPRORELIN": "LEUPROLIDE",
        "ALFACALCIDOL": "ALFACALCIDOL",
        "METFORMIN HYDROCHLORIDE": "METFORMIN",
        "ATORVASTATIN CALCIUM": "ATORVASTATIN",
        "ATORVASTATIN CALCIUM TRIHYDRATE": "ATORVASTATIN",
        "ROSUVASTATIN CALCIUM": "ROSUVASTATIN",
        "AMLODIPINE BESYLATE": "AMLODIPINE",
        "AMLODIPINE BESILATE": "AMLODIPINE",
        "LOSARTAN POTASSIUM": "LOSARTAN",
        "IRBESARTAN": "IRBESARTAN",
        "TELMISARTAN": "TELMISARTAN",
        "VALSARTAN": "VALSARTAN",
        # 額外常見成分
        "SIMETHICONE": "DIMETHICONE",
        "SIMETICONE": "DIMETHICONE",
        "GLUCOSE": "D-GLUCOSE",
        "GLUCOSE MONOHYDRATE": "D-GLUCOSE",
        "DEXTROSE MONOHYDRATE": "D-GLUCOSE",
        "DEXTROSE HYDROUS": "D-GLUCOSE",
        "DEXTROSE": "D-GLUCOSE",
        "HYDROUS DEXTROSE": "D-GLUCOSE",
        # 胺基酸 (TPN 常見)
        "GLYCINE": "GLYCINE",
        "L-ALANINE": "ALANINE",
        "L-ARGININE": "ARGININE",
        "L-HISTIDINE": "HISTIDINE",
        "L-ISOLEUCINE": "ISOLEUCINE",
        "L-LEUCINE": "LEUCINE",
        "L-LYSINE": "LYSINE",
        "L-METHIONINE": "METHIONINE",
        "L-PHENYLALANINE": "PHENYLALANINE",
        "L-PROLINE": "PROLINE",
        "L-SERINE": "SERINE",
        "L-THREONINE": "THREONINE",
        "L-TRYPTOPHAN": "TRYPTOPHAN",
        "L-TYROSINE": "TYROSINE",
        "L-VALINE": "VALINE",
    }

    for alias, canonical in synonym_map.items():
        if canonical in index and alias not in index:
            index[alias] = index[canonical]

    return index


def map_ingredient_to_drugbank(
    ingredient: str,
    name_index: Dict[str, str],
) -> Optional[str]:
    """將單一成分映射到 DrugBank ID

    映射策略（優先順序）：
    1. 使用 generate_name_variants 生成的所有變體嘗試匹配
    2. 移除鹽類後綴後匹配
    3. 使用基本名稱匹配
    4. 嘗試英式/美式拼寫轉換

    Args:
        ingredient: 標準化後的成分名稱
        name_index: 名稱索引

    Returns:
        DrugBank ID，若無法映射則回傳 None
    """
    if not ingredient:
        return None

    ingredient = ingredient.upper().strip()

    # 1. 完全匹配（原始名稱）
    if ingredient in name_index:
        return name_index[ingredient]

    # 1b. 嘗試標準化後的名稱
    normalized = normalize_ingredient(ingredient)
    if normalized and normalized in name_index:
        return name_index[normalized]

    # 1c. 嘗試所有名稱變體
    variants = generate_name_variants(ingredient)
    for variant in variants:
        if variant in name_index:
            return name_index[variant]

    # 2. 移除鹽類後綴
    salt_patterns = [
        r"\s+HCL$", r"\s+HYDROCHLORIDE$", r"\s+SODIUM$",
        r"\s+POTASSIUM$", r"\s+SULFATE$", r"\s+SULPHATE$", r"\s+MALEATE$",
        r"\s+ACETATE$", r"\s+CITRATE$", r"\s+PHOSPHATE$",
        r"\s+BROMIDE$", r"\s+CHLORIDE$", r"\s+TARTRATE$",
        r"\s+HBR$", r"\s+HYDROBROMIDE$", r"\s+FUMARATE$",
        r"\s+SUCCINATE$", r"\s+MESYLATE$", r"\s+BESYLATE$", r"\s+BESILATE$",
        r"\s+CALCIUM$", r"\s+MAGNESIUM$", r"\s+NITRATE$",
        r"\s+LACTATE$", r"\s+GLUCONATE$", r"\s+DISODIUM$",
        r"\s+ANHYDROUS$", r"\s+MONOHYDRATE$", r"\s+DIHYDRATE$",
        r"\s+TRIHYDRATE$", r"\s+HEXAHYDRATE$",
        r"\s+DIPROPIONATE$", r"\s+PROPIONATE$", r"\s+ACETONIDE$",
        r"\s+VALERATE$", r"\s+BUTYRATE$", r"\s+MONONITRATE$",
        r"\s+N-BUTYLBROMIDE$",  # HSA 特有格式
        r"\s+BUTYLBROMIDE$",
        r"\s+DIHYDROCHLORIDE$", r"\s+2HCL$",  # Cetirizine 類
        r"\s+DIMESYLATE$", r"\s+DIMESILATE$",  # Lisdexamfetamine
        r"\s+MEDOXOMIL$", r"\s+CILEXETIL$",  # 前驅藥酯類
        r"\s+ALFA$", r"\s+BETA$",  # 生物製劑變體
    ]

    base_ingredient = normalized or ingredient
    for pattern in salt_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient and base_ingredient != ingredient:
        if base_ingredient in name_index:
            return name_index[base_ingredient]
        # 嘗試英式→美式轉換
        base_american = normalize_british_spelling(base_ingredient)
        if base_american in name_index:
            return name_index[base_american]

    # 2b. 移除 L-/D-/DL- 前綴
    prefix_patterns = [r"^L-", r"^D-", r"^DL-"]
    base_ingredient = ingredient
    for pattern in prefix_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 3. 嘗試移除括號內容
    base_ingredient = re.sub(r"\s*\([^)]*\)", "", ingredient).strip()
    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 4. 最後嘗試英式→美式拼寫轉換
    american = normalize_british_spelling(ingredient)
    if american != ingredient and american in name_index:
        return name_index[american]

    return None


def map_fda_drugs_to_drugbank(
    fda_df: pd.DataFrame,
    drugbank_df: Optional[pd.DataFrame] = None,
    ingredient_field: str = "active_ingredients",
    license_field: str = "licence_no",
    brand_field: str = "product_name",
) -> pd.DataFrame:
    """將藥品資料映射到 DrugBank

    支援不同地區的欄位名稱：
    - 台灣: 主成分略述, 許可證字號, 中文品名
    - 新加坡 HSA: active_ingredients, licence_no, product_name

    Args:
        fda_df: 藥品資料 DataFrame
        drugbank_df: DrugBank 詞彙表（可選）
        ingredient_field: 成分欄位名稱
        license_field: 許可證欄位名稱
        brand_field: 品名欄位名稱

    Returns:
        包含映射結果的 DataFrame
    """
    if drugbank_df is None:
        drugbank_df = load_drugbank_vocab()

    # 建立索引
    name_index = build_name_index(drugbank_df)

    results = []

    for _, row in fda_df.iterrows():
        ingredient_str = row.get(ingredient_field, "")

        # 相容台灣欄位名稱
        if not ingredient_str:
            ingredient_str = row.get("主成分略述", "")

        if not ingredient_str or pd.isna(ingredient_str):
            continue

        # 提取所有成分及同義詞
        synonyms_data = get_all_synonyms(str(ingredient_str))

        for main_name, synonyms in synonyms_data:
            # 先嘗試主名稱
            drugbank_id = map_ingredient_to_drugbank(main_name, name_index)

            # 若失敗，嘗試同義詞
            if drugbank_id is None:
                for syn in synonyms:
                    drugbank_id = map_ingredient_to_drugbank(syn, name_index)
                    if drugbank_id:
                        break

            # 取得許可證號和品名（相容不同欄位名稱）
            license_id = row.get(license_field, row.get("許可證字號", ""))
            brand_name = row.get(brand_field, row.get("中文品名", ""))

            results.append({
                "license_id": license_id,
                "brand_name": brand_name,
                "original_ingredient": str(ingredient_str),
                "normalized_ingredient": main_name,
                "synonyms": "; ".join(synonyms) if synonyms else "",
                "drugbank_id": drugbank_id,
                "mapping_success": drugbank_id is not None,
            })

    return pd.DataFrame(results)


def get_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算映射統計

    Args:
        mapping_df: 映射結果 DataFrame

    Returns:
        統計字典
    """
    total = len(mapping_df)

    # 相容新舊欄位名稱
    success_col = "mapping_success" if "mapping_success" in mapping_df.columns else "映射成功"
    ingredient_col = "normalized_ingredient" if "normalized_ingredient" in mapping_df.columns else "標準化成分"

    success = mapping_df[success_col].sum() if success_col in mapping_df.columns else 0
    unique_ingredients = mapping_df[ingredient_col].nunique() if ingredient_col in mapping_df.columns else 0
    unique_drugbank = mapping_df[mapping_df[success_col]]["drugbank_id"].nunique() if success_col in mapping_df.columns else 0

    return {
        "total_ingredients": total,
        "mapped_ingredients": int(success),
        "mapping_rate": success / total if total > 0 else 0,
        "unique_ingredients": unique_ingredients,
        "unique_drugbank_ids": unique_drugbank,
    }
