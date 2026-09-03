---
layout: default
title: Sodium Zirconium Cyclosilicate
parent: 僅模型預測 (L5)
nav_order: 914
evidence_level: L5
indication_count: 10
---

# Sodium Zirconium Cyclosilicate
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

# Sodium Zirconium Cyclosilicate: From Hyperkalemia to Breast Fibrocystic Disease

## One-Sentence Summary

> Sodium zirconium cyclosilicate (SZC) is a non-absorbed intestinal cation-exchange agent used to lower serum potassium in hyperkalemia.
> The TxGNN model predicts it may be effective for **Breast Fibrocystic Disease**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review found no biologically plausible link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperkalemia *(inferred from mechanistic description in evidence pack; no official approved-label text available — drug not marketed in Singapore)* |
| Predicted New Indication | Breast Fibrocystic Disease |
| TxGNN Prediction Score | 93.41% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available from DrugBank (flagged as a data gap, DG002 — High severity). However, the rationale text accompanying each of the top-10 predictions consistently describes SZC as a **non-absorbed intestinal cation exchanger**: its Zr-Si lattice structure captures K⁺/NH₄⁺ in the gut lumen while releasing Na⁺/H⁺, which is consistent with SZC's known clinical role as a potassium binder in hyperkalemia management.

There is no established or plausible pharmacological pathway connecting this local, gut-restricted ion-exchange mechanism to breast fibrocystic disease, which is driven by hormonal (estrogen/progesterone) and epithelial proliferative processes. The evidence pack's own mechanistic assessment explicitly states this: *"無任何已知路徑與乳腺纖維囊性病變之激素/上皮增生機轉相關... 缺乏生物學合理性"* (no known pathway relates to the hormonal/epithelial-proliferative mechanisms of fibrocystic breast disease; biological plausibility is lacking).

This pattern repeats across predictions #2–8 (all benign breast conditions — benign mammary dysplasia, blunt duct adenosis, apocrine adenosis, breast abscess, fat necrosis, lactation disease, breast adenosis — all sharing similar TxGNN scores of ~0.88–0.93) and predictions #9–10 (rare coagulation disorders — heparin cofactor 2 deficiency, antithrombin deficiency type 2). None of these have an identified mechanistic rationale; they most likely reflect **knowledge-graph embedding proximity/noise** rather than genuine pharmacological relationships.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

This drug is not marketed in Singapore (0 registered licenses). No product authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA-level warnings and contraindications are flagged as a **Blocking** data gap (DG001) — without this data, safety review cannot proceed to Stage S1.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top-10 TxGNN-predicted indications for SZC sit at Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature. The evidence pack's own mechanistic analysis found no biologically plausible pathway linking SZC's gut-restricted cation-exchange mechanism to the predicted indications (predominantly benign breast conditions and rare coagulation disorders), suggesting these are graph-embedding artifacts rather than genuine repurposing candidates. In addition, SZC is not marketed in Singapore and a Blocking-severity data gap exists for TFDA/HSA safety labeling.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data via DrugBank API (resolves DG002)
- TFDA/HSA package insert warnings and contraindications (resolves DG001 — required before any S1 safety review)
- Independent preclinical or mechanistic evidence establishing a plausible biological link between SZC and breast tissue pathology before further investment
- Re-evaluation if new clinical trial or literature evidence emerges for any of the top-10 predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

