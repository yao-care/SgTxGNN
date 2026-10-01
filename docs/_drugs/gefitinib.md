---
layout: default
title: Gefitinib
parent: Low Evidence (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
---

# Gefitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Gefitinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Gefitinib is an oral EGFR tyrosine kinase inhibitor, used for non-small cell lung cancer (NSCLC). The TxGNN model predicts it may be effective for **gingival fibromatosis** with a very high score (99.89%), but **no clinical trials and no publications** currently support this direction, so it is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (from general drug knowledge and the retrieved literature; the Singapore licence records contain no indication text) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.89% (model rank 2108) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source data. Gefitinib is a selective inhibitor of the epidermal growth factor receptor (EGFR), a receptor that controls cell growth, survival and angiogenesis. Its efficacy in EGFR-mutant NSCLC is well established. Mechanistically, it may be applicable to gingival fibromatosis.

Gingival fibromatosis is a non-cancerous overgrowth of gum tissue. The only link the analysis offers is that EGFR signalling can drive fibroblast proliferation. This link is conceivable but **untested**. No study in the evidence pack connects gefitinib or EGFR inhibition to this condition.

The very high TxGNN score reflects a network-based association in the knowledge graph. It is not disease-specific evidence. It should be read as a hypothesis, not a finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16722P | GEFITINIB-TEVA FC TABLET 250MG | Film-coated tablet | Teva Pharmaceutical Industries, Ltd. |
| SIN16030P | VEIASU FILM-COATED TABLETS 250 MG | Film-coated tablet | Lotus Pharmaceutical Co., Ltd Nantou Plant |
| SIN16055P | INGEFITINIB FILM COATED TABLET 250MG | Film-coated tablet | REMEDICA LTD |
| SIN16130P | GEFTINAT FILM COATED TABLETS 250 MG | Film-coated tablet | Natco Pharma Limited - Pharma Division |
| SIN15984P | HOVID GEFITINIB TABLETS 250 MG | Film-coated tablet | Qilu Pharmaceutical (Hainan) Co. Ltd. |

All five products are oral tablets. The approved indication text is not recorded in the licence data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Low, as expected for this class; please refer to the package insert |
| Emetogenicity Classification | Low, as expected for this class; please refer to the package insert |
| Monitoring Items | Liver function is a typical monitoring item for this class; please refer to the package insert for the full list |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN score. There are no trials and no relevant publications for gingival fibromatosis, and the proposed EGFR–fibroblast link is untested. Package insert safety data has not been retrieved, which blocks safety screening.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (currently blocking)
- Mechanism of action data from DrugBank
- A targeted literature search for gefitinib or EGFR inhibition in gingival fibromatosis or fibroblast overgrowth, plus preclinical evidence
- Route and formulation assessment, since the only Singapore forms are oral tablets

**Other candidates:** Lung hilum carcinoma (rank 5) is probably an NSCLC anatomical subtype, so it is largely an on-label scenario rather than true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

