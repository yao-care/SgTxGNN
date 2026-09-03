---
layout: default
title: Prucalopride
parent: 僅模型預測 (L5)
nav_order: 831
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride: From Chronic Constipation (Class Use) to Amyloidosis-Related GI Motility Disorder

## One-Sentence Summary

> Prucalopride is a selective 5-HT4 receptor agonist used clinically to enhance colonic motility in chronic constipation (per evidence pack rationale notes; no structured original-indication or MOA record is available in this pack).
> Among 10 TxGNN-predicted indications, the top-ranked candidate (hypoalphalipoproteinemia, 99.82%) is explicitly flagged in the evidence pack as likely model noise with no mechanistic plausibility.
> The most defensible candidate is **Amyloidosis-related GI motility disorder**, supported by **2 case/cohort publications** describing amyloid-induced enteric neuromuscular dysfunction, though no clinical trial has directly tested prucalopride in this population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore license or `original_indications` record exists; class use (chronic constipation) is inferred only from rationale text, not a structured field |
| Predicted New Indication | Amyloidosis (GI motility disorder / chronic intestinal pseudo-obstruction) |
| TxGNN Prediction Score | 99.62% (rank 6 of candidate list; related entry "primary amyloidosis" at 99.56%, rank 9) |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Note on selection:** The single highest-scoring TxGNN prediction (hypoalphalipoproteinemia, 99.82%) was **not** used as the headline candidate. Its own `repurposing_rationale` states there is no known mechanistic or clinical link and explicitly labels it as likely prediction noise. The amyloidosis-related candidates are the only ones in this pack that reach L4 evidence (literature-supported) and an S1 decision stage ("Research Question"); all other 8 candidates remain L5/S0/Hold with no supporting evidence.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field (flagged as a High-severity data gap, DG002). Based on the mechanistic notes accompanying the predictions, prucalopride is described as a selective 5-HT4 receptor agonist that promotes colonic motility, a mechanism established for chronic constipation.

Amyloid protein deposition can infiltrate the intestinal smooth muscle layer and enteric nervous plexus, producing gastrointestinal motility failure that can progress to chronic intestinal pseudo-obstruction (CIPO). This creates a theoretical overlap with prucalopride's known pharmacology (correcting insufficient gut motility), since both the disease mechanism and the drug's action converge on enteric neuromuscular function.

However, this is an **indirect mechanistic inference, not direct treatment evidence**. The supporting literature only characterizes how amyloidosis produces GI dysmotility (and how it is frequently misdiagnosed as a functional GI disorder); none of the retrieved publications evaluate prucalopride's efficacy or safety in amyloidosis patients. No clinical trials (registered or ICTRP) currently exist for this drug-disease pair.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Cohort | Turkish J Gastroenterol | Specific GI motility disorders (gastroparesis, CIPO, colonic inertia) are commonly under-recognized in Asia and misdiagnosed as functional GI disorders by community physicians |
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Case Report | Cureus | 61-year-old man with recurrent dilated small bowel and multiple non-diagnostic laparotomies, ultimately attributed to amyloidosis presenting as chronic intestinal pseudo-obstruction |

---

## Singapore Market Information

Prucalopride currently has no marketing license record in this dataset — `taiwan_regulatory.licenses` is empty and market status is "Not Marketed."

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data are all unavailable in the current evidence pack. This is flagged as a **Blocking** data gap — DG001, TFDA/HSA label warnings and contraindications — and must be resolved before any S1 safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Even the best-supported candidate (amyloidosis-related GI motility disorder) rests only on indirect case/cohort literature describing disease mechanism, with no direct clinical evidence for prucalopride in this population, no registered trials, and a Blocking-severity gap in label safety data. The drug is also unregistered in the Singapore market, and the top TxGNN-scored candidate for this drug is independently assessed as likely noise.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/HSA label warnings and contraindications before any safety evaluation
- Resolve DG002: confirm mechanism of action via DrugBank API query
- Generate or identify direct clinical evidence (retrospective cohort or trial) evaluating prucalopride specifically in amyloidosis-associated GI dysmotility / CIPO
- Confirm Singapore/regional regulatory pathway status, since the drug currently holds zero local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

