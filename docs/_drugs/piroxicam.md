---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 792
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From Osteoarthritis/Rheumatoid Arthritis to Juvenile Idiopathic Arthritis

## One-Sentence Summary

> Piroxicam is a classic oxicam-class NSAID, historically used for osteoarthritis, rheumatoid arthritis, and related inflammatory joint conditions (specific Singapore licensing data not available in this dataset).
> After reviewing all 10 TxGNN-predicted indications, the only candidate supported by actual clinical evidence is **Juvenile Idiopathic Arthritis (JIA)** —
> the model's top-ranked predictions by raw score (rare skeletal dysplasia syndromes) show **zero clinical trials, zero literature, and no plausible mechanistic link**, and are explicitly flagged as likely knowledge-graph noise. JIA, by contrast, is backed by **1 RCT, 1 comparative clinical study, and 2 systematic reviews/meta-analyses** among 13 retrieved publications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Singapore license records). Piroxicam is generally known as an oxicam-class NSAID for osteoarthritis/rheumatoid arthritis. |
| Predicted New Indication | Juvenile Idiopathic Arthritis (selected over the nominal rank-1 prediction — see rationale below) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, Piroxicam is a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin synthesis, producing anti-inflammatory and analgesic effects. This mechanism is directly relevant to the synovial inflammation seen in Juvenile Idiopathic Arthritis (JIA), which is pathophysiologically similar to adult rheumatoid arthritis — a condition NSAIDs, including piroxicam, have long been used to treat.

**Important note on TxGNN ranking vs. evidence quality:** The 10 predictions in this evidence pack are ordered by raw TxGNN model score, not by evidence strength. Ranks 1–8 (rare skeletal dysplasia syndromes, WHIM syndrome, etc.) score higher numerically (99.99%) but have **no clinical trials, no literature, and no plausible biological connection** to piroxicam's COX-inhibition mechanism — the evidence pack itself labels these as probable rare-node graph noise. Rank 9 (rheumatoid nodulosis) has only one indirect case report about a different drug (methotrexate). Rank 10 (JIA, score 99.93%) is the only candidate where the mechanistic rationale, clinical trial history, and literature all converge, including a piroxicam-specific multicentre RCT and PK study in children. For this reason, JIA — not the numerically top-ranked candidate — is presented as the actionable finding in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | RCT | British Journal of Rheumatology | Multicentre double-blind crossover trial comparing piroxicam vs. naproxen in 47 children with juvenile chronic arthritis; no significant efficacy difference between the two NSAIDs. |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Clinical Study | European Journal of Rheumatology and Inflammation | Randomized comparison of piroxicam vs. naproxen in 26 children with juvenile rheumatoid arthritis; significant reduction in painful/swollen joints. |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Systematic Review / Network Meta-analysis | World Journal of Clinical Cases | Compared efficacy of various NSAIDs (including piroxicam) for JIA; optimal agent/regimen still undetermined. |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Systematic Review / Network Meta-analysis | Indian Pediatrics | Compared efficacy and safety of nine NSAIDs in JIA patients. |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Pharmacokinetic Study | European Journal of Clinical Pharmacology | Steady-state PK of piroxicam (0.4 mg/kg once daily) in 10 children with rheumatic disease; Cmax and half-life characterized. |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Review (Safety/Toxicity) | Clinical Rheumatology | Long-term toxicity review of antirheumatic/anti-inflammatory drugs, including NSAIDs, in a pediatric rheumatology cohort. |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Cohort/Observational | International Ophthalmology | Frequency of chronic iridocyclitis (ocular complication) in ANA-positive pauciarticular JCA; relevant to comorbidity management during NSAID therapy. |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderärztliche Praxis | Overview of pharmacologic therapy for juvenile chronic arthritis, discussing piroxicam and sulfasalazine. |
| [6753142](https://pubmed.ncbi.nlm.nih.gov/6753142/) | 1982 | Review | Schweizerische Medizinische Wochenschrift | Comparative review of newer NSAIDs' efficacy/tolerability, proposing rational prescribing approach in rheumatoid/osteoarthritic disease. |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review (Drug Delivery) | Critical Reviews in Therapeutic Drug Carrier Systems | Reviews microencapsulation drug-delivery systems for NSAIDs across arthritis types including JIA. |

---

## Singapore Market Information

This drug is currently **not marketed** in Singapore, and no authorization/license records are available in this dataset (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack — TFDA/HSA label data retrieval is a **Blocking** gap per `DG001`.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A piroxicam-specific multicentre RCT and a comparative clinical study in juvenile chronic/rheumatoid arthritis, supported by two independent systematic reviews of NSAIDs in JIA, provide L2-level evidence for pediatric use. However, the drug is not currently marketed in Singapore, and critical safety/label data are missing, so this cannot proceed without further data.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (Blocking gap, `DG001`)
- Confirmed mechanism of action data from DrugBank (`DG002`)
- Pediatric-specific safety monitoring plan (GI and renal risk, given long half-life of piroxicam in children)
- Singapore market entry/registration pathway assessment, since the product is currently unregistered
- Update `similarity_to_original` and `route_compatibility` fields (currently "pending") once original indication and dosage form data are confirmed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

