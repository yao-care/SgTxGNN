---
layout: default
title: Regorafenib
parent: Low Evidence (L5)
nav_order: 849
evidence_level: L5
indication_count: 10
---

# Regorafenib
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

# Regorafenib: From Refractory Colorectal Cancer and GIST to Liposarcoma

## One-Sentence Summary

Regorafenib is an oral multikinase inhibitor. Published abstracts describe activity in refractory gastrointestinal stromal tumours (GIST) and chemotherapy-refractory colorectal cancer. The TxGNN model predicts it may be effective for **liposarcoma**, with **2 clinical trials** and **9 publications** linked. However, the liposarcoma-specific randomized results are negative, so the prediction is not supported clinically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record. Literature describes refractory GIST and refractory colorectal cancer. |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 (Phase 2 randomized placebo-controlled evidence exists, but it does not support benefit in liposarcoma) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Regorafenib blocks several kinases: VEGFR1-3, TIE2, PDGFR, FGFR, KIT, RET and RAF. Blocking angiogenic and stromal kinase signalling is a plausible approach in soft tissue sarcoma. The model's high score fits this idea. Detailed mechanism-of-action data were not supplied in the DrugBank record, so this description comes from the evidence summary.

Liposarcoma is a soft tissue sarcoma, and regorafenib has been tested in this tumour class. However, activity within soft tissue sarcoma depends on histology. The REGOSARC trial reported efficacy in leiomyosarcoma, synovial sarcoma and other non-adipocytic sarcomas, but not in liposarcoma. The SARC024 liposarcoma cohort reached a similar conclusion and did not support routine use of regorafenib in this population. The mechanism is therefore plausible, but the clinical data for this specific histology are unfavourable.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | REGOSARC: randomized, double-blind, placebo-controlled trial in metastatic soft tissue sarcoma after anthracycline failure, with a dedicated liposarcoma cohort. Published analyses show benefit in non-adipocytic sarcomas but not in liposarcoma. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol across selected sarcoma subtypes. Its liposarcoma cohort (PMID 32701199) did not support routine use of regorafenib. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT (Phase 2) | The Oncologist | SARC024 liposarcoma cohort: confirms earlier data and does not support routine use of regorafenib in treatment-refractory liposarcoma. |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT (Phase 2) | The Lancet Oncology | REGOSARC primary report of safety and efficacy in anthracycline-pretreated metastatic soft tissue sarcoma. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT (updated analysis) | European Journal of Cancer | Efficacy in leiomyosarcoma, synovial and other non-adipocytic sarcoma, but not in liposarcoma. Includes post-cross-over regorafenib activity. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Secondary analysis | Cancer | Quality-adjusted time without symptoms or toxicity (Q-TWiST) analysis of REGOSARC in doxorubicin-pretreated non-adipocytic sarcoma. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial protocol | BMC Cancer | REGOSARC study protocol (no results). |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Overview of regorafenib's growing role in sarcoma treatment. |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | Maintenance therapy after first-line treatment in advanced soft tissue sarcoma. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study (different drug) | Anti-Cancer Drugs | Anlotinib in well-differentiated/dedifferentiated liposarcoma. Class-level context only. |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Case report (different drug) | Rare Tumors | Pazopanib activity in extraosseous Ewing sarcoma. Provided rationale for the SARC024 design. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14360P | Stivarga Tablet 40mg (Bayer AG, Leverkusen) | Tablet, film coated | Not listed in the supplied record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Typically blood counts, liver function and blood pressure. Confirm against the package insert. |
| Handling Protection | Oral film-coated tablet. Follow local hazardous drug handling policy and the package insert. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Phase 2 randomized evidence exists, but it points against benefit in liposarcoma. Both REGOSARC and the SARC024 liposarcoma cohort failed to support use in this histology. A high model score does not outweigh this.

**To proceed, the following is needed:**
- Review the full REGOSARC and SARC024 liposarcoma-cohort results to confirm the negative findings.
- Obtain the Singapore package insert, covering indications, warnings and contraindications.
- Retrieve mechanism-of-action data from DrugBank.
- Consider redirecting effort to **renal cell carcinoma**, where a Phase 2 single-arm trial (NCT00664326, PMID 22959186) shows direct activity. Any niche there, such as later-line use or checkpoint-inhibitor combinations, would need to be defined first.
- Treat the other liposarcoma and RCC subtype predictions (ovarian myxoid, spindle cell, TFE3-fusion and similar) as unsupported. They appear to be propagated from parent nodes and have no linked trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

