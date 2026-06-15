---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive NSCLC to Fibromatosis, Gingival

## One-Sentence Summary

Brigatinib (ALUNBRIG™) is a next-generation anaplastic lymphoma kinase (ALK) inhibitor approved globally for ALK-positive metastatic non-small cell lung cancer (NSCLC), though it is not currently registered in Singapore.
The TxGNN model ranks **Fibromatosis, Gingival** as its top predicted new indication (score: 99.89%), but **no clinical trials or supporting literature** exist for this direction, and the mechanistic link is considered implausible.
Across all 10 predicted indications, the most clinically actionable signals are concentrated in ALK-driven lung tumour subtypes and NF2-related schwannomatosis (rank 10), where emerging clinical evidence of tumour shrinkage with brigatinib has been reported.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive metastatic NSCLC (global FDA/EMA approval; no Singapore HSA registration) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published literature, Brigatinib is a next-generation small-molecule tyrosine kinase inhibitor with potent activity against ALK, ROS1, EGFR, and FLT3 — including mutation variants that confer resistance to the first-generation inhibitor crizotinib. It received FDA accelerated approval in April 2017 for crizotinib-refractory ALK-positive NSCLC, and full regulatory approval in 2020 based on the pivotal Phase 3 ALTA-1L trial, which demonstrated superior progression-free survival versus crizotinib in ALK inhibitor-naive advanced NSCLC patients. Outside its primary indication, preclinical and early clinical data suggest brigatinib also inhibits FAK and ErbB2, opening potential activity in NF2-driven tumours.

Gingival fibromatosis is a rare benign condition characterised by progressive fibrous overgrowth of gum tissue. Its established molecular drivers — SOS1 mutations, PTCH1 mutations, and TGF-β pathway dysregulation — bear no known relationship to the kinase targets of Brigatinib. There is no established biological pathway connecting ALK/ROS1/EGFR inhibition to gingival fibrous proliferation, and no plausible shared signalling mechanism has been proposed in the literature.

The TxGNN score of 99.89% for this indication most likely reflects a topological proximity artefact in the knowledge graph rather than a genuine pharmacological signal. The evidence pack explicitly categorises this as a probable false positive. No clinical trials have been initiated and no relevant literature exists. This prediction should not be prioritised for further investigation without new mechanistic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Brigatinib in fibromatosis, gingival.

---

## Literature Evidence

Currently no related literature available for Brigatinib in fibromatosis, gingival.

---

## Singapore Market Information

Brigatinib is not currently registered with the Health Sciences Authority (HSA) in Singapore. No product licences are on record.

---

## Cytotoxicity

Brigatinib is an antineoplastic agent (targeted therapy for ALK-positive malignancy). The following applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — next-generation ALK/ROS1/EGFR tyrosine kinase inhibitor (TKI); not a conventional cytotoxic |
| Myelosuppression Risk | Low (less myelosuppressive than conventional chemotherapy; anaemia and lymphopenia reported in Phase 3 trials at low frequency) |
| Emetogenicity Classification | Low (oral agent; nausea reported in approximately 24% of patients, typically grade 1–2) |
| Monitoring Items | Pulmonary function (early pulmonary adverse events occur within the first 7 days in 3–9% of patients — a brigatinib-specific signal requiring close monitoring); liver enzymes (ALT/AST); CPK; lipase/amylase; blood pressure; fasting blood glucose; QTc interval |
| Handling Protection | Standard oral antineoplastic handling precautions apply |

---

## Safety Considerations

Please refer to the package insert for safety information. No HSA-registered product data or Singapore-specific warnings are currently available. Note: a fatal tumour lysis syndrome case following brigatinib initiation after sequential ALK inhibitor therapy has been reported in the literature (PMID 34987411) and represents a rare but serious safety signal to be aware of in heavily pre-treated patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN top prediction of gingival fibromatosis is biologically implausible — Brigatinib's ALK/ROS1/EGFR kinase inhibition profile has no established intersection with the SOS1/PTCH1/TGF-β drivers of gingival fibromatosis, and the high prediction score is consistent with a knowledge-graph topological artefact rather than a pharmacological signal.

**To proceed, the following is needed:**

- **Retrieve MOA data** from DrugBank (DB12267) to enable full mechanistic analysis across all 10 predicted indications
- **Obtain the package insert** from the FDA, EMA, or PMDA to populate Singapore-specific safety warnings, contraindications, and drug interaction data
- **Re-classify ALK+ NSCLC anatomical subtypes**: Lung hilum carcinoma (rank 4) and pulmonary sulcus neoplasm (rank 8) should not be treated as novel indications — if ALK rearrangement is confirmed, both fall within the established ALTA-1L NSCLC framework and should be evaluated accordingly
- **Escalate NF2-related schwannomatosis** (currently mapped under rank 10 with an incorrect disease label): PMID 38904277 (NEJM 2024) demonstrates clinical tumour shrinkage with brigatinib in NF2-SWN patients via FAK/ErbB2 inhibition; once correctly re-labelled, this indication qualifies for an L3 evidence review and warrants a dedicated repurposing assessment
- **Evaluate Singapore registration strategy** for the established ALK+ NSCLC indication: Brigatinib is currently unregistered in Singapore despite strong Phase 3 ALTA-1L support and approvals in the US, EU, and Japan — this may represent an unmet access gap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

