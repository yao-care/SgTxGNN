---
layout: default
title: Benzoyl Peroxide
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Benzoyl Peroxide
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

# Benzoyl Peroxide: From Acne Vulgaris to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Benzoyl peroxide (BPO) is a well-established topical antimicrobial and keratolytic agent widely used for acne vulgaris, exerting its effects through oxidative bactericidal activity against *Cutibacterium acnes* and mild follicular desquamation.
The TxGNN model predicts it may be effective for **Vulvar Inverted Follicular Keratosis**, a rare benign epithelial neoplasm of the follicular infundibulum.
There are currently **0 clinical trials** and **0 publications** supporting this direction, placing evidence at the minimum possible level (L5) — this candidate is not ready for further development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne Vulgaris (topical antimicrobial / keratolytic) |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on well-established pharmacological knowledge, benzoyl peroxide is a topical oxidizing agent that generates reactive oxygen species (ROS), exerting bactericidal activity against *Cutibacterium acnes* and mild keratolytic activity that promotes follicular epithelial desquamation. It is not absorbed systemically to any clinically meaningful extent.

Vulvar inverted follicular keratosis is a rare benign lesion characterized by squamous proliferation originating from the follicular infundibulum. The TxGNN model's high score likely derives from the knowledge graph's "follicular keratinization abnormality" node, which BPO is connected to via its keratolytic properties. At a superficial level, a drug that modulates follicular keratinization could theoretically influence follicular keratotic lesions — hence the model's prediction.

However, the anatomical gap is critical. BPO is designed for sebaceous gland–rich skin (face, chest, back), and its tolerance on vulvar mucosa has never been established. The vulvar epithelium has significantly different permeability, pH, and irritant sensitivity. There is no mechanistic evidence that BPO's keratolytic activity would be effective or safe for a benign follicular neoplasm at this anatomical site. This prediction most likely reflects KG over-generalization rather than a genuine therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Benzoyl peroxide is **not currently registered or marketed in Singapore**. No HSA authorization records are available.

---

## Safety Considerations

- **Photosensitizing effect**: BPO enhances UV-induced skin damage. This is clinically relevant because two of the top 10 TxGNN predictions (phototoxic dermatitis, hydroa vacciniforme) involve photosensitive conditions — BPO would be **contraindicated**, not therapeutic, in those contexts.
- **Contact sensitization**: BPO is a recognised contact allergen. Allergic contact dermatitis is a documented adverse effect with prolonged use, confirmed by published review data (PMID 25982754).
- **Mucosal irritation**: Application to mucosal surfaces (directly relevant to the vulvar indication) poses significant irritation and tissue damage risk not present with standard dermal application. No mucosal safety data exist.

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (vulvar inverted follicular keratosis) has zero supporting clinical or preclinical evidence, a significant anatomical safety concern regarding mucosal application, and no mechanistic pathway beyond KG generalization. The overall candidate profile across all 10 predictions is weak — 9 of 10 indications are Hold/L5, and several represent mechanistic contradictions (BPO as a cause of phototoxic dermatitis and contact sensitization, not a treatment).

The single indication worth retaining for further discussion is **Rank 4: Acne Keloid (L4, Research Question)** — BPO's upstream anti-inflammatory activity against *C. acnes* provides indirect rationale for reducing the inflammatory trigger of acne keloidalis nuchae. This would be framed as **preventive** intervention on upstream follicular inflammation, not treatment of established keloid. Even here, the clinical trial found (NCT07015931) studies retinoids against acne vulgaris, not BPO against keloid, offering only indirect contextual support.

**To proceed with the acne keloid research question, the following is needed:**
- Formal mechanism of action data from DrugBank (DG002 remediation)
- Safety profile confirmation for prolonged topical use in keloid-prone skin types (Fitzpatrick III–V)
- A prospectively designed pilot study framed as "BPO for prevention of acne keloidalis nuchae recurrence" in at-risk populations
- MOA gap (DG002) and safety gap (DG001) must both be resolved before S1 safety screening can proceed

> ⚠️ **Research note only.** This report is intended for exploratory research purposes. All predictions require clinical validation before any therapeutic application. This document does not constitute medical advice.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

