---
layout: default
title: Tremelimumab
parent: Low Evidence (L5)
nav_order: 1007
evidence_level: L5
indication_count: 10
---

# Tremelimumab
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

# Tremelimumab: From Oncology (Original Indication Not Recorded) to Diabetic Cataract

## One-Sentence Summary

Tremelimumab is a CTLA-4-blocking monoclonal antibody (a T-cell checkpoint inhibitor) used in oncology, but the Evidence Pack does not record its approved indication.
The TxGNN model predicts it may be effective for **diabetic cataract**, along with nine other eye conditions, mostly cataract subtypes.
There are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (described as an oncology drug) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, tremelimumab is a CTLA-4-blocking antibody. It releases the brake on T-cell activation and is used in cancer treatment.

**The prediction is not mechanistically supported.** Lens opacity in diabetes is driven by polyol pathway activity, oxidative stress and glycation, and CTLA-4 blockade does not act on any of these. The score is probably a graph artefact. Eight of the ten predictions are cataract subtypes with identical or near-identical scores (0.984–0.985), which points to a shared disease-class signal in the knowledge graph rather than drug-specific biology.

The tenth prediction, diabetic retinopathy (score 98.19%), has only a weak, speculative link through inflammation. Boosting T-cell activity could worsen ocular inflammation, and checkpoint inhibitors are known to cause ocular immune-related adverse events such as uveitis. For these indications, a safety signal is more plausible than a benefit.

Other predicted indications, all with no trial or literature support:

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Immature cataract | 98.41% |
| 3 | Mature cataract | 98.41% |
| 4 | Tetanic cataract | 98.41% |
| 5 | Craniostenosis cataract | 98.41% |
| 6 | Type 2 diabetes-associated cataract | 98.41% |
| 7 | Cortical cataract | 98.39% |
| 8 | Nuclear senile cataract | 98.39% |
| 9 | Senile cataract | 98.33% |
| 10 | Diabetic retinopathy | 98.19% |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16845P | IMJUDO Concentrate for Solution for Infusion 20mg/ml | Infusion, solution concentrate |

The manufacturer is Vetter Pharma-Fertigung GmbH & Co. KG. The only available route is injectable. The registration's approved indication text is not provided in the data.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (CTLA-4 checkpoint inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Ocular safety signal**: Checkpoint inhibitors are associated with ocular immune-related adverse events such as uveitis. This is a particular concern for any eye-related use.
- **Drug Interactions**: The interaction query returned no records. This is not evidence that none exist.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials or literature, and no plausible mechanistic link between CTLA-4 blockade and cataract. A systemic immunotherapy with immune-related adverse event risk is also a poor benefit-risk fit for a condition routinely corrected by surgery.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The approved indication text for the Singapore registration
- Any preclinical or clinical evidence linking CTLA-4 modulation to lens or retinal disease
- A review of ocular immune-related adverse event data for checkpoint inhibitors

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

