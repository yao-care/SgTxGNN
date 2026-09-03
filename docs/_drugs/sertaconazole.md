---
layout: default
title: Sertaconazole
parent: 僅模型預測 (L5)
nav_order: 899
evidence_level: L5
indication_count: 10
---

# Sertaconazole
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

# Sertaconazole: From Superficial Fungal Skin Infections to Dermatophytosis of Groin and Perianal Area

## One-Sentence Summary

Sertaconazole is a topical imidazole antifungal established for superficial fungal skin infections (dermatophytosis, cutaneous candidiasis, pityriasis versicolor), though it is not currently registered in Singapore.
The TxGNN model's top-ranked prediction is **Dermatophytosis of Groin and Perianal Area** (tinea cruris) with a prediction score of **99.98%**,
but this specific indication currently has **no clinical trials or literature** directly attached in the evidence pack — the highest confidence score is not yet backed by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; per literature (PMID 19275277), internationally indicated for superficial skin mycoses (dermatophytosis, cutaneous candidiasis, pityriasis versicolor) |
| Predicted New Indication | Dermatophytosis of groin and perianal area (tinea cruris) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking data gap in this evidence pack). Based on literature evidence attached to related predictions in this pack (e.g., PMID 19275277, PMID 23566144), Sertaconazole is an imidazole-class antifungal that inhibits ergosterol biosynthesis and disrupts fungal cell wall integrity — a mechanism directly applicable to dermatophyte and yeast infections of the skin.

The predicted new indication, dermatophytosis of groin and perianal area (commonly known as tinea cruris), belongs to the same disease family as sertaconazole's well-established uses: tinea corporis, tinea pedis, and cutaneous candidiasis. Mechanistically, there is no meaningful distinction between dermatophyte infection at different body sites — the pathogen biology and drug action are the same. This is supported indirectly by strong evidence at rank 2 (tinea corporis, L2, 20 publications including multiple RCTs) and rank 3 (cutaneous candidiasis, L2, Phase II trial), which validate sertaconazole's efficacy across the broader dermatophytosis/candidiasis spectrum.

However, for the specific rank-1 indication (groin/perianal dermatophytosis), the evidence pack currently contains **zero clinical trials and zero literature entries** directly tied to this term — likely because trial/publication indexing uses "tinea cruris" rather than the exact TxGNN disease ontology label. The mechanistic plausibility is high, but direct evidence has not yet been located and mapped.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: Closely related indications within this same drug's prediction set do have strong literature support — see "Related High-Evidence Indications" below.*

---

## Singapore Market Information

Sertaconazole is not currently registered in Singapore (0 licenses on file). No authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available for this drug — flagged as a Blocking data gap requiring TFDA/HSA label retrieval.)

---

## Related High-Evidence Indications (Supporting Context)

Although the top-ranked prediction lacks direct evidence, several other TxGNN-predicted indications for sertaconazole in this evidence pack are well supported and may warrant separate evaluation:

| Rank | Disease | TxGNN Score | Evidence Level | Trials/Literature | Recommendation |
|------|---------|-------------|-----------------|-------------------|-----------------|
| 2 | Tinea corporis | 99.94% | L2 | 20 publications (multiple RCTs) | Proceed with Guardrails |
| 3 | Cutaneous candidiasis | 99.63% | L2 | 4 publications (incl. Phase II trial) | Proceed with Guardrails |
| 7 | Superficial mycosis | 99.55% | L2 | 14 publications | Proceed with Guardrails |
| 9 | Pityriasis versicolor | 99.45% | L2 | 6 publications (incl. clinical trial) | Proceed with Guardrails |

Ranks 4, 5, 6, 8, and 10 (Majocchi granuloma, ectothrix/endothrix infectious disease, dermatophytosis of scalp/beard, tinea profunda) are L5 (model prediction only, no usable evidence) and are recommended **Hold**. Note: rank 8's attached literature was almost entirely irrelevant (beard reconstruction surgery, unrelated topics) and should be treated as noise rather than supporting evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (dermatophytosis of groin and perianal area) has a very high TxGNN confidence score but zero directly attached clinical trials or literature, placing it at Evidence Level L5. Combined with two Blocking/High-severity data gaps (TFDA/HSA label warnings and mechanism of action), this indication is not yet ready to advance past initial screening.

**To proceed, the following is needed:**
- Retrieve TFDA/HSA-equivalent package insert (warnings, contraindications) — currently a Blocking gap
- Retrieve confirmed mechanism of action from DrugBank — currently a High-severity gap
- Re-run literature/trial search using synonym term "tinea cruris" to check whether evidence exists under alternate naming
- Consider re-prioritizing evaluation toward rank 2 (tinea corporis) and rank 3 (cutaneous candidiasis), which already meet L2 evidence with multiple RCTs and could proceed with guardrails sooner
- Confirm Singapore regulatory pathway, since sertaconazole currently has no local registration (0 licenses)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

