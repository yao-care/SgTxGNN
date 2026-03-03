# SgTxGNN - Drug Repurposing Predictions for Singapore

[![Website](https://img.shields.io/badge/Website-sgtxgnn.yao.care-blue)](https://sgtxgnn.yao.care)
[![FHIR R4](https://img.shields.io/badge/FHIR-R4-green)](https://sgtxgnn.yao.care/fhir/metadata)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Drug repurposing predictions for Singapore HSA-approved medications using Harvard's TxGNN model.

## Disclaimer

- **This project is for research purposes only and does not constitute medical advice**
- All drug repurposing candidates require clinical validation before application
- Predictions should not be used for direct clinical decision-making

## Project Overview

### Key Statistics

| Metric | Value |
|--------|-------|
| **Drugs Analysed** | 745 |
| **Repurposing Predictions** | 31,543 |
| **Diseases Covered** | 4,589 |
| **Dual-Validated (KG+DL)** | 1,217 |

### Evidence Level Distribution

| Level | Count | Description |
|-------|-------|-------------|
| **L1** | - | Multiple Phase 3 RCTs |
| **L2** | - | Single RCT or Phase 2 trials |
| **L3** | - | Observational studies |
| **L4** | 1,217 | Preclinical/mechanistic (KG+DL) |
| **L5** | 30,326 | Model prediction only |

---

## Prediction Methods

Following TxGNN's design, two prediction methods are available:

| Method | Speed | Precision | Requirements | Output |
|--------|-------|-----------|--------------|--------|
| Knowledge Graph | Fast (seconds) | Lower | None | `repurposing_candidates.csv` |
| Deep Learning | Slow (hours) | Higher | Conda + PyTorch + DGL | `txgnn_checkpoint.csv` |

**Key Difference**: The Knowledge Graph method directly queries known drug-disease relationships; the Deep Learning method uses neural network models to infer potential relationships and compute confidence scores.

### Knowledge Graph Method

```bash
uv run python scripts/run_kg_prediction.py
```

Directly queries drug-disease relationships in the TxGNN knowledge graph.

**Output**: `data/processed/repurposing_candidates.csv`

| Metric | Value |
|--------|-------|
| HSA Total Drugs | 11,466 |
| Mapped to DrugBank | 745 (6.5%) |
| DrugBank Mapping Rate | 73.87% |
| Diseases Mapped | 166 |
| Repurposing Candidates | 22,136 |

### Deep Learning Method

```bash
# Requires conda environment with PyTorch + DGL
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

Uses TxGNN's pre-trained neural network model to compute prediction scores.

**Output**: `data/processed/txgnn_checkpoint.csv`

| Metric | Value |
|--------|-------|
| Total Predictions | 29,100 |
| Drugs Involved | 745 |
| Average Confidence | 0.85+ |
| High Confidence (>0.99) | 1,217 |

### Unified Predictions

Both methods are merged into a single output:

**Output**: `data/processed/unified_predictions.csv`

| Source | Count | Description |
|--------|-------|-------------|
| **KG+DL** | 1,217 | Validated by both methods (highest confidence) |
| **DL only** | 27,883 | Deep Learning prediction |
| **KG only** | 2,443 | Knowledge Graph prediction |
| **Total** | 31,543 | All unique predictions |

---

## Quick Start

### Step 1: Download Data

| File | Source | Location | Purpose |
|------|--------|----------|---------|
| HSA Drug Data | [data.gov.sg](https://data.gov.sg/) | `data/raw/` | Singapore drug registry |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | `data/node.csv` | Node data |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | `data/kg.csv` | Knowledge graph |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | `data/edges.csv` | Edge data (for DL) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | `model_ckpt/` | Pre-trained model (for DL) |

### Step 2: Install Dependencies

```bash
# Install basic dependencies
uv sync

# Run tests
uv run pytest tests/
```

### Step 3: Process HSA Data

```bash
uv run python scripts/process_fda_data.py
```

This generates `data/raw/sg_hsa_drugs.json`.

### Step 4: Prepare Vocabulary Data

```bash
uv run python scripts/prepare_external_data.py
```

This generates files in `data/external/`:
- `drugbank_vocab.csv` - DrugBank vocabulary
- `disease_vocab.csv` - Disease vocabulary
- `drug_disease_relations.csv` - Drug-disease relationships

### Step 5: Run Predictions

```bash
# Knowledge Graph method
uv run python scripts/run_kg_prediction.py

# Deep Learning method (requires conda environment)
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

### Step 6: Generate FHIR Resources

```bash
uv run python scripts/generate_fhir_resources.py
```

---

## SMART on FHIR Integration

SgTxGNN provides a SMART on FHIR app for EHR integration.

### Features

- View patient medications from EHR
- Display repurposing predictions for current medications
- Evidence-based insights with source attribution

### Testing

Use the [SMART App Launcher](https://launch.smarthealthit.org/) with:

```
Launch URL: https://sgtxgnn.yao.care/smart/launch.html
FHIR Version: R4
```

### FHIR Resources

| Endpoint | Description |
|----------|-------------|
| `/fhir/metadata` | CapabilityStatement |
| `/fhir/MedicationKnowledge/{id}` | Drug information |
| `/fhir/ClinicalUseDefinition/{id}` | Repurposing predictions |

---

## Data Sources

| Source | Provider | Description |
|--------|----------|-------------|
| **TxGNN** | Harvard Medical School | Core prediction model |
| **HSA** | Health Sciences Authority | Singapore drug registry |
| **DrugBank** | University of Alberta | Drug-target database |
| **ClinicalTrials.gov** | NIH | Clinical trial registry |
| **PubMed** | NIH | Biomedical literature |

---

## Project Structure

```
SgTxGNN/
├── README.md                    # Project documentation
├── CLAUDE.md                    # AI assistant guide
├── pyproject.toml               # Python package config
│
├── data/                        # Data directory
│   ├── kg.csv                   # TxGNN knowledge graph
│   ├── node.csv                 # TxGNN node data
│   ├── raw/
│   │   └── sg_hsa_drugs.json    # Singapore HSA drug data
│   ├── external/                # Generated by prepare_external_data.py
│   │   ├── drugbank_vocab.csv
│   │   ├── disease_vocab.csv
│   │   └── drug_disease_relations.csv
│   └── processed/
│       ├── drug_mapping.csv           # Drug → DrugBank mapping
│       ├── disease_mapping.csv        # Indication → Disease mapping
│       ├── repurposing_candidates.csv # KG method results
│       ├── txgnn_checkpoint.csv       # DL method results
│       └── unified_predictions.csv    # Merged predictions
│
├── model_ckpt/                  # TxGNN pre-trained model
│   ├── model.pt
│   └── ...
│
├── src/txgnn/                   # Core code
│   ├── data/
│   │   └── loader.py            # HSA data loader
│   ├── mapping/
│   │   ├── normalizer.py        # Drug name normalisation
│   │   ├── drugbank_mapper.py   # DrugBank ID mapping
│   │   └── disease_mapper.py    # Indication → Disease mapping
│   ├── predict/
│   │   ├── repurposing.py       # KG method prediction
│   │   └── txgnn_model.py       # DL method prediction
│   └── collectors/              # Evidence collection
│       ├── base.py
│       ├── clinicaltrials.py
│       ├── pubmed.py
│       ├── drugbank.py
│       └── sghsa.py             # Singapore HSA collector
│
├── scripts/                     # Execution scripts
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   ├── run_txgnn_prediction.py
│   └── generate_fhir_resources.py
│
├── docs/                        # Website (Jekyll)
│   ├── _config.yml
│   ├── index.md
│   ├── _drugs/                  # 745 drug pages
│   ├── smart/                   # SMART on FHIR app
│   │   ├── launch.html
│   │   └── app.html
│   └── fhir/                    # FHIR resources
│       └── metadata
│
└── tests/                       # Test suite
    ├── test_loader.py
    ├── test_normalizer.py
    └── ...
```

---

## Related Resources

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine 2023
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org) - Interactive prediction explorer
- [TwTxGNN](https://twtxgnn.yao.care) - Taiwan version

---

## Citation

If you use this dataset or software, please cite:

```bibtex
@software{sgtxgnn2026,
  author       = {Yao.Care},
  title        = {SgTxGNN: Drug Repurposing Predictions for Singapore HSA-Approved Medications},
  year         = 2026,
  url          = {https://sgtxgnn.yao.care}
}
```

Please also cite the original TxGNN paper:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and Chandak, Payal and Wang, Qianwen and Haber, Shreyas and Zitnik, Marinka},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/yao-care/SgTxGNN).
