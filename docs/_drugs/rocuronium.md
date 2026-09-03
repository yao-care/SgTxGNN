---
layout: default
title: Rocuronium
parent: 僅模型預測 (L5)
nav_order: 871
evidence_level: L5
indication_count: 10
---

# Rocuronium
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

Using the provided Evidence Pack directly (no additional skill needed — this is a template-driven report generation task).

# Rocuronium: From Neuromuscular Blockade in General Anesthesia to Migraine Disorder

## One-Sentence Summary

Rocuronium is a peripheral non-depolarizing neuromuscular blocking agent (NMBA) used as an adjunct to general anesthesia (drug class inferred from the evidence pack; no structured original-indication data was provided). The TxGNN model predicts it may be effective for **Migraine Disorder**, but this direction is currently supported by only **1 loosely-related clinical trial** and **no literature**, and the drug is not marketed in Singapore.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry data. Rocuronium is a peripheral NMBA used in general anesthesia (inferred from evidence-pack mechanistic notes) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the available evidence-pack annotations, rocuronium is a non-depolarizing NMBA that acts at nicotinic acetylcholine receptors at the peripheral neuromuscular junction; it has very low blood-brain-barrier penetration and no known central mechanism.

There is no established pharmacological rationale connecting a peripheral muscle relaxant to migraine pathophysiology, which is primarily a central/trigeminovascular disorder. The single supporting trial (a pediatric pharmacokinetics study covering many unrelated drugs) does not test rocuronium against migraine and offers no mechanistic or clinical signal.

Taken together, this prediction should be treated as a low-confidence, model-only signal — likely arising from indirect co-occurrence patterns in the knowledge graph (e.g., rocuronium's frequent use in surgical/anesthesia contexts that also involve headache-related outcome reporting) rather than a genuine pharmacological link.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3,520 | Pediatric pharmacokinetics study of multiple "understudied" drugs administered per standard of care; not designed to evaluate rocuronium for migraine treatment |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Rocuronium is not currently marketed in Singapore (0 registrations on file); no license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted migraine indication has no plausible mechanistic basis (rocuronium is a peripherally-acting NMBA with negligible CNS penetration) and is supported only by an unrelated pediatric pharmacokinetics trial. Combined with the absence of Singapore market presence and missing safety/MOA data, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank (currently a High-severity data gap, DG002)
- Package insert warnings/contraindications (currently a Blocking data gap, DG001) — required before any S1 safety screening
- A credible preclinical or mechanistic study linking peripheral NMBA activity to migraine pathophysiology, if this candidate is to be pursued further
- Note: among the 10 TxGNN-predicted indications in this pack, **headache disorder** (rank 10) has a materially stronger evidence base (L3, decision stage S1) — including an RCT/cohort study showing rocuronium-sugammadex may reduce post-ECT myalgia/headache versus succinylcholine. If pursuing a headache-related indication, that candidate — not migraine — is the more defensible starting point.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

