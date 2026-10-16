---
layout: default
title: Trifarotene
parent: Low Evidence (L5)
nav_order: 1023
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Trifarotene: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne"
monitor_inn: "Trifarotene"
predicted_indications: ["zinc, elevated plasma", "pyogenic arthritis-pyoderma gangrenosum-acne syndrome", "demodicidosis of sebaceous gland", "spondyloarthropathy, susceptibility to", "malaria", "Zollinger-Ellison syndrome", "Ehlers-Danlos syndrome", "Beare-Stevenson cutis gyrata syndrome", "isolated congenital adermatoglyphia", "malignant atrophic papulosis"]
---

# Trifarotene
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

# Trifarotene: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Trifarotene is a topical retinoid originally used to treat acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but **no clinical trials and no publications** currently support this direction. The prediction rests on computational network analysis alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (the approved indication text on the Singapore licence is not available; acne is taken from the TxGNN knowledge graph) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology data show that trifarotene is a synthetic retinoid acting on retinoic acid receptors (RAR-α, RAR-β and RAR-γ). Other sources describe it as a selective RAR-γ agonist. It is applied as a 0.005% cream, and its high metabolic instability suggests limited systemic exposure.

For elevated plasma zinc, no plausible mechanistic link could be identified. It is a metabolic or laboratory finding with no known retinoid-receptor pathway. A topical drug with minimal systemic exposure is also unlikely to change plasma zinc levels. The high TxGNN score appears to be a network-based artefact rather than a pharmacologically grounded signal.

Other top-ranked predictions are also weakly supported. The most plausible among them are conditions with a skin or follicular component:
- **PAPA syndrome (rank 2, score 99.32%)**: only the acne manifestation is indirectly related.
- **Demodicidosis of the sebaceous gland (rank 3, score 98.42%)**: shares the pilosebaceous unit with acne, but trifarotene has no antiparasitic activity.

None of the top 10 predictions has clinical trials or literature behind it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication.

(For reference, trifarotene completed Phase 3 trials in acne vulgaris, including the long-term safety study NCT02189629. These concern the original indication, not the predicted one.)

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16571P | AKLIEF CREAM 50mcg/g (Laboratoires GALDERMA) | Cream (topical) | Not listed in the data compiled for this report |

---

## Cytotoxicity

Not applicable (trifarotene is not an antineoplastic drug). Section omitted.

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed with 3 entries. All are pharmacological target relationships (RAR-α, RAR-β, RAR-γ), not drug-drug interactions with clinical severity ratings. Systemic exposure from topical use is expected to be limited.

Please refer to the package insert for warnings and contraindications. The label text could not be retrieved for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for elevated plasma zinc has no supporting trials or literature, and no plausible mechanistic link. Topical administration with low systemic exposure further weakens its plausibility. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Retrieve and review the HSA package insert for warnings and contraindications (a blocking gap for safety screening)
- Obtain detailed mechanism of action data from DrugBank
- Identify any biological rationale linking retinoid receptor signalling to zinc homeostasis, and search for supporting literature
- Assess route compatibility, since the drug is available only as a topical cream
- If a repurposing direction is pursued, consider re-prioritising candidates with a skin or follicular link (e.g., demodicidosis, the acne component of PAPA syndrome). Each would still need its own evidence review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

