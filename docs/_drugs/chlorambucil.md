---
layout: default
title: Chlorambucil
parent: Low Evidence (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Chlorambucil
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

# Chlorambucil: From Registered Antineoplastic Use to CLL/SLL with IGHV Somatic Hypermutation

## One-Sentence Summary

Chlorambucil is an oral alkylating chemotherapy drug that is registered and marketed in Singapore. The registration data supplied do not state its approved indication.
The TxGNN model predicts it may be effective for **chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) with immunoglobulin heavy chain variable-region gene somatic hypermutation**.
**No clinical trials and no publications** specific to this subtype are currently available, so the prediction rests on model output and mechanism alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated (the Singapore license has no approved indication text) |
| Predicted New Indication | CLL/SLL with immunoglobulin heavy chain variable-region gene somatic hypermutation |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the DrugBank input. From the evidence review, chlorambucil is a DNA-crosslinking alkylating agent that is cytotoxic to lymphocytes.

The predicted indication is a molecular subtype of CLL/SLL, a lymphoid malignancy, so the mechanism is plausible. However, the package contains no trial or literature evidence specific to the IGHV-mutated subtype.

Broader CLL evidence is captured under a separate prediction, "lymphoid neoplasm". It is summarised in the conclusion below.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11696P | LEUKERAN TABLET 2 mg (Revised Formula) | Film-coated tablet (oral) | Not stated in the registry data |

Manufacturer: Excella GmbH & Co. KG.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-crosslinking alkylating agent) |
| Myelosuppression Risk | Flagged as a key guardrail in the evidence review; please refer to the package insert warnings and precautions for grading |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC with differential); please refer to the package insert for other monitoring |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

The evidence review also notes secondary malignancy risk after alkylator therapy as a general consideration for chlorambucil.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.72%), but there is no clinical trial or publication specific to the IGHV-mutated CLL/SLL subtype (L5, stage S0). Package insert safety data are also missing, and this blocks safety screening.

For context, the broader prediction **"lymphoid neoplasm"** (rank 9) has much stronger support. It carries Level L1 evidence and a "Proceed with Guardrails" recommendation. The evidence there includes multiple Phase 3 CLL trials in which chlorambucil is a backbone or comparator (e.g., NCT03462719, NCT01678430) and the randomized IELSG-19 trial in MALT lymphoma (PMID 28355112). That is effectively an established use rather than a novel repurposing. Any further work would likely be better anchored on that indication.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indication), which is a blocking data gap.
- Mechanism-of-action data from DrugBank.
- Subtype-specific evidence for IGHV-mutated CLL/SLL, for example a targeted search of CLL trials that report IGHV status.
- Positioning against current targeted therapies, since chlorambucil is best suited to older or less-fit patients.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

