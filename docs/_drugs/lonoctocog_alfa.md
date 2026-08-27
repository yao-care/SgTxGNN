---
layout: default
title: Lonoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
---

# Lonoctocog Alfa
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

# Lonoctocog alfa: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Lonoctocog alfa (AFSTYLA) is a recombinant single-chain Factor VIII (rFVIII) product, approved internationally for the treatment and prophylaxis of bleeding episodes in patients with Hemophilia A.
The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease**, with a high algorithmic confidence score of 99.85%.
However, there are currently **0 clinical trials** and **0 publications** supporting this repurposing direction, placing this prediction at the lowest evidence level (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hemophilia A (Factor VIII deficiency) — treatment and prophylaxis of bleeding |
| Predicted New Indication | Pseudo-von Willebrand disease (Platelet-type vWD) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Lonoctocog alfa is a recombinant Factor VIII single-chain molecule (rFVIII-SC) that restores the function of the intrinsic coagulation pathway by forming a tenase complex with activated Factor IX (FIXa) on phosphatidylserine-rich platelet surfaces, thereby activating Factor X and propagating the coagulation cascade.

Pseudo-von Willebrand disease (platelet-type vWD) is caused by a gain-of-function mutation in platelet glycoprotein GPIbα, which results in enhanced affinity for ultra-large vWF multimers. This causes spontaneous binding and consumption of circulating large vWF multimers, secondarily depleting the carrier protein for Factor VIII and potentially shortening FVIII half-life. At the level of the knowledge graph, TxGNN likely scored this prediction highly because vWF and FVIII are tightly coupled nodes — vWF stabilises and chaperrones circulating FVIII in plasma.

However, the causal direction matters critically: the core defect in pseudo-vWD is in the platelet GPIb receptor, not in FVIII abundance or function. Supplementing rFVIII does not correct the underlying platelet-vWF hyperadhesion and will not prevent large-multimer depletion. Standard treatment is platelet transfusion; DDAVP is avoided because it releases endogenous vWF and can worsen thrombocytopenia. **This prediction is most likely a network-proximity artefact rather than a genuine therapeutic opportunity.** Across all 10 ranked predictions in this pack, the mechanistic links range from very weak to contraindicated (notably TTP at rank 10, where a pro-coagulant agent could be harmful).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## All Predicted Indications — Mechanistic Assessment

Since this report covers a purely model-driven prediction set with no clinical evidence for any indication, a comparative mechanistic overview of all 10 ranked predictions is provided below to support the Hold decision:

| Rank | Disease | TxGNN Score | Mechanistic Assessment | Risk Flag |
|------|---------|------------|----------------------|-----------|
| 1 | Pseudo-von Willebrand disease | 99.85% | Indirect: FVIII depletion is secondary to GPIb defect; rFVIII does not correct root cause | Network artefact |
| 2 | Primary release disorder of platelets | 99.84% | No link: dense/alpha-granule defects are in primary haemostasis; FVIII acts in secondary coagulation | No mechanistic basis |
| 3 | Glanzmann thrombasthenia | 99.76% | Weak: GPIIb/IIIa deficiency reduces platelet aggregation; rFVIII (unlike rFVIIa) requires functional platelet phospholipid surface to act | Should not be confused with rFVIIa indication |
| 4 | Scott syndrome | 99.44% | Theoretically partial: Scott syndrome impairs PS externalisation, which is the very scaffold FVIII needs — adding substrate without the scaffold has limited benefit | Theoretical substrate without scaffold |
| 5 | Acquired coagulation factor deficiency | 98.85% | Highest potential (if = Acquired Hemophilia A), but inhibitory antibodies limit standard rFVIII utility; obizur preferred | Highest of 10; still L5 |
| 6 | Bleeding diathesis due to collagen receptor defect | 98.71% | No link: GPVI/GP Ia-IIa defects are in platelet adhesion signalling, unrelated to FVIII | No mechanistic basis |
| 7 | Haemorrhagic disorder due to constitutional thrombocytopenia | 98.64% | Very weak: "coagulation support" concept unvalidated for rFVIII in thrombocytopenia | No clinical data |
| 8 | Oesophageal varices without bleeding | 98.41% | No link: portal hypertension treated by pressure reduction, not haemostatic augmentation; FVIII is typically normal/elevated in cirrhosis | No mechanistic basis |
| 9 | Oesophageal varices with bleeding | 98.41% | No link: multi-factor coagulation deficiency in liver disease; single FVIII supplementation insufficient | No mechanistic basis |
| 10 | Thrombotic thrombocytopenic purpura | 98.13% | **Contraindicated direction**: TTP is a thrombotic (not haemorrhagic) condition; adding rFVIII to a prothrombotic state could be harmful | ⚠️ High-risk false positive |

---

## Singapore Market Information

Lonoctocog alfa is **not registered** in Singapore. There are no product authorisations on record.

---

## Safety Considerations

Please refer to the package insert for safety information. No Singapore-registered package insert is available; consult the EMA/FDA prescribing information for AFSTYLA (CSL Behring).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications currently sit at Evidence Level L5 (model prediction only, no clinical or preclinical studies identified), and mechanistic analysis indicates that the majority of predictions are likely knowledge-graph network-proximity artefacts arising from the tight vWF–FVIII coupling in the graph, rather than genuine drug-repurposing opportunities. One prediction (Acquired Coagulation Factor Deficiency, rank 5, if specifically referring to Acquired Hemophilia A) merits separate targeted investigation, but remains L5 pending any supporting data.

**To proceed, the following is needed:**

- **Clarify the highest-potential indication**: Determine whether rank 5 ("acquired coagulation factor deficiency") specifically refers to Acquired Hemophilia A (AHA); if so, commission a focused literature review on rFVIII utility in AHA versus inhibitor bypass strategies
- **Retrieve full MOA data**: Query DrugBank API for DB13998 to obtain complete pharmacodynamic, pharmacokinetic, and binding-site data (Data Gap DG002)
- **Obtain Singapore/international prescribing information**: Download and parse the FDA/EMA AFSTYLA label for contraindications, warnings, and populations (Data Gap DG001)
- **Re-evaluate rank 3 (Glanzmann)** separately: Although rFVIII is not indicated, rFVIIa is — this distinction should be documented to avoid clinical misinterpretation
- **Flag rank 10 (TTP)** as a confirmed false positive: Add to KG exclusion list to prevent this association from re-surfacing in future pipeline runs
- **Do not pursue ranks 1, 2, 6, 8, 9** further: Mechanistic disconnection is fundamental, not a gap in evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

