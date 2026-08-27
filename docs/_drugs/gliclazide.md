---
layout: default
title: Gliclazide
parent: 僅模型預測 (L5)
nav_order: 476
evidence_level: L5
indication_count: 10
---

# Gliclazide
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

# Gliclazide: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Gliclazide is a second-generation sulfonylurea, widely used for Type 2 Diabetes Mellitus by stimulating pancreatic β-cell insulin secretion.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome (SPS)**,
with a prediction score of **97.96%** — however, **no clinical trials and no published literature** currently support this direction, making this a pure computational hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (sulfonylurea class oral antidiabetic) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 97.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally recorded in this Evidence Pack. Based on established pharmacological knowledge, Gliclazide is a second-generation sulfonylurea that blocks ATP-sensitive potassium channels (KATP / SUR1) on pancreatic β-cells, causing membrane depolarisation and subsequent insulin release. It also possesses antioxidant properties (free radical scavenging via its azabicyclo-octyl ring) not found in first-generation agents.

The scientific rationale for the SPS prediction lies in a shared molecular target. Classic Stiff Person Syndrome is characterised by anti-GAD65 (glutamic acid decarboxylase 65) autoantibodies. GAD65 is expressed not only in pancreatic β-cells — where it participates in GABA synthesis — but also in GABAergic interneurons of the central nervous system. When GAD65 function is impaired, GABA synthesis decreases, leading to disinhibition of motor neurons and the cardinal symptom of muscle rigidity. The hypothesis is that KATP channel blockade by Gliclazide, which is expressed in CNS neurons as well as β-cells, could theoretically modulate GABAergic synaptic transmission and partially compensate for the GAD65-deficient GABA synthesis deficit.

It is important to emphasise that this mechanistic link, while scientifically coherent, remains entirely theoretical and has not been tested in preclinical models or clinical settings. The connection is two steps removed: Gliclazide → KATP blockade in neurons → altered GABA transmission → SPS symptom modulation. No peer-reviewed study, animal experiment, or case report has yet explored this pathway for SPS.

---

## All Predicted Indications — Summary

The TxGNN model generated 10 candidate indications for Gliclazide. All are L5 (computational prediction only).

| Rank | Disease | Score | Mechanistic Plausibility | Recommendation |
|------|---------|-------|--------------------------|----------------|
| 1 | Classic Stiff Person Syndrome | 97.96% | Moderate — GAD65/KATP/GABAergic hypothesis | Research Question |
| 2 | Focal Stiff Limb Syndrome | 97.96% | Moderate — SPS subtype, same pathway | Research Question |
| 3 | Thiamine-Responsive Dysfunction Syndrome (TRMA) | 97.79% | Moderate — β-cell dysfunction component; thiamine is primary therapy | Research Question |
| 4 | Opsismodysplasia | 97.72% | Weak — SHIP2/PI3K pathway is very indirect | Hold |
| 5 | Pancreatic Agenesis | 96.64% | None — target tissue (β-cells) absent | Hold |
| 6 | Drug-Induced Localized Lipodystrophy | 96.43% | Indirect — reducing insulin injection frequency + antioxidant effect | Research Question |
| 7 | Centrifugal Lipodystrophy | 96.23% | Weak — possible clustering artefact in model | Hold |
| 8 | Pressure-Induced Localized Lipoatrophy | 96.14% | None — mechanical cause, no pharmacological pathway | Hold |
| 9 | Idiopathic Localized Lipodystrophy | 95.94% | Weak — insufficient mechanistic basis | Hold |
| 10 | Autoimmune Oophoritis | 88.15% | Weak — antioxidant anti-inflammatory effect is non-specific | Hold |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Gliclazide in any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for Gliclazide in any of the 10 predicted indications.

---

## Singapore Market Information

Gliclazide is **not currently registered** with the Health Sciences Authority (HSA) in Singapore. No product authorisations on record.

> **Note:** Gliclazide is registered and widely marketed in many regional markets including Taiwan, Japan, Europe (e.g., Diamicron®, Diamicron MR®), Australia, and across Southeast Asia. Its absence from Singapore's HSA register is a regulatory gap specific to this jurisdiction and does not reflect the drug's global availability or safety profile.

---

## Safety Considerations

Formal safety data (warnings, contraindications, drug interactions) was not retrievable in this Evidence Pack cycle.

> Please refer to the package insert and current HSA/regulatory guidance for complete safety information. As a sulfonylurea, general class considerations include: hypoglycaemia risk (especially in elderly, renally impaired, or food-restricted patients), avoidance in Type 1 Diabetes and diabetic ketoacidosis, and potential interactions with other antidiabetics, NSAIDs, and CYP2C9 inhibitors/inducers.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (Classic Stiff Person Syndrome, score 97.96%) carries a scientifically interesting mechanistic hypothesis linking pancreatic KATP channel pharmacology to GABAergic CNS dysfunction via shared GAD65 biology. However, the evidence base is entirely computational (L5), with zero clinical trials, zero peer-reviewed publications, and zero preclinical data supporting this specific application. Additionally, Gliclazide is not registered in Singapore, creating a significant regulatory barrier. The prediction for Pancreatic Agenesis (Rank 5) is pharmacologically implausible and illustrates the model's limitations in filtering out biologically impossible candidates.

**To proceed, the following is needed:**

- **MOA confirmation:** Obtain complete DrugBank entry for Gliclazide (DB01120) to formally document SUR1/KATP mechanism and off-target CNS effects
- **Preclinical feasibility study:** Test Gliclazide in a validated GAD65-antibody animal model of SPS (e.g., GAD65 immunised rodents) to confirm CNS KATP engagement
- **Literature gap analysis:** Systematic review of sulfonylurea effects on GABAergic neurotransmission in any CNS disorder, to establish proof-of-concept
- **Safety data collection:** Download and parse TFDA and EMA/TGA product monographs to complete the DG001 blocking data gap before any clinical consideration
- **Singapore regulatory pathway:** If preclinical evidence warrants progression, initiate HSA registration assessment or identify a suitable registered formulation for potential off-label use discussion
- **Prioritisation decision:** Of the 10 predicted indications, Classic SPS (Rank 1) and Thiamine-Responsive Dysfunction Syndrome (Rank 3) carry the most coherent mechanistic rationale and should be the focus of any exploratory literature mining effort; Pancreatic Agenesis (Rank 5), Pressure-Induced Lipoatrophy (Rank 8), and Centrifugal Lipodystrophy (Rank 7) should be deprioritised due to absent mechanistic plausibility

---

*This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

