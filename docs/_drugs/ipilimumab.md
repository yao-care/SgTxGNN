---
layout: default
title: Ipilimumab
parent: Low Evidence (L5)
nav_order: 541
evidence_level: L5
indication_count: 10
---

# Ipilimumab
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

# Ipilimumab: From Melanoma to Choroideremia

## One-Sentence Summary

Ipilimumab is an anti-CTLA-4 antibody used in cancer immunotherapy, principally for melanoma.
The TxGNN model predicts it may be effective for **choroideremia**, an inherited retinal degeneration.
**No clinical trials** and **no publications** currently support this direction, and the mechanistic review found no plausible link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma (from the candidate's mechanistic notes; the Singapore licence record contains no indication text) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on known information, ipilimumab blocks CTLA-4, a checkpoint on T cells, and so releases anti-tumour T-cell priming and expansion. That mechanism underlies its proven efficacy in melanoma.

That mechanism does not carry over to choroideremia. Choroideremia is an X-linked retinal degeneration caused by loss of the CHM/REP1 gene. It is not driven by tumour immune escape, so CTLA-4 blockade has no clear rationale.

The very high TxGNN score is most likely an artefact of the knowledge graph. Ipilimumab sits close to melanoma nodes, including eye-related melanoma nodes, and this proximity probably inflated the prediction. The score should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14598P | YERVOY INJECTION CONCENTRATE 5MG/ML | Injection, solution, concentrate | Not listed in the record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Low; toxicity is mainly immune-mediated rather than direct marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC, liver and renal function, thyroid and adrenal function, and signs of immune-related adverse events (colitis, dermatitis, hepatitis, endocrinopathies) |
| Handling Protection | Please refer to the package insert and institutional policy for handling of antineoplastic biologics |

## Safety Considerations

- **Ocular immune-related adverse events**: These are a specific concern for any retinal or eye-related use, because ipilimumab can cause immune-mediated inflammation in ocular tissue.

Please refer to the package insert for other safety information, including warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (evidence level L5). There are no trials or publications, and the mechanistic review found no plausible link between CTLA-4 blockade and CHM/REP1-driven retinal degeneration. Immune-related ocular toxicity adds a safety concern.

**To proceed, the following is needed:**
- A credible biological rationale linking CTLA-4 blockade to choroideremia, or preclinical evidence
- The HSA package insert warnings and contraindications
- Mechanism of action data (MOA) from DrugBank
- Attention to the melanoma-subtype predictions in this pack (non-cutaneous and acral lentiginous melanoma, both L2), which have far stronger evidence and are better candidates for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

