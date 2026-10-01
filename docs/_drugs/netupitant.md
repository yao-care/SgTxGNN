---
layout: default
title: Netupitant
parent: Low Evidence (L5)
nav_order: 701
evidence_level: L5
indication_count: 10
---

# Netupitant
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

# Netupitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Netupitant is a substance P/NK1 receptor antagonist, used in the fixed-dose combination AKYNZEO with palonosetron to prevent chemotherapy-induced nausea and vomiting.
The TxGNN model ranks **nephrogenic syndrome of inappropriate antidiuresis** as its top prediction, with a score of 98.35%.
There are currently **0 clinical trials** and **0 publications** supporting this direction, and the evidence pack itself describes the prediction as likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced nausea and vomiting (taken from the evidence pack's mechanism notes; the Singapore approved-indication text is empty) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 98.35% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Netupitant is described as an NK1 receptor antagonist, and its efficacy in chemotherapy-induced nausea and vomiting is established.

Nephrogenic syndrome of inappropriate antidiuresis is caused by gain-of-function variants in the vasopressin V2 receptor gene (*AVPR2*). NK1 antagonism does not act on this pathway, so **no mechanistic link is known**. The high graph score is not supported by any identifiable biology.

### Other Predicted Indications (for context)

All ten predictions are L5 with a Hold recommendation, and none has clinical trial support.

- **Migraine (ranks 3, 4 and 6):** These are the only biologically plausible candidates, through substance P/NK1 signaling in the trigeminovascular system. However, earlier NK1 antagonists reportedly showed no efficacy in acute migraine trials. The 20 papers retrieved for the rank-4 migraine-susceptibility term concern epilepsy and migraine genetics, and none studies netupitant or NK1 antagonism.
- **Pulmonary hypertension and coronary artery disease:** The links are weak and speculative. Netupitant's CYP3A4 inhibition also raises interaction concerns with common cardiopulmonary drugs.
- **Leprosy, kyphoscoliotic heart disease, hyperargininemia and hypertrichosis:** No plausible mechanism was identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15031P | AKYNZEO CAPSULES 300MG/0.5MG | Capsule, gelatin coated (oral) | Not provided in the source data |

## Safety Considerations

Please refer to the package insert for safety information.

- **Drug Interactions:** No interaction records were found in the queried database. The evidence pack notes that netupitant is a CYP3A4 inhibitor, which is relevant to co-medications such as statins, antiplatelet agents and cardiopulmonary drugs.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials or drug-specific publications, and no plausible link between NK1 antagonism and *AVPR2* gain-of-function disease. Of the ten predictions, only migraine has a credible hypothesis, and it is weakened by the failure of earlier NK1 antagonists.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (currently blocking the safety screening step)
- Detailed mechanism of action data, for example from DrugBank
- Netupitant-specific preclinical or clinical evidence for any candidate indication, with migraine as the most plausible one to examine first
- Review of the CYP3A4 interaction profile against the drugs commonly used in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

