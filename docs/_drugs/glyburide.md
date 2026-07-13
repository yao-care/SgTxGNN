---
layout: default
title: Glyburide
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
---

# Glyburide
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

# Glyburide: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Glyburide is a second-generation sulfonylurea antidiabetic drug, originally used to manage Type 2 Diabetes Mellitus by blocking pancreatic ATP-sensitive potassium (KATP) channels to stimulate insulin secretion.
The TxGNN model's highest-ranked prediction identifies **Opsismodysplasia** as a potential new indication (score 97.24%), but this prediction carries **no clinical trial or literature support** and mechanistic analysis strongly suggests a false positive.
Across all 10 predicted indications in this multi-candidate Evidence Pack, only **Pancreatic Agenesis** (rank 9, 94.34%) has any associated literature (20 publications, L4 level), and even that requires careful subtype stratification before conclusions can be drawn.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.24% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, formal mechanism of action data is not available from the regulatory source. Based on published pharmacology, Glyburide (also known internationally as Glibenclamide) blocks the ATP-sensitive potassium channel complex—composed of the SUR1 regulatory subunit and the Kir6.2 pore—in pancreatic beta cells. Channel closure leads to membrane depolarization, voltage-gated calcium influx, and glucose-independent insulin secretion. Beyond glycaemic control, Glyburide also modulates the NLRP3 inflammasome through SUR1 channels in macrophages, giving it a secondary anti-inflammatory dimension.

Opsismodysplasia is a rare skeletal dysplasia caused by loss-of-function mutations in INPPL1, the gene encoding the SHIP2 lipid phosphatase. SHIP2 hydrolyses phosphatidylinositol-3,4,5-trisphosphate (PIP₃), and its absence dysregulates PI3K-AKT signalling in chondrocytes, producing severe metaphyseal abnormalities and dwarfism. This phosphoinositide pathway is entirely distinct from KATP channel pharmacology; there is no established molecular intersection between Glyburide's mechanism and the INPPL1/SHIP2 axis.

The high TxGNN score (97.24%) most likely reflects a structural artefact of the knowledge graph: distant "metabolic signalling → skeletal development" node embeddings create a high-cosine-similarity link without any direct therapeutic logic. This is a well-recognised pattern of high-scoring false positives in graph neural network-based repurposing models and should not be interpreted as biological evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Glyburide in Opsismodysplasia.

---

## Literature Evidence

Currently no related literature available for Glyburide in Opsismodysplasia.

---

## All Predicted Indications — Summary Overview

This Evidence Pack covers 10 predicted indications (candidate ID: TW-DB01016-multi). Nine of ten are L5 with no supporting evidence; only Pancreatic Agenesis (rank 9) reaches L4.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Opsismodysplasia | 97.24% | L5 | Hold |
| 2 | Focal Stiff Limb Syndrome | 96.90% | L5 | Hold |
| 3 | Classic Stiff Person Syndrome | 96.90% | L5 | Hold |
| 4 | Thiamine-Responsive Dysfunction Syndrome | 96.77% | L5 | Hold |
| 5 | Drug-Induced Localized Lipodystrophy | 95.22% | L5 | Hold |
| 6 | Centrifugal Lipodystrophy | 94.92% | L5 | Hold |
| 7 | Pressure-Induced Localized Lipoatrophy | 94.79% | L5 | Hold |
| 8 | Idiopathic Localized Lipodystrophy | 94.47% | L5 | Hold |
| **9** | **Pancreatic Agenesis** | **94.34%** | **L4** | **Research Question** |
| 10 | Autoimmune Oophoritis | 82.22% | L5 | Hold |

### Mechanistic Notes on L5 Predictions

| Disease | Why the KG Link Is Misleading |
|---------|-------------------------------|
| Focal / Classic Stiff Person Syndrome | ~30–40% of SPS patients have co-morbid T1D; KG path runs "Glyburide → Diabetes → GAD65 → SPS." This is a shared-antigen comorbidity, not a treatment rationale. |
| Thiamine-Responsive Dysfunction Syndrome | TRMA beta cells are partially preserved early; thiamine replacement, not sulfonylureas, is the definitive treatment and can reverse damage. |
| Drug-Induced / Idiopathic / Centrifugal / Pressure-Induced Lipodystrophy | All connect via "antidiabetic → adipose metabolism" KG nodes; none involve KATP pharmacology. |
| Autoimmune Oophoritis | Lowest score (82.22%); theoretical NLRP3 anti-inflammatory link is too weak to pursue. |

---

## Notable Finding: Pancreatic Agenesis (Rank 9, L4)

Pancreatic Agenesis is the only indication with retrievable literature (20 publications), but the evidence requires critical subtype stratification before any repurposing conclusion is drawn.

**Subtype A — KATP Channel Mutation-Related Neonatal Diabetes (ABCC8 / KCNJ11 mutations)**
Approximately 50% of permanent neonatal diabetes cases are caused by gain-of-function mutations in KCNJ11 or ABCC8 (the SUR1 subunit). These mutations render the KATP channel constitutively open, suppressing insulin secretion. Critically, mutant KATP channels retain sulfonylurea-binding capacity, and Glyburide/Glibenclamide can close them and restore insulin release. Switching from insulin to sulfonylurea therapy in this subgroup is an **established clinical practice** supported by multiple case series and observational studies—effectively L1-L2 level evidence for this subtype. However, the correct diagnostic label should be "KATP channel neonatal diabetes," not "pancreatic agenesis."

**Subtype B — True Pancreatic Agenesis (PTF1A / PDX1 enhancer mutations)**
In these patients, the pancreatic anlage fails to form; beta cells are entirely absent. The KATP channel drug target simply does not exist, and Glyburide is therapeutically inert.

The 20 retrieved publications are primarily STZ-induced rodent diabetic models, beta cell function assays, and general antidiabetic herbal comparison studies—none directly addresses Glyburide in pancreatic agenesis. The signal originates from thematic proximity in the knowledge graph, not from disease-specific studies.

### Key Literature for Pancreatic Agenesis

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37251668](https://pubmed.ncbi.nlm.nih.gov/37251668/) | 2023 | Case Report | Front Endocrinol | Successful switch from continuous subcutaneous insulin infusion to sulfonylurea in two KCNJ11-mutation neonatal diabetes patients; demonstrates sulfonylurea efficacy in KATP mutation subtype |
| [28943513](https://pubmed.ncbi.nlm.nih.gov/28943513/) | 2018 | Case Report | J Clin Res Pediatr Endocrinol | PTF1A enhancer mutations causing isolated pancreatic agenesis (Subtype B, no beta cells) alongside one KCNJ11 DEND syndrome case; highlights the critical distinction between subtypes |
| [41693148](https://pubmed.ncbi.nlm.nih.gov/41693148/) | 2026 | Functional Study (ex vivo) | J Clin Endocrinol Metab | Pancreatic islet functional evaluation in Beckwith-Wiedemann syndrome with congenital hyperinsulinism; elucidates hyperinsulinism pathophysiology |
| [26132582](https://pubmed.ncbi.nlm.nih.gov/26132582/) | 2015 | Animal Study | PLoS One | Glibenclamide used as a pharmacological tool to probe KATP channel function in hypothyroid rat islets; not a therapeutic study |
| [27656398](https://pubmed.ncbi.nlm.nih.gov/27656398/) | 2016 | Basic Science | Mol Metab | Mitochondrial pyruvate carrier role in glucose-stimulated insulin secretion; mechanistic beta cell physiology relevant to drug target understanding |

---

## Singapore Market Information

Glyburide currently holds **no product registrations** with the Health Sciences Authority (HSA) of Singapore. The drug is not marketed and no authorization numbers are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Two data gaps were flagged as blocking or high-severity: (1) HSA/TFDA package insert warnings and contraindications have not been retrieved — this blocks formal safety screening (S1 stage); (2) formal MOA data from DrugBank API was not retrieved, limiting mechanistic linkage analysis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction (Opsismodysplasia, 97.24%) is a knowledge graph false positive with no mechanistic basis, no clinical trials, and no supporting literature; nine of ten predictions are L5 "Hold." The one indication with any literature signal (Pancreatic Agenesis, L4) is a mixed population where Glyburide is only relevant to the KATP-mutation neonatal diabetes subtype, which should be pursued under a different disease classification.

**To proceed, the following is needed:**

- **Resolve data gaps first:**
  - Retrieve DrugBank MOA data to complete mechanistic linkage analysis
  - Download and parse the TFDA/HSA package insert PDF to obtain formal warnings and contraindications, which are currently blocking S1 safety screening

- **For the Pancreatic Agenesis / KATP Neonatal Diabetes research question:**
  - Reframe the search as "Sulfonylurea (Glyburide/Glibenclamide) in KCNJ11 or ABCC8 mutation neonatal diabetes" to retrieve higher-quality, disease-specific evidence
  - Patient genotyping is mandatory before any clinical use — Subtype A (KATP mutation) responds; Subtype B (true agenesis) does not
  - Conduct a dedicated systematic literature review on sulfonylurea switch therapy in monogenic neonatal diabetes

- **Singapore regulatory pathway:**
  - If any indication is eventually pursued, a de novo HSA registration process would be required (currently 0 licensed products)

- **Deprioritise remaining predictions:**
  - Ranks 1–8 and rank 10 all lack mechanistic plausibility and supporting evidence; no further resources should be allocated without new experimental data

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any clinical application. This analysis reflects a data cutoff of 2026-04-04.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

