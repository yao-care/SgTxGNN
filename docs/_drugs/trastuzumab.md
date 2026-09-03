---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 1002
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Trastuzumab is a humanized anti-HER2 (ERBB2) monoclonal antibody already established as standard-of-care therapy for HER2-overexpressing breast cancer. The TxGNN model predicts efficacy in **progesterone-receptor (PR) positive breast cancer**, supported by **36 clinical trials** (including multiple completed Phase 3 RCTs) and **20 publications**. However, the underlying evidence indicates this is largely a restatement of trastuzumab's existing HER2-positive indication rather than a genuinely novel repurposing signal — PR status is a co-occurring molecular marker, not the mechanistic driver of response, so HER2 confirmation should gate any use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (established standard of care; not extractable from Singapore registration data as the product is currently unregistered locally) |
| Predicted New Indication | Progesterone-Receptor Positive Breast Cancer |
| TxGNN Prediction Score | 99.90% (rank 1913) |
| Evidence Level | L1 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal DrugBank-sourced mechanism-of-action record is not available (flagged as a High-severity data gap, DG002). Based on the mechanistic rationale captured in the evidence pack, trastuzumab is a humanized monoclonal antibody directed against HER2/neu (ERBB2). It blocks HER2-mediated downstream signaling and triggers antibody-dependent cellular cytotoxicity (ADCC) against HER2-overexpressing tumor cells.

The predicted indication — PR-positive breast cancer — is labeled by progesterone-receptor status rather than HER2 status. In practice, however, response to trastuzumab is determined by HER2 amplification/overexpression, and PR status is simply a co-occurring molecular classifier used alongside ER/HER2 in breast cancer subtyping (e.g., "triple-positive" ER+/PR+/HER2+ tumors). Trastuzumab is already the standard of care for HER2-positive breast cancer irrespective of PR status, meaning this TxGNN prediction largely reflects an already-validated core indication rather than a true repurposing signal.

Because of this, the mechanistic plausibility is high, but the clinical value of the "new indication" label is limited unless it is explicitly interpreted as **HER2-positive/PR-positive breast cancer**, with HER2 IHC/FISH confirmation used as the eligibility guardrail rather than PR status alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant chemotherapy ± trastuzumab in node-positive/high-risk node-negative HER2-low invasive breast cancer |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Double-blind RCT of QL1209 (anti-HER2 biosimilar) + trastuzumab + docetaxel vs pertuzumab + trastuzumab + docetaxel in HER2+/ER-PR-negative early/locally advanced breast cancer |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Completed | 3,436 | AC followed by weekly paclitaxel ± trastuzumab as adjuvant treatment for HER2-overexpressing node-positive/high-risk breast cancer |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab vs placebo with neoadjuvant chemo + trastuzumab + pertuzumab in early HER2+ breast cancer |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane-based chemo + lapatinib vs + trastuzumab as first-line therapy in HER2+ metastatic breast cancer |
| [NCT04420598](https://clinicaltrials.gov/study/NCT04420598) | Phase 2 | Completed | 41 | Trastuzumab deruxtecan (T-DXd) in HER2+ advanced breast cancer with brain metastases/leptomeningeal carcinomatosis |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Letrozole + trastuzumab in HER2+/ER- and/or PR-positive metastatic breast cancer |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Neoadjuvant neratinib + aromatase inhibitor + trastuzumab in ER+/HER2+ breast cancer |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Completed | 37 | Everolimus + trastuzumab + letrozole in HR+/HER2+ metastatic breast cancer and other solid tumors |
| [NCT03013504](https://clinicaltrials.gov/study/NCT03013504) | Phase 3 | Completed | 503 | Biosimilar (HD201) vs Herceptin® equivalence trial in HER2+ early breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT | Lancet Oncol | 5-year NeoSphere data: neoadjuvant pertuzumab + trastuzumab improves pathological complete response in HER2+ breast cancer |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | Lancet Oncol | monarcHER: abemaciclib + trastuzumab ± fulvestrant vs chemo + trastuzumab in HR+/HER2+ advanced breast cancer |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncol | ExteNET: neratinib after trastuzumab-based adjuvant therapy in HER2+ breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Ann Oncol | WSG-ADAPT HER2+/HR-: de-escalated neoadjuvant trastuzumab + pertuzumab ± paclitaxel |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncol | WSG-TP-II: endocrine therapy + trastuzumab + pertuzumab vs de-escalated chemo in HR+/HER2+ early breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2+ breast cancer |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Cohort/Translational | Theranostics | Molecular portraits and trastuzumab responsiveness in ER+/PR+/HER2+ ("triple-positive") breast cancer |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | Retrospective | BMC Cancer | Trastuzumab + fulvestrant combination in HR+/HER2+ advanced breast cancer |
| [40763319](https://pubmed.ncbi.nlm.nih.gov/40763319/) | 2025 | Regulatory Summary | J Clin Oncol | FDA approval summary for trastuzumab deruxtecan in HR+/HER2-low/ultralow breast cancer |
| [38034484](https://pubmed.ncbi.nlm.nih.gov/38034484/) | 2024 | Preclinical | Oncol Lett | Progesterone + estradiol reverses trastuzumab's inhibitory effect on triple-positive (ER+/PR+/HER2+) breast cancer cells — directly relevant to the PR/HER2 crosstalk mechanism |

---

## Singapore Market Information

Trastuzumab currently has **no product registrations in Singapore** (market status: 未上市 / Not Marketed; total licenses: 0). No authorization records, product names, or approved indication text are available in the regulatory data source.

---

## Cytotoxicity

Trastuzumab is an antineoplastic biologic (anti-HER2 monoclonal antibody) used in the treatment of breast cancer, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2/ERBB2 humanized monoclonal antibody; not a conventional cytotoxic chemotherapy agent) |
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
Multiple completed Phase 3 RCTs (e.g., NCT01275677, NCT04629846, NCT00005970, NCT03726879) and mechanistic/translational literature support trastuzumab's efficacy in HER2-positive breast cancer, satisfying L1 evidence criteria. However, the "PR-positive breast cancer" label is not itself the mechanistic target — HER2 status is — so this should be treated as confirmation of an existing core indication rather than a novel repurposing opportunity, and use should be gated on HER2 IHC/FISH positivity rather than PR status alone.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/HSA package insert warnings and contraindications before any S1 safety pre-assessment can proceed
- Resolve DG002 (High): confirm formal DrugBank/regulatory mechanism-of-action record
- Confirm HER2 IHC/FISH status as the clinical eligibility guardrail (not PR status alone)
- Assess feasibility and requirements for Singapore market registration, since trastuzumab currently has zero SIN licenses
- Obtain cardiac safety (LVEF monitoring) and infusion-reaction data from the official package insert, given known class-level trastuzumab cardiotoxicity not captured in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

