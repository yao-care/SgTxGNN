---
layout: default
title: Gallium Nitrate
parent: 僅模型預測 (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
---

# Gallium Nitrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Gallium Nitrate: From Cancer-Related Hypercalcemia to Sickle Cell-Hemoglobin C Disease Syndrome

## One-Sentence Summary

Gallium nitrate is a metal-based compound originally developed as an antineoplastic agent and best known for treating cancer-related hypercalcemia.
The TxGNN model assigns it the highest prediction score of **98.18%** for **Sickle Cell-Hemoglobin C Disease Syndrome**, but this is currently supported by **0 clinical trials and 0 publications**.
Notably, a closely ranked prediction — **Plasma Cell Myeloma (rank 6, score 98.12%)** — is backed by **9 publications** including a pilot RCT, and represents the most actionable research direction in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cancer-related hypercalcemia (inferred from literature; not registered in Singapore) |
| Predicted New Indication | Sickle Cell-Hemoglobin C Disease Syndrome |
| TxGNN Prediction Score | 98.18% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Gallium (Ga³⁺) chemically mimics ferric iron (Fe³⁺) due to a nearly identical ionic radius and charge. Inside cells, gallium competes with iron at the active sites of iron-dependent enzymes — most notably **ribonucleotide reductase (RNR)**, the rate-limiting enzyme for DNA precursor synthesis. By displacing iron and rendering RNR non-functional, gallium inhibits cellular proliferation. This mechanism underlies its original antitumor activity and also explains its potent effects on bone resorption, since osteoclasts are metabolically iron-dependent.

For sickle cell disease, the theoretical link runs through iron oxidation: hemoglobin S (HbS) undergoes iron-mediated oxidation that promotes polymerization and sickling under low-oxygen conditions. Gallium's competitive displacement of Fe³⁺ could theoretically modulate this process. However, this reasoning is entirely inferential — no laboratory studies in sickle cell models, no animal experiments, and no human data have been published to support gallium nitrate in HbSC disease specifically.

The identical TxGNN prediction score across all five sickle cell variants in this pack (all 0.9818) is a clear signal that this is a **batch-level graph-inference result** rather than an individually validated prediction. By contrast, **Plasma Cell Myeloma** — where gallium's dual mechanism of osteoclast suppression and plasma cell RNR inhibition is well described — carries nine publications and a pilot randomized trial, making it the more biologically coherent and clinically tractable direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Sickle Cell-Hemoglobin C Disease Syndrome.

---

## Literature Evidence

*No literature is available for Sickle Cell-Hemoglobin C Disease Syndrome (rank 1). The table below covers **Plasma Cell Myeloma (rank 6, TxGNN score 98.12%)**, which has the highest evidence level in this pack and is mechanistically linked to gallium nitrate's established biological actions.*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8246033](https://pubmed.ncbi.nlm.nih.gov/8246033/) | 1993 | Pilot RCT | J Clin Oncol | Pilot randomized study of low-dose gallium nitrate added to standard antimyeloma chemotherapy; evaluated whether the addition could preserve or increase bone mass and prevent osteolysis in patients with osteolytic myeloma |
| [12776256](https://pubmed.ncbi.nlm.nih.gov/12776256/) | 2003 | Cohort | Semin Oncol | Retrospective cohort: patients with advanced-stage multiple myeloma receiving gallium nitrate alongside chemotherapy showed prolonged survival; characterized bone destruction mediated by osteoclastic resorption as the primary target |
| [12002765](https://pubmed.ncbi.nlm.nih.gov/12002765/) | 2002 | Retrospective Cohort | Leuk Lymphoma | 13 of 167 patients treated with M-2 protocol plus adjuvant gallium nitrate for osteolysis demonstrated extended survival compared to M-2 regimen alone in advanced-stage MM |
| [12776253](https://pubmed.ncbi.nlm.nih.gov/12776253/) | 2003 | Review | Semin Oncol | Gallium nitrate highly effective for both PTHrP-mediated and non-PTHrP-mediated cancer hypercalcemia; mechanism on bone clearly distinct from bisphosphonates — enhances calcium and phosphate content with direct noncytotoxic effects on bone tissue |
| [12776254](https://pubmed.ncbi.nlm.nih.gov/12776254/) | 2003 | Mechanistic Review | Semin Oncol | Gallium preferentially accumulates in trace amounts in metabolically active bone; inhibits osteoclast-mediated bone resorption by a mechanism distinct from bisphosphonates; potential utility across myeloma, bone metastases, Paget's disease, and osteoporosis |
| [9362436](https://pubmed.ncbi.nlm.nih.gov/9362436/) | 1997 | Clinical Review | Cancer | Randomized double-blind data showed gallium nitrate superior to etidronate, calcitonin, and pamidronate for hypercalcemia; both bone resorption reduction and direct antineoplastic effects discussed |
| [24021907](https://pubmed.ncbi.nlm.nih.gov/24021907/) | 2014 | Clinical Review | Am J Kidney Dis | Hypercalcemia of malignancy management including myeloma-related osteolysis; gallium nitrate cited as an effective option; four mechanistic categories of malignant hypercalcemia reviewed |
| [3533251](https://pubmed.ncbi.nlm.nih.gov/3533251/) | 1986 | Early Clinical Observation | Cancer Treat Rep | Original development of gallium nitrate as antineoplastic agent; antitumor activity demonstrated in multiple murine tumor models (carcinosarcoma, fibrosarcoma, lymphoma, osteosarcoma); dose-limiting renal toxicity established in preclinical species |
| [15478593](https://pubmed.ncbi.nlm.nih.gov/15478593/) | 2004 | Nursing/Clinical Review | ONS News | Clinical applications of gallium nitrate reviewed in the oncology nursing context, covering hypercalcemia, multiple myeloma, lymphoma, and bladder cancer; antisense and apoptosis-targeting therapies discussed alongside |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Originally developed as conventional antineoplastic (metal-based, first-in-class gallium compound); primary clinical use subsequently shifted to bone disease and cancer-related hypercalcemia |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Renal function (established dose-limiting toxicity from preclinical species and early clinical data); serum calcium and phosphate; CBC |
| Handling Protection | Consult cytotoxic drug handling guidelines given antineoplastic developmental history |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

### For Rank 1 — Sickle Cell-Hemoglobin C Disease Syndrome

**Decision: Hold**

**Rationale:**
The high TxGNN score (98.18%) reflects gallium's iron-metabolism interference pathway as recognized by the graph model, but the identical scores across all five sickle cell variants confirm this is undifferentiated batch inference with no validating data at any level — preclinical, clinical, or epidemiological. This hypothesis should not advance without foundational in vitro evidence first.

**To proceed, the following would be needed:**
- In vitro studies of gallium nitrate in HbSC red blood cell sickling models
- Animal studies in humanized HbSC mouse models
- Mechanistic justification distinguishing HbSC from the other four co-predicted sickle cell variants (currently scores are identical — no pharmacological differentiation)

---

### Priority Research Direction — Plasma Cell Myeloma (Rank 6)

**Decision: Research Question** *(prospective study design required)*

**Rationale:**
Multiple observational studies and a pilot RCT (PMID 8246033) demonstrate gallium nitrate's ability to attenuate myeloma-related osteolysis, with survival signals in advanced-stage patients treated alongside standard chemotherapy. The triple mechanism — RNR inhibition in proliferating plasma cells, direct osteoclast suppression, and disruption of the iron-rich bone marrow microenvironment — provides strong biological plausibility. Evidence is classified as L3.

**To proceed, the following is needed:**
- Retrieve and review the full package insert (FDA/TFDA) to document contraindications and key warnings — currently a blocking data gap
- Obtain detailed mechanism of action data from DrugBank
- Conduct a formal nephrotoxicity risk assessment for the myeloma population, where renal impairment is highly prevalent
- Design a Phase 2 trial evaluating gallium nitrate as an adjunct to modern myeloma regimens (e.g., bortezomib-based or daratumumab-based combinations), with skeletal-related events as the primary endpoint
- Head-to-head comparison with zoledronic acid (current standard of care for myeloma bone disease) to define differentiated value
- Singapore regulatory pathway assessment, as the drug is currently not marketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

