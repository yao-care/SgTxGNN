---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
---

# Finasteride
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

# Finasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is a 5α-reductase type II inhibitor, established in clinical practice for reducing prostate volume in benign prostatic hyperplasia (BPH) and for slowing androgen-dependent hair loss (androgenetic alopecia). The TxGNN model ranks **Ambras Type Hypertrichosis Universalis Congenita** as its top predicted new indication with a score of **99.99%**, yet this rare genetic hair disorder is non-androgen-dependent, and there are currently **0 clinical trials** and **0 publications** supporting this specific direction — the prediction is considered a knowledge graph structural artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia / Androgenetic Alopecia (established globally; not currently registered in Singapore) |
| Predicted New Indication (Rank 1) | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Finasteride inhibits 5α-reductase type II, the enzyme responsible for converting testosterone to dihydrotestosterone (DHT) primarily within the prostate and skin. By suppressing intraprostatic DHT, Finasteride reduces prostate volume — a mechanism proven across multiple Phase 3 RCTs for BPH. In androgenetic alopecia, lower scalp DHT slows the miniaturization of androgen-sensitive follicles, prolonging hair retention. These two established uses share a single unifying pharmacology: blocking androgen-driven tissue growth.

Ambras Syndrome (Ambras type hypertrichosis universalis congenita) presents an entirely different biological picture. It is caused by a chromosomal structural rearrangement at 8q22–q24 that disrupts a yet-uncharacterized locus governing hair follicle suppression. The excessive hair growth is generalized, affects androgen-independent body regions (including the face and ears in neonates), and is not regulated by DHT or androgen-receptor signalling. Finasteride's mechanism — reducing DHT to *decrease* androgen-sensitive hair growth — is pharmacologically opposed to any meaningful intervention in Ambras Syndrome; suppressing DHT cannot reverse a genetic defect in hair follicle patterning.

The TxGNN model assigned a high score to this pairing, most likely because the knowledge graph encodes several hair-disorder nodes in close proximity (androgenetic alopecia, hypertrichosis, Ambras syndrome) and Finasteride's strong connection to the hair domain propagates through graph edges regardless of biological direction. This is a well-recognised limitation of KG-based repurposing: graph proximity does not guarantee mechanistic compatibility. The mechanistic rationale for this prediction does not hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Finasteride in Ambras Type Hypertrichosis Universalis Congenita.

---

## Literature Evidence

Currently no related literature available for Finasteride in Ambras Type Hypertrichosis Universalis Congenita.

---

## Singapore Market Information

Finasteride is currently not registered with the Health Sciences Authority (HSA) of Singapore. No product authorisations, brand names, or approved indications are on record. This is notable given that the drug holds approved indications in numerous other jurisdictions (BPH and male pattern baldness in the US, EU, Japan, and Taiwan).

---

## Safety Considerations

Please refer to the package insert for safety information. Singapore-specific prescribing information (TFDA/HSA monograph warnings and contraindications) was not available at the time of this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ambras Type Hypertrichosis Universalis Congenita is a non-androgen-dependent genetic condition; Finasteride's DHT-suppression mechanism is not only irrelevant but pharmacologically opposed to treating excess hair growth that arises from a chromosomal structural defect. With zero supporting evidence (L5), no clinical basis exists to pursue this repurposing direction.

---

### Note on the Full Prediction Set

Reviewing all 10 TxGNN predictions reveals one candidate with genuine mechanistic grounding:

**Rank 7 — Prostate Calculus (TxGNN score 98.60%, Evidence Level L3, recommendation: Proceed with Guardrails)**

Prostatic calculi most commonly arise secondary to chronic outflow obstruction from BPH, which impairs ductal drainage and promotes calcification. Finasteride reduces intraprostatic DHT, shrinks the prostate gland, and improves urodynamic flow — creating conditions theoretically less conducive to calculus formation. Ten publications were retrieved linking BPH management (including medical therapy) to bladder and prostate calculi outcomes, though none used prostate calculus as a primary RCT endpoint.

---

**To proceed (recommended path: prostate calculus), the following is needed:**

- Complete MOA data from DrugBank to support the mechanistic narrative in regulatory submissions
- HSA/TFDA package insert safety data (currently unavailable) to enable a full safety assessment
- A prospective study — ideally a randomised controlled trial — examining Finasteride's effect on prostatic calculus incidence, size progression, and recurrence following endoscopic removal
- Pathway to Singapore registration: Finasteride is not currently marketed in Singapore; a regulatory dossier referencing established BPH indications from other jurisdictions (US, EU) would be a prerequisite before any new indication can be explored locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

