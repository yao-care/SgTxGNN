---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 1045
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Gram-Positive Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

> Vancomycin is a glycopeptide antibiotic internationally used to treat serious Gram-positive bacterial infections such as MRSA. The TxGNN model's top-ranked prediction suggests potential activity in **Diffuse Scleroderma**, but this signal is currently supported only by a single, unrelated case report and no clinical trials — the evidence review flags it as likely knowledge-graph noise rather than a genuine mechanistic finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Singapore/Taiwan-approved label text on file (0 local registrations); internationally indicated for serious Gram-positive bacterial infections (e.g., MRSA) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Vancomycin is not available in this evidence pack (data gap, blocking). Based on known information, Vancomycin is a glycopeptide antibiotic that inhibits bacterial cell-wall peptidoglycan synthesis, and its efficacy against Gram-positive infections is well established. Diffuse scleroderma, by contrast, is an autoimmune/fibrotic disease driven by TGF-β signalling and fibroblast activation — a biological pathway with no known connection to cell-wall synthesis inhibition.

There is no plausible pharmacological bridge between the original antibacterial mechanism and this predicted autoimmune indication. The single supporting literature record is a case report of exfoliative erythroderma with sepsis, which does not describe Vancomycin use in scleroderma. Given the absence of mechanistic rationale, clinical trials, or directly relevant literature, this top-ranked TxGNN score is best interpreted as a graph-embedding artifact rather than a credible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case Report | The American Journal of Case Reports | Describes a case of diffuse exfoliative erythroderma with sepsis and eosinophilia; does not evaluate Vancomycin as a scleroderma treatment and has no direct bearing on this indication. |

---

## Singapore Market Information

Vancomycin currently has no registered authorizations in Singapore (0 licenses on file); the drug is not marketed locally.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (diffuse scleroderma) has no plausible mechanistic link to Vancomycin's antibacterial mode of action, is supported by only one unrelated case report, and has zero clinical trial evidence — this does not meet the threshold to advance past initial screening.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- Any mechanistic or preclinical rationale connecting glycopeptide antibiotics to autoimmune fibrotic disease, if this indication is to be pursued further
- Local market/registration status confirmation, since Vancomycin currently has 0 Singapore licenses

**Note on other candidates in this evidence pack:** Of the 10 predicted indications screened, most (diffuse scleroderma, paratyphoid fever, salmonellosis, typhoid fever, congenital analbuminemia, hyperamylasemia, polyclonal hyperviscosity syndrome, blood group incompatibility, premalignant hematological disease) show either mechanistic contradiction (e.g., predicted efficacy against Gram-negative organisms, which Vancomycin cannot penetrate) or no biological connection at all — all rated Hold. The only candidate with mechanistic plausibility and moderate-quality supporting literature is **Streptococcal pneumonia** (rank 9, evidence level L3, decision stage S2, "Research Question"), which represents an extension of Vancomycin's existing Gram-positive antibacterial use (e.g., for penicillin-resistant pneumococcus or β-lactam-allergic patients) rather than a novel repurposing signal. If further work is pursued on this drug, that candidate — not diffuse scleroderma — is the more defensible starting point.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

