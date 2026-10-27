---
layout: default
title: Calcitriol
parent: Low Evidence (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Calcitriol: predicted new indication Vitamin D deficiency (obsolete ontology term) (evidence level L5). Approved use: Hypoparathyroidism, renal osteodystrophy…"
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hereditary hypophosphatemic rickets", "hypophosphatemic rickets", "osteomalacia (disease)", "vitamin D-dependent rickets"]
---

# Calcitriol
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

## Calcitriol: From Hypoparathyroidism and Renal Osteodystrophy to Vitamin D Deficiency
{: .text-alpha }

## One-Sentence Summary

Calcitriol is the active hormonal form of vitamin D. It is used for calcium and phosphate disorders such as hypoparathyroidism and renal osteodystrophy.
The TxGNN model's top-ranked prediction is **vitamin D deficiency**, but the disease term is flagged as obsolete and likely duplicates existing indications.
**No clinical trials and no publications** were retrieved for it, so this prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypoparathyroidism, renal osteodystrophy, hypercalcemia-related and phosphorus metabolism disorders (from the knowledge graph, as the registration records list no indication text) |
| Predicted New Indication | Vitamin D deficiency (obsolete ontology term) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Calcitriol is the active form of vitamin D (1,25-dihydroxyvitamin D3). It acts through the vitamin D receptor to regulate calcium and phosphate balance, so a link to vitamin D deficiency is biologically plausible.

However, the predicted disease term is marked obsolete in the disease ontology and overlaps with conditions calcitriol already treats. The high score therefore mostly reflects the model's network proximity rather than a new therapeutic opportunity. In practice, replacing vitamin D deficiency with an already-activated metabolite is usually not the main use. Calcitriol is generally reserved for situations where activation is impaired, such as kidney disease or hypoparathyroidism.

The data compiled for this report also include stronger-supported candidates, which are summarised in the conclusion below.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN13449P | MEDITROL | Capsule, liquid filled | Mega Lifesciences Public Company Limited |
| SIN12258P | RASPUTIN SOFT CAPSULE 0.25 mcg | Capsule, liquid filled | Young Il Pharm Co Ltd / Hanmi Pharmaceuticals |
| SIN03865P | ROCALTROL CAPSULE 0.25 mcg | Capsule, liquid filled | Catalent Germany Eberbach GmbH / allphamed PHARBIL Arzneimittel GmbH (primary packager) |
| SIN12160P | SILKIS OINTMENT 3 mcg/g | Ointment | Laboratoires Galderma |

All four registrations are valid single-ingredient products (three oral capsules and one topical ointment). No approved indication text is recorded for them.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (graph-derived, not label text): kidney disease, sarcoidosis, hypercalcemia, nephrocalcinosis, nephrolithiasis, phosphorus metabolism disease, hyperphosphatemia, hypervitaminosis, acute urate nephropathy, pyoureter, and arteriosclerosis obliterans.
- **Drug Interactions** (100 interactions recorded; main ones listed):
  - **Major:** cholecalciferol, calcifediol, burosumab
  - **Moderate:**
    - Thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone, bendroflumethiazide, benzthiazide)
    - Anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butabarbital, butalbital)
    - Bile acid sequestrants (cholestyramine, colesevelam, colestipol)
    - Digoxin and digitoxin
    - Aluminum hydroxide
    - Topical calcipotriol

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests only on a model score. It has no trials or literature, and the disease term is obsolete and overlaps with existing indications. It should not drive a repurposing decision on its own.

Other predictions in the same data have meaningful support and could be evaluated as separate candidates:
- **Hereditary hypophosphatemic rickets / hypophosphatemic rickets** (L3, Proceed with Guardrails): an early Phase 1 study of calcitriol monotherapy in X-linked hypophosphatemia (NCT03748966, n=16) and a Phase 4 dosing trial (NCT03820518, n=100, status unknown), plus several reviews and guidelines.
- **Vitamin D-dependent rickets** (L3, Proceed with Guardrails): a strong mechanistic rationale in type 1A and supporting clinical series, but no registered trials.
- **Osteomalacia** (L4, research question) has only indirect, review-level evidence. **Renal tubular acidosis** (L4, Hold) has only physiology studies, case reports and reviews.

**To proceed, the following is needed:**
- Re-anchor the candidate on a non-obsolete disease term, or select one of the stronger-supported indications above as the lead.
- Package insert warnings and contraindications from the HSA, which are currently unavailable.
- Detailed mechanism of action data.
- For rickets indications: a monitoring plan for serum and urinary calcium, PTH, and renal ultrasound (hypercalciuria, nephrocalcinosis, hyperparathyroidism), plus a Phase 3 or comparative study to strengthen the evidence base.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

