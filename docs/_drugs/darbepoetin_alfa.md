---
layout: default
title: Darbepoetin Alfa
parent: Low Evidence (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Darbepoetin Alfa: predicted new indication Amenorrhea (evidence level L5). Approved use: Not stated in the Singapore licence records available"
monitor_inn: "Darbepoetin alfa"
predicted_indications: ["amenorrhea (disease)", "renin-angiotensin-aldosterone system-blocker-induced angioedema", "anaphylaxis", "psoriasis", "penile fibromatosis", "food-dependent exercise-induced anaphylaxis", "Peyronie disease", "Ledderhose disease", "infantile digital fibromatosis", "HER2 positive breast carcinoma"]
---

# Darbepoetin Alfa
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

## Darbepoetin alfa: From Anaemia (Erythropoiesis Stimulation) to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Darbepoetin alfa is a long-acting erythropoiesis-stimulating agent (an erythropoietin receptor agonist) that is marketed in Singapore as an injectable. The TxGNN model predicts it may be effective for **amenorrhea**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records available |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 96.73% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, darbepoetin alfa is an erythropoiesis-stimulating agent that acts on the erythropoietin receptor to increase red blood cell production. Its established use is in anaemia, but the approved indication text is missing from the Singapore records.

The link to amenorrhea is indirect at best. One speculative route is that correcting anaemia in chronic disease might ease disruption of the hypothalamic-pituitary-gonadal axis. No data support this. The high TxGNN score (0.967) reflects network-based similarity, not clinical findings.

Other top predictions show the same pattern. They include renin-angiotensin-aldosterone system-blocker-induced angioedema, anaphylaxis, psoriasis, several fibromatoses (penile fibromatosis, Peyronie disease, Ledderhose disease, infantile digital fibromatosis) and HER2-positive breast carcinoma. All are evidence level L5 with no supporting trials. Several are mechanistically implausible, and the review of these predictions raises specific safety concerns:
- Darbepoetin can itself cause hypersensitivity reactions, so its use in anaphylaxis conditions is unsupported.
- Erythropoiesis-stimulating agents carry warnings of increased tumour progression and shortened survival in cancer patients, which argues against any anticancer repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for amenorrhea.

Across all ten top predictions, the only paper retrieved was a 2025 case report on deucravacitinib in psoriasis with myelodysplastic syndrome ([PMID 40519492](https://pubmed.ncbi.nlm.nih.gov/40519492/), Cureus). It does not study darbepoetin alfa and offers no meaningful support.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14739P | NESP Injection Plastic Syringe 10 μg/0.5 ml | Injection, solution, concentrate | Not available |
| SIN14740P | NESP Injection Plastic Syringe 20 μg/0.5 ml | Injection, solution, concentrate | Not available |
| SIN14741P | NESP Injection Plastic Syringe 30 μg/0.5 ml | Injection, solution, concentrate | Not available |
| SIN14742P | NESP Injection Plastic Syringe 40 μg/0.5 ml | Injection, solution, concentrate | Not available |
| SIN14743P | NESP Injection Plastic Syringe 60 μg/0.5 ml | Injection, solution, concentrate | Not available |

All seven licences (the two remaining strengths are 120 μg and 180 μg) are valid single-ingredient products made by Terumo Corporation (Kofu Factory).

## Safety Considerations

- **Contraindication signals from the knowledge graph**: Hypertensive disorder and hypertension appear as drug-disease contraindication edges. These come from a knowledge graph, not from label text, and should be checked against the package insert.
- **Drug Interactions**: 17 interactions were identified.
  - **Major (4)**: carfilzomib, lenalidomide, pomalidomide, thalidomide.
  - **Moderate (3)**: cyclosporine, human C1-esterase inhibitor, conestat alfa.
  - **Minor (10)**: ACE inhibitors (fosinopril, benazepril, captopril, enalapril, lisinopril, moexipril, perindopril, quinapril, ramipril, trandolapril).

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for amenorrhea is supported only by a network-based score. There are no trials or relevant publications, and the mechanistic link is speculative. The safety profile of erythropoiesis-stimulating agents (hypertension, thrombotic risk, tumour-progression concerns) adds caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, and the approved indication text for the Singapore licences
- Detailed mechanism of action data (e.g. from DrugBank)
- A literature and trial search specific to darbepoetin or erythropoietin in amenorrhea, including hypothalamic-pituitary-gonadal effects in chronic kidney disease
- A safety assessment covering hypertension, thrombosis and hypersensitivity in the target population
- Assessment of the same evidence gaps for the other top-ranked predictions before any is prioritised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

