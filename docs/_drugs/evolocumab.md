---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
---

# Evolocumab
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

# Evolocumab: From Hypercholesterolemia to Symptomatic Hemophilia in Female Carriers

## One-Sentence Summary

Evolocumab (Repatha) is a fully human monoclonal antibody targeting PCSK9, approved in major markets for the treatment of hypercholesterolemia and reduction of cardiovascular events in high-risk patients.
The TxGNN model predicts it may have activity in **symptomatic hemophilia in female carriers** as its top-ranked novel indication — however, the mechanistic rationale for this connection is extremely thin.
Across all 10 predicted indications, **zero clinical trials and zero publications** were identified to support any repurposing direction; all predictions rest on model inference alone (Evidence Level L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / Cardiovascular risk reduction (PCSK9 inhibitor) |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, Evolocumab is a fully human monoclonal antibody (IgG2) that binds to PCSK9 (Proprotein Convertase Subtilisin/Kexin Type 9) and prevents it from binding to LDL receptors on hepatocytes. This increases LDL receptor recycling to the cell surface, substantially reducing circulating LDL-cholesterol. Its proven benefit lies in lipid metabolism and atherosclerotic cardiovascular disease prevention (most notably demonstrated in the FOURIER trial).

The top-ranked predicted indication — symptomatic hemophilia in female carriers — operates in an entirely different physiological domain. X-linked hemophilia carriers have heterozygous Factor VIII or IX mutations, resulting in variable clotting factor levels. The knowledge graph connection most likely arises because PCSK9 is expressed at low levels on platelet surfaces and may marginally influence platelet membrane cholesterol composition, which in turn affects activation thresholds. However, this is a highly indirect and multi-hop pathway — there is no established mechanism by which PCSK9 inhibition can compensate for or modulate Factor VIII/IX deficiency.

Of all 10 predictions in this batch, the second-ranked indication — **familial apolipoprotein C-II deficiency** — carries the most scientifically plausible rationale. ApoC-II is a necessary activator of lipoprotein lipase (LPL); its deficiency causes severe hypertriglyceridemia. While Evolocumab primarily targets LDL-C, PCSK9 inhibitors have demonstrated modest TG-lowering effects (−5% to −15%) in multiple RCTs, suggesting shared upstream lipid metabolism regulation. This represents the only hypothesis in this batch with a conceivable biological basis and could serve as a starting point for exploratory research in rare lipid disorders.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## All Predicted Indications at a Glance

The following table summarises all 10 TxGNN-predicted indications and their mechanistic plausibility assessments:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Plausibility | Recommendation |
|------|----------------------|-------------|--------------------------|----------------|
| 1 | Symptomatic hemophilia in female carriers | 99.82% | Very low — indirect platelet cholesterol pathway | Hold |
| 2 | Familial apolipoprotein C-II deficiency | 99.50% | Moderate — shared lipid metabolism upstream | Research Question |
| 3 | Thrombocytopenic purpura | 99.42% | Very low — no mechanism linking PCSK9 to autoimmune platelet destruction | Hold |
| 4 | Factor XI deficiency | 99.29% | Very low — serine protease taxonomy artefact only | Hold |
| 5 | Hemophilia A with vascular abnormality | 99.22% | Low — vascular protection effect exists but irrelevant to FVIII deficiency | Hold |
| 6 | Disease of catalytic activity | 99.08% | None — ontology parent node artefact; not a clinical diagnosis | Hold |
| 7 | Hemorrhagic disease of newborn | 98.89% | Very low — indirect vitamin K lipoprotein transport hypothesis | Hold |
| 8 | X-linked ichthyosis (without STS deficiency) | 98.84% | Very low — systemic PCSK9 inhibition does not affect cutaneous cholesterol sulfate pathway | Hold |
| 9 | Inherited thrombophilia | 98.82% | Very low — animal model hypothesis only; no human data | Hold |
| 10 | Disorder of vitamins/cofactors metabolism and transport | 98.80% | None — ontology parent node artefact; not a clinical diagnosis | Hold |

---

## Singapore Market Information

Evolocumab has no registered products in Singapore as of the data cut-off (2026-06-21). It is approved and marketed in the US (Repatha, Amgen), EU, Japan, and Taiwan under various regulatory pathways, but HSA registration has not been obtained.

---

## Safety Considerations

Please refer to the package insert for safety information. No Singapore-specific prescribing information or warnings data was available in the Evidence Pack for this analysis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are rated L5 — model inference only — with zero supporting clinical trials or literature. The top-ranked indication (hemophilia in female carriers) lacks any credible mechanistic link to PCSK9 inhibition. The sole exception worth monitoring is the rank-2 prediction (familial ApoC-II deficiency), which at least shares a lipid metabolism context with Evolocumab's established pharmacology.

**To proceed with any further evaluation, the following is needed:**

- **For familial ApoC-II deficiency (rank 2 only):** Conduct a targeted literature search in rare lipid disorder databases (OMIM, Orphanet, lipid clinic case series); assess whether any PCSK9 inhibitor has been used off-label in severe hypertriglyceridemia due to LPL pathway defects
- **MOA documentation:** Obtain full DrugBank entry for Evolocumab to formally confirm mechanism and drug class for the Evidence Pack
- **Pipeline-level filtering:** Indications classified as ontology parent nodes ("disease of catalytic activity", "disorder of other vitamins and cofactors metabolism and transport") should be suppressed at the KG post-processing stage to prevent non-actionable entries from consuming evidence collection resources
- **Singapore registration feasibility:** Assess HSA regulatory pathway if any downstream indication ever reaches L3+ evidence — current zero-registration status means a full de novo application would be required

> ⚠️ This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

