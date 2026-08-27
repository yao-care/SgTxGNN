---
layout: default
title: Lincomycin
parent: 僅模型預測 (L5)
nav_order: 596
evidence_level: L5
indication_count: 10
---

# Lincomycin
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

Using the txgnn-pipeline domain context (this is a TxGNN drug-repurposing evidence pack) together with the fixed v5 report template supplied in the prompt. I verified every field against the JSON before writing it in — no invented values, and I flag where the source data itself calls out a result as likely noise or as a data gap, per this repo's no-fabrication rule.

A structural note before the report: `predicted_indications[0]` (the template's mandated source for "Predicted New Indication") is explicitly annotated in its own `repurposing_rationale` as probable model noise (identical score to rank 2, zero mechanistic link, zero evidence). I report it as instructed, state that caveat honestly rather than presenting it as a clean finding, and add one supplementary section — not in the template — summarizing all 10 screened candidates, since this evidence pack (`candidate_id: TW-DB01627-multi`) is a multi-candidate screen and hiding ranks 2–10 would misrepresent how much was actually evaluated.

---

# Lincomycin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

*Note: this top-ranked prediction is flagged in the source evidence as a likely model-noise artifact — see "Why is This Prediction Reasonable?" below.*

## One-Sentence Summary

Lincomycin is a lincosamide-class antibiotic historically used against Gram-positive and anaerobic bacterial infections; it is **not currently registered or marketed in Singapore**, so no local approved-indication text exists for it. The TxGNN model's top-ranked repurposing candidate is **polyclonal hyperviscosity syndrome**, but this candidate has **0 clinical trials** and **0 publications** supporting it, and it shares an identical prediction score with the next-ranked candidate — a pattern the evidence pack itself identifies as likely embedding-space noise rather than a genuine signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — not registered in Singapore (no approved indication text on file); generally known as an antibacterial (Gram-positive/anaerobic coverage) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Lincomycin is not available in this evidence pack (flagged as data gap **DG002**, severity High). Based on general pharmacological knowledge, Lincomycin inhibits bacterial protein synthesis by binding the 50S ribosomal subunit, and has historically been used for Gram-positive and anaerobic bacterial infections.

For the top-ranked prediction, **polyclonal hyperviscosity syndrome** — a haematological/rheological disorder driven by excess immunoglobulin production — there is no plausible mechanistic link to an antibacterial protein-synthesis inhibitor. The evidence pack's own rationale flags this directly: this candidate's TxGNN score (0.9914100766181946) is **identical** to the next-ranked candidate, hyperamylasemia, which is likewise mechanistically unrelated to antibiotic activity. Two unrelated diseases receiving the exact same score is characteristic of embedding-space proximity noise rather than a real biological signal, and neither candidate is backed by any clinical trial or publication.

Looking across all 10 candidates TxGNN surfaced for this drug (see "Other Screened Candidates" below), the only ones with any plausible mechanistic basis are infection-related: **septicemic plague** (rank 8, caused by the Gram-negative bacterium *Yersinia pestis*) and **urinary tract infection** (rank 10). Even these are weak — lincosamides have poor intrinsic activity against Gram-negative organisms and are not standard-of-care for either indication (aminoglycosides/tetracyclines/fluoroquinolones for plague; agents like cephalexin for UTI). No candidate in this evidence pack reaches a level of mechanistic or empirical support that would justify a Go decision.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (polyclonal hyperviscosity syndrome).

## Literature Evidence

Currently no related literature available for the top-ranked prediction (polyclonal hyperviscosity syndrome).

## Other Screened Candidates (Ranks 2–10)

*Supplementary transparency table — this evidence pack screened 10 candidate indications for Lincomycin; only the rank-1 candidate is covered by the standard template sections above.*

| Rank | Disease | Score | Evidence Level | Recommendation | Note |
|------|---------|-------|-----------------|-----------------|------|
| 2 | Hyperamylasemia | 99.14% | L5 | Hold | Identical score to rank 1; no mechanistic link; no evidence |
| 3 | Congenital analbuminemia | 99.06% | L5 | Hold | Genetic albumin-synthesis defect; no mechanistic link |
| 4 | Blood group incompatibility | 98.76% | L5 | Hold | Immune rejection process; no mechanistic link |
| 5 | Premalignant hematological system disease | 98.65% | L5 | Hold | Haematopoietic stem-cell disorder; no mechanistic link |
| 6 | Monoclonal gammopathy | 98.48% | L5 | Hold | 4 publications, but all are keyword coincidences (myeloma cell decontamination, bisphosphonate-related jaw osteonecrosis) — not treatment evidence |
| 7 | Hematological disease with acquired peripheral neuropathy | 98.39% | L5 | Hold | No mechanistic link; no evidence |
| 8 | Septicemic plague | 98.11% | **L3** | **Research Question** | Caused by a Gram-negative bacterium (mechanistically plausible in principle); evidence is limited to *in vitro* susceptibility surveys, not clinical efficacy; lincosamides are not standard-of-care for plague |
| 9 | Congenital hematological disorder | 97.96% | L5 | Hold | 1 trial (broad paediatric PK/PD registry, not disease-specific) and 1 unrelated animal-model paper |
| 10 | Urinary tract infection (disease) | 97.77% | L4 | Hold | 4 trials + 20 publications, but none evaluate Lincomycin specifically for UTI; most concern other antibiotic classes or veterinary/animal studies |

## Singapore Market Information

Lincomycin is currently **not registered or marketed in Singapore** (`market_status: 未上市`, `total_licenses: 0`). No authorization records are available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug–drug interaction data are all unavailable in this evidence pack — see data gap **DG001**, severity Blocking, which prevents this candidate from advancing to the S1 safety-screening stage.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No candidate reaches L1/L2 evidence (a completed Phase 2/3 RCT); the highest evidence tier reached across all 10 screened candidates is L3 (septicemic plague, *in vitro* susceptibility data only).
- The top-ranked candidate (polyclonal hyperviscosity syndrome) is explicitly flagged in the source rationale as likely model noise, not a genuine signal.
- Lincomycin is not currently registered or marketed in Singapore, and a Blocking data gap (missing package-insert warnings/contraindications, DG001) prevents safety screening from proceeding.

**To proceed, the following is needed:**
- TFDA/HSA package-insert data (warnings, contraindications) to resolve the Blocking gap (DG001)
- Mechanism-of-action data via DrugBank API to resolve the High-severity gap (DG002)
- If pursuing the septicemic plague or UTI directions specifically, Lincomycin-specific efficacy studies (current literature covers other antibiotic classes or non-human models, not Lincomycin itself)
- Reassessment of Singapore market/registration status before any local development path is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

