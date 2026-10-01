---
layout: default
title: Fenoterol
parent: Low Evidence (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Fenoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fenoterol: From Bronchodilator Use to Multiple System Atrophy

## One-Sentence Summary

Fenoterol is a beta2-adrenergic agonist bronchodilator, marketed in Singapore mainly as a component of Berodual and Duovent inhalation products. The registration records supplied contain no indication text.
The TxGNN model predicts it may be effective for **multiple system atrophy (MSA)**, but **no clinical trials and no publications** support this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (fenoterol is a beta2-agonist bronchodilator) |
| Predicted New Indication | Multiple system atrophy |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, fenoterol is a beta2-adrenergic agonist. It relaxes airway smooth muscle and is used to relieve bronchospasm. Its efficacy in airway disease is established, but this does not carry over to MSA.

MSA is a neurodegenerative disease. Beta2-mediated vasodilation could worsen the neurogenic orthostatic hypotension typical of MSA. So the pharmacology does not support a benefit here, and it raises a plausible safety concern. No rationale for disease modification was identified. The high score is best read as a knowledge-graph association, not as evidence of efficacy.

The other top predictions show the same pattern. None has any retrieved trial or publication.

- **Postural orthostatic tachycardia syndrome (99.61%)**: beta-agonism would be expected to raise heart rate and could worsen symptoms.
- **Variably protease-sensitive prionopathy (99.54%)**: no plausible link to prion misfolding or clearance.
- **Open-angle glaucoma (99.43%), primary hereditary glaucoma (99.37%) and glaucoma 1, open angle (98.16%)**: only a weak adrenergic effect on intraocular pressure. The first and third are near-duplicate ontology terms, and inhaled or systemic exposure differs from topical ocular delivery.
- **Raynaud disease (99.41%)**: a theoretical vasodilatory rationale, but systemic cardiac effects and better-supported alternatives such as calcium channel blockers.
- **Sinoatrial block (99.35%) and sinoatrial node disease (99.25%)**: a theoretical chronotropic rationale, but proarrhythmic risk.
- **Anaphylaxis (98.28%)**: could only help with the bronchospasm component. Epinephrine remains first-line.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07913P | DUOVENT UDVS NEBULISER SOLUTION | Solution | Not stated in registration data |
| SIN11739P | BERODUAL N METERED DOSE INHALER | Aerosol, spray | Not stated in registration data |
| SIN02664P | BERODUAL SOLUTION | Solution | Not stated in registration data |

All three products are inhaled or nebulised forms. Whether these routes suit MSA, glaucoma or any other predicted disease has not been assessed.

## Safety Considerations

Please refer to the package insert for safety information.

Pharmacology-based concerns raised in the prediction review:
- **MSA:** possible worsening of neurogenic orthostatic hypotension through beta2-mediated vasodilation.
- **POTS:** possible increase in heart rate and symptoms.
- **Cardiac conduction disorders:** proarrhythmic potential.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions are model-only (L5) with no supporting trials or literature. For the top prediction (MSA) and several others (POTS, sinoatrial disorders), the known pharmacology points toward possible harm rather than benefit.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications and approved indications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- A targeted literature and trial search for fenoterol or beta2-agonists in the top predicted diseases
- A safety and direction-of-effect review, especially for MSA, POTS and the cardiac conduction disorders
- An assessment of route compatibility, since the current products are inhaled or nebulised
- Merging duplicate glaucoma entries for review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

