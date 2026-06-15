---
layout: default
title: Bortezomib
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Bortezomib
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

# Bortezomib: From Multiple Myeloma to Vertebral Anomalies and Variable Endocrine and T-Cell Dysfunction

## One-Sentence Summary

Bortezomib (Velcade) is a first-in-class 26S proteasome inhibitor, approved globally as a primary treatment for multiple myeloma and relapsed mantle cell lymphoma, though it holds no current product registration in Singapore.
The TxGNN model predicts it may be effective for **Vertebral Anomalies and Variable Endocrine and T-Cell Dysfunction** (score: 96.10%),
with **no clinical trials** and **no publications** currently supporting this specific direction — this is a purely model-driven prediction based on graph neural network inference, without any clinical or experimental evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple Myeloma / Mantle Cell Lymphoma (globally approved; not registered in Singapore) |
| Predicted New Indication | Vertebral Anomalies and Variable Endocrine and T-Cell Dysfunction |
| TxGNN Prediction Score | 96.10% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bortezomib is a reversible, selective inhibitor of the 26S proteasome, targeting specifically the chymotrypsin-like proteolytic activity of the β5 catalytic subunit. By blocking proteasomal degradation, it causes accumulation of polyubiquitinated regulatory proteins, stabilises pro-apoptotic factors (including IκBα, p53, Bax, and Bik), induces endoplasmic reticulum stress, and powerfully suppresses the NF-κB survival signalling axis. This combination of effects underlies its established clinical utility in multiple myeloma and mantle cell lymphoma, where constitutive NF-κB activation and high proteasomal load are hallmarks of the malignancy.

"Vertebral anomalies and variable endocrine and T-cell dysfunction" is an extremely rare congenital syndrome characterised by structural vertebral defects combined with endocrine dysfunction and immune dysregulation at the T-cell level. The theoretical basis for TxGNN's prediction likely derives from Bortezomib's known ability to modulate T-cell function: proteasome inhibition alters MHC-I antigen presentation, disrupts T-cell homeostatic signalling via NF-κB suppression, and can influence the balance between regulatory and effector T-cell populations. These mechanisms may have indirect relevance to the T-cell dysfunction component of this syndrome.

However, there is no established direct mechanistic link between proteasome inhibition and the pathogenesis of vertebral anomaly syndromes, which are primarily driven by developmental genetic programmes (e.g., NOTCH signalling, somitogenesis transcription factors) entirely unrelated to proteasome biology. The high TxGNN score (0.961, graph rank 24,031) reflects structural similarity in the disease–gene knowledge graph rather than any validated biological or clinical rationale. No clinical trials have been registered, no relevant publications exist, and no preclinical model data supports this use. This prediction should be treated as a hypothesis-generating signal only, with no near-term clinical development pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Bortezomib is not currently registered with Singapore's Health Sciences Authority (HSA). No product licences were found in the regulatory database. Clinicians requiring Bortezomib in Singapore would need to access it via special approval or importation pathways.

---

## Cytotoxicity

Bortezomib is an antineoplastic agent used for haematological malignancies. The cytotoxicity assessment below is based on its established pharmacological class and internationally published prescribing information.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Proteasome inhibitor (novel mechanism; distinct from conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Moderate to High: Thrombocytopenia is the hallmark haematologic toxicity. Platelet nadir typically occurs around Day 11 of a 21-day cycle and recovers by Day 21. Neutropenia and anaemia are also observed. |
| Emetogenicity Classification | Low (minimal emetogenic potential per MASCC/ESMO oncology guidelines) |
| Monitoring Items | CBC with differential and platelet count before each dose; liver function tests; renal function; blood glucose (especially in diabetic patients); peripheral neuropathy clinical assessment each cycle |
| Handling Protection | Must follow institutional cytotoxic drug handling regulations: gloves and protective gown required; avoid skin and mucous membrane contact; dispose of as hazardous waste |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high predictive score (96.10%) to Bortezomib for vertebral anomalies and variable endocrine and T-cell dysfunction, this remains a purely model-derived prediction backed by zero clinical trials, zero supporting publications, and no established mechanistic connection to this rare congenital developmental syndrome. At the current evidence level (L5), no clinical development activities can be justified.

**To proceed, the following is needed:**
- Basic mechanistic investigation to determine whether proteasome inhibition modulates any pathway relevant to vertebral anomaly or T-cell dysfunction in this specific syndrome
- Retrieval of Bortezomib's full mechanism of action documentation from DrugBank (currently a data gap) to identify any overlooked biological connections
- Identification of relevant patient-derived cell lines, animal models, or organoids that recapitulate this syndrome's pathophysiology
- Acquisition of Bortezomib's Singapore package insert or international SmPC to establish a full safety reference baseline
- Review of whether the T-cell dysfunction component of this syndrome shares any molecular features with the immune dysregulation Bortezomib modulates in myeloma (e.g., NF-κB pathway involvement)
- Expert consultation with rare disease specialists to evaluate whether the genetic architecture of this syndrome overlaps with proteasome-regulated processes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

