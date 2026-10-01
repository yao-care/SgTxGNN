---
layout: default
title: Vincristine
parent: Low Evidence (L5)
nav_order: 1059
evidence_level: L5
indication_count: 10
---

# Vincristine
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

# Vincristine: From Antineoplastic Chemotherapy to Ganglioneuroblastoma

## One-Sentence Summary

Vincristine is an antimitotic chemotherapy drug. The Singapore registry record does not state its approved indication.
The TxGNN model predicts it may be effective for **Ganglioneuroblastoma**, a tumour on the neuroblastic tumour spectrum.
Support is indirect: **4 clinical trials** (vincristine is part of the background chemotherapy, not the tested variable) and **6 publications** (mostly case reports).

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Ganglioneuroblastoma |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L3 (see note below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The upstream pack assigned L2. By the L1–L5 rules, L2 requires a completed Phase 2/3 RCT, and none exists here. The only completed trial is a Phase 1 pilot. The Phase 2 trial is single-arm and still active, and the Phase 3 trials are recruiting without results. The supporting literature is case-level or observational, so I rate it L3.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. From general pharmacology, vincristine binds tubulin, blocks microtubule polymerization and arrests dividing cells in metaphase. This makes it active against rapidly proliferating tumours.

Ganglioneuroblastoma belongs to the same neuroblastic tumour family as neuroblastoma. Vincristine is a standard backbone drug in neuroblastoma induction regimens. The mechanistic link is therefore plausible.

However, most of the evidence concerns neuroblastoma in general, not ganglioneuroblastoma specifically. No study isolates vincristine's own contribution. The TxGNN score is a graph-based prediction and does not replace clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Phase 2 | Active, not recruiting | 42 | Single-arm pilot adding dinutuximab and sargramostim to induction chemotherapy in newly diagnosed high-risk neuroblastoma. Supports feasibility and safety of the combination, not a vincristine-specific effect. |
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Phase 3 | Recruiting | 750 | Tests adding 131I-MIBG or lorlatinib to intensive therapy in high-risk neuroblastoma or ganglioneuroblastoma. Vincristine-based induction is the backbone. No results yet. |
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Phase 3 | Recruiting | 478 | Tests adding dinutuximab to intensive multimodal therapy in newly diagnosed high-risk neuroblastoma. Vincristine is in the background chemotherapy. No results yet. |
| [NCT01798004](https://clinicaltrials.gov/study/NCT01798004) | Phase 1 | Completed | 150 | Pilot of busulfan/melphalan consolidation after induction chemotherapy. Vincristine appears only in the preceding induction, so relevance is indirect. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Prospective clinical trial | Pediatric Blood & Cancer | Japanese trial (JN-L-10) using image-defined risk factors to time surgery in low-risk neuroblastoma. Concerns surgical decisions, not vincristine. |
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Case report | Postgraduate Medical Journal | Unresectable spinal ganglioneuroblastoma in a 21-year-old. A regimen including doxorubicin, vincristine, cyclophosphamide, etoposide, ifosfamide and cisplatin gave histologically proven complete remission. |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Case report | J Pediatr Hematol Oncol | Ganglioneuroblastoma presenting with obstructive jaundice, treated with a regimen containing cisplatin, pirarubicin/doxorubicin, cyclophosphamide and vincristine. |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Case report/Review | J Thorac Cardiovasc Surg | 31 patients with intrathoracic ganglioneuroblastoma treated with surgery, radiation or chemotherapy. 27 survived, with follow-up up to 25 years. Vincristine's role is not specified. |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Case report | J Pediatr Hematol Oncol | Infant with stage 4 multifocal ganglioneuroblastoma and gastric involvement. |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Case report | Hinyokika Kiyo | Adult adrenal ganglioneuroblastoma with giant regional lymph node metastasis, treated with multimodality therapy. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10319P | VINRACINE INJ. 1 mg/ml (Korea United Pharmaceutical Inc) | Injection | Not stated in the registry record |

## Cytotoxicity

The registry record has no toxicity data. The entries below reflect general knowledge of the vinca alkaloid class and must be confirmed against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, antimitotic) |
| Myelosuppression Risk | Generally low to moderate. Neurotoxicity is the dose-limiting concern. |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC, liver function, neurological assessment, bowel function (constipation/ileus) |
| Handling Protection | Must follow cytotoxic drug handling regulations. Intravenous use only; it is a vesicant, so avoid extravasation. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Vincristine is already a backbone drug in neuroblastoma induction regimens, and ganglioneuroblastoma lies on the same tumour spectrum. This makes the prediction plausible. However, no study tests vincristine specifically in ganglioneuroblastoma. Direct evidence is limited to case reports, and the larger trials use vincristine only as background therapy.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications, interactions). This is a blocking gap for safety screening.
- The approved indication text for SIN10319P.
- Detailed mechanism-of-action data from DrugBank.
- Review of disease-specific data from the ongoing Phase 3 neuroblastoma/ganglioneuroblastoma trials (NCT03126916, NCT06172296) once results are available.
- Pediatric oncology specialist oversight of any use, with dosing and neurotoxicity monitoring protocols.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

