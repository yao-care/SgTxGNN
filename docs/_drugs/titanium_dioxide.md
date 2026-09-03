---
layout: default
title: Titanium Dioxide
parent: 僅模型預測 (L5)
nav_order: 988
evidence_level: L5
indication_count: 10
---

# Titanium Dioxide
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

# Titanium dioxide: From Excipient to Model Noise — No Viable Repurposing Signal

## One-Sentence Summary

Titanium dioxide (DrugBank DB09536) is an inorganic pigment/excipient with no recorded therapeutic indication and no known pharmacological mechanism of action. TxGNN assigns near-saturated prediction scores (~99.998%) across ten disease candidates — ranging from diabetic retinopathy to multiple cataract subtypes — but **none are supported by clinical trials, and the five literature hits retrieved are all unrelated tool/method-development studies rather than therapeutic evidence.** This pattern strongly suggests knowledge-graph noise rather than a genuine repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable (no recorded therapeutic indication; used as excipient/pigment) |
| Predicted New Indication | Drug-induced osteoporosis (top rank; 9 additional candidates, mostly cataract subtypes) |
| TxGNN Prediction Score | 99.9998% (rank 1); scores cluster at 99.998–99.9998% across all 10 candidates |
| Evidence Level | L5 (model prediction only, no clinical or mechanistic support for any candidate) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Mechanism of action data for titanium dioxide is not available. Titanium dioxide is an inorganic compound used industrially and pharmaceutically as a white pigment, opacifier, and inert excipient in tablet coatings — it is not developed or used as a pharmacologically active therapeutic agent, and DrugBank does not list any approved indication for it.

Because there is no original indication and no MOA to anchor a mechanistic rationale, the relationship between titanium dioxide and any of the ten predicted diseases (drug-induced osteoporosis, diabetic retinopathy, diabetic cataract, and related eye/bone conditions) cannot be pharmacologically justified. All ten candidates in this evidence pack score within a narrow, saturated band (~0.99998–0.9999998), which is consistent with a systematic artifact of the knowledge graph — likely driven by titanium dioxide nanoparticles' frequent appearance in unrelated *research contexts* (e.g., as tools for extracellular vesicle purification or retinal imaging) rather than any therapeutic association. The clustering of near-identical, near-maximal scores across an entire disease family (all cataract subtypes) is a known TxGNN failure pattern for nodes lacking real pharmacological edges in the graph.

The five literature records retrieved for diabetic retinopathy — the only candidate with any literature — confirm this: all describe titanium dioxide nanoparticles being used as laboratory tools (EV purification substrates, retinal imaging conjugates, diagnostic phantoms) or reviewed generically as nanomedicine carriers, none as a treatment for diabetic retinopathy itself. No candidate has any clinical trial evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the ten predicted indications.

---

## Literature Evidence

Literature exists only for **diabetic retinopathy** (rank 2); all other candidates have none.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39566751](https://pubmed.ncbi.nlm.nih.gov/39566751/) | 2025 | Imaging/Diagnostic tool | Methods | TiO₂ nanoparticle–fluorescein conjugates evaluated as an imaging agent for fundus fluorescein angiography, not as a treatment for diabetic retinopathy |
| [41637842](https://pubmed.ncbi.nlm.nih.gov/41637842/) | 2026 | Review | J Trace Elem Med Biol | General review of metallic nanoparticles in diabetes mellitus; does not specifically validate TiO₂ as a diabetic retinopathy therapy |
| [38078945](https://pubmed.ncbi.nlm.nih.gov/38078945/) | 2023 | Method/Tool development | Analytical Chemistry | TiO₂ microparticles used as a purification substrate for circulating RNA/EV analysis; not a therapeutic study |
| [36197877](https://pubmed.ncbi.nlm.nih.gov/36197877/) | 2022 | Method/Tool development | Analytical Chemistry | TiO₂ microparticles used to purify plasma extracellular vesicles for metabolomic profiling of diabetic retinopathy patients; a diagnostic biomarker tool, not treatment |
| [20059246](https://pubmed.ncbi.nlm.nih.gov/20059246/) | 2009 | Instrumentation/Phantom study | J Biomed Optics | Eye phantom device for retinal oximetry calibration; unrelated to TiO₂ as a drug |

None of these papers support a therapeutic role for titanium dioxide in diabetic retinopathy.

---

## Singapore Market Information

Titanium dioxide has no drug registrations in Singapore (0 licenses; not marketed as a therapeutic product).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are available in the evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Titanium dioxide has no known therapeutic mechanism of action and no original indication to anchor a repurposing hypothesis. All ten predicted indications lack clinical trial support, and the only available literature (for diabetic retinopathy) consists exclusively of nanoparticle tool/imaging studies unrelated to treatment efficacy. The near-uniform, saturated TxGNN scores across an entire disease family (all cataract subtypes at ~0.99998) is a strong signature of knowledge-graph noise for a pharmacologically inert excipient node, not a genuine biological signal.

**To proceed, the following is needed:**
- Confirmation of whether this DrugBank entry should even be treated as a candidate for repurposing screening (recommend excluding inert excipients/pigments from future TxGNN candidate pools)
- If retained, independent mechanistic or in vitro/in vivo pharmacology data establishing any plausible biological activity of titanium dioxide relevant to bone metabolism or ocular/retinal disease
- No further evidence collection is recommended for this candidate absent such foundational data — resources are better allocated to candidates with an established original indication and MOA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

