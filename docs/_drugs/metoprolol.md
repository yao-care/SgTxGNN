---
layout: default
title: Metoprolol
parent: 僅模型預測 (L5)
nav_order: 661
evidence_level: L5
indication_count: 10
---

# Metoprolol
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

Using the report structure specified in the prompt. A quick data-fidelity note before the report: the evidence pack's `predicted_indications[0]` (rank 1, "malignant renovascular hypertension") has notably weaker evidence than several lower-ranked candidates in the same pack (e.g., rank 9 "chronic pulmonary heart disease" has L1 evidence with 15 trials + 20 papers). Per the template's explicit extraction rule, the report below is built on `predicted_indications[0]` as instructed — the stronger alternative is flagged in the Conclusion section rather than substituted, so nothing in the evidence pack is silently dropped.

---

# Metoprolol: From Hypertension / Post-MI Management to Malignant Renovascular Hypertension

## One-Sentence Summary

> Metoprolol is a β1-selective adrenergic receptor blocker whose established pharmacological role is in cardiovascular conditions such as hypertension, angina, and post-myocardial-infarction management.
> The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**,
> but currently this specific prediction is supported by **0 clinical trials** and only **2 publications**, both of which are classified as off-topic by the evidence pack itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available as a formal registration record (drug is unmarketed in this jurisdiction); pharmacologically known as a β1-selective adrenergic blocker used for hypertension, angina, and post-MI care |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic rationale captured in the evidence pack itself, Metoprolol is a cardioselective β1-adrenergic receptor blocker, a drug class with proven efficacy across multiple cardiovascular indications, and mechanistically it may be applicable to malignant renovascular hypertension.

The proposed mechanistic link is that β1-blockade suppresses renin release from the juxtaglomerular apparatus, which is theoretically relevant to renovascular hypertension driven primarily by renin-angiotensin system activation — this is the same pharmacological basis by which beta-blockers are already used as adjunct antihypertensive therapy. This is a plausible, well-grounded pharmacological hypothesis rather than an established clinical finding.

However, the evidence pack's own literature classification is important context: the two retrieved PubMed articles for this indication (on hypertensive optic neuropathy and pheochromocytoma diagnostic biomarkers) are explicitly labeled "Off-topic" and assessed as search noise rather than supporting evidence. In other words, the mechanistic rationale is sound in principle, but at present it is **not** backed by disease-specific clinical or trial evidence — this prediction sits at the "Research Question" stage (S1), not a validated repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15231398](https://pubmed.ncbi.nlm.nih.gov/15231398/) | 2004 | Off-topic (視神經病變) | Survey of Ophthalmology | Case report of hypertensive optic neuropathy secondary to renal artery stenosis from Takayasu's arteritis; not a Metoprolol-specific treatment study |
| [1988765](https://pubmed.ncbi.nlm.nih.gov/1988765/) | 1991 | Off-topic (嗜鉻細胞瘤診斷標記) | Medicine | Evaluates Chromogranin A as a diagnostic biomarker for pheochromocytoma in the differential diagnosis of hypertension; not related to Metoprolol treatment of this indication |

Both articles are classified by the evidence pack as off-topic to this specific indication and should be treated as search noise rather than supporting evidence.

---

## Singapore Market Information

Metoprolol currently has **0 registrations** on record in this jurisdiction's regulatory data (market status: 未上市 / Not Marketed). No license entries are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: This evidence pack flags the absence of TFDA label warnings/contraindications as a Blocking data gap — DG001 — which prevents a formal S1 safety pre-assessment for this drug. Drug interaction lookup also returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (malignant renovascular hypertension) has a sound mechanistic rationale but zero clinical trials and only two literature hits, both classified as off-topic by the evidence pack itself — this is evidence level L4/S1 ("Research Question"), not yet actionable.
- A Blocking data gap (DG001: no TFDA label warnings/contraindications) prevents even a basic safety pre-screen, and the drug is currently unmarketed (0 registrations) in this jurisdiction.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (DG001 — Blocking; required before any S1 safety pre-assessment)
- DrugBank mechanism-of-action data (DG002 — High priority; needed to properly assess mechanistic plausibility)
- Indication-specific literature search targeting Metoprolol's role in renin-angiotensin suppression / malignant renovascular hypertension specifically (current results are off-topic and do not constitute supporting evidence)
- Consider a separate, dedicated evaluation of **chronic pulmonary heart disease** (rank 9 in this same evidence pack), which shows substantially stronger evidence — L1, 15 clinical trials including completed Phase 4 RCTs, and 20 publications including 2024 NEJM/JAMA-level RCTs — and may warrant a "Proceed with Guardrails" pathway independent of this report's primary candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

