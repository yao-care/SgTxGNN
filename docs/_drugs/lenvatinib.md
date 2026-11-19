---
layout: default
title: Lenvatinib
parent: Medium Evidence (L3-L4)
nav_order: 587
evidence_level: L3
indication_count: 5
last_modified_at: 2026-11-20
monitor_inn: "Lenvatinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "angiolipoma", "familial spontaneous pneumothorax", "endocrine-cerebro-osteodysplasia syndrome"]
description: "Lenvatinib: predicted new indication Liposarcoma (evidence level L3). In Singapore: 2 HSA registrations (2 valid)"
---

# Lenvatinib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **5** 
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

## Lenvatinib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Lenvatinib is an oral multi-targeted tyrosine kinase inhibitor that blocks tumour blood-vessel growth and proliferative signalling.
The TxGNN model predicts it may be effective for **liposarcoma**, with **1 clinical trial** and **1 single-arm phase Ib/II publication** directly addressing this disease (evidence level **L3**).
No randomised trial exists yet.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L3 |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lenvatinib: "Lenvatinib is a kinase inhibitor that inhibits the kinase activities of vascular endothelial growth factor (VEGF) receptors VEGFR1 (FLT1), VEGFR2 (KDR), and VEGFR3 (FLT4). Lenvatinib inhibits other kinases that have been implicated in pathogenic angiogenesis, tumor growth, and cancer progression in addition to their normal cellular functions, including fibroblast growth factor (FGF) receptors FGFR1, 2, 3, and 4; platelet derived growth factor receptor alpha (PDGFRA), KIT, and RET." ([DailyMed: Lenvima (lenvatinib) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4bedd21-efde-44c6-9d9c-b48b78d7ed1e), label version 2026-10-14; accessed 2026-11-19.) Based on general knowledge, lenvatinib inhibits several receptor tyrosine kinases (VEGFR1-3, FGFR1-4, PDGFRα, RET, KIT). This suppresses tumour angiogenesis and proliferative signalling, which are relevant in many solid tumours.

Liposarcoma is a soft tissue sarcoma that depends on blood supply and growth-factor signalling. Combined with eribulin, a microtubule inhibitor, lenvatinib showed activity in advanced liposarcoma and leiomyosarcoma in a clinical study. CDK4 amplification, common in well-differentiated and dedifferentiated liposarcoma, is discussed in the literature as a context for synergistic inhibition.

The mechanistic reasoning above is inferred rather than drawn from recorded mechanism data, so it should be treated as supportive, not confirmatory.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/Phase 2 | Completed | 30 | Single-arm study (LEADER) of lenvatinib plus eribulin in inoperable or metastatic adipocytic sarcoma and leiomyosarcoma, testing safety and efficacy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase Ib/II single-arm trial | Clinical Cancer Research | LEADER study of lenvatinib plus eribulin in advanced liposarcoma and leiomyosarcoma, where treatment options are limited |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical/biomarker study | Experimental Hematology & Oncology | CDK4 as a prognostic biomarker in soft tissue sarcoma and synergy of its inhibition in dedifferentiated liposarcoma |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical study | Anticancer Research | Eribulin combined with mechanistically different anticancer agents showed broad preclinical antitumour activity |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case report | Case Reports in Oncology | Tumour shrinkage in a dedifferentiated liposarcoma patient with lung metastasis given individualised multimodal treatment |

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN14982P | LENVIMA HARD CAPSULE 4MG | CAPSULE | Valid |
| SIN14983P | LENVIMA HARD CAPSULES 10 MG | CAPSULE | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; routine blood counts, liver and renal function are generally advisable |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screen. Examples at the **Major** level are dolasetron and cisapride. Many **Moderate** interactions were listed, including famotidine, loperamide, clarithromycin, levofloxacin, granisetron, palonosetron, naltrexone, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, sodium sulfate, magnesium citrate, magnesium hydroxide, lactulose, lactitol, glycerin, castor oil). Metronidazole is listed as **Minor**.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L3. It rests on one completed single-arm phase Ib/II study (NCT03526679; PMID 36129471) of lenvatinib plus eribulin that directly addresses liposarcoma. There is no randomised trial. The prediction score is high (0.9951), but the evidence is small and non-randomised, so use should stay within a research setting.

**To proceed, the following is needed:**
- A randomised or larger controlled study in liposarcoma
- Detailed mechanism of action data
- Package insert warnings and contraindications, which are not available in the data compiled for this report
- A review of the Major-level interactions, particularly QT-prolonging agents such as dolasetron and cisapride, before any use
- A safety monitoring plan for the lenvatinib plus eribulin combination

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lenvima (lenvatinib) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4bedd21-efde-44c6-9d9c-b48b78d7ed1e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

