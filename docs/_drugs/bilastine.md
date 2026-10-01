---
layout: default
title: Bilastine
parent: Low Evidence (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Bilastine
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

# Bilastine: From Allergic Conditions (H1 Antihistamine Use) to Duodenal Obstruction

## One-Sentence Summary

Bilastine is a non-sedating H1 antihistamine, used for allergic rhinoconjunctivitis and urticaria.
The TxGNN model predicts it may be effective for **duodenal obstruction**, but there are **0 clinical trials** and **0 publications** supporting this direction, and the pharmacology does not support it either.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records. Published literature describes allergic rhinoconjunctivitis and urticaria. |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 97.73% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Bilastine is described as a selective, peripherally restricted H1-receptor antagonist. Its efficacy in allergic rhinitis and urticaria is well established.

Duodenal obstruction is a mechanical or structural condition, and H1 blockade has no plausible effect on it. The high score (0.977) appears to come from proximity in the knowledge graph, not from pharmacology.

The prediction is therefore best read as a model artifact, not a credible repurposing lead. The same applies to the other gastrointestinal predictions for this drug (duodenal ulcer, gastric ulcer, duodenogastric reflux, duodenitis). Histamine-driven acid secretion works through H2 receptors, not H1.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN17104P | BILAXTEN TABLET 20 MG (PHARMACY ONLY) | Tablet |
| SIN14661P | BILAXTEN TABLET 20 mg | Tablet |
| SIN15963P | BILAXTEN ORAL SOLUTION 2.5MG/ML | Solution |
| SIN15874P | BILAXTEN ORODISPERSIBLE TABLET 10MG | Orally disintegrating tablet |
| SIN16474P | ALIGRIN TABLET 20MG | Tablet |

Approved indication text is not recorded for any of these licences.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanism, trial or publication behind the duodenal obstruction prediction. The score reflects graph proximity only.

**To proceed, the following is needed:**
- Any mechanistic or clinical rationale for H1 antagonism in duodenal obstruction. Without one, the candidate should not advance.
- The HSA package insert (warnings, contraindications and approved indications) and DrugBank mechanism data, both currently missing.

**Better-supported candidates for the same drug (not the primary prediction):**
- **Allergic urticaria** (score 86.4%, L1): a Phase 3 RCT (NCT00421109, n=522) and meta-analyses in chronic urticaria. This largely confirms existing labelled use and is not a new repurposing finding. Proceed with Guardrails.
- **Cold urticaria** (score 90.2%, L2): a completed Phase 2/3 placebo-controlled crossover study (NCT01271075, n=20) and one RCT publication (PMID 23742030). Up-dosing to 40–80 mg is off-label and the sample is small. Proceed with Guardrails.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

