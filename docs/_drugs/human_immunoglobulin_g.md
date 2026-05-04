---
layout: default
title: Human Immunoglobulin G
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Human Immunoglobulin G
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

# Human Immunoglobulin G: From Immune-Mediated Disorders to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Human immunoglobulin G (IVIG) is a pooled plasma-derived antibody preparation with broad immunomodulatory properties, commonly used for immune deficiency and autoimmune conditions; however, no registered indications are documented in the Singapore regulatory database.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy (NPDR)**, with **no clinical trials** and only **1 publication** (a biomarker study) currently available to support this direction.
The evidence base is limited exclusively to a model prediction, and the sole available study characterises IgG Fc glycosylation as a diagnostic biomarker rather than a therapeutic target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication data available in Singapore |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this submission. Based on known pharmacological information, Human immunoglobulin G (IVIG) is a concentrated preparation of polyclonal immunoglobulin G antibodies pooled from healthy human donors. Its established efficacy across immune-mediated conditions involves multiple pathways: Fc receptor modulation, complement regulation, anti-idiotype neutralisation, and potent anti-inflammatory effects driven by highly sialylated IgG fractions. These mechanisms collectively suppress aberrant immune activation.

The biological rationale linking IVIG to severe nonproliferative diabetic retinopathy (NPDR) is currently speculative. The sole supporting publication (PMID 40204274) reports that the IgG Fc N-glycosylation profile — specifically the degree of galactosylation and sialylation — differs significantly across patients with no DR, NPDR, and proliferative DR. This is an exploratory diagnostic biomarker finding about the patient's *endogenous* IgG, not evidence for therapeutic IVIG administration.

There is theoretical plausibility in that highly sialylated IVIG (as found in high-dose intravenous immunoglobulin therapy) carries known anti-inflammatory properties that could theoretically attenuate the microvascular inflammatory cascade underlying diabetic retinopathy. However, this mechanistic bridge has not been tested in any clinical or preclinical study targeting NPDR specifically. The high TxGNN score most likely reflects the model's recognition of IgG's broad immunomodulatory role within its knowledge graph, rather than disease-specific empirical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40204274](https://pubmed.ncbi.nlm.nih.gov/40204274/) | 2025 | Biomarker Study | Molecular & Cellular Proteomics | IgG Fc N-glycosylation patterns (galactosylation, sialylation) differ between 47 NDR, 51 NPDR, and 62 PDR patients using mass spectrometry; findings propose disease-specific IgG glycoforms as potential diagnostic biomarkers — not a therapeutic intervention study |

---

## Singapore Market Information

Human immunoglobulin G (DrugBank ID: DB00028) is not currently registered or marketed in Singapore. No product licences are on record in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is confined to a single exploratory biomarker study; no clinical or preclinical studies support therapeutic IVIG use in severe nonproliferative diabetic retinopathy, and the drug carries no Singapore market registration, making near-term clinical translation infeasible.

**To proceed, the following is needed:**
- Complete mechanism of action documentation (full DrugBank profile including pharmacodynamics and known targets)
- Clarification of whether TxGNN's prediction reflects polyclonal IVIG or IgG-class monoclonal antibodies (e.g., anti-VEGF agents such as faricimab or bevacizumab), as model class conflation is a likely confound
- Preclinical studies specifically testing IVIG in diabetic retinopathy animal models
- Safety profile documentation — key warnings, contraindications, and drug interaction data from the approved package insert
- Singapore regulatory pathway assessment for IVIG registration before any clinical feasibility evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

