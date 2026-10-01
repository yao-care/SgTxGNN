---
layout: default
title: Avibactam
parent: Low Evidence (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Avibactam
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

# Avibactam: From Beta-Lactamase Inhibitor Partner (Ceftazidime-Avibactam) to Streptococcal Pneumonia

## One-Sentence Summary

Avibactam is a beta-lactamase inhibitor marketed in Singapore only as part of the ceftazidime-avibactam combination (Zavicefta) and has no antibacterial activity of its own.
The TxGNN model predicts it may be effective for **streptococcal pneumonia** with a very high score (99.70%), but **0 clinical trials** and **0 publications** support this prediction.
The high score is most likely a knowledge-graph artifact, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied registration data (marketed as the ceftazidime-avibactam combination) |
| Predicted New Indication | Streptococcal pneumonia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Avibactam is known to inhibit serine beta-lactamases. It is used to protect a partner beta-lactam (ceftazidime) from enzymatic breakdown, and it has no intrinsic antibacterial activity.

This mechanism fits the prediction poorly. Pneumococcal (*Streptococcus pneumoniae*) resistance to beta-lactams is mainly mediated by altered penicillin-binding proteins (PBPs), not by beta-lactamase production. A beta-lactamase inhibitor therefore has little to add against this pathogen.

The high TxGNN score most likely reflects the drug's network proximity to other antibacterial agents in the knowledge graph, not a real therapeutic link. No trial or publication was found to counter this interpretation.

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
| SIN15870P | ZAVICEFTA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 2G/0.5G | Injection, powder, for solution |

Only injectable forms are registered. No approved indication text was supplied.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by the model score alone, with no trials or literature. The known mechanism (serine beta-lactamase inhibition, no intrinsic antibacterial activity) does not fit a pneumococcal target, where resistance is mainly PBP-mediated. The other top-10 predictions (for example influenza susceptibility, urinary schistosomiasis, hyperamylasemia and squamous cell lung carcinoma) also lack a plausible mechanism. For *Staphylococcus aureus* infection (rank 7), the available records are only indirect. The anti-staphylococcal activity in the one relevant in vitro study comes from ceftaroline, not avibactam.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any in vitro or clinical evidence that avibactam adds value in pneumococcal infection; without it, this prediction should not advance beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

