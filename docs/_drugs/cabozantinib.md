---
layout: default
title: Cabozantinib
parent: Medium Evidence (L3-L4)
nav_order: 190
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

Cabozantinib is an oral multi-kinase inhibitor that is marketed in Singapore as CABOMETYX. The evidence pack links it to renal cell carcinoma but does not record the Singapore label indication text.
The TxGNN model predicts it may be effective for **liposarcoma**, but only **1 clinical trial** (a soft tissue sarcoma trial with no reported results) and **1 publication** (a Phase 1 safety study) currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (inferred from the clinical evidence in the pack; the HSA indication text is blank) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cabozantinib inhibits VEGFR2, MET and AXL. These kinases are implicated in tumour angiogenesis and immune evasion in sarcoma. Detailed mechanism of action data is not available in the source record. The mechanism above comes from the pack's repurposing rationale.

Kidney cancer and sarcoma are both solid tumours that depend on new blood vessel growth. Cabozantinib is established in renal cell carcinoma, and a Phase 1 publication notes it "demonstrates activity in multiple soft tissue sarcoma subtypes". That gives the prediction some biological plausibility.

The evidence is still indirect. The only Phase 2 trial covers soft tissue sarcoma broadly, so liposarcoma is likely a subgroup. The very high TxGNN score (0.998) is a model prediction and has not been confirmed clinically for this histology.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, not recruiting | 66 | Randomised comparison of ipilimumab + nivolumab alone versus combined with cabozantinib in advanced soft tissue sarcoma. No results are available yet, and liposarcoma is likely only a subgroup. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 trial | Am J Clin Oncol | Evaluated the safety of neoadjuvant cabozantinib combined with radiation therapy in extremity soft tissue sarcoma. Combining the two had been limited by concern about fistula or perforation. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15606P | CABOMETYX Film Coated Tablet 20 mg | Tablet, film coated |
| SIN15607P | CABOMETYX Film Coated Tablet 40 mg | Tablet, film coated |
| SIN15608P | CABOMETYX Film Coated Tablet 60 mg | Tablet, film coated |

The manufacturers are Patheon Inc. and Rottendorf Pharma GmbH. The route is oral.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR2, MET, AXL) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count, liver and renal function, blood pressure and electrolytes, as generally applied to this drug class |
| Handling Protection | Follow institutional hazardous-drug handling policy for oral anticancer agents |

## Safety Considerations

Please refer to the package insert for safety information.

One safety point from the literature: concurrent use with radiation therapy has raised concern about fistula or perforation, which is the reason for the Phase 1 study above.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the only supporting trial is a broad soft tissue sarcoma study with no reported results. The only publication is a Phase 1 safety study. There is no liposarcoma-specific efficacy evidence.

**To proceed, the following is needed:**
- Results from NCT05836571, with a liposarcoma subgroup analysis
- Efficacy data from Phase 2 or later studies in liposarcoma
- HSA package insert warnings, contraindications and the approved indication text
- Mechanism of action data confirmed against DrugBank
- A safety plan for any radiation combination (fistula and perforation risk)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

