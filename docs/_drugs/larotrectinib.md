---
layout: default
title: Larotrectinib
parent: 僅模型預測 (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
---

# Larotrectinib
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

# Larotrectinib: From NTRK Gene Fusion-Positive Solid Tumors to Multiple Endocrine Neoplasia

## One-Sentence Summary

Larotrectinib is a highly selective pan-TRK (NTRK1/2/3) kinase inhibitor, globally approved as a tissue-agnostic therapy for NTRK gene fusion-positive solid tumors (not currently registered in Taiwan). The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia**, but this direction is currently supported by only **1 clinical trial** (an indirectly-relevant basket trial) and **2 publications** (neither evaluating larotrectinib itself) — the underlying mechanistic pathway (RET) differs from larotrectinib's actual target (NTRK), so this is a low-confidence, model-only signal rather than an evidence-backed lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NTRK gene fusion-positive solid tumors (tissue-agnostic; global label — not registered in Taiwan) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for larotrectinib is not available in this evidence pack (flagged as a High-severity data gap). Based on what is known from the supporting evidence itself, larotrectinib is a selective inhibitor of the TRKA/B/C proteins encoded by the NTRK1/2/3 genes, and its approved use is restricted to tumors carrying an NTRK gene fusion, regardless of tumor site of origin.

Multiple Endocrine Neoplasia (particularly MEN2, which includes medullary thyroid carcinoma) is driven almost exclusively by germline **RET** mutations — a genetically and pharmacologically distinct kinase target from NTRK. Larotrectinib has no reported direct inhibitory activity against RET. The two literature citations retrieved for this pairing (PMID 31322645, PMID 38438731) both discuss RET-targeted agents (selpercatinib, pralsetinib) and kinase-inhibitor classes used in thyroid cancer broadly — they support the biology of RET-driven disease, not any direct pharmacological link to larotrectinib.

The most plausible explanation for this prediction is that the TxGNN model's knowledge-graph embeddings place NTRK and RET close together because both are receptor tyrosine kinases frequently discussed in the same thyroid-cancer treatment context, rather than reflecting a real drug-mechanism-to-disease relationship. This should be treated as a hypothesis-generating signal only, not as evidence of clinical activity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, Not Recruiting | 6,452 | NCI-MATCH — a multi-arm, genomically-driven basket trial for refractory solid tumors, lymphomas, and multiple myeloma. The larotrectinib arm enrolls only NTRK-fusion-positive tumors; patients are not selected by a Multiple Endocrine Neoplasia diagnosis, so relevance to this specific indication is indirect (evidence-pack relevance grade: C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Reviews kinase inhibitors (vandetanib, cabozantinib, sorafenib, lenvatinib, dabrafenib/trametinib, and RET-selective agents) approved for advanced thyroid cancer; does not evaluate larotrectinib or MEN directly. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Review/Case report | NPJ Precision Oncology | Describes acquired resistance mechanisms to RET inhibitors (selpercatinib) in RET-driven medullary thyroid carcinoma, a manifestation of MEN2; informative on RET biology but does not study larotrectinib. |

---

## Singapore Market Information

Larotrectinib currently has **no registered product license** in the Taiwan regulatory dataset used for this evaluation (market status: 未上市 / Not Marketed, 0 total licenses). No authorization, product name, dosage form, or approved indication text is available to tabulate.

---

## Cytotoxicity

Larotrectinib is an antineoplastic agent (targeted small-molecule kinase inhibitor used in oncology), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective pan-TRK / NTRK kinase inhibitor) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Not directly established in this evidence pack. Note: the rank-10 prediction in this same pack flags thrombocytopenia as a *possible class-related adverse effect* of kinase inhibitors (including larotrectinib), not a treatable indication — this is an important causality-direction caveat, not efficacy evidence |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Standard kinase-inhibitor monitoring is reasonable pending label confirmation: CBC with differential, liver function, renal function |
| Handling Protection | Oral targeted agent; standard oncology-drug handling precautions apply, but confirm against the official package insert since TFDA labeling data is currently unavailable (blocking data gap) |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available for larotrectinib in this evidence pack (DrugBank DDI query returned "not found"; TFDA label warnings/contraindications are recorded as a **Blocking** data gap, DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic basis is weak: Multiple Endocrine Neoplasia (MEN2) is driven by RET mutations, while larotrectinib selectively targets NTRK — a different kinase pathway. Supporting evidence (1 indirectly-relevant basket trial, 2 reviews not studying larotrectinib) does not establish a direct drug-disease link, consistent with the evidence pack's own S0/Hold classification.
- Safety evaluation cannot proceed to a Stage 1 review because the TFDA label (warnings/contraindications) is a **Blocking** data gap (DG001), and larotrectinib is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- Larotrectinib package insert / TFDA label (warnings, contraindications, DDI) — currently blocking
- Confirmed mechanism-of-action documentation (DrugBank API or equivalent) — currently a High-severity gap
- Preclinical or mechanistic studies directly testing NTRK-pathway involvement in MEN2/RET-driven disease, since none currently exist
- A trial or case series enrolling patients by MEN diagnosis (rather than by NTRK-fusion status) before this candidate can be considered for Stage 1 advancement

**Data quality note:** This evidence pack's other ranked candidates (ranks 2–10) include predictions the pipeline itself has flagged as low-value or erroneous — e.g., two veterinary diseases (malignant catarrh, infectious bovine rhinotracheitis) that appear to be cross-species ontology noise, a "breast tumor luminal A or B" candidate whose 19 retrieved articles are keyword-polluted matches to "B cell"/"Hepatitis B" content unrelated to breast cancer subtyping, and a "thrombocytopenia" candidate that is more plausibly a known adverse effect than a treatable indication. None of these should be advanced without a pipeline/data-source review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

