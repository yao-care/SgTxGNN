---
layout: default
title: Vinblastine
parent: Low Evidence (L5)
nav_order: 1058
evidence_level: L5
indication_count: 10
---

# Vinblastine
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

# Vinblastine: From Vinca Alkaloid Chemotherapy to Rhabdomyosarcoma

## One-Sentence Summary

Vinblastine is a vinca alkaloid chemotherapy drug that blocks cell division. The HSA records for its two Singapore registrations do not state an approved indication.
The TxGNN model predicts it may be effective for **Rhabdomyosarcoma**, but there are currently **0 registered clinical trials** for this indication, and the **15 publications** retrieved are mostly case reports, preclinical studies, or work on related drugs (vinorelbine).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA records (all approved indication text is blank) |
| Predicted New Indication | Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 (preclinical studies and case reports only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank record provided. Based on known pharmacology, vinblastine is a vinca alkaloid that binds tubulin, blocks microtubule assembly, and arrests rapidly dividing cells in mitosis.

Rhabdomyosarcoma is a highly proliferative, chemosensitive soft tissue tumour, mainly in children. Other vinca-class agents (vincristine, vinorelbine) are already used in its regimens. This supports plausibility at the drug-class level.

Vinblastine-specific support is thin. Old xenograft work shows that one of three rhabdomyosarcoma lines (Rh28) was very responsive to vinblastine, while the other two showed only marginal activity. Clinical evidence is limited to case reports in which vinblastine was given as part of a combination, so its individual contribution cannot be isolated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomized trials or systematic reviews were retrieved. The table lists the most relevant items, ordered roughly by relevance to vinblastine in rhabdomyosarcoma.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38050209](https://pubmed.ncbi.nlm.nih.gov/38050209/) | 2023 | Case report/review | Medicine | Adult perianal rhabdomyosarcoma. A partial response was seen after nivolumab, dacarbazine, cisplatin and vinblastine, followed by surgery. |
| [2451411](https://pubmed.ncbi.nlm.nih.gov/2451411/) | 1987 | Case report/review | Hinyokika Kiyo | Refractory prostatic rhabdomyosarcoma in a child. The pelvic mass shrank rapidly on cisplatin, vinblastine and peplomycin after standard chemotherapy failed. The patient had relapsed 4 months after surgery. |
| [2417460](https://pubmed.ncbi.nlm.nih.gov/2417460/) | 1985 | Case report | Hinyokika Kiyo | Prostatic rhabdomyosarcoma in a child treated with cisplatin, vinblastine and bleomycin after the first regimen (vincristine, actinomycin D, cyclophosphamide). |
| [6692363](https://pubmed.ncbi.nlm.nih.gov/6692363/) | 1984 | Preclinical | Cancer Research | In three rhabdomyosarcoma xenografts, vinblastine was very active in the Rh28 line but only marginally active in the other two. |
| [3329524](https://pubmed.ncbi.nlm.nih.gov/3329524/) | 1987 | Preclinical/mechanistic | Anti-Cancer Drug Design | Rhabdomyosarcoma xenograft model examining why vincristine and vinblastine differ in therapeutic selectivity. |
| [26024389](https://pubmed.ncbi.nlm.nih.gov/26024389/) | 2015 | Preclinical | Cell Death & Differentiation | PLK1 inhibitors and microtubule-destabilizing drugs were synergistically lethal in rhabdomyosarcoma models. |
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase II (vinorelbine, not vinblastine) | European Journal of Cancer | Vinorelbine plus low-dose oral cyclophosphamide in relapsed or refractory paediatric solid tumours, with good tolerance and efficacy in rhabdomyosarcoma. Class-level evidence only. |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Clinical study (vinorelbine) | Cancer | Vinorelbine showed activity in rhabdomyosarcoma among previously treated advanced childhood sarcomas. |
| [15378498](https://pubmed.ncbi.nlm.nih.gov/15378498/) | 2004 | Pilot study (vinorelbine) | Cancer | Dose-finding pilot of vinorelbine plus low-dose cyclophosphamide as a maintenance regimen in refractory or recurrent sarcoma. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07944P | DBL™ VINBLASTINE INJECTION (Hospira Australia) | Injection | Not stated in HSA record |
| SIN10987P | VELBASTINE FOR INJECTION 10 mg/vial (Korea United Pharmaceutical) | Injection, powder, for solution | Not stated in HSA record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, antimitotic) |
| Myelosuppression Risk | High (bone marrow suppression is a recognised class concern; literature on leukaemia use also flags it) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations. Please refer to the package insert for administration precautions. |

The myelosuppression and emetogenicity ratings come from general knowledge of the drug class, not from the Evidence Pack.

## Safety Considerations

Please refer to the package insert for safety information.

One literature signal was retrieved. A 1988 case report in neuroblastoma (PMID 3411345) describes severe ileus with cisplatin plus vinblastine infusion.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.86%), and the antimitotic mechanism is plausible for a chemosensitive tumour like rhabdomyosarcoma. However, there are no registered trials. The clinical evidence is a few case reports of combination regimens, and the only vinca-class efficacy data come from vinorelbine, so vinblastine-specific efficacy is unproven. Safety data from the package insert are also missing.

**To proceed, the following is needed:**
- HSA package insert warnings, contraindications and approved indications (download and parse the PDF from the HSA website)
- Detailed mechanism of action data (query the DrugBank API)
- Evidence on vinblastine's individual contribution in rhabdomyosarcoma, for example comparative or registry data against vincristine or vinorelbine regimens
- A safety and myelosuppression monitoring plan for paediatric and young-adult patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

