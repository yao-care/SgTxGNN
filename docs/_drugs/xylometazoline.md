---
layout: default
title: Xylometazoline
parent: Medium Evidence (L3-L4)
nav_order: 1080
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-14
monitor_inn: "Xylometazoline"
predicted_indications: ["nasal cavity disease"]
description: "Xylometazoline: predicted new indication Nasal cavity disease (evidence level L3). Approved use: Not recorded in the local data"
---

# Xylometazoline
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
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

## Xylometazoline: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Xylometazoline is a topical nasal decongestant, originally used for pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **no registered clinical trials** and only **6 publications** (small clinical and physiological studies) supporting this direction.
This prediction largely overlaps with the existing use of the drug, so it is an extension of an existing indication rather than a truly novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L3 |
| Singapore Market Status | Marketed (valid licences: 3 of 3) |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled sources. Based on known pharmacology, xylometazoline is a topical alpha-adrenergic agonist. It constricts blood vessels in the nasal mucosa, which reduces swelling and lowers nasal airway resistance. Pharmacology records link it to alpha-2 adrenoceptor subtypes (2A, 2B, 2C) and the alpha-1D adrenoceptor, although affinity data at the human targets are not available, so a primary target has not been confirmed.

The original indications (common cold and pharyngitis) involve upper airway mucosal congestion. "Nasal cavity disease" is a broad category that covers this same problem. Decongestion, widening of the nasal cavity and preparing the nose for endoscopy all rely on the same vasoconstrictive effect. The prediction is therefore mechanistically reasonable, but it largely restates the drug's current use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24158493](https://pubmed.ncbi.nlm.nih.gov/24158493/) | 2013 | RCT (double-blind, placebo-controlled) | JAMA Otolaryngol Head Neck Surg | Children's nasal preparation spray (decongestant plus local anaesthetic) before flexible nasendoscopy compared with placebo |
| [22427029](https://pubmed.ncbi.nlm.nih.gov/22427029/) | 2013 | Prospective randomised blinded study (100 patients) | Eur Arch Otorhinolaryngol | Cotton pledget packing compared with topical spray for nasal preparation before endoscopy |
| [24023995](https://pubmed.ncbi.nlm.nih.gov/24023995/) | 2013 | Clinical study | Korean J Anesthesiol | Xylometazoline spray compared with epinephrine gauze packing for expanding the nasal cavity before nasotracheal intubation |
| [8740084](https://pubmed.ncbi.nlm.nih.gov/8740084/) | 1996 | Double-blind randomised study (18 subjects) | Arzneimittel-Forschung | Rhinomanometric comparison of a tuaminoheptane/N-acetylcysteine decongestant against xylometazoline and placebo |
| [1281924](https://pubmed.ncbi.nlm.nih.gov/1281924/) | 1992 | Physiological study | Rhinology | Nasal airflow asymmetry in healthy subjects and in people with colds, and how xylometazoline affects it |
| [34783482](https://pubmed.ncbi.nlm.nih.gov/34783482/) | 2021 | Review | Vestnik Otorinolaringologii | Treatment of inflammatory nasal and sinus diseases in the elderly, including combined decongestant sprays |


---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11622P | OTRIVIN NASAL DROPS 0.05% | Solution | Not stated in the licence record |
| SIN11624P | OTRIVIN NASAL SPRAY 0.1% | Spray | Not stated in the licence record |
| SIN15198P | SNUP STADA® SPRAY 0.1% | Spray | Not stated in the licence record |

---

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease links, not label text):** hypertension and hypertensive disorder, diabetes mellitus, diabetic ketoacidosis, heart disease and cardiovascular disease, hyperthyroidism, Graves disease and thyrotoxicosis.
- **Rebound congestion:** Prolonged use can cause rhinitis medicamentosa (rebound congestion), so duration of use should be limited.
- **Neurovascular risk:** A case report (CMAJ, 2020) links recurrent thunderclap headaches from reversible cerebral vasoconstriction syndrome to xylometazoline use together with duloxetine and rhinitis medicamentosa. This is a safety signal, not evidence of benefit for headache.
- **Drug interactions:** No drug-drug interactions are listed. The interaction query returned only receptor-binding pharmacology records (alpha-1D, alpha-2A, alpha-2B, alpha-2C adrenoceptors and a mouse TAAR4P entry).

Please refer to the package insert for full warnings, as the label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The nasal cavity disease prediction is mechanistically sound and supported by small clinical and physiological studies, including randomised comparisons in nasal procedure preparation. It overlaps heavily with xylometazoline's existing use for nasal congestion and colds. There are no registered trials, and the evidence is of limited size.

**To proceed, the following is needed:**
- Singapore package insert text (warnings, contraindications and approved indications), since the licence records contain no indication text
- Detailed mechanism of action and human receptor affinity data
- A defined scope for "nasal cavity disease" (for example procedural decongestion versus symptomatic treatment)
- A limit on duration of use to prevent rebound congestion
- Cardiovascular and cerebrovascular safety screening for patients with hypertension, heart disease, diabetes or thyroid disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

