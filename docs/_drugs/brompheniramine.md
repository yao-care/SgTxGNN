---
layout: default
title: Brompheniramine
parent: Medium Evidence (L3-L4)
nav_order: 179
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Brompheniramine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, common cold…"
monitor_inn: "Brompheniramine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "pharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis", "anorectal stricture"]
---

# Brompheniramine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Brompheniramine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Brompheniramine is a first-generation H1-antihistamine, originally used for allergic rhinitis, vasomotor rhinitis, the common cold, allergic conjunctivitis and urticaria.
The TxGNN model predicts it may be effective for **allergic urticaria**, but **no clinical trials and no publications** were found in the data compiled for this report, so support rests on class-level mechanistic reasoning only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, common cold, atopic/papillary/vernal conjunctivitis, familial dermatographia, urticaria, angioedema (the Singapore licence record contains no indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, brompheniramine is a first-generation H1-antihistamine. It blocks histamine at H1 receptors and also has anticholinergic activity.

Allergic urticaria is largely driven by mast cell degranulation and histamine release, so H1 blockade is mechanistically coherent. Urticaria and angioedema are already listed among the drug's original indications, so this prediction is effectively an on-label or near-label use rather than true repurposing.

The other predicted indications follow the same pattern. Cold urticaria, nasal cavity disease and nasopharyngitis overlap with existing indications. Pharyngitis and acute laryngopharyngitis would at most gain indirect symptom relief. Recalcitrant atopic dermatitis and atopic IgE responsiveness are unlikely to benefit beyond symptom control, because histamine is not the dominant driver. Rosacea conjunctivitis is also unlikely to benefit, and oral anticholinergic drying could worsen dry eye. Anorectal stricture (score 80.9%) has no plausible mechanistic link and is probably a knowledge-graph artifact.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10526P | BOMEX TABLET 4 mg | Tablet (oral) | Not stated in the registration record |

The single registration is a valid single-ingredient product made by Y S P Industries (M) Sdn Bhd.

---

## Safety Considerations

**Contraindications flagged in the drug-disease knowledge graph (not package-insert text):**
These conditions are linked to the drug as contraindications or cautions. They need confirmation against the official label.
- **Cardiovascular:** hypertension, hypotensive disorder, coronary artery disease, myocardial infarction, coronary thrombosis
- **Respiratory:** chronic obstructive pulmonary disease (including severe early onset)
- **Gastrointestinal:** gastric ulcer, peptic ulcer disease, inflammatory bowel disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, pancreatitis
- **Hepatic and renal:** liver failure, liver disease, gallbladder disease, kidney disease, pyoureter
- **Endocrine and metabolic:** hypothyroidism, myxedema, congenital hypothyroidism, diabetes mellitus, diabetic ketoacidosis
- **Neurological and other:** epilepsy, substance abuse/dependence, benign prostatic hyperplasia, ocular hypertension, hemoglobinopathy

**Drug Interactions:** The interaction query returned 100 records, and the 20 shown include the following.
- **Major:** potassium chloride and potassium citrate
- **Moderate, anticholinergics (additive effects):** hyoscyamine, atropine, scopolamine, dicyclomine, clidinium, glycopyrronium (including topical), mepenzolate, methscopolamine, propantheline
- **Moderate, opioids and CNS-active agents:** morphine (including liposomal), opium, loperamide, eluxadoline, dronabinol, nabilone
- **Moderate, other:** metoclopramide

Package-insert warnings and contraindications are not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.87%), and H1 blockade is mechanistically sound for allergic urticaria. However, urticaria is already an original indication, and no clinical trials or literature were found for the predicted use. Newer non-sedating antihistamines are generally preferred, which weakens the case for a sedating first-generation drug. The package-insert safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications for BOMEX from the HSA website
- Detailed mechanism of action data (MOA)
- Brompheniramine-specific clinical or literature evidence in urticaria
- Confirmation of whether the approved Singapore indications already cover urticaria
- A comparison with non-sedating H1-antihistamines, and a review of the safety profile, including the knowledge-graph contraindications and anticholinergic interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

