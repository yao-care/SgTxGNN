---
layout: default
title: Betamethasone
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Betamethasone
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

# Betamethasone: From Inflammatory Conditions to Alopecia Areata

## One-Sentence Summary

Betamethasone is a potent synthetic glucocorticoid widely used to treat inflammatory, allergic, and autoimmune conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata** — a non-scarring autoimmune hair loss disorder —
with **7 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory and allergic conditions (no Singapore registration data available) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Betamethasone is a potent synthetic glucocorticoid — approximately 25–35 times more potent than prednisolone — that acts by activating glucocorticoid receptors (GR) to broadly suppress T-cell-mediated autoimmune activity. Alopecia areata (AA) is driven primarily by CD8⁺ cytotoxic T cells breaking down the immune privilege of hair follicles, leading to non-scarring, patchy hair loss. This makes betamethasone's mechanism of action directly applicable: it downregulates key Th1/Th2 pro-inflammatory cytokines (IL-2, IFN-γ, IL-4), suppresses NF-κB pathway activation, and inhibits perifollicular lymphocyte infiltration.

What sets betamethasone apart from other corticosteroids in this context is its clinical versatility. It can be delivered via topical cream or solution (for mild localized disease), intralesional injection (for focal patches), or systemic oral mini-pulse regimens (for moderate-to-severe or rapidly progressive AA) — and each route has independent clinical trial evidence in AA. This flexibility makes it a practical candidate across disease severity tiers.

The TxGNN model prediction is therefore not speculative: corticosteroids are already a cornerstone of AA management globally, and betamethasone has been directly evaluated as the intervention drug (not merely a background comparator) in multiple completed RCTs, including a Phase 2 trial (NCT06786689) that compared betamethasone oral mini-pulse against azathioprine pulse therapy. The mechanistic rationale and clinical evidence together place this among the more actionable predictions in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | Completed | 60 | Only completed RCT directly evaluating Betamethasone: compared oral mini-pulse (BOMP) vs weekly Azathioprine pulse in moderate-to-severe AA |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Unknown | 59 | Head-to-head comparison of topical cetirizine 1% vs topical betamethasone valerate 0.1% in localized AA |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | Unknown | 60 | Topical betamethasone valerate 0.1% as active comparator vs pentoxifylline 2% gel and metformin 10% gel in patchy AA |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | Completed | 40 | Topical minoxidil 5% combined with potent topical corticosteroid vs intralesional triamcinolone in AA; class-level support for topical corticosteroid efficacy |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | Completed | 50 | Topical betamethasone vs topical latanoprost in localized AA; confirms betamethasone as the established active standard in head-to-head comparisons |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-analysis (Cochrane) | Cochrane Database Syst Rev | Comprehensive network meta-analysis of AA treatments; highest-tier evidence for positioning betamethasone relative to immunosuppressants and other corticosteroids |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | J Am Acad Dermatol | Microneedle transdermal delivery of compound betamethasone in AA; non-inferior efficacy with significantly reduced procedural pain vs conventional intralesional injection |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | Comparative RCT | Cureus | Topical betamethasone dipropionate vs topical minoxidil in AA; directly compared two commonly used agents with clinical outcome data |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT (double-blind, placebo-controlled) | Iran J Pharm Res | Oral betamethasone pulse vs methotrexate vs combination in severe AA (n=36); betamethasone arm demonstrated clinically meaningful hair regrowth |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | Prospective Comparative Study | Cureus | Oral betamethasone mini-pulses in moderate-to-severe AA; evaluated efficacy, safety, and tolerability profile of an intermittent dosing regimen |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | Within-patient RCT | J Dermatol Treat | Intralesional betamethasone vs triamcinolone acetonide in localized AA; first within-patient RCT comparing two intralesional corticosteroids head-to-head in AA |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | Corticosteroid pulse therapy in AA: efficacy rates, relapse patterns, side effects, and prognostic factors across different pulse regimens including betamethasone |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | Comparative Study | Dermatol Ther | Six-arm blinded RCT comparing latanoprost, minoxidil, betamethasone, and combinations in AA (n=108 total); betamethasone arms serve as active reference |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | Clinical Interventional Study | Arch Dermatol Res | Fractional CO₂ laser alone vs combined with betamethasone valerate in AA; combination therapy showed superior hair regrowth at 3 months |
| [26691357](https://pubmed.ncbi.nlm.nih.gov/26691357/) | 2015 | Comparative Study | J Coll Physicians Surg Pak | Intralesional triamcinolone acetonide vs topical betamethasone valerate in localized AA; demonstrated comparable efficacy supporting topical route as a viable alternative |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Key warnings, contraindications, and drug interaction data were not retrievable from the Singapore HSA database for this submission. Full safety profiling from the product's reference dossier (e.g., FDA, EMA, or TGA label) is required before any clinical use decision.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT (NCT06786689) directly evaluated betamethasone oral mini-pulse in moderate-to-severe AA, multiple RCTs in the published literature confirm topical and intralesional betamethasone efficacy across AA subtypes, and a Cochrane network meta-analysis provides the highest tier of comparative evidence. The mechanistic basis is sound and the clinical signal is consistent across routes and severities. However, betamethasone is currently not registered in Singapore, requiring a full regulatory pathway before clinical deployment.

**To proceed, the following is needed:**
- Full safety profile retrieval from a reference regulatory authority (FDA/EMA/TGA): key warnings, contraindications, and major drug interactions
- Mechanism of action documentation (DrugBank full record or approved package insert)
- Singapore HSA regulatory strategy: assess whether a new drug application or reliance pathway on an existing approval is more appropriate
- Definition of target patient population and preferred route of administration (topical for mild/localized vs intralesional for focal patches vs oral mini-pulse for moderate-to-severe)
- Long-term safety monitoring plan covering HPA axis suppression, adrenal insufficiency risk, skin atrophy (for topical formulations), and ocular pressure monitoring
- Comparative effectiveness evaluation against JAK inhibitors (baricitinib, ritlecitinib), which have recently received regulatory approvals for AA in multiple markets and now represent the emerging standard of care for severe disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

