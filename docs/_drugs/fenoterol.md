---
layout: default
title: Fenoterol
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Fenoterol
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

# Fenoterol: From Bronchodilator/Tocolytic to Multiple System Atrophy

## One-Sentence Summary

Fenoterol (DB01288) is a selective β2-adrenergic agonist classically used as a bronchodilator for asthma and as a tocolytic agent for preterm labor, though it currently holds no registered product in Singapore.
The TxGNN model predicts it may have potential relevance in **Multiple System Atrophy (MSA)** — a rare, progressive multisystem neurodegeneration — based on β2-mediated neuroprotective signalling pathways.
However, this prediction is supported by **no clinical trials and no published literature** specific to this indication, placing confidence at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Singapore registration; drug known as bronchodilator/tocolytic by pharmacological class) |
| Predicted New Indication | Multiple System Atrophy |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, Fenoterol is a selective β2-adrenergic receptor agonist — the same receptor class that includes salbutamol (albuterol) and salmeterol. Its established uses centre on bronchial smooth muscle relaxation (asthma, COPD) and uterine smooth muscle relaxation (tocolysis in preterm labour).

The connection to Multiple System Atrophy rests on an indirect mechanistic hypothesis: β2 adrenergic receptors are expressed in the central nervous system, and β2 agonism activates the cAMP/PKA signalling pathway, which has been associated with neuroprotective effects in some animal models. Other β2 agonists — notably clenbuterol — have shown disease-modifying signals in preclinical models of neurodegeneration. MSA is driven by α-synuclein aggregation causing multi-system neuronal loss; β2 agonism may theoretically attenuate neuroinflammation or promote autophagy-mediated clearance.

That said, this mechanistic hypothesis is distant and speculative. MSA also features prominent autonomic failure, and β2 agonism might provide short-term symptomatic relief of orthostatic hypotension without addressing disease progression. Critically, there is no preclinical or clinical evidence specifically for Fenoterol in MSA. The TxGNN high score most likely reflects shared nodes in the autonomic nervous system subgraph of the knowledge graph, not validated biological proximity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Fenoterol has no registered products with the Health Sciences Authority (HSA) of Singapore. It is not marketed and has zero active licences on record.

---

## All Predicted Indications — Summary

Since the primary indication (Multiple System Atrophy) carries the lowest evidence level with a strong "Hold" recommendation, a brief overview of all 10 predicted indications is provided for completeness:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Concern |
|------|---------|-------------|---------------|---------------|-------------|
| 1 | Multiple System Atrophy | 99.70% | L5 | Hold | No clinical/preclinical data; mechanistic distance far |
| 2 | Postural Orthostatic Tachycardia Syndrome | 99.61% | L5 | **Hold** ⚠️ | Mechanistic contradiction — β2 agonism may worsen POTS |
| 3 | Variably Protease-Sensitive Prionopathy | 99.54% | L5 | Hold | Ultra-rare prion disease; no known drug intersection |
| 4 | Open-Angle Glaucoma | 99.43% | L5 | Hold | Weak mechanistic basis; standard of care uses β-blockers |
| 5 | Raynaud Disease | 99.41% | L5 | Research Question | β2 vasodilation plausible; no direct evidence |
| 6 | Primary Hereditary Glaucoma | 99.37% | L5 | Hold | Structural/genetic cause; pharmacology does not address root defect |
| 7 | Sinoatrial Block | 99.35% | L4 | Research Question | Class-effect positive chronotropy known; fenoterol-specific data absent |
| 8 | Sinoatrial Node Disease | 99.25% | L4 | Research Question | Same rationale as sinoatrial block |
| 9 | Anaphylaxis | 98.28% | L4 | Research Question | Strong class-effect (β2 bronchodilation in anaphylaxis); fenoterol-specific data absent |
| 10 | Glaucoma 1, Open Angle (OMIM) | 98.16% | L5 | Hold | MYOC/CYP1B1 structural pathology; β2 mechanistically irrelevant |

> **⚠️ Special note on POTS (Rank 2):** β2 agonists cause peripheral vasodilation and reflex tachycardia — directly worsening the defining pathophysiology of POTS. Current standard of care uses β-blockers (propranolol), midodrine (α1 agonist), or ivabradine. This is a mechanistic contradiction, not just a data gap.

---

## Safety Considerations

Please refer to the package insert for safety information. No safety data (warnings, contraindications, or drug interactions) was retrievable from the evidence pack for this candidate.

> Clinically, as a β2 adrenergic agonist, Fenoterol carries class-level risks including tachycardia, hypokalaemia, tremor, and — at high doses — β1 cross-activation leading to arrhythmia. These are important considerations for any cardiac indication (e.g., sinoatrial block) in this prediction list.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are unsupported by any registered clinical trials or published literature for Fenoterol specifically. The top indication (Multiple System Atrophy) rests on an indirect, speculative mechanistic link with no preclinical validation. Two indications carry active mechanistic concerns (POTS presents a direct pharmacological contraindication; hereditary glaucoma subtypes are structurally determined). The drug is not marketed in Singapore, eliminating any existing regulatory pathway advantage.

**To proceed, the following would be needed:**

- **MOA data from DrugBank**: Retrieve full pharmacology profile (receptor binding affinities, β1/β2 selectivity ratio, CNS penetrance) to validate neuroprotective hypothesis
- **Literature broadening**: Extend PubMed search to include β2-agonist class effects in MSA animal models (clenbuterol, formoterol as analogues) to assess whether class-level evidence justifies a research question designation
- **Preclinical feasibility assessment**: Determine if Fenoterol crosses the blood-brain barrier at therapeutic doses — a prerequisite for any CNS repurposing hypothesis
- **Safety package**: Obtain TFDA or EMA package insert to complete contraindication and warning assessment before any clinical pathway discussion
- **Raynaud / Anaphylaxis / SA node indications (Ranks 5, 7–9)**: These three-to-four "Research Question" candidates with L4 class-effect rationales may be more actionable — consider running targeted literature searches for β2 agonists (not Fenoterol specifically) in these conditions to determine if the class evidence is sufficient to elevate them to a hypothesis-generation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

