---
layout: default
title: Testosterone Propionate
parent: Low Evidence (L5)
nav_order: 963
evidence_level: L5
indication_count: 10
---

# Testosterone Propionate
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

# Testosterone Propionate: From Androgen Therapy to Urethral Obstruction Sequence

## One-Sentence Summary

Testosterone propionate is an androgen (male sex hormone) ester, and no approved indication is recorded in the Singapore registration data.
The TxGNN model predicts it may be effective for **urethral obstruction sequence**, a congenital obstructive uropathy.
This prediction has **0 clinical trials** and **0 publications** behind it, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Urethral obstruction sequence |
| TxGNN Prediction Score | 93.26% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Testosterone propionate is generally understood as an androgen receptor agonist, so its effects would come from androgen signalling.

The link to the predicted indication is weak. Urethral obstruction sequence is a congenital obstruction of the urinary outflow tract, and its treatment is mainly surgical or drainage-based. No clear androgen-mediated mechanism connects the drug to this condition. The high graph score probably reflects proximity to other genitourinary and gonadal disorders in the knowledge graph, not a real therapeutic rationale. Similarity to the original indication has not been assessed, because no original indication is recorded.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04555P | SUSTANON 250 INJECTION | Injection | Not specified in registration data |

The manufacturer is EVER Pharma Jena GmbH. The only available route is injectable.

## Safety Considerations

Please refer to the package insert for safety information. No warnings or contraindications were provided, and the drug-interaction query returned no records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials or literature, and its mechanistic link is weak, since the condition is managed surgically. Safety data are also missing, so the candidate cannot move to safety screening.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indications), which is currently blocking
- Mechanism of action data from DrugBank
- Any supporting trials or literature for urethral obstruction sequence, or a decision to drop this prediction
- Route compatibility assessment (not yet done)

**Other predictions worth noting:**
- **Testicular regression syndrome** (rank 3, score 87.67%, L4, "Research Question") is the only prediction with a plausible rationale. Androgen replacement for the resulting androgen deficiency is mechanistically coherent. The single supporting paper is a 1980 case-level report on anorchia (PMID [6775612](https://pubmed.ncbi.nlm.nih.gov/6775612/)). Its design could not be confirmed, so this is indirect evidence at best.
- **Freemartinism** (rank 5, score 87.26%, L4, "Hold") is supported only by three animal studies (PMIDs [8349280](https://pubmed.ncbi.nlm.nih.gov/8349280/), [658891](https://pubmed.ncbi.nlm.nih.gov/658891/), [2229590](https://pubmed.ncbi.nlm.nih.gov/2229590/)). It is a bovine condition with no human therapeutic target.
- The remaining seven predictions are L5 with no evidence provided, and several look like knowledge-graph artifacts (for example tetragametic chimerism and polysomy of X chromosome).

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

