---
layout: default
title: Terbutaline
parent: 僅模型預測 (L5)
nav_order: 957
evidence_level: L5
indication_count: 10
---

# Terbutaline
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

# Terbutaline: From Established Bronchodilator Use to Obstructive Lung Disease

## One-Sentence Summary

> Terbutaline is a short-acting β2-adrenergic agonist bronchodilator, referenced throughout the clinical evidence base primarily for asthma and COPD symptom relief (e.g. as the comparator/rescue medication "Bricanyl"/"Turbuhaler" in dozens of trials).
> The TxGNN model's top prediction — **Obstructive Lung Disease** — is supported by **68 clinical trials** and **20 publications**, but the model's own repurposing rationale notes this is effectively a confirmation of the drug's already-established pharmacological use rather than a genuinely novel indication.
> Terbutaline is currently **not marketed in Singapore** (0 registrations on file).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Singapore regulatory data (unlicensed, no license records). Evidence corpus consistently associates terbutaline with asthma/bronchospasm management as a SABA bronchodilator. |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned at the drug level (`original_moa: [Data Gap]`). However, the TxGNN repurposing rationale for this candidate does provide mechanistic detail: **terbutaline is a selective β2-adrenergic receptor agonist** that increases intracellular cAMP in bronchial smooth muscle cells, producing smooth-muscle relaxation and bronchodilation — the core pharmacological mechanism underlying treatment of obstructive airway diseases (asthma/COPD).

Importantly, the model's own reasoning flags a caveat that should shape interpretation: *"this indication is essentially an existing/already-approved use rather than a new one; the mechanistic linkage is extremely strong and already clinically validated."* This is corroborated by the evidence pack itself — the vast majority of clinical trials retrieved for "obstructive lung disease" use terbutaline (Bricanyl/Turbuhaler) as a standard rescue bronchodilator or active comparator in asthma/COPD studies, not as an experimental new therapy.

In other words, this candidate functions less as a novel drug-repurposing signal and more as **validation that the TxGNN model correctly recovers a drug's true pharmacology**. For Singapore specifically — where terbutaline currently holds no market authorization — the practical value of this evidence lies in supporting a conventional registration pathway for the known bronchodilator indication, rather than justifying an off-label repurposing program.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Completed | 4,215 | Large RCT comparing Symbicort "as needed" vs. Pulmicort BID + terbutaline "as needed" in asthma; terbutaline used as reliever in a major treatment arm |
| [NCT00259766](https://clinicaltrials.gov/study/NCT00259766) | Phase 3 | Completed | 1,970 | Health-economics/real-life evaluation comparing Symbicort maintenance+reliever vs. Pulmicort+Oxis+Bricanyl (terbutaline) as-needed in asthma |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Completed | 3,850 | Compares Symbicort "as needed" with terbutaline "as needed" alone, and with Pulmicort BID + terbutaline "as needed" in asthma |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Completed | 2,091 | 12-month RCT: Symbicort SMART vs. Symbicort BID + terbutaline as-needed in asthma |
| [NCT00242775](https://clinicaltrials.gov/study/NCT00242775) | Phase 3 | Completed | 2,100 | 6-month RCT: Symbicort vs. Seretide + terbutaline as-needed in persistent asthma |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Completed | 860 | As-needed Budesonide/Formoterol vs. regular Budesonide/Formoterol + as-needed terbutaline in mild-moderate persistent asthma |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Completed | 95 | Cross-over PD study of Bricanyl (terbutaline) Turbuhaler M3 vs. M2 on methacholine-induced bronchoconstriction protection |
| [NCT00750568](https://clinicaltrials.gov/study/NCT00750568) | N/A | Unknown | 36 | PK/PD of continuous IV terbutaline infusion in pediatric severe status asthmaticus |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Completed | 120 | 2024 RCT comparing IV magnesium sulfate vs. terbutaline for pediatric acute asthma exacerbation in emergency settings |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Completed | 24 | Crossover study of relative efficacy of terbutaline Turbuhaler 0.4mg vs. salbutamol pMDI 200μg in Japanese asthma patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | RCT | Acad Emerg Med | Nebulized terbutaline + ipratropium vs. terbutaline alone in AECOPD requiring NIV; double-blind RCT |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | Br J Dis Chest | Double-blind crossover RCT: oral terbutaline increased diaphragmatic contraction force in COPD patients |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | RCT | Chest | Crossover RCT on beta-blocker/terbutaline interaction effects in chronic obstructive lung disease |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | Int J Clin Pharmacol Ther Toxicol | Double-blind 2-week study comparing oral clenbuterol and terbutaline in chronic obstructive lung disease |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Study | Ann Palliat Med | N-acetylcysteine + terbutaline sulfate in elderly COPD patients; apoptosis/anti-apoptosis mechanism |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Review | J Allergy Clin Immunol | Overview of asthma as an obstructive airway disease, including bronchodilator pharmacology |
| [20004090](https://pubmed.ncbi.nlm.nih.gov/20004090/) | 2010 | Study | Respir Med | Emitted dose and lung deposition of inhaled terbutaline from Turbuhaler under varying conditions |
| [3044105](https://pubmed.ncbi.nlm.nih.gov/3044105/) | 1988 | Study | Am J Med Sci | Double-blind RCT: oral terbutaline augments cardiac performance in COPD patients |
| [2805868](https://pubmed.ncbi.nlm.nih.gov/2805868/) | 1989 | Study | Chest | Effects of IV terbutaline on ventilation-perfusion distribution and hemodynamics in COPD |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | Study | Respir Med | Double-blind crossover study: inhaled terbutaline effect on FEV1, FVC, dyspnoea, walking distance in COLD |

---

## Singapore Market Information

Terbutaline currently holds **no marketing authorization in Singapore** — the evidence pack records 0 total licenses and a market status of "Not Marketed." No product registration entries were available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the underlying data pack flags a **Blocking** data gap — HSA/regulatory label warnings and contraindications were not retrieved — which prevents a preliminary safety assessment (S1 stage) at this time. Drug interaction lookup also returned no results.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is driven by multiple large, completed Phase 3 RCTs, but nearly all of this evidence reflects terbutaline's already-established bronchodilator role in asthma/COPD rather than a genuinely novel repurposing signal — the model's own rationale confirms this. Since terbutaline is unlicensed in Singapore, the realistic near-term action is supporting a standard registration dossier for the known indication, not an exploratory repurposing initiative.

**To proceed, the following is needed:**
- Resolve the **Blocking** data gap: obtain official label warnings/contraindications (source: regulatory label PDF) before any safety evaluation can proceed
- Obtain confirmed mechanism-of-action (MOA) documentation from DrugBank to replace the current data gap
- Clarify original/historical indication status, since no Singapore license records exist to anchor the "original indication" baseline
- If pursuing market entry, treat this as a standard new-registration dossier (asthma/COPD bronchodilator) rather than a repurposing candidate, and deprioritize the lower-evidence predictions (ranks 2–10, all L4/L5 with sparse or absent supporting data)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

