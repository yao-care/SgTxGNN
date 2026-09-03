---
layout: default
title: Phenol
parent: 僅模型預測 (L5)
nav_order: 776
evidence_level: L5
indication_count: 10
---

# Phenol
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

# Phenol: From No Established Indication to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Phenol (DrugBank DB03255) has no approved indication or mechanism-of-action record in this evidence pack and is not currently marketed in Singapore (0 registrations). The TxGNN model's top-ranked prediction, **Acrodermatitis Chronica Atrophicans**, is a pure model score supported by **0 clinical trials** and **0 publications**. Across all 10 predicted indications screened for this candidate, only **Acne Keloid** (rank 5) reached a minimally credible evidence tier (L4, based on 4 dermatology publications on phenol chemical peels) — the top-ranked signal reported below remains unsupported.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — no approved indications on record (data gap, see below) |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for phenol is not available in this evidence pack (data gap DG002, severity: High). Phenol is a well-characterized small phenolic compound long used in medicine as a topical antiseptic, local anesthetic/sclerosing agent, and — as documented in the literature evidence retrieved for a *different* candidate indication in this screen — as a chemical peeling agent in dermatology (PMID 17204096: *"Effectiveness of modified phenol peel (Exoderm) on facial wrinkles, acne scars and other skin problems"*). No original/approved indication is registered for phenol in the current dataset, and it holds no marketing authorization in Singapore.

For the top-ranked prediction, Acrodermatitis Chronica Atrophicans — a late-stage cutaneous manifestation of Lyme borreliosis — the evidence pack's own rationale explicitly states there is **no known pathological mechanistic link** to phenol's corrosive/antiseptic/chemical-peel actions. No clinical trials, ICTRP records, or PubMed literature were retrieved for this specific drug–disease pair (0/0/0). This ranking is therefore a raw TxGNN embedding-similarity score (99.95%, global rank 1146) rather than a hypothesis with independent support.

By contrast, the one candidate indication in this screen with a plausible mechanistic story is **Acne Keloid** (rank 5, score 99.94%): phenol's keratolytic/corrosive action in chemical peeling is used clinically to remodel acne scarring and pigmentary skin lesions, and four dermatology publications (tier 2–3, cohort/case-series and reviews) discuss phenol peels and keloidal/hyperpigmented outcomes in acne patients — though none directly test phenol against keloidal acne as a primary endpoint. This is the only prediction in the full set that reached evidence level L4 / decision stage S1 ("Research Question"); all other nine candidates, including the top-ranked one reported above, remain at L5/Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

No Singapore market authorizations are on record for phenol; it is currently classified as **Not Marketed** (0 registrations, 0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Acrodermatitis Chronica Atrophicans) is evidence level L5 — a model score only, with the model's own mechanistic rationale explicitly denying plausibility and zero supporting trials or literature.
- Phenol is not marketed in Singapore, and a Blocking data gap on safety labeling (DG001: TFDA/HSA warnings and contraindications) prevents any Stage 1 safety screening for this candidate.

**To proceed, the following is needed:**
- HSA/TFDA product label (warnings, contraindications) — currently a Blocking data gap (DG001), required before any safety pre-screen
- Mechanism-of-action confirmation via DrugBank API — High-severity gap (DG002)
- If the more credible signal is pursued instead — Acne Keloid (rank 5) — a targeted literature/trial search specifically on phenol peel outcomes in keloidal/hypertrophic acne scarring, since current evidence is indirect (general chemical-peel literature, not keloid-specific endpoints)
- Route-of-administration and dosage-form compatibility assessment (currently "pending" for all candidate indications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

