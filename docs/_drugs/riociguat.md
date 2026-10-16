---
layout: default
title: Riociguat
parent: Low Evidence (L5)
nav_order: 871
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Riociguat: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Pulmonary arterial hypertension"
monitor_inn: "Riociguat"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypertrichosis (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with connective tissue disease", "pulmonary arterial hypertension associated with chronic hemolytic anemia", "pulmonary arterial hypertension associated with HIV infection"]
---

# Riociguat
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

# Riociguat: From Pulmonary Arterial Hypertension to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Riociguat is an oral drug originally used to treat pulmonary arterial hypertension (PAH) and chronic thromboembolic pulmonary hypertension (CTEPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-growth disorder.
This prediction currently has **no supporting clinical trials and no publications**, so it rests on the model's graph-based inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension; chronic thromboembolic pulmonary hypertension |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 94.92% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Riociguat is a soluble guanylate cyclase (sGC) stimulator. It acts on the nitric oxide (NO)–sGC–cGMP pathway, promoting blood vessel relaxation in the lung circulation. Detailed mechanism-of-action data are not available in the compiled data, so this description rests on the drug's known drug class.

For this predicted indication, **no mechanistic link has been established**. Nothing connects NO–sGC–cGMP signalling to the development of a congenital hair-growth disorder. The high score looks like a network-based inference. It may reflect similarity to other hair-related disease nodes in the knowledge graph rather than a biological rationale.

Vasodilators such as minoxidil are known to *cause* hypertrichosis as a side effect. If anything, that points to a safety concern, not a treatment rationale, and no riociguat-specific evidence on this question was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Riociguat is marketed in Singapore as ADEMPAS film-coated tablets (oral), with 5 valid single-ingredient registrations and none cancelled. The manufacturer for all five is Bayer AG, Leverkusen. The approved indication text was not listed for these registrations.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14678P | ADEMPAS Film-Coated Tablet 0.5 mg | Tablet, film coated |
| SIN14679P | ADEMPAS Film-Coated Tablet 1.0 mg | Tablet, film coated |
| SIN14680P | ADEMPAS Film-Coated Tablet 1.5 mg | Tablet, film coated |
| SIN14681P | ADEMPAS Film-Coated Tablet 2.0 mg | Tablet, film coated |
| SIN14682P | ADEMPAS Film-Coated Tablet 2.5 mg | Tablet, film coated |

---

## Safety Considerations

- **Drug Interactions**: 75 interactions were identified. The ones listed here are all moderate-level:
  - Proton pump inhibitors: omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Antacids and minerals: aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, hydroxide and oxide
  - Others: dexamethasone, clarithromycin, papaverine, mannitol
- **Class-related concern**: Vasodilators can cause excessive hair growth, which is relevant to the predicted indication.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). There are no trials or publications, and no plausible biological mechanism links riociguat to this disorder. Vasodilators are associated with hypertrichosis as a side effect, so the direction may even be unfavourable.

**To proceed, the following is needed:**
- A biological rationale linking sGC/cGMP signalling to the pathogenesis of Ambras syndrome, supported by preclinical studies
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the HSA website
- Any case reports or early-phase studies in congenital hypertrichosis

**Note on other predictions from the same analysis:** Two other predicted indications are much better supported and fall within the PAH disease family where riociguat is already used. Both are rated L2 and "Proceed with Guardrails":
- **PAH associated with connective tissue disease** is supported by a PATENT-1 subgroup analysis (PMID 27457511), a systematic review (PMID 38378970) and observational data.
- **PAH associated with congenital heart disease** is supported by a PATENT-1/2 subgroup analysis (PMID 26135803).

Guardrails for both include avoiding PDE5 inhibitor or nitrate combinations, monitoring for hypotension and, in congenital heart disease, careful haemodynamic monitoring. These are better candidates for further evaluation than the top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

