---
layout: default
title: Midostaurin
parent: 僅模型預測 (L5)
nav_order: 667
evidence_level: L5
indication_count: 10
---

# Midostaurin
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

# Midostaurin: From Undocumented Original Indication to Familial Thrombocytosis

## One-Sentence Summary

Midostaurin's original approved indication and mechanism of action are not documented in this evidence pack (flagged as data gaps DG002 and unrecorded `original_indications`). The TxGNN model predicts it may be effective for **Familial Thrombocytosis**, but this ranking currently has **0 clinical trials** and **0 publications** supporting it — the model's own rationale notes no known mechanistic overlap between midostaurin's targets and this disease's genetic drivers.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap) |
| Predicted New Indication | Familial Thrombocytosis |
| TxGNN Prediction Score | 98.92% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for midostaurin is not available from DrugBank in this evidence pack. From literature associated with a different candidate indication in this same pack (metastatic melanoma, PMID 16969355), midostaurin is described as a multikinase inhibitor of protein kinase C alpha (PKCα), VEGFR2, KIT, PDGFR, and FLT3 — but this characterization is incidental to this report's primary prediction and has not been independently verified against DrugBank for this candidate.

For the top-ranked prediction, familial thrombocytosis, the evidence pack's own mechanistic assessment is unfavorable: this disease is typically driven by germline mutations in *THPO* or *MPL*, pathways with no documented overlap with midostaurin's known targets (PKC/FLT3/KIT). The high TxGNN score therefore appears to reflect a statistical association in the knowledge graph rather than a validated biological pathway, and is not corroborated by any clinical trial or published literature.

Notably, this candidate's own predicted-indications list contains other entries with somewhat more substantive evidence — thrombocythemia (rank 5, L4, supported by FLT3-ITD mouse-model literature) and metastatic melanoma (rank 3, L2, supported by a completed Phase 2 trial) — but the melanoma trial (PMID 16969355) concluded midostaurin **lacked activity** in that setting, which further weakens confidence in extrapolating this drug's targets to other indications in this family.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Midostaurin has no marketing authorizations on record in Singapore (0 registrations; market status: not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: PKC/FLT3/KIT/PDGFR/VEGFR2), based on literature associated with a separate candidate indication in this pack; not confirmed against DrugBank categories for this report |
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
The top-ranked prediction (familial thrombocytosis) has no clinical trial or literature support and is an L5, model-prediction-only signal. The evidence pack's own mechanistic review finds no credible target overlap between midostaurin and this disease's known genetic drivers, so the prediction does not currently warrant advancement.

**To proceed, the following is needed:**
- TFDA/HSA label warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action from DrugBank (DG002)
- Documented original approved indication(s) for this drug
- Preclinical or mechanistic studies directly linking midostaurin's targets (PKC/FLT3/KIT) to thrombopoiesis pathways (THPO/MPL) before further evaluation of this specific indication
- If pursuing alternative candidates in this pack, dedicated evaluation of thrombocythemia (L4) or re-assessment of melanoma-family indications in light of the existing negative Phase 2 result
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

