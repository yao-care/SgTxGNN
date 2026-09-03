---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 727
evidence_level: L5
indication_count: 10
---

# Olaparib
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

# Olaparib: From BRCA-Mutated Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib is an oral PARP1/2 inhibitor originally developed for BRCA-mutated, platinum-sensitive ovarian cancer. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, a direction already supported by **50 clinical trials** and **20 publications** — including two pivotal Phase III trials (OlympiAD, OlympiA) that have led to approval of olaparib for BRCA-mutated breast cancer in other jurisdictions. The drug is not currently registered or marketed locally.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered locally (no approved_indication_text on file); internationally approved for BRCA-mutated, platinum-sensitive ovarian cancer |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in the drug record itself, but the mechanism is well documented across the evidence pack's own clinical and literature sources: olaparib is a poly(ADP-ribose) polymerase (PARP1/2) inhibitor. By blocking base-excision repair of single-strand DNA breaks, it forces tumor cells that already carry a homologous-recombination defect (most commonly a BRCA1/BRCA2 mutation) to rely on PARP-mediated repair for survival — inhibiting PARP in this context causes synthetic lethality and selective tumor cell death (PMID 26344419).

BRCA1/BRCA2 mutations are a shared molecular driver of both ovarian and breast cancer, since both genes function in the same homologous-recombination DNA repair pathway. This shared biology is the direct link between olaparib's original ovarian cancer use and its activity in breast cancer: the same synthetic-lethality mechanism that kills BRCA-deficient ovarian tumor cells applies equally to BRCA-deficient breast tumor cells.

This is not a purely hypothetical repurposing signal — olaparib has already demonstrated efficacy in BRCA-mutated breast cancer in large, randomized Phase III trials (OlympiAD for metastatic disease, OlympiA for high-risk early-stage adjuvant treatment) and is approved for this indication in multiple regulatory jurisdictions. The TxGNN signal for this market therefore reflects a genuine care gap (local registration) rather than an unproven biological hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04421963](https://clinicaltrials.gov/study/NCT04421963) | Phase 3 | Active, not recruiting | 185 | Rollover study (ROSY-O) continuing olaparib treatment for patients deriving clinical benefit from prior olaparib oncology studies |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Real-world Indian cohort: olaparib in platinum-sensitive relapsed ovarian cancer and metastatic breast cancer with germline BRCA1/2 mutation |
| [NCT02734004](https://clinicaltrials.gov/study/NCT02734004) | Phase 1/2 | Active, not recruiting | 264 | Olaparib + durvalumab (± bevacizumab) in advanced solid tumors, including breast cancer |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | Active, not recruiting | 50 | Neoadjuvant olaparib monotherapy vs. olaparib+durvalumab in BRCA-mutated, early-stage HER2-negative breast cancer |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Phase 2 | Recruiting | 176 | Olaparib + elacestrant vs. olaparib alone in HR-positive/HER2-negative advanced breast cancer with gBRCA1/2 mutation |
| [NCT03660826](https://clinicaltrials.gov/study/NCT03660826) | Phase 2 | Active, not recruiting | 288 | Randomized platform trial including olaparib monotherapy and olaparib+cediranib arms |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin-olaparib followed by olaparib monotherapy vs. capecitabine as first-line treatment in BRCA1/2-mutated, HER2-negative advanced breast cancer |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Completed | 99 | Open-label, non-randomized study of olaparib (AZD2281) in BRCA-associated or triple-negative breast cancer and ovarian carcinoma, assessing response rate |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Phase 1 | Completed | 118 | Olaparib combined with PI3K inhibitors (BKM120/BYL719) in recurrent triple-negative breast cancer or high-grade serous ovarian cancer |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Completed | 24 | Olaparib with radiation therapy in inflammatory, locoregionally advanced/metastatic or residual triple-negative breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT (Phase III, OlympiA) | New England Journal of Medicine | Adjuvant olaparib reduces recurrence risk in BRCA1/2-mutated, high-risk early breast cancer |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT (OlympiA, OS analysis) | Annals of Oncology | Interim overall survival analysis confirms benefit of adjuvant olaparib in gBRCA1/2 early breast cancer |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT (Phase III, OlympiAD) | New England Journal of Medicine | Olaparib shows antitumor activity in metastatic breast cancer with germline BRCA mutation |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT (OlympiAD, final OS) | Annals of Oncology | Final overall survival and tolerability results of olaparib vs. chemotherapy in gBRCA-mutated HER2-negative metastatic breast cancer |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT (OlympiAD, extended follow-up) | European Journal of Cancer | Extended follow-up confirms progression-free survival benefit and safety profile of olaparib in gBRCA-mutated metastatic breast cancer |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT (Phase II, TBCRC048) | Journal of Clinical Oncology | Olaparib shows response in metastatic breast cancer with somatic BRCA1/2 or other homologous-recombination gene mutations |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT (Phase II, I-SPY2) | Cancer Cell | Durvalumab + olaparib + paclitaxel increases pathologic complete response in high-risk HER2-negative breast cancer |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | RCT (Phase II/III, PARTNER) | Nature | Neoadjuvant olaparib added to carboplatin-paclitaxel evaluated in BRCA-wild-type triple-negative breast cancer |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | Overview of PARP inhibitors, including olaparib, approved as monotherapy for gBRCA-mutated, HER2-negative breast cancer |
| [31650727](https://pubmed.ncbi.nlm.nih.gov/31650727/) | 2020 | Review | Annals of Laboratory Medicine | Review of BRCA1/BRCA2 pathogenic variant breast cancer treatment and prevention strategies |

---

## Singapore Market Information

Olaparib currently has no marketing authorization or registration records on file (total registrations: 0; market status: Not Marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (No drug interaction records were found in the current query; key warnings and contraindications data are not yet available.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two independent Phase III randomized controlled trials (OlympiAD, OlympiA) plus a broad supporting body of Phase I/II studies establish that olaparib is effective in BRCA-mutated breast cancer, and this indication is already approved in other jurisdictions — meeting the L1 evidence bar. However, olaparib is not currently registered locally, so market entry (not just clinical validation) is the remaining gap.

**To proceed, the following is needed:**
- Local product label / package insert with key warnings and contraindications (currently flagged as a Blocking data gap — required before any S1 safety assessment)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (currently a High-severity data gap)
- A completed drug-drug interaction review (current query returned no results)
- A local registration/licensing pathway assessment, since the drug currently has zero registrations in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

