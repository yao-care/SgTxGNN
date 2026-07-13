---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Chemotherapy-Induced Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant human granulocyte colony-stimulating factor (G-CSF), widely used globally for the prevention and treatment of chemotherapy-induced neutropenia and as a hematopoietic stem cell (HSC) mobilizing agent — however, it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **14 clinical trials** and **1 publication** currently identified; however, all existing evidence relates to HSCT support roles rather than direct intervention for platelet release disorders.
The mechanistic rationale relies on an indirect pathway (G-CSF → HSC mobilization → allogeneic HSCT → hematopoietic reconstitution → correction of congenital platelet release defects), and no study has directly investigated this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally indicated for chemotherapy-induced neutropenia and HSC mobilization |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Filgrastim is a recombinant form of human G-CSF that binds the CSF3 receptor (G-CSFR/CSF3R), activating JAK2/STAT3 and MAPK/ERK signaling to stimulate proliferation, differentiation, and survival of neutrophil precursors. It also mobilizes HSCs from bone marrow into peripheral blood, making it the backbone of stem cell collection protocols before transplantation.

Primary release disorder of platelets (also known as primary secretion disorders) involves dysfunction in the dense granule (δ-granule) or alpha granule (α-granule) release pathways — platelets fail to properly secrete their contents upon activation, impairing secondary aggregation and clot consolidation. The TxGNN model's predicted mechanistic link operates through two theoretical pathways: (1) G-CSF receptors are expressed at low levels on megakaryocyte (MK) progenitors, suggesting a theoretically possible minor direct effect on platelet progenitor biology; and (2) more importantly, G-CSF mobilizes HSCs for allogeneic HSCT, which reconstitutes the entire hematopoietic system — potentially replacing donor-derived megakaryocytes and correcting congenital platelet release defects from their root cause.

However, this mechanistic rationale is indirect and speculative. The G-CSF receptor signaling pathway (CSF3R → JAK2 → STAT3/ERK) has no established regulatory role over granule biogenesis or release mechanisms within mature platelets. All 14 identified clinical trials feature Filgrastim strictly in its conventional role as an HSCT support agent, and none are designed to study platelet release disorders. The near-perfect TxGNN score likely reflects the broad connectivity of the "platelet" and "hematopoietic stem cell" nodes in the knowledge graph rather than direct molecular pathway support.

---

## Clinical Trial Evidence

> **Important caveat:** All identified trials feature Filgrastim as an HSCT mobilization or chemotherapy-support agent. None are directly designed to treat primary release disorder of platelets. The trial list below represents the evidence landscape retrieved by the search pipeline, not direct indication-specific evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Multi-center RCT comparing best available therapy vs. autologous HSCT for treatment-resistant relapsing multiple sclerosis; Filgrastim used as part of the mobilization regimen — the highest-quality trial retrieved, though with only indirect relevance |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT for hematologic malignancies using busulfan, fludarabine and TBI; Filgrastim serves as the HSC mobilizing agent — a completed trial providing safety and mobilization data |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood stem cell transplantation for high-risk pediatric sarcomas; Filgrastim used as standard supportive therapy during HSC collection |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT for patients with life-threatening GATA2 mutations (a hematologic disorder affecting hematopoiesis); Filgrastim as mobilizing agent — small sample but completed |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs. unselected autologous SCT in advanced mantle cell lymphoma and DLBCL; provides data on Filgrastim-mobilized graft composition |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir for CMV reactivation prevention in severe sepsis/trauma-associated respiratory failure (GRAIL study); Filgrastim used in post-transplant context, no platelet disorder relevance |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion followed by autologous HSCT in severe SLE; Filgrastim as HSC mobilization support — very small sample |
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSCT for hematological malignancies; trial terminated, limiting data value |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile (NLRP3 inhibitor) for moderate COVID-19 and early cytokine release syndrome; terminated early, no relevant contribution |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved HLA-mismatched unrelated donor bone marrow with PTCy for allogeneic transplantation; withdrawn before enrollment, no data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Clinical Observational | Frontiers in Immunology | G-CSF mobilization of peripheral blood stem cells in healthy allogeneic donors causes preferential mobilization of specific lymphocyte subsets; relevant as background evidence for understanding G-CSF's broader immunological effects on graft cellular composition, though not directly addressing platelet release function |

---

## Singapore Market Information

Filgrastim is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. There are no authorized products on record in the Singapore regulatory database.

Should a repurposing clinical program be considered, a new regulatory filing with HSA would be required from the outset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-perfect TxGNN prediction score (99.998%), the underlying evidence for Filgrastim in primary release disorder of platelets is entirely indirect. All 14 retrieved clinical trials use Filgrastim as an HSCT mobilization support agent — none target platelet release dysfunction as the primary endpoint. The sole literature piece addresses lymphocyte subset mobilization dynamics, not platelet biology. The proposed mechanistic pathway (G-CSF → allogeneic HSCT → donor hematopoietic reconstitution → correction of congenital platelet secretion defects) is biologically coherent in principle but has not been tested clinically, and the direct molecular link between CSF3R signaling and platelet granule release pathways remains unestablished.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve Filgrastim's full DrugBank pharmacology profile to confirm whether G-CSF receptor expression on megakaryocyte progenitors is sufficient to justify a direct (non-HSCT) therapeutic hypothesis
- **Focused literature search**: Search specifically for G-CSF effects on megakaryopoiesis, platelet granulogenesis, and secretion function (dense granule release, α-granule release) in preclinical and clinical settings
- **Disease subtype clarification**: Specify the molecular subtype of "primary release disorder of platelets" (e.g., Hermansky-Pudlak syndrome, Chediak-Higashi, isolated dense granule deficiency) — mechanistic feasibility varies substantially by subtype
- **Case report or registry review**: Search hematology registries and published case series for any instances of Filgrastim use in patients with congenital platelet secretion disorders (e.g., in the context of HSCT donor mobilization where the recipient had platelet release disorder)
- **Singapore regulatory pathway scoping**: If a hypothesis is confirmed at preclinical level, engage HSA for early scientific advice on first-in-indication clinical trial design
- **Safety data retrieval**: Download and parse the Filgrastim package insert to complete the S1 safety screening that is currently blocked by missing warning and contraindication data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

