---
layout: default
title: Bisacodyl
parent: Low Evidence (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bisacodyl: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Constipation disorder"
---

# Bisacodyl
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

# Bisacodyl: From Constipation to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Bisacodyl is a stimulant laxative originally used to treat **constipation**.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but this rests on model output alone: **0 clinical trials** and **0 publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 97.69% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, bisacodyl is a stimulant laxative that acts locally on the colonic mucosa and enteric nerves to increase bowel movement and secretion. Its efficacy in constipation is established.

For the predicted indication, no plausible mechanistic link can be established from the data compiled for this report. Exercise-induced malignant hyperthermia is a skeletal muscle disorder linked to abnormal calcium release (for example, through the RYR1 receptor), which is unrelated to colonic stimulation. The high score is most likely an artifact of the model's graph neighbourhood rather than a pharmacological signal. Several other malignant hyperthermia entries (ranks 4 and 9) also appear among the top predictions, which suggests correlated rather than independent signals.

Other top-ranked predictions show the same pattern: dyspepsia, nephrogenic syndrome of inappropriate antidiuresis, common cold, pharyngitis, familial periodic paralysis, acute laryngopharyngitis and acute pulmonary heart disease all have no trials or literature. For some of these, bisacodyl's fluid and potassium loss could be a safety concern rather than a benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Bisacodyl has 11 valid single-ingredient registrations in Singapore and none cancelled. The approved indication text is not available for any of them. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN02432P | Laxodyl Tablet 5 mg | Enteric coated tablet | Sunward Pharmaceutical Private Limited |
| SIN02689P | S.L. Laxative Tablet 5 mg | Enteric coated tablet | Beacons Pharmaceuticals Pte. Ltd. |
| SIN03319P | Unilax Tablet 5 mg | Enteric coated tablet | Beacons Pharmaceuticals Pte. Ltd. |
| SIN03615P | Bisacodyl Tablet 5 mg | Enteric coated tablet | Beacons Pharmaceuticals Pte. Ltd. |
| SIN14002P | Bisacodyl Suppositories 5 mg | Suppository | Y.S.P. Industries (M) Sdn. Bhd. |

Available forms are oral enteric coated tablets and suppositories.

---

## Safety Considerations

- **Contraindications (from knowledge graph associations, not label text)**: The model's knowledge graph links bisacodyl with caution in the following conditions: ileus, intestinal obstruction, toxic megacolon, appendicitis, anus disease, *Clostridium difficile* colitis, epilepsy, kidney disease, anuria, pyoureter, nephrocalcinosis, congestive heart failure, atrioventricular block, potassium deficiency disease, hypercalcemia disease, phosphorus metabolism disease, hyperkalemic periodic paralysis, periodic paralysis, hypoaldosteronism disease and myotonia congenita.
- **Drug Interactions**: 100 interactions were identified, and all those displayed are rated Moderate. Examples include furosemide, hydrochlorothiazide, acetazolamide, amiloride, hydrocortisone, triamcinolone, amiodarone, tramadol, salbutamol and propofol. Many involve diuretics, corticosteroids and other agents that can add to electrolyte loss, particularly potassium.
- **Relevance to the predicted indications**: Bisacodyl-induced fluid and potassium loss could theoretically be harmful in water-balance disorders and periodic paralysis.

Please refer to the package insert for label warnings.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no identifiable mechanistic link. The pharmacology of a locally acting colonic stimulant does not fit a skeletal muscle calcium-release disorder, and the potential fluid and electrolyte effects add safety concerns.

**To proceed, the following is needed:**
- Detailed mechanism of action data for bisacodyl
- Package insert warnings and contraindications from the HSA
- Any preclinical or clinical evidence linking bisacodyl to the predicted condition
- Independent review of whether the clustered malignant hyperthermia predictions reflect a true signal or a model artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

