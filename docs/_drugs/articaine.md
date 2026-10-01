---
layout: default
title: Articaine
parent: Low Evidence (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Articaine
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

# Articaine: From Local Anaesthesia to Gout

## One-Sentence Summary

Articaine is an amide local anaesthetic, marketed in Singapore as dental injection products (the registered indication text is not available in the data).
The TxGNN model predicts it may be effective for **Gout**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anaesthesia (inferred from drug class; registered indication text is not available) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the source record. Based on its drug class, articaine blocks voltage-gated sodium channels, which stops nerve conduction and produces local anaesthesia.

Gout is driven by urate crystal deposition and the resulting inflammation. Nothing in sodium-channel blockade connects to urate metabolism or gouty inflammation. The 99.58% score is a knowledge-graph prediction (rank 5775) and should not be read as evidence of benefit. The same is true of the other nine candidates: none has a plausible mechanism or supporting clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Candidates (for Context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|------|
| 1 | Gout | 99.58% | L5 | Hold |
| 2 | Exostosis | 99.42% | L5 | Hold |
| 3 | Allergic asthma | 99.38% | L5 | Hold |
| 4 | Intrinsic asthma | 99.34% | L5 | Hold |
| 5 | Exostoses, multiple | 98.90% | L5 | Hold |
| 6 | Hypotrichosis simplex of the scalp | 98.62% | L5 | Hold |
| 7 | Alopecia | 98.58% | L5 | Hold |
| 8 | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 98.49% | L5 | Hold |
| 9 | Brain small vessel disease 1 with or without ocular anomalies | 98.48% | L5 | Hold |
| 10 | Congenital hypotrichosis milia | 98.44% | L5 | Hold |

Two of these candidates had literature retrieved, and neither is evidence of benefit:
- **Allergic asthma:** The three papers concern hypersensitivity to local anaesthetics (paediatric diagnostic testing, dental allergy, prilocaine compartment allergy). They raise a caution for atopic patients rather than support efficacy.
- **Brain small vessel disease:** The papers cover congenital ocular anomalies and do not mention articaine or local anaesthetics. They appear to be matched on disease terms only.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN05504P | UBISTESIN INJECTION | Injection | 3M Deutschland GmbH |
| SIN05505P | UBISTESIN FORTE INJECTION | Injection | 3M Deutschland GmbH |
| SIN12648P | CITOCARTIN 100 INJECTION 1.7 ml/cartridge | Injection | Laboratorios Normon, S.A. |
| SIN15913P | ARTINIBSA 4% WITH EPINEPHRINE SOLUTION FOR INJECTION 1:100000 | Injection, solution | Laboratorios Inibsa, S.A. |
| SIN14537P | Posicaine-100 Injection | Injection, solution | Novocol Pharmaceutical of Canada Inc. |

All five products are injectable only. Approved indication text is not recorded for any of them.

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.
- **Hypersensitivity**: The allergy literature retrieved for the asthma candidates indicates local anaesthetic hypersensitivity reactions are a recognised concern, so caution applies in atopic patients.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions are L5, model-only, with no clinical trials and no drug-specific literature. For the top candidate, gout, there is no plausible mechanistic link. Articaine's route (injectable, local) is also not compatible with the systemic use gout would require, though route compatibility has not yet been assessed.

**To proceed, the following is needed:**
- HSA package insert (warnings and contraindications), which is required before any safety screening
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- The registered indication text for the Singapore licences
- A drug-specific literature and trial search for articaine in gout, since none has been retrieved
- Route-compatibility assessment for any candidate indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

