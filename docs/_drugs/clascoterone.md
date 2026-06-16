---
layout: default
title: Clascoterone
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Clascoterone
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

# Clascoterone: From Acne Vulgaris to Candidiasis

## One-Sentence Summary

Clascoterone is a topical androgen receptor (AR) antagonist, originally developed and approved for the treatment of acne vulgaris.
The TxGNN model predicts it may be effective for **Candidiasis** with a prediction score of **94.82%**,
however **no clinical trials and no supporting publications** currently exist for this indication — this is a model-only prediction requiring significant caution.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris (topical androgen receptor antagonist; not registered in Singapore) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 94.82% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Clascoterone (Winlevi®) is a first-in-class topical androgen receptor antagonist. It competitively inhibits dihydrotestosterone (DHT) binding to the androgen receptor in sebaceous glands and hair follicles, thereby reducing sebum production and the downstream inflammatory cascade responsible for acne lesions. Its systemic exposure after topical application is extremely low (Cmax ~0.3 ng/mL), which limits any off-target systemic effects.

The mechanistic bridge between AR antagonism and candidiasis is weak. Candidiasis is a fungal infection caused by *Candida* species, and Clascoterone has no known antifungal properties, does not target fungal cell wall synthesis, membrane ergosterol pathways, or any other established antifungal mechanism. Androgen receptors play an indirect role in immune modulation, and androgens are known to influence susceptibility to certain infections — but this represents a distal and unproven pathway.

The high TxGNN score (94.82%) most likely reflects non-specific co-activation of shared skin disease nodes within the knowledge graph, rather than a true mechanistic or pharmacological relationship. The model's own repurposing rationale flags this as a probable false positive driven by the topological proximity of dermatological disease nodes in the knowledge graph, rather than any direct biological mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Clascoterone in candidiasis.

---

## Literature Evidence

Currently no related literature available for Clascoterone in candidiasis.

---

## Singapore Market Information

Clascoterone is not registered or marketed in Singapore. No product licenses are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA label warnings and contraindications were identified as data gaps (severity: Blocking) and drug interaction data returned no results in the current Evidence Pack. A full safety assessment cannot be completed until the product monograph is retrieved and reviewed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but the mechanistic link between androgen receptor antagonism and fungal candidiasis is biologically implausible without supporting data. With zero clinical trials, zero supporting publications, no Singapore registration, and no available safety data, there is insufficient basis to advance this candidate at this time. This prediction is classified as L5 (model-only) and is a probable knowledge graph false positive arising from shared dermatological disease nodes.

**To proceed, the following would be needed:**
- Retrieve and review the full product monograph (TFDA/FDA label) for warnings, contraindications, and known drug interactions
- Obtain confirmed mechanism of action data from DrugBank or primary literature
- Conduct a hypothesis-generating literature search specifically examining androgen receptor signalling and *Candida* immune evasion or susceptibility
- If a plausible biological rationale is established, commission preclinical (in vitro/in vivo) studies to test antifungal activity or immunomodulatory effects relevant to candidiasis
- Consider whether any of the other TxGNN-ranked candidates (e.g., **Adrenal Gland Hyperfunction**, rank 9, which has the strongest mechanistic connection given Clascoterone's structural relationship to cortexolone) represent a more scientifically justified repurposing priority

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

