---
layout: default
title: Atezolizumab
parent: Medium Evidence (L3-L4)
nav_order: 117
evidence_level: L3
indication_count: 10
---

# Atezolizumab
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Atezolizumab: From Transitional Cell Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab is a PD-L1 inhibitor originally used to treat transitional cell (urothelial) carcinoma.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**,
but direct support is thin: **1 clinical trial** (a multi-tumour Phase 1b study) and **no publications** currently address this specific disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, atezolizumab is a PD-L1 inhibitor, its efficacy in urothelial carcinoma has been established, and mechanistically it may be applicable to prostatic urethra urothelial carcinoma.

Prostatic urethra urothelial carcinoma is histologically the same tumour type as the approved indication (transitional cell carcinoma), arising from the same urothelial lining but at a different anatomical site. The PD-1/PD-L1 axis rationale therefore carries over directly.

The one supporting trial is a multi-tumour Phase 1b study that includes urothelial carcinoma cohorts, so the prostatic urethra subsite is not isolated. The prediction is mechanistically sound, but site-specific evidence is lacking.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 | Active, not recruiting | 914 | Cabozantinib alone or with atezolizumab in locally advanced or metastatic solid tumours, including urothelial carcinoma (bladder, renal pelvis, ureter, urethra). Assesses safety, tolerability, preliminary efficacy and PK. Not specific to the prostatic urethra. |

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15964P | TECENTRIQ Concentrate for Solution for Infusion 840 mg/14 mL | Infusion, solution concentrate | Not listed in the compiled data |
| SIN15425P | TECENTRIQ Concentrate for Solution for Infusion 1200 mg/20 mL | Infusion, solution concentrate | Not listed in the compiled data |
| SIN17033P | TECENTRIQ Solution for Injection 1875 mg/15 mL | Injection, solution | Not listed in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Low; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert; typically includes CBC, liver, renal and thyroid function, and monitoring for immune-related adverse events |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Drug Interactions:** 75 interactions were identified in the compiled data. Examples include:
- **Major:** adalimumab, baricitinib, BCG live vaccine (Tice substrain)
- **Moderate:** systemic corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, methylprednisolone, among others), other immunosuppressants (azathioprine, alemtuzumab, anakinra, alefacept), roflumilast, and certain vaccines (tetanus toxoid, anthrax, adenovirus)

Immunosuppressants and corticosteroids may blunt the immune activation that PD-L1 blockade relies on. For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Prostatic urethra urothelial carcinoma shares its histology with the approved indication, and atezolizumab is already marketed in Singapore. However, the only trial is an early-phase, multi-tumour study with no site-specific results and no supporting publications, so this should be treated as a research question rather than a ready-to-adopt indication.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text from HSA (currently missing, which blocks safety screening)
- Mechanism of action data from DrugBank
- Subgroup or site-specific efficacy data for prostatic urethra involvement from urothelial carcinoma studies
- A review of immunosuppressant and corticosteroid co-medication in the target population

### Other Predicted Indications (Brief Note)

- **Endocervical carcinoma** has the most developed evidence among the other predictions (one completed Phase 2 trial of atezolizumab plus bevacizumab, NCT02921269, n=11; one completed Phase 1 trial, NCT03738228, n=40), but both are small early-phase studies. Its literature is a review of a different histology.
- The remaining predictions (sarcomatoid and papillary urothelial variants, uterine ligament and rare cervical adenocarcinomas) rest on model scores alone, with no trials or publications. They are on **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

