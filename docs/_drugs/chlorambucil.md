---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Chlorambucil
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

# Chlorambucil: From Lymphoid Malignancies to CLL/SLL with IGHV Somatic Hypermutation

## One-Sentence Summary

Chlorambucil is a classic nitrogen mustard alkylating agent with a long history of use in lymphoid malignancies including chronic lymphocytic leukemia (CLL), though no formal Singapore market registration is recorded in the current dataset.
The TxGNN model predicts it may be effective for the specific molecular subtype **CLL/SLL with IGHV Somatic Hypermutation** (mutated-IGHV CLL), with a prediction score of **99.72%**.
While **no clinical trials or literature** are available for this precise molecular subtype in the current evidence pack, the broader lymphoid neoplasm category (Rank 9) is supported by **over 10 completed Phase 3 RCTs** and a rich literature base, reaching **Evidence Level L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; historically used internationally for CLL and lymphoid malignancies |
| Predicted New Indication | CLL/SLL with IGHV Somatic Hypermutation (mutated-IGHV subtype) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L4 (for this specific molecular subtype; broader CLL/lymphoid neoplasm evidence reaches L1) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the current dataset (DG002). Based on well-established pharmacological knowledge, Chlorambucil belongs to the nitrogen mustard class of bifunctional alkylating agents. It exerts cytotoxic activity by forming DNA interstrand cross-links, disrupting DNA replication and transcription, and ultimately triggering apoptosis. This mechanism has proven particularly effective against slowly proliferating B-cell malignancies — precisely the biological niche occupied by CLL/SLL.

The predicted indication represents an important biological subdivision within CLL. **Mutated-IGHV CLL** (post-germinal center B cells that have undergone somatic hypermutation) is generally associated with a more favorable prognosis compared to unmutated-IGHV CLL. Historically, mutated-IGHV CLL cells show greater susceptibility to DNA-damaging alkylating agents because they are less dependent on BCR signaling survival pathways. This mechanistic alignment directly supports why TxGNN flags this subtype as a high-probability candidate for chlorambucil activity.

Although no trial data specifically targeting the mutated-IGHV subtype with chlorambucil appears in the current dataset, multiple landmark Phase 3 trials across the broader CLL/SLL population — including RESONATE-2 (ibrutinib vs. chlorambucil), CLL11 (obinutuzumab plus chlorambucil vs. rituximab plus chlorambucil), and the IELSG-19 trial in MALT lymphoma — have established chlorambucil as the historical standard comparator for first-line therapy in treatment-naïve patients. The TxGNN prediction is therefore mechanistically coherent and supported by a rich indirect evidence base from closely related disease entities.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for CLL/SLL with IGHV Somatic Hypermutation specifically.

> **Context**: Dedicated trials for this molecular subtype do not exist in the current evidence pack. However, the broader **Lymphoid Neoplasm** category (Rank 9 in this report) encompasses over 30 registered trials where chlorambucil serves as a primary treatment arm or active comparator, including multiple completed Phase 3 RCTs directly relevant to CLL/SLL biology. Retrospective subgroup analysis of those trials stratified by IGHV mutation status would constitute the most efficient path to evidence generation for this specific subtype.

---

## Literature Evidence

Currently no related literature available for CLL/SLL with IGHV Somatic Hypermutation specifically.

> **Context**: Relevant supportive literature is captured under the **Lymphoid Neoplasm** category (Rank 9), including IELSG-19 (PMID [28355112](https://pubmed.ncbi.nlm.nih.gov/28355112/)), a Phase 3 RCT establishing chlorambucil ± rituximab efficacy in MALT lymphoma; IELSG38 (PMID [38385243](https://pubmed.ncbi.nlm.nih.gov/38385243/), 2024), confirming front-line chlorambucil-based therapy in extranodal marginal zone lymphoma; and PMID [36672456](https://pubmed.ncbi.nlm.nih.gov/36672456/) reporting 5-year outcomes of ibrutinib versus chlorambucil from the RESONATE-2 Phase 3 study.

---

## Singapore Market Information

Chlorambucil currently has **no registration** with the Singapore Health Sciences Authority (HSA). No licensed products, approved indications, or authorised dosage forms are recorded in the current dataset.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No registered products found |

---

## Cytotoxicity

Chlorambucil is a conventional cytotoxic alkylating agent (nitrogen mustard class) used in the treatment of lymphoid malignancies; this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard alkylating agent |
| Myelosuppression Risk | High — dose-dependent bone marrow suppression (neutropenia, thrombocytopenia, anaemia) is the primary dose-limiting toxicity; cumulative doses increase risk of prolonged cytopenias |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (before each cycle and periodically during treatment), hepatic function, renal function, neurological status (CNS toxicity reported at high pulse doses) |
| Handling Protection | Must be handled in accordance with cytotoxic drug handling regulations; preparation should occur in a biological safety cabinet with appropriate personal protective equipment |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Chlorambucil has a well-established mechanistic basis for activity in CLL/SLL broadly, and the mutated-IGHV molecular subtype is historically the population most likely to respond favorably to alkylating agents. The TxGNN prediction is biologically coherent, and L1-level evidence exists for the parent CLL/lymphoid neoplasm category. However, direct evidence specific to this molecular subtype remains at Level L4 within this evidence pack, and Singapore does not currently have a registered product.

**To proceed, the following is needed:**

- **IGHV subgroup analysis**: Conduct retrospective subgroup analysis of completed Phase 3 CLL trials (e.g., RESONATE-2 NCT01722487, CLL11 NCT01010061) stratified by IGHV mutation status to confirm differential efficacy of chlorambucil in mutated-IGHV patients
- **Singapore regulatory assessment**: Resolve the Blocking data gap (DG001) by reviewing HSA or international package inserts for warnings, contraindications, and approved indications before any clinical application
- **MOA documentation**: Retrieve full DrugBank mechanism of action data (DG002) to complete mechanistic plausibility analysis
- **Competitive landscape review**: Assess whether BTK inhibitors (ibrutinib, acalabrutinib) or venetoclax-based regimens have fully displaced chlorambucil even in mutated-IGHV patients, particularly in the Singaporean treatment context
- **Special population safety plan**: Develop a monitoring protocol for elderly patients with renal impairment or cardiac comorbidities, who represent the primary target population for chlorambucil-based CLL therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

