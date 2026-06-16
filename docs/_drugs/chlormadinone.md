---
layout: default
title: Chlormadinone
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Chlormadinone
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

# Chlormadinone: From Hormonal Contraception to Antithrombin Deficiency Type 2

## One-Sentence Summary

Chlormadinone (chlormadinone acetate, CMA) is a synthetic anti-androgenic progestogen historically used in hormonal contraception and androgen-dependent conditions.
The TxGNN model predicts it may be effective for **Antithrombin Deficiency Type 2** with a prediction score of 98.71%, yet **no clinical trials** and **no supporting literature** exist for this indication.
Across all 10 predicted indications, the highest-evidence prediction is **Thrombophilia** (rank 10, L4), where 7 publications document CMA use in high-risk patients — as a safety-monitored contraceptive option, not a treatment for the coagulopathy itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in regulatory data (contextually: progestogen-based hormonal contraception and androgen-dependent conditions) |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 98.71% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on contextual evidence across the 10 predicted indications, Chlormadinone acetate (CMA) is an anti-androgenic synthetic progestogen that influences the progestogen receptor, reduces androgenic activity, and modulates the coagulation cascade — most notably by affecting activated protein C (APC) resistance and fibrinolytic activity.

The TxGNN model established a network connection between Chlormadinone and antithrombin deficiency type 2 via coagulation regulatory nodes — specifically the antithrombin system ↔ progestogen-coagulation pathway. Progestogens are pharmacologically known to influence coagulation factors VII and VIII, and to alter APC resistance, which explains why the knowledge graph identifies a topological link between CMA and heritable coagulopathies.

**Critical mechanistic caveat — direction of effect matters:** The predicted connection is biologically plausible but pharmacologically backwards for therapeutic repurposing. Progestogens, including CMA, are generally *pro-coagulant* agents — they reduce APC sensitivity and may increase thrombotic risk, particularly in patients who already have antithrombin deficiency. The TxGNN model appears to be capturing a pharmacological interaction (potential adverse effect) rather than a therapeutic opportunity. This is a consistent pattern across the top-ranked predictions: the progestogen–coagulation network connection reflects drug *involvement* in coagulation biology, not the ability to correct coagulation defects.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Chlormadinone in Antithrombin Deficiency Type 2.

---

## Literature Evidence

Currently no related literature available for Chlormadinone in Antithrombin Deficiency Type 2.

---

## Prediction Landscape — All 10 Candidates

The following summarises all TxGNN predictions in this multi-candidate pack. Rank 1 is the highest-scored prediction; rank 10 (Thrombophilia) carries the most real-world evidence.

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Publications | Decision | Key Concern |
|------|---------|-------------|----------------|--------|--------------|----------|-------------|
| 1 | Antithrombin Deficiency Type 2 | 98.71% | L5 | 0 | 0 | Hold | Pro-coagulant direction; no evidence |
| 2 | Heparin Cofactor 2 Deficiency | 98.67% | L5 | 0 | 0 | Hold | Topology-only; no biological specificity |
| 3 | Factor 5 Excess / Spontaneous Thrombosis | 98.64% | L5 | 0 | 0 | Hold | CMA may worsen APC resistance |
| 4 | Candidiasis | 98.62% | L5 | 0 | 3 | Hold | Literature shows CMA *increases* risk |
| 5 | Plasma Cell Myeloma | 97.89% | L5 | 0 | 0 | Hold | No clinical or preclinical data |
| 6 | Heart Neoplasm | 97.77% | L5 | 0 | 1 | Hold | Hormone-risk framework only |
| 7 | Rheumatoid Arthritis | 97.72% | L5 | 0 | 1 | Hold | Bidirectional; insufficient data |
| 8 | Indolent Plasma Cell Myeloma | 97.68% | L5 | 0 | 0 | Hold | Same path as rank 5; ontology similarity only |
| 9 | Gout | 97.68% | L5 | 0 | 0 | Hold | Estrogen drives urate excretion; progestogen effect minimal |
| 10 | Thrombophilia | 97.66% | **L4** | 0 | **7** | Hold* | Context: safe contraceptive use, not treatment |

> \* Thrombophilia at rank 10 reaches L4 and S1 in the scoring pipeline. If the research question is reframed from "treating thrombophilia" to "safe hormonal contraception in high-VTE-risk women," the evidence supports L3/S2. See detail below.

---

## Rank 10 Deep Dive: Thrombophilia (Highest-Evidence Prediction)

Although ranked 10th by TxGNN score, Thrombophilia is the most clinically informative prediction in this pack because it is the only one supported by substantive literature.

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15541404](https://pubmed.ncbi.nlm.nih.gov/15541404/) | 2004 | Retrospective Cohort | *Contraception* | 204 women at high VTE risk; CMA at antigonadotropic doses (n=102) evaluated for venous impact — landmark CMA safety data in thrombophilic women |
| [25961217](https://pubmed.ncbi.nlm.nih.gov/25961217/) | 2010 | Clinical Cohort | *Hormone Mol Biol Clin Invest* | Antigonadotropic progestogens (incl. CMA) as contraceptives when combined pill is contraindicated; supports CMA as lower-thrombotic-risk option |
| [15333036](https://pubmed.ncbi.nlm.nih.gov/15333036/) | 2004 | Cross-sectional Cohort | *J Thromb Haemost* | CMA-only OC shows less APC resistance than 2nd/3rd-generation combined OCs; key mechanistic differentiation data |
| [2409608](https://pubmed.ncbi.nlm.nih.gov/2409608/) | 1985 | Clinical Study | *Sovetskaia Meditsina* | Platelet aggregation effects of sex steroids in climacteric dysfunctional uterine haemorrhage |
| [1199513](https://pubmed.ncbi.nlm.nih.gov/1199513/) | 1975 | Clinical Study | *Zentralbl Gynakol* | Fibrinolytic split products during Ovosiston (Mestranol + CMA 2 mg) use; fibrinolytic activity increases vs. normal cycle |
| [6083922](https://pubmed.ncbi.nlm.nih.gov/6083922/) | 1984 | Clinical Cohort | *Folia Haematol* | Case of thrombophilia with OC use as a contributing thrombogenic factor; clotting variable changes discussed |
| [21437840](https://pubmed.ncbi.nlm.nih.gov/21437840/) | 2011 | Case Report | *Klin Monbl Augenheilkd* | Hemicentral retinal artery occlusion from low-dose OC; illustrates thromboembolic risk of OC even at low doses |

### Interpretive Note

The literature documents CMA as a **safer-than-combined-pill contraceptive option** for women already at high VTE risk (e.g., inherited thrombophilia, prior thrombosis). This is not evidence that CMA *treats* thrombophilia. The evidence framework is:

- CMA causes **less APC resistance** than levonorgestrel-based or third-generation combined OCs
- CMA is therefore considered a **lower-VTE-risk** progestogen-only option in women who cannot use estrogen-containing contraceptives
- This is a risk-management / harm-reduction positioning, not a therapeutic repurposing

---

## Singapore Market Information

Chlormadinone is not currently registered in Singapore. No marketing authorization records are on file.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registrations found |

---

## Safety Considerations

All Safety data (key warnings, contraindications, drug interactions) is currently unavailable in the Evidence Pack. Please refer to the package insert and prescribing information for full safety details.

Contextual risk signals identified from the literature include:

- **Thromboembolic risk**: CMA and combined OCs containing CMA have been associated with increased VTE risk; fibrinolytic and APC-resistance changes are documented
- **Pro-coagulant effect**: Particularly relevant given top predictions involve coagulation disorders — any exploration in these populations would require rigorous haemovigilance

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score of 98.71% for Antithrombin Deficiency Type 2, the mechanistic analysis reveals that the knowledge graph connection is directionally adverse — Chlormadinone as a progestogen may *increase* coagulation risk in antithrombin-deficient patients rather than treating the underlying condition. Zero clinical trials and zero direct literature exist for this indication. Across all 10 predicted indications, all recommendations are Hold, with the highest-evidence prediction (Thrombophilia, L4) documenting CMA as a safety-managed contraceptive option in high-risk patients — not as a therapeutic agent.

**To proceed, the following is needed:**

- **MOA data retrieval**: Query DrugBank API for complete mechanism of action, receptor binding profile, and pharmacodynamics
- **Safety profile completion**: Download and parse the prescribing information / SPC for key warnings and contraindications (classified as Blocking data gap)
- **Mechanistic directionality review**: Determine whether any of the 10 KG-predicted connections reflects a genuine therapeutic effect vs. adverse pharmacology before advancing any candidate
- **Reframing analysis for Thrombophilia**: If the research question is redefined as "safe hormonal contraception in women with inherited thrombophilia," the Thrombophilia indication may be eligible for S2 (literature review stage), pending safety data availability
- **Regulatory feasibility check**: Confirm whether any jurisdiction has CMA registered for gynaecological or haematological indications to establish a bridging strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

