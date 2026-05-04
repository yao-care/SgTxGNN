---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Deferiprone
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

# Deferiprone: From Iron Overload (Thalassemia) to Hepatic Porphyria

## One-Sentence Summary

Deferiprone (DB08826) is an oral iron chelator with established global use in transfusion-dependent iron overload, most notably beta-thalassemia major — though its registered indications are not reflected in the Singapore database (data gap in this Evidence Pack).
The TxGNN model predicts it may be effective for **Hepatic Porphyria**, with **0 clinical trials** and **2 preclinical/case-series publications** currently supporting this direction, placing overall evidence at the preclinical stage.
The mechanistic rationale — iron excess as a key driver of porphyrin accumulation — is biologically plausible, but robust human clinical data specific to hepatic porphyria remain absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iron overload in transfusion-dependent thalassemia *(note: original_indications field empty in this Evidence Pack — data gap)* |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 (preclinical studies and mechanism studies only) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Deferiprone (3-hydroxy-4-pyridinone, L1) is a small-molecule oral iron chelator. Its mechanism centres on forming stable 3:1 complexes with ferric iron (Fe³⁺), facilitating urinary iron excretion and reducing tissue iron burden. Although detailed MOA data was not retrievable via DrugBank in this Evidence Pack, Deferiprone is a WHO Essential Medicine with decades of clinical use for iron overload in haemoglobinopathies. Its key mechanistic property — mobilising intracellular and hepatic iron — is directly relevant to the predicted indication.

Hepatic porphyria, particularly **Porphyria Cutanea Tarda (PCT)**, is characterised by elevated hepatic iron that inhibits uroporphyrinogen decarboxylase (UROD), the enzyme whose dysfunction leads to pathological porphyrin accumulation. Excess iron promotes reactive oxygen species (ROS) generation, which further impairs UROD and accelerates toxic uroporphyrin build-up in the liver. Standard phlebotomy works precisely by depleting hepatic iron — the same endpoint an oral chelator could achieve non-invasively, particularly in patients unsuitable for phlebotomy.

The TxGNN prediction therefore reflects a genuine mechanistic overlap: an iron-reducing drug applied to an iron-driven disease. The supporting literature confirms this concept in animal models (PCT mouse) and a related porphyria subtype (CEP), though no randomised clinical trials in hepatic porphyria patients have been conducted with Deferiprone. The evidence base remains at L4.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Preclinical / Case series | *Blood* | Iron chelation rescued hemolytic anemia and skin photosensitivity in a mouse model and case series of **Congenital Erythropoietic Porphyria (CEP)** — a related but distinct porphyria subtype. Supports the concept that iron reduction ameliorates porphyrin-driven pathology. |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Animal experiment | *Hepatology* | Deferiprone (L1) reduced hepatic uroporphyrin accumulation in **Hfe⁻/⁻ mice** (a PCT model) comparably to an iron-deficient diet. Directly demonstrates Deferiprone's iron-chelating effect in a porphyria cutanea tarda model. |

---

## Singapore Market Information

Deferiprone is not currently registered with the Health Sciences Authority (HSA) in Singapore. No authorisation records are available.

---

## Safety Considerations

Singapore-specific prescribing information (package insert warnings and contraindications) could not be retrieved, as Deferiprone is not registered in Singapore. Please refer to the approved package inserts from jurisdictions where Deferiprone is marketed (e.g., EU SmPC for Ferriprox®, or FDA label) for full safety information, including:

- Known serious risks: **agranulocytosis / neutropenia** (requires weekly absolute neutrophil count monitoring)
- GI side effects (nausea, vomiting, abdominal pain)
- Arthropathy
- Potential for zinc chelation

No drug–drug interaction data was returned in this Evidence Pack query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting Deferiprone for hepatic porphyria is limited to a PCT mouse model and a CEP case series — both indirectly related to the target indication. No human clinical trials exist, and Singapore regulatory status is absent (no HSA registration), making immediate clinical development in Singapore premature without a full regulatory pathway assessment.

**To proceed, the following is needed:**

- **Mechanistic gap fill**: Retrieve full DrugBank MOA entry and confirm iron-chelation specificity relevant to UROD inhibition reversal in PCT vs. other hepatic porphyrias
- **Safety dossier**: Obtain and parse Deferiprone package inserts (Ferriprox® EU SmPC / FDA label) to populate key warnings, contraindications, and DDI data — currently blocking (DG001)
- **Clinical feasibility study**: Assess whether Deferiprone could be tested in PCT patients who are poor candidates for phlebotomy (e.g., those with anaemia or poor venous access) — as a proof-of-concept Phase 1/2 study
- **Patient population scoping**: Estimate hepatic porphyria prevalence in Singapore (likely very rare) to determine commercial and public health justification
- **Regulatory pathway**: Consult HSA on requirements for first-in-Singapore registration of Deferiprone before any repurposing programme can advance
- **Comparator landscape**: Map existing treatments (phlebotomy, low-dose hydroxychloroquine) to define where Deferiprone could offer differentiated value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

