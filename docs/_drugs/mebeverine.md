---
layout: default
title: Mebeverine
parent: Low Evidence (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
---

# Mebeverine
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

# Mebeverine: From Spasm-Related Gastrointestinal Symptoms to Cauda Equina Syndrome

## One-Sentence Summary

Mebeverine is a musculotropic antispasmodic used for spasm-related gastrointestinal symptoms. The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this is a **model prediction only**, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spasm-related gastrointestinal symptoms (general pharmacological use; the Singapore licence records contain no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 98.01% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, mebeverine is a musculotropic antispasmodic that relaxes smooth muscle. Its efficacy in gastrointestinal spasm is the basis for the theory that it could apply to other smooth-muscle problems.

Cauda equina syndrome involves bowel and bladder sphincter and detrusor dysfunction. A smooth-muscle relaxant could in theory ease some of these symptoms. It would not treat the underlying nerve compression, which is a surgical emergency, so any benefit would be symptomatic at most.

The link rests on general pharmacology alone. No trials or publications support it, and the high score may reflect knowledge-graph proximity rather than real clinical signal.

Other predictions from the model, all also L5 except one:
- **Neurogenic bladder (score 96.8%):** biologically plausible through smooth-muscle relaxation, but the disease term is flagged obsolete in the ontology. It is classed as a Research Question, and the mapping should be checked first.
- **Gastroduodenitis (score 81.1%):** the only candidate with any literature (L4). It is a single 2009 review on gastroesophageal reflux treatment that does not mention mebeverine, so it is at most indirect context.
- **Insomnia, rhinitis, and the mitral valve prolapse entries:** no plausible mechanism, likely knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN09873P | MEBETIN TABLET 135 mg | Tablet, sugar coated (oral) | Sam Chun Dang Pharm Co Ltd |
| SIN07666P | DUSPATALIN RETARD CAPSULE 200 mg | Capsule (oral) | Abbott Biologicals B.V. / Mylan Laboratories SAS / Abbott Laboratories GmbH |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is scored high (98.01%) but has no trials or literature behind it, so it is L5. The proposed mechanism is theoretical, and mebeverine would not address the cause of cauda equina syndrome, which needs urgent surgery.

**To proceed, the following is needed:**
- Mechanism of action data for mebeverine (for example, from DrugBank)
- Package insert warnings and contraindications from HSA, needed for safety screening
- Approved indication text for the Singapore licences
- A literature and trial search targeted at mebeverine in bladder or bowel dysfunction from neurological causes
- Resolution of the obsolete "neurogenic bladder" ontology mapping, if that candidate is pursued instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

