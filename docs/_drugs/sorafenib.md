---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 920
evidence_level: L5
indication_count: 10
---

# Sorafenib
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

# Sorafenib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is a multi-kinase inhibitor (RAF/MEK/ERK and VEGFR/PDGFR/c-KIT) whose approved use — evident across the trial evidence in this pack — centers on advanced/metastatic **Renal Cell Carcinoma (RCC)**. The TxGNN model predicts it may also be effective for **Liposarcoma**, but current support comes from only **2 clinical trials** (neither specific to liposarcoma) and **no dedicated literature**, so the signal remains preliminary.

> ⚠️ Note: The evidence pack's `original_indications` field is empty and `original_moa` is flagged as a data gap. The "Renal Cell Carcinoma" original indication above is inferred from repeated references within the clinical trial and rationale data (e.g., NCT01613846: "Both drugs are registered for this indication" [RCC]; rank-3 rationale: "Sorafenib 為已核准之 RCC…標準治療"), not from a confirmed regulatory label.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal Cell Carcinoma (inferred from trial/rationale evidence; not confirmed by regulatory label — see data gap) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (`original_moa`) is flagged as a data gap in this evidence pack. However, the repurposing rationale attached to the top prediction indicates Sorafenib inhibits the RAF/MEK/ERK signaling cascade and the receptor tyrosine kinases VEGFR, PDGFR, and c-KIT — a mechanism consistent with its established anti-angiogenic and anti-proliferative activity in RCC.

The rationale explicitly notes that this mechanism gives Sorafenib theoretical activity against vascularized soft tissue sarcomas as a class. However, it also flags an important caveat: liposarcoma — particularly the myxoid subtype driven by the **FUS-DDIT3** fusion — is not a classical receptor-tyrosine-kinase-dependent tumor. The mechanistic link is therefore described in the evidence pack itself as an **indirect extension** rather than a disease-specific mechanism, which is consistent with the modest evidence base below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Sorafenib (BAY 43-9006) studied in advanced soft tissue sarcomas broadly, not liposarcoma-specific; Grade B relevance — subgroup data needed to confirm efficacy in liposarcoma. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 study of oral **regorafenib** (a related but distinct BAY multi-kinase inhibitor) in selected sarcoma subtypes; cites precedent for sorafenib activity in osteogenic/Ewing sarcoma. Grade C — not direct sorafenib evidence, mechanistic analogy only. |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Sorafenib currently has no registered product authorizations in Singapore (0 licenses on file; market status: Not Marketed).

---

## Cytotoxicity

**This drug is antineoplastic** (multi-kinase inhibitor used in RCC/oncology settings per trial evidence), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target kinase inhibitor: RAF/VEGFR/PDGFR/c-KIT) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction (Liposarcoma) rests on only two Phase 2 trials, neither of which enrolled a liposarcoma-specific population — one is not even a sorafenib trial (regorafenib). Combined with a **Blocking** data gap on TFDA/HSA warnings and contraindications (required before any S1 safety screen) and the fact that Sorafenib is not currently marketed in Singapore, the evidence is insufficient to proceed past a research-question stage for this indication.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) to unblock the S1 safety evaluation
- Confirmed original indication and formal MOA data from DrugBank/regulatory source
- Liposarcoma-subgroup outcome data from NCT00217620 (or a dedicated liposarcoma trial) to replace the current indirect mechanistic extrapolation
- Consider re-evaluating rank 3 (Unclassified Renal Cell Carcinoma — L2, Proceed with Guardrails, Grade B trial + 3 supporting literature items) as a stronger near-term candidate, given it builds directly on Sorafenib's established RCC activity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

