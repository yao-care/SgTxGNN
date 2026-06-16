---
layout: default
title: Clidinium
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 10
---

# Clidinium
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

# Clidinium: From Gastrointestinal Anticholinergic to Peptic Ulcer Disease

## One-Sentence Summary

Clidinium is a quaternary ammonium muscarinic receptor antagonist, classically used in combination with chlordiazepoxide (Librax) for gastrointestinal spasm and functional bowel disorders.
Although the TxGNN model's highest-ranked prediction—cauda equina syndrome—is identified as a spurious graph artefact, the model also predicts efficacy for **Peptic Ulcer Disease** (Rank #4), supported by **7 publications** including one controlled clinical trial and one clinical evaluation, making this the most actionable repurposing candidate.
Several other high-ranked predictions (myasthenia gravis variants, Ranks 5–7) carry a **mechanistic contradiction warning** and should not be pursued.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; classically used as a component of Librax (clidinium + chlordiazepoxide) for GI spasm and irritable bowel syndrome |
| Predicted New Indication (Most Actionable) | Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.83% (Rank #4 overall; Rank #1 cauda equina syndrome flagged as spurious) |
| Evidence Level | L3 — Observational studies and controlled clinical evaluations |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is currently unavailable as a data gap. However, Clidinium is a well-characterised quaternary ammonium compound that acts as an M1/M3 muscarinic receptor antagonist at enteric nerve terminals and gastric parietal cells. By blocking vagally mediated cholinergic input, it reduces basal and stimulated gastric acid secretion and relieves smooth muscle spasm throughout the gastrointestinal tract.

This mechanism directly underpins the plausibility of the peptic ulcer disease prediction. Anticholinergic agents were a cornerstone of peptic ulcer management in the pre-PPI era precisely because of their acid-suppressing and antispasmodic properties. Clidinium in the Librax combination was specifically developed for this indication, and multiple clinical evaluations from the 1960s–1980s documented its use in duodenal and gastroduodenal ulcer. A more recent controlled trial (2016) evaluated clidinium-C as an adjunct to PPI-based triple therapy for *Helicobacter pylori* eradication, suggesting a contemporary clinical niche may still exist.

By contrast, the model's highest-scoring prediction (cauda equina syndrome, 99.93%) is attributable to a spurious knowledge graph path via a "neurogenic bladder" intermediate node—cauda equina syndrome is a neurosurgical emergency requiring urgent spinal decompression, for which anticholinergic therapy has no mechanistic basis. Similarly, myasthenia gravis predictions (Ranks 5–7) represent direct mechanistic contradictions: standard MG treatment requires enhancing acetylcholine signalling, while Clidinium blocks it.

---

## All Predicted Indications at a Glance

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Assessment |
|------|-----------|-------------|----------------|----------------|------------|
| 1 | Cauda equina syndrome | 99.93% | L5 | **Hold** | Spurious graph path — surgical emergency; anticholinergics irrelevant |
| 2 | Neurogenic bladder | 99.91% | L4 | Research Question | Class-effect plausible; anticholinergics are standard for overactive bladder |
| 3 | Gastroduodenitis | 99.89% | L4 | Research Question | Mechanistically moderate; 2 old case series, no trials |
| **4** | **Peptic ulcer disease** | **99.83%** | **L3** | **Proceed with Guardrails** | **Best evidence; controlled evaluations + adjunct trial** |
| 5 | Myasthenia gravis with thymus hyperplasia | 99.71% | L5 | **Hold** | ⚠️ Mechanistic contradiction — opposes ACh signalling |
| 6 | Limb-girdle autoimmune myasthenia | 99.68% | L5 | **Hold** | ⚠️ Mechanistic contradiction — potentially harmful |
| 7 | Neonatal myasthenia gravis | 99.66% | L5 | **Hold** | ⚠️ Mechanistic contradiction + high-risk neonatal population |
| 8 | Autoimmune disease of PNS | 99.63% | L5 | **Hold** | No mechanistic basis; non-specific graph connection |
| 9 | Disease of receptor activity | 99.61% | L5 | **Hold** | Ontological super-class artefact; structural false positive |
| 10 | Large intestine disease | 99.16% | L4 | Research Question | Plausible for IBS-D; 1 physiological study in NEJM |

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Clidinium in any of the 10 predicted indications (ClinicalTrials.gov and ICTRP searches both returned zero results).

---

## Literature Evidence

### Peptic Ulcer Disease (Rank #4 — Primary Focus)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27386057](https://pubmed.ncbi.nlm.nih.gov/27386057/) | 2016 | Controlled Clinical Trial | Caspian J Intern Med | Evaluated addition of clidinium-C to 14-day PPI-based triple therapy for *H. pylori* eradication; assessed whether adjunct anticholinergic improved eradication rate and reduced antibiotic side effects |
| [4892352](https://pubmed.ncbi.nlm.nih.gov/4892352/) | 1969 | Clinical Evaluation (controlled) | Br J Clin Pract | Clinical evaluation of clidinium and Librax in the management of duodenal ulcer; controlled design comparing outcomes |
| [6896942](https://pubmed.ncbi.nlm.nih.gov/6896942/) | 1982 | Clinical Observation | Wiadomosci Lekarskie | Investigated prevention of duodenal ulcer recurrence after cimetidine treatment, with anticholinergic support |
| [14497768](https://pubmed.ncbi.nlm.nih.gov/14497768/) | 1962 | Clinical Trial (early phase) | Minerva Medica | Clinical trials of Librax (clidinium + chlordiazepoxide) across multiple digestive tract diseases including peptic ulcer |
| [14477958](https://pubmed.ncbi.nlm.nih.gov/14477958/) | 1962 | Clinical Case Series | Hospital (Rio de Janeiro) | Treatment of gastroduodenal peptic ulcer with clidinium bromide and chlordiazepoxide combination; preliminary case series |
| [14142206](https://pubmed.ncbi.nlm.nih.gov/14142206/) | 1964 | Clinical Case Series | Rev Clin Espanola | Results with chlordiazepoxide + clidinium bromide (anxiolytic + anticholinergic combination) in gastroduodenal ulcer |
| [28539](https://pubmed.ncbi.nlm.nih.gov/28539/) | 1978 | Animal Study | Pharmacology | Benzodiazepine–anticholinergic combinations (including clidinium) showed additive/supra-additive protection against stress-induced gastric mucosal erosion in mice |

### Large Intestine Disease (Rank #10)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [345122](https://pubmed.ncbi.nlm.nih.gov/345122/) | 1978 | Clinical Observation (physiological) | N Engl J Med | Studied colonic myoelectrical activity in IBS patients; a single oral dose of clidinium bromide was assessed for its effect on postprandial colonic spike and motor activity |

---

## Singapore Market Information

Clidinium (DrugBank: DB00771) has **no registered products in Singapore**. No license authorisation data is available for this drug.

---

## Safety Considerations

Formal package insert warnings and contraindications are not available as a data gap, and no drug–drug interaction data was retrieved. Please refer to the package insert for complete safety information.

**Critical mechanistic safety flags identified from prediction analysis:**

- **Myasthenia gravis (all forms — Ranks 5, 6, 7):** Anticholinergic agents are fundamentally contraindicated in myasthenia gravis. Standard MG treatment relies on acetylcholinesterase inhibitors (e.g., pyridostigmine) to amplify ACh signalling at the neuromuscular junction; Clidinium's muscarinic blockade opposes this mechanism and could precipitate myasthenic crisis. The risk is compounded in neonates (Rank 7), who have immature hepatic metabolism and reduced clearance capacity.

- **Cauda equina syndrome (Rank 1):** This is a neurosurgical emergency where bladder dysfunction is a key monitoring indicator. Anticholinergic suppression of bladder sensation could mask symptom progression and delay life-saving surgical intervention.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Peptic Ulcer Disease only — all other indications require Hold or further research)*

**Rationale:**
Clidinium has a mechanistically sound and historically documented role in peptic ulcer disease, with controlled clinical evaluations spanning the 1960s through a 2016 adjunct H. pylori eradication trial. However, the evidence base predates modern RCT standards, and the drug is not currently marketed in Singapore, requiring a full regulatory pathway assessment before any clinical application.

**Hard stops — do not proceed:**
- Ranks 5, 6, 7 (all myasthenia gravis variants): Direct mechanistic contradiction; pursuing these predictions would be clinically harmful
- Rank 1 (cauda equina syndrome): Spurious graph artefact; surgical emergency outside the scope of pharmacotherapy
- Rank 9 (disease of receptor activity): Ontological classification node, not a real clinical entity

**To proceed with peptic ulcer disease investigation, the following is needed:**
- Full MOA data from DrugBank (data gap — required for mechanistic confirmation)
- Package insert warnings and contraindications (data gap — required for safety screening)
- Drug–drug interaction assessment, particularly with CNS depressants and other anticholinergics (data gap)
- Modern systematic review or meta-analysis of anticholinergics as adjuncts to H. pylori eradication therapy
- Clarification of whether the target formulation is standalone Clidinium or the Librax combination (clidinium + chlordiazepoxide), as efficacy evidence is largely combination-based
- Singapore regulatory pathway assessment (no existing market authorisation)
- Phase 2 proof-of-concept trial design if historical evidence review is supportive
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

