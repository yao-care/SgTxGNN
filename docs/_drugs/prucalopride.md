---
layout: default
title: Prucalopride
parent: Low Evidence (L5)
nav_order: 831
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride: From Gastrointestinal Motility Disorders to Hypoalphalipoproteinemia

## One-Sentence Summary

Prucalopride is a selective 5-HT4 receptor agonist with gastrointestinal prokinetic activity, and it is marketed in Singapore as Resolor tablets.
The TxGNN model ranks **hypoalphalipoproteinemia** (low HDL cholesterol) as its top prediction, but **no clinical trials and no publications** support it, and no biological link is known.
Of the 10 predicted indications, only the amyloidosis-related ones have any literature, and that literature is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (approved-indication text is empty); pharmacologically a GI prokinetic |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Prucalopride is known as a selective 5-HT4 receptor agonist that stimulates gastrointestinal motility.

For hypoalphalipoproteinemia, **no plausible link was identified**. Prucalopride has no known role in HDL metabolism. The high score (0.998) is a graph-based prediction only, with no trial or literature support.

The same applies to the next four predictions. There is no known connection to LDL receptor function in homozygous familial hypercholesterolemia. There is no effect on acid secretion or mucosal defence in duodenal ulcer. There is no antifungal mechanism in oral candidiasis. And there is no link to lipid metabolism in the familial combined hyperlipidemia entry, which is flagged **obsolete** in the ontology and may map to a deprecated node.

The only candidates with a partial rationale are the amyloidosis-related ones (amyloidosis, primary amyloidosis, acquired amyloid peripheral neuropathy). Amyloid infiltration of the gut wall or autonomic nerves can cause intestinal dysmotility or pseudo-obstruction, and a prokinetic might relieve those symptoms. This would be symptom management only and would not modify the underlying amyloid disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for hypoalphalipoproteinemia or any of the other 9 predicted indications).

---

## Literature Evidence

Currently no related literature available for hypoalphalipoproteinemia.

Two papers were retrieved for the amyloidosis-related predictions. Neither tests prucalopride:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Cohort | Turk J Gastroenterol | Specific GI motility disorders (gastroparesis, chronic intestinal pseudo-obstruction, colonic inertia) are often misdiagnosed as functional GI disorders by community physicians. This is a diagnostic study, not a prucalopride treatment study. |
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Case report | Cureus | A 61-year-old man with amyloidosis presenting as chronic intestinal pseudo-obstruction. It shows amyloidosis as a cause of dysmotility, not prucalopride efficacy. |

---

## Other Predicted Indications (Ranks 2–10)

| Rank | Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Homozygous familial hypercholesterolemia | 99.67% | L5 | Hold |
| 3 | Duodenal ulcer | 99.65% | L5 | Hold |
| 4 | Oral candidiasis | 99.64% | L5 | Hold |
| 5 | Familial combined hyperlipidemia (obsolete term) | 99.62% | L5 | Hold |
| 6 | Amyloidosis | 99.62% | L4 | Research Question |
| 7 | Strongyloidiasis | 99.60% | L5 | Hold |
| 8 | HIV infectious disease | 99.60% | L5 | Hold |
| 9 | Primary amyloidosis | 99.56% | L4 | Research Question |
| 10 | Acquired amyloid peripheral neuropathy | 99.55% | L5 | Hold |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14103P | Resolor Film-coated Tablet 1 mg | Tablet, film coated | Not listed in registration record |
| SIN14104P | Resolor Film-coated Tablet 2 mg | Tablet, film coated | Not listed in registration record |

Both products are manufactured by Janssen Cilag S.p.A. and are oral formulations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hypoalphalipoproteinemia) has no clinical trials, no literature, and no plausible mechanism. The amyloidosis-related candidates have an indirect, symptom-level rationale only, and their retrieved papers do not test prucalopride. Nothing here currently justifies moving forward.

**To proceed, the following is needed:**
- HSA package insert (warnings, contraindications, approved indication), which is required before any safety screening
- Mechanism of action data from DrugBank
- Reconciliation of the obsolete familial combined hyperlipidemia term with its current ontology node
- For the amyloidosis-related candidates, a targeted search for prucalopride use in amyloid-associated GI dysmotility, framed as symptom management rather than disease modification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

