---
layout: default
title: Penicillamine
parent: Low Evidence (L5)
nav_order: 766
evidence_level: L5
indication_count: 10
---

# Penicillamine
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

# Penicillamine: From Established Chelation Uses to Megaloblastic Anemia

## One-Sentence Summary

Penicillamine is a copper and cystine chelator marketed in Singapore as an oral capsule (Cupripen). The TxGNN model predicts it may be effective for **megaloblastic anemia**, but **no clinical trials and no publications** support this prediction, and the mechanism argues against it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence record |
| Predicted New Indication | Megaloblastic anemia |
| TxGNN Prediction Score | 98.02% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, penicillamine is a copper and cystine chelator. Its established uses are in copper-overload and cystine-related conditions, and the same evidence pack shows it as a comparator in Wilson disease trials.

The prediction is **not mechanistically convincing**. Megaloblastic anemia is driven mainly by vitamin B12 or folate deficiency, which chelation does not address. Penicillamine's labelled haematological toxicities include bone marrow suppression, aplastic anemia and thrombocytopenia, and they argue against its use in an anemia. The high score (98.02%) most likely reflects graph-topology artefacts rather than a real biological link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08173P | CUPRIPEN 250 CAPSULE 250 mg (Laboratorios Rubio SA) | Capsule (oral) | Not stated in the licence record |

## Safety Considerations

- **Key Warnings**: Penicillamine has labelled haematological toxicities: bone marrow suppression, aplastic anemia and thrombocytopenia. These are directly relevant to any anemia indication.
- **Drug Interactions**: No interaction records were found in the query.

For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no trials or literature. Penicillamine's chelating mechanism does not fit a B12/folate-deficiency anemia, and its known marrow toxicity is a safety signal against this use.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indications), which is currently a blocking gap
- Mechanism of action data from DrugBank
- Any mechanistic or clinical evidence that penicillamine benefits megaloblastic anemia; none was found

**Other predicted indications in this pack:**
- The "disease of transporter activity" prediction (score 93.0%) has L1 evidence. It maps to Wilson disease and cystinuria, which are established penicillamine uses rather than novel repurposing. It includes the CHELATE Phase 3 RCT (PMID 36183738), which used penicillamine as the active comparator. It would need mapping to specific diseases before any recommendation.
- The "tricarboxylic acid cycle disorder" prediction (score 93.5%) is a hypothesis-generating research question only. Its support is indirect, from cuproptosis literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

