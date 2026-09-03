---
layout: default
title: Venetoclax
parent: 僅模型預測 (L5)
nav_order: 1051
evidence_level: L5
indication_count: 10
---

# Venetoclax
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Venetoclax: From Unregistered Status in Singapore to Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma (IGHV-Mutated Subtype)

## One-Sentence Summary

Venetoclax is a BCL-2 inhibitor that is currently **not marketed in Singapore** (0 registrations), and no original-indication data is available in this evidence pack.
The TxGNN model's top-ranked prediction is **Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma (CLL/SLL) with IGHV somatic hypermutation**,
but for this specific ontology term there are currently **0 clinical trials** and **0 publications** — the prediction is supported only by general mechanistic reasoning, not by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not registered in Singapore and no original indication data was provided |
| Predicted New Indication | Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 (0 clinical trials, 0 literature for this specific term — model prediction only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap, DG002). Based on known pharmacological information, Venetoclax is a BH3-mimetic that selectively inhibits BCL-2, a pro-survival protein overexpressed in CLL/SLL tumor cells; by blocking BCL-2, Venetoclax restores the intrinsic apoptotic pathway and induces tumor cell death. This mechanism is the basis of Venetoclax's globally established, FDA-approved use as a standard therapy (alone or with anti-CD20 antibodies) for CLL/SLL.

The specific ontology term predicted here — CLL/SLL with IGHV somatic hypermutation — refers to a prognostic subtype rather than a distinct disease. IGHV mutation status stratifies CLL patients into better- (mutated) vs. worse-prognosis (unmutated) groups, but it does not change the core BCL-2 dependency that makes CLL/SLL broadly responsive to Venetoclax. The complete absence of trials/literature tied to this exact term is therefore best interpreted as an **ontology granularity gap in the evidence search**, not as evidence against the mechanism — the drug's own related evidence pack entries (e.g., rank 2, "pre-germinal center CLL/SLL," rank 4 "myeloid leukemia") show that Venetoclax has substantial, well-established evidence in the broader CLL/SLL and hematologic malignancy space.

**Recommended follow-up**: re-run evidence collection using the broader term "chronic lymphocytic leukemia" (rather than the IGHV-mutation-qualified subtype) to surface the pivotal trials (e.g., MURANO, CLL14) that actually support this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific ontology term.

---

## Literature Evidence

Currently no related literature available for this specific ontology term.

*(Note: the closely related entry "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma" in the same evidence pack cites one review, PMID [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/), on BCR structure/IGHV subsets in CLL — background context only, not direct efficacy evidence for Venetoclax.)*

---

## Singapore Market Information

Venetoclax has **no registered license in Singapore** (`total_licenses: 0`, `market_status: 未上市/Not Marketed`). No product/dosage-form/indication data is available to tabulate.

---

## Cytotoxicity

Venetoclax is an antineoplastic agent (targeted BCL-2 inhibitor used in hematologic malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BH3-mimetic / selective BCL-2 inhibitor) |
| Myelosuppression Risk | High — neutropenia and thrombocytopenia are commonly reported, particularly in combination regimens (e.g., thrombocytopenia 80%, fatigue 60% in bendamustine-rituximab-ibrutinib combinations); tumour lysis syndrome and myelosuppression are the most frequently encountered toxicities across venetoclax-based regimens |
| Emetogenicity Classification | Low to moderate (oral targeted agent) |
| Monitoring Items | CBC with differential, renal function, electrolytes and uric acid (tumour lysis syndrome risk during dose ramp-up), liver function |
| Handling Protection | Must follow cytotoxic/antineoplastic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/local package-insert warnings and contraindications are flagged as a Blocking data gap, DG001 — this must be resolved before any Stage 1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's #1-ranked prediction for Venetoclax, "CLL/SLL with IGHV somatic hypermutation," currently has zero directly matched clinical trials or publications, and the drug itself is not registered in Singapore. While the underlying BCL-2 mechanism is well established for CLL/SLL broadly (and even more strongly for AML — see rank 4 in the underlying prediction set, which carries L2 evidence with a "Proceed with Guardrails" recommendation), this specific granular ontology term lacks the direct evidence needed to move past a research question stage.

**To proceed, the following is needed:**
- TFDA/local regulatory label (warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal mechanism-of-action documentation (DG002)
- Re-run evidence search using the broader "chronic lymphocytic leukemia" term to capture pivotal trials (e.g., MURANO) already known to support this drug class in CLL/SLL
- If pursuing repurposing in Singapore, evaluate whether the better-evidenced predicted indications in this dataset (myeloid leukemia/AML, follicular lymphoma) represent a more actionable entry point, given their stronger L2-level trial support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

