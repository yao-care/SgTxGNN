---
layout: default
title: Luspatercept
parent: 僅模型預測 (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
---

# Luspatercept
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

# Luspatercept: From Beta-Thalassemia / MDS-Related Anemia to Monosomy X

## One-Sentence Summary

Luspatercept (Reblozyl) is a first-in-class erythroid maturation agent that blocks TGF-β superfamily ligands (GDF11/GDF8), approved globally for transfusion-dependent beta-thalassemia and MDS-associated anemia with ring sideroblasts.
The TxGNN model predicts it may be effective for **Monosomy X (Turner Syndrome)** as its top-ranked new indication; however, this prediction carries **no supporting clinical trials or published literature**.
Among all 10 predicted indications in this Evidence Pack, **Pyruvate Kinase Deficiency** (rank 6, L1) and **Beta-Thalassemia Beta+ Silent Allele** (rank 7, L1) represent substantially stronger mechanistic and clinical repurposing candidates.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally approved for beta-thalassemia and MDS-related anemia |
| Predicted New Indication | Monosomy X (Turner Syndrome, 45,X) |
| TxGNN Prediction Score | 96.0% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Luspatercept is a recombinant fusion protein (ActRIIA-IgG1 Fc) that acts as a TGF-β superfamily ligand trap. It selectively binds GDF11 and GDF8, blocking SMAD2/3 phosphorylation and thereby promoting late-stage erythroid differentiation. This mechanism directly corrects ineffective erythropoiesis — the pathological accumulation of immature red blood cell precursors that fail to mature — in diseases such as beta-thalassemia and MDS with ring sideroblasts.

Monosomy X (Turner syndrome, 45,X) is a chromosomal aneuploidy characterized by gonadal dysgenesis, short stature, cardiovascular anomalies, and endocrine dysfunction. While some Turner syndrome patients may experience mild secondary anemia (e.g., from hypothyroidism or chronic inflammation), the core pathology is a structural chromosomal defect entirely upstream of the erythroid maturation pathway that Luspatercept targets. Luspatercept does not repair chromosomal abnormalities, restore sex hormone production, or address the primary disease drivers in Turner syndrome.

This high prediction score (96.0%) most likely reflects topological proximity between rare hematological and chromosomal disease nodes within the TxGNN knowledge graph, rather than a genuine biological relationship. No preclinical studies, mechanism papers, or clinical observations have been published linking GDF11/SMAD2 blockade to Turner syndrome management. This prediction is assessed as a knowledge graph structural artifact with negligible translational potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Luspatercept in Monosomy X.

---

## Literature Evidence

Currently no related literature available for Luspatercept in Monosomy X.

---

## Singapore Market Information

Luspatercept is not currently registered in Singapore. No HSA authorizations are on record.

> **Note:** Luspatercept (Reblozyl®) holds FDA approval (November 2019) for transfusion-dependent beta-thalassemia and (April 2020) for lower-risk MDS with ring sideroblasts, as well as EMA approval for similar indications. A Singapore (HSA) regulatory submission has not been identified in this data package.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data, key warnings, or contraindication records are available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction of Monosomy X is mechanistically implausible — Luspatercept's erythroid maturation mechanism has no established connection to the chromosomal and endocrine pathophysiology of Turner syndrome — and is entirely unsupported by clinical or preclinical evidence. This prediction should not advance to clinical evaluation.

**Higher-priority candidates identified within this Evidence Pack:**

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|------------|---------------|----------------|
| 6 | Pyruvate Kinase Deficiency of Red Cells | 93.8% | L1 | Proceed with Guardrails |
| 7 | Beta-Thalassemia, Beta+, Silent Allele | 93.3% | L1 | Proceed with Guardrails |
| 10 | Hb Bart's Hydrops Fetalis | 92.8% | L4 | Research Question |

**To proceed with the higher-priority candidates (Ranks 6 & 7), the following is needed:**

- Retrieve full MOA documentation from DrugBank (resolves data gap DG002)
- Retrieve Singapore package insert warnings and contraindications (resolves data gap DG001)
- Conduct targeted ClinicalTrials.gov search for Luspatercept + pyruvate kinase deficiency, as the Evidence Pack query returned zero results but published investigator-initiated studies may exist
- Develop a Singapore regulatory pathway strategy, given HSA non-registration status
- Confirm route-of-administration compatibility (Luspatercept is subcutaneous injection; verify feasibility for the target indication patient population)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

