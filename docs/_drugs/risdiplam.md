---
layout: default
title: Risdiplam
parent: Low Evidence (L5)
nav_order: 874
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Risdiplam: predicted new indication Acne (evidence level L5). Approved use: Not listed in the Singapore license record (the drug is known as an S…"
monitor_inn: "Risdiplam"
predicted_indications: ["acne (disease)", "drug-induced osteoporosis", "zinc, elevated plasma", "common wart", "metastatic melanoma", "dermatitis", "non-cutaneous melanoma", "acrodermatitis chronica atrophicans", "epithelioid cell melanoma", "eyelid melanoma"]
---

# Risdiplam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Risdiplam: From Spinal Muscular Atrophy to Acne
{: .text-alpha }

## One-Sentence Summary

Risdiplam is an oral SMN2 splicing modifier that is marketed in Singapore as EVRYSDI and is generally used for spinal muscular atrophy (SMA). The Singapore license record compiled for this report does not list an indication text.
The TxGNN model predicts it may be effective for **acne**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Singapore license record (the drug is known as an SMA treatment) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Risdiplam is known to be an SMN2 splicing modifier that increases inclusion of exon 7 in SMN2 transcripts, and it is used in spinal muscular atrophy. No mechanistic pathway is supported that links SMN2 splicing modulation to sebaceous gland biology or *Cutibacterium acnes*.

The high TxGNN score (99.45%, rank 6885) is therefore best read as a possible knowledge-graph artifact, for example driven by shared gene-network neighbours or off-target associations, and not as independent biological evidence. The other top-ranked predictions are also unsupported by the data:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Drug-induced osteoporosis | 97.72% | L5 | Reduced bone density in SMA relates to the disease, not to a therapeutic effect of risdiplam |
| 3 | Zinc, elevated plasma | 97.32% | L5 | A laboratory finding; no plausible mechanism identified |
| 4 | Common wart | 97.21% | L5 | HPV-driven; no antiviral or immunomodulatory mechanism supported |
| 5 | Metastatic melanoma | 96.84% | L5 | Altered splicing is a theme in cancer, but any link is speculative |
| 6 | Dermatitis | 96.62% | L5 | No anti-inflammatory or skin-barrier mechanism supported |
| 7 | Non-cutaneous melanoma | 96.18% | L5 | Likely reflects melanoma-related graph neighbours |
| 8 | Acrodermatitis chronica atrophicans | 96.11% | L5 | Borrelia infection, treated with antibiotics; no link to risdiplam |
| 9 | Epithelioid cell melanoma | 95.93% | L5 | Speculative, based on similarity to other melanoma terms |
| 10 | Eyelid melanoma | 95.88% | L5 | Likely reflects clustering of melanoma nodes in the graph |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16349P | EVRYSDI POWDER FOR ORAL SOLUTION 0.75 MG/ML | Powder, for solution | Not listed in the license record |

---

## Safety Considerations

- **Drug Interactions** (2 moderate-level interactions found):
  - Metformin (Moderate)
  - Methylnaltrexone (Moderate)

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials or publications were found for acne or for any of the other nine top-ranked indications, and no plausible mechanistic link is supported. The evidence level is L5 for all of them.

**To proceed, the following is needed:**
- Mechanism of action data for risdiplam from DrugBank, to allow a proper mechanistic analysis
- The HSA package insert, to confirm the approved indication, warnings and contraindications, and complete safety screening
- Preclinical or mechanistic evidence connecting SMN2 splicing modulation to acne biology
- A route compatibility assessment: risdiplam is available only as an oral solution, while acne is commonly treated topically
- A review of whether the prediction is a knowledge-graph artifact, for example by checking the shared neighbours that drive the score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

