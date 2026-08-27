---
layout: default
title: Lisdexamfetamine
parent: 僅模型預測 (L5)
nav_order: 600
evidence_level: L5
indication_count: 10
---

# Lisdexamfetamine
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

# Lisdexamfetamine: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

Lisdexamfetamine (LDX) is a CNS stimulant prodrug enzymatically converted to d-amphetamine in the body, clinically established worldwide as a first-line pharmacotherapy for attention-deficit/hyperactivity disorder (ADHD). The TxGNN model predicts it may be effective for **Specific Developmental Disorder** — a broad neurodevelopmental disease category under ICD-10 F80–F90 that directly encompasses ADHD — with **1 clinical trial** and **2 publications** currently supporting this direction; a Phase 2/3 RCT in Japanese pediatric patients provides the core evidence underpinning an L2 rating.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ADHD (Attention-Deficit/Hyperactivity Disorder) — not formally registered in Singapore |
| Predicted New Indication | Specific Developmental Disorder |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lisdexamfetamine is a prodrug composed of L-lysine covalently linked to d-amphetamine. Following oral administration, it is enzymatically hydrolysed in red blood cells to release active d-amphetamine, which promotes reversal of the dopamine transporter (DAT) and norepinephrine transporter (NET), sharply increasing synaptic catecholamine concentrations in the prefrontal cortex. This mechanism directly addresses the core neurobiological deficit of ADHD — impaired dopaminergic and noradrenergic signalling in frontal executive networks — and explains LDX's regulatory approvals in the US (FDA, 2007), EU, and Japan. Formal MOA data was not retrieved from DrugBank in this evidence pack; the above description is drawn from published pharmacology literature.

ADHD (ICD-10 F90) belongs to the broader "specific developmental disorder" disease group (ICD-10 F80–F90: neurodevelopmental disorders encompassing language, motor, scholastic, and attention disorders). This makes the TxGNN prediction a category-level extension of established clinical evidence rather than a classically novel repurposing signal. The mechanistic link is direct: LDX's prefrontal dopamine/norepinephrine augmentation maps precisely onto the shared pathophysiology of attention dysregulation, executive function deficits, and developmental learning impairments across this entire disease class.

Critically, a multicenter, randomized, double-blind, placebo-controlled Phase 2/3 trial conducted in Japanese paediatric patients (PMID 31718254) confirms LDX efficacy within this disease group, demonstrating significant reduction in ADHD-RS-IV total scores across doses of 30–70 mg/day over four weeks. This Asian-population dataset is particularly relevant for Singapore market assessment, where a comparable genetic and metabolic background may be expected.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | Completed | 27 | Mechanistic study exploring reinforcing effects of smoking in adult ADHD patients, including whether stimulant medication (LDX) potentiates smoking reward via ADHD symptom improvement, mood enhancement, or arousal. Not a primary efficacy trial for developmental disorders, but provides CNS mechanistic data in an ADHD/neurodevelopmental population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31718254](https://pubmed.ncbi.nlm.nih.gov/31718254/) | 2020 | Phase 2/3 RCT | J Child Adolesc Psychopharmacol | Multicenter, randomized, double-blind, placebo-controlled trial of LDX 30/50/70 mg/day for 4 weeks in 76 Japanese paediatric patients (ages 6–17) with ADHD. Primary endpoint (ADHD-RS-IV total score change from baseline) was met with statistical significance. Key Asian-population dataset directly applicable to Singapore. |
| [37849578](https://pubmed.ncbi.nlm.nih.gov/37849578/) | 2023 | Case Report | Cureus | An 18-year-old female with Hao-Fountain syndrome (USP7 mutation), intellectual disability, and comorbid ADHD. No LDX treatment data; documents co-occurrence of ADHD within a rare neurodevelopmental syndrome — contextually relevant to the breadth of the specific developmental disorder category but does not provide LDX efficacy evidence. |

---

## Singapore Market Information

Lisdexamfetamine is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No marketing authorisations or product licences are on file in this evidence pack. As an amphetamine-class controlled substance, regulatory scheduling classification under Singapore's Misuse of Drugs Act must be confirmed as a prerequisite to any registration pathway assessment.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not retrieved in this evidence pack. Full package insert review (including cardiovascular risk, abuse potential, psychiatric adverse events, and MAO inhibitor interactions) is required before any clinical or regulatory decision.

---

⚠️ **Adverse Effect Signals Identified in Secondary TxGNN Predictions**

Two lower-ranked predictions contain important safety signals that should be incorporated into any risk management plan:

- **Trichotillomania (Rank #7):** Two published reports (PMID [32932388](https://pubmed.ncbi.nlm.nih.gov/32932388/); PMID [31984712](https://pubmed.ncbi.nlm.nih.gov/31984712/)) document LDX and other CNS stimulants *inducing* new-onset trichotillomania (hair-pulling disorder) rather than treating it. Excess dopaminergic activation may reinforce compulsive repetitive behaviour circuits (basal ganglia–anterior cingulate pathway). This should be classified as a **potential contraindication signal** in patients with body-focused repetitive behaviour (BFRB) history, not a repurposing target.

- **Transient Tic Disorder (Rank #8):** Pharmacovigilance analyses and ADHD adverse event management reviews (PMID [37645441](https://pubmed.ncbi.nlm.nih.gov/37645441/); PMID [23294014](https://pubmed.ncbi.nlm.nih.gov/23294014/)) consistently position tics as a side effect requiring monitoring during stimulant therapy. Dopamine pathway potentiation may theoretically worsen striatal motor output in tic-prone patients. No therapeutic benefit signal exists.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
ADHD is definitionally a specific developmental disorder (ICD-10 F90), and a Phase 2/3 RCT in an Asian paediatric population confirms LDX efficacy within this disease class, supporting an L2 evidence level. The biological rationale is mechanistically sound and category-consistent. However, LDX is an amphetamine-class controlled substance with significant regulatory and safety complexities that must be resolved before any further development step in Singapore.

**To proceed, the following is needed:**

- **Controlled substance classification:** Confirm LDX's scheduling status under Singapore's Misuse of Drugs Act (MDA) and determine whether a Therapeutic Products (TP) licence application is feasible under the current controlled drug framework
- **Full package insert review:** Retrieve HSA-equivalent or FDA/EMA labelling to document cardiovascular warnings, psychiatric adverse events, contraindications (including MAO inhibitor co-administration), and abuse/dependence precautions — all currently flagged as data gaps in this evidence pack
- **Drug interaction assessment:** Conduct a formal DDI screen; the current evidence pack returned zero interactions due to query failure, not confirmed absence of interactions
- **Population scope clarification:** Define whether the clinical target remains ADHD specifically, or whether evidence for other conditions within the "specific developmental disorder" category (e.g., specific learning disability F81, developmental coordination disorder F82) is also being pursued, as each sub-category requires separate evidence review
- **Risk management protocol:** Incorporate monitoring plans for trichotillomania and tic exacerbation, both identified as adverse effect signals in this evidence pack
- **Narcolepsy secondary opportunity:** Consider a separate evaluation of narcolepsy (TxGNN Rank #9, L3 evidence; 2 completed Phase 1/2 trials, case series, and multiple historical reviews documenting amphetamine-class use for excessive daytime sleepiness) — this represents a biologically plausible secondary repurposing candidate warranting its own evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

