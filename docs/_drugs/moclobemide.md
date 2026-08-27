---
layout: default
title: Moclobemide
parent: 僅模型預測 (L5)
nav_order: 666
evidence_level: L5
indication_count: 10
---

# Moclobemide
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

# Moclobemide: From Depression to Agoraphobia

## One-Sentence Summary

Moclobemide is a reversible inhibitor of monoamine oxidase A (RIMA), originally developed and used as an antidepressant for major depressive disorder and dysthymia. The TxGNN model predicts it may also be effective for **Agoraphobia** (typically presenting with panic disorder), with **0 registered clinical trials** but **12 supporting publications**, including two randomized controlled trials, currently available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (Major Depressive Disorder / Dysthymia) — inferred from known drug class information (see note below); no structured `original_indications` data available in this Evidence Pack |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available from DrugBank in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on known pharmacological information, moclobemide is a reversible inhibitor of monoamine oxidase A (RIMA) — a class distinct from older irreversible MAO inhibitors — and its antidepressant efficacy has been extensively established through decades of clinical trials in major depression, dysthymia, and atypical depression.

Depression and agoraphobia (usually co-occurring with panic disorder) share substantial pharmacological and neurobiological overlap: both are thought to involve dysregulation of serotonergic and noradrenergic signaling, and MAO-A inhibition increases synaptic availability of these monoamines. This mechanistic overlap explains why a drug developed for depression would plausibly show efficacy in panic-related anxiety disorders such as agoraphobia.

This is further supported by real-world clinical use: moclobemide has been directly studied — including in placebo-controlled and comparator-controlled randomized trials — specifically for panic disorder with agoraphobia, social phobia, and other anxiety disorders, lending strong mechanistic and empirical plausibility to the TxGNN prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

*(ClinicalTrials.gov and ICTRP searches for "Moclobemide" + "agoraphobia" both returned 0 results as of the data cutoff.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10448444](https://pubmed.ncbi.nlm.nih.gov/10448444/) | 1999 | RCT | The British Journal of Psychiatry | Randomised placebo-controlled trial of moclobemide, cognitive-behavioural therapy, and their combination in panic disorder with agoraphobia |
| [10361962](https://pubmed.ncbi.nlm.nih.gov/10361962/) | 1999 | RCT | European Archives of Psychiatry and Clinical Neuroscience | Multicenter double-blind RCT (n=135): moclobemide 450 mg/day vs. clomipramine 150 mg/day in DSM-III-R panic disorder with/without agoraphobia |
| [32002937](https://pubmed.ncbi.nlm.nih.gov/32002937/) | 2020 | Review | Advances in Experimental Medicine and Biology | Guideline-based review of psychopharmacological treatments for panic disorder/agoraphobia and other anxiety disorders |
| [28867934](https://pubmed.ncbi.nlm.nih.gov/28867934/) | 2017 | Review | Dialogues in Clinical Neuroscience | Treatment recommendations for anxiety disorders (GAD, panic disorder/agoraphobia, social anxiety disorder) based on guidelines and meta-analyses |
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatrica Scandinavica Supplementum | Review of reversible MAO-A inhibitors (brofaromine, moclobemide, toloxatone); moclobemide showed antidepressant activity across 4 placebo-controlled trials |
| [2248064](https://pubmed.ncbi.nlm.nih.gov/2248064/) | 1990 | Review | Acta Psychiatrica Scandinavica Supplementum | Reviews MAOI efficacy in controlled studies of panic disorder with agoraphobia, social phobia, atypical depression, and other conditions |
| [8313401](https://pubmed.ncbi.nlm.nih.gov/8313401/) | 1993 | RCT | Clinical Neuropharmacology | 8-week randomized double-blind trial comparing a reversible MAO-A inhibitor to clomipramine in panic disorder, supporting RIMA-class efficacy |
| [16850261](https://pubmed.ncbi.nlm.nih.gov/16850261/) | 2006 | Clinical Study | Metabolic Brain Disease | SPECT study comparing citalopram and moclobemide effects on resting brain perfusion in social anxiety disorder |
| [12006898](https://pubmed.ncbi.nlm.nih.gov/12006898/) | 2002 | Reanalysis | Journal of Clinical Psychopharmacology | Reanalysis of dose-response and therapeutic response models in panic disorder, including moclobemide data |
| [7954487](https://pubmed.ncbi.nlm.nih.gov/7954487/) | 1994 | Open-label Study | Clinical Neuropharmacology | 12-week open pilot study (n=35) of moclobemide 300-600 mg/day in social phobia; consistent improvement in fear and avoidance symptoms |

---

## Singapore Market Information

Moclobemide currently has **no registration records** in Singapore (market status: Not Marketed, 0 licenses on file). No product authorization, brand name, or approved indication text is available from the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI data are all currently unavailable — flagged as a Blocking-severity data gap, DG001. This gap must be resolved via TFDA/HSA package insert retrieval before any safety (S1) evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported by a very high TxGNN score (99.43%) and a reasonably strong historical literature base — including two double-blind randomized controlled trials directly studying moclobemide in panic disorder with agoraphobia — but the drug is not currently marketed in Singapore (0 registrations), and the Blocking-severity gap in TFDA/HSA warning/contraindication data prevents even a preliminary safety (S1) assessment.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) to close the Blocking data gap (DG001)
- Detailed mechanism of action data from DrugBank to close the High-severity gap (DG002)
- Confirmation of DDI profile, particularly relevant given moclobemide's MAO-A inhibition (interactions with serotonergic agents, sympathomimetics, triptans)
- Clarification of whether the predicted "agoraphobia" indication should be scoped as "panic disorder with agoraphobia," consistent with how it appears in the supporting literature
- An assessment of the regulatory pathway for market entry in Singapore, since no existing registration currently exists to build upon
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

