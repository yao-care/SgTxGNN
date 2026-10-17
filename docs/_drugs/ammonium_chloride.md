---
layout: default
title: Ammonium Chloride
parent: Low Evidence (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ammonium Chloride: predicted new indication Acute laryngopharyngitis (evidence level L5). Approved use: Pharyngitis, common cold, nasopharyngitis"
monitor_inn: "Ammonium chloride"
predicted_indications: ["acute laryngopharyngitis", "nasal cavity disease", "faucial diphtheria", "cervical disc degenerative disorder", "allergic urticaria", "trigeminal autonomic cephalalgia", "headache disorder", "tracheal disease", "papillary conjunctivitis", "gonococcal urethritis"]
---

# Ammonium Chloride
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

# Ammonium Chloride: From Pharyngitis and Common Cold to Acute Laryngopharyngitis

## One-Sentence Summary

Ammonium chloride is a traditional expectorant, originally used for pharyngitis, common cold and nasopharyngitis.
The TxGNN model predicts it may be effective for **acute laryngopharyngitis**, but **0 clinical trials** and **0 publications** currently support this prediction.
It is essentially an extension of the existing label, not a true repurposing finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold, nasopharyngitis (the Singapore licence records contain no indication text) |
| Predicted New Indication | Acute laryngopharyngitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ammonium chloride is a long-established expectorant, usually found in combination cough syrups. Its efficacy in upper respiratory conditions such as pharyngitis and the common cold is part of its traditional use, and mechanistically it may be applicable to acute laryngopharyngitis.

Acute laryngopharyngitis is anatomically and clinically very close to the approved indications (pharyngitis, nasopharyngitis, common cold). The high TxGNN score most likely reflects this proximity in the knowledge graph. It does not reflect new biological evidence.

Other predicted indications are much weaker. Examples are faucial diphtheria, cervical disc degenerative disorder and gonococcal urethritis, which have no plausible link to the drug's pharmacology. The top-ranked prediction is therefore the most reasonable, but it remains unvalidated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for acute laryngopharyngitis.

---

## Singapore Market Information

All 17 licences are valid single-ingredient registrations. The licence records contain no approved indication text. The table shows 5 of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02839P | BEANAMINE EXPECTORANT | Solution | Not stated in the data |
| SIN08782P | DIPHEN 5 EXPECTORANT | Syrup | Not stated in the data |
| SIN08799P | DIPHEN 10 EXPECTORANT | Syrup | Not stated in the data |
| SIN09014P | PHENEXPECT SYRUP | Syrup | Not stated in the data |
| SIN03335P | XSP-BENA EXPECTORANT | Syrup | Not stated in the data |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text)**: The graph links ammonium chloride to several conditions where use is a concern. The main ones are:
  - Liver failure and impaired renal function
  - Anuria
  - Adrenocortical insufficiency and Addison disease
  - Hypertension
  - Pulmonary edema
  - Coronary artery disease and myocardial ischemia
  - Epilepsy
  - Peptic ulcer disease
  - Hyperthyroidism
  - Angle-closure glaucoma
  - Others (e.g., benign prostatic hyperplasia, anxiety disorders, necrotizing enterocolitis)
- **Drug Interactions**: 21 interactions are recorded. None is major.
  - **Moderate**: amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine
  - **Minor**: ephedrine, pseudoephedrine, tricyclic antidepressants (amitriptyline, clomipramine, desipramine, doxepin, imipramine, nortriptyline, protriptyline, trimipramine), methadone, mexiletine, flecainide

Package insert warnings and contraindications have not been retrieved. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no trials and no literature, and the evidence level is L5. The prediction mostly restates the existing label for pharyngitis and the common cold, so it adds little new repurposing value. The knowledge-graph contraindication signals also remain unreviewed against the label.

**To proceed, the following is needed:**
- Singapore package insert warnings, contraindications and approved indication text for the 17 licences
- Mechanism of action data
- Confirmation of whether acute laryngopharyngitis is already covered by the current labelled indications, since this would make the prediction a label clarification and not a repurposing project
- Review of the knowledge-graph contraindications (especially renal, hepatic, and acid-base risks) against the label

---

## Other Predicted Indications Worth Noting

Only one other prediction has any supporting literature, and it is weak.

- **Headache disorder (rank 7, score 97.99%, evidence level L4)**: Four 1950s reports describe ammonium chloride in chronic migraine and chronic headache.
  - They are historical and likely uncontrolled, and their abstracts were not available.
  - They are hypothesis-generating at best (PMIDs [13254186](https://pubmed.ncbi.nlm.nih.gov/13254186/), [13345397](https://pubmed.ncbi.nlm.nih.gov/13345397/), [13317850](https://pubmed.ncbi.nlm.nih.gov/13317850/), [13466764](https://pubmed.ncbi.nlm.nih.gov/13466764/)).
  - Any follow-up would need a modern controlled design and a safety review (metabolic acidosis, hepatic or renal impairment).
- **Allergic urticaria and tracheal disease**: The retrieved articles are spurious matches (occupational epoxy dermatitis, and a plant extract study), so they provide no support.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

