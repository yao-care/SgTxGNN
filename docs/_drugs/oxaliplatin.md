---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 740
evidence_level: L5
indication_count: 10
---

# Oxaliplatin
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

# Oxaliplatin: From Colorectal Cancer to Malignant Pleural Mesothelioma

## One-Sentence Summary

Oxaliplatin is a third-generation platinum compound whose established global indication is metastatic colorectal cancer (typically combined with 5-FU/leucovorin, FOLFOX). The TxGNN model predicts it may also be effective for **Malignant Pleural Mesothelioma**, with **5 clinical trials** and **20 publications** currently supporting this direction — though evidence is limited to small, non-randomized Phase II studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (global reference indication; no local licenses on file) |
| Predicted New Indication | Malignant Pleural Mesothelioma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (DrugBank MOA field is unpopulated). Based on known pharmacology, oxaliplatin is a platinum-based alkylating agent that forms DNA inter-strand and intra-strand crosslinks, blocking DNA replication and transcription in rapidly dividing tumor cells — a mechanism it shares with cisplatin/carboplatin, but with a distinct diaminocyclohexane carrier ligand that gives it activity independent of mismatch-repair status.

Malignant pleural mesothelioma is, like colorectal cancer, a solid tumor for which platinum-based combination chemotherapy (classically cisplatin or carboplatin plus pemetrexed) is already standard first-line care. This shared reliance on platinum-DNA damage as the therapeutic backbone is the mechanistic basis for the TxGNN prediction: substituting oxaliplatin for cisplatin/carboplatin within a doublet (with gemcitabine, raltitrexed, or vinorelbine) is a biologically plausible extension rather than a novel mechanism.

That said, all supporting clinical data identified here are small (n≈14–70), single-arm or retrospective Phase II experiences from the early 2000s, predating pemetrexed-based standard of care. None are randomized, and no trial directly compares oxaliplatin-based regimens against the current cisplatin/pemetrexed standard, so the mechanistic plausibility is stronger than the direct clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Completed | 29 | Oxaliplatin + gemcitabine as 1st/2nd-line therapy for pleural/peritoneal mesothelioma; evaluated response rate. Directly relevant. |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Unknown | 29 | Bortezomib (Velcade) + Eloxatin (oxaliplatin) in previously treated pleural/peritoneal mesothelioma; two-stage design, small sample. |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | Not yet recruiting | 30 | Neoadjuvant cadonilimab + chemotherapy for gastroesophageal junction/gastric cancer; oxaliplatin is a background regimen component, not mesothelioma-related. Low relevance. |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | Recruiting | 345 | First-in-human dose escalation of CBL-B inhibitor NX-1607 across advanced malignancies; not oxaliplatin-specific. Low relevance. |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | Unknown | 1000 | International registry of intraperitoneal aerosol chemotherapy (PIPAC/PITAC) for pleural/peritoneal malignancies; not a systemic oxaliplatin trial. Low relevance. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase 2 single-arm (pilot) | Tumori | Oxaliplatin + raltitrexed active in inoperable malignant pleural mesothelioma, confirming earlier phase I signal |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase 2 single-arm (multicenter) | Clinical Lung Cancer | Gemcitabine + oxaliplatin in 25 MPM patients; multicenter activity evaluation |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Phase 2 single-arm (observational) | J Occup Med Toxicol | Oxaliplatin ± gemcitabine in pretreated MPM patients after pemetrexed failure |
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase 2 | J Clin Oncol | Raltitrexed + oxaliplatin in 70 MPM patients (15 pretreated, 55 naive); active combination |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase 2 | Lung Cancer | Vinorelbine + oxaliplatin as first-line therapy in untreated MPM |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase 2 | Lung Cancer | Raltitrexed-oxaliplatin inactive as second-line MPM treatment; no objective responses in 14 evaluable patients |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review | Int J Mol Sci | Reviews immunomodulatory effects of cisplatin/oxaliplatin/pemetrexed on immune checkpoint expression in MPM, informing chemo-immunotherapy sequencing |
| [12601280](https://pubmed.ncbi.nlm.nih.gov/12601280/) | 2003 | Review | Curr Opin Oncol | Overview of MPM chemotherapy including raltitrexed-oxaliplatin results |
| [11836672](https://pubmed.ncbi.nlm.nih.gov/11836672/) | 2002 | Review | Semin Oncol | Reviews antifolate-based regimens including raltitrexed/oxaliplatin combination in MPM |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Retrospective cohort | Eur J Cancer | Institut Gustave Roussy 9-year, 163-patient experience including raltitrexed-oxaliplatin regimen |

## Singapore Market Information

Oxaliplatin currently has no registered license in Singapore in this dataset (market status: not marketed; 0 total registrations).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (third-generation platinum-based alkylating agent) |
| Myelosuppression Risk | Medium (neutropenia and thrombocytopenia are recognized class effects; peripheral sensory neuropathy, not myelosuppression, is oxaliplatin's dose-limiting toxicity) |
| Emetogenicity Classification | Moderate to high |
| Monitoring Items | CBC with differential, hepatic and renal function, neurological assessment for peripheral neuropathy |
| Handling Protection | Cytotoxic drug handling precautions required (personal protective equipment, closed-system transfer devices per institutional policy) |

Jurisdiction-specific warnings and contraindications are not yet available (blocking data gap) — please refer to the package insert warnings and precautions once local labeling is obtained.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is sound (platinum-DNA damage shared with the current MPM standard of care), but supporting clinical evidence is limited to small, non-randomized Phase II/retrospective studies from the early 2000s (L2), predating the pemetrexed-based standard of care. The drug is not currently registered in Singapore, and local safety labeling (warnings, contraindications, DDI) is a blocking data gap that prevents even an initial S1 safety screen.

**To proceed, the following is needed:**
- HSA/TFDA package insert data (warnings, contraindications) to clear the blocking safety gap
- Confirmed DrugBank MOA record for mechanistic verification
- Updated evidence search against current pemetrexed/platinum standard-of-care comparators (no head-to-head data currently identified)
- Route/formulation compatibility assessment if local registration is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

