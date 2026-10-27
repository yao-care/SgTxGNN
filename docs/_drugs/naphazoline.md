---
layout: default
title: Naphazoline
parent: Low Evidence (L5)
nav_order: 698
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Naphazoline: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not stated in the Singapore license records (the product types are na…"
monitor_inn: "Naphazoline"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Naphazoline
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

## Naphazoline: From Nasal and Ocular Decongestion to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Naphazoline is a topical alpha-adrenergic vasoconstrictor used as a nasal and ocular decongestant (it reduces redness and swelling by narrowing blood vessels).
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore license records (the product types are nasal spray, nebuliser and ophthalmic solution; reduction of eye redness is the known clinical use) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. From pharmacology data, naphazoline binds alpha-1A, alpha-2A and alpha-2C adrenoceptors. It is a vasoconstrictor that temporarily reduces eye redness by narrowing swollen blood vessels.

The prediction is **not well supported mechanistically**. Hypotrichosis simplex of the scalp is a genetic hair disorder, and no known mechanism links alpha-adrenergic vasoconstriction to hair follicle growth. Vasoconstriction could even reduce scalp blood flow, the opposite of what a hair-growth agent needs. The high TxGNN score most likely reflects proximity in the knowledge graph rather than pharmacology.

The other top-ranked predictions show the same pattern. They are mostly hair-related conditions (congenital hypotrichosis milia, diffuse alopecia areata, alopecia, hypertrichosis) and rare congenital syndromes, none with a plausible mechanism. The two glaucoma predictions (primary hereditary glaucoma and open-angle glaucoma) have a plausible ocular route, but they also carry a safety concern (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03722P | NAZAL SPRAY | Spray | Not stated in records |
| SIN07343P | FLUCUR NEBULISER | Spray | Not stated in records |
| SIN04717P | NAPHCON-A STERILE OPHTHALMIC SOLUTION | Solution | Not stated in records |

All three licenses are valid single-ingredient products.

---

## Safety Considerations

- **Disease-related cautions from the knowledge graph** (drug-disease contraindication links in the TxGNN knowledge graph, not label text):
  - Cardiovascular: hypertension, hypertensive disorder, cardiovascular disease, heart disease
  - Metabolic and endocrine: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
  - Ocular: angle-closure glaucoma, closed-angle glaucoma, eye infectious disease, conjunctivitis
- **Relevance to glaucoma predictions:** alpha-agonists can cause pupil dilation, which carries a risk of angle closure in susceptible eyes. Any glaucoma use would need to overcome this concern.
- **Drug Interactions:** Pharmacology data show naphazoline acts on alpha-1A, alpha-2A and alpha-2C adrenoceptors (human) and a mouse trace amine receptor (Taar4). No drug-drug interaction levels were reported.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5), with no clinical trials or relevant publications. The pharmacology argues against a hair-growth effect, and the opposite effect (reduced perfusion) is plausible. For the glaucoma-related predictions, the only retrieved paper concerns topical corticosteroids, not naphazoline, and angle-closure warnings are a safety concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the three Singapore licenses
- Any direct preclinical or clinical evidence of naphazoline in hair disorders or glaucoma; without it, the prediction should not advance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

