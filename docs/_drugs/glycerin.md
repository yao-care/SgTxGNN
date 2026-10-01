---
layout: default
title: Glycerin
parent: Low Evidence (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
---

# Glycerin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Glycerin: From Constipation Relief to Cauda Equina Syndrome

## One-Sentence Summary

Glycerin is marketed in Singapore as an osmotic laxative in syrup and enema products, so its original use appears to be constipation relief. The registrations carry no approved-indication text, so this is inferred from product type. The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction, and no plausible pharmacological link was found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in registrations (inferred: constipation, from syrup/enema products) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, glycerin is an osmotic agent used as a laxative, and its use for constipation is well established. Mechanistically, there is no evident route by which it would help cauda equina syndrome.

Cauda equina syndrome is a compressive injury to the lumbosacral nerve roots. Osmotic dehydration is not a recognised treatment for it, and the supplied data identified no pharmacological link, trials or literature. The high score (rank 5,615 in the model's ranking) is best read as a statistical artefact of the knowledge graph rather than a mechanistic signal.

Other predictions for glycerin have somewhat more plausible rationales, though all are still weak:
- **Open-angle glaucoma** (score 99.59%, L4): osmotic lowering of intraocular pressure is established mainly for acute angle-closure episodes, so the link to chronic open-angle disease is indirect. The supplied literature does not show glycerin acting as a therapeutic agent there.
- **Irritable bowel syndrome** (score 99.49%, L4): plausible only for constipation-predominant IBS, with no IBS-specific evidence supplied.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN02748P | LEMON SWEET PURGATIVE SYRUP | Syrup | Syarikat Wen Ken Drug Sdn Bhd |
| SIN02959P | HUACHI ENEMA | Enema | Jen Sheng Pharmaceutical Co Ltd |
| SIN03514P | MINICA S ENEMA | Enema | Yukinomoto Honten Co., Ltd |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for glycerin in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials, no literature and no plausible mechanism for cauda equina syndrome. Package insert safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (blocking gap)
- Mechanism of action data, for example from DrugBank
- Approved-indication text for the three Singapore registrations, to confirm the original indication
- A documented mechanistic rationale for cauda equina syndrome; otherwise consider redirecting effort to the glaucoma or constipation-predominant IBS candidates

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

