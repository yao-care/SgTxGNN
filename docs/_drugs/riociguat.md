---
layout: default
title: Riociguat
parent: Low Evidence (L5)
nav_order: 862
evidence_level: L5
indication_count: 10
---

# Riociguat
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

# Riociguat: From Pulmonary Arterial Hypertension to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Riociguat is marketed in Singapore as ADEMPAS and is described in the supplied literature as approved for pulmonary arterial hypertension (PAH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **0 clinical trials** and **0 publications** support this prediction.
It is a graph-based signal only and no mechanistic link is supported by the data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (from the supplied literature; the Singapore license records contain no indication text) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 94.92% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Riociguat is a soluble guanylate cyclase (sGC) stimulator. It raises cGMP, which causes pulmonary vasodilation and anti-remodeling effects. Detailed mechanism-of-action data from DrugBank is not currently available.

On the available evidence, this prediction is **not well supported**. Ambras syndrome is a rare congenital disorder with a developmental and genetic basis, and sGC stimulation has no established relevance to it. The high score (0.949) may simply reflect vasodilator-class neighbors in the knowledge graph.

Some vasodilators, such as minoxidil, are known to cause hypertrichosis, but through a different mechanism (K-ATP channel opening). The related hypertrichosis prediction (rank 5) should be read as a possible adverse-effect signal or graph artifact, not as a therapeutic lead.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14678P | ADEMPAS Film-Coated Tablet 0.5 mg | Tablet, film coated |
| SIN14679P | ADEMPAS Film-Coated Tablet 1.0 mg | Tablet, film coated |
| SIN14680P | ADEMPAS Film-Coated Tablet 1.5 mg | Tablet, film coated |
| SIN14681P | ADEMPAS Film-Coated Tablet 2.0 mg | Tablet, film coated |
| SIN14682P | ADEMPAS Film-Coated Tablet 2.5 mg | Tablet, film coated |

All five products are oral tablets manufactured by Bayer AG, Leverkusen. The records contain no approved-indication text.

## Safety Considerations

Package insert data (warnings, contraindications) was not retrieved, and no drug-interaction records were found. Please refer to the package insert for safety information.

The evidence pack's rationale text for other riociguat indications also flags the following. These notes are not from the package insert and should be verified against it:
- Pregnancy is contraindicated.
- Co-administration with PDE5 inhibitors or nitrates is contraindicated.
- CYP3A4/P-gp inhibitors, such as ritonavir-boosted regimens, raise riociguat exposure.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5, stage S0). No trials or publications exist, and no plausible sGC-mediated mechanism links riociguat to Ambras syndrome.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting sGC/cGMP signaling to the disease
- Download and parsing of the HSA package insert, which is a blocking gap for safety screening
- Mechanism-of-action data from DrugBank
- Evidence that this signal is not simply a vasodilator-class hypertrichosis adverse-effect association

**Other predictions for riociguat in this pack:**
Two lower-ranked predictions have far stronger support than this one. They are PAH associated with congenital heart disease (rank 6) and PAH associated with connective tissue disease (rank 8).

- **Evidence:** Both are rated L1 and "Proceed with Guardrails". The evidence is post hoc or prospectively planned subgroup analyses of the Phase 3 PATENT-1/-2 trials (PMID 26135803 and 27457511), and these are small subgroups.
- **Limits:** The connective tissue disease prediction has no registered trial in the pack.
- **Related prediction:** PAH associated with HIV infection (rank 10) is a research question only (L4).

If the goal is a practical repurposing candidate for riociguat, these are better starting points.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

