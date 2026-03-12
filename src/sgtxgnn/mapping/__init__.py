"""實體映射模組"""

from .normalizer import (
    normalize_ingredient,
    extract_ingredients,
    get_all_synonyms,
    generate_name_variants,
    strip_salt_suffix,
    normalize_british_spelling,
    BRITISH_TO_AMERICAN,
    SALT_SUFFIXES,
)
from .drugbank_mapper import (
    load_drugbank_vocab,
    build_name_index,
    map_ingredient_to_drugbank,
    map_fda_drugs_to_drugbank,
    get_mapping_stats,
)
from .disease_mapper import (
    load_disease_vocab,
    build_disease_index,
    normalize_disease_name,
    get_diseases_for_atc,
    map_atc_to_diseases,
    map_fda_drugs_to_diseases,
    get_mapping_stats as get_disease_mapping_stats,
    ATC_TO_DISEASE_CATEGORIES,
    DISEASE_SYNONYMS,
)

__all__ = [
    # Normalizer
    "normalize_ingredient",
    "extract_ingredients",
    "get_all_synonyms",
    "generate_name_variants",
    "strip_salt_suffix",
    "normalize_british_spelling",
    "BRITISH_TO_AMERICAN",
    "SALT_SUFFIXES",
    # Drug mapping
    "load_drugbank_vocab",
    "build_name_index",
    "map_ingredient_to_drugbank",
    "map_fda_drugs_to_drugbank",
    "get_mapping_stats",
    # Disease mapping (Singapore: ATC-based)
    "load_disease_vocab",
    "build_disease_index",
    "normalize_disease_name",
    "get_diseases_for_atc",
    "map_atc_to_diseases",
    "map_fda_drugs_to_diseases",
    "get_disease_mapping_stats",
    "ATC_TO_DISEASE_CATEGORIES",
    "DISEASE_SYNONYMS",
]
