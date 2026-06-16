---
layout: default
title: Ebastine
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Ebastine
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

# Ebastine: From Allergic Rhinitis / Urticaria to Coronary Artery Disease

## One-Sentence Summary

Ebastine is a second-generation H1 antihistamine, clinically used for allergic rhinitis and chronic urticaria.
The TxGNN model predicts it may be effective for **Coronary Artery Disease**,
with **0 clinical trials** and **1 computational publication** currently supporting this direction — evidence remains at the preclinical mechanistic stage only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis / Chronic urticaria (no Singapore registration on record) |
| Predicted New Indication | Coronary Artery Disease |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ebastine is a second-generation H1 receptor antagonist used for allergic conditions. Beyond its classical H1-blocking activity, ebastine has been identified as a ligand that interacts with cytochrome P450 2J2 (CYP2J2), an enzyme expressed abundantly in cardiac and vascular tissue.

CYP2J2 catalyses the epoxidation of arachidonic acid to epoxyeicosatrienoic acids (EETs), which are known to exert vasodilatory, anti-inflammatory, and anti-thrombotic cardioprotective effects. If ebastine inhibits CYP2J2, it could theoretically modulate the arachidonic acid–EET axis and thereby influence coronary artery disease pathophysiology. A 2008 computational study (PMID 18004755) used homology modelling and molecular dynamics simulation to demonstrate that ebastine can dock into the CYP2J2 active site, providing the only molecular-level mechanistic evidence for this connection.

However, the mechanistic direction remains critically unresolved: whether CYP2J2 inhibition in this context is cardioprotective or detrimental has not been established. There are no in vivo animal studies, no observational human data, and no clinical trials. The TxGNN prediction appears to be driven by graph proximity between ebastine's CYP2J2 interaction node and cardiovascular disease nodes, rather than a directly validated therapeutic pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18004755](https://pubmed.ncbi.nlm.nih.gov/18004755/) | 2008 | Computational (In silico) | Proteins | Homology modelling and molecular dynamics simulation of human CYP2J2 demonstrate that ebastine binds to the enzyme's active site. CYP2J2 catalyses epoxidation of arachidonic acid to EETs, which are associated with coronary artery disease, hypertension, and carcinogenesis; the study identifies CYP2J2 as a potential drug target and biomarker. |

---

## Singapore Market Information

Ebastine is not currently registered in Singapore. No marketing authorizations or product licences are on record with HSA.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole supporting evidence is a single 2008 in silico study demonstrating ebastine's structural compatibility with the CYP2J2 active site — there are no clinical trials, no in vivo studies, and no human data linking ebastine to coronary artery disease outcomes. The direction of the CYP2J2–EET effect (protective vs. harmful) in this setting remains unresolved, making the biological rationale insufficient to advance.

**To proceed, the following is needed:**
- Full CYP2J2 inhibition kinetics (IC₅₀, selectivity vs. other CYP isoforms) for ebastine confirmed in wet-lab assays
- In vivo animal model data evaluating ebastine's effect on myocardial or vascular endpoints
- Mechanistic clarification of whether CYP2J2 inhibition is cardioprotective or detrimental in coronary artery disease models
- Complete MOA profile and safety data from DrugBank and package inserts (currently unavailable — data gap DG002/DG001)
- HSA registration review if Singapore-market application is intended
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

