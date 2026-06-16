---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Erdafitinib
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

# Erdafitinib: From Urothelial Carcinoma to Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib (Balversa) is a pan-FGFR (fibroblast growth factor receptor 1–4) inhibitor approved for locally advanced or metastatic urothelial carcinoma harboring FGFR2/3 alterations.
The TxGNN model predicts potential therapeutic utility in **Pulmonary Hypertension** with a score of **99.38%**, however **no clinical trials and no published literature** have been identified to support this direction — this remains a purely model-driven hypothesis at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma with FGFR2/3 gene alterations |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on publicly known information, erdafitinib is a selective, orally bioavailable pan-FGFR inhibitor that targets FGFR1, FGFR2, FGFR3, and FGFR4 through competitive ATP-binding inhibition, blocking downstream RAS–MAPK and PI3K–AKT proliferative signalling cascades. It received FDA approval in April 2019 under the brand name Balversa for patients with locally advanced or metastatic urothelial carcinoma harboring susceptible FGFR2/3 alterations.

The mechanistic rationale for pulmonary arterial hypertension (PAH) draws on the known role of FGFR1 and FGFR2 in pulmonary vascular biology. FGFR1/2 are expressed on pulmonary arterial endothelial cells and smooth muscle cells, and FGF2 signalling has been shown to drive aberrant proliferation of pulmonary arterial smooth muscle cells (PASMCs) — a central feature of PAH vascular remodelling. By inhibiting FGFR-mediated signalling, erdafitinib could theoretically attenuate this pathological process.

It is important to note that this mechanistic link is pre-clinical in nature. No clinical trials or publications investigating erdafitinib in PAH have been identified. The prediction relies entirely on knowledge graph inference by the TxGNN model, and should be treated as a hypothesis-generating signal rather than actionable clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Erdafitinib in Pulmonary Hypertension.

---

## Literature Evidence

Currently no related literature available for Erdafitinib in Pulmonary Hypertension.

---

## Singapore Market Information

Erdafitinib is not currently registered with the Health Sciences Authority (HSA) in Singapore. No product authorisation records are available at this time.

---

## Cytotoxicity

Erdafitinib is an antineoplastic targeted therapy indicated for cancer treatment, and is subject to cytotoxic drug handling considerations.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (Pan-FGFR kinase inhibitor) |
| Myelosuppression Risk | Low to Moderate (anaemia reported; does not carry the typical broad myelosuppressive profile of conventional cytotoxics) |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | Serum phosphate (hyperphosphataemia is a common on-target effect), renal function, ophthalmic exam (central serous retinopathy / retinal pigment epithelial detachment risk), liver function, CBC |
| Handling Protection | Follow institutional cytotoxic drug handling and disposal procedures per applicable guidelines |

---

## Safety Considerations

> ⚠️ **Mechanistic Safety Signal — Amenorrhea**: The TxGNN model predicts an association between erdafitinib and amenorrhea (rank 3, score 99.26%). This is flagged as a **direction-incorrect** prediction: FGFR1 loss-of-function mutations naturally cause Kallmann syndrome (anosmia + hypogonadotropic amenorrhoea). As an FGFR1 inhibitor, erdafitinib may **induce or exacerbate** menstrual irregularities rather than treat them. This signal should be tracked as a potential adverse effect in female patients, not as a therapeutic indication.

For complete warnings, contraindications, and drug interaction data, please refer to the full Balversa (erdafitinib) prescribing information / package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.38%) to pulmonary hypertension, and a biologically plausible FGFR–FGF2 vascular remodelling mechanism exists, the current evidence base is L5 — model prediction only, with zero clinical trials, zero supporting publications, no Singapore regulatory footprint, and absent formal MOA documentation in the evidence pack. The drug's oncology-grade toxicity profile (hyperphosphataemia, retinal toxicity) also requires careful evaluation before considering application in a non-oncology PAH population.

An additional pattern is noted across the top-10 predictions: three separate ALS-related ontology nodes appear (ranks 5, 7, 8), suggesting possible knowledge graph node redundancy that may inflate scores for neurological indications.

**To proceed, the following is needed:**

- Formal DrugBank MOA documentation confirming FGFR1/2 inhibition profile specific to pulmonary vasculature
- Pre-clinical PAH model data (e.g., MCT or SU5416/hypoxia rat models) demonstrating FGFR inhibition efficacy
- Cross-reference review of nintedanib (a multi-kinase inhibitor including FGFR) PAH/ILD data as a mechanistic analogue to assess feasibility of the class effect
- Safety assessment of hyperphosphataemia and retinal toxicity acceptability for a chronic PAH patient population (vs. short-course oncology use)
- Singapore HSA regulatory pathway assessment (new drug application vs. expanded indication, noting zero current registrations)
- Ophthalmic and endocrine safety monitoring plan if exploratory PAH studies are initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

