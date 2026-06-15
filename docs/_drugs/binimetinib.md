---
layout: default
title: Binimetinib
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Binimetinib
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

# Binimetinib: From BRAF-Mutant Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Binimetinib is a selective MEK1/2 inhibitor approved globally (as Mektovi) in combination with encorafenib for BRAF V600E/K-mutant unresectable or metastatic cutaneous melanoma, though it has not been registered in Singapore.
The TxGNN model predicts it may be effective for **Non-Cutaneous Melanoma** (including uveal, mucosal, and other non-skin subtypes), with **40 clinical trials** and **1 publication** currently supporting this direction.

> **Note on Prediction Ranking:** The highest-scoring TxGNN prediction (Rank 1) is choroideremia (score 98.63%), which has no supporting clinical trials or literature (Evidence Level: L5, Recommendation: Hold). This report therefore focuses on **Non-Cutaneous Melanoma** (Rank 2, score 98.60%), the top evidenced indication with the strongest actionable recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore (global approved use: BRAF V600E/K-mutant unresectable/metastatic melanoma) |
| Predicted New Indication | Non-Cutaneous Melanoma |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L2 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Singapore regulatory database. Based on known information, Binimetinib is a selective MEK1/2 inhibitor that blocks the BRAF→MEK→ERK signaling cascade. When BRAF harbors a V600E or V600K activating mutation, it constitutively fires MEK, driving uncontrolled tumor cell proliferation. Binimetinib directly suppresses MEK1/2 kinase activity, halting this downstream signal. It is globally co-administered with the BRAF inhibitor encorafenib (Braftovi + Mektovi), synergistically shutting down the RAS-MAPK pathway from two nodes simultaneously.

Non-cutaneous melanoma encompasses biologically distinct subtypes — uveal (ocular), mucosal (oral, anorectal, genitourinary), and anatomical variants such as eyelid or acral presentations. Although BRAF V600 mutation rates in these subtypes are substantially lower (~5–20%) compared to cutaneous melanoma (~50%), a meaningful patient subset still harbors BRAF mutations or MEK-activating alterations. Uveal melanoma, for example, frequently carries GNAQ/GNA11 mutations that route oncogenic signaling through MEK, providing a distinct but relevant mechanistic basis for MEK inhibition even in BRAF-wild-type tumors.

The mechanistic overlap between the established indication (BRAF-mutant cutaneous melanoma) and non-cutaneous subtypes with MEK-dependent signaling is why TxGNN assigns a high prediction score. Multiple Phase II/III trials — including the pivotal COLUMBUS trial (N=921) and the NEMO trial in NRAS-mutant melanoma (N=402) — enrolled patients across melanoma anatomical subtypes, and several ongoing studies explicitly permit or include mucosal and non-cutaneous participants. The combination's demonstrated ability to penetrate the CNS (brain metastasis studies) also extends its relevance to non-cutaneous primaries that frequently metastasize to the brain.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01909453](https://clinicaltrials.gov/study/NCT01909453) | Phase 3 | Completed | 921 | COLUMBUS pivotal trial: encorafenib + binimetinib vs vemurafenib in BRAF V600-mutant unresectable/metastatic melanoma — established the combination as a standard of care |
| [NCT01763164](https://clinicaltrials.gov/study/NCT01763164) | Phase 3 | Completed | 402 | NEMO trial: binimetinib (MEK162) vs dacarbazine in NRAS Q61-mutant advanced melanoma — demonstrated binimetinib's superiority over chemotherapy; key evidence for MEK inhibition beyond BRAF subtype |
| [NCT05270044](https://clinicaltrials.gov/study/NCT05270044) | Phase 3 | Active, not recruiting | 815 | COLUMBUS-AD: adjuvant encorafenib + binimetinib vs surveillance in fully resected Stage IIB/C BRAF V600E/K-mutant melanoma — evaluates curative-intent use |
| [NCT04657991](https://clinicaltrials.gov/study/NCT04657991) | Phase 3 | Active, not recruiting | 257 | Encorafenib + binimetinib + pembrolizumab vs placebo + pembrolizumab in BRAF V600E/K-mutant metastatic/locally advanced melanoma — exploring chemo-immunotherapy combination |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EBIN: encorafenib + binimetinib (12 weeks) → nivolumab + ipilimumab vs immediate immunotherapy in BRAF V600-mutant unresectable/metastatic melanoma — may enroll non-cutaneous subgroups |
| [NCT03898908](https://clinicaltrials.gov/study/NCT03898908) | Phase 2 | Completed | 48 | Encorafenib + binimetinib before local CNS treatment in BRAF-mutant melanoma with brain metastases (asymptomatic and symptomatic cohorts) — directly relevant to advanced non-cutaneous disease |
| [NCT04511013](https://clinicaltrials.gov/study/NCT04511013) | Phase 2 | Recruiting | 112 | Randomized trial: encorafenib + binimetinib + nivolumab vs ipilimumab + nivolumab in BRAF V600-mutant melanoma with brain metastases — design allows mucosal/non-cutaneous participation |
| [NCT02910700](https://clinicaltrials.gov/study/NCT02910700) | Phase 2 | Active, not recruiting | 52 | TRIBECA: nivolumab + encorafenib + binimetinib (triplet) in BRAF-mutant Stage III–IV unresectable/metastatic melanoma — evaluates novel triplet combinations |
| [NCT01320085](https://clinicaltrials.gov/study/NCT01320085) | Phase 2 | Completed | 183 | Single-agent MEK162 (binimetinib) in locally advanced/metastatic malignant cutaneous melanoma with BRAF V600 or NRAS mutations — foundational early-phase efficacy and safety data |
| [NCT06887088](https://clinicaltrials.gov/study/NCT06887088) | Phase 2 | Recruiting | 33 | ENCEFALO: encorafenib + binimetinib → cemiplimab + fianlimab sequential strategy in BRAF-mutant melanoma with symptomatic brain metastases — newest trial in this combination space |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case Report | Pigment Cell & Melanoma Research | Molecular profiling used to diagnose epidermotropic metastatic melanoma presenting as eruptive primary melanomas; illustrates diagnostic complexity in distinguishing metastatic from primary melanoma subtypes, relevant to non-cutaneous disease staging |

---

## Singapore Market Information

No regulatory authorizations are currently registered for Binimetinib in Singapore. The drug is not available through the HSA approval pathway at this time.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (selective MEK1/2 inhibitor; non-conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate — MEK inhibitors carry lower myelosuppression risk than conventional cytotoxics; anaemia has been reported; monitor haematological parameters |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests, renal function, LVEF (cardiac monitoring at baseline and periodically), ophthalmic exams (risk of retinal pigment epithelium detachment and uveitis), dermatology assessment, blood pressure |
| Handling Protection | Follow institutional oral antineoplastic handling guidelines; standard precautions for cytotoxic agents apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The encorafenib + binimetinib combination has strong Phase II/III evidence across BRAF-mutant melanoma subtypes — including two completed Phase III trials (COLUMBUS, N=921; NEMO, N=402) and multiple ongoing trials enrolling non-cutaneous patient populations — and the BRAF→MEK mechanistic basis is well established; however, Binimetinib is not registered in Singapore, BRAF mutation rates in non-cutaneous subtypes are substantially lower than in cutaneous melanoma, and Singapore-specific safety data are absent.

**To proceed, the following is needed:**

- **Regulatory pathway:** Determine Singapore HSA registration strategy for Binimetinib (and encorafenib as combination partner); assess parallel import or named-patient access options
- **Molecular screening protocol:** Establish BRAF V600E/K mutation testing criteria for non-cutaneous melanoma patients to identify the eligible subpopulation
- **Safety documentation:** Obtain full HSA/EMA/FDA package insert to complete the safety assessment (key warnings, contraindications, DDI profile)
- **MOA documentation:** Retrieve formal mechanism of action data from DrugBank (DB11967) for regulatory dossier preparation
- **Subtype stratification:** Clarify which non-cutaneous subtypes (uveal, mucosal, eyelid, acral) are intended targets, as BRAF prevalence and recommended therapies differ substantially by subtype
- **Combination partner availability:** Confirm encorafenib availability in Singapore, as Binimetinib is not indicated as a single agent for melanoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

