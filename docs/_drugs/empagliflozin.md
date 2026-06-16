---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Empagliflozin
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

# Empagliflozin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Empagliflozin is a selective SGLT2 inhibitor approved for type 2 diabetes mellitus, heart failure, and chronic kidney disease, but currently has no HSA (Singapore) regulatory registration on file.
The TxGNN model's top prediction is **Focal Stiff Limb Syndrome** (score 99.06%), alongside 9 additional rare disease candidates spanning neurological, skeletal, and metabolic conditions.
However, **no clinical trials and no relevant literature** support this direction, and the mechanistic link between SGLT2 inhibition and stiff-person spectrum disorders remains unestablished — the high score most likely reflects knowledge graph topology noise rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (SGLT2 inhibitor class; no HSA indication text on file) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Singapore Market Status | Not registered (0 licenses on record — possible data gap, see note below) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Empagliflozin is a highly selective sodium-glucose cotransporter 2 (SGLT2) inhibitor. By blocking SGLT2 in the proximal renal tubule, it forces urinary glucose excretion independent of insulin secretion or sensitivity. Beyond glycaemic control, it has demonstrated cardiovascular protection (reduced hospitalisation for heart failure and CV death in EMPA-REG OUTCOME) and renal protection (slowed eGFR decline in EMPA-KIDNEY), likely through haemodynamic offloading, NF-κB inhibition, oxidative stress reduction, and mitochondrial stabilisation. This breadth of pleiotropic effects is why the TxGNN model generates a wide range of repurposing candidates.

Focal Stiff Limb Syndrome is a focal variant of Stiff Person Syndrome (SPS), an autoimmune neurological disorder in which anti-GAD65 antibodies attack GABAergic interneurons, producing focal muscle rigidity and episodic spasms. The pathophysiology is fundamentally GABAergic autoimmunity — mechanistically distinct from metabolic, renal, or haemodynamic disease where SGLT2 inhibitors have documented effects. SGLT2 inhibitors have no known direct or indirect GABAergic mechanism.

The high TxGNN score (0.9906) most likely reflects **graph topology noise**: SPS has a well-documented epidemiological co-occurrence with type 1 diabetes (anti-GAD65 antibodies are shared markers), making the SPS node closely adjacent to the diabetes node cluster in the knowledge graph. This neighbourhood proximity inflates the predicted score without reflecting a genuine pharmacological connection. This interpretation is further supported by the fact that rank 1 (focal stiff limb syndrome) and rank 2 (classic stiff person syndrome) share an identical TxGNN score of 0.9906, strongly suggesting the model treats them as the same node cluster rather than independently derived predictions.

---

## All Predicted Indications — Overview

This is a multi-indication candidate evaluation. Ten rare disease predictions were generated and assessed:

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Key Note |
|------|---------|-------------|----------------|----------|----------|
| 1 | Focal Stiff Limb Syndrome | 99.06% | L5 | Hold | Likely graph noise; GAD65/diabetes comorbidity node adjacency |
| 2 | Classic Stiff Person Syndrome | 99.06% | L5 | Hold | Identical score to rank 1; treated as same node cluster by model |
| 3 | Opsismodysplasia | 99.03% | L5 | Hold | INPPL1/SHIP2 → PI3K connection theoretical; ultra-rare, gene therapy is the relevant direction |
| 4 | Thiamine-Responsive Dysfunction Syndrome | 98.99% | L5 | Hold ⚠️ | **Active safety risk**: SGLT2 inhibitors can deplete thiamine — likely a contraindication in this population |
| 5 | Drug-Induced Localized Lipodystrophy | 98.46% | L5 | Hold | Injection-site mechanical injury; no systemic metabolic mechanism applies |
| 6 | Centrifugal Lipodystrophy | 98.39% | L5 | Hold | Paediatric onset; empagliflozin not approved in patients under 18 |
| 7 | Pressure-Induced Localized Lipoatrophy | 98.34% | L5 | Hold | Pure physical injury mechanism; no pharmacological rationale |
| 8 | Idiopathic Localized Lipodystrophy | 98.25% | L5 | Hold | Ranks 5–8 are ICD subtypes of the same pathological category: ontology leakage |
| 9 | Pancreatic Agenesis | 98.07% | L4 | Research Question | **Best mechanistic fit**: insulin-independent glucose lowering may support neonatal diabetes from agenesis |
| 10 | Autoimmune Oophoritis | 92.37% | L5 | Hold | Organ-specific autoimmunity; non-specific anti-inflammatory link is insufficient |

---

## Clinical Trial Evidence

Currently no clinical trials are registered for any of the 10 predicted indications.

---

## Literature Evidence

Only **Pancreatic Agenesis (rank 9)** returned literature results. Both publications are indirect pharmacological references and are not specific to pancreatic agenesis:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26583910](https://pubmed.ncbi.nlm.nih.gov/26583910/) | 2015 | RCT / Combination Therapy | Expert Opinion on Pharmacotherapy | Empagliflozin + linagliptin in T2DM: documents empagliflozin's insulin-independent mechanism (renal glucose excretion) alongside DPP-4 inhibition targeting beta/alpha cell dysfunction — establishes the pharmacological basis for non-insulin-mediated glucose control |
| [35234250](https://pubmed.ncbi.nlm.nih.gov/35234250/) | 2022 | Cohort / Diabetic Complications | Bioscience Reports | SGLT2 inhibition in diabetic retinopathy: contextualises empagliflozin use in settings of insufficient pancreatic insulin production, indirectly relevant to the insulin-deficiency phenotype of pancreatic agenesis |

> **Important caveat**: Neither publication studies pancreatic agenesis. These citations provide indirect pharmacological support for the insulin-independent mechanism hypothesis only and do not constitute clinical evidence for the repurposing indication.

---

## Singapore Market Information

No HSA (Health Sciences Authority, Singapore) registrations were found for Empagliflozin in the current dataset.

> **Data Gap Notice**: This is likely a data retrieval gap rather than a true absence from the Singapore market. Empagliflozin (Jardiance®, Boehringer Ingelheim / Eli Lilly) holds regulatory approvals in the United States (FDA 2014), European Union (EMA 2014), Japan (PMDA 2015), and Taiwan (TFDA). Clinicians and researchers should verify current HSA registration status directly via the [HSA Drug Product Search](https://eservice.hsa.gov.sg/prism/common/enquirepublic/SearchDRProduct.do) before drawing conclusions.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, drug interactions) was not retrieved in this Evidence Pack.

Please refer to the package insert for safety information.

> **⚠️ Critical Safety Flag — Rank 4 Prediction (Thiamine-Responsive Dysfunction Syndrome)**
>
> Published pharmacovigilance data and case reports indicate that SGLT2 inhibitors, including empagliflozin, can cause thiamine (Vitamin B1) depletion, with documented cases of Wernicke's encephalopathy in high-risk patients. In Thiamine-Responsive Megaloblastic Anaemia (TRMA, Rogers Syndrome — caused by SLC19A2 transporter mutations), thiamine uptake is already critically impaired at the cellular level. Administering empagliflozin to this population would risk **compounding an existing thiamine deficit**, potentially precipitating life-threatening neurological deterioration.
>
> This prediction is flagged as a likely **model false-positive with an associated active harm signal**. It should be excluded from further repurposing evaluation and noted in the TxGNN graph correction list for this indication node.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Nine of ten predicted indications are L5 (model prediction only), with no clinical trials, no targeted literature, and weak or absent mechanistic rationale. The two highest-ranked indications (stiff person syndrome variants) reflect graph topology noise, not pharmacological signal. One prediction (thiamine-responsive dysfunction syndrome, rank 4) carries an active patient safety risk and should be treated as a contraindication signal rather than a repurposing opportunity.

**The single actionable lead:**

Pancreatic Agenesis (Rank 9) is the only prediction with a theoretically sound mechanistic rationale: empagliflozin's glucose-lowering action is entirely insulin-independent (operating via renal SGLT2 blockade), which is pharmacologically compatible with the absolute insulin insufficiency caused by congenital pancreatic agenesis (PDX1/PTF1A mutations). This is a genuine mechanistic insight, even though current literature support is indirect.

**To advance the Pancreatic Agenesis research question, the following is needed:**

- Systematic case report review: SGLT2 inhibitors in neonatal diabetes and congenital insulin-deficient conditions
- Paediatric safety and dosing profile review (pancreatic agenesis typically presents at birth or in infancy; empagliflozin lacks paediatric approval for most age groups)
- Endocrinology expert consultation on whether SGLT2 inhibitor adjunct therapy is feasible alongside exogenous insulin replacement in this population
- Rare disease registry linkage (e.g., EURO-NDM, PDX1 registry) to identify any prior off-label use

**For all other indications:**

No further investigation is recommended at this stage. Reassess if TxGNN model updates with improved ontology-aware graph topology correction produce meaningfully different rankings for these indications. The four localized lipodystrophy subtypes (ranks 5–8) and the two SPS variants (ranks 1–2) should be grouped as single ontology clusters rather than evaluated as independent repurposing opportunities.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

