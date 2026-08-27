---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 639
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From NSAID Indications (Osteoarthritis/Rheumatoid Arthritis) to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

> Meloxicam is an oxicam-class, COX-2-preferential NSAID generally used to relieve inflammation and pain in conditions such as osteoarthritis and rheumatoid arthritis (Singapore-specific approved indication text is not available in this evidence pack).
> Of 10 TxGNN-predicted indications reviewed for this candidate, most scored highest by raw model confidence but were flagged as biologically implausible knowledge-graph artifacts; the most credible signal is **Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis (JIA)**,
> supported by **1 publication** (a safety cohort study) and a mechanistically direct rationale, though **no dedicated clinical trials** currently exist for this exact subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (Meloxicam is generally classified as an NSAID for osteoarthritis/rheumatoid arthritis) |
| Predicted New Indication | Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (DrugBank query succeeded but did not return a structured MOA field). Based on known pharmacological classification, Meloxicam is an oxicam-class NSAID that preferentially inhibits COX-2, reducing prostaglandin-mediated inflammation and pain; this class of drug is already an established, guideline-referenced option for symptomatic control of inflammatory joint disease, including juvenile idiopathic arthritis (JIA) in several jurisdictions.

Juvenile idiopathic arthritis — including the rheumatoid-factor-positive polyarticular subtype — is an inflammatory joint disease driven by the same COX-mediated pathways that Meloxicam already targets in adult osteoarthritis and rheumatoid arthritis. The mechanistic link is therefore direct rather than speculative: this is a within-class extension (NSAID → inflammatory arthritis) rather than a repurposing into an unrelated disease area.

It is important to note that this candidate was selected after screening TxGNN's full top-10 output for this drug. Six of the ten predicted indications (ranks 1–4, 9, 10 — e.g., acromesomelic dysplasia, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, WHIM syndrome) are rare structural, genetic, or developmental disorders with **no known inflammatory pathology** and were explicitly annotated in the evidence pack as likely knowledge-graph embedding artifacts, with zero supporting trials or literature and a "Hold" recommendation. Rheumatoid factor-positive polyarticular JIA (rank 8) is the only candidate in this set that reached decision stage S2 with a "Proceed with Guardrails" recommendation and actual literature support, making it the most defensible candidate to advance for further evaluation despite ranking below several implausible high-score predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Cohort (Phase 4 registry) | Pediatric Rheumatology Online Journal | Long-term safety and developmental outcomes in JIA patients treated with celecoxib or nonselective NSAIDs in routine clinical practice; this is a safety-focused registry study, not an efficacy trial specific to this JIA subtype |

---

## Singapore Market Information

Meloxicam is currently **not marketed** in Singapore under this evidence pack (0 registrations found). No license/authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong — Meloxicam's COX-2-mediated anti-inflammatory action directly matches the inflammatory joint pathology of polyarticular JIA — but the only supporting literature is a safety/registry cohort study rather than a subtype-specific efficacy trial, and the drug is not currently marketed in Singapore, so both clinical and regulatory gaps must be closed before advancing further.

**To proceed, the following is needed:**
- Regulatory package insert (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Detailed mechanism-of-action data from DrugBank or equivalent source — currently a **High** severity data gap (DG002)
- Efficacy-specific studies or trials of Meloxicam in rheumatoid factor-positive polyarticular JIA (current evidence is safety-only, in a related but non-identical NSAID population)
- Drug-drug interaction data (current DDI query returned no results)
- Confirmation of Singapore market registration pathway, since the drug currently has zero local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

