---
layout: default
title: Pyrazinamide
parent: 僅模型預測 (L5)
nav_order: 833
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

> Pyrazinamide is a first-line antituberculosis agent, historically used as part of combination therapy for *Mycobacterium tuberculosis* infection.
> The TxGNN model predicts it may be effective for **Infectious Otitis Media**,
> but currently **no clinical trials** and **no publications** directly support this specific prediction — the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (based on drug's known antimycobacterial mechanism; no Taiwan/Singapore approved-label text is available — see Data Gaps below) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (no clinical trials, no literature) |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pyrazinamide is not available in this evidence pack (flagged as a High-severity data gap). Based on information found elsewhere in the pack, pyrazinamide is a prodrug that is converted to pyrazinoic acid, which inhibits *Mycobacterium tuberculosis* within the acidic intracellular environment of macrophages. It is a component of standard first-line antituberculosis combination regimens, not used as monotherapy.

For the top-ranked predicted indication, **infectious otitis media**, there is no direct clinical trial or literature evidence in this pack — the TxGNN score is high, but the prediction is unsupported by any real-world data (L5, model prediction only).

Notably, several **related** predicted indications in this same pack — middle ear disease (rank 2), chronic otitis media (rank 4), suppurative otitis media (rank 5), and infectious otitis interna (rank 10) — are supported by multiple case reports and case series describing **tuberculous otitis media**, a rare form of extrapulmonary tuberculosis in which *M. tuberculosis* infects the middle ear. This provides a plausible biological rationale for pyrazinamide's association with the broader "otitis media" disease cluster: the model may be capturing a real extrapulmonary-TB signal, but the specific term "infectious otitis media" has not yet been directly evidenced, and the diagnosis would need to be confirmed as tuberculous (not general bacterial/viral) in origin before pyrazinamide — always as part of standard multi-drug anti-TB therapy — would be applicable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

This drug is currently **not registered/marketed** (未上市, 0 licenses on file). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** Local regulatory label warnings and contraindications (DG001) are marked as a **Blocking** data gap in this evidence pack — this must be resolved before any S1 safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (infectious otitis media) has a high TxGNN score but zero direct clinical trial or literature support (L5). While related otitis-media terms show case-report-level evidence for tuberculous otitis media, that evidence has not been mapped to this specific predicted term, and the drug is not currently marketed locally.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain local package insert / label warnings and contraindications before any safety pre-assessment
- Resolve DG002 (High): confirm mechanism of action via DrugBank to support mechanistic-link analysis
- Clarify disease-term overlap between "infectious otitis media" and the literature-supported "tuberculous otitis media" cluster (ranks 2, 4, 5, 10) to determine if they represent the same clinical entity
- If pursued, restrict to cases with confirmed *M. tuberculosis* etiology, using pyrazinamide only as part of standard combination anti-TB therapy, not monotherapy
- Assess local registration/import pathway, since the drug currently has no market presence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

