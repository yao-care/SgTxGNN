---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
---

# Ioversol
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

# Ioversol: From Diagnostic Imaging to Osteoarthritis

## One-Sentence Summary

Ioversol is a water-soluble, non-ionic iodinated contrast medium used exclusively as a diagnostic imaging agent for radiographic procedures including CT, angiography, and urography — it carries no approved therapeutic indications.
The TxGNN model's top-ranked prediction is **osteoarthritis susceptibility** (99.67%), though this represents a genetic predisposition phenotype rather than a directly druggable condition; the more clinically relevant Rank 2 prediction is **osteoarthritis** (99.63%), supported by **4 clinical trials** and **1 publication** — however, all of these investigate Lipiodol-based genicular artery embolization, not Ioversol's direct therapeutic activity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diagnostic imaging contrast enhancement (radiographic/CT procedures) |
| Predicted New Indication | Osteoarthritis Susceptibility (Rank 1) / Osteoarthritis (Rank 2) |
| TxGNN Prediction Score | 99.67% (Rank 1) / 99.63% (Rank 2) |
| Evidence Level | L5 (Rank 1) / L4 (Rank 2) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, Ioversol is a water-soluble, non-ionic, low-osmolar iodinated contrast medium whose sole clinical function is diagnostic imaging — it enhances X-ray attenuation via its high iodine content to provide contrast in CT scans, angiography, and other radiographic procedures. It carries no anti-inflammatory, chondroprotective, analgesic, or immunomodulatory properties of any kind.

The top-ranked TxGNN prediction, **osteoarthritis susceptibility**, represents a genetic predisposition phenotype driven by variants in genes such as GDF5 and ALDH1A2 — this is not a pharmacologically targetable disease state but rather a heritable trait. Ioversol has no gene-modifying or epigenetic regulatory mechanism, and the high prediction score most likely reflects short-distance proximity to the osteoarthritis node within the TxGNN knowledge graph topology rather than a genuine mechanistic prediction.

The Rank 2 prediction, **osteoarthritis**, has a marginally more plausible contextual connection: iodinated contrast media are used as procedural adjuncts during genicular artery embolization (GAE), an emerging interventional therapy for knee OA pain that targets synovial neovascularization. However, all current GAE clinical trials use **Lipiodol** (ethiodized oil) — an oil-based emulsion with dual embolic and contrast properties — which is chemically and mechanistically distinct from Ioversol's water-soluble, non-embolic formulation. In any GAE procedure, Ioversol's role would be inert vessel visualization only, not therapeutic contribution.

---

## Clinical Trial Evidence

> ⚠️ **Important note**: The top-ranked prediction (osteoarthritis susceptibility, Rank 1) has no registered clinical trials. The four trials below are associated with the Rank 2 prediction (osteoarthritis) and involve genicular artery embolization — however, all use Lipiodol or ethiodized oil as the investigational embolization agent, not Ioversol itself.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04733092](https://clinicaltrials.gov/study/NCT04733092) | Phase 1 | Completed | 22 | Safety and efficacy of Lipiodol emulsion embolization for inflammatory hypervascularization in knee OA and periarticular pain; first-in-man pain relief validation |
| [NCT06497140](https://clinicaltrials.gov/study/NCT06497140) | Phase 3 | Recruiting | 130 | Multicenter randomized sham-controlled RCT of GAE using ethiodized oil-based emulsion for symptomatic knee OA; currently the highest-quality trial design in the GAE field |
| [NCT06611007](https://clinicaltrials.gov/study/NCT06611007) | Phase 1/2 | Recruiting | 15 | Pilot study evaluating safety and efficacy of Lipiodol® arterial embolization for symptomatic digital (hand) OA refractory to conventional treatment |
| [NCT06859164](https://clinicaltrials.gov/study/NCT06859164) | Phase 2 | Recruiting | 50 | NIH-NIAMS funded pilot sham-controlled RCT of GAE for symptomatic knee OA; assessing enrollment feasibility and pain reduction (KOOS pain subscore) at 3 months |

---

## Literature Evidence

> ⚠️ **Important note**: The top-ranked prediction (osteoarthritis susceptibility, Rank 1) has no supporting literature. The publication below is associated with the Rank 2 prediction (osteoarthritis) but evaluates Lipiodol-based embolization — not Ioversol as a therapeutic agent.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Phase 1 RCT | Diagnostic and Interventional Imaging | LipioJoint-1 trial: evaluated safety and efficacy of transient genicular artery embolization using an ethiodized oil-based emulsion for knee OA; demonstrated proof-of-concept for GAE as an OA pain intervention |

---

## Singapore Market Information

Ioversol currently has no HSA registrations in Singapore and is not marketed. No authorized product table can be generated.

---

## Safety Considerations

No Singapore-registered package insert is available. Please refer to the international prescribing information (Optiray®, Guerbet) for full safety data.

The following considerations are relevant for iodinated contrast media as a class:

- **Renal toxicity**: Risk of contrast-induced acute kidney injury; pre-procedure renal function assessment (eGFR) and adequate hydration are standard practice
- **Hypersensitivity reactions**: Anaphylactoid reactions are possible; emergency management protocols should be in place at administration sites
- **Hemoglobinopathy patients**: Available safety data (PMID 22195536) indicate that modern low- and iso-osmolar iodinated contrast agents show less in vitro erythrocyte sickling compared to older ionic agents, though clinical monitoring in patients with sickle cell disease remains warranted

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ioversol is a diagnostic imaging agent with no established therapeutic mechanism for osteoarthritis, joint disease, or any of the other TxGNN-predicted conditions. The high prediction scores for osteoarthritis susceptibility and osteoarthritis most likely reflect knowledge graph topology artifacts (proximity to the OA node cluster) rather than genuine biological plausibility. All available clinical evidence pertains to Lipiodol-based GAE — a chemically and mechanistically distinct intervention that cannot be extrapolated to support Ioversol repurposing.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis explaining how a non-embolic, water-soluble contrast agent could exert therapeutic benefit in OA independent of its imaging role
- In vitro or preclinical evidence for any direct pharmacological activity on joint tissue, synovium, or inflammatory pathways
- KG graph analysis to determine whether the high TxGNN scores represent a genuine biological signal or an artifact of osteoarthritis node centrality in the graph
- If the broader goal is to evaluate GAE as an OA intervention, the relevant investigational product is **Lipiodol** or microparticle-based embolic agents — not Ioversol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

