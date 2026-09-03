---
layout: default
title: Piperazine
parent: 僅模型預測 (L5)
nav_order: 788
evidence_level: L5
indication_count: 10
---

# Piperazine
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

# Piperazine: From Anthelmintic Therapy to Echinococcus granulosus Infection

## One-Sentence Summary

> Piperazine is a classical anthelmintic historically used against intestinal roundworm and pinworm infections (no official Singapore registry indication text is on file for this drug).
> The TxGNN model predicts it may be effective for **Echinococcus granulosus infectious disease (hydatid disease)**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanism is pharmacologically inconsistent with the target parasite.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no Singapore market authorization exists; piperazine is historically known as an anthelmintic for roundworm/pinworm infections (general pharmacology background, not registry data) |
| Predicted New Indication | Echinococcus granulosus infectious disease |
| TxGNN Prediction Score | 97.74% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, registry-confirmed mechanism of action data for piperazine is not available in this evidence pack. Based on general pharmacological literature, piperazine is understood to act as a **GABA-gated chloride channel agonist**, causing flaccid paralysis of the neuromuscular system in nematodes (roundworms, pinworms), which are then expelled by normal intestinal peristalsis.

However, *Echinococcus granulosus* is a **cestode (tapeworm)**, not a nematode. Cestode neuromuscular pharmacology differs substantially from that of nematodes, and piperazine has no established historical efficacy against cestode infections. The evidence pack's own mechanistic assessment explicitly flags this as a weak, indirect analogy rather than a biologically grounded hypothesis — the prediction appears to be driven by graph-level proximity in the knowledge graph (e.g., shared "anthelmintic" or "antiparasitic" category nodes) rather than a validated pharmacological pathway.

No clinical trials or published studies link piperazine directly to *E. granulosus* treatment, and no in vitro or animal data specific to piperazine (as opposed to related anthelmintics) were retrieved. This combination — high model score, but mechanistic inconsistency and a complete absence of supporting evidence — is characteristic of a low-confidence, exploratory-only signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Piperazine currently holds **no market authorization in Singapore** (total registrations: 0). No licensed products, dosage forms, or approved indication text are on file for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Additional Notes on Other Predicted Indications

This evidence pack is a multi-indication candidate covering 10 TxGNN predictions for piperazine. Two points are worth flagging for anyone reviewing the full candidate set:

- **Cystic echinococcosis (rank 10)** reached a higher evidence tier (**L4, decision stage S1, "Research Question"**) based on decades-old in vitro screening literature testing various agents (including piperazine-related compounds) against hydatid cyst membranes and scolices. This is the only candidate in the set that clears Hold status, though the historical literature requires manual verification to confirm piperazine itself (versus related compounds) was the tested agent.
- **Malaria (rank 5)** should be disregarded as evidence. The 20 literature entries retrieved for this candidate almost entirely concern **piperaquine**, a structurally distinct bisquinoline antimalarial, not **piperazine**. This is a likely drug-name string-matching artifact in the literature pipeline and should be corrected at the data-cleaning stage rather than treated as repurposing evidence.
- All remaining candidates (echinococcus granulosus infection, citrullinemia types I, mastocytosis variants, urea cycle disorder) are **L5, Hold**, with no mechanistic rationale, no clinical trials, and literature — where present — unrelated to piperazine specifically.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no clinical, observational, or drug-specific preclinical evidence supporting piperazine's use in *Echinococcus granulosus* infection, and the proposed nematocidal mechanism does not plausibly extend to cestode biology. The drug also has no current market presence in Singapore.

**To proceed, the following is needed:**
- Confirmed, registry-sourced mechanism of action (MOA) data for piperazine
- Direct in vitro or in vivo testing of piperazine (not related compounds) against *Echinococcus* species
- Manual verification of the rank-10 cystic echinococcosis literature (PMID 15269042, 14044745, 24822340, 14183098, 1758368, 4477636) to confirm piperazine was an actual tested agent — this is the more promising lead within the candidate set and warrants prioritized follow-up over the rank-1 prediction
- TFDA/regulatory safety data (key warnings, contraindications, DDI) currently marked as data gaps in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

