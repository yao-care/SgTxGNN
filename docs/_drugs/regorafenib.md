---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 849
evidence_level: L5
indication_count: 10
---

# Regorafenib
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

# Regorafenib: From Metastatic Colorectal Cancer to Liposarcoma

## One-Sentence Summary

> Regorafenib is an oral multikinase inhibitor globally approved for refractory metastatic colorectal cancer, gastrointestinal stromal tumour (GIST), and hepatocellular carcinoma.
> The TxGNN model predicts it may be effective for **Liposarcoma**,
> with **2 completed Phase 2 clinical trials** and **9 publications** currently available — however, both completed trials specifically failed to show benefit in the liposarcoma subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (drug not marketed); globally approved for metastatic colorectal cancer, GIST, and hepatocellular carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 (2 completed Phase 2 RCTs specific to liposarcoma) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data for regorafenib is not available in this evidence pack (data gap). However, mechanistic annotations elsewhere in the pack describe regorafenib as an oral multikinase inhibitor targeting VEGFR1–3, PDGFR, RET, KIT, and RAF — producing anti-angiogenic and antiproliferative effects. This is consistent with regorafenib's known real-world approvals for GIST and metastatic colorectal cancer, both of which rely on disruption of tumour angiogenesis and stromal kinase signalling.

Liposarcoma and other soft-tissue sarcomas (STS) share biological dependence on angiogenic and receptor tyrosine kinase pathways, which is why related multitargeted TKIs (pazopanib, sorafenib) have been explored or approved in this disease group. This mechanistic rationale is why regorafenib has been formally tested in liposarcoma in two independent randomized trials (REGOSARC, SARC024).

**Important caveat**: despite the strong mechanistic rationale and very high TxGNN score, the actual completed clinical evidence in liposarcoma specifically is **negative**. The REGOSARC trial (NCT01900743) showed regorafenib was effective in leiomyosarcoma and synovial sarcoma, but *not* in the liposarcoma cohort. The SARC024 liposarcoma cohort (NCT02048371) similarly did not support routine use of regorafenib in this population. This is a case where a high AI prediction score is not corroborated — and is actively contradicted — by downstream clinical trial evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | REGOSARC — randomized, double-blind, placebo-controlled trial in anthracycline-refractory metastatic STS across 5 cohorts (including Cohort A: liposarcoma). Regorafenib improved outcomes in leiomyosarcoma, synovial sarcoma, and other non-adipocytic sarcomas, **but not in the liposarcoma cohort**. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 — basket protocol testing oral regorafenib across selected sarcoma subtypes; the liposarcoma cohort results did **not support routine use** of regorafenib in this population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | Lancet Oncology | REGOSARC primary results: regorafenib improved progression-free survival in doxorubicin-refractory advanced STS, driven mainly by non-adipocytic subtypes. |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarcoma cohort results confirm lack of benefit; routine use of regorafenib in treatment-refractory liposarcoma is not supported. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT (updated/crossover analysis) | European Journal of Cancer | Updated REGOSARC analysis confirms efficacy in leiomyosarcoma/synovial sarcoma but not liposarcoma, including post-crossover activity data. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Post-hoc analysis (RCT) | Cancer | Q-TWiST analysis of REGOSARC showing quality-adjusted time benefit for regorafenib in non-adipocytic STS. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Study Protocol | BMC Cancer | Describes REGOSARC trial design and rationale based on angiogenesis signaling in sarcoma biology. |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Reviews regorafenib's growing role across STS subtypes, including liposarcoma, leiomyosarcoma, and GIST. |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | Reviews maintenance therapy strategies after first-line treatment for advanced STS, including TKI-based approaches. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study (different drug: anlotinib) | Anti-Cancer Drugs | Notes regorafenib and pazopanib as approved TKIs for non-adipocytic STS, contextualizing anlotinib's activity in liposarcoma. |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Case report (different drug: pazopanib) | Rare Tumors | Case of pazopanib activity in Ewing sarcoma, cited as rationale for testing regorafenib across sarcoma subtypes in SARC024. |

---

## Singapore Market Information

Regorafenib currently has **no registration records** in Singapore — the drug is not marketed and no HSA authorization data is available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral multikinase/VEGFR inhibitor), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns liposarcoma a very high prediction score (99.76%), the two completed randomized Phase 2 trials that directly tested regorafenib in liposarcoma (REGOSARC, SARC024) both failed to demonstrate efficacy in this specific subtype — this is a case where clinical trial evidence overturns the model prediction. Regorafenib is also not currently registered in Singapore.

**To proceed, the following is needed:**
- Confirm whether any newer trials or biomarker-selected liposarcoma subpopulations show a positive signal
- Obtain official MOA and TFDA/HSA-equivalent label safety data (currently data gaps: DG001, DG002)
- Consider redirecting evaluation toward non-adipocytic STS subtypes (leiomyosarcoma, synovial sarcoma) where REGOSARC showed actual clinical benefit
- Singapore HSA registration status and route-of-administration confirmation if repurposing is pursued for any STS indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

