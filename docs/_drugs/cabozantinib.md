---
layout: default
title: Cabozantinib
parent: Medium Evidence (L3-L4)
nav_order: 191
evidence_level: L3
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is an oral multikinase inhibitor, originally used to treat renal cell carcinoma and medullary thyroid carcinoma.
The TxGNN model predicts it may be effective for **liposarcoma**, but the evidence is thin: **1 clinical trial** (a mixed soft tissue sarcoma study) and **1 publication** (a Phase 1 study) support this direction, and neither is specific to liposarcoma.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (clear cell and non-papillary types) and medullary thyroid carcinoma (the Singapore licence records contain no indication text) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold (research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cabozantinib inhibits several receptor tyrosine kinases, including VEGFR2, MET and AXL. These pathways are involved in tumour angiogenesis, invasion and immune evasion, and they are also implicated in sarcoma biology.

Its efficacy in renal cell carcinoma is well established. Mechanistically, the same pathways could plausibly apply to soft tissue sarcomas, of which liposarcoma is one subtype. However, the available clinical signals come from general sarcoma studies, not liposarcoma-specific ones. The very high TxGNN score is therefore not yet backed by liposarcoma-specific efficacy data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, not recruiting | 66 | Randomized comparison of ipilimumab + nivolumab alone vs. with cabozantinib in advanced soft tissue sarcoma. Liposarcoma is probably a subset, but the trial is not liposarcoma-specific and no results are reported. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 trial | American Journal of Clinical Oncology | Evaluated the safety of neoadjuvant cabozantinib with radiation therapy in extremity soft tissue sarcoma. The study addressed concerns about fistula or perforation risk with concurrent radiation. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15606P | CABOMETYX Film Coated Tablet 20 mg | Film-coated tablet | Not specified in the available records |
| SIN15607P | CABOMETYX Film Coated Tablet 40 mg | Film-coated tablet | Not specified in the available records |
| SIN15608P | CABOMETYX Film Coated Tablet 60 mg | Film-coated tablet | Not specified in the available records |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; at minimum a full blood count, liver and renal function, and blood pressure are generally monitored for this drug class |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 potential interactions. Major-level interactions among those listed include acetylsalicylic acid, cisapride, clarithromycin, dolasetron, granisetron and levofloxacin. Several of these are QT-prolonging drugs, so combined use warrants caution. Moderate-level interactions include loperamide, aprepitant, dexamethasone and several laxatives (bisacodyl, castor oil, lactulose, lactitol, magnesium citrate, glycerin).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
Liposarcoma is predicted with a very high model score, but the supporting evidence is limited to one non-specific Phase 2 sarcoma trial without reported results and one Phase 1 safety study. Nothing yet shows efficacy specifically in liposarcoma.

**To proceed, the following is needed:**
- Liposarcoma-specific efficacy data, such as subtype results from the sarcoma trial above or a dedicated study
- Detailed mechanism of action data
- Package insert warnings and contraindications, which are required before safety screening can proceed
- Approved indication text for the Singapore registrations
- A review of the major drug interactions, particularly QT-prolonging drugs, for the intended population

## Other Predicted Indications Worth Noting

The model's other top predictions fall into three groups:

- **Renal cell carcinoma subtypes (supported):**
  - **Unclassified renal cell carcinoma** has the strongest subtype evidence (L2). It is supported by several Phase 2 trials of cabozantinib with nivolumab (with or without ipilimumab), plus published Phase 2 and retrospective data in non-clear cell RCC. The recommendation is Proceed with Guardrails, though the evidence is limited by small numbers and the lack of Phase 3 trials.
  - **Renal cell carcinoma with Xp11.2/TFE3 translocations** (L2, Proceed with Guardrails) rests on small Phase 2 trials in variant-histology RCC, with no subtype-specific results.
  - **Childhood kidney cell carcinoma** (L2, Research Question) has one Phase 2 pediatric trial of 109 patients with mixed tumour types and no results available.
- **Renal carcinoma (general):** Rated L1 with Phase 3 RCTs (METEOR, CheckMate 9ER, COSMIC-313). It is an established indication, so it validates the model rather than offering new repurposing evidence.
- **Unsupported predictions (Hold, L5):** Ovarian myxoid liposarcoma, renal cell carcinoma associated with neuroblastoma, amyotrophic lateral sclerosis, bilateral parasagittal parieto-occipital polymicrogyria and angiolipoma have no trials or literature. The last three have no plausible mechanistic rationale and likely reflect graph-based artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

