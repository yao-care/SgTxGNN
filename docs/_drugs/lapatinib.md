---
layout: default
title: Lapatinib
parent: Low Evidence (L5)
nav_order: 572
evidence_level: L5
indication_count: 10
---

# Lapatinib
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

# Lapatinib: From HER2-Positive Breast Cancer to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib is an oral EGFR/HER2 kinase inhibitor, and the literature in the evidence pack places it in HER2-positive breast cancer. The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (the Singapore registration record does not state an indication, so this is inferred from the supplied literature) |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on the supplied papers and rationale text, lapatinib inhibits EGFR and HER2 and is used in HER2-positive breast cancer.

The link to DFSP is weak. DFSP is driven by the COL1A1-PDGFB fusion, which acts through PDGFRB signalling, not EGFR/HER2. The high score (0.993) most likely reflects proximity to other sarcomas in the knowledge graph, not a validated mechanism. No direct mechanistic link was identified, and no trials or literature were retrieved. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for dermatofibrosarcoma protuberans.

Other predicted candidates were also reviewed. None has trial evidence, and the literature is preclinical or indirect:

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Plasmodium falciparum malaria | 98.02% | L4 | Best-supported candidate. [PMID 32235391](https://pubmed.ncbi.nlm.nih.gov/32235391/) (2020, *Molecules*) reports in vitro that lapatinib inhibits haemozoin formation in malaria parasites. Two related medicinal-chemistry papers ([29301082](https://pubmed.ncbi.nlm.nih.gov/29301082/), [25685309](https://pubmed.ncbi.nlm.nih.gov/25685309/)) study lapatinib-derived scaffolds, not lapatinib itself. No human data exist. Classified as a research question. |
| Fibroblastic neoplasm | 98.43% | L4 | [PMID 34239043](https://pubmed.ncbi.nlm.nih.gov/34239043/) (2021, *Oncogene*) concerns stromal-driven lapatinib resistance in HER2-positive breast cancer. It is indirect and does not support efficacy in this indication. |
| Lymphangiomyoma | 97.29% | L4 | [PMID 20979677](https://pubmed.ncbi.nlm.nih.gov/20979677/) (2010, *Respiratory Care*) is a case report of chemotherapy-associated pneumothoraces in lymphangioleiomyomatosis (LAM). It gives no evidence of efficacy, and LAM is driven by mTOR, not EGFR/HER2. |
| Conventional fibrosarcoma, kidney fibrosarcoma, heart fibrosarcoma, low grade fibromyxoid sarcoma, cysticercosis, coenurosis | 97.45–98.36% | L5 | Prediction only. No trials or literature, and no plausible mechanism identified. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13366P | Tykerb tablet 250mg | Tablet, film coated (oral) | Not stated in the registration record |

Manufacturer: Glaxo Operations UK Ltd (trading as GlaxoWellcome Operations) and Sandoz S.R.L.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR/HER2 kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No interactions were found in the drug interaction query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (DFSP) has no supporting trials or literature, and its known driver (PDGFRB signalling) does not match lapatinib's EGFR/HER2 target. The only candidate with a plausible mechanism is malaria, and that evidence is preclinical and in vitro only, so it is better treated as a research question than a repurposing candidate.

**To proceed, the following is needed:**
- The HSA package insert, to obtain warnings, contraindications and the approved indication (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For DFSP: preclinical evidence of EGFR/HER2 or PDGFRB-pathway activity of lapatinib in DFSP models
- For malaria: exposure versus effective concentration data, anti-plasmodial dosing and safety, and comparison with existing antimalarials

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

