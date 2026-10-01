---
layout: default
title: Lanreotide
parent: Low Evidence (L5)
nav_order: 571
evidence_level: L5
indication_count: 10
---

# Lanreotide
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

# Lanreotide: From a Somatostatin Analogue to Hypertrichosis

## One-Sentence Summary

Lanreotide is a somatostatin analogue marketed in Singapore as an injectable prolonged-release product.
The TxGNN model predicts it may be effective for **Hypertrichosis**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Lanreotide is a somatostatin analogue that acts as an SSTR2/SSTR5 agonist. The registered indication text is also missing from the supplied data, so the original-to-new indication relationship cannot be assessed.

The supplied data does not support a plausible route from somatostatin receptor signalling to hair-growth disorders. The very high TxGNN score (99.97%) reflects graph proximity only. Related hair-disorder nodes (e.g., Ambras-type hypertrichosis and genetic hair shaft abnormalities) also score highly, which suggests the score may be inflated by that clustering. Until a biological rationale or direct evidence is found, this prediction should be treated as a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14289P | Somatuline Autogel Prolonged Release Solution for Injection in a Pre-filled Syringe 120 mg | Injection, solution |
| SIN14291P | Somatuline Autogel Prolonged Release Solution for Injection in a Pre-filled Syringe 60 mg | Injection, solution |
| SIN14290P | Somatuline Autogel Prolonged Release Solution for Injection in a Pre-filled Syringe 90 mg | Injection, solution |

The manufacturer is Ipsen Pharma Biotech.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials, no literature and no supported mechanism. Evidence is L5, and the safety and mechanism data gaps are unresolved.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A targeted literature and trial search linking somatostatin analogues to hypertrichosis; without any such signal, deprioritise this indication

**Note on other candidates:** Among the other predictions for this drug, *polycystic kidney disease 3 with or without polycystic liver disease* (rank 8, score 98.84%) is the most biologically plausible. Somatostatin analogues lower cAMP via SSTR2 in cholangiocytes and renal tubular cells. One lanreotide-specific review (PMID 26126910) and several guidelines and reviews were retrieved, but no lanreotide trial. It is graded L4, "Research Question", and would be a better next investigation than hypertrichosis. All results are for research reference only and require clinical validation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

