---
layout: default
title: Pertuzumab
parent: Low Evidence (L5)
nav_order: 773
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From an Unspecified Original Indication (HER2-Positive Breast Cancer in Practice) to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Pertuzumab is a HER2-targeted monoclonal antibody. The Singapore registration data supplied here do not state an approved indication, so the original indication could not be confirmed from the input.
The TxGNN model predicts it may be effective for **progesterone-receptor positive breast cancer**, with **10 clinical trials** and **20 publications** retrieved.
The prediction is largely an on-label subtype of HER2-positive breast cancer rather than true repurposing, and the strongest evidence comes from HER2-positive populations, not from PR status.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied registration data (all approved indication texts are empty) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 by the rule (2 completed Phase 3 RCTs); caveat: neither trial specifically enrolled PR-positive patients |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism data were not supplied in the input. Pertuzumab is a HER2 dimerization inhibitor. It binds the extracellular domain II of HER2 and blocks HER2/HER3 heterodimerization. It acts on HER2-driven tumour biology, not on PR status.

HER2-positive breast cancer includes both hormone-receptor-negative and hormone-receptor-positive tumours. HER2+/PR+ disease is a hormone-receptor-positive subtype of HER2-positive breast cancer, so pertuzumab's mechanism applies whenever the tumour is HER2-driven. Crosstalk between HER2 and estrogen receptor signalling also motivates combining anti-HER2 therapy with endocrine therapy in this subtype.

Because the original indication and MOA fields were empty, on-label status could not be confirmed from the supplied data. Use should be restricted to confirmed HER2-positive disease. PR-positive status alone does not justify use.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Double-blind equivalence trial of a pertuzumab biosimilar (QL1209) vs reference pertuzumab with trastuzumab + docetaxel in HER2+, ER/PR-negative early or locally advanced breast cancer |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | Double-blind comparison of BCD-178 vs Perjeta as neoadjuvant therapy in HER2+ disease lacking ER and PR |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab vs placebo added to neoadjuvant chemotherapy with trastuzumab + pertuzumab in early HER2+ breast cancer |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | Randomized 4-arm neoadjuvant study comparing pathological complete response with trastuzumab, docetaxel and pertuzumab combinations |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | NEOADAPT: neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab without chemotherapy in HR+ (ER+ and/or PR+) HER2+ disease; very small enrollment |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | DECRESCENDO: chemotherapy de-escalation with SC pertuzumab/trastuzumab in HER2+, ER-negative, node-negative disease |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | T-DM1 + pertuzumab pre-operatively; impact of HER2 heterogeneity |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | TBCRC 023: lapatinib + trastuzumab ± endocrine therapy (pertuzumab link is indirect) |

Two further retrieved trials (a withdrawn Phase 2 with 0 enrolled and a retrospective HER2-low prevalence study) are omitted because they provide no efficacy data. Only NEOADAPT enrolled a PR-positive population, and it is very small.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (Phase 2) | Lancet Oncol | NeoSphere 5-year analysis. The primary analysis showed a significantly higher pathological complete response with pertuzumab + trastuzumab + docetaxel. This report covers progression-free survival, disease-free survival and safety. |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (Phase 2) | Ann Oncol | WSG-ADAPT HER2+/HR-: tests whether 12 weeks of trastuzumab + pertuzumab, with or without weekly paclitaxel, achieves comparable pCR |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (Phase 3) | Br J Cancer | Phase 3 equivalence study of pertuzumab biosimilar QL1209 vs Perjeta in HER2+, ER/PR-negative disease |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncol | WSG-TP-II: endocrine therapy + trastuzumab/pertuzumab vs de-escalated chemotherapy in HR+/ERBB2+ early breast cancer |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (Phase 2) | J Clin Oncol | PERTAIN: first-line trastuzumab + aromatase inhibitor ± pertuzumab in HER2+/HR+ metastatic or locally advanced disease (the supplied abstract states the aim only) |
| [37723497](https://pubmed.ncbi.nlm.nih.gov/37723497/) | 2023 | Retrospective | World J Surg Oncol | Real-world Chinese study; the title reports that PR status is a more decisive factor than ER status for the benefit of adding pertuzumab in HER2+/node-positive disease (hypothesis-level) |
| [40076535](https://pubmed.ncbi.nlm.nih.gov/40076535/) | 2025 | Systematic review | Int J Mol Sci | Pertuzumab + trastuzumab + docetaxel as adjuvant doublet therapy for HER2+ breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2+ breast cancer |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Review | Cancer Treat Rev | HR+/HER2+ breast cancer: about half of HER2-overexpressing tumours also express hormone receptors, with cross-talk between the pathways |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | Trial design (Phase 2) | Future Oncol | DECRESCENDO rationale: de-escalating chemotherapy in HER2+, ER-negative, node-negative early breast cancer |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14501P | PERJETA Concentrate for Solution for Infusion 420 mg/14 mL | Infusion, solution concentrate |
| SIN16247P | PHESGO Solution for Subcutaneous Injection 1200 mg/600 mg / 15 mL | Injection, solution |
| SIN16248P | PHESGO Solution for Subcutaneous Injection 600 mg/600 mg / 10 mL | Injection, solution |

The supplied data do not include approved indication text for any of these authorizations. The manufacturers are Roche Diagnostics GmbH (Perjeta) and F. Hoffmann-La Roche Ltd (Phesgo).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs and several randomized Phase 2 trials support pertuzumab-based regimens in HER2-positive breast cancer. The evidence concerns HER2 status, not PR status, and none of it is PR-specific. Of the HER2+/HR+ trials, only NEOADAPT enrolled a PR-positive population, and it had 7 patients. Use should therefore be limited to confirmed HER2-positive disease.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening): download and parse the package insert PDF from the HSA website
- Approved indication text for the three Singapore authorizations, to confirm the on-label status
- Mechanism of action data from DrugBank
- Results from the HR+/HER2+ trials (WSG-TP-II, PERTAIN, ADEPT, NEOADAPT) to define PR-positive subgroup benefit
- A cardiac and general safety monitoring plan, based on the package insert

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

