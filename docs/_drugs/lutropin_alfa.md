---
layout: default
title: Lutropin Alfa
parent: 僅模型預測 (L5)
nav_order: 618
evidence_level: L5
indication_count: 10
---

# Lutropin Alfa
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

# Lutropin alfa: From Hypogonadotropic Hypogonadism to Postural Orthostatic Tachycardia Syndrome

## One-Sentence Summary

Lutropin alfa (Luveris®) is a recombinant human luteinizing hormone (LH) approved internationally for stimulating follicular development in women with severe LH and FSH deficiency (hypogonadotropic hypogonadism).
The TxGNN model predicts it may be effective for **Postural Orthostatic Tachycardia Syndrome (POTS)** as its top-ranked novel indication, with **no clinical trials** and **no published literature** currently supporting this direction.
This is a 10-candidate multi-indication evaluation; 9 of 10 candidates are at Evidence Level L5, with the sole exception being **Multiple Endocrine Neoplasia** (rank 9, L4 — 1 Phase IV trial identified).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypogonadotropic hypogonadism (infertility due to severe LH/FSH deficiency) |
| Predicted New Indication (Top) | Postural Orthostatic Tachycardia Syndrome (POTS) |
| TxGNN Prediction Score | 97.04% (Global rank #21,133) |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## All Predicted Indications

| Rank | Disease | TxGNN Score | TxGNN Global Rank | Evidence Level | Decision |
|------|---------|-------------|-------------------|----------------|---------|
| 1 | Postural Orthostatic Tachycardia Syndrome | 97.04% | #21,133 | L5 | Hold |
| 2 | Peptic Esophagitis | 97.02% | #21,178 | L5 | Hold |
| 3 | Trichotillomania | 96.31% | #23,442 | L5 | Hold |
| 4 | Raynaud Disease | 95.65% | #25,103 | L5 | Hold |
| 5 | Duodenal Ulcer | 95.58% | #25,278 | L5 | Hold |
| 6 | Tourette Syndrome | 95.18% | #26,288 | L5 | Hold |
| 7 | Esophageal Disease | 94.93% | #26,872 | L5 | Hold |
| 8 | Sinoatrial Block | 94.91% | #26,919 | L5 | Hold |
| **9** | **Multiple Endocrine Neoplasia** | **94.87%** | **#26,990** | **L4** | **Research Question** |
| 10 | Duodenogastric Reflux | 94.58% | #27,640 | L5 | Hold |

> **Note on TxGNN global ranks**: All 10 predictions fall between global ranks #21,000–27,640, indicating these are not among the model's highest-confidence predictions for this drug. The percentage scores reflect similarity within the model's output distribution, not absolute therapeutic confidence.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmaceutical information, Lutropin alfa is a recombinant human LH that binds to LH/hCG receptors (LHCGR) on ovarian granulosa and theca cells, driving follicular maturation and stimulating downstream estrogen and progesterone biosynthesis. It is co-administered with follitropin alfa (FSH) to restore the hormonal milieu in women whose pituitary cannot produce adequate endogenous LH.

For the top TxGNN prediction — **POTS** — the biological rationale is indirect. LH fluctuates across the menstrual cycle, and POTS symptoms are known to worsen at specific cycle phases in affected women. Estrogen, a downstream product of LH-driven ovarian activity, modulates venous compliance and autonomic tone. POTS disproportionately affects women of reproductive age, supporting a hormonal-autonomic hypothesis. However, this represents a multi-step downstream cascade (LH → estrogen → venous/autonomic changes → POTS symptoms) rather than a direct LH therapeutic action, with no interventional evidence of any kind. The mechanistic distance is too large to support development priority.

Among all 10 predictions, **Multiple Endocrine Neoplasia (MEN, rank 9)** provides the most coherent clinical rationale. MEN1 syndrome frequently involves pituitary adenomas that suppress gonadotropin secretion, leading to secondary hypogonadotropic hypogonadism — the precise condition Lutropin alfa is designed to treat. This is not a mechanistically novel repurposing; it is an indication extension where an established therapy addresses a well-defined disease subgroup within the MEN patient population. The remaining predictions (esophageal diseases, neuropsychiatric conditions, cardiovascular) largely reflect distal hormonal cascade effects or knowledge-graph clustering artifacts without plausible direct mechanistic links.

---

## Clinical Trial Evidence

No clinical trials were identified for the top predicted indication (Postural Orthostatic Tachycardia Syndrome) or for 8 of the other 9 predicted indications.

The following trial was identified for **Multiple Endocrine Neoplasia (rank 9)**:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01081626](https://clinicaltrials.gov/study/NCT01081626) | Phase IV | Completed | 310 | Open-label post-marketing RCT comparing individualized vs. conventional Gonal-f dosing (co-administered with Lutropin alfa) for ovulation induction in WHO Group II chronic anovulatory women. MEN patients with pituitary adenoma-related LH deficiency may form a disease subgroup, but MEN is not the primary indication studied — direct MEN-specific efficacy data requires subgroup analysis confirmation. |

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## Singapore Market Information

Lutropin alfa is **not registered in Singapore**. There are currently no marketing authorizations on record.

Luveris® (Merck/EMD Serono) holds EMA marketing approval for hypogonadotropic hypogonadism in the European Union and several other markets, but no registration has been filed with the Health Sciences Authority (HSA) of Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

Safety data (key warnings, contraindications, drug-drug interactions) was not available in the current Evidence Pack. Before any clinical application or regulatory submission, the Luveris® EMA Summary of Product Characteristics (SmPC) should be reviewed, with particular attention to:
- Ovarian hyperstimulation syndrome (OHSS) risk when combined with FSH
- Multiple pregnancy risk
- Hormone-sensitive conditions as potential contraindications

---

## Conclusion and Next Steps

**Decision: Hold (Ranks 1–8, 10) | Research Question (Rank 9 — Multiple Endocrine Neoplasia)**

**Rationale:**
Nine of ten predictions are at Evidence Level L5 with global TxGNN ranks above #21,000, reflecting low model confidence relative to the drug's full prediction landscape. Most mechanistic links are indirect, multi-step hormonal cascade effects — insufficient to justify development investment without foundational evidence. Multiple Endocrine Neoplasia is the sole exception: MEN1-related pituitary dysfunction causing secondary hypogonadotropic hypogonadism is a clinically recognized scenario where Lutropin alfa's approved mechanism directly applies.

**To proceed with the MEN Research Question, the following is needed:**

- Confirm whether NCT01081626 enrolled MEN patients as a defined subgroup and request published subgroup efficacy and safety data
- Conduct a targeted systematic literature review for LH supplementation specifically in MEN-associated hypogonadotropic hypogonadism
- Retrieve full MOA data from DrugBank API (Data Gap DG002)
- Retrieve package insert warnings and contraindications — download Luveris® EMA SmPC PDF (Data Gap DG001)
- Assess Singapore HSA regulatory pathway: since the drug is not currently registered in Singapore, a full new Drug Product License application would be required before any MEN-specific indication can be pursued locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

