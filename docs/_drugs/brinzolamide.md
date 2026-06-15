---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Brinzolamide
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

# Brinzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide (Azopt®) is a topical carbonic anhydrase II (CA-II) inhibitor globally approved for lowering intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension, but it currently carries no Singapore market registration.
The TxGNN model assigns it the highest prediction score among all candidates for **Primary Hereditary Glaucoma** (99.48%), driven by the near-complete mechanistic overlap between hereditary and sporadic open-angle glaucoma at the pharmacological target level.
However, direct clinical evidence for this specific subtype is currently absent — **0 clinical trials** and **0 publications** targeting primary hereditary glaucoma have been identified, placing this squarely as a model-driven research hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (global approval; no Singapore registration) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on published reviews in the supporting literature (PMID 14565787, 18312166), Brinzolamide belongs to the topical carbonic anhydrase inhibitor (CAI) class. It selectively inhibits the CA-II isoenzyme expressed in the ciliary body epithelium, reducing bicarbonate secretion and thereby suppressing aqueous humor formation by up to approximately 18% from baseline. This direct reduction in aqueous inflow lowers IOP and has been associated with secondary improvements in retinal blood flow. Efficacy in primary open-angle glaucoma (POAG) and ocular hypertension is well established across multiple Phase 3 trials.

Primary hereditary glaucoma — principally juvenile-onset open-angle glaucoma (JOAG) arising from mutations in the *MYOC* or *OPTN* genes — shares the same core pathophysiology: impaired aqueous outflow that drives IOP elevation, which in turn damages the optic nerve head. Critically, the genetic cause operates upstream of the ciliary body; it does not alter the anatomy or biochemistry of the aqueous secretory pathway that Brinzolamide targets. A drug that reduces aqueous production via CA-II inhibition will lower IOP in a MYOC-mutant eye by exactly the same pharmacological mechanism as in a sporadic POAG eye. The therapeutic target and the disease's primary treatable lesion therefore remain fully aligned.

The TxGNN knowledge graph score of 0.9948 — the highest in this analysis — reflects that primary hereditary glaucoma shares a dense cluster of biological and clinical nodes with POAG in the knowledge graph. This is mechanistically sensible: both subtypes fall under the umbrella of open-angle glaucoma pathophysiology, and the knowledge graph captures that shared biology. The model prediction is therefore well-grounded, even though dedicated hereditary-subtype trial data do not yet exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for Primary Hereditary Glaucoma.

> **Supporting context**: Extensive Phase 3 evidence exists for Brinzolamide in the closely related open-angle glaucoma population (TxGNN ranks 2–4 in this analysis, all L1 evidence, including trials of up to n = 1,184 patients). That evidence base provides strong mechanistic support for the predicted efficacy in hereditary subtypes where elevated IOP is the primary driver, but it does not constitute direct evidence for the hereditary indication.

---

## Literature Evidence

Currently no related literature specifically addressing Brinzolamide in Primary Hereditary Glaucoma is available.

---

## Singapore Market Information

Brinzolamide has no current registrations with the Health Sciences Authority (HSA) of Singapore. There are no approved product listings, authorisation numbers, or dosage forms on record for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
While the mechanistic link between Brinzolamide's CA-II inhibition and IOP lowering in primary hereditary glaucoma is theoretically sound and the TxGNN model score is the highest in this analysis, the complete absence of clinical trial data or published literature specifically in hereditary glaucoma populations — combined with no Singapore market registration — means there is insufficient evidence to support a clinical introduction recommendation at this stage.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve full DrugBank pharmacology data (mechanism, targets, pathways) to formalise the mechanistic rationale
- **Singapore regulatory pathway assessment**: Determine whether the HSA would accept extrapolation from POAG Phase 3 data for a hereditary glaucoma indication, or whether a separate IND/NDA submission is required
- **Targeted literature search**: Conduct a focused search on CAI use (including oral acetazolamide and topical dorzolamide as class comparators) in JOAG and MYOC-mutation carriers to identify any case series or observational data
- **Safety data retrieval**: Obtain HSA/TGA/FDA-approved prescribing information to populate key warnings, contraindications, and paediatric safety profile (relevant given JOAG onset in younger patients)
- **Paediatric considerations**: Since hereditary glaucoma frequently presents in juveniles, review brinzolamide's paediatric safety data (NCT00061516 provides partial Phase 3 paediatric data in the related glaucoma population)
- **Comparator landscape review**: Assess whether oral acetazolamide or topical dorzolamide already serves this niche in Singapore clinical practice, and whether unmet need exists for a better-tolerated topical CAI

> *This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

