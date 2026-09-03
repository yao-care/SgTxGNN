---
layout: default
title: Verteporfin
parent: 僅模型預測 (L5)
nav_order: 1054
evidence_level: L5
indication_count: 10
---

# Verteporfin
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

# Verteporfin: From Photodynamic Therapy for Wet AMD to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

> Verteporfin is a benzoporphyrin-derivative photosensitizer historically used in photodynamic therapy (PDT) for neovascular (wet) age-related macular degeneration and choroidal neovascularization.
> The TxGNN model predicts it may be effective for **Mitochondrial Oxidative Phosphorylation Disorder due to Nuclear DNA Anomalies**,
> but currently **0 clinical trials** and **0 publications** support this specific direction — this is a model-generated hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in structured Singapore registrational data (drug not marketed locally). Publicly documented use is photodynamic therapy for wet AMD / choroidal neovascularization (supported by literature evidence in this pack, e.g. PMID 17579286) |
| Predicted New Indication | Mitochondrial Oxidative Phosphorylation Disorder due to Nuclear DNA Anomalies |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on publicly known pharmacology, verteporfin is a photosensitizing agent that, upon activation by a 690 nm laser, generates reactive oxygen species leading to selective occlusion of abnormal, leaky vasculature. This mechanism underlies its established use in ocular PDT for wet AMD and pathologic myopia-related CNV — a **vascular** disease process.

The top-ranked predicted indication, mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies, is a **genetic/metabolic** disease affecting cellular energy production, not a vascular pathology. There is no obvious mechanistic bridge between light-triggered vascular photothrombosis and correction of a nuclear-DNA-encoded OXPHOS defect, and no clinical trial or literature evidence in this pack substantiates such a link.

Given the absence of supporting evidence and the lack of a clear mechanistic rationale, this prediction should be treated as a preliminary knowledge-graph signal requiring independent mechanistic and preclinical validation before further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Verteporfin currently has no marketing authorization registered in Singapore (market status: **Not Marketed**, 0 licenses on file). No product-level regulatory data (dosage form, approved indication text) is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (flagged as a Blocking-severity data gap, DG001 — TFDA/HSA label warnings and contraindications have not yet been retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication has no supporting clinical trial or literature evidence (Evidence Level L5), no established mechanistic rationale linking ocular PDT vascular action to a nuclear-DNA mitochondrial disorder, and a Blocking-severity safety data gap prevents any S1 safety pre-screening.

**To proceed, the following is needed:**
- Retrieve TFDA/HSA package insert warnings and contraindications (DG001, Blocking)
- Obtain verteporfin's formal mechanism of action from DrugBank (DG002, High)
- Identify preclinical or mechanistic studies connecting verteporfin/PDT to mitochondrial OXPHOS pathways before advancing this candidate
- Consider re-evaluating lower-ranked candidates with existing literature support (e.g. rank 10, "retinal dystrophy in systemic or cerebroretinal lipidoses," which has 11 associated publications) as a more evidence-grounded alternative for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

