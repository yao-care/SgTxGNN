---
layout: default
title: Rasburicase
parent: Low Evidence (L5)
nav_order: 847
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase: From Tumor-Lysis-Related Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase enzyme that lowers serum uric acid. It is approved for acute hyperuricemia related to tumor lysis, though the Singapore license record supplied has no indication text.
The TxGNN model predicts it may be effective for **renal hypouricemia**, a condition in which uric acid is already low.
There are **0 clinical trials** and **0 publications** supporting this prediction, and the mechanism points the opposite way, so it is most likely a model artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore license record (the pack's rationale describes acute tumor-lysis-related hyperuricemia) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available. Rasburicase is a recombinant urate oxidase. It converts uric acid to allantoin and lowers serum uric acid.

The predicted indication works against this mechanism. Renal hypouricemia is already a state of low uric acid, so further lowering is not therapeutic and could be harmful. The high TxGNN score is most likely a graph-proximity artifact, caused by shared uric acid and urate pathway nodes, and is not evidence of benefit.

Among the other nine predictions, only **partial HPRT deficiency** (Kelley-Seegmiller variant) has a plausible biological link, because it involves purine overproduction and hyperuricemia. Even there, rasburicase is an infused enzyme for acute use and is poorly suited to chronic management. It also does not address xanthine and hypoxanthine accumulation. The remaining predictions (hepatic porphyria, portal and hepatic vascular conditions, renal tubular acidosis, phenylalanine metabolism disorders) have no identifiable mechanistic link.

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
| SIN12055P | FASTURTEC POWDER FOR SOLUTION FOR INFUSION 1.5 mg/vial | Injection, powder, for solution | Not listed in the record |

---

## Safety Considerations

- **Mechanistic concern**: Further lowering of urate in a patient who already has low uric acid (renal hypouricemia) could be harmful.

Please refer to the package insert for all other safety information, including warnings, contraindications, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials or publications. The drug's urate-lowering mechanism runs opposite to the condition's pathophysiology, so the predicted benefit is implausible and there is a potential for harm.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- The approved indication text for SIN12055P
- A mechanistic and clinical review of partial HPRT deficiency, the most plausible of the ten predictions, if a repurposing direction is still wanted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

