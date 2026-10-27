---
layout: default
title: Eravacycline
parent: Low Evidence (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eravacycline: predicted new indication Bronchitis (evidence level L5). Approved use: Not stated in the registration data compiled for this report"
monitor_inn: "Eravacycline"
predicted_indications: ["bronchitis", "laryngotracheitis", "bronchial neoplasm (disease)", "conjunctivitis", "sclerosing cholangitis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "rheumatoid arthritis"]
---

# Eravacycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Eravacycline: From Antibacterial Therapy to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Eravacycline is a fluorocycline tetracycline-class intravenous antibiotic that is marketed in Singapore as XERAVA.
The TxGNN model predicts it may be effective for **bronchitis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so it remains a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 96.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, eravacycline is a tetracycline-class antibiotic (a fluorocycline) with broad-spectrum activity against Gram-positive, Gram-negative and anaerobic bacteria. Its antibacterial action is understood to come from inhibiting bacterial protein synthesis at the 30S ribosomal subunit, and it is generally positioned as a reserve-class intravenous agent. The registration data do not list an approved indication.

Bacterial bronchitis or lower respiratory tract infection is mechanistically plausible for a broad-spectrum antibiotic, which likely explains the high TxGNN score. However, there are important limits:

- No clinical trials or literature were found for this indication.
- Its lung penetration and clinical efficacy in respiratory infection are not established in the data.
- Most acute bronchitis is viral, so any antibiotic benefit would be limited to selected bacterial cases.
- Using a reserve-class IV antibiotic for a mostly self-limiting condition would raise antimicrobial stewardship concerns.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15930P | XERAVA Powder for Concentrate for Solution for Infusion 50 mg per vial | Injection, powder, lyophilized, for solution | Not stated in the registration data |

## Safety Considerations

- **Drug Interactions**: 24 interactions were identified in the interaction database; 20 are itemised in the data compiled for this report. Key ones:
  - **Major**: Vitamin A, isotretinoin, acitretin, tretinoin, bexarotene (retinoids, a recognised concern with tetracyclines because of the risk of raised intracranial pressure), as well as lumacaftor, apalutamide and mitotane.
  - **Moderate**: Warfarin, dicoumarol, ethinylestradiol, picosulfuric acid, methoxsalen, mycophenolic acid, topical aminolevulinic acid and methyl aminolevulinate.
  - **Minor**: Clarithromycin, cobicistat, ketoconazole, ceritinib.

Other safety information (key warnings and contraindications) was not available; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on model score alone (L5), with no clinical trials or publications. Most bronchitis is viral, and using a reserve-class IV antibiotic for it raises stewardship concerns. Safety label information is also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA), so safety screening can be completed
- Approved indication text for the Singapore registration
- Mechanism of action data and lung-tissue penetration data
- Clinical or microbiological evidence in bacterial lower respiratory tract infection
- Confirmation of route compatibility (the only available form is intravenous)

### Other Predicted Indications (for reference)

All have no trials or literature (L5):

| Rank | Predicted Indication | Score | Recommendation |
|---|---|---|---|
| 2 | Laryngotracheitis | 86.51% | Hold |
| 3 | Bronchial neoplasm | 85.97% | Hold |
| 4 | Conjunctivitis | 85.88% | Hold |
| 5 | Sclerosing cholangitis | 84.42% | Research Question |
| 6 | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 77.54% | Hold |
| 7 | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 77.46% | Hold |
| 8 | Brain small vessel disease 1 with or without ocular anomalies | 76.50% | Hold |
| 9 | Diabetic nephropathy | 76.05% | Hold |
| 10 | Rheumatoid arthritis | 73.27% | Research Question |

Of these, sclerosing cholangitis and rheumatoid arthritis have some class-level biological plausibility from other tetracyclines, but no eravacycline-specific data. The rare genetic disorders (ranks 6–8) have no plausible antibacterial mechanism and likely reflect knowledge-graph artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

