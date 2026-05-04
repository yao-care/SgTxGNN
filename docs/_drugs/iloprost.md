---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Iloprost
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

# Iloprost: From Pulmonary Arterial Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Iloprost is a synthetic prostacyclin (PGI₂) analogue approved in multiple countries for the treatment of pulmonary arterial hypertension (PAH) and peripheral vascular disease. The TxGNN model ranks **Hypotrichosis Simplex of the Scalp** as its top predicted new indication, with a prediction score of **99.45%**. However, **no clinical trials or published literature** currently support this specific application, making this a pure algorithmic prediction without empirical backing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary arterial hypertension; peripheral vascular disease (not currently registered in Singapore) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on published pharmacological knowledge, Iloprost is a synthetic prostacyclin analogue that acts primarily through the IP (prostacyclin) receptor and PPAR-γ, producing pulmonary and systemic vasodilation, inhibiting smooth muscle cell proliferation, and reducing platelet aggregation. These effects form the basis for its approved use in PAH and vascular occlusive conditions.

The theoretical basis for the TxGNN prediction may involve the IP receptor's hypothetical role in promoting microvascular proliferation around hair follicles, which could indirectly support follicular survival and hair growth. However, this mechanistic link is entirely speculative. No biological experiments, animal models, or pathophysiological studies have established a connection between prostacyclin signalling and hypotrichosis simplex of the scalp.

Hypotrichosis Simplex of the Scalp is a rare, genetically-determined condition (associated with mutations in LPAR6, LIPH, and related genes governing hair follicle lipid metabolism), whose pathogenesis does not intersect with the prostacyclin pathway in any established way. The TxGNN model's high score almost certainly reflects graph topology proximity in the knowledge graph rather than a true mechanistic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Iloprost is currently **not marketed in Singapore**. No product licences or approved registrations are on record with the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While TxGNN assigns a 99.45% prediction score, there is zero empirical evidence — no preclinical studies, no clinical trials, and no published literature — supporting Iloprost's use in Hypotrichosis Simplex of the Scalp. The mechanistic link is hypothetical at best, and the disease's genetic aetiology makes a prostacyclin-based intervention biologically implausible without further foundational research.

**To proceed, the following is needed:**
- Preclinical studies (in vitro/in vivo) investigating IP receptor expression and functional role in hair follicle biology
- Basic research establishing whether prostacyclin signalling influences the lipid metabolism pathways disrupted in LPAR6/LIPH-mutant hypotrichosis
- Mechanism of action data (MOA) for Iloprost (retrievable via DrugBank API — see Data Gap DG002)
- Safety and warning data from the Singapore HSA or alternative regulatory sources (see Data Gap DG001)

> **Note for prioritisation:** This report presents TxGNN's highest-scored prediction. Among all 10 candidates in this Evidence Pack, the **PAH-associated indications** (CHD-PAH, CTD-PAH, HIV-PAH) carry substantially stronger evidence (L2–L3) with "Proceed with Guardrails" recommendations, and may represent higher-yield repurposing opportunities for Iloprost. A separate report for those indications is recommended.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

