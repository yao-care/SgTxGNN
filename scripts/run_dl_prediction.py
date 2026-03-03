#!/usr/bin/env python3
"""執行 TxGNN 深度學習預測 - Singapore HSA 版本

使用 TxGNN 深度學習模型進行老藥新用預測。
需要額外安裝 PyTorch、DGL 和 TxGNN。

使用方法:
    uv run python scripts/run_dl_prediction.py

前置條件:
    1. 已執行 run_kg_prediction.py（產生 drug_mapping.csv）
    2. 已安裝深度學習依賴（見下方說明）
    3. 已下載 TxGNN 預訓練模型

安裝深度學習依賴:
    # 建議使用獨立的 conda 環境
    conda create -n txgnn python=3.11 -y
    conda activate txgnn

    # CPU 版本（macOS / Linux）
    pip install torch==2.2.2 torchvision==0.17.2
    pip install dgl==1.1.3

    # 或 CUDA 版本（Linux/Windows with NVIDIA GPU）
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
    pip install dgl -f https://data.dgl.ai/wheels/cu118/repo.html

    # 安裝 TxGNN
    pip install git+https://github.com/mims-harvard/TxGNN.git
    pip install pandas tqdm pyyaml pydantic ogb gdown

下載預訓練模型:
    # 模型會自動下載，或手動下載：
    # https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj
    # 解壓縮到 model_ckpt/ 目錄

產生檔案:
    data/processed/txgnn_dl_predictions.csv
"""

import sys
from pathlib import Path


def check_and_run():
    """檢查依賴並執行預測"""
    print("=" * 60)
    print("TxGNN 深度學習預測 - Singapore HSA")
    print("=" * 60)
    print()

    # 嘗試導入依賴
    missing = []

    try:
        import torch
        print(f"✓ PyTorch {torch.__version__}")
        if torch.cuda.is_available():
            print(f"  CUDA 可用: {torch.cuda.get_device_name(0)}")
        else:
            print("  使用 CPU 模式")
    except ImportError:
        missing.append("torch")
        print("✗ PyTorch 未安裝")

    try:
        import dgl
        print(f"✓ DGL {dgl.__version__}")
    except ImportError:
        missing.append("dgl")
        print("✗ DGL 未安裝")

    try:
        import txgnn
        print("✓ TxGNN")
    except ImportError:
        missing.append("TxGNN")
        print("✗ TxGNN 未安裝")

    print()

    if missing:
        print("=" * 60)
        print("缺少必要套件，請按照以下步驟安裝：")
        print("=" * 60)
        print()
        print("# 建議使用獨立的 conda 環境")
        print("conda create -n txgnn python=3.11 -y")
        print("conda activate txgnn")
        print()
        print("# CPU 版本（macOS / Linux）")
        print("pip install torch==2.2.2 torchvision==0.17.2")
        print("pip install dgl==1.1.3")
        print()
        print("# 安裝 TxGNN 和其他依賴")
        print("pip install git+https://github.com/mims-harvard/TxGNN.git")
        print("pip install pandas tqdm pyyaml pydantic ogb gdown")
        print()
        print("# 然後重新執行此腳本")
        print("python scripts/run_dl_prediction.py")
        print()
        return 1

    # 檢查必要檔案
    base_dir = Path(__file__).parent.parent
    drug_mapping_path = base_dir / "data" / "processed" / "drug_mapping.csv"

    if not drug_mapping_path.exists():
        print(f"✗ 找不到藥物映射檔案: {drug_mapping_path}")
        print("  請先執行: uv run python scripts/run_kg_prediction.py")
        return 1

    print(f"✓ 藥物映射: {drug_mapping_path}")
    print()

    # 執行預測（使用本地模組）
    import sys
    import importlib.util

    # 直接載入本地模組
    spec = importlib.util.spec_from_file_location(
        "txgnn_model",
        base_dir / "src" / "txgnn" / "predict" / "txgnn_model.py"
    )
    txgnn_model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(txgnn_model)
    run_taiwan_drug_prediction = txgnn_model.run_taiwan_drug_prediction

    print("開始執行 TxGNN 深度學習預測...")
    print("（支援中斷續算，可隨時 Ctrl+C 中斷）")
    print()

    try:
        result = run_taiwan_drug_prediction(
            drug_mapping_path=drug_mapping_path,
            output_path=base_dir / "data" / "processed" / "txgnn_dl_predictions.csv",
            min_score=0.5,  # 只保留分數 > 0.5 的預測
            top_k_per_drug=50,  # 每個藥物保留前 50 個疾病
        )

        print()
        print("=" * 60)
        print("深度學習預測完成！")
        print("=" * 60)

        if len(result) > 0:
            print(f"  總預測數: {len(result)}")
            print(f"  獨特藥物: {result['drugbank_id'].nunique()}")
            print(f"  獨特疾病: {result['潛在新適應症'].nunique()}")

        return 0

    except Exception as e:
        print(f"執行時發生錯誤: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(check_and_run())
