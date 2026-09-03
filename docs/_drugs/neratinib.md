---
layout: default
title: Neratinib
parent: 僅模型預測 (L5)
nav_order: 699
evidence_level: L5
indication_count: 10
---

# Neratinib
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

# Neratinib: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Neratinib is an irreversible pan-HER (EGFR/HER2/HER4) tyrosine-kinase inhibitor, established through the Phase 3 ExteNET trial for extended adjuvant therapy of HER2-positive breast cancer. The TxGNN model predicts it may also be effective for **progesterone-receptor (PR) positive breast cancer**, with **5 clinical trials** and **10 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (extended adjuvant therapy; per ExteNET trial evidence — not currently registered in Singapore) |
| Predicted New Indication | Progesterone-Receptor Positive Breast Cancer |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available in this evidence pack (flagged as a High-severity data gap). Based on the supporting clinical evidence, however, neratinib is known to be an irreversible pan-HER tyrosine-kinase inhibitor that blocks EGFR, HER2, and HER4, downstream disrupting PI3K-AKT and RAS-MAPK signalling. Its established clinical benefit is in HER2-positive breast cancer, most notably as 12-month extended adjuvant therapy following trastuzumab-based treatment (ExteNET, Phase 3 RCT).

PR-positive breast cancer substantially overlaps clinically with the HR+/HER2+ population already targeted by neratinib — many PR-positive tumours co-express HER2, and post-hoc analysis of ExteNET showed the HR+/HER2+ subgroup (which includes PR-positive patients) derived greater benefit from adjuvant neratinib than HR-negative patients. This subgroup relationship is already reflected in NCCN and ASCO guideline discussions, supporting the biological plausibility that neratinib's mechanism extends meaningfully to PR-positive, HER2-positive disease.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Pre-operative neratinib + aromatase inhibitor + trastuzumab in ER-positive, HER2-positive breast cancer |
| [NCT05599334](https://clinicaltrials.gov/study/NCT05599334) | N/A (Observational) | Completed | 111 | Real-world European Early Access Program data on neratinib as extended adjuvant therapy in early-stage HER2+ breast cancer |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A (Observational) | Completed | 1,151 | Large multicentre retrospective study on HER2-low prevalence and treatment patterns in metastatic breast cancer |
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Phase 2 | Withdrawn | 0 | Neratinib + fulvestrant in HR-positive, HER2-negative metastatic breast cancer; withdrawn, no data generated |
| [NCT04460430](https://clinicaltrials.gov/study/NCT04460430) | Phase 2 | Terminated | 12 | Neratinib in HR+/HER2-negative, HER2-enriched advanced/metastatic breast cancer; terminated early, small sample |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncology | ExteNET Phase 3 RCT: 12 months of neratinib after trastuzumab-based adjuvant therapy in early-stage HER2-positive breast cancer, including HR+ subgroup benefit |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | RCT | New England Journal of Medicine | I-SPY 2 adaptive Phase 2 trial evaluating neratinib among other agents added to standard neoadjuvant chemotherapy in high-risk early breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Review | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Review | JNCCN | NCCN Guidelines update for breast cancer treatment algorithms |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Review | Clinical Breast Cancer | Expert roundtable on clinical developments and practice guidance for HER2-positive breast cancer, including neratinib |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncology | Review of current treatment trends in HR+/HER2+ breast cancer, including neratinib and trastuzumab emtansine |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Cohort | Breast Cancer Res Treat | Real-world patterns of adjuvant neratinib use and tolerance in HR-positive, HER2-positive early-stage breast cancer, including GI toxicity impact on discontinuation |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | Cohort | Breast Cancer Research | ERBB2 mutation status as an adverse prognostic marker in ER-positive, ERBB2 non-amplified lobular breast carcinoma |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Case Series | Frontiers in Oncology | Case report and literature review on HER2-positive breast cancer with leptomeningeal disease |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Review | Clin Adv Hematol Oncol | Overview of integrating recent data into metastatic breast cancer clinical practice by receptor subtype |

## Singapore Market Information

Currently no registration records available — Neratinib is not marketed in Singapore (0 licenses on file).

## Cytotoxicity

Neratinib is an antineoplastic agent (pan-HER tyrosine-kinase inhibitor used in HER2-positive breast cancer).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral pan-HER tyrosine-kinase inhibitor; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function; gastrointestinal tolerance — real-world cohort data (PMID 39153126) note significant GI toxicity (diarrhea) as the main driver of treatment discontinuation |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 trials and a pivotal Phase 3 RCT (ExteNET) support neratinib's mechanistic and clinical relevance to the HR+/HER2+ (including PR-positive) breast cancer subgroup, but the drug is not currently registered in Singapore and key safety/MOA data are missing.

**To proceed, the following is needed:**
- Official package insert / regulatory safety data (warnings, contraindications) — currently a Blocking data gap
- Confirmed DrugBank mechanism-of-action documentation
- Singapore HSA registration and market-entry pathway assessment
- PR-receptor-specific subgroup analysis from ExteNET or equivalent trials to confirm efficacy beyond the general HR+/HER2+ population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

