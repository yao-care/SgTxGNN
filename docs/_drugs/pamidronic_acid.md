---
layout: default
title: Pamidronic Acid
parent: Low Evidence (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
---

# Pamidronic Acid
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

# Pamidronic Acid: From Bone Disorders to HIV Infection

## One-Sentence Summary

Pamidronic acid is an intravenous bisphosphonate, used clinically for bone conditions such as hypercalcaemia of malignancy, osteolytic lesions and Paget's disease of bone. The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **0 clinical trials** and only **1 preclinical study** directly supporting this. The remaining papers are reviews and adverse-event case reports.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record. Literature describes hypercalcaemia of malignancy, osteolytic lesions and Paget's disease of bone |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 (preclinical / mechanistic only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Pamidronic acid is a nitrogen-containing bisphosphonate. This class inhibits farnesyl pyrophosphate synthase, so isopentenyl pyrophosphate accumulates inside cells. This accumulation activates Vγ9Vδ2 γδ T cells, a kind of immune cell that can find and kill virus-infected cells. A 2023 laboratory study reported that aminobisphosphonates can reactivate the latent HIV-1 reservoir in cells from people living with HIV.

This fits the "shock and kill" HIV cure strategy. Latent virus is first woken up, then the immune system eliminates the infected cells. A 2018 review supports the role of γδ T cells in this approach. The prediction is therefore mechanistically plausible, but it rests on laboratory and ex vivo work only. No study has tested pamidronate for HIV in patients.

Other papers linking pamidronate and HIV are case reports of harm, not efficacy. These include collapsing focal segmental glomerulosclerosis (a kidney lesion) and bone problems in HIV patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37744358](https://pubmed.ncbi.nlm.nih.gov/37744358/) | 2023 | Preclinical / ex vivo study | Front Immunol | Aminobisphosphonates reactivated latent HIV-1 in cellular reservoirs, supporting a shock-and-kill approach |
| [29925697](https://pubmed.ncbi.nlm.nih.gov/29925697/) | 2018 | Review | JCI Insight | γδ T cells as an immunotherapy approach for HIV cure strategies |
| [11983250](https://pubmed.ncbi.nlm.nih.gov/11983250/) | 2002 | Review | Vaccine | Innate T cell immunity in HIV infection and immunotherapy with phosphocarbohydrates as a concept |
| [16761013](https://pubmed.ncbi.nlm.nih.gov/16761013/) | 2006 | Case report (adverse event) | Kidney Int | Collapsing focal segmental glomerulosclerosis associated with HIV and pamidronate. This is a safety signal, not efficacy |
| [20713349](https://pubmed.ncbi.nlm.nih.gov/20713349/) | 2011 | Case report (adverse event) | Endocr Pract | Osteoporosis and hip osteonecrosis in an HIV-infected man on inhaled corticosteroids and ritonavir-boosted therapy. Not efficacy evidence |
| [9302445](https://pubmed.ncbi.nlm.nih.gov/9302445/) | 1997 | Case report | AIDS | Hypercalcaemia in an AIDS patient given growth hormone. Not relevant to efficacy |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN11543P | PAMISOL CONCENTRATED INJECTION 30 mg/10 ml | Injection | Hospira Australia Pty Ltd |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

Points from the supplied literature:
- **Kidney**: pamidronate-associated collapsing focal segmental glomerulosclerosis was reported in an HIV patient (PMID 16761013), so renal function monitoring is important in this population.
- **Bone**: osteonecrosis is a recognised bisphosphonate-class concern. Monitor calcium and the risk of osteonecrosis of the jaw.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by clinical data. The only direct support is a preclinical study, and there are no registered trials of pamidronate for HIV. The HIV-related case reports describe harm, not benefit.

**Other predictions from the same run:**
- **Paget disease of bone** (score 96.6%) is an established use of pamidronate, supported by a Cochrane review of bisphosphonates. It is not a true repurposing candidate, but it could proceed with guardrails after checking the indication against the local label.
- **Paget disease of bone 2, early-onset** is an extrapolation from classic Paget disease with no disease-specific evidence.
- The other predictions (e.g. cholelithiasis, GNE myopathy, obsolete familial combined hyperlipidemia, osteomesopyknosis, feline and simian immunodeficiency) have no trials or literature and no plausible mechanism. Most appear to be knowledge-graph artifacts.

**To proceed, the following is needed:**
- The HSA package insert, including approved indications, warnings and contraindications
- Confirmed mechanism of action data from DrugBank
- Replication of the latent-reservoir reactivation findings, then a proof-of-concept study in people living with HIV
- A renal and bone safety plan for HIV patients, who are often on antiretrovirals that affect the kidney and bone

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

