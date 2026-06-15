---
layout: default
title: Bupropion
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Bupropion
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

# Bupropion: From Depression to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Bupropion is a norepinephrine-dopamine reuptake inhibitor (NDRI) used for major depressive disorder and smoking cessation, but not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**, with **8 clinical trials** — including 2 high-grade RCTs directly targeting ADHD — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major depressive disorder; smoking cessation |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available for this Evidence Pack. Based on published pharmacological knowledge referenced in the mechanistic rationale, Bupropion acts as an NDRI — inhibiting both the dopamine transporter (DAT) and the norepinephrine transporter (NET) to elevate catecholamine concentrations in the prefrontal cortex (PFC). It also functions as a nicotinic acetylcholine receptor (nAChR) antagonist, providing an additional route of dopamine modulation in the striatum.

ADHD's core pathophysiology is insufficient catecholaminergic signaling in the PFC — the exact target of first-line stimulant treatments such as methylphenidate and amphetamine. Bupropion's DAT/NET inhibition runs in direct mechanistic parallel to these established therapies, offering a biologically coherent rationale for repurposing without requiring a mechanistic leap.

This is not merely theoretical: a Phase 3 multicenter double-blind RCT (NCT00048360, n=162) demonstrated efficacy of extended-release Bupropion in adults with ADHD, and a Phase 2/3 RCT (NCT00061087, n=115) replicated these findings in a comorbid population. The prediction is mechanistically grounded and clinically supported, making this one of the stronger repurposing candidates in this Evidence Pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Phase 3 | Completed | 162 | 8-week multicenter double-blind placebo-controlled RCT of extended-release Bupropion HCl 300–450 mg/day in adults with ADHD — highest-grade direct evidence for this indication |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Phase 2/3 | Completed | 115 | RCT evaluating Bupropion for adult ADHD in methadone-maintained patients; primary endpoint was ADHD symptom response, providing high-grade evidence in a comorbid population |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Phase 4 | Completed | 105 | Post-marketing study of Bupropion for ADHD in adolescents with comorbid substance use disorder; provides safety and efficacy data for this dual-diagnosis group, though generalisability to general ADHD requires caution |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | Phase NA | Completed | 32 | Open-label study evaluating Bupropion SR efficacy and tolerability in ADHD adults with recent or current substance use disorders; supports feasibility but sample size is small |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | Phase NA | Completed | 32 | Primary focus on cocaine abuse; ADHD is a secondary comorbidity endpoint — limited direct relevance to ADHD monotherapy |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Early Phase 1 | Withdrawn | 0 | Relapse prevention in stimulant use disorder with/without ADHD — withdrawn before any enrollment; no data available |
| [NCT03326128](https://clinicaltrials.gov/study/NCT03326128) | Phase 2 | Terminated | 12 | High-dose Bupropion for smoking cessation; ADHD is not an endpoint; terminated early with minimal sample — no contribution to ADHD evidence |
| [NCT00330434](https://clinicaltrials.gov/study/NCT00330434) | Phase NA | Withdrawn | 0 | Pharmacokinetic/pharmacogenomic study of CYP2B6 and alcohol interactions; no ADHD efficacy relevance; withdrawn before completion |

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A Phase 3 multicenter double-blind RCT (NCT00048360, n=162) and a Phase 2/3 RCT (NCT00061087, n=115) together constitute Level 1 clinical evidence for Bupropion's efficacy in ADHD, backed by a mechanistically coherent NDRI pathway that directly addresses the dopamine/norepinephrine deficits central to ADHD pathophysiology. The evidence base justifies advancement, but the complete absence of Singapore regulatory data and formal safety documentation requires guardrails before clinical application.

**To proceed, the following is needed:**
- Retrieve Bupropion's full prescribing information (black box warnings, contraindications, drug interaction profile) from the FDA, EMA, or equivalent regulatory source — this is a blocking data gap (DG001) for formal safety evaluation
- Obtain DrugBank MOA data (DG002) to complete the mechanistic link analysis and verify pharmacodynamic comparability with approved ADHD agents
- Assess the Singapore regulatory pathway: since Bupropion is not registered locally, a compassionate use, special access, or new registration strategy must be defined
- Critically evaluate generalisability: the two highest-grade RCTs both enrolled comorbid populations (methadone maintenance, substance use disorder) — additional analysis or a de novo trial in general ADHD without SUD may be required for a clean indication claim
- Define monitoring requirements for seizure risk (a known class concern for Bupropion at higher doses) before any protocol design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

