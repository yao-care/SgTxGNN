---
layout: default
title: Imipenem
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Imipenem
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

# Imipenem: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Imipenem is a broad-spectrum carbapenem antibiotic originally used for the treatment of serious bacterial infections caused by susceptible gram-positive and gram-negative organisms.
The TxGNN model predicts it may be effective for **Diffuse Scleroderma**,
however, **no clinical trials** and **no publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (broad-spectrum gram-positive and gram-negative coverage) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known information, Imipenem is a carbapenem β-lactam antibiotic that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBP1a, PBP1b, PBP2, and PBP3), resulting in broad-spectrum bactericidal activity against serious gram-positive and gram-negative pathogens. It is typically administered intravenously in combination with cilastatin (a renal dehydropeptidase inhibitor that prevents tubular degradation of imipenem).

Diffuse scleroderma (systemic sclerosis, dcSSc) is an autoimmune fibrotic disease characterised by widespread skin and visceral fibrosis driven by TGF-β signalling, vascular injury, and B-cell/T-cell autoimmune dysregulation. These pathological mechanisms share no known overlap with imipenem's antibacterial mode of action.

While emerging research has proposed that gut microbiome dysbiosis may play a role in scleroderma pathogenesis—potentially offering a speculative indirect link to antibiotic therapy—there is currently no clinical or preclinical evidence demonstrating that carbapenem antibiotics confer any therapeutic benefit in this condition. The exceptionally high TxGNN score (0.9999) most plausibly reflects a spurious association within the knowledge graph, rather than a genuine biological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Imipenem has no authorised products registered in Singapore (0 licences on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No biological plausibility connects imipenem's antibacterial mechanism to the autoimmune and fibrotic pathogenesis of diffuse scleroderma, and the complete absence of supporting clinical trials or published literature renders this prediction unsupportable at this stage.

**To proceed, the following is needed:**
- A mechanistic hypothesis linking imipenem (or the carbapenem class broadly) to scleroderma-relevant biology (e.g., microbiome-mediated immune modulation, gut dysbiosis correction)
- At least one preclinical study demonstrating any relevant effect in an animal model of systemic sclerosis
- Knowledge graph audit to determine whether the TxGNN high score arises from a spurious topological association rather than curated biological evidence
- Full MOA data retrieval from DrugBank (currently a data gap) to enable proper mechanistic analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

