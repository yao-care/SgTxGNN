---
layout: default
title: Bifonazole
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Bifonazole
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

# Bifonazole: From Superficial Fungal Infections to Pulmonary Hypertension

## One-Sentence Summary

Bifonazole is a broad-spectrum topical imidazole antifungal agent, classically used for the treatment of superficial fungal infections of the skin (dermatomycoses including tinea and cutaneous candidiasis).
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with a prediction score of 96.30%.
However, there are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction, and the proposed mechanistic rationale is highly speculative.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Superficial fungal infections (dermatomycoses) — no Singapore HSA-registered indications on file |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 96.30% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the Evidence Pack (data gap DG002). Based on established pharmacological knowledge, Bifonazole is an imidazole antifungal that inhibits fungal CYP51A1 (lanosterol 14α-demethylase), disrupting ergosterol biosynthesis in the fungal cell membrane. This renders it effective against a broad range of dermatophytes and yeasts. Its clinical use has been confined to topical skin preparations.

The TxGNN-hypothesised pathway connecting Bifonazole to pulmonary hypertension runs as follows: CYP enzyme inhibition → altered arachidonic acid metabolism → pulmonary vascular tone modulation. This is a distant extrapolation. Certain azole antifungals (notably ketoconazole) have demonstrated off-target inhibition of mammalian CYP enzymes involved in prostacyclin and thromboxane synthesis, and this has attracted some research interest in vascular biology. However, there is no published evidence that Bifonazole specifically inhibits pulmonary vascular CYP isoforms at clinically relevant concentrations.

A further critical barrier is pharmacokinetics. Bifonazole is a topical-only agent with minimal systemic absorption. There is no established route of administration that would deliver therapeutically meaningful concentrations to the pulmonary vasculature. The high TxGNN score most likely reflects knowledge graph signal propagation through shared CYP-related nodes rather than genuine mechanistic or clinical plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Bifonazole is not currently registered with the Health Sciences Authority (HSA) of Singapore. No product licences are on file, and the drug has no approved indications in the Singapore market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (96.30%), the proposed link between Bifonazole and pulmonary hypertension lacks mechanistic foundation, has zero supporting clinical or preclinical literature, and is pharmacokinetically implausible given the drug's exclusively topical route of administration. The drug is also not marketed in Singapore, and key safety data (warnings, contraindications, MOA profile) remain unavailable.

**To proceed, the following is needed:**
- Pharmacokinetic data confirming whether any systemic route of administration can achieve lung-tissue concentrations adequate for vascular CYP inhibition
- In vitro studies confirming Bifonazole's activity on mammalian pulmonary vascular CYP isoforms (specifically those involved in prostacyclin/thromboxane pathways)
- Complete safety profile: package insert warnings, contraindications, and drug-drug interaction screening
- Preclinical efficacy data in pulmonary hypertension animal models before any further investment is considered

---

> **⚑ Higher-Priority Repurposing Candidate Flagged**
>
> Among the 10 TxGNN predictions reviewed for this evidence pack, **Mycotic Corneal Ulcer (Fungal Keratitis)** (Rank 7; TxGNN score 93.29%; Evidence Level **L4**; Decision Stage **S1**) is the only indication with a mechanistically sound rationale. Bifonazole's CYP51A1 inhibition directly targets the same fungal pathway responsible for Aspergillus, Fusarium, and Candida keratitis. Other azoles (voriconazole, fluconazole) are already used clinically for this indication, providing a clear regulatory and clinical precedent. Recommended immediate next steps for this candidate: (1) in vitro MIC testing against common corneal fungal pathogens; (2) ocular local-tolerance assessment for an ophthalmic formulation; (3) literature search specifically for "bifonazole keratitis" or "bifonazole eye." This candidate merits a dedicated full evidence review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

