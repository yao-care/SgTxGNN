---
layout: default
title: Labetalol
parent: Low Evidence (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
---

# Labetalol
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

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Labetalol is an alpha- and beta-blocking antihypertensive, marketed in Singapore as an injection and a tablet.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**.
Currently there are **0 clinical trials** and only **2 case reports** supporting this direction, so it is a research question rather than an established use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the approved indication text in the Singapore registrations is blank; hypertension is inferred from the drug class) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 (case reports only, no trials) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known pharmacology, labetalol combines alpha-1 and non-selective beta blockade, which lowers vascular resistance and heart rate. It is already used clinically in hypertensive emergencies.

Renovascular hypertension is driven by the renin-angiotensin system, so beta-blockade, which reduces renin release, may add benefit. In that sense, the predicted indication is a more severe and more specific form of the condition the drug is already used for.

The TxGNN score is very high (rank 9,960 in the model), but the same score is given to the neighbouring entry "malignant hypertensive renal disease". This suggests a shared graph neighbourhood rather than independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | Med J Aust | A 20-year-old man with malignant hypertension and renal arteritis after hallucinogen use. Blood pressure was controlled initially with minoxidil and labetalol, and the arteritis resolved with prednisone. |
| [15113447](https://pubmed.ncbi.nlm.nih.gov/15113447/) | 2004 | Case report | BMC Nephrol | An 18-month-old child with hyponatremic hypertensive syndrome presenting as malignant hypertension. The abstract provided does not mention labetalol. |

Both are single-patient reports. They do not show that labetalol is effective for this condition.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN02281P | TRANDATE INJECTION 100 mg/20 ml (UBI Pharma Inc) | Injection |
| SIN05162P | TRANTALOL TABLET 100 mg (Duopharma (M) Sdn Bhd) | Tablet |

Both routes (injectable and oral) are available. Approved indication text is not listed in the registration records.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible, and labetalol is already used in severe hypertension. However, evidence consists only of two case reports, with no clinical trials. The high model score is shared with a neighbouring entry and is not independently corroborated.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications) to complete safety screening
- Confirmed mechanism of action data from DrugBank
- Controlled or observational data on labetalol in renovascular or malignant hypertension
- Confirmation of the registered indication text for both Singapore licences

Of the other predicted indications, open-angle glaucoma has slightly more direct support (a 1981 study reporting an ocular hypotensive effect in rabbit and human eyes), but this is early, small-scale evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

