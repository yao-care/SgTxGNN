---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 1071
evidence_level: L5
indication_count: 10
---

# Zanamivir
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

> Zanamivir is a neuraminidase inhibitor originally developed for treating influenza virus infection.
> The TxGNN model predicts it may be effective for **Pyelonephritis**,
> but currently there are **0 clinical trials** and **0 publications** supporting this specific direction,
> and the evidence pack itself flags this link as a likely artifact of knowledge-graph embedding similarity rather than a real biological connection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (viral) infection — not present in local registry data; based on known drug class (neuraminidase inhibitor) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured registry (flagged as Data Gap DG002). Based on annotations embedded elsewhere in this evidence pack, Zanamivir is a neuraminidase (NA) inhibitor developed for influenza A/B virus infection, with efficacy established through head-to-head trials against oseltamivir in hospitalized patients.

Pyelonephritis, however, is predominantly a bacterial upper urinary tract infection (commonly caused by *E. coli* and other Gram-negative uropathogens). Its pathophysiology does not involve viral neuraminidase, and no shared drug target, pathway, or clinical mechanism links it to Zanamivir's known pharmacology.

The evidence pack's own repurposing rationale is explicit on this point: it states there is "no pharmacological mechanism overlap" and attributes the prediction to "indirect KG embedding similarity, not a real biological connection." No clinical trials or literature were retrieved for this specific indication. **This prediction should be treated as a low-confidence model artifact rather than a mechanistically grounded repurposing hypothesis.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Zanamivir currently has no marketing authorizations on record (`total_licenses: 0`, `market_status: 未上市`). No registration data is available to populate a licenses table.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA label warnings and contraindications are recorded as a **Blocking** data gap (DG001) — this must be resolved before any safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (pyelonephritis) has no supporting clinical trials or literature, no plausible mechanistic link, and the evidence pack explicitly characterizes the association as a likely false-positive from embedding-based similarity. Evidence level is L5 (model prediction only), and a Blocking safety data gap (TFDA/HSA label warnings and contraindications) remains unresolved.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for Zanamivir (DG002)
- TFDA/HSA product label — warnings, contraindications, DDI data (DG001, Blocking)
- Any preclinical or mechanistic evidence linking neuraminidase inhibition to bacterial pyelonephritis pathophysiology (none currently identified)
- Re-evaluation of lower-ranked candidates in this pack, several of which (e.g., HIV susceptibility, rank 7) show higher nominal evidence levels (L4) but are also flagged as likely drug/trial mismatches and require manual verification before consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

