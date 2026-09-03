---
layout: default
title: Velaglucerase Alfa
parent: 僅模型預測 (L5)
nav_order: 1049
evidence_level: L5
indication_count: 10
---

# Velaglucerase Alfa
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

# Velaglucerase Alfa: From Gaucher Disease to Steel Syndrome

## One-Sentence Summary

Velaglucerase alfa is a recombinant glucocerebrosidase enzyme replacement therapy, originally used to treat **Gaucher disease (type 1)**.
The TxGNN model's top-ranked prediction is **Steel syndrome**, but **this evidence pack itself states there is no known biological link** between the two conditions, and there are currently **0 clinical trials** and **0 publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (type 1) — enzyme replacement therapy target; not confirmed via Singapore label text (drug is unregistered) |
| Predicted New Indication | Steel syndrome |
| TxGNN Prediction Score | 96.99% |
| Evidence Level | L5 (model prediction only, no clinical/literature support) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is unresolved). Based on known pharmacology, velaglucerase alfa is a recombinant human glucocerebrosidase that replaces the deficient enzyme in Gaucher disease, a lysosomal storage disorder caused by GBA gene mutations.

The top-ranked predicted indication, **Steel syndrome**, is a skeletal dysplasia (spine-pelvis-femur anomaly) caused by **COL27A1** gene mutations — a collagen structural defect with no known involvement of the glucocerebrosidase/lysosomal storage pathway. The evidence pack's own mechanistic annotation explicitly states: *"no known biological link"* between the two conditions, and characterizes this as a purely data-driven prediction with no mechanistic plausibility.

It is worth noting that several **lower-ranked** candidates in this pack (e.g., rank 5 Wolman disease, rank 7 cholesteryl ester storage disease) at least share a *lysosomal storage disorder* category with Gaucher disease, even though they act via a different enzyme (LIPA, not GBA). By contrast, the rank-1 candidate (Steel syndrome) has the **weakest** biological rationale among all 10 predictions returned, despite having the highest raw score — suggesting the ranking here should not be read as a proxy for clinical plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Velaglucerase alfa is **not currently marketed** in Singapore (0 registrations, no license records available). No approved indication text, product name, or dosage form data exists in the regulatory registry to report.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/HSA label warnings and contraindications data could not be retrieved for this drug (flagged as a **Blocking** data gap — see Conclusion), so a formal safety pre-screen (S1 stage) cannot currently be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication (Steel syndrome) has no clinical trials, no literature, and — per the evidence pack's own mechanistic analysis — no known biological pathway connecting it to velaglucerase alfa's mode of action. Combined with a Blocking-severity data gap on drug label warnings/contraindications, this candidate cannot proceed past the S0 (hypothesis) stage.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) — currently blocking any safety pre-screen
- Confirmed mechanism of action (MOA) from DrugBank or primary literature
- Re-evaluation of whether the rank-1 candidate (Steel syndrome) should be deprioritized in favor of candidates with at least categorical mechanistic overlap (e.g., other lysosomal storage disorders), pending any future clinical/literature evidence
- If pursuing further, prioritize generating at least preclinical/mechanistic evidence before advancing any of the 10 listed candidates beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

