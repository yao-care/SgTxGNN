---
layout: default
title: Dulaglutide
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
---

# Dulaglutide
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

# Dulaglutide: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Dulaglutide (Trulicity) is a long-acting GLP-1 receptor agonist originally developed and approved for the management of Type 2 Diabetes Mellitus in adults, acting by stimulating insulin secretion and suppressing glucagon in a glucose-dependent manner.

The TxGNN model predicts it may be effective for **Opsismodysplasia** as the top-ranked candidate, with a prediction score of **97.05%** — however, this prediction is supported by **no clinical trials and no published literature**, placing it squarely at the lowest evidence tier.

Across all 10 predictions in this batch, the pattern is consistent: high TxGNN scores driven by network topology proximity, with zero empirical evidence for any of the predicted indications. All 10 are assigned **Evidence Level L5** and a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (GLP-1 receptor agonist class) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dulaglutide is a GLP-1 (glucagon-like peptide-1) receptor agonist. It binds to GLP-1 receptors expressed on pancreatic beta cells and multiple other tissues, triggering a cAMP → PKA → PI3K signalling cascade. This pathway stimulates glucose-dependent insulin secretion, suppresses glucagon, slows gastric emptying, and reduces appetite. The PI3K/AKT/mTOR node is the key intersection point with many other biological processes.

Opsismodysplasia is a rare, severe skeletal dysplasia caused by loss-of-function mutations in **INPPL1** (encoding SHIP2, a phosphoinositide phosphatase). SHIP2 is a negative regulator of PI3K signalling — when SHIP2 is non-functional, PI3K/AKT/mTOR signalling becomes dysregulated, impairing chondrocyte differentiation and endochondral ossification. The TxGNN model likely scores this association highly because both Dulaglutide's mechanism and SHIP2 dysfunction converge on the same PI3K network node.

However, the biological rationale for therapeutic benefit is very weak. Opsismodysplasia is a **congenital structural bone defect** — the skeletal malformation is established in utero and cannot be reversed by metabolic pathway modulation. There is no preclinical evidence that GLP-1 receptor agonism influences cartilage formation or chondrocyte biology. This is a textbook case of **network topology driving a false positive**: shared pathway nodes inflate the TxGNN score without translating to therapeutic relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dulaglutide in any of the 10 predicted indications in this batch.

---

## Literature Evidence

Currently no related literature available for Dulaglutide in any of the 10 predicted indications in this batch.

---

## Singapore Market Information

Dulaglutide is not registered with the Health Sciences Authority (HSA) of Singapore. No product authorisations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Dulaglutide in this batch are rare or ultra-rare diseases with zero supporting clinical trials or published literature. The high prediction scores (0.70–0.97) reflect shared network topology — particularly the GLP-1 → cAMP → PKA → PI3K pathway intersecting with multiple disease-associated nodes — rather than genuine pharmacological evidence. The top prediction (opsismodysplasia) is a congenital skeletal dysplasia where drug-induced pathway modulation cannot address the underlying structural defect.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve Dulaglutide's full pharmacological profile from DrugBank (DB09045) to enable proper mechanistic scoring
- **Singapore registration status clarification**: Confirm whether Dulaglutide (Trulicity/Awiqli) has been submitted to HSA or is under review
- **Prioritisation within the prediction batch**: Of the 10 indications, **Autoimmune Oophoritis** (rank 10) warrants the closest second look — GLP-1R is expressed in granulosa cells, and GLP-1's immunomodulatory effects (Treg/Th17 balance, NF-κB suppression) provide the most biologically coherent rationale, despite its lower TxGNN score (70%)
- **Known indications gap**: Dulaglutide has established cardiovascular outcomes data (REWIND trial, CVOT) and an approved indication for CV risk reduction in T2DM patients — these are not reflected in this Evidence Pack and should be cross-checked against the full prediction list for potential missed hits
- **Rare disease feasibility screen**: Before advancing any of the 10 candidates, confirm patient population size and whether orphan drug regulatory pathways (e.g., HSA Orphan Drug Scheme) would apply
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

