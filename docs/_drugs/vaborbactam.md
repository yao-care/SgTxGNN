---
layout: default
title: Vaborbactam
parent: Low Evidence (L5)
nav_order: 1038
evidence_level: L5
indication_count: 10
---

# Vaborbactam
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

# Vaborbactam: From Bacterial Infection (Beta-Lactamase Inhibitor) to Osteoarthritis

## One-Sentence Summary

Vaborbactam is a beta-lactamase inhibitor with no antibacterial activity of its own. It is used only in combination with meropenem to treat bacterial infections.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is model-only and, in our assessment, most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration text. Used as a beta-lactamase inhibitor with meropenem for bacterial infections |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Vaborbactam is a cyclic boronic acid serine beta-lactamase inhibitor. It protects a partner antibiotic (meropenem) from enzymatic breakdown and has no intrinsic antibacterial activity.

**The prediction is not mechanistically supported.** Vaborbactam has no known action on cartilage, synovial inflammation, or joint degradation pathways. Bacterial beta-lactamase inhibition does not connect to the biology of osteoarthritis.

The very high score (0.985) most likely reflects sparse drug annotation in the knowledge graph. The drug has no recorded mechanism, indications, or drug interactions there. The same pattern appears across the other top predictions:

- Osteoarthritis susceptibility
- Rheumatoid arthritis
- Gout
- Several rare skeletal dysplasias (pseudoachondroplasia, brachyolmia, acromesomelic dysplasia and related syndromes)
- Hepatic porphyria

All of these look like graph-neighbourhood bias rather than a drug-specific signal. None has any clinical or literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN17224P | VABOREM POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 1G/1G | Injection, powder, for solution |

The manufacturer is ACS DOBFAR S.P.A. The product is injectable only.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried database.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials, no publications, and no plausible mechanism linking a beta-lactamase inhibitor to osteoarthritis. The high score is most likely an artifact of sparse drug annotation in the knowledge graph. The injectable-only presentation is also unlikely to suit a chronic joint condition, although route compatibility has not yet been assessed.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, to reassess any mechanistic link
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Any preclinical or clinical evidence that vaborbactam affects joint or cartilage biology. Without it, this candidate should not advance

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

