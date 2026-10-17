---
layout: default
title: Chlorambucil
parent: Low Evidence (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Chlorambucil: predicted new indication CLL/SLL with immunoglobulin heavy chain variable-region gene somatic… (evidence level L5). Approved use: Hodgkin lymphoma, follicular lymphoma, mature B-cell ne…"
monitor_inn: "Chlorambucil"
predicted_indications: ["chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma", "lymphoid neoplasm", "upper aerodigestive tract neoplasm"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Chlorambucil: From Hodgkin Lymphoma and Other Lymphoid Malignancies to CLL/SLL with Somatic Hypermutation of the IGHV Gene

## One-Sentence Summary

Chlorambucil is an oral alkylating chemotherapy drug, originally used for Hodgkin lymphoma, follicular lymphoma, acute lymphoblastic leukaemia and related B-cell cancers.
The TxGNN model predicts it may be effective for **chronic lymphocytic leukaemia/small lymphocytic lymphoma (CLL/SLL) with IGHV somatic hypermutation**.
Currently there are **no clinical trials and no publications** specific to this subtype, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma, follicular lymphoma, mature B-cell neoplasms, acute lymphoblastic leukaemia, Richter syndrome (from the knowledge graph; the Singapore licence record contains no indication text) |
| Predicted New Indication | CLL/SLL with immunoglobulin heavy chain variable-region gene somatic hypermutation (IGHV-mutated) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Chlorambucil is known to be a DNA alkylating agent. It cross-links DNA and induces apoptosis in malignant lymphoid cells. Its efficacy in B-cell malignancies is established, and mechanistically it may be applicable to this CLL/SLL subtype.

The predicted indication is a molecular subtype of CLL/SLL, a disease for which chlorambucil is already widely used. The link is therefore plausible, but this is subtype stratification of an existing use rather than true repurposing. The very high TxGNN score most likely reflects how close this entry sits to CLL in the disease ontology. It is not independent evidence of benefit in this subtype.

Newer targeted agents (BTK and BCL2 inhibitors) are now generally preferred over chlorambucil in CLL, which limits the practical value of this direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific subtype.

---

## Literature Evidence

Currently no related literature available for this specific subtype.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11696P | LEUKERAN TABLET 2 mg (Revised Formula) (Excella GmbH & Co. KG) | Film-coated tablet (oral) | Not stated in the licence record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (neutropenia, thrombocytopenia, leukopenia and anaemia are all flagged in the knowledge graph) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for detailed requirements.

---

## Safety Considerations

- **Disease-level cautions from the knowledge graph (not label text):** The knowledge graph links chlorambucil to cautions or contraindications in the following areas.
  - Blood and marrow: thrombocytopenia, neutropenia, agranulocytosis, leukopenia, lymphopenia, anaemia, acute leukaemia.
  - Lung: interstitial lung disease, pulmonary fibrosis.
  - Liver: drug-induced liver injury.
  - Kidney: nephrotic syndrome.
  - Nervous system: epilepsy.
- **Drug Interactions:** 100 interactions were recorded.
  - Major: deferiprone and samarium-153 lexidronam.
  - Moderate: amphotericin B (including lipid, cholesteryl sulfate and liposomal forms), palifermin, strontium-89 chloride, mercaptopurine, roflumilast and chloramphenicol.
  - Several others (for example warfarin, prednisone, omeprazole) are of unknown severity.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is plausible because chlorambucil is already used in CLL, but no trial or publication specific to the IGHV-mutated subtype was found, and the high score is largely ontology proximity. The practical clinical value is also limited, as targeted agents are now preferred in CLL.

Other predicted indications in the same analysis have stronger support and may be better candidates for review:
- Lymphoid neoplasm (L1): many completed Phase 3 trials, plus the IELSG-19 trial in MALT lymphoma. It is largely confirmatory of existing uses.
- Primary pulmonary lymphoma (L3): mainly case series and retrospective cohorts, with one older Phase II study in mixed haematological malignancies.

**To proceed, the following is needed:**
- Subtype-specific efficacy data (IGHV-mutated CLL/SLL) from trials or retrospective analyses
- Package insert warnings and contraindications from the HSA record
- Mechanism of action data, for example from DrugBank
- Comparison against current standard therapy (BTK and BCL2 inhibitors) to define any remaining niche
- A safety monitoring plan covering myelosuppression, secondary malignancy and teratogenicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

