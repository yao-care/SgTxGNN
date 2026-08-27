---
layout: default
title: Lemborexant
parent: 僅模型預測 (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
---

# Lemborexant
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

# Lemborexant: From Unmarketed in Singapore to Insomnia Disorder (Sleep Onset & Maintenance)

## One-Sentence Summary

> Lemborexant is a dual orexin receptor antagonist (DORA) that is **not currently registered or marketed in Singapore**.
> The TxGNN model's top-ranked prediction is **Insomnia Disorder (Sleep Disorder, Initiating and Maintaining Sleep)** —
> which is in fact the drug's already-established global indication (approved in the US, Japan, and Canada) rather than a novel repurposing hypothesis —
> supported by **1 directly related clinical trial** and **20 publications**, including two completed Phase 3 RCTs (SUNRISE 1 and SUNRISE 2).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established locally — Lemborexant is not yet registered in Singapore; no local original indication is on file |
| Predicted New Indication | Insomnia Disorder (Sleep Disorder, Initiating and Maintaining Sleep) |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed drug-level mechanism-of-action data is not yet on file for this product record. However, the evidence pack's mechanistic analysis confirms Lemborexant is a **dual orexin receptor antagonist (DORA)**, acting as a competitive antagonist at both OX1R and OX2R (with greater affinity for OX2R). By blocking orexin/hypocretin signalling, it reduces wake drive and promotes both sleep onset and sleep maintenance — this is its core, well-characterized pharmacological mechanism.

Unlike typical repurposing candidates, this prediction does not link two distinct diseases through an indirect mechanistic bridge. Insomnia is Lemborexant's **primary, already-approved indication overseas** (marketed as Dayvigo in the US, Japan, and Canada since 2019–2020). The TxGNN model has essentially re-identified the drug's core indication from the knowledge graph, which is expected given the direct pharmacological fit between orexin antagonism and difficulty initiating/maintaining sleep.

In the Singapore context, therefore, "Proceed with Guardrails" does not imply a need for additional repurposing-style clinical validation. Instead, it reflects that this is a **standard new drug registration pathway** — the priority is submitting a complete local dossier (including HSA-specific labelling, warnings, and DDI data) rather than generating new efficacy evidence, since the efficacy evidence base from other jurisdictions is already substantial (L1).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06928766](https://clinicaltrials.gov/study/NCT06928766) | Phase 2 | Not Yet Recruiting | 15 | Double-blind, placebo-controlled RCT of eszopiclone vs. lemborexant in people with obstructive sleep apnoea (OSA) and a low arousal threshold who have difficulty maintaining or falling asleep (COMISA population); addresses a challenging-to-treat overlap syndrome. |

*Note: This table reflects trials mapped to the top predicted indication only. Lemborexant also has additional Phase 3 pivotal trials (SUNRISE 1/2) captured in the literature evidence below rather than the clinical trials evidence field.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Network Open | Pivotal trial (SUNRISE 1) comparing lemborexant with placebo and zolpidem ER in older adults with insomnia disorder; established efficacy and safety in this population. |
| [32585700](https://pubmed.ncbi.nlm.nih.gov/32585700/) | 2020 | RCT (Phase 3, long-term) | Sleep | SUNRISE 2: long-term (12-month) efficacy and tolerability of lemborexant vs. placebo in adults with insomnia disorder. |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | Review (systematic review + NMA) | Translational Psychiatry | Comparative efficacy and safety of the three approved DORAs (daridorexant, lemborexant, suvorexant) for insomnia. |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Review (network meta-analysis) | Lancet | Large-scale network meta-analysis of pharmacological treatments for acute and long-term insomnia management in adults. |
| [36701954](https://pubmed.ncbi.nlm.nih.gov/36701954/) | 2023 | Review (systematic review + NMA) | Sleep Medicine Reviews | Systematic review and network meta-analysis ranking 20 insomnia medications by efficacy and tolerability. |
| [33636648](https://pubmed.ncbi.nlm.nih.gov/33636648/) | 2021 | Cohort (post-marketing) | Sleep Medicine | Long-term (up to 12 months) real-world effectiveness and safety outcomes for lemborexant from Study 303 (SUNRISE-2 extension). |
| [32096020](https://pubmed.ncbi.nlm.nih.gov/32096020/) | 2020 | Review (drug profile) | Drugs | "Lemborexant: First Approval" — summarizes the regulatory approval basis, pharmacology, and clinical development programme for insomnia. |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | Post-hoc analysis | Sleep Medicine | Effect of lemborexant on sleep architecture in patients with insomnia disorder and comorbid mild obstructive sleep apnea (COMISA). |
| [37796657](https://pubmed.ncbi.nlm.nih.gov/37796657/) | 2023 | Comparative analysis | Journal of Clinical Psychiatry | Indirect comparison of lemborexant vs. daridorexant using number needed to treat (NNT), number needed to harm (NNH), and likelihood to help/harm. |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Review (network meta-analysis) | Journal of Managed Care & Specialty Pharmacy | Network meta-analysis comparing lemborexant's efficacy and safety against other insomnia treatments. |

---

## Singapore Market Information

Lemborexant currently holds **no market authorization in Singapore** — the drug is not registered, and there are no licensed products, dosage forms, or approved indication texts on file (total registrations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. No local (HSA) warnings, contraindications, or drug-drug interaction data are currently available in the evidence pack for this record.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Overseas clinical evidence for insomnia is strong (Evidence Level L1, supported by two completed Phase 3 RCTs — SUNRISE 1 and SUNRISE 2 — plus multiple systematic reviews/network meta-analyses), and Lemborexant is already approved for this indication in the US, Japan, and Canada. However, the product has zero registrations in Singapore, and local safety/regulatory data (HSA label, contraindications, DDI profile) are entirely missing, so market entry should proceed through the standard registration pathway with careful safety documentation rather than being treated as a validated local indication.

**To proceed, the following is needed:**
- HSA-specific package insert with warnings and contraindications (currently a Blocking data gap — DG001)
- Verified mechanism-of-action and drug interaction data via DrugBank API (High-severity data gap — DG002)
- Local drug-drug interaction (DDI) database query, currently returning "not found"
- A Singapore registration dossier plan, given the current total of 0 local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

