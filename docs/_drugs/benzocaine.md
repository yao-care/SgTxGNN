---
layout: default
title: Benzocaine
parent: Low Evidence (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Benzocaine: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Tinea pedis, dermatitis, pharyngitis, tinea corporis, tinea infection"
monitor_inn: "Benzocaine"
predicted_indications: ["papillary conjunctivitis", "blepharoconjunctivitis", "rosacea conjunctivitis", "dyspepsia", "ulcerative blepharitis", "parasitic eyelid infestation", "noninfectious dermatoses of eyelid", "nasal cavity disease", "acute laryngopharyngitis"]
---

# Benzocaine
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

# Benzocaine: From Tinea Pedis, Dermatitis and Pharyngitis to Papillary Conjunctivitis

## One-Sentence Summary

> Benzocaine is a topical ester local anaesthetic, originally used for symptom relief in conditions such as tinea pedis, dermatitis, pharyngitis, tinea corporis and tinea infection.
> The TxGNN model predicts it may be effective for **papillary conjunctivitis**,
> but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on a model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, dermatitis, pharyngitis, tinea corporis, tinea infection (from the TxGNN knowledge graph; no approved indication text is available for the Singapore licences) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Benzocaine is known as a topical ester local anaesthetic that blocks voltage-gated sodium channels. That could in principle numb ocular surface irritation.

The link to the original indications is symptomatic only. Benzocaine relieves pain and itch in skin and throat conditions, and it does not treat the underlying infection or inflammation. Papillary conjunctivitis is often allergic or contact-related, so the mechanistic fit is weak.

There are also specific concerns about ocular use: possible corneal toxicity, and benzocaine's recognised potential as a contact sensitiser, which could worsen an allergic eye condition. The high TxGNN score should therefore be read as a hypothesis, not as evidence of benefit.

**Other predicted indications (ranked by TxGNN score):**

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Blepharoconjunctivitis | 98.79% | L5 | Hold. Only symptomatic relief is conceivable, with no anti-infective or anti-inflammatory activity. |
| 3 | Rosacea conjunctivitis | 98.62% | L5 | Hold. The disease is driven by inflammation and meibomian gland dysfunction, which benzocaine does not address. |
| 4 | Dyspepsia | 98.29% | L4 | Research question. There is indirect evidence (see below). |
| 5 | Ulcerative blepharitis | 98.19% | L5 | Hold. No mechanism links benzocaine to the infectious or inflammatory cause. |
| 6 | Parasitic eyelid infestation | 98.04% | L5 | Hold. No antiparasitic activity. |
| 7 | Cutaneous candidiasis | 97.87% | L5 | Hold. Benzocaine is not an antifungal. |
| 8 | Noninfectious dermatoses of eyelid | 97.69% | L5 | Hold. The eyelid is a sensitive site and benzocaine is a contact sensitiser. |
| 9 | Nasal cavity disease | 96.68% | L5 | Hold. The term is nonspecific and no disease-specific evidence was provided. |
| 10 | Acute laryngopharyngitis | 96.63% | L4 | Research question. It is an anatomical extension of the existing pharyngitis use. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for papillary conjunctivitis. No trials were found for the other nine predicted indications either.

---

## Literature Evidence

Currently no related literature is available for papillary conjunctivitis.

The only publications found relate to the fourth-ranked prediction, dyspepsia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15219296](https://pubmed.ncbi.nlm.nih.gov/15219296/) | 2004 | RCT | The Journal of Emergency Medicine | Single-blinded comparison of viscous lidocaine versus benzocaine as the topical anaesthetic in a GI cocktail for dyspepsia in emergency patients. Benzocaine was tested as a comparator component, so benzocaine-specific efficacy is not established. |
| [23565580](https://pubmed.ncbi.nlm.nih.gov/23565580/) | 2013 | Mechanistic/physiology study | Neurogastroenterology and Motility | Examined the role of duodenal mucosal nerve endings in the acid-induced duodenogastric reflex using benzocaine in healthy volunteers. It is consistent with a local anaesthetic acting on mucosal sensory nerves, but it is not a treatment study. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07825P | HURRICAINE GEL 20% | Gel | Not stated |
| SIN10762P | TOPICALE GEL 180 mg/g | Gel | Not stated |
| SIN08158P | HURRICAINE SPRAY 20% | Spray | Not stated |
| SIN12391P | FREEZ-EEZ TOPICAL ANESTHETIC GEL 20% w/w | Gel | Not stated |
| SIN08535P | HORF LOZENGES | Lozenge | Not stated |

A sixth licence, SIN04392P (DORITHRICIN THROAT LOZENGES, lozenge), is also valid. All 6 licences are valid single-ingredient products. No approved indication text is available for any of them.

---

## Safety Considerations

- **Methemoglobinemia**: this is a known concern with benzocaine on mucosal surfaces, noted for the laryngopharyngeal use.
- **Contact sensitisation**: benzocaine is a recognised contact sensitiser. This matters particularly for ocular and eyelid uses, where it could worsen allergic or dermatitic conditions.
- **Ocular use**: there are concerns about corneal toxicity with topical use in the eye.
- **Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not label text, so they need verification against the package insert): liver failure and liver disease, kidney disease, epilepsy, porphyria (including inherited porphyria), blood coagulation disease, thrombocytopenia, neutropenia and agranulocytosis, diabetes mellitus and diabetic ketoacidosis, hepatic coma and encephalopathy, hypercalcaemia, hyperparathyroidism, and substance abuse/dependence. Others listed are anxiety and neurotic disorders, herpes simplex infection, sarcoidosis and gastritis.
- **Drug interactions**: no interaction records were found.

Please refer to the package insert for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, papillary conjunctivitis, rests on a model score alone (L5), with no trials or publications. The plausible benefit is only symptomatic, while ocular sensitisation and corneal toxicity concerns could outweigh it. Of the other predictions, dyspepsia and acute laryngopharyngitis (both L4) are the most reasonable research questions.

**To proceed, the following is needed:**
- The package insert warnings and contraindications from the HSA website, which are required before any safety screening.
- Mechanism of action data from DrugBank.
- Approved indication text for the Singapore licences.
- For ocular indications, preclinical ocular tolerability and sensitisation data, and a check of route and formulation compatibility (no ophthalmic benzocaine product is registered in Singapore).
- For dyspepsia or acute laryngopharyngitis, a targeted literature review and a pilot study design.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

