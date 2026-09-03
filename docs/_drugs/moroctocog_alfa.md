---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 680
evidence_level: L5
indication_count: 10
---

# Moroctocog Alfa
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

Using no dedicated skill here — this is a direct report-generation task fully specified by the prompt template itself, not a coding/build/deploy workflow that maps to an available skill.

A note before the report: `predicted_indications[0]` (rank 1, "primary release disorder of platelets") is the highest TxGNN score, but its own `repurposing_rationale` explicitly states the mechanism doesn't match (platelet granule-release defect vs. a coagulation-factor product) and its evidence is grade-C/irrelevant. I built the report on rank 1 per the template's extraction rule, but reported that mismatch honestly rather than writing false supporting rationale, and flagged rank 4 as the more defensible alternative in the conclusion.

---

# Moroctocog Alfa: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a recombinant Factor VIII (B-domain deleted) product used to replace clotting factor in Hemophilia A. The TxGNN model's top-ranked prediction is **Primary Release Disorder of Platelets**, with a **99.97% prediction score**, but this indication currently has **0 directly relevant clinical trials** and **0 supporting publications** — the 7 trials retrieved were all graded low-relevance (keyword overlap only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A (congenital Factor VIII deficiency) — inferred from drug identity described in the evidence pack; no formal Singapore label text available (not marketed) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for moroctocog alfa is not available in this evidence pack (marked as a data gap). Based on the drug's known identity referenced elsewhere in the evidence pack, moroctocog alfa is a recombinant human Factor VIII product — it replaces a deficient coagulation factor in the intrinsic clotting cascade, and its efficacy in Hemophilia A is well established.

**This mechanism does not map onto the predicted indication.** Primary release disorder of platelets is a platelet granule-release defect (a qualitative platelet function disorder), not a coagulation-factor deficiency. The evidence pack's own mechanistic assessment states this directly: *"血小板顆粒釋放障礙為血小板功能性缺陷，與凝血因子（FVIII）路徑無直接關係，機轉不支持"* — supplementing Factor VIII would not correct a platelet granule-release defect. The high TxGNN score most likely reflects semantic proximity between "bleeding/hemostasis" concepts in the knowledge graph rather than a real pharmacological mechanism, which is consistent with the L5 evidence level and Hold recommendation assigned to this candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Post-COVID-19-vaccination syndrome symptom/lab study; matched only via coagulation-related keywords, not disease-relevant (grade C) |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not yet recruiting | 80 | Observational coagulation profiling in newly diagnosed AML patients; not a treatment trial for platelet release disorder (grade C) |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Artificial liver support system (DPMAS+TPE) in acute-on-chronic liver failure, effect on coagulation; unrelated (grade C) |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | BAX855 (PEGylated rFVIII) in severe Hemophilia A patients undergoing surgery; different drug, original indication only (grade C) |
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | BIVV001 (rFVIIIFc-VWF-XTEN) safety/efficacy/PK in adult severe Hemophilia A; different drug, original indication only (grade C) |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | BIVV001 in pediatric severe Hemophilia A; different drug, original indication only (grade C) |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Systemic/portal hemostasis exploration in TIPS procedure patients; unrelated (grade C) |

**None of these trials directly evaluate moroctocog alfa for platelet release disorder.** All were graded low relevance (C) — retrieved via generic coagulation/hemostasis keyword overlap.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Moroctocog alfa is not currently registered or marketed in Singapore (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.97% TxGNN score is not supported by mechanism, clinical trials, or literature — the evidence pack's own mechanistic review states platelet granule-release disorder is unrelated to the FVIII replacement pathway, and all 7 retrieved trials were graded irrelevant. This is an L5, model-prediction-only candidate.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Formal original-indication label text (Singapore registration data is empty; drug is not marketed locally)

**Note:** Within the same evidence pack, **rank 4 — "acquired coagulation factor deficiency"** (TxGNN score 99.88%, evidence level L3, decision stage S1, recommendation "Research Question") has a mechanistically coherent rationale (FVIII replacement in acquired Hemophilia A) and 13 clinical trials + 4 publications, several directly on FVIII-class replacement therapy. That candidate is a substantially stronger repurposing signal than the rank-1 prediction covered above and may warrant its own evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

