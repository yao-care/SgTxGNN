---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
---

# Felodipine
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

# Felodipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Felodipine is a second-generation dihydropyridine calcium channel blocker (CCB), widely used internationally for the treatment of hypertension, though it carries no current registration in Singapore.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia (Group 3 PH)**,
with **no clinical trials** and **20 publications** retrieved — none of which directly evaluate Felodipine in this indication; the literature reflects general hypoxia biology, and established cardiology guidelines actually caution against CCB use in Group 3 PH.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; no local regulatory record available |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Felodipine is a vascular-selective dihydropyridine CCB that blocks L-type calcium channels in arterial smooth muscle cells, producing vasodilation and reducing systemic vascular resistance. Detailed MOA data from DrugBank is currently unavailable, but this pharmacological profile is well-established in the published literature. The drug is recognised internationally as a first-line or add-on agent for hypertension, with evidence supporting use in angina and stroke prevention.

On the surface, a mechanistic case can be made: as an arterial vasodilator, Felodipine could theoretically reduce pulmonary vascular resistance (PVR) in pulmonary hypertension. CCBs are indeed effective in Group 1 pulmonary arterial hypertension (PAH) — but only in the roughly 10–15% of patients who demonstrate a positive acute vasoreactivity response on right heart catheterisation.

The critical problem is that the target indication here — Group 3 PH, driven by lung disease and/or hypoxia (e.g., COPD, interstitial lung disease) — operates through a fundamentally different mechanism: hypoxic pulmonary vasoconstriction (HPV). HPV is a protective physiological reflex that shunts blood away from poorly ventilated lung regions to preserve systemic oxygenation. Felodipine, by inhibiting HPV, would worsen ventilation-perfusion (V/Q) mismatch and risk deepening systemic hypoxaemia. Current ESC/ERS pulmonary hypertension guidelines explicitly state that CCBs are not indicated — and may be harmful — in Group 3 PH. The TxGNN prediction most likely arises from graph-proximity associations between "CCB" and "pulmonary hypertension" nodes in the knowledge graph, without discriminating between PH subgroups.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

The 20 retrieved publications address general hypoxia biology (neurodegeneration, tumour microenvironment, immunology, altitude physiology) and do not evaluate Felodipine in pulmonary hypertension. The most informative items are listed below for context.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39841808](https://pubmed.ncbi.nlm.nih.gov/39841808/) | 2025 | Review | Science Translational Medicine | Chronic continuous hypoxia may benefit mitochondrial disease, autoimmunity, and aging in preclinical models, but translating to patients poses major safety challenges |
| [28972206](https://pubmed.ncbi.nlm.nih.gov/28972206/) | 2017 | Review | Nature Reviews Immunology | Hypoxia in physiological and pathological niches modulates innate and adaptive immunity in context-dependent ways |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Brain is acutely vulnerable to hypoxia; hypoxia is pivotal in Alzheimer's, Parkinson's, and neurodegeneration, yet altitude-related hypoxia may paradoxically benefit aging |
| [15192444](https://pubmed.ncbi.nlm.nih.gov/15192444/) | 2004 | Review | Current Opinion in Clinical Nutrition | Chronic hypoxia in COPD and high-altitude exposure share metabolic features (body mass loss, exercise intolerance), suggesting common pathophysiology |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Reviews fundamental mechanisms of hypoxaemia including V/Q mismatch — foundational to understanding Group 3 PH pathophysiology |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Hypoxia influences growth, metabolism, pH homeostasis, and angiogenesis; contributes to vascular disease and cancer |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Tumour hypoxia drives resistance to radiotherapy and immunotherapy; not relevant to Felodipine or PH |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Both acute and chronic hypoxia induce cognitive deficits via distinct neurological mechanisms |
| [40963621](https://pubmed.ncbi.nlm.nih.gov/40963621/) | 2025 | Review | Frontiers in Immunology | HIF-1α links hypoxia in the tumour microenvironment to autoimmune disease progression |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends in Cancer | Deubiquitinases regulate HIF abundance and represent potential drug targets in hypoxic tumours |

> **Note:** None of the 20 retrieved publications directly evaluate Felodipine in pulmonary hypertension owing to lung disease or hypoxia. This literature corpus provides background on hypoxia pathobiology only and does not constitute clinical evidence for this repurposing indication.

---

## Singapore Market Information

Felodipine is not currently registered in Singapore. No marketing authorisations are on record with the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinical safety alert specific to this indication:** Beyond standard adverse drug reactions, use of Felodipine in Group 3 PH carries an on-target pharmacodynamic safety concern. By inhibiting hypoxic pulmonary vasoconstriction (HPV) — a critical compensatory reflex in lung disease patients — Felodipine may worsen V/Q mismatch and deepen systemic hypoxaemia. This is not a labelled warning but a mechanistic contraindication identified in the ESC/ERS 2022 Pulmonary Hypertension Guidelines.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numerical score to this prediction (99.91%), but the mechanistic analysis reveals a fundamental mismatch: Felodipine's CCB action inhibits the very physiological reflex (hypoxic pulmonary vasoconstriction) that Group 3 PH patients depend on, and current ESC/ERS guidelines advise against CCB use in this subgroup. There are no clinical trials and no direct pharmacological publications supporting this indication.

**To proceed, the following would be needed:**

- Identification of a specific patient subpopulation within Group 3 PH where vasodilatory benefit outweighs HPV inhibition risk (e.g., concurrent systemic hypertension with mild PH)
- Preclinical data (animal model) demonstrating net haemodynamic and oxygenation benefit
- Clarification of Felodipine's full MOA profile (DrugBank data gap — remediation: query DrugBank API)
- Singapore/HSA regulatory filing review and package insert analysis to establish baseline safety profile (TFDA/HSA data gap — remediation: download and parse local product monograph)
- Formal consultation with a pulmonary hypertension specialist before any clinical investigation is designed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

