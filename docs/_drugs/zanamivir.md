---
layout: default
title: Zanamivir
parent: Low Evidence (L5)
nav_order: 1071
evidence_level: L5
indication_count: 10
---

# Zanamivir
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Zanamivir is a viral neuraminidase inhibitor, and its only Singapore registration is an inhaled powder (Relenza Rotadisk). The registration record does not list an approved indication. The TxGNN model predicts it may be effective for **pyelonephritis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the registration record (zanamivir is a viral neuraminidase inhibitor, i.e. an anti-influenza antiviral) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Zanamivir is known as a neuraminidase inhibitor that acts on influenza viruses, and it is not an antibacterial agent.

The link to the predicted indication is weak. Pyelonephritis is usually a bacterial infection of the kidney, and zanamivir has no expected antibacterial activity. The high TxGNN score (0.998) reflects an association in the knowledge graph, not evidence from trials or literature. This prediction should be treated as a graph artifact until independent data show otherwise.

The other top-ranked predictions are also unsupported: tyrosine and phenylalanine metabolism disorders, Pierre Robin syndrome, and several "susceptibility to infection" entries such as Legionnaire disease, dengue, aspergillosis and schistosomiasis. All are rated L5 with a Hold recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11199P | RELENZA ROTADISK 5 mg/dose | Powder, metered | Not listed in the record |

The manufacturer is Glaxo Wellcome Production / GlaxoSmithKline Australia Pty Ltd. Only an inhaled-powder form is registered, so there is no route-compatibility data for a systemic infection such as pyelonephritis.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no trials or publications for pyelonephritis, and there is no plausible mechanism for a viral neuraminidase inhibitor in a bacterial kidney infection. The only registered form is an inhaled powder, and no safety information is available.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is currently blocking safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence of activity in urinary tract or kidney infection
- An assessment of whether a systemic route of administration would be feasible, given that only an inhaled form is registered in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

