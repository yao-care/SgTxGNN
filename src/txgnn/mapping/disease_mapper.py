"""疾病映射模組 - Singapore 版本

由於 HSA 資料無適應症欄位，本模組採用 ATC 代碼推斷疾病類別的策略。
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# ATC 第一層分類 → 常見疾病類別
# 這個映射用於從 ATC 代碼推斷可能的適應症類別
ATC_TO_DISEASE_CATEGORIES = {
    "A": [  # 消化道及代謝
        "diabetes", "diabetes mellitus", "type 2 diabetes",
        "gastroesophageal reflux", "peptic ulcer", "gastritis",
        "constipation", "diarrhea", "nausea", "vomiting",
        "obesity", "malnutrition", "vitamin deficiency",
    ],
    "B": [  # 血液及造血器官
        "anemia", "thrombosis", "deep vein thrombosis",
        "pulmonary embolism", "coagulation disorder",
        "thrombocytopenia", "hemophilia", "bleeding disorder",
    ],
    "C": [  # 心血管系統
        "hypertension", "heart failure", "coronary artery disease",
        "myocardial infarction", "angina", "arrhythmia",
        "atrial fibrillation", "hyperlipidemia", "atherosclerosis",
        "peripheral vascular disease", "edema",
    ],
    "D": [  # 皮膚病
        "psoriasis", "eczema", "dermatitis", "acne",
        "fungal skin infection", "bacterial skin infection",
        "urticaria", "pruritus", "wound", "burn",
    ],
    "G": [  # 泌尿生殖系統及性激素
        "urinary tract infection", "benign prostatic hyperplasia",
        "erectile dysfunction", "menopause", "endometriosis",
        "contraception", "infertility", "vaginal infection",
    ],
    "H": [  # 全身性激素製劑
        "hypothyroidism", "hyperthyroidism", "adrenal insufficiency",
        "cushing syndrome", "growth hormone deficiency",
        "diabetes insipidus", "hypopituitarism",
    ],
    "J": [  # 全身性抗感染藥
        "bacterial infection", "pneumonia", "sepsis",
        "urinary tract infection", "skin infection",
        "viral infection", "influenza", "herpes",
        "fungal infection", "tuberculosis", "hiv infection",
    ],
    "L": [  # 抗腫瘤及免疫調節劑
        "cancer", "breast cancer", "lung cancer", "colon cancer",
        "leukemia", "lymphoma", "multiple myeloma",
        "rheumatoid arthritis", "psoriatic arthritis",
        "crohn disease", "ulcerative colitis", "multiple sclerosis",
    ],
    "M": [  # 肌肉骨骼系統
        "rheumatoid arthritis", "osteoarthritis", "gout",
        "osteoporosis", "back pain", "muscle spasm",
        "fibromyalgia", "bursitis", "tendinitis",
    ],
    "N": [  # 神經系統
        "epilepsy", "migraine", "headache", "neuropathic pain",
        "parkinson disease", "alzheimer disease", "dementia",
        "depression", "anxiety", "schizophrenia", "bipolar disorder",
        "insomnia", "adhd", "opioid dependence",
    ],
    "P": [  # 抗寄生蟲藥
        "malaria", "helminth infection", "scabies",
        "pediculosis", "amebiasis", "giardiasis",
    ],
    "R": [  # 呼吸系統
        "asthma", "copd", "chronic obstructive pulmonary disease",
        "allergic rhinitis", "cough", "bronchitis",
        "pneumonia", "respiratory tract infection",
    ],
    "S": [  # 感覺器官
        "glaucoma", "dry eye", "conjunctivitis", "macular degeneration",
        "cataract", "otitis media", "hearing loss",
    ],
    "V": [  # 其他
        "diagnostic agent", "contrast medium", "antidote",
        "nutritional supplement",
    ],
}

# 常見英文疾病名稱標準化（同義詞 → 標準名稱）
DISEASE_SYNONYMS = {
    # 糖尿病
    "dm": "diabetes mellitus",
    "t2dm": "type 2 diabetes mellitus",
    "type ii diabetes": "type 2 diabetes mellitus",
    "niddm": "type 2 diabetes mellitus",
    "t1dm": "type 1 diabetes mellitus",
    "iddm": "type 1 diabetes mellitus",

    # 高血壓
    "htn": "hypertension",
    "high blood pressure": "hypertension",
    "elevated blood pressure": "hypertension",

    # 心臟病
    "cad": "coronary artery disease",
    "ihd": "ischemic heart disease",
    "chd": "coronary heart disease",
    "mi": "myocardial infarction",
    "heart attack": "myocardial infarction",
    "chf": "congestive heart failure",
    "hf": "heart failure",
    "af": "atrial fibrillation",
    "afib": "atrial fibrillation",

    # 呼吸系統
    "copd": "chronic obstructive pulmonary disease",
    "rti": "respiratory tract infection",
    "urti": "upper respiratory tract infection",
    "lrti": "lower respiratory tract infection",

    # 感染
    "uti": "urinary tract infection",
    "ssti": "skin and soft tissue infection",
    "tb": "tuberculosis",

    # 癌症
    "ca": "cancer",
    "nsclc": "non-small cell lung cancer",
    "sclc": "small cell lung cancer",
    "crc": "colorectal cancer",
    "hcc": "hepatocellular carcinoma",
    "rcc": "renal cell carcinoma",
    "aml": "acute myeloid leukemia",
    "cml": "chronic myeloid leukemia",
    "all": "acute lymphoblastic leukemia",
    "cll": "chronic lymphocytic leukemia",
    "nhl": "non-hodgkin lymphoma",
    "mm": "multiple myeloma",

    # 精神/神經
    "mdd": "major depressive disorder",
    "gad": "generalized anxiety disorder",
    "ocd": "obsessive compulsive disorder",
    "ptsd": "post traumatic stress disorder",
    "pd": "parkinson disease",
    "ad": "alzheimer disease",
    "ms": "multiple sclerosis",

    # 其他
    "ra": "rheumatoid arthritis",
    "oa": "osteoarthritis",
    "ibd": "inflammatory bowel disease",
    "uc": "ulcerative colitis",
    "cd": "crohn disease",
    "gerd": "gastroesophageal reflux disease",
    "bph": "benign prostatic hyperplasia",
    "dvt": "deep vein thrombosis",
    "pe": "pulmonary embolism",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 小寫版本
        index[disease_name.upper()] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:
                index[kw] = (disease_id, disease_name)

    return index


def normalize_disease_name(name: str) -> str:
    """標準化疾病名稱"""
    name_lower = name.lower().strip()

    # 查找同義詞
    if name_lower in DISEASE_SYNONYMS:
        return DISEASE_SYNONYMS[name_lower]

    return name_lower


def get_diseases_for_atc(atc_code: str) -> List[str]:
    """根據 ATC 代碼取得可能的疾病類別"""
    if not atc_code or len(atc_code) < 1:
        return []

    first_level = atc_code[0].upper()
    return ATC_TO_DISEASE_CATEGORIES.get(first_level, [])


def map_atc_to_diseases(
    atc_code: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將 ATC 代碼映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 取得 ATC 對應的疾病類別
    disease_categories = get_diseases_for_atc(atc_code)

    for category in disease_categories:
        category_upper = category.upper()

        # 完全匹配
        if category_upper in disease_index:
            disease_id, disease_name = disease_index[category_upper]
            results.append((disease_id, disease_name, 0.7))  # ATC 推斷的信心度較低
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if category_upper in index_kw or index_kw in category_upper:
                results.append((disease_id, disease_name, 0.5))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:10]  # 最多返回 10 個匹配


def map_fda_drugs_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    atc_field: str = "atc_code",
    license_field: str = "licence_no",
    brand_field: str = "product_name",
) -> pd.DataFrame:
    """將藥品 ATC 代碼映射到 TxGNN 疾病

    由於 HSA 資料無適應症欄位，使用 ATC 代碼推斷疾病類別。
    """
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        atc_code = row.get(atc_field, "")

        if not atc_code or pd.isna(atc_code):
            continue

        # 使用 ATC 代碼映射
        matches = map_atc_to_diseases(str(atc_code), disease_index)

        if matches:
            for disease_id, disease_name, confidence in matches:
                results.append({
                    "license_id": row.get(license_field, ""),
                    "brand_name": row.get(brand_field, ""),
                    "atc_code": atc_code,
                    "disease_id": disease_id,
                    "disease_name": disease_name,
                    "confidence": confidence,
                    "mapping_method": "atc_inference",
                })

    return pd.DataFrame(results)


def get_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算映射統計"""
    total = len(mapping_df)
    unique_drugs = mapping_df["license_id"].nunique() if "license_id" in mapping_df.columns else 0
    unique_diseases = mapping_df["disease_id"].nunique() if "disease_id" in mapping_df.columns else 0

    return {
        "total_mappings": total,
        "unique_drugs": unique_drugs,
        "unique_diseases": unique_diseases,
    }
