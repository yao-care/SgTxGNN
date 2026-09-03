---
layout: default
title: Tyrothricin
parent: 僅模型預測 (L5)
nav_order: 1028
evidence_level: L5
indication_count: 10
---

# Tyrothricin
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

# Tyrothricin: From Topical Anti-infective Use to Insomnia

## One-Sentence Summary

> Tyrothricin (gramicidin + tyrocidine complex) is a peptide antibiotic whose modern clinical use is restricted to topical applications (oral cavity, skin) due to systemic toxicity (hemolysis, nephrotoxicity) when absorbed.
> The TxGNN model's top-ranked prediction is **Insomnia**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model itself flags no known mechanistic link between the drug's membrane-disruption/pore-forming action and CNS sleep pathways (GABA, melatonin, orexin).
> This is a pure knowledge-graph embedding signal with no translational or clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered in this evidence pack; historically used topically (oral cavity/skin) as an antiseptic peptide — no license or indication-text data available |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 91.52% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the evidence pack's own mechanistic assessment, tyrothricin's known pharmacology — bacterial cell membrane disruption and gramicidin-mediated cation channel formation — has **no established relationship** with the central nervous system pathways that regulate sleep (GABAergic signaling, melatonin, orexin). No mechanistic hypothesis, preclinical model, or clinical observation connects this drug to insomnia.

The rationale text accompanying this prediction explicitly states that the association is "purely a TxGNN knowledge-graph embedding similarity, with no clinical or translational evidence." In other words, the model has identified a statistical proximity in the embedding space, not a biologically plausible repurposing candidate.

By contrast, it is worth noting that lower-ranked predictions in this same evidence pack — particularly **enterocolitis** and **gastroenteritis** — have a much more coherent mechanistic story (tyrothricin/gramicidin's direct antibacterial action against enteric pathogens, supported by historical dysentery treatment literature from the 1940s–50s). These represent a more defensible research direction than the top-ranked insomnia prediction, though they too require modern re-validation given the drug's known systemic toxicity profile.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Tyrothricin has no current marketing authorization registered in Singapore (0 licenses on file). No product, dosage form, or approved indication data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** A Blocking-severity data gap has been identified — TFDA/HSA label warnings and contraindications have not yet been retrieved for this drug, and this must be resolved before any Stage 1 safety assessment can proceed. Drug-drug interaction data was also queried with no results found (0 interactions on file).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (insomnia) has no clinical trials, no literature, and no plausible mechanistic link — it is classified as L5 evidence (model prediction only) with an explicit "Hold" recommendation from the scoring engine itself. Combined with a Blocking-severity gap in basic drug safety data (no label warnings/contraindications available), this candidate cannot advance to any substantive evaluation stage.

**To proceed, the following is needed:**
- Retrieve TFDA/HSA package insert data (warnings, contraindications) — currently Blocking
- Confirm mechanism of action via DrugBank or primary literature
- If pursuing repurposing further, redirect research priority toward the gastroenteritis/enterocolitis hypothesis (L3–L4 evidence, historical dysentery treatment literature), which has a coherent mechanistic rationale, rather than the top-ranked but mechanistically unsupported insomnia signal
- Modern safety re-evaluation of systemic exposure risk (hemolysis, nephrotoxicity) before considering any indication requiring non-topical administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

