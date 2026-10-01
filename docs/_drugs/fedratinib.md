---
layout: default
title: Fedratinib
parent: Low Evidence (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Fedratinib
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

# Fedratinib: From Myelofibrosis to Benign PEComa

## One-Sentence Summary

Fedratinib is an oral JAK2-selective kinase inhibitor, registered in Singapore as INREBIC capsules. The TxGNN model predicts it may be effective for **benign PEComa** (and related conditions such as lymphangiomyoma), but **no clinical trials and no publications** currently support this direction. It is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myelofibrosis (general labelling knowledge; the supplied Singapore record and DrugBank entry list no indication text) |
| Predicted New Indication | Benign PEComa |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. Fedratinib is a JAK2-selective inhibitor, and it also has FLT3 and BRD4 activity. Its efficacy in its original setting, which is JAK/STAT-driven myeloproliferative disease, is established.

For the top-ranked prediction, the link is weak. PEComa and the related lymphangiomyoma and lymphangioleiomyomatosis are driven mainly by mTOR pathway hyperactivation (TSC1/TSC2 loss). Any connection to a JAK2 inhibitor would run through indirect JAK/STAT-mTOR crosstalk. The 99.84% score is a graph-based signal only.

Other predictions in the top 10 follow a similar pattern:

| Predicted Disease | Score | Rationale | Assessment |
|------|------|------|------|
| Dermatofibrosarcoma protuberans | 99.80% | Driven by PDGFRB signalling. Fedratinib has no known PDGFR activity. | Weak link |
| Rhabdoid tumor / familial rhabdoid tumor | 99.78% / 99.77% | Loss of SMARCB1. Fedratinib's BRD4 activity offers a loose epigenetic angle. | Speculative, unvalidated |
| Familial Mediterranean fever | 99.75% | Pyrin inflammasome/IL-1 disease. JAK2 inhibition might dampen downstream cytokines. | Indirect |
| Hemophagocytic lymphohistiocytosis (HLH), malignancy- or infection-associated | 99.74% | IFN-γ-driven hypercytokinemia signals through JAK1/2-STAT1, and JAK inhibition is a recognised concept in HLH. | **Most biologically plausible in the set** |

The HLH rationale rests on JAK inhibitors as a class, not on fedratinib data. Fedratinib is JAK2-selective with less JAK1 activity, and it carries a Wernicke encephalopathy boxed warning, which is a concern in a critically ill population. For infection-associated HLH, the trigger must also be treated, which complicates any repurposing study design.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16617P | INREBIC CAPSULES 100 MG (Celgene International Sarl) | Capsule | Not stated in the supplied record |

Fedratinib is available in Singapore only as an oral capsule.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. Cytopenias are a recognised concern with JAK inhibitors. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Full blood count, liver and renal function, and neurological status (given the Wernicke encephalopathy warning) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Key Warnings**: The predictions record a Wernicke encephalopathy boxed warning for fedratinib. This is especially relevant in critically ill populations such as HLH.

The full warnings and contraindications from the Singapore package insert were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone, with no trials or publications (L5). The mechanistic links to the top-ranked mTOR-driven diseases are indirect and speculative. HLH is the only prediction with a credible class-level rationale, and it can be kept as a research question rather than a candidate for development.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data (for example, from DrugBank)
- Preclinical or clinical evidence specific to fedratinib in HLH, or in PEComa/LAM if mTOR-JAK/STAT crosstalk is to be pursued
- A safety assessment of the Wernicke encephalopathy risk in the target population

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

