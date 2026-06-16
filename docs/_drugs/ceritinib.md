---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: From ALK+ Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Ceritinib (Zykadia) is a second-generation ALK (anaplastic lymphoma kinase) inhibitor developed by Novartis, approved globally for the treatment of ALK-rearranged non-small cell lung cancer (NSCLC), though not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**, with **no clinical trials** and **no publications** directly supporting this indication.
Although the prediction score is high (99.86%), current mechanistic evidence does not support an ALK-driven role in gingival fibromatosis, and the score likely reflects graph-structural proximity within the knowledge graph rather than true biological relevance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-rearranged Non-Small Cell Lung Cancer (NSCLC) — inferred from global approval history; no Singapore HSA registration on file |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ceritinib is a potent, orally bioavailable small-molecule inhibitor of ALK tyrosine kinase, with approximately 20-fold greater potency against ALK than its predecessor crizotinib. It was granted FDA Breakthrough Therapy designation and first approved in 2014 for second-line treatment of ALK-positive metastatic NSCLC. Its known targets include ALK, IGF-1R (insulin-like growth factor 1 receptor), and FAK (focal adhesion kinase). Across its approved indications, the drug's activity is entirely dependent on the presence of an ALK gene rearrangement or activating mutation as the oncogenic driver — without this, no therapeutic rationale exists.

Fibromatosis, Gingival (gingival fibromatosis) is a rare hereditary or drug-induced condition characterised by abnormal proliferation of gingival fibroblasts, with disease pathogenesis centred on TGF-β/CTGF signalling pathways and extracellular matrix dysregulation. ALK signalling has no established role in this disease process. Gingival fibromatosis is classified as a benign fibrous overgrowth, entirely distinct from the ALK-fusion-driven malignancies for which ceritinib was developed.

The TxGNN model's high prediction score for this indication most likely reflects the spatial proximity of "lung/fibrosis-associated" and "fibromatosis" nodes within the knowledge graph topology, rather than a genuine biological connection. There are no clinical trials, preclinical studies, or case reports supporting ceritinib use in gingival fibromatosis. Without a mechanistic rationale or any supporting evidence, this prediction should be treated as a knowledge-graph false positive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Ceritinib is not currently registered with the Health Sciences Authority (HSA) in Singapore. No product authorisations are on file.

> **Note:** Ceritinib (brand name Zykadia) has received marketing approval in the United States (FDA, 2014), the European Union (EMA, 2015), and multiple other jurisdictions for ALK-rearranged NSCLC. Clinicians in Singapore seeking to use ceritinib would need to access it via a Special Access Route (SAR) or clinical trial pathway.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (ALK tyrosine kinase inhibitor — not conventional cytotoxic) |
| Myelosuppression Risk | Low to Moderate (not primarily myelosuppressive; haematological toxicity less prominent than with conventional chemotherapy, but monitoring recommended) |
| Emetogenicity Classification | Moderate to High (nausea, vomiting, and diarrhoea are among the most common dose-limiting adverse effects; taking with food at reduced dose [450 mg] significantly improves GI tolerability) |
| Monitoring Items | Liver function tests (ALT/AST — hepatotoxicity reported), fasting blood glucose (hyperglycaemia), ECG/QTc interval (QT prolongation risk), CBC, renal function, and pulmonary function (interstitial lung disease risk) |
| Handling Protection | Standard oral targeted therapy precautions apply; classify as cytotoxic for handling per institutional pharmacy policy |

---

## Safety Considerations

Formal Singapore HSA package insert data was not retrieved for this report. Based on published regulatory summaries and the literature in this evidence pack, the following key safety concerns are known:

- **QT Prolongation:** Ceritinib prolongs the QTc interval; ECG monitoring is required, particularly in patients on concomitant QT-prolonging agents (documented in pharmacovigilance analysis, PMID 34864500; QT case report, PMID 29413968).
- **Hepatotoxicity:** Significant elevations in liver transaminases have been reported; liver function monitoring is mandatory.
- **Interstitial Lung Disease / Pneumonitis:** Serious and potentially fatal ILD/pneumonitis has been observed, including one published case of diffuse infiltrative lung disease with pericarditis and pleural effusion attributed to ceritinib (PMID 31280988).
- **Hyperglycaemia:** Fasting blood glucose monitoring required; insulin or oral hypoglycaemic dose adjustment may be needed.
- **GI Toxicity:** Nausea, diarrhoea, vomiting, and abdominal pain are very common; the 450 mg with-food dosing schedule was developed specifically to address this (PMID 32838488).

> For complete prescribing information including contraindications and full drug interaction data, please refer to the official Zykadia package insert (Novartis) or the EMA/FDA Summary of Product Characteristics.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Fibromatosis, Gingival is a benign fibroblast proliferative disorder driven by TGF-β/CTGF pathways, not ALK signalling. There is no mechanistic basis for ceritinib use in this condition, no clinical trials, and no supporting literature. The TxGNN high prediction score is consistent with a knowledge-graph structural artefact rather than a genuine repurposing signal.

**To proceed, the following would be needed:**
- Identification of ALK expression or activating ALK mutations in gingival fibromatosis tissue samples (would require molecular pathology investigation — currently no evidence this exists)
- Preclinical in vitro data demonstrating ceritinib activity in fibroblast or gingival tissue models
- Re-evaluation of this prediction entry: the evidence pack for **rank 5 (Lung Benign Neoplasm)** contains 20 literature references including a Phase 3 RCT (ASCEND-4, PMID 28126333) and multiple meta-analyses for ALK+ NSCLC, and may represent a more actionable repurposing candidate if reclassified to its correct indication (ALK+ NSCLC). This entry should be reviewed by the clinical team for reclassification.
- Singapore HSA registration strategy should be evaluated separately if ceritinib is intended for use in ALK+ NSCLC patients in Singapore, independent of repurposing considerations.

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

