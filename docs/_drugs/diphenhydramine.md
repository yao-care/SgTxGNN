---
layout: default
title: Diphenhydramine
parent: Low Evidence (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Diphenhydramine
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

# Diphenhydramine: From Allergic Conditions to Rosacea Conjunctivitis

## One-Sentence Summary

Diphenhydramine is a first-generation antihistamine, primarily used for allergic reactions such as urticaria and allergic rhinitis.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis** with a very high score, but **0 clinical trials** and **0 publications** currently support this direction.
This prediction is best treated as a low-confidence, model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic conditions (urticaria, allergic rhinitis); the Singapore registrations list no indication text |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, diphenhydramine is an H1 receptor antagonist. Its efficacy in allergic conditions is well established, and blocking histamine-mediated ocular itching could mechanistically be applicable to some eye conditions.

The link to rosacea conjunctivitis is weak, though. Rosacea-associated eye disease is mainly driven by meibomian gland dysfunction and inflammation, not by histamine. The very high score (0.992) is therefore likely a knowledge-graph proximity artifact, meaning the drug and disease sit close together in the graph without a real therapeutic connection. No trials or literature were retrieved to test this.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Showing 5 of 14 registrations:

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN00362P | BENOCTEN TABLET 50 mg | Tablet |
| SIN10851P | PAXIDORM TABLETS 25 mg | Tablet, sugar coated |
| SIN02839P | BEANAMINE EXPECTORANT | Solution |
| SIN08782P | DIPHEN 5 EXPECTORANT | Syrup |
| SIN08799P | DIPHEN 10 EXPECTORANT | Syrup |

## Safety Considerations

No package insert warnings, contraindications, or drug interaction records were available. Please refer to the package insert for safety information.

For context, the literature retrieved for other candidate indications describes the following class-level concerns:
- **Central nervous system effects**: First-generation antihistamines such as diphenhydramine cause sedation, cognitive impairment and impaired driving performance. A CSACI position statement (2019) recommends second-generation agents as first line.
- **Anticholinergic effects**: These include dry mouth, dizziness and orthostatic hypotension. Caution is warranted in older adults and with other anticholinergic or CNS-depressant drugs.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and the mechanistic link is weak because rosacea eye disease is not primarily histamine-driven. Diphenhydramine's known sedation and anticholinergic burden add to the case against pursuing this indication.

**To proceed, the following is needed:**
- A literature and mechanism review showing a histamine-driven component in rosacea conjunctivitis
- Any clinical or preclinical evidence of diphenhydramine in ocular rosacea
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the HSA
- Route compatibility assessment, since the Singapore products are oral only and an ocular use would need a different route

**Note on other predicted indications:**
- Rank 2, **rhinitis**, is the best supported candidate. It has one completed Phase 4 randomized trial (NCT00648973, n=1021) and a randomized trial publication (PMID 16680933). This is probably an existing use rather than new repurposing, and the Evidence Pack recommends Proceed with Guardrails.
- Rank 3, **allergic urticaria**, is the next best. It rests on small comparator trials and is also rated Proceed with Guardrails.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

