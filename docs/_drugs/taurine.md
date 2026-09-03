---
layout: default
title: Taurine
parent: 僅模型預測 (L5)
nav_order: 946
evidence_level: L5
indication_count: 10
---

# Taurine
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

# Taurine: From Unregistered Indication to Alcohol Withdrawal Delirium

## One-Sentence Summary

> Taurine is an endogenous amino acid with no currently approved drug indication on record in Singapore (not marketed).
> The TxGNN model predicts it may be effective for **Alcohol Withdrawal Delirium**,
> but this is currently supported by only **1 clinical trial** (low relevance) and **7 publications**, mostly reviews and observational/animal studies rather than direct interventional evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record — Taurine is not a registered pharmaceutical product in Singapore |
| Predicted New Indication | Alcohol Withdrawal Delirium |
| TxGNN Prediction Score | 93.07% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap; requires DrugBank API query). Based on the evidence pack's mechanistic rationale, taurine is proposed to act as an endogenous positive modulator of GABA-A receptors with anti-glutamatergic (anti-excitotoxic) activity — a profile mechanistically analogous to acamprosate, a drug already approved for alcohol withdrawal/dependence management. This theoretical basis is why the model links taurine to CNS hyperexcitability states such as alcohol withdrawal delirium.

However, because taurine has no registered indication anywhere in the Singapore market and no confirmed original MOA, there is no existing "indication-to-indication" bridge to lean on — this is a purely mechanism-driven, model-generated hypothesis rather than an extension of established clinical use. Supporting literature is largely indirect: several papers describe taurine-GABA neurochemical interactions in barbiturate-dependence animal models, and one paper (Litten 1996) discusses taurine's theoretical class alongside acamprosate as a GABAergic anti-withdrawal agent, but none directly test taurine as a treatment for alcohol withdrawal delirium in humans.

The single identified clinical trial (ADEPT feasibility study) does not administer taurine as an intervention; it was flagged as Grade C relevance (disease-domain co-occurrence only, not a taurine trial). This gap between mechanistic plausibility and direct clinical testing is the core reason this candidate remains at an early research-question stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855699](https://clinicaltrials.gov/study/NCT00855699) | Phase 4 | Completed | 36 | ADEPT feasibility study comparing pharmacological regimens for alcohol detoxification in primary care. **Note: taurine is not the studied intervention** — relevance graded C (disease-domain match only, not drug-specific). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2085344](https://pubmed.ncbi.nlm.nih.gov/2085344/) | 1990 | Cohort (RCT-derived) | Alcohol and Alcoholism | Multicenter double-blind placebo-controlled study of acamprosate (a taurine-analog, calcium acetylhomotaurinate) reducing alcohol relapse markers — supports the taurine/GABAergic mechanistic class, but does not test taurine itself. |
| [26314552](https://pubmed.ncbi.nlm.nih.gov/26314552/) | 2016 | Review | European Addiction Research | Descriptive review of approved AD/AWS medication efficacy by gender; taurine not among approved agents discussed. |
| [8865961](https://pubmed.ncbi.nlm.nih.gov/8865961/) | 1996 | Review | Alcoholism: Clinical and Experimental Research | Reviews pharmacotherapies for alcohol problems since 1991, including GABAergic/glutamatergic withdrawal agents as a class. |
| [18281128](https://pubmed.ncbi.nlm.nih.gov/18281128/) | 2008 | Review | La Revue de Médecine Interne | General review of alcohol dependence diagnosis and treatment; no taurine-specific data. |
| [26394517](https://pubmed.ncbi.nlm.nih.gov/26394517/) | 2015 | Review | Nihon Rinsho | Review of pharmacological therapies for alcohol use disorder and withdrawal delirium in Japan; taurine not specifically addressed. |
| [9411716](https://pubmed.ncbi.nlm.nih.gov/9411716/) | 1997 | Review | Schweizerische Medizinische Wochenschrift | Overview of new pharmacological agent classes for alcoholism treatment, including withdrawal syndrome agents. |
| [14679678](https://pubmed.ncbi.nlm.nih.gov/14679678/) | 2003 | Review | Therapie | Adverse-effect review of acamprosate (structurally related to taurine) in alcohol dependence treatment. |

---

## Singapore Market Information

Taurine is **not currently marketed** as a registered pharmaceutical product in Singapore (0 authorizations on record). No product listing, dosage form, or approved indication text is available for comparison.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA-equivalent label warnings and contraindications are currently unavailable (flagged as a **Blocking** data gap — DG001), which prevents formal S1 safety pre-assessment for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to mechanistic extrapolation (L4) and observational/animal-model literature; the only identified clinical trial does not test taurine directly (Grade C relevance), and no interventional human data support taurine specifically — as opposed to its structural analog acamprosate — for alcohol withdrawal delirium. A blocking safety data gap also prevents formal risk assessment at this stage.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA-equivalent label warnings/contraindications for taurine
- Resolve DG002: confirm taurine's mechanism of action via DrugBank
- Identify or design a clinical study testing taurine (not acamprosate) directly as an intervention in alcohol withdrawal/delirium tremens
- Clarify taurine's regulatory status and any existing approved use (e.g., dietary supplement vs. drug) to establish a proper indication baseline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

