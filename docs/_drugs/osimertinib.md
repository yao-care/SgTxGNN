---
layout: default
title: Osimertinib
parent: 僅模型預測 (L5)
nav_order: 738
evidence_level: L5
indication_count: 10
---

# Osimertinib
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

# Osimertinib: From Non-Small Cell Lung Cancer to Thrombocytopenia

## One-Sentence Summary

Osimertinib is a third-generation EGFR tyrosine kinase inhibitor (EGFR-TKI), used as first-line therapy for EGFR-mutation-positive non-small cell lung cancer (NSCLC), as documented across the retrieved literature.
The TxGNN model's top prediction for this drug is **Thrombocytopenia** (score 98.46%), but the underlying **8 clinical trials** and **20 publications** show this is a known **adverse effect** of osimertinib (bone-marrow suppression), not a therapeutic relationship — this candidate does not represent a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer, EGFR mutation-positive (per literature evidence; not present in the regulatory record) |
| Predicted New Indication | Thrombocytopenia |
| TxGNN Prediction Score | 98.46% |
| Evidence Level | L4 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the retrieved literature, Osimertinib is a third-generation EGFR-TKI used as first-line treatment for EGFR-mutation-positive NSCLC.

However, this candidate does **not** hold up as a genuine repurposing signal. Every clinical trial and publication retrieved under "thrombocytopenia" describes it as a **hematological adverse event of osimertinib** — including case reports of severe thrombocytopenia requiring drug rechallenge (PMID 36729978) or switching to an alternative EGFR-TKI (aumolertinib, PMID 36730569), a meta-analysis of RCTs quantifying osimertinib-related haematological toxicity (PMID 39159992), and a FAERS-based disproportionality analysis of EGFR-TKI adverse-event profiles (PMID 40135231). None of the 8 associated clinical trials studied osimertinib as a treatment for thrombocytopenia — they are all NSCLC combination-therapy trials in which thrombocytopenia was, at most, a safety-monitoring endpoint.

This pattern — a high TxGNN score backed entirely by adverse-event literature rather than efficacy evidence — repeats across nearly all of this drug's top-10 predictions (heart neoplasm, thrombotic disease, heart conduction disease, cardiovascular disease, heart disease are all cardiotoxicity signals; several others are ultra-rare genetic platelet disorders with zero supporting evidence). It strongly suggests the knowledge graph is encoding drug–adverse-event edges as generic drug–disease associations, producing a spurious "treats" signal that is in fact a **safety signal in reverse**.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03989115](https://clinicaltrials.gov/study/NCT03989115) | Phase 1/2 | Completed | 113 | RMC-4630 + osimertinib safety/PK study in EGFR+ NSCLC; thrombocytopenia not a treatment target |
| [NCT03455829](https://clinicaltrials.gov/study/NCT03455829) | Phase 1/2 | Completed | 30 | G1T38 + osimertinib in EGFR+ metastatic NSCLC |
| [NCT03381274](https://clinicaltrials.gov/study/NCT03381274) | Phase 1/2 | Active, not recruiting | 43 | Novel combination therapies in previously treated EGFRm NSCLC |
| [NCT07458919](https://clinicaltrials.gov/study/NCT07458919) | Early Phase 1 | Not yet recruiting | 94 | 1st- vs 3rd-generation EGFR-TKI in NSCLC with 19delins mutation |
| [NCT07285148](https://clinicaltrials.gov/study/NCT07285148) | Phase 1/2 | Not yet recruiting | 253 | ANS014004 + EGFR-TKI in EGFR+ NSCLC |
| [NCT02789345](https://clinicaltrials.gov/study/NCT02789345) | Phase 1 | Completed | 29 | Ramucirumab/necitumumab + osimertinib in T790M+ NSCLC |
| [NCT02424617](https://clinicaltrials.gov/study/NCT02424617) | Phase 1/2 | Completed | 40 | BGB324 (bemcentinib) + erlotinib in NSCLC |
| [NCT03940703](https://clinicaltrials.gov/study/NCT03940703) | Phase 2 | Active, not recruiting | 140 | Tepotinib + osimertinib in MET-amplified NSCLC (INSIGHT 2) |

*All trials are NSCLC combination-therapy studies; none evaluate osimertinib as a treatment for thrombocytopenia.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39159992](https://pubmed.ncbi.nlm.nih.gov/39159992/) | 2024 | RCT Meta-analysis | BMJ Support Palliat Care | Meta-analysis quantifying osimertinib-related haematological toxicity incidence in NSCLC |
| [36729978](https://pubmed.ncbi.nlm.nih.gov/36729978/) | 2023 | Case Report | Anti-Cancer Drugs | Severe thrombocytopenia from osimertinib + sitagliptin combination; successful rechallenge after remission |
| [36730569](https://pubmed.ncbi.nlm.nih.gov/36730569/) | 2023 | Case Report | Anti-Cancer Drugs | Osimertinib-induced severe thrombocytopenia managed by switching to aumolertinib |
| [40115544](https://pubmed.ncbi.nlm.nih.gov/40115544/) | 2025 | Case Report | Case Reports in Oncology | Thrombocytopenia in an EGFR-mutant NSCLC patient with ARDS treated via ECMO + osimertinib |
| [40135231](https://pubmed.ncbi.nlm.nih.gov/40135231/) | 2025 | Disproportionality Analysis | Frontiers in Pharmacology | Network meta-analysis/FAERS disproportionality analysis of EGFR-TKI adverse-event profiles |
| [37760942](https://pubmed.ncbi.nlm.nih.gov/37760942/) | 2023 | Cohort | Biomedicines | Prospective cohort correlating plasma osimertinib levels with treatment efficacy and adverse events |
| [33755621](https://pubmed.ncbi.nlm.nih.gov/33755621/) | 2021 | Review | American Journal of Nursing | Notes thrombocytopenia among common adverse effects of osimertinib |
| [33376097](https://pubmed.ncbi.nlm.nih.gov/33376097/) | 2021 | Phase Ib Trial | Clinical Cancer Research | Osimertinib + navitoclax (BCL-2/BCL-xL inhibitor) combination; hematologic effects relevant to platelet counts |

---

## Singapore Market Information

Osimertinib currently has no marketing authorization on file in Singapore (0 registrations recorded in this evidence pack).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (third-generation EGFR tyrosine kinase inhibitor); not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Moderate — leukopenia, lymphopenia, thrombocytopenia, neutropenia, and anemia are reported as common adverse effects; rare severe thrombocytopenia cases requiring rechallenge or drug switch have been documented |
| Emetogenicity Classification | Low (typical for oral EGFR-TKIs); not directly assessed in this evidence pack — please refer to the package insert |
| Monitoring Items | CBC with differential (thrombocytopenia, neutropenia, anemia); cardiac monitoring (ECG/QT interval, LVEF) given documented cardiotoxicity signals; liver function |
| Handling Protection | Standard precautions for oral antineoplastic/targeted agents per institutional hazardous-drug handling policy |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (TFDA/HSA label data is flagged as a **Blocking** data gap — DG001 — preventing progress to the S1 safety review stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN predictions for Osimertinib (thrombocytopenia, heart neoplasm, thrombotic disease, heart conduction disease, cardiovascular disease, heart disease, plus several ultra-rare genetic platelet disorders with zero evidence) are consistently backed by adverse-event/toxicity literature rather than therapeutic evidence, indicating these are likely artifacts of the knowledge graph encoding drug-safety edges as drug-disease associations rather than genuine repurposing signals. Combined with the Blocking-severity gap in TFDA/HSA label data, this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) — required to clear the Blocking gap (DG001) before any safety review
- Confirmed mechanism of action (DG002)
- Re-screening of TxGNN output with adverse-event/pharmacovigilance edges excluded or down-weighted, to distinguish genuine efficacy signals from toxicity signals
- If a genuine therapeutic candidate exists further down this drug's ranked list, re-evaluate it independently — the current top 10 does not contain one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

