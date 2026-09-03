---
layout: default
title: Pamidronic Acid
parent: 僅模型預測 (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
---

# Pamidronic Acid
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

# Pamidronic Acid: From Bisphosphonate Bone Therapy to HIV Infectious Disease

## One-Sentence Summary

Pamidronic acid (DrugBank DB00282) is a second-generation nitrogen-containing bisphosphonate; its original approved indications are not recorded in this evidence pack.
The TxGNN model predicts it may be effective for **HIV Infectious Disease**, based on the drug's known ability to activate Vγ9Vδ2 γδ T cells via osteoclast FPPS inhibition — a mechanism explored in HIV "shock-and-kill" cure strategies.
Evidence for this specific link is currently limited to **0 clinical trials** and **6 publications**, most of which are mechanism-level or case reports of adverse events rather than efficacy studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no license or original-indication data provided) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for pamidronic acid is not available in this evidence pack. Based on the information that is available, pamidronic acid is a nitrogen-containing bisphosphonate that inhibits farnesyl pyrophosphate synthase (FPPS) in osteoclasts, a mechanism most clearly documented for its rank-6 predicted indication, Paget disease of bone (an established bisphosphonate indication supported by a Cochrane systematic review, PMID 29192423).

For the HIV prediction specifically, the repurposing rationale supplied with this pack notes that FPPS inhibition by aminobisphosphonates causes accumulation of upstream isoprenoid metabolites (e.g., isopentenyl pyrophosphate), which is a known activator of Vγ9Vδ2 γδ T cells. This immunological activation is being explored as part of "shock-and-kill" strategies aimed at reactivating latent HIV-1 reservoirs so that immune effector cells can clear infected cells. This is a plausible immunopharmacological mechanism, but it is distinct from — and much less validated than — pamidronic acid's established bone-metabolism pharmacology.

It is worth noting that several other TxGNN candidates in this pack are simply rediscoveries of pamidronic acid's known bisphosphonate pharmacology (Paget disease of bone, its early-onset genetic subtype, osteomesopyknosis), which lends indirect credibility to the model's mechanistic reasoning in general, even though the top-ranked HIV prediction itself remains mechanism-only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29925697](https://pubmed.ncbi.nlm.nih.gov/29925697/) | 2018 | Review | JCI Insight | Discusses γδ T cells as an immunotherapeutic approach for HIV cure strategies, including agents that expand or activate this T-cell subset |
| [11983250](https://pubmed.ncbi.nlm.nih.gov/11983250/) | 2002 | Review | Vaccine | Reviews innate T-cell immunity to HIV and phosphocarbohydrate/phosphoantigen-based immune intervention strategies |
| [37744358](https://pubmed.ncbi.nlm.nih.gov/37744358/) | 2023 | In vitro/Preclinical | Frontiers in Immunology | Shows aminobisphosphonates (including pamidronate) can reactivate the latent HIV-1 reservoir in cells from people living with HIV, as part of "shock-and-kill" latency-reversal research |
| [16761013](https://pubmed.ncbi.nlm.nih.gov/16761013/) | 2006 | Case Report (adverse event) | Kidney International | Describes collapsing focal segmental glomerulosclerosis associated with HIV and pamidronate use — a safety signal, not efficacy evidence |
| [20713349](https://pubmed.ncbi.nlm.nih.gov/20713349/) | 2011 | Case Report (adverse event) | Endocrine Practice | Reports osteoporosis and bilateral hip osteonecrosis in an HIV-infected patient on corticosteroids and antiretroviral therapy; pamidronate context is incidental |
| [9302445](https://pubmed.ncbi.nlm.nih.gov/9302445/) | 1997 | Case Report (adverse event) | AIDS | Reports hypercalcemia in an AIDS patient treated with growth hormone; not a pamidronate efficacy study |

---

## Safety Considerations

Please refer to the package insert for safety information.

A **Blocking** data gap (DG001) was identified: local drug-label warnings and contraindications have not yet been retrieved, and this pack cannot proceed to an initial safety assessment (S1) until that data is obtained. A **High**-severity gap (DG002) also exists for the drug's mechanism-of-action data, which limits the analysis above.

---

## Conclusion and Next Steps

**Decision: Research Question (Hold pending further evidence)**

**Rationale:**
The HIV indication is supported only by mechanism-level and preclinical evidence (Evidence Level L4) — there are no clinical trials, and most identified literature consists of adverse-event case reports rather than efficacy data. Combined with a Blocking safety data gap, this candidate is not yet ready for any development or clinical decision-making.

**To proceed, the following is needed:**
- Drug label warnings and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action data for pamidronic acid (DG002, High)
- Preclinical or early-phase clinical data specifically testing pamidronate as an HIV latency-reversing agent
- Original approved indication and Singapore licensing data, currently absent from this pack

*Note: This drug's rank-6 prediction, Paget disease of bone (Evidence Level L1, decision stage S3, "Proceed with Guardrails," supported by a Cochrane systematic review), reflects an already-established bisphosphonate indication and may warrant separate review if regulatory registration is being considered.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

