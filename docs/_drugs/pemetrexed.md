---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 764
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is a multitargeted antifolate originally established as first-line therapy (with cisplatin) for malignant pleural mesothelioma. The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**, with **11 clinical trials** and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant Pleural Mesothelioma (with cisplatin, first-line) — inferred from trial/literature context in this evidence pack; formal Singapore label text unavailable (drug not marketed locally) |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

The formal `original_moa` field is a data gap (DG002, High severity) — DrugBank MOA has not yet been retrieved for this candidate. However, trial-level evidence in this pack (NCT02588781) describes pemetrexed as "a multitargeted antifolate inhibiting thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT)" — key folate-dependent enzymes required for DNA synthesis in rapidly dividing cells.

Malignant pleural mesothelioma and malignant peritoneal mesothelioma both arise from mesothelial cells lining serosal cavities (pleura vs. peritoneum), sharing tumor biology, proliferation kinetics, and histologic subtypes (epithelioid/sarcomatoid/biphasic). Because pemetrexed's antifolate mechanism targets proliferation machinery rather than an anatomically restricted target, the rationale for cross-cavity efficacy is mechanistically sound. Notably, NCCN guidelines already list pemetrexed+cisplatin as a treatment option for peritoneal mesothelioma, and this is corroborated independently by dedicated Phase 2 trials in this evidence pack (e.g., NCT00061477, completed, n=48, enrolling both pleural and peritoneal mesothelioma patients).

The main gap versus a pure "repurposing" claim is that most peritoneal-specific evidence is extrapolated from the pleural pivotal trial rather than from completed peritoneal-specific Phase 3 RCTs — hence the L2 (not L1) evidence rating.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Randomized trial of intraperitoneal vs. intravenous chemotherapy after cytoreductive surgery + HIPEC for malignant peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | PIPAC + systemic chemotherapy (cisplatin+pemetrexed) vs. systemic chemotherapy alone as 1st-line MPeM treatment |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Sintilimab + bevacizumab + pemetrexed/cisplatin in unresectable malignant peritoneal mesothelioma |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Maintenance talazoparib after first-line platinum-based chemo in pleural/peritoneal mesothelioma |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed + gemcitabine as front-line therapy for pleural or peritoneal mesothelioma |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin, pemetrexed, and imatinib mesylate in unresectable/metastatic malignant mesothelioma |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 with pemetrexed and cisplatin in arginine-requiring tumors including peritoneal mesothelioma |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Carboplatin/pemetrexed/bevacizumab ± atezolizumab (immunotherapy) for peritoneal mesothelioma |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | Vorinostat with pemetrexed-cisplatin in malignant pleural mesothelioma |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 + cisplatin/pemetrexed in advanced solid tumors/mesothelioma refractory to pemetrexed-cisplatin |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert Rev Anticancer Ther | First-line pemetrexed + cisplatin efficacy specifically evaluated in malignant peritoneal mesothelioma |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective study | Jpn J Clin Oncol | Efficacy/safety of pemetrexed + cisplatin as first-line chemotherapy in advanced MPeM |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | J Gastrointest Oncol | Diagnosis and management of patients with malignant peritoneal mesothelioma |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | Treatment options for malignant peritoneal mesothelioma, incl. systemic chemotherapy |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | Overview of malignant peritoneal mesothelioma biology and treatment |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort/Case series | Pleura and Peritoneum | Bidirectional chemotherapy (incl. pemetrexed regimens) enabling surgery + HIPEC in initially unresectable MPeM |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Reports | Response to rechallenge with cisplatin + pemetrexed in MPeM |
| [29423664](https://pubmed.ncbi.nlm.nih.gov/29423664/) | 2018 | Review | Ann Surg Oncol | Current management and future opportunities for peritoneal mesothelioma |
| [22104079](https://pubmed.ncbi.nlm.nih.gov/22104079/) | 2012 | Review | Cancer Treat Rev | Update on diffuse malignant peritoneal mesothelioma treatment |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multi-center cohort | Ann Surg Oncol | Treatment strategies and outcomes in malignant peritoneal mesothelioma |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (multitargeted antifolate class — inhibits thymidylate synthase, DHFR, GARFT) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 trials directly support pemetrexed-based regimens in malignant peritoneal mesothelioma, and NCCN already lists this use, but no completed peritoneal-specific Phase 3 RCT exists — most confirmatory strength is extrapolated from the pleural mesothelioma pivotal trial (L2 evidence).

**To proceed, the following is needed:**
- TFDA/HSA label warnings and contraindications (DG001, Blocking — currently no S1 safety screening possible)
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- Drug-drug interaction data (current DDI query returned no results)
- Singapore market entry status confirmation, since the drug is currently unregistered locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

