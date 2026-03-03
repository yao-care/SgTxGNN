---
layout: default
title: Resources
nav_order: 9
has_children: true
description: "Data sources, downloads, and research resources"
permalink: /resources/
---

# Resources
{: .fs-9 }

Data sources, downloads, and research materials
{: .fs-6 .fw-300 }

---

## Available Resources

| Resource | Description |
|----------|-------------|
| [Data Sources]({{ '/resources/sources/' | relative_url }}) | Information about our data sources |
| [Data Downloads]({{ '/resources/downloads/' | relative_url }}) | Download datasets in various formats |
| [Research Cases]({{ '/resources/case-studies/' | relative_url }}) | Example analyses and tutorials |

---

## Quick Downloads

### Prediction Data

| File | Format | Description |
|------|--------|-------------|
| [Unified Predictions]({{ '/data/unified_predictions.csv' | relative_url }}) | CSV | All 31,543 predictions |
| [Drug List]({{ '/data/drugs.json' | relative_url }}) | JSON | 745 drugs with metadata |
| [Search Index]({{ '/data/search-index.json' | relative_url }}) | JSON | Full searchable index |

### FHIR Resources

| Resource | Endpoint |
|----------|----------|
| Capability Statement | `/fhir/metadata` |
| MedicationKnowledge | `/fhir/MedicationKnowledge/{id}` |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/{id}` |

---

## Citation

If you use SgTxGNN data in your research, please cite:

```bibtex
@software{sgtxgnn2026,
  author       = {Yao.Care},
  title        = {SgTxGNN: Drug Repurposing Predictions for Singapore},
  year         = 2026,
  url          = {https://sgtxgnn.yao.care}
}
```

And the original TxGNN paper:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

## External Resources

### TxGNN

- [TxGNN Project Page](https://zitniklab.hms.harvard.edu/projects/TxGNN/)
- [TxGNN Paper](https://www.nature.com/articles/s41591-023-02233-x)
- [TxGNN Explorer](http://txgnn.org)
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)

### Singapore Healthcare

- [HSA Singapore](https://www.hsa.gov.sg/)
- [MOH Singapore](https://www.moh.gov.sg/)
- [data.gov.sg](https://data.gov.sg/)

### Drug Databases

- [DrugBank](https://go.drugbank.com/)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)

---

## API Access

SgTxGNN data is available via FHIR API:

```bash
# Get drug information
curl https://sgtxgnn.yao.care/fhir/MedicationKnowledge/DB00945

# Get predictions for a drug
curl https://sgtxgnn.yao.care/fhir/ClinicalUseDefinition?subject=MedicationKnowledge/DB00945
```

See [FHIR API Documentation]({{ '/smart/fhir-api/' | relative_url }}) for details.

---

<div class="disclaimer">
<strong>Terms of Use</strong><br>
SgTxGNN data is provided for research and educational purposes. Commercial use requires separate licensing. See individual data source terms for specific restrictions.
</div>
