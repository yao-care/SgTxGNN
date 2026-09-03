---
layout: default
title: Netupitant
parent: 僅模型預測 (L5)
nav_order: 701
evidence_level: L5
indication_count: 10
---

# Netupitant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Netupitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Netupitant is an NK1 receptor antagonist, best known as a component of the NEPA combination (netupitant/palonosetron) used to prevent chemotherapy-induced nausea and vomiting. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis**, but this prediction currently has **no supporting clinical trials or published literature** — it is a model-only hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced nausea and vomiting (CINV), based on general pharmacological knowledge of the NEPA combination — not recorded in this evidence pack |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 98.35% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for netupitant is not populated in this evidence pack (`original_moa` is a data gap). Based on general pharmacological knowledge, netupitant is an NK1 (neurokinin-1) receptor antagonist that blocks substance P signaling, and is used in combination with palonosetron for CINV prophylaxis.

Nephrogenic syndrome of inappropriate antidiuresis is a disorder of vasopressin (antidiuretic hormone) receptor signaling. There is no established pharmacological pathway linking NK1 receptor blockade to antidiuretic hormone receptor activity. The evidence pack's own mechanistic assessment for this candidate states the link is weak: *"no known direct association between NK1 receptor antagonism and antidiuretic hormone receptor signaling; the mechanistic connection is tenuous and this is a TxGNN prediction only, with no clinical or literature evidence."*

In short, this candidate ranks highly on the TxGNN score alone, but has no mechanistic, preclinical, or clinical corroboration at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this evidence pack flags a Blocking data gap — TFDA/regulatory label warnings and contraindications for netupitant have not yet been retrieved, which prevents any safety pre-screening (S1 stage) for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (nephrogenic syndrome of inappropriate antidiuresis) has Evidence Level L5 — a TxGNN score with zero supporting clinical trials or literature, and the mechanistic rationale is explicitly assessed as weak. The drug is also not currently marketed in Singapore, so there is no local regulatory or safety baseline to build on.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications for netupitant (currently a Blocking data gap)
- Confirmed mechanism-of-action documentation (currently a High-severity data gap)
- Preclinical or mechanistic studies directly testing NK1 antagonism in antidiuretic hormone/vasopressin-receptor-mediated conditions before any clinical evaluation is warranted
- Note: rank 4 ("migraine with or without aura, susceptibility to") returned 20 PubMed hits, but on review these are epilepsy-genetics papers largely tangential to netupitant or migraine specifically — this candidate would need a targeted literature re-query before being considered a stronger alternative lead.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

