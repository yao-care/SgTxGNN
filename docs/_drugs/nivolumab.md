---
layout: default
title: Nivolumab
parent: 僅模型預測 (L5)
nav_order: 711
evidence_level: L5
indication_count: 10
---

# Nivolumab
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

# Nivolumab: From Cutaneous Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Nivolumab is an anti-PD-1 immune checkpoint inhibitor whose mechanism has been established in cutaneous melanoma and other solid tumours. The TxGNN model predicts it may also be effective for **non-cutaneous melanoma** (a category spanning mucosal, acral, ocular and other rare melanoma subtypes), with **50 clinical trial records** and **8 publications** currently informing this direction, most of which are indirect (general advanced-melanoma) evidence rather than subtype-specific pivotal trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous melanoma (mechanism confirmed per evidence rationale; not derived from local license data, which is unavailable) |
| Predicted New Indication | Non-cutaneous melanoma |
| TxGNN Prediction Score | 98.41% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Nivolumab in this evidence pack. Based on known information from the evidence provided, Nivolumab is an anti-PD-1 checkpoint inhibitor that restores tumour-specific T-cell activity, and this mechanism is already well established in cutaneous melanoma.

Non-cutaneous melanoma (including mucosal, acral, uveal, amelanotic and other rare histological/anatomical subtypes) shares the same underlying melanocytic tumour biology as cutaneous melanoma, so the PD-1 blockade mechanism is theoretically transferable. However, these subtypes generally carry a lower tumour mutational burden (TMB) than UV-driven cutaneous melanoma, which is expected to translate into a lower objective response rate to checkpoint inhibition even though the mechanism itself remains applicable.

Evidence quality varies substantially across the non-cutaneous subtypes bundled under this prediction: mucosal melanoma has the most mature subtype-specific data (pooled analyses, dedicated Phase 2 trials), while subtypes such as CDK4-linked, epithelioid, balloon-cell, or lentigo maligna melanoma are supported mainly by case reports or model prediction alone. The rank-1 prediction ("non-cutaneous melanoma" as a general category) is best supported by a large national non-interventional study (n=1,087) and a completed Phase 1/2 trial in previously treated solid tumours, both of which include non-cutaneous cases within broader melanoma populations rather than as a dedicated stratum.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02593786](https://clinicaltrials.gov/study/NCT02593786) | Phase 1/2 | Completed | 58 | Nivolumab monotherapy in previously treated Chinese patients with advanced/recurrent solid tumours, including melanoma; direct single-agent efficacy/safety data |
| [NCT02990611](https://clinicaltrials.gov/study/NCT02990611) | N/A (NIS) | Completed | 1,087 | Large national non-interventional study describing safety/effectiveness of nivolumab ± ipilimumab across advanced melanoma subgroups |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EORTC randomized trial: sequential targeted therapy (encorafenib+binimetinib) then ipilimumab+nivolumab vs immediate combination immunotherapy in BRAF V600-mutant melanoma |
| [NCT05200143](https://clinicaltrials.gov/study/NCT05200143) | Phase 2 | Terminated | 4 | Triplet ipilimumab+nivolumab+cabozantinib in anti-PD-1/PD-L1 refractory cutaneous melanoma; terminated early with very small cohort |
| [NCT02599402](https://clinicaltrials.gov/study/NCT02599402) | Phase 3 | Completed | 533 | CheckMate 401: nivolumab+ipilimumab followed by nivolumab monotherapy as first-line therapy in unresectable/metastatic melanoma |
| [NCT07221734](https://clinicaltrials.gov/study/NCT07221734) | Phase 3 | Recruiting | 632 | Randomized biosimilar (MB11) vs reference Opdivo comparison in previously untreated advanced melanoma; PK/efficacy/safety/immunogenicity |
| [NCT04930783](https://clinicaltrials.gov/study/NCT04930783) | Phase 1 | Recruiting | 30 | Personalized neoantigen vaccine (NeoVax) + CDX-301 combined with nivolumab or pembrolizumab in melanoma |
| [NCT04462406](https://clinicaltrials.gov/study/NCT04462406) | Phase 2 | Active, not recruiting | 150 | Biomarker (PET/CT)-driven early discontinuation of anti-PD-1 therapy in unresectable stage IIIB-IV melanoma |
| [NCT02723006](https://clinicaltrials.gov/study/NCT02723006) | Phase 1 | Terminated | 22 | Multi-arm study of investigational agents combined with nivolumab/ipilimumab checkpoint inhibitors in advanced melanoma |
| [NCT02977052](https://clinicaltrials.gov/study/NCT02977052) | Phase 2 | Unknown | 186 | OpACIN-neo: optimal neoadjuvant dosing scheme of ipilimumab + nivolumab in stage III melanoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26841210](https://pubmed.ncbi.nlm.nih.gov/26841210/) | 2016 | Cohort | J Eur Acad Dermatol Venereol | Single-institution study directly comparing cutaneous and non-cutaneous melanoma outcomes under nivolumab treatment |
| [30510916](https://pubmed.ncbi.nlm.nih.gov/30510916/) | 2018 | Cohort (biomarker) | Frontiers in Oncology | Serum soluble CD163 evaluated as a predictive marker of nivolumab effectiveness in advanced melanoma |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohort | Current Oncology | Retrospective comparison of anti-PD-1 monotherapy vs combination with ipilimumab by age group in advanced melanoma |
| [30549256](https://pubmed.ncbi.nlm.nih.gov/30549256/) | 2019 | Cohort | Int J Rheum Dis | Investigates association between good oncological response and development of rheumatic immune-related adverse events after PD-1 inhibitor therapy |
| [28171845](https://pubmed.ncbi.nlm.nih.gov/28171845/) | 2017 | Case Report | Int J Surg Case Rep | First reported case of metastatic anorectal amelanotic (non-cutaneous) melanoma with marked response to nivolumab |
| [34176837](https://pubmed.ncbi.nlm.nih.gov/34176837/) | 2022 | Case Report | Internal Medicine (Tokyo) | Mediastinal malignant melanoma (rare non-cutaneous primary) markedly shrinking on nivolumab monotherapy |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case Report | Cureus | Metastatic melanoma in the transverse colon; systemic immunotherapy discussed as part of management |
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case Report | Pigment Cell Melanoma Res | Epidermotropic metastatic melanoma continuing to form new primary-like lesions despite adjuvant nivolumab |

---

## Singapore Market Information

Nivolumab currently has no market authorization record in Singapore (0 licenses on file), so no local product/authorization table can be presented.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — checkpoint inhibitors are not classically myelosuppressive; primary toxicity concern is immune-related adverse events (irAEs) rather than bone marrow suppression. No institution-specific toxicity data available in this evidence pack |
| Emetogenicity Classification | Low (typical for PD-1/PD-L1 checkpoint inhibitors as a class) |
| Monitoring Items | Immune-related adverse event surveillance (thyroid function, liver enzymes, renal function, colitis/diarrhea symptoms, pneumonitis, skin toxicity); baseline and periodic CBC still reasonable given limited local safety data |
| Handling Protection | Please refer to the package insert warnings and precautions; no local handling/protection data available |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The rank-1 prediction (non-cutaneous melanoma) is supported by L2-level evidence — a completed Phase 1/2 trial and a large real-world non-interventional study (n=1,087) — but this evidence largely reflects general advanced-melanoma populations rather than a dedicated non-cutaneous-melanoma trial arm, and lower TMB in non-cutaneous subtypes is expected to reduce response rates relative to cutaneous melanoma. Guardrails are warranted given this indirectness, combined with a complete absence of local (Singapore) regulatory and safety data.

**To proceed, the following is needed:**
- Local product label warnings/contraindications (currently a blocking data gap preventing initial safety screening)
- Mechanism of action (MOA) documentation to formally support the mechanistic rationale linking cutaneous and non-cutaneous melanoma
- Local market authorization assessment, since Nivolumab is not currently registered in Singapore
- Subtype-stratified efficacy data (e.g., mucosal, acral, uveal) to replace the current reliance on pooled or general advanced-melanoma cohorts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

