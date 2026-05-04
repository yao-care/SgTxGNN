---
layout: default
title: Abiraterone
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Abiraterone
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

# Abiraterone: From Prostate Cancer to Migraine Disorder

## One-Sentence Summary

Abiraterone is a potent CYP17A1 inhibitor (androgen biosynthesis inhibitor) established in the treatment of castration-resistant prostate cancer, suppressing androgen synthesis in the adrenal glands and tumour tissue.
The TxGNN model predicts it may be effective for **Migraine Disorder**,
however there are currently **no clinical trials** and **no publications** directly supporting this repurposing direction, making this a purely model-driven, speculative prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Castration-resistant prostate cancer (not registered in Singapore) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, Abiraterone is a selective inhibitor of CYP17A1 (17α-hydroxylase/C17,20-lyase), the enzyme responsible for androgen biosynthesis in the adrenal glands, testes, and tumour tissue. Its efficacy in castration-resistant prostate cancer is well-established through multiple Phase 3 trials, and it acts by depleting circulating androgens and their steroid precursors.

The theoretical link to migraine rests on the known hormonal dimension of migraine pathophysiology. Migraine — particularly menstrual migraine — is modulated by sex hormone fluctuations: oestrogen withdrawal lowers neuronal threshold and enhances trigeminal neurovascular excitability. By inhibiting CYP17A1, Abiraterone broadly suppresses adrenal steroidogenesis, altering the hormonal environment that may influence migraine susceptibility. In theory, this could reduce hormonally-driven migraine frequency.

However, this mechanistic chain is highly speculative. CYP17A1 inhibition has no established direct connection to the core pathophysiological mechanisms of migraine — cortical spreading depression, trigeminovascular peptide release (CGRP), or central sensitisation. No preclinical studies have tested this hypothesis, and the hormonal pathway implicated is indirect. This prediction should currently be treated as a hypothesis-generating signal, not a repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Abiraterone is not currently registered or marketed in Singapore. No Health Sciences Authority (HSA) authorisation records are on file. The drug therefore has no approved indication, dosage form, or post-marketing safety data accessible through the Singapore regulatory pathway.

---

## Cytotoxicity

Abiraterone is an antineoplastic agent used in the treatment of prostate cancer and meets the criteria for inclusion of this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Androgen biosynthesis inhibitor (CYP17A1 inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — hormonal mechanism of action; significant myelosuppression is not an expected toxicity |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (hepatotoxicity), serum potassium (hypokalemia due to mineralocorticoid excess), blood pressure (fluid retention, hypertension), serum cortisol, adrenal insufficiency signs |
| Handling Protection | Standard oral antineoplastic handling precautions apply; dedicated cytotoxic preparation facilities are not required for oral formulations under most institutional policies, but local SOPs should be consulted |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** All safety data — including key warnings, contraindications, and drug-drug interaction records — were not retrievable in this evidence cycle. TFDA package insert parsing and DDI database query both returned no results. This is classified as a blocking data gap (DG001) and must be resolved before any clinical feasibility assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (98.81%), this prediction is unsupported by any clinical trials or relevant literature, has no established pharmacological mechanism connecting CYP17A1 inhibition to migraine pathophysiology, and involves a drug with zero Singapore regulatory presence and unavailable safety data. The totality of evidence does not justify progression at this time.

**To proceed, the following is needed:**

- **Mechanistic validation**: Preclinical studies or literature demonstrating any effect of androgen suppression or CYP17A1 inhibition on trigeminovascular excitability, cortical spreading depression, or CGRP signalling
- **MOA data**: Retrieve full DrugBank entry (DB05812) to confirm pharmacological class, targets, and known off-target effects
- **Safety data**: Parse TFDA (or EMA/FDA) package insert to extract key warnings, contraindications, and drug interactions — currently a blocking data gap
- **DDI assessment**: Perform structured DDI query using an alternative source (e.g., DrugBank DDI, Drugs.com, or clinical pharmacology databases)
- **Population context**: Evaluate whether Abiraterone's safety profile (mineralocorticoid excess, hepatotoxicity, adrenal insufficiency) is acceptable in a migraine patient population who are predominantly women of reproductive age — notably different from the approved prostate cancer population
- **Regulatory pathway**: Assess requirements for first-in-indication registration in Singapore should evidence emerge in the future
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

