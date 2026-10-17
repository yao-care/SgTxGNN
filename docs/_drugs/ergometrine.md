---
layout: default
title: Ergometrine
parent: Low Evidence (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ergometrine: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not listed in the Singapore licence text (the approved indication fie…"
monitor_inn: "Ergometrine"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "nephrogenic syndrome of inappropriate antidiuresis", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "leprosy", "pulmonary hypertension"]
---

# Ergometrine
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

# Ergometrine: From Uterotonic Use to Hypertrichosis (Computational Prediction Only)

## One-Sentence Summary

Ergometrine is an ergot alkaloid used as a uterotonic. It is marketed in Singapore as an injection (Syntometrine). The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** support this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Singapore licence text (the approved indication field is empty) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From general pharmacology, ergometrine is an ergot alkaloid that acts as a uterotonic through serotonin (5-HT2), alpha-adrenergic and dopaminergic receptor activity.

None of these pathways is an established driver of hair growth, and no plausible mechanistic link to hypertrichosis was identified. The very high TxGNN score most likely reflects a graph-based prediction artefact rather than a real biological relationship.

The other top predictions fall into the same pattern. They include Ambras-type congenital hypertrichosis (a genetic disorder), nephrogenic syndrome of inappropriate antidiuresis, malformation syndromes, genetic hair shaft abnormalities and leprosy. All lack a pharmacological rationale and have no trials or literature.

Two predictions have some indirect literature:
- **Migraine disorder (rank 7, score 99.93%):** Related ergot alkaloids such as ergotamine, dihydroergotamine and methysergide are established in migraine therapy, so a class-level link is plausible. The retrieved papers are a methysergide monograph and a case report of postpartum cerebral angiopathy, neither of which shows efficacy for ergometrine. Its vasoconstrictive risk is a safety concern.
- **Pulmonary hypertension (rank 10, score 99.83%):** The literature points to risk rather than benefit, because ergot alkaloids can raise vascular resistance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hypertrichosis.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03588P | SYNTOMETRINE INJECTION (Panpharma GmbH) | Injection | Not stated in the licence record |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** hypertensive disorder, hypertension, epilepsy, kidney disease, liver disease, gallbladder disease, stroke and cerebrovascular disorders, cerebral infarction, arteriosclerosis obliterans, HELLP syndrome, pyoureter.
- **Drug interactions:** 83 interactions were recorded. Major-level examples include isometheptene, epinephrine, ephedrine, lorcaserin, clarithromycin and cobicistat. Moderate-level examples include doxycycline, tetracycline, aprepitant, dexamethasone, cimetidine, miconazole and clotrimazole.
- **Vasoconstriction:** Case literature on postpartum cerebral angiopathy and cautions about uterotonics in cardiac disease and pulmonary hypertension raise concern about ischaemic risk in any new use.

Please also refer to the package insert for full warnings and contraindications, as this information was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible mechanism. The vasoconstrictive safety profile and the knowledge-graph contraindications make a new use harder to justify. The indirect migraine signal is class-based and does not support ergometrine specifically.

**To proceed, the following is needed:**
- The Singapore package insert, including warnings, contraindications and approved indications
- Mechanism of action data from DrugBank
- Direct preclinical or clinical evidence for the predicted indication
- If a new indication is pursued, migraine is the only candidate with a plausible class-level rationale, and it would need a dedicated benefit-risk assessment of vasoconstrictive and cerebrovascular risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

