---
layout: default
title: Lomefloxacin
parent: 僅模型預測 (L5)
nav_order: 604
evidence_level: L5
indication_count: 10
---

# Lomefloxacin
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

# Lomefloxacin: From Bacterial Infections to Laryngotracheitis

## One-Sentence Summary

Lomefloxacin is a second-generation fluoroquinolone antibiotic, belonging to a class of broad-spectrum antibacterials that act by inhibiting bacterial DNA gyrase and topoisomerase IV enzymes, historically used for urinary tract and respiratory tract infections.
The TxGNN model predicts it may be effective for **Laryngotracheitis (croup)**, with **0 clinical trials** and **0 publications** currently supporting this direction — making this a purely model-driven hypothesis at the earliest exploratory stage.
Notably, several other top-ranked predictions appear to reflect **known adverse effects** of fluoroquinolones (QT prolongation, aortic aneurysm) rather than therapeutic opportunities, raising important questions about model signal interpretation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (UTI, lower respiratory tract infections) |
| Predicted New Indication | Laryngotracheitis (Croup) |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological class, Lomefloxacin is a second-generation fluoroquinolone antibiotic that inhibits bacterial DNA gyrase (topoisomerase II) and topoisomerase IV — enzymes essential for bacterial DNA replication and repair. This results in broad-spectrum bactericidal activity covering Gram-negative organisms (including *Haemophilus influenzae*, *Moraxella catarrhalis*) and some Gram-positive pathogens relevant to respiratory tract infections.

Laryngotracheitis, commonly known as croup, is predominantly caused by parainfluenza viruses (types 1 and 2), with secondary bacterial superinfection occurring in a minority of severe or prolonged cases. The TxGNN prediction likely reflects the fluoroquinolone class's well-established coverage of respiratory bacterial pathogens and the knowledge graph edges connecting this drug class to upper and lower respiratory tract infection nodes — rather than a specific mechanistic link to croup pathophysiology. This represents a class-level association rather than a disease-specific therapeutic rationale.

The biological plausibility is therefore limited and indirect: lomefloxacin could theoretically be useful only in the uncommon scenario of bacterial superinfection complicating croup, but fluoroquinolones are not guideline-recommended for this indication, and the primary viral etiology would not respond to antibiotic treatment.

---

## ⚠️ Safety Signal Review — Adverse Effect Predictions

A critical observation from this evidence pack: **8 out of 10 top TxGNN predictions involve cardiac conditions**, and multiple entries explicitly flag that these predictions likely represent **fluoroquinolone adverse effect pathways** captured in the knowledge graph, not therapeutic opportunities:

| Rank | Predicted Disease | Signal Type | Key Concern |
|------|------------------|-------------|-------------|
| 3 | Heart Conduction Disease | ⛔ Reverse Safety Signal | Fluoroquinolones cause QTc prolongation via hERG channel blockade; may induce Torsades de Pointes |
| 10 | Heart Aneurysm | ⛔ FDA Black Box Warning | FDA 2018 black box warning: fluoroquinolones increase aortic aneurysm and dissection risk via MMP activation and collagen degradation |
| 6 | Pericardium Disease | ⚠️ Potential Harm | Fluoroquinolones have been associated with drug-induced pericarditis |
| 9 | Myocardial Rupture | ⚠️ Potential Harm | Fluoroquinolone collagen synthesis inhibition may worsen tissue fragility |

These predictions should be interpreted as **contraindications or cautions** discovered via adverse drug reaction–disease knowledge graph paths — not as repurposing leads.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lomefloxacin in any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for Lomefloxacin in any of the 10 predicted indications.

---

## Safety Considerations

Please refer to the package insert for safety information.

Based on known fluoroquinolone class effects (independent of the data pack), the following class-level cautions are relevant for this evaluation:

- **QT Prolongation**: Fluoroquinolones block hERG potassium channels; lomefloxacin carries QTc prolongation risk. Contraindicated with other QT-prolonging agents.
- **Aortic Aneurysm/Dissection**: FDA Black Box Warning (2018) applies to all systemic fluoroquinolones, including lomefloxacin. Avoid in patients with known aortic aneurysm or risk factors.
- **Tendinopathy/Tendon Rupture**: Class Black Box Warning; risk increased with corticosteroid co-use and in elderly patients.
- **Photosensitivity**: Lomefloxacin has notably high photosensitivity risk compared to other fluoroquinolones — a class-differentiating safety concern.
- **CNS Effects**: Seizures, confusion, and peripheral neuropathy are class-level risks.

---

## Conclusion and Next Steps

**Decision: Research Question (Hold for Most Cardiac Predictions)**

**Rationale:**
For the top-ranked indication (laryngotracheitis), this is a model-prediction-only signal (L5) with no supporting clinical trials or literature. The biological rationale is class-level and indirect, as croup is a viral condition where antibiotics have no primary role. For the cardiac predictions (ranks 2–10), the weight of evidence suggests these represent **adverse effect associations** rather than therapeutic opportunities — several are explicitly contraindicated based on known fluoroquinolone pharmacology.

**To proceed with laryngotracheitis as a research question, the following is needed:**

- Confirm mechanism of action data via DrugBank API (DG002 data gap)
- Literature review on fluoroquinolone use in bacterial tracheitis or croup superinfection (narrative review, not captured in evidence pack query)
- Clarify whether TxGNN cardiac predictions are being correctly classified as adverse-drug-reaction nodes vs. therapeutic-indication nodes in the knowledge graph — this may indicate a model calibration issue for this drug class
- Expert pharmacological consultation on fluoroquinolone class appropriateness for upper respiratory indications given the unfavorable safety profile (QT prolongation, tendinopathy, photosensitivity)
- Singapore market assessment: Drug is currently not marketed; registration pathway evaluation would be required before any clinical development consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

