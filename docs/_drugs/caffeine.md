---
layout: default
title: Caffeine
parent: Low Evidence (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Caffeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis…"
monitor_inn: "Caffeine"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "acute laryngopharyngitis", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
---

# Caffeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Caffeine: From Headache and Rhinitis Indications to Nasal Cavity Disease

## One-Sentence Summary

Caffeine is a central nervous system stimulant, originally used for allergic and vasomotor rhinitis, migraine and other headache disorders, and the common cold and pharyngitis (typically in combination analgesic and cold products).
The TxGNN model predicts it may be effective for **nasal cavity disease**, but **no clinical trials** and only **3 publications** (preclinical or tangential) support this direction.
The evidence is essentially a computational prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis, common cold, headache disorders (cluster headache, paroxysmal hemicrania, hemicrania continua) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

*Note: The approved indication text is not recorded in the Singapore licence data compiled for this report. The original indications above come from the TxGNN knowledge graph.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, caffeine is an adenosine receptor antagonist and has vasoconstrictive effects. Its efficacy in headache and cold-type conditions is established mainly as a component of combination products, and it may mechanistically be applicable to nasal conditions.

The prediction appears to be driven largely by proximity to caffeine's existing rhinitis indications (allergic and vasomotor rhinitis). Bitter taste receptors are also expressed in airway and nasal tissue, which offers another possible link.

However, the retrieved literature does not show a therapeutic effect in nasal cavity disease. It consists of a bitter taste receptor review, a nasal caffeine gel formulated for cognition after sleep deprivation, and a rat lung carcinogenesis study with black tea. The high score therefore reflects network similarity rather than direct evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are expressed in airways, including the nasal cavity, and have a possible role in airway physiology |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Formulation/preclinical | Current Drug Delivery | Nasal thermo-sensitive caffeine in situ gel designed to improve cognition after sleep deprivation (not a nasal disease use) |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine inhibited NNK-induced lung tumours in rats (not nasal disease) |

---

## Singapore Market Information

Twenty valid single-ingredient registrations are on record. The approved indication text is not available for any of them. Five main authorisations are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09110P | PANADOL EXTRA CAPLET | Tablet | Not recorded |
| SIN14833P | PANADOL EXTRA EFFERVESCENT TABLET 500MG/65MG | Effervescent tablet | Not recorded |
| SIN13452P | Panadol FluMax Caplets | Film-coated tablet | Not recorded |
| SIN07778P | STONA COLD CAPLETS | Film-coated tablet | Not recorded |
| SIN16929P | GENCEBOK SOLUTION FOR INFUSION 10MG/ML | Infusion solution | Not recorded |

Available dosage forms include oral capsules and tablets (plain, film-coated, sugar-coated, effervescent) and one injectable infusion solution.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text)**: hypertension, orthostatic hypotension, long QT syndrome, liver failure and liver disease, kidney disease, epilepsy, insomnia, anxiety disorders, COPD, peptic and gastric ulcer, inflammatory bowel disease, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism, porphyria, and others.
- **Drug Interactions**: 75 interactions recorded. Major: cocaine (nasal and topical). Moderate examples: alosetron, adenosine, anagrelide, bendamustine, capmatinib, ciprofloxacin, cycloserine, dipyridamole, duloxetine, obeticholic acid. Minor examples: acetylsalicylic acid, cimetidine, atazanavir, disulfiram.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by model similarity to existing rhinitis indications. There are no clinical trials, and the retrieved literature is preclinical or off-target, so the evidence is at L5. The nasal route would also need a suitable formulation, and the knowledge graph lists several cardiovascular and neurological cautions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently missing, blocking safety screening)
- Mechanism of action data (e.g. from DrugBank)
- Clinical or well-designed preclinical evidence of benefit in specific nasal conditions
- Assessment of route and formulation suitability for nasal use

---

### Other Predicted Indications (for reference)

| Rank | Disease | Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|---|
| 2 | Thrombotic disease | 99.90% | L4 | Hold | Reviews on hemostasis show inconsistent effects, possibly harmful |
| 3 | Acute laryngopharyngitis | 99.89% | L5 | Hold | Restates existing pharyngitis/cold indications; no evidence retrieved |
| 4 | Papillary conjunctivitis | 99.79% | L5 | Hold | Speculative link to allergic inflammation |
| 5 | Neuralgia | 99.34% | L4 | Research Question | Rat studies support analgesic adjuvant role; no human trials |
| 6 | Glossodynia | 99.26% | L5 | Hold | No evidence retrieved |
| 7 | Coccygodynia | 99.22% | L5 | Hold | No evidence retrieved |
| 8 | Trigeminal autonomic cephalalgia | 99.21% | L4 | Research Question | Largely overlaps existing headache indications |
| 9 | Hypnic headache | 99.17% | L3 | Research Question | Case series and reviews describe caffeine as first-line therapy; no controlled trials |
| 10 | Vein disease | 99.06% | L4 | Hold | Only indirect, mostly off-target evidence |

Among these, **hypnic headache** has the strongest supporting evidence (case series and narrative reviews recommending caffeine, with no randomised trials) and may be the more promising candidate for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

