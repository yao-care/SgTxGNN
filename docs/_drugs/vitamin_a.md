---
layout: default
title: Vitamin A
parent: 僅模型預測 (L5)
nav_order: 1062
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamin A: From Nutritional Deficiency to Congenital Prothrombin Deficiency

## One-Sentence Summary

> Vitamin A (DrugBank DB00162) is a fat-soluble vitamin classically used to prevent and treat vitamin A deficiency; it is **not currently marketed in Singapore** and has no local approved indication on file.
> The TxGNN model's top-ranked prediction is **Congenital Prothrombin Deficiency**, but the supporting evidence review flags this as a **likely false-positive signal** — the 5 retrieved clinical trials are about unrelated coagulation-factor products, not Vitamin A, and there is **no literature** support.
> With an Evidence Level of **L5** (model prediction only, no relevant studies) and mechanism of action data missing entirely, this candidate does not currently meet the bar for further evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore (HSA) license or approved indication text on file for this product |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Vitamin A in this evidence pack (flagged as a Blocking-severity data gap). Based on general pharmacological knowledge, Vitamin A (retinol) and its active metabolites (retinoic acid) act via nuclear retinoid receptors to regulate epithelial differentiation, immune function, and vision — mechanisms unrelated to coagulation.

Congenital prothrombin deficiency is a disorder of Factor II synthesis, a pathway that depends on **Vitamin K**, not Vitamin A. The evidence review explicitly concludes there is **no substantive mechanistic link** between the two, and suggests the high TxGNN score most likely reflects a knowledge-graph artifact — probable confusion between "vitamin" category nodes (Vitamin A vs. Vitamin K) rather than a genuine pharmacological signal.

Consistent with this, none of the five retrieved clinical trials actually studied Vitamin A for this indication — they involve prothrombin complex concentrates (Beriplex), rare-disease patient registries, and unrelated cardiovascular supplement trials that happened to share disease-domain keywords. No supporting literature was found at all. This combination (high model score + mechanistically implausible + no direct evidence) is the classic pattern of a TxGNN false positive and should not be interpreted as a genuine repurposing opportunity without further model-level investigation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Phase 2 | Completed | 90 | Vitalliver efficacy/safety in decompensated cirrhosis — coagulation-adjacent but no Vitamin A intervention |
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Recruiting | 480 | Haemophilia and bone loss (PHILEOS) — factor VIII/IX deficiency, unrelated to Vitamin A |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completed | 25 | Dietary supplement (L-arginine, Pycnogenol, vitamin K2, lipoic acid, B-vitamins) for endothelial function in hypertension — not Vitamin A |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Phase 3 | Completed | 40 | BERIPLEX® P/N (prothrombin complex concentrate) for reversal of oral anticoagulation — unrelated product class |
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Completed | 220 | Registry of adult inborn errors of metabolism in Switzerland — observational, no Vitamin A intervention |

**None of these trials directly evaluate Vitamin A for congenital prothrombin deficiency.**

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Vitamin A (DB00162) currently holds **no HSA marketing authorization** in Singapore (0 licenses on file). No dosage form, product name, or approved indication data is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no mechanistic basis (Vitamin K, not Vitamin A, governs prothrombin synthesis), no supporting literature, and no clinical trials that actually tested Vitamin A for this indication — evidence level L5 with a decision stage of S0. Combined with the absence of MOA data (Blocking gap) and no Singapore market presence, this candidate does not warrant further clinical or regulatory investment at this time.

**To proceed, the following is needed:**
- Root-cause investigation of the TxGNN knowledge graph to confirm/rule out vitamin-category node confusion (Vitamin A vs. Vitamin K)
- DrugBank MOA data retrieval (DG002)
- HSA label/warning data if this candidate is ever escalated (DG001, currently blocking)

**Note for reviewers:** This evidence pack contains other Vitamin A predictions with substantially stronger support that may warrant separate evaluation — notably **"perinatal disease"** (rank 8, Evidence Level L1, multiple Cochrane reviews on Vitamin A for preventing bronchopulmonary dysplasia/mortality in very-low-birth-weight infants, recommendation: Proceed with Guardrails) and **"cell proliferation disorder"** (rank 5, Evidence Level L2, retinoid mechanism well-established in oncology, recommendation: Proceed with Guardrails). These would likely be more productive candidates for a follow-up report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

