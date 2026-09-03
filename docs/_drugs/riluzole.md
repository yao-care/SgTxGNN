---
layout: default
title: Riluzole
parent: 僅模型預測 (L5)
nav_order: 860
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: From No Registered Indication to Bilateral Parasagittal Parieto-Occipital Polymicrogyria

## One-Sentence Summary

> Riluzole's original indication and mechanism of action are not available in the current evidence pack, and the drug is not marketed in Singapore.
> The TxGNN model's top-ranked prediction is **Bilateral Parasagittal Parieto-Occipital Polymicrogyria**,
> but this candidate is supported by **0 clinical trials** and **0 publications**, and the model's own rationale states there is no known mechanistic link to riluzole.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore license data, no original indication or MOA on file (data gap) |
| Predicted New Indication | Bilateral Parasagittal Parieto-Occipital Polymicrogyria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for riluzole is not available in this evidence pack. Based on the model's own repurposing rationale, riluzole is known externally to act via glutamate release inhibition and voltage-gated sodium channel blockade — a mechanism relevant to motor neuron excitotoxicity.

The predicted indication, bilateral parasagittal parieto-occipital polymicrogyria, is a congenital cortical malformation caused by abnormal neuronal migration during brain development. According to the model's own rationale text, there is **no known mechanistic relationship** between this condition and riluzole's glutamate/sodium-channel modulating activity. This candidate arises purely from statistical association within the knowledge graph, without mechanistic plausibility or any supporting clinical evidence.

**Note:** This same evidence pack contains a much better-supported candidate — rank 8, "amyotrophic lateral sclerosis, susceptibility to" (L1, decision stage S3, 20 supporting publications, recommendation "Proceed with Guardrails") — which aligns with riluzole's well-established pharmacology. That candidate would be a more appropriate subject for a standalone evaluation report; see Next Steps below.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information. Note that this drug currently has a **Blocking**-severity data gap on TFDA-equivalent label warnings/contraindications (DG001), meaning this candidate cannot yet proceed to a formal safety pre-assessment (S1) regardless of efficacy evidence.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (bilateral parasagittal parieto-occipital polymicrogyria) has no mechanistic plausibility, no clinical trials, and no literature support — it is a pure statistical output from the knowledge graph (Evidence Level L5). Combined with a blocking gap in drug label/safety data, there is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- Riluzole's mechanism of action (MOA) from DrugBank or equivalent source
- TFDA-equivalent product label (warnings, contraindications) to clear the blocking safety data gap
- Original indication / regulatory history for riluzole, since Singapore market data shows zero registrations
- If pursuing this drug further, prioritize evaluating **rank 8 ("amyotrophic lateral sclerosis, susceptibility to")** instead, given its L1 evidence level and 20 supporting publications — this is a substantially stronger candidate within the same evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

