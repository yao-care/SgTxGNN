---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Everolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Everolimus: From Advanced Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Everolimus is a potent mTORC1 inhibitor with globally established oncology applications — including advanced renal cell carcinoma, neuroendocrine tumors, and hormone receptor-positive breast cancer — though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Liposarcoma** (specifically the dedifferentiated subtype, DDLPS), with **1 active Phase II clinical trial** and **4 publications** currently supporting this direction.
The mechanistic rationale is strong: DDLPS demonstrates consistent activation of the Akt/mTOR pathway, providing a direct biological basis for targeting with an mTOR inhibitor.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced renal cell carcinoma (globally approved; not registered in Singapore) |
| Predicted New Indication | Liposarcoma (Dedifferentiated subtype, DDLPS) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Everolimus functions as a selective inhibitor of mTORC1 (mechanistic target of rapamycin complex 1), a master regulator of cell growth, protein synthesis, autophagy, and angiogenesis. By blocking mTORC1, everolimus suppresses tumor cell proliferation and reduces production of hypoxia-inducible factor-1α (HIF-1α), thereby impairing tumor vasculature. This mechanism is well-established across multiple solid tumors and represents the drug's core oncologic rationale.

Dedifferentiated liposarcoma (DDLPS) is a clinically aggressive soft tissue sarcoma for which chemotherapy remains the standard of care but offers limited benefit. Immunohistochemical and in vitro analyses of 99 DDLPS specimens (PMID 26518767) demonstrate significant activation of both the Akt/mTOR and MAPK signaling pathways — precisely the nodes that everolimus targets. In addition, DDLPS harbors characteristic amplification of chromosome 12q13-15, which co-amplifies CDK4 alongside MDM2, making CDK4/6-dependent cell cycle progression a parallel vulnerability. Blocking both the mTOR survival axis (via everolimus) and CDK4/6-driven proliferation (via ribociclib) creates mechanistic synergy demonstrated in multiple preclinical tumor models.

This convergence of mTOR pathway activation in DDLPS and the availability of a selective mTORC1 inhibitor makes the TxGNN prediction scientifically coherent. The ongoing Phase II trial NCT03114527 is directly testing this hypothesis in a clinical setting, translating the preclinical rationale into prospective human data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase II | Active, Not Recruiting | 48 | Two-arm study of Ribociclib (300 mg/day, 3 weeks on/1 week off) + Everolimus (2.5 mg) in advanced DDL (Arm A) and LMS (Arm B) with ≥1 prior systemic therapy; evaluates anti-tumor activity of this CDK4/6 + mTOR dual blockade |
| [NCT01216839](https://clinicaltrials.gov/study/NCT01216839) | Phase II | Unknown | 20 | Everolimus monotherapy in children and adolescents with refractory/relapsed rhabdomyosarcoma and other soft tissue sarcomas (includes sarcoma class broadly) |
| [NCT00187174](https://clinicaltrials.gov/study/NCT00187174) | Phase I | Completed | 41 | RAD001 (Everolimus) in pediatric recurrent/refractory solid tumors; established safety and tolerability profile supporting sarcoma-context use |
| [NCT03245151](https://clinicaltrials.gov/study/NCT03245151) | Phase I/II | Completed | 64 | Lenvatinib + Everolimus in recurrent/refractory pediatric solid tumors; RP2D established, antitumor activity evaluated across sarcoma and other histologies (results published 2025, PMID 40313040) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase II Trial Report (SAR-096) | Clinical Cancer Research | Reports results of the Ribociclib + Everolimus Phase II trial in advanced DDL and LMS; CDK4/6 + mTOR dual blockade shown to have synergistic growth inhibition in preclinical models, with this trial providing the first dedicated clinical evaluation in DDLPS |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translational/Mechanistic | Tumour Biology | IHC analysis of 99 DDLPS specimens confirms significant activation of Akt/mTOR and MAPK pathways; in vitro study demonstrates antitumor effect of mTOR inhibitor in DDLPS cell lines — key mechanistic rationale for everolimus use |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (Preclinical PDOX Models) | Frontiers in Oncology | Review of patient-derived orthotopic xenograft (PDOX) models for sarcoma; CDK inhibitors (palbociclib and related agents) show effective combination activity; provides broader preclinical framework for CDK + mTOR targeting in sarcoma |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical Combination Study | Anticancer Research | Eribulin combined with mechanistically distinct anticancer agents (including mTOR pathway agents) evaluated against liposarcoma xenograft models; supports multi-agent approach for liposarcoma treatment |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — mTORC1 inhibitor (rapalog class); not conventional cytotoxic |
| Myelosuppression Risk | Low to moderate (anemia, thrombocytopenia, and neutropenia reported but less severe than conventional chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, serum creatinine and BUN, fasting blood glucose, serum triglycerides and cholesterol, pulmonary function (risk of non-infectious pneumonitis), hepatic function |
| Handling Protection | Standard oral targeted therapy handling applies; classified as hazardous drug — cytotoxic handling precautions recommended per institutional policy |

---

## Safety Considerations

Formal safety data (warnings, contraindications, drug-drug interactions) was not retrievable from Singapore-registered prescribing information, as Everolimus is currently not registered in Singapore.

Please refer to the originator package insert (Afinitor® / Votubia® / Certican®) and/or EMA/FDA prescribing information for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for Everolimus in liposarcoma is supported by a direct mechanistic link (confirmed mTOR pathway activation in DDLPS tissue specimens), a published Phase II trial result (SAR-096, PMID 37967116), and an actively recruiting Phase II study (NCT03114527) testing the Ribociclib + Everolimus combination in exactly this population. The evidence reaches L2, making this the strongest repurposing signal in the cohort.

**To proceed, the following is needed:**

- **Regulatory pathway clarification**: Everolimus is not registered in Singapore — a compassionate use, clinical trial import, or parallel import pathway must be identified before any patient-level access
- **MOA formal documentation**: Retrieve DrugBank/prescribing information to formally document the mTOR mechanism and complete the S1 safety screen (currently flagged as Blocking gap DG001/DG002)
- **Safety profile review**: Obtain and review full Singapore-applicable package insert or EMA Summary of Product Characteristics (SmPC) to document contraindications, key warnings (particularly non-infectious pneumonitis, hyperglycemia, immunosuppression), and significant drug interactions
- **Results from NCT03114527**: Monitor publication of the SAR-096 Phase II results for the DDL arm (Arm A) specifically — current PMID 37967116 may represent interim or partial data; full results will determine whether this advances to S3 or above
- **Patient selection criteria**: Define subtype-specific inclusion (DDLPS vs. other liposarcoma subtypes) and confirm CDK4 amplification status as a potential biomarker for patient selection in any local protocol development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

