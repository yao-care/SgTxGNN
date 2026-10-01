---
layout: default
title: Secukinumab
parent: Low Evidence (L5)
nav_order: 889
evidence_level: L5
indication_count: 10
---

# Secukinumab
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

# Secukinumab: From an Anti-IL-17A Antibody to Primary Release Disorder of Platelets

## One-Sentence Summary

Secukinumab is an anti-IL-17A monoclonal antibody marketed in Singapore as COSENTYX.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this direction.
The score comes from graph-based prediction only, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.16% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the database. Secukinumab is known to be an anti-IL-17A monoclonal antibody, and it is an injectable biologic. The registry entries do not list approved indication text, so the original indication cannot be confirmed from this data.

**The prediction is not mechanistically supported.** No known role of IL-17A has been identified in platelet granule release defects. The high score is most likely a graph-based artefact, for example from shared platelet-related neighbours in the knowledge graph. It should not be read as a signal of real efficacy.

### Other Top Predictions

None of the other top-10 predictions has clinical trial support, and all are at Evidence Level L5.

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Pseudo-von Willebrand disease | 97.74% | Gain-of-function GP1BA defect, unrelated to IL-17A |
| 3 | Glanzmann thrombasthenia | 97.34% | Inherited integrin αIIbβ3 defect, no plausible mechanism |
| 4 | HER2 positive breast carcinoma | 96.48% | IL-17 role in the tumour microenvironment is preclinical and speculative |
| 5 | Drug-induced osteoporosis | 95.27% | IL-17A promotes osteoclastogenesis via RANKL, so blockade is theoretically bone-protective. This is the only candidate flagged as a research question. |
| 6–9 | Breast cancer subtypes (normal breast-like, PR-positive, luminal A/B, PR-negative) | 94.5–95.1% | No evidence-based link. The identical scores for ranks 6 and 7 suggest an ontology artefact. |
| 10 | Fetal and neonatal alloimmune thrombocytopenia | 92.69% | Driven by maternal anti-HPA alloantibodies. Pregnancy and neonatal safety data would be a major barrier. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top prediction.

For rank 8 (breast tumour luminal A or B), 19 publications were retrieved, but all are keyword noise. The search matched terms such as "B cell" and "hepatitis B", and none concerns secukinumab or luminal breast cancer. They provide no support and were not used to upgrade the evidence level.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16359P | COSENTYX Solution for Injection in Pre-filled UnoReady Pen 300mg/2ml | Injection, solution | Novartis Pharma Stein AG |
| SIN14751P | COSENTYX Solution for Injection in Prefilled Syringe 150mg/ml | Injection, solution | Novartis Pharma Stein AG / Novartis Pharmaceutical Manufacturing GmbH |
| SIN14750P | COSENTYX Solution for Injection in Prefilled SensoReady Pen 150mg/ml | Injection, solution | Novartis Pharma Stein AG / Novartis Pharmaceutical Manufacturing GmbH |
| SIN16315P | COSENTYX Solution for Injection in Prefilled Syringe 75mg/0.5ml | Injection, solution | Novartis Pharma Stein AG |

Approved indication text is blank in the registry records, so it is not shown here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials, no relevant literature and no plausible mechanistic link between IL-17A inhibition and platelet granule release defects. The 98.16% score reflects graph-based prediction only, and the evidence remains at L5.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data for secukinumab, to allow a proper mechanistic-link analysis
- Targeted literature and trial searches for secukinumab or IL-17A with platelet function disorders, since the current searches returned nothing relevant
- If the team wants a lead worth exploring, drug-induced osteoporosis (rank 5) has the most plausible biology through IL-17A and RANKL-driven bone resorption, but it would first need a preclinical or observational evidence review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

