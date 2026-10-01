---
layout: default
title: Adenosine
parent: Low Evidence (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Adenosine
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

# Adenosine: From Unrecorded Original Indication to Obsolete Bundle Branch Block

## One-Sentence Summary

Adenosine is an injectable drug marketed in Singapore under two registrations, but the HSA data provided does not record its approved indication.
The TxGNN model ranks **obsolete bundle branch block** as its top predicted new use, but this is a model prediction only, with **0 clinical trials** and **0 publications** behind it. The term is also flagged "obsolete" in the ontology, so it is probably a legacy or duplicate node.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (HSA indication text is empty) |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Adenosine's known pharmacology is that it slows conduction through the atrioventricular (AV) node. Because of this, it can unmask or cause conduction block rather than treat it.

The high TxGNN score most likely reflects the model linking adenosine to conduction-system disorders in the knowledge graph. The "obsolete" flag suggests a legacy or duplicate ontology node. No trial or paper supports a therapeutic benefit, and the mechanism argues against one. The prediction is therefore not considered credible as a treatment idea.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16391P | CADEN SOLUTION FOR INJECTION 6 MG / 2 ML | Injection, solution | Not recorded |
| SIN07679P | ADENOCOR INJECTION 3MG/ML | Injection | Not recorded |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or literature. The target term is flagged obsolete, and adenosine's AV-nodal blocking effect argues against benefit in conduction block.

**To proceed, the following is needed:**
- Confirm whether the "obsolete bundle branch block" node maps to a current disease term. If it does not, drop the prediction.
- Obtain the HSA package insert to fill in the approved indication, warnings and contraindications.
- Retrieve adenosine's mechanism of action from DrugBank.
- Consider the two better-supported candidates in this pack instead. Both are L4, and both need verification before any decision:
  - **Catecholaminergic polymorphic ventricular tachycardia**: the evidence is a single case report of ATP terminating bidirectional VT and preclinical work. The Phase 2a trial NCT07263139 tests AGP100, which is not confirmed to be adenosine-related.
  - **Open-angle glaucoma**: the Phase 3 trial NCT02565173 tests trabodenoson, an adenosine A1 agonist, so it is class-level evidence only. Its outcome should be checked before it is treated as supportive.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

