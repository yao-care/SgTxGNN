# SgTxGNN

Singapore drug repurposing predictions using TxGNN.

## Overview

This project uses TxGNN (Therapeutic Target Prediction using Graph Neural Networks) to identify potential drug repurposing candidates for Singapore's approved medications.

## Installation

```bash
uv sync
```

## Usage

```bash
# Process HSA (Health Sciences Authority) drug data
uv run python scripts/process_fda_data.py

# Prepare vocabulary data
uv run python scripts/prepare_external_data.py

# Run knowledge graph predictions
uv run python scripts/run_kg_prediction.py

# Generate FHIR resources
uv run python scripts/generate_fhir_resources.py
```

## Disclaimer

This project is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
