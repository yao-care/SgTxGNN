---
layout: default
title: Oxymetholone
parent: 僅模型預測 (L5)
nav_order: 744
evidence_level: L5
indication_count: 10
---

# Oxymetholone
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

# Oxymetholone: From Aplastic Anemia to Seborrheic Dermatitis

## One-Sentence Summary

Oxymetholone is a 17α-alkylated anabolic-androgenic steroid whose established clinical use is stimulating red blood cell production in aplastic anemia. The TxGNN model predicts a possible link to **Seborrheic Dermatitis**, but this is currently based on knowledge-graph topology alone — **0 clinical trials** and **0 publications** support this specific indication, and the underlying rationale actually points toward a risk of aggravation rather than treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Aplastic anemia (per known pharmacology noted in the evidence rationale; not derived from a Singapore registration, as the drug is unmarketed there) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.05% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Oxymetholone is not available in the evidence pack (MOA: Data Gap). Based on known information cited alongside the prediction, Oxymetholone is a synthetic anabolic-androgenic steroid whose proven clinical efficacy is in stimulating erythropoiesis for aplastic anemia — it is not part of a recognized dermatological drug class.

The mechanistic link offered for seborrheic dermatitis is that androgen receptor activation increases sebaceous gland secretion and keratinocyte proliferation, which theoretically overlaps with the sebaceous-gland pathophysiology of seborrheic dermatitis. However, this overlap points in the **wrong direction**: increased androgenic sebum production is more consistent with worsening or triggering seborrheic dermatitis than treating it. The TxGNN score reflects graph-topological similarity between disease/drug nodes, not a validated therapeutic hypothesis, and no clinical or literature evidence currently exists to support a treatment effect.

Given the theoretical mechanism runs counter to a therapeutic rationale, and no supporting trials or publications exist, this candidate should be treated as a low-confidence, hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Oxymetholone is not marketed in Singapore — no registration records are available (total_licenses = 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on knowledge-graph similarity (L5, S0) with zero supporting clinical trials or literature, and the proposed androgenic mechanism plausibly worsens rather than treats seborrheic dermatitis. The drug is also unmarketed in Singapore, with no safety or MOA data currently available.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently a Blocking data gap
- Verified mechanism of action data from DrugBank or primary literature
- Preclinical or case-level evidence specifically evaluating androgens in seborrheic dermatitis, including assessment of sebum-stimulation risk
- Confirmation of regulatory pathway, since the drug has no existing Singapore registration to leverage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

