---
layout: default
title: Everolimus
parent: Low Evidence (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: Repurposing Prediction for Liposarcoma

## One-Sentence Summary

Everolimus is an oral mTOR inhibitor that is marketed in Singapore as Afinitor and Certican tablets. The TxGNN model predicts it may be useful for **liposarcoma**, and support is limited: **1 Phase 2 clinical trial** and **4 publications**, all in a combination regimen with ribociclib and only in the dedifferentiated subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 per the Evidence Pack. The only trial is a non-randomized Phase 2 combination study that is still active, so a stricter reading would rank it lower (L3–L4). |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

The registry data do not list an approved-indication text for any Singapore license, so the original indication is not shown here.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this data pack. Everolimus is known as an mTORC1 inhibitor, and the rationale below relies on that general knowledge rather than a retrieved MOA record.

Dedifferentiated liposarcoma (DDLS) shows activation of the Akt-mTOR and MAPK pathways. In a study of 99 DDLS specimens, an mTOR inhibitor also showed antitumour effects in vitro (PMID 26518767). This gives a biological reason to block mTOR in this disease.

The clinical trial pairs everolimus with ribociclib, a CDK4/6 inhibitor. CDK4 amplification is typical of dedifferentiated liposarcoma, and the two drugs showed synergistic growth inhibition in multiple tumour models. The weak point is that all support comes from this combination in one subtype. The contribution of everolimus alone cannot be separated, and nothing here supports extending the finding to other liposarcoma subtypes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B) after at least 1 prior systemic therapy. Two-centre study. The primary aim is anti-tumour activity. Started 2017, estimated completion December 2025. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 trial report | Clin Cancer Res | Report of the ribociclib + everolimus study in advanced DDL and LMS. The rationale is CDK4/6 targeting in DDL and mTOR targeting in LMS. The abstract excerpt provided does not include efficacy results. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Preclinical / tissue study | Tumour Biol | Akt-mTOR and MAPK pathways are activated in 99 dedifferentiated liposarcoma specimens. An in vitro mTOR inhibitor study was also done. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | Sarcoma PDOX mouse models used to find combination therapies with the CDK inhibitor palbociclib. It concerns CDK inhibition rather than everolimus directly. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Res | Eribulin combined with other anticancer agents in xenograft models. Eribulin is used in liposarcoma, but this paper is not about everolimus and has only indirect relevance. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN13194P | Certican Tablets 0.25 mg | Tablet |
| SIN13196P | Certican Tablets 0.5 mg | Tablet |
| SIN13195P | Certican Tablets 0.75 mg | Tablet |
| SIN13750P | Afinitor Tablet 5 mg | Tablet |
| SIN13749P | Afinitor Tablet 10 mg | Tablet |

All five products are oral tablets from Novartis. Approved-indication text was not available for any of them.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC), liver and renal function. Confirm the full list against the package insert. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. The HSA package insert has not been retrieved, and no drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The liposarcoma signal rests on a single Phase 2 combination trial in the dedifferentiated subtype, with no efficacy outcomes in the data provided. The safety review is also blocked because the package insert has not been obtained. Among the other predictions for everolimus, unclassified renal cell carcinoma (rank 9) has much stronger support: randomized Phase 2 trials against sunitinib (ASPEN and ESPN) and several single-arm studies. It is rated L2 and "Proceed with Guardrails" in the Evidence Pack, and is the better candidate to pursue first.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, interactions), which currently blocks safety screening
- Mechanism-of-action data from DrugBank
- Efficacy results (response rate, progression-free survival) from the completed NCT03114527 study and its 2024 publication
- Evidence that separates everolimus's contribution from ribociclib's, and any data beyond the dedifferentiated subtype
- Confirmation of the approved indications for the Singapore licenses

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

