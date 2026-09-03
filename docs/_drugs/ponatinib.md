---
layout: default
title: Ponatinib
parent: 僅模型預測 (L5)
nav_order: 799
evidence_level: L5
indication_count: 10
---

# Ponatinib
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

# Ponatinib: From Chronic Myeloid Leukemia to Liposarcoma

> **Note on candidate selection**: Among the 10 TxGNN top-ranked candidates in this Evidence Pack, the #1-ranked prediction ("fibromatosis, gingival") has **zero** supporting clinical trials or literature, and the source rationale itself flags it as a low-credibility prediction. Several other top-10 entries (ranks 3, 6, 7, 8, 10) are similarly unsupported, and two entries (ranks 3 and 8) show clear signs of **entity-linking artifacts** — their attached "literature" is about unrelated topics (frontotemporal dementia reviews, leukemia treatment history) that only superficially match the disease name string. This report therefore features **Liposarcoma (rank 2)**, the highest-evidence candidate in the set (Evidence Level L4, Decision Stage S1), as the representative prediction for evaluation.

---

## One-Sentence Summary

> Ponatinib is a multi-target tyrosine kinase inhibitor whose established use (per literature retrieved in this pack) is in chronic myeloid leukemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukemia (Ph+ ALL); it is **not currently marketed in Singapore**.
> The TxGNN model predicts potential activity in **Liposarcoma**, with **0 clinical trials** and **1 preclinical publication** currently supporting this direction.
> Evidence is preliminary (mechanism/preclinical-target level only) and safety label data remain a **blocking data gap**, so this candidate is not ready to advance beyond a research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukemia (CML) / Ph+ acute lymphoblastic leukemia (inferred from retrieved literature; no Singapore license record exists for this field) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Ponatinib is formally marked as a data gap in this Evidence Pack (DG002, High severity). However, literature incidentally retrieved during evidence collection (PMID 37399979, *Biochim Biophys Acta Rev Cancer*, 2023) independently describes Ponatinib as a third-generation BCR-ABL tyrosine kinase inhibitor that also potently inhibits FGFR, PDGFR, KIT, RET, and SRC family kinases — i.e., a broad multi-target kinase inhibitor rather than a BCR-ABL-selective agent.

This broader kinase profile is mechanistically relevant to liposarcoma: certain liposarcoma subtypes (notably myxoid and dedifferentiated liposarcoma) are driven in part by FGFR and PDGFRα signaling. A kinase-profiling/screening study (PMID 29132397, *Journal of Hematology & Oncology*, 2017) used RNAi and drug-screening approaches to identify druggable kinase targets in liposarcoma, supporting the general premise that kinase inhibition is a viable therapeutic strategy in this tumor type.

Importantly, this is a **target-identification study**, not a direct efficacy study of Ponatinib in liposarcoma models — the rationale in the Evidence Pack explicitly notes it is unclear whether Ponatinib itself was tested in the reported screen. The mechanistic link is therefore plausible but indirect, and no clinical or direct preclinical efficacy data for Ponatinib specifically in liposarcoma currently exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) | 2017 | Preclinical/Screening | Journal of Hematology & Oncology | RNAi and drug-screening kinase profiling of liposarcoma identified druggable kinase targets, supporting kinase inhibition as a viable therapeutic strategy in this understudied tumor type; direct Ponatinib activity data not confirmed. |

---

## Cytotoxicity

Ponatinib is an antineoplastic kinase inhibitor (per literature retrieved for CML/Ph+ ALL treatment context in this pack).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — multi-target tyrosine kinase inhibitor (BCR-ABL / FGFR / PDGFR / KIT / RET / SRC), per PMID 37399979 |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions; literature incidentally retrieved in this pack (see Safety Considerations below) points to cardiovascular, renal, and pulmonary monitoring as relevant for this drug class |
| Handling Protection | Please refer to institutional hazardous drug handling protocols for oral antineoplastic agents |

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug–drug interactions) are marked as a **Blocking** data gap in this Evidence Pack (DG001) — TFDA/HSA label data have not been obtained, and DDI lookup returned no results.

However, several Ponatinib-specific safety publications were incidentally retrieved during evidence collection for other candidate indications in this pack (not from the official DDI/label pipeline). These are flagged here as supplementary signals only, and should not substitute for formal label review:

- **Cardiotoxicity**: [PMID 30629146](https://pubmed.ncbi.nlm.nih.gov/30629146/) — mechanisms of Ponatinib-induced cardiotoxicity; [PMID 35152199](https://pubmed.ncbi.nlm.nih.gov/35152199/) and [PMID 26008987](https://pubmed.ncbi.nlm.nih.gov/26008987/) — cardiovascular toxicity associated with TKI therapy in CML.
- **Pulmonary toxicity**: [PMID 38077703](https://pubmed.ncbi.nlm.nih.gov/38077703/) — case report of Ponatinib-induced pneumonitis with severe ARDS; [PMID 32527740](https://pubmed.ncbi.nlm.nih.gov/32527740/) — pulmonary complications of BCR-ABL TKIs as a class.
- **Renal safety**: [PMID 37046701](https://pubmed.ncbi.nlm.nih.gov/37046701/) — pharmacovigilance review of renal adverse events across BCR-ABL TKIs.

For authoritative safety information, the official package insert / TFDA-HSA label review (DG001 remediation) is required before any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Safety label data are a Blocking data gap (DG001) — the drug cannot proceed to a formal S1 safety pre-evaluation until TFDA/HSA warning and contraindication data are obtained.
- Ponatinib is not currently marketed in Singapore (0 registrations), and the featured predicted indication (Liposarcoma) is supported only by indirect, target-identification-level preclinical evidence (L4) with no clinical trials or direct Ponatinib efficacy data.
- Of the 10 TxGNN top-ranked candidates reviewed, only 2 (Liposarcoma, Lung Benign Neoplasm) reach even a preliminary "Research Question" stage (S1); the remaining 8 show no corroborating evidence or apparent entity-linking artifacts and should not be advanced.

**To proceed, the following is needed:**
- Official TFDA/HSA package insert data (warnings, contraindications) to resolve DG001 (Blocking)
- Confirmed mechanism-of-action data from DrugBank to resolve DG002
- A direct preclinical efficacy study of Ponatinib (not just target-screening data) in liposarcoma cell lines or models
- Ongoing monitoring for new liposarcoma or FGFR/PDGFR-driven sarcoma trials involving Ponatinib
- Re-review of lower-ranked candidates only if genuine (non-artifact) supporting evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

