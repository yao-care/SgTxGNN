---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 995
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From Original Indication (Not Specified) to Polycystic Kidney Disease

## One-Sentence Summary

> Tolvaptan is a selective vasopressin V2-receptor antagonist; the original indication is not recorded in this evidence pack.
> The TxGNN model predicts it may be effective for **Polycystic Kidney Disease (ADPKD, with or without polycystic liver disease)**,
> a use already supported by **2 completed Phase 3 RCTs** and **20 related publications** — and already approved internationally under the brand name Jynarque.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no `original_indications` or license data provided) |
| Predicted New Indication | Polycystic Kidney Disease 3, with or without Polycystic Liver Disease (ADPKD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tolvaptan is not available in this evidence pack (flagged as a High-severity data gap, DG002). However, the model's repurposing rationale supplies the relevant pharmacology: tolvaptan is a selective vasopressin V2-receptor antagonist that blocks cAMP accumulation in renal tubular epithelial cells. This cAMP pathway is the key driver of cyst formation and enlargement following *PKD1*/*PKD2* mutations, which cause autosomal dominant polycystic kidney disease (ADPKD).

Unlike many TxGNN candidates that rely purely on embedding similarity, this prediction reflects an indication tolvaptan already holds in multiple jurisdictions (approved as Jynarque for ADPKD). The evidence pack notes that although this local market shows "未上市" (not marketed) status, large Phase 3 trials and international approvals already exist — meaning the local gap is a regulatory/registration gap rather than an evidence gap.

Because the mechanistic link (V2 receptor → cAMP → cystogenesis) is direct and well-characterized rather than inferred, this is one of the stronger candidates in the prediction set — in contrast to lower-ranked candidates in this same pack (e.g., hypertrichosis, Dandy-Walker malformation), which the model itself flags as likely knowledge-graph noise with no mechanistic or literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack (the `clinical_trials` field is empty). Note: the pivotal trials supporting this indication — TEMPO 3:4 (NCT00428948) and REPRISE (NCT02160145) — are referenced in the literature evidence below but were not captured in the structured clinical trial registry field of this pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | N Engl J Med | TEMPO 3:4 trial: tolvaptan slowed total kidney volume growth and eGFR decline in early ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | N Engl J Med | REPRISE trial: confirmed efficacy and safety of tolvaptan in later-stage ADPKD |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Cochrane Systematic Review | Cochrane Database Syst Rev | Systematic review of disease-modifying agents (including tolvaptan) for ADPKD progression |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review/Meta-analysis | Nefrologia | Meta-analysis confirming efficacy and safety of tolvaptan in ADPKD |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Review/Consensus | Nephrol Dial Transplant | ERA/ERKNet/PKD International consensus on tolvaptan use in ADPKD post-TEMPO 3:4 |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | J Hepatol | EASL guidelines on management of cystic liver diseases, including polycystic liver disease |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive review of ADPKD pathophysiology and management |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Review of polycystic kidney/liver disease; notes tolvaptan slows renal function decline and cyst growth |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum of polycystic kidney/liver diseases and resulting phenotypes |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | Reviews emerging ADPKD therapies beyond tolvaptan, confirming tolvaptan as current standard of care |

---

## Singapore Market Information

This drug is currently **not registered/marketed** in this jurisdiction (`market_status`: 未上市, `total_licenses`: 0). No authorization records are available to list.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in this evidence pack; note that DG001 flags missing local label warnings/contraindications as a **Blocking** severity gap.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (TEMPO 3:4, REPRISE) plus multiple consensus guidelines and systematic reviews provide strong (L1) evidence for tolvaptan's efficacy in ADPKD, and the drug is already approved for this indication internationally (Jynarque). However, this jurisdiction currently has zero registrations and no local safety label data, so local regulatory and safety review are required before proceeding.

**To proceed, the following is needed:**
- Local package insert / label data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Formal mechanism-of-action documentation from DrugBank or manufacturer (DG002)
- Local regulatory registration status and pathway assessment, given current "not marketed" status
- Drug-drug interaction data (current query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

