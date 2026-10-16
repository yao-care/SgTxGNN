---
layout: default
title: Framycetin
parent: Low Evidence (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Framycetin: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not available (the registered approved-indication text is empty)"
monitor_inn: "Framycetin"
predicted_indications: ["sclerosing cholangitis", "urinary tract infection (disease)", "congenital prothrombin deficiency", "Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "bronchitis", "genital herpes", "vitamin deficiency disorder"]
---

# Framycetin
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

# Framycetin: From an Unspecified Original Indication to Sclerosing Cholangitis

## One-Sentence Summary

Framycetin is an aminoglycoside antibiotic marketed in Singapore as a topical ointment (PROCTOSEDYL OINTMENT), but the approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, with a very high score, but **no clinical trials and no publications** currently support this direction.
This is a model prediction only (evidence level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the registered approved-indication text is empty) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, framycetin is an aminoglycoside antibiotic with poor systemic absorption. Aminoglycosides generally act against Gram-negative bacteria, and mechanistically it may be applicable to conditions involving gut bacteria.

A gut-restricted antibacterial could theoretically influence the gut-liver axis. A comparable idea has been explored with oral vancomycin in primary sclerosing cholangitis. However, there is no framycetin-specific or aminoglycoside-specific data in this disease. The high TxGNN score is a computational prediction and should not be read as evidence of efficacy.

For context, the other top predictions are:

| Rank | Predicted Indication | Score | Plausibility |
|---|---|---|---|
| 2 | Urinary tract infection | 99.42% | Plausible class activity; urinary exposure uncertain, nephrotoxicity concern |
| 3 | Congenital prothrombin deficiency | 99.41% | No plausible mechanism; likely model artifact |
| 4 | Ureaplasma urethritis | 99.28% | Weak; aminoglycosides have limited activity |
| 5 | Gonococcal urethritis | 99.28% | Class-level rationale only |
| 6 | Uterine inflammatory disease | 99.18% | Class-level plausibility only |
| 7 | Xanthogranulomatous pyelonephritis | 99.18% | Nephrotoxicity concern; surgical management usual |
| 8 | Bronchitis | 98.95% | One historical 1956 report; weak support |
| 9 | Genital herpes | 98.66% | Viral; no antiviral activity expected |
| 10 | Vitamin deficiency disorder | 96.79% | Likely spurious; could worsen deficiency |

## Literature Evidence

No literature is available for the top predicted indication (sclerosing cholangitis). The only publication retrieved across the predictions relates to a lower-ranked indication, bronchitis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13316238](https://pubmed.ncbi.nlm.nih.gov/13316238/) | 1956 | Other (historical clinical report, design unclear) | Bruxelles Medical | "Trial therapy with new antibiotic framycetin in pneumology"; no abstract available, so findings cannot be verified |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN01718P | PROCTOSEDYL OINTMENT | Ointment | Not available |

## Safety Considerations

- **Class-related concerns (from the prediction rationales):** Systemic aminoglycoside use is limited by nephrotoxicity and ototoxicity. Oral aminoglycosides can alter gut flora and cause malabsorption.
- No drug-interaction records were found.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for sclerosing cholangitis rests on model output alone, with no clinical trials or literature, and the mechanistic argument is only by analogy to another gut-restricted antibiotic. The Singapore product is a topical ointment, so route compatibility with a hepatobiliary indication is unestablished.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Approved indication text for the Singapore licence
- Mechanism of action data (for example, from DrugBank)
- Preclinical or clinical evidence for aminoglycosides in sclerosing cholangitis, and a route and exposure assessment (for example, oral gut-restricted versus topical)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

