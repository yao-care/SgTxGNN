"""老藥新用預測模組"""

from .repurposing import (
    load_drug_disease_relations,
    find_repurposing_candidates,
    generate_repurposing_report,
)

__all__ = [
    # Knowledge Graph based
    "load_drug_disease_relations",
    "find_repurposing_candidates",
    "generate_repurposing_report",
]

# 嘗試導入可選模組
try:
    from .txgnn_model import (
        TxGNNPredictor,
        CheckpointManager,
        detect_device,
        check_dependencies,
        download_pretrained_model,
        download_kg_data,
        run_taiwan_drug_prediction,
    )
    __all__.extend([
        "TxGNNPredictor",
        "CheckpointManager",
        "detect_device",
        "check_dependencies",
        "download_pretrained_model",
        "download_kg_data",
        "run_taiwan_drug_prediction",
    ])
except ImportError:
    # TxGNN 深度學習模組需要額外依賴
    pass
