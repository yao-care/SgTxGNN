---
layout: default
title: Carbinoxamine
parent: Low Evidence (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Carbinoxamine
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

# Carbinoxamine: From Antihistamine Use to Allergic Urticaria

## One-Sentence Summary

Carbinoxamine is a first-generation H1-receptor antagonist (antihistamine). The Singapore registration record does not list an approved indication.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **0 clinical trials** and **0 publications** supporting this in the dataset.
The prediction is model-based only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. Based on known information, carbinoxamine is a first-generation H1-receptor antagonist. Its antihistamine class is the standard therapy class for allergic conditions, so it may be mechanistically applicable to allergic urticaria.

In allergic urticaria, mast cells release histamine, which causes wheals and flares. Blocking the H1 receptor directly targets this step. The original indication field is empty, so the link between the original and new indications cannot be assessed. Allergic urticaria may already fall under the drug's existing labelling, which would make it a labelling overlap rather than true repurposing. This cannot be confirmed from the data provided.

The very high TxGNN score (0.9999) most likely reflects the drug-class relationship. It is not evidence for carbinoxamine itself.

The model also predicted nine other indications, with scores from 93.2% to 99.96%. Cold urticaria (99.96%) is the next most plausible, again as a class-level inference. Others include pharyngitis, atopic dermatitis and headache disorder. These have weak or no mechanistic links, and several are non-specific terms that are likely knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07964P | BECAME TABLET | Tablet (oral) | Not stated in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a plausible drug-class mechanism, but no carbinoxamine-specific trial or publication supports it. The package insert safety data is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is a blocking gap
- Carbinoxamine's mechanism of action data, for example from the DrugBank API
- Confirmation of the original approved indication, to rule out a labelling overlap with allergic urticaria
- Carbinoxamine-specific clinical evidence in allergic urticaria
- A comparison against second-generation antihistamines, which are generally preferred over sedating first-generation agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

