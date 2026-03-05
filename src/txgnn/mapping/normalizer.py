"""主成分名稱標準化

支援 HSA (新加坡) 和 TFDA (台灣) 的成分格式。
"""

import re
from typing import List, Tuple, Optional


# 英式 → 美式拼寫對照表
BRITISH_TO_AMERICAN = {
    # 拼寫差異
    "SULPHATE": "SULFATE",
    "SULPHUR": "SULFUR",
    "SULPHA": "SULFA",
    "SULPHONE": "SULFONE",
    "SULPHONATE": "SULFONATE",
    "ALUMINIUM": "ALUMINUM",
    "HAEMOGLOBIN": "HEMOGLOBIN",
    "OESTROGEN": "ESTROGEN",
    "OESTRADIOL": "ESTRADIOL",
    "HAEM": "HEME",
    "COLOUR": "COLOR",
    "FIBRE": "FIBER",
    "CENTRE": "CENTER",
    "LITRE": "LITER",
    "METRE": "METER",
    "FAVOUR": "FAVOR",
    # 藥名差異 - 英式→美式/DrugBank
    "PARACETAMOL": "ACETAMINOPHEN",
    "ADRENALINE": "EPINEPHRINE",
    "NORADRENALINE": "NOREPINEPHRINE",
    "LIGNOCAINE": "LIDOCAINE",
    "FRUSEMIDE": "FUROSEMIDE",
    "GLYCERYL TRINITRATE": "NITROGLYCERIN",
    "SALBUTAMOL": "ALBUTEROL",
    "ACICLOVIR": "ACYCLOVIR",
    "CICLOSPORIN": "CYCLOSPORINE",
    "CLOMIFENE": "CLOMIPHENE",
    "DEXTROPROPOXYPHENE": "PROPOXYPHENE",
    "MITOZANTRONE": "MITOXANTRONE",
    "PHENOBARBITONE": "PHENOBARBITAL",
    "PETHIDINE": "MEPERIDINE",
    "RIFAMPICIN": "RIFAMPIN",
    "THIOPENTONE": "THIOPENTAL",
    # 英式藥名（額外常見）
    "AMOXYCILLIN": "AMOXICILLIN",
    "AMPICILLIN": "AMPICILLIN",
    "GUAIPHENESIN": "GUAIFENESIN",
    "SULPHAMETHOXAZOLE": "SULFAMETHOXAZOLE",
    "CHLORPHENIRAMINE": "CHLORPHENIRAMINE",
    "PROMETHAZINE": "PROMETHAZINE",
    "DIPHENHYDRAMINE": "DIPHENHYDRAMINE",
    # INN → USAN/DrugBank 名稱
    "GLIBENCLAMIDE": "GLYBURIDE",
    "SOMATROPIN": "SOMATOTROPIN",
    "HYOSCINE": "SCOPOLAMINE",
    "METAMIZOLE": "DIPYRONE",
    "AMBROXOL": "AMBROXOL",
    # 其他常見變體
    "5-FLUOROURACIL": "FLUOROURACIL",
    "5-FU": "FLUOROURACIL",
}

# 常見鹽類後綴（用於生成替代名稱）
SALT_SUFFIXES = [
    "HYDROCHLORIDE", "HCL", "HCL.", "HYDROCHLORIDUM",
    "SULFATE", "SULPHATE",
    "SODIUM", "POTASSIUM", "CALCIUM", "MAGNESIUM",
    "ACETATE", "CITRATE", "PHOSPHATE", "NITRATE",
    "MALEATE", "FUMARATE", "SUCCINATE", "TARTRATE",
    "MESYLATE", "BESYLATE", "TOSYLATE",
    "MONOHYDRATE", "DIHYDRATE", "TRIHYDRATE",
    "ANHYDROUS",
]


def normalize_british_spelling(name: str) -> str:
    """將英式拼寫轉換為美式拼寫"""
    result = name
    for british, american in BRITISH_TO_AMERICAN.items():
        # 完整詞替換
        result = re.sub(rf"\b{british}\b", american, result, flags=re.IGNORECASE)
    return result


def extract_eqv_name(name: str) -> Optional[str]:
    """從 HSA 的 EQV/EQUIVALENT TO 格式提取標準名稱

    HSA 格式:
    - "GENTAMICIN SULPHATE EQV GENTAMICIN"
    - "45.8MG LOSARTAN EQUIVALENT TO LOSARTAN POTASSIUM"
    → 提取 "GENTAMICIN" 或 "LOSARTAN"
    """
    # 匹配 "... EQV ..." 或 "... EQUIVALENT TO ..." 模式
    match = re.search(r"\b(?:EQV|EQUIVALENT TO)\s+(.+?)(?:\s+\d|$)", name, re.IGNORECASE)
    if match:
        eqv_name = match.group(1).strip()
        # 移除劑量資訊（如 "BASE 500MG"）
        eqv_name = re.sub(r"\s+(BASE\s*)?\d+(\.\d+)?\s*(MG|G|MCG|IU|ML|%|UNIT).*$", "", eqv_name, flags=re.IGNORECASE)
        return eqv_name.strip()
    return None


def clean_dosage_prefix(name: str) -> str:
    """移除成分名稱開頭的劑量資訊

    例如: "4.56MG DONEPEZIL FREE BASE" → "DONEPEZIL FREE BASE"
    """
    # 移除開頭的劑量（如 "4.56MG ", "100MG "）
    cleaned = re.sub(r"^\d+(\.\d+)?\s*(MG|G|MCG|IU|ML|%|UNIT)\s+", "", name, flags=re.IGNORECASE)
    # 移除結尾的括號殘餘
    cleaned = re.sub(r"\)$", "", cleaned)
    return cleaned.strip()


def normalize_ingredient(name: str) -> str:
    """標準化單一成分名稱

    處理邏輯：
    1. 移除開頭的劑量資訊
    2. 處理 HSA 的 EQV/EQUIVALENT TO 格式
    3. 移除括號內的同義詞（EQ TO ...）
    4. 移除其他括號內容（如 VIT B2）
    5. 移除 FREE BASE、B.P. 等後綴
    6. 英式 → 美式拼寫轉換
    7. 統一大小寫
    8. 移除多餘空白

    Args:
        name: 原始成分名稱

    Returns:
        標準化後的名稱
    """
    if not name:
        return ""

    # 統一大寫（先做，方便後續處理）
    name = name.upper().strip()

    # 移除開頭的劑量資訊
    name = clean_dosage_prefix(name)

    # 處理 HSA 的 EQV/EQUIVALENT TO 格式 - 提取標準名稱
    eqv_name = extract_eqv_name(name)
    if eqv_name:
        name = eqv_name.upper()
    else:
        # 如果沒有 EQV，移除結尾的劑量資訊
        name = re.sub(r"\s+\d+(\.\d+)?\s*(MG|G|MCG|IU|ML|%|UNIT).*$", "", name, flags=re.IGNORECASE)

    # 統一全形括號為半形
    name = name.replace("（", "(").replace("）", ")")

    # 移除括號內容（包含 EQ TO 的同義詞、VIT 等）
    # 但保留括號前的主名稱
    name = re.sub(r"\s*\([^)]*\)", "", name)

    # 移除 FREE BASE、B.P.、USP、BP 等後綴
    name = re.sub(r"\s+(FREE\s+)?BASE$", "", name)
    name = re.sub(r"\s+B\.?P\.?$", "", name)
    name = re.sub(r"\s+USP$", "", name)
    name = re.sub(r"\s+MICRONIZED$", "", name)
    name = re.sub(r"\s+ANHYDROUS$", "", name)

    # 英式 → 美式拼寫轉換
    name = normalize_british_spelling(name)

    # 移除多餘空白
    name = re.sub(r"\s+", " ", name)

    return name.strip()


def extract_ingredients(ingredient_str: str) -> List[str]:
    """從主成分略述欄位提取所有成分

    支援的分隔符：
    - 台灣 FDA: ; 或 ;;
    - 新加坡 HSA: && 或 ;

    Args:
        ingredient_str: 主成分略述欄位原始值

    Returns:
        標準化後的成分列表
    """
    if not ingredient_str:
        return []

    # 統一分隔符號
    # 台灣: ;; 或 ;
    # 新加坡 HSA: && 或 ;
    ingredient_str = ingredient_str.replace(";;", ";").replace("；", ";").replace("&&", ";")

    # 分割
    parts = ingredient_str.split(";")

    # 標準化每個成分
    ingredients = []
    for part in parts:
        normalized = normalize_ingredient(part)
        if normalized and normalized not in ingredients:
            ingredients.append(normalized)

    return ingredients


def extract_primary_ingredient(ingredient_str: str) -> str:
    """提取主要成分（第一個成分）

    Args:
        ingredient_str: 主成分略述欄位原始值

    Returns:
        主要成分名稱（標準化後）
    """
    ingredients = extract_ingredients(ingredient_str)
    return ingredients[0] if ingredients else ""


def strip_salt_suffix(name: str) -> Optional[str]:
    """移除鹽類後綴，返回基本名稱

    例如：METFORMIN HYDROCHLORIDE → METFORMIN
    """
    name_upper = name.upper()
    for suffix in SALT_SUFFIXES:
        pattern = rf"\s+{suffix}\b"
        if re.search(pattern, name_upper):
            base = re.sub(pattern, "", name_upper).strip()
            if base and base != name_upper:
                return base
    return None


def generate_name_variants(name: str) -> List[str]:
    """生成名稱變體以增加映射機會

    包含：
    1. 原始名稱（標準化後）
    2. 移除鹽類後綴的基本名稱
    3. 英式/美式拼寫變體
    """
    variants = []
    name_upper = name.upper().strip()

    # 1. 標準化名稱
    normalized = normalize_ingredient(name)
    if normalized:
        variants.append(normalized)

    # 2. 移除鹽類後綴
    base_name = strip_salt_suffix(normalized)
    if base_name and base_name not in variants:
        variants.append(base_name)

    # 3. 如果有 EQV 模式，也加入 EQV 前的名稱（可能是完整鹽類形式）
    eqv_name = extract_eqv_name(name_upper)
    if eqv_name:
        # 加入 EQV 後的名稱
        eqv_normalized = normalize_british_spelling(eqv_name.upper())
        if eqv_normalized and eqv_normalized not in variants:
            variants.append(eqv_normalized)

    return variants


def get_all_synonyms(ingredient_str: str) -> List[Tuple[str, List[str]]]:
    """提取成分及其所有同義詞

    從括號中的 EQ TO 或 HSA 的 EQV 格式提取同義詞

    Args:
        ingredient_str: 主成分略述欄位原始值

    Returns:
        [(主名稱, [同義詞列表]), ...]
    """
    if not ingredient_str:
        return []

    # 統一分隔符號
    ingredient_str = ingredient_str.replace(";;", ";").replace("；", ";")
    parts = ingredient_str.split(";")

    results = []
    for part in parts:
        part = part.strip()
        if not part:
            continue

        # 統一括號
        part = part.replace("（", "(").replace("）", ")")

        # 優先處理 HSA 的 EQV 格式
        eqv_name = extract_eqv_name(part)
        if eqv_name:
            main_name = normalize_british_spelling(eqv_name.upper())
            # EQV 前面的部分作為同義詞（通常是鹽類形式）
            pre_eqv = re.split(r"\s+EQV\s+", part, flags=re.IGNORECASE)[0]
            pre_eqv = normalize_british_spelling(pre_eqv.upper().strip())
            synonyms = [pre_eqv] if pre_eqv and pre_eqv != main_name else []
        else:
            # 提取主名稱（括號前的部分）
            main_match = re.match(r"^([^(]+)", part)
            if not main_match:
                continue

            main_name = main_match.group(1).strip().upper()
            main_name = re.sub(r"\s+", " ", main_name)
            main_name = normalize_british_spelling(main_name)

            synonyms = []

        # 提取所有 EQ TO 同義詞（台灣格式）
        eq_matches = re.findall(r"EQ TO\s+([^)]+)", part, re.IGNORECASE)
        for match in eq_matches:
            syn = match.strip().upper()
            syn = re.sub(r"\s+", " ", syn)
            syn = re.sub(r"\s*\(.*$", "", syn)
            syn = normalize_british_spelling(syn)
            if syn and syn != main_name and syn not in synonyms:
                synonyms.append(syn)

        # 加入移除鹽類後綴的基本名稱
        base_name = strip_salt_suffix(main_name)
        if base_name and base_name != main_name and base_name not in synonyms:
            synonyms.append(base_name)

        results.append((main_name, synonyms))

    return results
