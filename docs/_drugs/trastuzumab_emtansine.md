---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 1004
evidence_level: L5
indication_count: 10
---

# Trastuzumab Emtansine
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Trastuzumab emtansine (T-DM1) is an antibody-drug conjugate originally developed and approved for HER2-positive breast cancer.
The TxGNN model predicts it may also be effective for **Progesterone-Receptor Positive Breast Cancer**,
with **4 clinical trials** and **14 publications** currently supporting this direction — though the underlying biology suggests this is a population sub-stratification of the existing approved indication rather than a genuinely novel mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (inferred from evidence-pack mechanistic rationale; no Singapore label text available — see Market Information) |
| Predicted New Indication | Progesterone-Receptor Positive Breast Cancer |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available for this drug at the drug-level field. Based on the mechanistic evidence captured in the repurposing rationale, T-DM1 is an anti-HER2 antibody-drug conjugate: trastuzumab binds HER2-overexpressing tumor cells, the complex is internalized, and the released cytotoxic payload DM1 (mertansine) disrupts microtubule assembly, triggering apoptosis. This mechanism is HER2-driven, not hormone-receptor-driven.

Progesterone-receptor (PR) status is a separate biomarker layer used to sub-classify breast cancer alongside HER2 and estrogen-receptor (ER) status. T-DM1's approved use already spans HER2-positive breast cancer regardless of PR status — meaning "progesterone-receptor positive breast cancer" is essentially a clinically-relevant subgroup within the existing HER2-positive population, not a distinct disease with a separate target pathway.

Because the drug's cytotoxic activity depends on HER2 expression rather than PR expression, applying T-DM1 to the PR-positive subgroup is mechanistically sound as long as HER2 positivity is also present. This is best understood as a **population extension of an already-established indication** rather than a novel repurposing hypothesis — which is consistent with the large volume of Phase 2–4 evidence already generated in HER2-positive populations that happen to be PR-positive.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: double-blind, placebo-controlled trial of atezolizumab + neoadjuvant AC→paclitaxel+trastuzumab+pertuzumab in early HER2-positive breast cancer; large confirmatory dataset supporting the HER2-driven regimen backbone |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | Preoperative T-DM1 + pertuzumab in early-stage HER2-positive breast cancer; examines impact of HER2 heterogeneity on treatment response |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | DECRESCENDO: de-escalation study of neoadjuvant chemo + dual HER2 blockade in HER2-positive, ER-negative, node-negative early breast cancer; terminated, limiting evidence strength |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective non-interventional study on HER2-low prevalence and treatment patterns in metastatic breast cancer; descriptive epidemiology, not efficacy evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Review | J Clin Oncol | ASCO guideline update on systemic therapy for HER2-positive advanced breast cancer, including T-DM1 as an established treatment option |
| [29939838](https://pubmed.ncbi.nlm.nih.gov/29939838/) | 2018 | Review | J Clin Oncol | ASCO clinical practice guideline update on systemic therapy for HER2-positive advanced breast cancer |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncology | Reviews current treatment trends in HR+/HER2+ breast cancer; positions T-DM1 among novel anti-HER2 agents enabling long-term disease control |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Case Report | Frontiers in Oncology | Case of HER2-positive, ER/PR-negative breast cancer with leptomeningeal disease; contextualizes HER2-targeted treatment options |
| [25873876](https://pubmed.ncbi.nlm.nih.gov/25873876/) | 2015 | Case Report | Case Reports in Oncology | Dose-reduced T-DM1 shown to be active and safe in a HER2-positive breast cancer patient with acute hepatic dysfunction |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Pending classification | Pharmacological Research | Overview of targeted and cytotoxic inhibitors in breast cancer, stratified by HER2/HR/ER/PR status |
| [35140078](https://pubmed.ncbi.nlm.nih.gov/35140078/) | 2022 | Case Report | BMJ Case Reports | Case of receptor conversion (including PR status change) with vocal cord paralysis in metastatic breast cancer |
| [40642740](https://pubmed.ncbi.nlm.nih.gov/40642740/) | 2025 | Pending classification | J Medical Cases | Long durable response with trastuzumab deruxtecan in HER2-mutant triple-negative breast cancer; discusses HER2 pathway relevance across receptor subtypes |
| [24799465](https://pubmed.ncbi.nlm.nih.gov/24799465/) | 2014 | Guideline | J Clin Oncol | ASCO clinical practice guideline on systemic therapy for HER2-positive advanced breast cancer |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guideline | Eur J Cancer | EGTM biomarker guideline: ER/PR should be measured on all invasive breast cancers; HER2 status determines eligibility for anti-HER2 therapies including T-DM1 |

---

## Singapore Market Information

Trastuzumab emtansine is **not currently registered or marketed in Singapore** — the evidence pack shows zero authorizations (`total_licenses: 0`), so no product/dosage-form/indication records are available for this jurisdiction.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Antibody-Drug Conjugate) — anti-HER2 monoclonal antibody conjugated to the cytotoxic microtubule inhibitor DM1 (mertansine) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by one completed Phase 3 trial (NCT03726879) plus multiple Phase 2 studies in HER2-positive breast cancer populations, but the PR-positive "new indication" is mechanistically an existing-indication subgroup rather than a novel repurposing hypothesis, and the drug currently has zero market authorizations in Singapore with blocking gaps in local safety/label data.

**To proceed, the following is needed:**
- Local (Singapore/HSA) package insert warnings, contraindications, and prescribing information (currently a Blocking data gap)
- Formal, structured mechanism-of-action documentation from DrugBank or equivalent source
- Confirmation that trial/literature evidence reflects genuine PR-status-stratified outcomes, not just PR status as an incidental biomarker within HER2-positive cohorts
- Regulatory pathway assessment given the drug is not currently registered in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

