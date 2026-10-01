---
layout: default
title: Vinorelbine
parent: Low Evidence (L5)
nav_order: 1060
evidence_level: L5
indication_count: 10
---

# Vinorelbine
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

# Vinorelbine: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

Vinorelbine is a vinca alkaloid chemotherapy. The retrieved literature describes it as an established agent for non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Ewing sarcoma**.
Currently **4 clinical trials** and **5 publications** are linked to this direction, but none is specific to Ewing sarcoma alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration data. Published literature describes established use in NSCLC |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L2 per the Evidence Pack. Caveat: the completed Phase 2 studies are single-arm and cover mixed pediatric tumors, not Ewing sarcoma alone |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Vinorelbine is a vinca alkaloid that binds tubulin and blocks mitotic spindle formation. Ewing sarcoma is a rapidly proliferating, chemosensitive tumor, so an antimitotic agent is a plausible fit.

The most relevant clinical signal comes from a regimen of vinorelbine with low-dose (metronomic) cyclophosphamide. It has been studied in children and young adults with relapsed or refractory solid tumors, including Ewing tumors. The very high TxGNN score is consistent with this signal but is not evidence in itself.

Detailed mechanism-of-action data from DrugBank were not available in this evidence pack. The mechanism above comes from general knowledge of the vinca alkaloid class.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | Unknown | 210 | Vinorelbine + cyclophosphamide in refractory or relapsed tumors, explicitly including Ewing tumors. The regimen matches the published sarcoma literature |
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | Completed | 50 | Vinorelbine in children with recurrent or refractory cancers. Mixed tumor population, so Ewing-specific efficacy is uncertain |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | N/A | Active, not recruiting | 100 | Prospective cohort of risk-stratified treatment in pediatric Ewing sarcoma in China. Vinorelbine's contribution is unclear |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | Recruiting | 105 | CAMPFIRE pediatric master protocol. Vinorelbine is not clearly a Ewing-specific arm |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase II trial | Eur J Cancer | Vinorelbine + continuous low-dose cyclophosphamide in children and young adults with relapsed or refractory solid tumors. Good tolerance, with efficacy highlighted in rhabdomyosarcoma |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Phase II trial | Cancer | Vinorelbine in previously treated advanced childhood sarcomas. Activity shown in rhabdomyosarcoma |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Front Pharmacol | Review of chemotherapy drugs for soft tissue sarcomas |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Preclinical | Int J Cancer | A PLK1 inhibitor combined with microtubule-interfering drugs, including vinorelbine, synergistically induced apoptosis in Ewing sarcoma cells |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case report | BMC Urol | Extraosseous Ewing sarcoma of the kidney, diagnostic focus. Not evidence for vinorelbine efficacy |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN06778P | NAVELBINE INJECTION 10 mg/ml | Injection | FAREVA PAU |
| SIN12547P | NAVELBINE SOFT CAPSULE 30 mg | Capsule, liquid filled | CATALENT GERMANY EBERBACH GMBH / FAREVA PAU |
| SIN12546P | NAVELBINE SOFT CAPSULE 20 mg | Capsule, liquid filled | CATALENT GERMANY EBERBACH GMBH / FAREVA PAU |

Approved indication text was not provided for these registrations. Both injectable and oral routes are available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, antimitotic) |
| Myelosuppression Risk | High. Neutropenia is the dose-limiting toxicity, as noted in the supplied literature |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full details.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, and Phase 2 data support vinorelbine plus low-dose cyclophosphamide in relapsed pediatric sarcomas. However, the evidence is not Ewing-specific, comes from single-arm studies, and the key trial status is unknown. The Singapore package insert safety data are also missing. Once these gaps are closed, this could move to Proceed with Guardrails as a research question.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (blocking)
- Ewing sarcoma-specific response data from the vinorelbine + cyclophosphamide studies
- Confirmation of the status and results of NCT00180947
- Detailed mechanism of action data from DrugBank

This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

