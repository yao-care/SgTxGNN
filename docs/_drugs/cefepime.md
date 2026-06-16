---
layout: default
title: Cefepime
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Cefepime
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

# Cefepime: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Cefepime is a fourth-generation cephalosporin antibiotic, established in clinical practice for empirical treatment of serious bacterial infections — including febrile neutropenia, hospital-acquired pneumonia, and complicated urinary tract infections.
The TxGNN model's top prediction identifies **Polyclonal Hyperviscosity Syndrome** as a candidate new indication, scoring a high confidence of **98.69%**.
However, this prediction is supported by **zero clinical trials and zero publications**, placing it at evidence level **L5**, and the mechanistic rationale is assessed as implausible — the high score likely reflects a knowledge graph structural artifact rather than a genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore (no HSA indication data available); globally established for serious bacterial infections and febrile neutropenia |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 98.69% |
| Evidence Level | L5 (model prediction only; no supporting studies) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Cefepime exerts its antibacterial effect by binding to penicillin-binding proteins (PBPs) and inhibiting bacterial cell wall synthesis. As a fourth-generation cephalosporin, it offers broad-spectrum coverage including anti-*Pseudomonas aeruginosa* activity and stability against AmpC beta-lactamases — properties that make it valuable for empirical treatment of febrile neutropenia and healthcare-associated infections.

Polyclonal hyperviscosity syndrome is a fundamentally different disease process: it arises from massive overproduction of multiple immunoglobulin clones across different B-cell lineages, driving pathological elevation of blood viscosity. Its pathological core is immune dysregulation and aberrant protein production — mechanisms entirely outside the antibacterial spectrum of Cefepime. Cefepime has no documented anti-inflammatory, immunomodulatory, or anti-immunoglobulin activity, and no known interaction with the signalling pathways governing B-cell proliferation or immunoglobulin secretion.

The mechanistic analysis embedded in this Evidence Pack explicitly flags that the high TxGNN score (0.9869) for this indication most likely reflects a **knowledge graph co-occurrence bias** — a strong statistical link between plasma cell disease nodes and antibiotic drug nodes in the knowledge graph, driven by the clinical reality that antibiotics are routinely administered to immunocompromised plasma cell disease patients for infection management. This is a known failure mode of graph-based repurposing models: the model learns that a drug frequently appears in the context of a disease, without discriminating between treating the disease versus treating its infectious complications. **This prediction is assessed as scientifically implausible under current mechanistic understanding.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered for polyclonal hyperviscosity syndrome.

---

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

---

## Singapore Market Information

Cefepime is currently **not registered** with the Health Sciences Authority (HSA) in Singapore. No product authorizations, dosage form records, or approved indication texts are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Key safety signals identified from broader evidence review** (sourced from literature collected across other predicted indications in this pack):
>
> - **Cefepime-induced neurotoxicity (CIN):** Encephalopathy, myoclonus, and seizures are documented adverse effects, with significantly elevated risk in patients with renal impairment due to drug accumulation. This is a well-established safety concern requiring dose adjustment by creatinine clearance.
> - **Elevated free drug exposure in hypoalbuminaemia:** Cefepime's protein binding is approximately 20%. In patients with severe hypoalbuminaemia (e.g., congenital analbuminaemia or liver failure), free drug concentrations rise substantially, increasing neurotoxicity risk.
> - **Acute interstitial nephritis:** A biopsy-confirmed case has been reported in the literature (PMID 25886295).
> - **Drug-induced pancreatic enzyme elevation:** Some literature notes Cefepime as a rare cause of pancreatitis-like presentations, which is relevant to the hyperamylasaemia prediction cluster.
>
> These signals are relevant to patient selection and monitoring in any future use scenarios.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Cefepime's mechanism of action — PBP binding and bacterial cell wall synthesis inhibition — has no plausible connection to immunoglobulin overproduction or blood viscosity regulation in polyclonal hyperviscosity syndrome. The TxGNN model's high confidence score is assessed as a knowledge graph structural artefact arising from the co-occurrence of antibiotics and plasma cell diseases in clinical contexts, not from a genuine pharmacological relationship. With zero supporting clinical trials and zero supporting literature, there is no evidence base to justify further investigation of this specific pairing.

**To proceed with any further evaluation, the following is needed:**

- **Mandatory:** Retrieve the full Cefepime prescribing information (package insert) from HSA or international regulatory sources to complete the safety gap assessment (DG001)
- **Mandatory:** Query the DrugBank API for complete mechanism of action data to enable proper mechanistic link analysis (DG002)
- **Recommended:** Apply knowledge graph de-biasing techniques to re-score TxGNN predictions for Cefepime, filtering out co-occurrence signals driven by infection management rather than direct therapeutic effect
- **For any other indication in this pack:** Rank 8 (septicemic plague) and Rank 10 (infectious otitis media) carry stronger mechanistic rationale, with animal-model data (PMID 20583467) and microbiological plausibility respectively — these are more appropriate candidates for further research question development if resources are available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

