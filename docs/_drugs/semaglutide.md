---
layout: default
title: Semaglutide
parent: Low Evidence (L5)
nav_order: 896
evidence_level: L5
indication_count: 10
---

# Semaglutide
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

# Semaglutide: From Weight Management to Focal Stiff Limb Syndrome

## One-Sentence Summary

Semaglutide is a GLP-1 receptor agonist marketed in Singapore as Wegovy injection pens. The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, a rare neurological disorder. **No clinical trials and no publications** currently support this prediction, so it rests on a graph-based score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the HSA data supplied. The Wegovy-branded products are generally positioned for chronic weight management. |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Semaglutide belongs to the GLP-1 receptor agonist class, which lowers glucose in a glucose-dependent way and reduces body weight. Its efficacy in metabolic indications is well established.

Focal stiff limb syndrome is a rare autoimmune/neurological disorder linked to impaired GABAergic signalling. No established GLP-1 receptor pathway connects it to semaglutide. The only speculative bridge is the anti-inflammatory effects sometimes reported for GLP-1 receptor agonists, and nothing retrieved supports it.

The score of 98.64% is identical to that of classic stiff person syndrome (rank 2). This suggests a shared disease-node artifact in the knowledge graph rather than an independent signal for this disease. The prediction should be treated as a hypothesis for screening, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

The Singapore registrations (15 in total) are all injectable solutions. The oral tablet route is also listed for semaglutide. Approved indication text is not recorded for these licences. The first 5 are shown below.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16708P | WEGOVY Solution for Injection in Pre-filled Pen 2.4MG/0.75ML | Injection, solution |
| SIN16745P | WEGOVY 0.5 MG/DOSE FlexTouch Solution for Injection in Pre-filled Pen 1.34 MG/ML | Injection, solution |
| SIN16706P | WEGOVY Solution for Injection in Pre-filled Pen 0.25MG/0.5ML | Injection, solution |
| SIN16705P | WEGOVY Solution for Injection in Pre-filled Pen 0.5MG/0.5ML | Injection, solution |
| SIN16746P | WEGOVY 1 MG/DOSE FlexTouch Solution for Injection in Pre-filled Pen 1.34 MG/ML | Injection, solution |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5, with no trials, no literature, and no plausible mechanistic link. The high score looks like a graph artifact, since it is identical to the score for classic stiff person syndrome. The other nine predicted indications are also L5 and Hold. The only literature retrieved for any of them (pancreatic agenesis) is tangential preclinical or safety material.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the Singapore licences, to confirm the original indication
- Mechanism of action data from DrugBank
- A targeted literature search for GLP-1 receptor agonists in stiff person spectrum disorders, covering case reports and mechanistic studies
- Review of the identical-score pattern across the stiff person disease nodes to rule out a graph artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

