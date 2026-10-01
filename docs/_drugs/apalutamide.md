---
layout: default
title: Apalutamide
parent: Low Evidence (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Apalutamide
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

# Apalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Apalutamide is an oral androgen receptor (AR) antagonist, marketed in Singapore as ERLEADA and used in prostate cancer. The registration record does not list an approved indication, so this is inferred from the literature.
The TxGNN model predicts it may be relevant to **prostate cancer/brain cancer susceptibility**, but this is a genetic susceptibility label rather than a treatable disease.
There are **0 clinical trials** and **0 publications** for this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the registration data (inferred as prostate cancer from the literature) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 98.43% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the record. Apalutamide is an AR antagonist. It blocks androgen binding, nuclear translocation and AR-mediated transcription, and its efficacy in prostate cancer is well documented.

The predicted entry is a genetic susceptibility label, not a disease state that can be treated. The high score (0.984) most likely reflects the link to prostate cancer in the knowledge graph. That link is the drug's existing use, so it is not a new repurposing opportunity. Nothing in the record supports an AR-antagonist mechanism in the brain cancer component.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Related Evidence from Other Predicted Entries

The Evidence Pack holds the substantive evidence under other, lower-ranked predictions. All of it concerns prostate cancer, the existing use, and none tests a new indication.

| Predicted Entry | Evidence Level | Decision | Notes |
|---------|------|------|------|
| Male reproductive organ cancer (rank 8) | L1 | Proceed with Guardrails | Phase 3 trials [NCT02489318](https://clinicaltrials.gov/study/NCT02489318) (TITAN) and [NCT03767244](https://clinicaltrials.gov/study/NCT03767244), plus RCT publications [31150574](https://pubmed.ncbi.nlm.nih.gov/31150574/) (TITAN) and [29420164](https://pubmed.ncbi.nlm.nih.gov/29420164/) (SPARTAN). All are in prostate cancer. Extension to testicular or penile cancer is unsupported. |
| Benign neoplasm of prostate (rank 7) | L4 | Hold | Only indirect prostate cancer evidence, matched by the word "prostate". |
| Benign reproductive system neoplasm (rank 4) | L4 | Hold | Only an observational study in metastatic prostate cancer. |
| Ranks 2, 3, 5, 6, 9, 10 | L5 | Hold | Graph-based prediction only, with no trials or literature. Several are likely knowledge-graph artifacts. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15698P | ERLEADA FILM-COATED TABLET 60MG | Tablet, film coated (oral) | Not provided in the record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (AR antagonist), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a genetic susceptibility label, not a treatable disease, and it has no trials or literature. The strong evidence in the pack (L1) supports the existing prostate cancer use, so it is not evidence for a new indication.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (currently a blocking gap)
- Mechanism of action data from DrugBank
- Confirmation of the approved indication text against the HSA label
- Expert review of whether this susceptibility term maps to a real treatable indication
- Any new-indication evaluation should be re-run on a specific, treatable disease entry rather than this label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

