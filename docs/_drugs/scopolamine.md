---
layout: default
title: Scopolamine
parent: Low Evidence (L5)
nav_order: 897
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Scopolamine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Peptic ulcer disease, allergic rhinitis, uveitis, motion sickness…"
monitor_inn: "Scopolamine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "atopic conjunctivitis", "rosacea conjunctivitis", "vernal conjunctivitis", "nasal cavity disease", "acute laryngopharyngitis"]
---

# Scopolamine
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

# Scopolamine: From Peptic Ulcer Disease and Motion Sickness to Cauda Equina Syndrome

## One-Sentence Summary

Scopolamine is a non-selective muscarinic antagonist, originally used for conditions such as peptic ulcer disease, motion sickness, irritable bowel syndrome, uveitis and allergic rhinitis.
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, allergic rhinitis, uveitis, motion sickness, irritable bowel syndrome and others (from the knowledge graph; no approved indication text is available for Singapore licences) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, scopolamine is a non-selective muscarinic antagonist (anticholinergic). Its efficacy in conditions such as motion sickness, gastrointestinal spasm and uveitis is established, and mechanistically it may be applicable to bladder and bowel dysfunction.

Cauda equina syndrome causes bladder and bowel dysfunction. Antimuscarinics can relieve detrusor overactivity and so may offer symptomatic relief. However, scopolamine would not treat the underlying compressive nerve injury, and the data do not support a direct link. The high TxGNN score is a computational prediction only.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | Score | Comment |
|---|---|---|---|
| 2 | Neurogenic bladder (obsolete term) | 99.98% | Plausible class-level antimuscarinic effect, but central side effects limit use and better bladder-selective agents exist |
| 3 | Papillary conjunctivitis | 99.98% | Indirect link; antihistamines and mast-cell stabilisers are more appropriate |
| 4 | Atopic conjunctivitis | 99.80% | Does not address IgE-mediated inflammation; may worsen dry eye |
| 5 | Rosacea conjunctivitis | 99.40% | No clear mechanism; tear-film reduction could aggravate symptoms |
| 6 | Vernal conjunctivitis | 99.08% | Th2-driven disease; link is only through allergic and ocular indications |
| 7 | Nasal cavity disease | 98.998% | Biologically coherent (existing rhinitis uses) but a very broad category |
| 8 | Acute laryngopharyngitis | 98.87% | Adjacent to historical pharyngitis and common cold uses; drying may be undesirable in acute infection |
| 9 | Idiopathic uveal effusion syndrome | 98.30% | Strongest mechanistic rationale (cycloplegia), but definitive management is usually surgical |
| 10 | Idiopathic panuveitis | 98.14% | Effectively an existing indication; symptomatic benefit only |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly supports the lead prediction (cauda equina syndrome). The only publication retrieved was for a lower-ranked prediction, nasal cavity disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31183806](https://pubmed.ncbi.nlm.nih.gov/31183806/) | 2019 | Preclinical (animal model) | Molecular Neurobiology | Intranasal melanin-concentrating hormone improved memory impairment in mouse models. Scopolamine was used only to induce amnesia, so this is not evidence of benefit for nasal disease. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07796P | FUCON INJECTION 20 mg/ml | Injection | Not available |
| SIN09563P | VACOPAN INJECTION 20 mg/ml | Injection | Not available |
| SIN02854P | HYOMIDE TABLET 10 mg | Tablet, sugar coated | Not available |
| SIN07177P | FUCON CAPSULE 10 mg | Capsule | Not available |
| SIN16636P | YSP HYOSCINE INJECTION 20MG/ML | Injection, solution | Not available |

A sixth licence, SIN07433P (HYOSUN SYRUP 5mg/5 ml), is also valid. All six are single-ingredient products and none is cancelled.

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug-disease edges, not package insert text):
- Cardiovascular and respiratory: hypertension, chronic obstructive pulmonary disease
- Eye, urinary and gastrointestinal: open-angle glaucoma, benign prostatic hyperplasia, gastric ulcer, pancreatitis
- Liver, kidney and gallbladder: liver failure, liver disease, hepatic coma, kidney disease, gallbladder disease, pyoureter
- Neuropsychiatric: epilepsy, psychotic and schizophrenia-spectrum disorders, anxiety and neurotic disorders, dysthymic disorder
- Metabolic and haematological: diabetes mellitus, diabetic ketoacidosis, porphyria, thrombocytopenia, neutropenia, agranulocytosis

**Drug Interactions:** 100 interactions were found. Examples of moderate-level interactions include:
- Other anticholinergics and antimuscarinics: hyoscyamine, aclidinium, amitriptyline, amantadine
- Sedating antihistamines: chlorpheniramine, acrivastine, phenyltoloxamine
- Opioids and CNS depressants: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, ethanol
- Others: botulinum toxin type A, phenylephrine, acebutolol, acetylcholine, loperamide

Minor interactions include acetaminophen and hydrochlorothiazide. For package insert warnings, please refer to the product label.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cauda equina syndrome is supported only by the model score (Evidence Level L5), with no trials or literature. Antimuscarinics could at most relieve symptoms, not treat the underlying cause. Scopolamine also has central side effects and a long list of contraindications, and better-suited bladder agents exist. Of the predictions, idiopathic uveal effusion syndrome has the most plausible mechanism, and idiopathic panuveitis largely overlaps with existing uses.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (a blocking gap for safety screening)
- Detailed mechanism of action data
- Scopolamine-specific clinical or observational evidence for the target indication
- Approved indication text for the Singapore licences
- Assessment of route compatibility (injectable, oral and syrup forms are available locally)
- Comparison against established treatments, including bladder-selective antimuscarinics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

