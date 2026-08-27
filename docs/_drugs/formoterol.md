---
layout: default
title: Formoterol
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Formoterol
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

# Formoterol: From Established Bronchodilator Therapy to TxGNN-Predicted Indications

## Evaluator's Note on This Report

This evidence pack (`TW-DB00983-multi`, v4) contains **10 TxGNN-predicted indications** for Formoterol, ranked by model score. The single highest-scoring prediction — *respiratory malformation* — is explicitly flagged in the pack's own `repurposing_rationale` as a likely **knowledge-graph node-contamination artifact**: none of its 18 linked trials or 10 publications actually studies airway malformation; all are routine asthma/COPD studies that happen to share graph neighbors with the disease label. Following the score ranking alone would produce a misleading headline, so this report leads with the **evidence-supported cluster** (bronchitis, obstructive lung disease, asthma — all Evidence Level L1) and treats the remaining seven low/no-evidence predictions as a rejected list. Full candidate-by-candidate scoring is preserved below for auditability.

---

## One-Sentence Summary

> Formoterol is a long-acting β2-adrenergic agonist (LABA) bronchodilator; no original indication record was available in the regulatory dataset (Data Gap), but literature within this evidence pack consistently identifies it as an asthma/COPD bronchodilator.
> Of TxGNN's 10 predicted indications, three — **Bronchitis**, **Obstructive Lung Disease**, and **Asthma** — are backed by **L1-grade evidence** (multiple completed Phase 3 RCTs, including landmark trials such as ETHOS, KRONOS, FULFIL, Novel START and SYGMA), while the other seven (including the top-scored "respiratory malformation") have **no genuine supporting trial or literature evidence** and are recommended **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (Data Gap). Formoterol is internationally established as a LABA bronchodilator (per literature within this pack). |
| Top TxGNN-Ranked Prediction | Respiratory malformation (score 99.92%, rank 1588) — assessed as a likely model artifact |
| Best-Evidenced Predictions | Bronchitis (99.92%), Obstructive Lung Disease (99.90%), Asthma (99.74%) — all Evidence Level **L1** |
| Evidence Level (best cluster) | **L1** — ≥2 completed Phase 3 RCTs per indication |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (Bronchitis / Obstructive Lung Disease / Asthma) — **Hold** for the remaining 7 candidates |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data was not retrievable for this record (Data Gap, DG002). However, literature captured in this evidence pack consistently and independently characterizes Formoterol's pharmacology: it is described as "a highly selective and potent β2-agonist that relaxes airway smooth muscle" (PMID 33273813) with rapid onset (within minutes) and a long duration of action (~12 hours), used as monotherapy or in fixed-dose combination with inhaled corticosteroids (budesonide, beclometasone, mometasone, fluticasone) and/or LAMAs (glycopyrronium, tiotropium, aclidinium).

This mechanism maps directly onto airway smooth-muscle relaxation, which is the core therapeutic need in **obstructive airway disease** — a spectrum that includes asthma, chronic bronchitis, and COPD. The TxGNN model's high scores for "bronchitis," "obstructive lung disease," and "asthma" are therefore not a repurposing discovery in the strict sense, but a **correct rediscovery of Formoterol's own pharmacological class** — which independently validates that the model's embedding space places Formoterol appropriately relative to its true mechanism.

By contrast, the remaining seven predicted indications have no plausible mechanistic link to β2-adrenergic bronchodilation: structural/congenital conditions (respiratory malformation, Rienhoff syndrome — a TGFB2-related connective tissue disorder), a genetic susceptibility trait (not a treatable disease entity), a Th2-mediated skin barrier disease (atopic eczema), and irreversible structural lung lesions (compensatory emphysema, interstitial emphysema, hyperlucent lung). None of these has literature or trial support in this pack, consistent with the mechanistic mismatch.

---

## All 10 Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Basis |
|------|---------|-------------|-----------------|----------|-------|
| 1 | Respiratory malformation | 99.92% | L5 | Hold | 18 trials / 10 papers reviewed — all are routine asthma/COPD studies; no malformation-specific evidence. Assessed as node contamination. |
| 2 | **Bronchitis** | 99.92% | **L1** | **Proceed with Guardrails** | Multiple completed Phase 3 RCTs directly in chronic bronchitis/COPD populations. |
| 3 | Rienhoff syndrome | 99.90% | L5 | Hold | No trials, no literature; no biological plausibility (TGFB2-related connective tissue disorder). |
| 4 | **Obstructive lung disease** | 99.90% | **L1** | **Proceed with Guardrails** | Core on-mechanism indication; large Phase 3/4 RCTs and real-world cohorts (up to 22,369 patients). |
| 5 | **Asthma** | 99.74% | **L1** | **Proceed with Guardrails** | Landmark NEJM/Lancet RCTs (Novel START, SYGMA, CARE) directly support ICS/formoterol therapy. |
| 6 | Asthma-related traits, susceptibility to | 99.50% | L5 | Hold | Genetic susceptibility trait, not a treatable disease; no trials/literature. |
| 7 | Atopic eczema | 98.98% | L4 | Hold | Only 1 trial/2 papers, none targeting eczema treatment; mechanistic mismatch (skin barrier disease vs. bronchodilation). |
| 8 | Compensatory emphysema | 98.13% | L5 | Hold | No trials/literature; structural post-surgical lesion, not an inflammatory/obstructive target. |
| 9 | Interstitial emphysema | 98.13% | L5 | Hold | No trials/literature; acute structural air-leak pathology, unrelated to smooth-muscle relaxation. |
| 10 | Hyperlucent lung | 98.13% | L5 | Hold | No trials/literature; irreversible structural damage (e.g., Swyer-James), not a bronchodilator target. |

---

## Clinical Trial Evidence
*(Bronchitis / Obstructive Lung Disease / Asthma cluster — top 10 across the three L1 candidates)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Completed | 799 | Long-term (12-month) safety of arformoterol in COPD/chronic bronchitis patients. |
| [NCT00250679](https://clinicaltrials.gov/study/NCT00250679) | Phase 3 | Completed | 443 | Long-term safety and efficacy of arformoterol tartrate inhalation solution in COPD. |
| [NCT03662711](https://clinicaltrials.gov/study/NCT03662711) | Phase 4 | Terminated | 843 | LABD ± inhaled corticosteroid vs. LABD alone on re-hospitalization/death in elderly COPD patients with cardiac comorbidity. |
| [NCT06473779](https://clinicaltrials.gov/study/NCT06473779) | Phase 3b | Active, not recruiting | 296 | Assesses whether tezepelumab-treated severe asthma patients can reduce background (formoterol-containing) maintenance therapy. |
| [NCT00252785](https://clinicaltrials.gov/study/NCT00252785) | Phase 3 | Completed | 340 | Symbicort (budesonide/formoterol) vs. Pulmicort + theophylline in Japanese asthma patients. |
| [NCT00394368](https://clinicaltrials.gov/study/NCT00394368) | Phase 3 | Completed | 180 | Beclomethasone/formoterol pMDI vs. fluticasone/salmeterol in moderate-to-severe persistent asthma. |
| [NCT00646009](https://clinicaltrials.gov/study/NCT00646009) | Phase 3 | Completed | 48 | Onset of bronchodilation: Symbicort vs. Advair Diskus vs. Ventolin HFA in asthma. |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completed | 22,155 | Post-authorization real-world drug-utilisation study of aclidinium/formoterol in Europe. |
| [NCT06744374](https://clinicaltrials.gov/study/NCT06744374) | N/A | Completed | 22,369 | Real-world US comparative-effectiveness study: mortality/cardiopulmonary outcomes with formoterol-containing single- vs. multiple-inhaler triple therapy in COPD. |
| [NCT01462942](https://clinicaltrials.gov/study/NCT01462942) | Phase 3 | Completed | 2,443 | Aclidinium/formoterol fixed-dose combination vs. monotherapy/placebo in stable COPD. |

---

## Literature Evidence
*(Bronchitis / Obstructive Lung Disease / Asthma cluster — top 10, prioritizing Tier-1 RCTs)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33252985](https://pubmed.ncbi.nlm.nih.gov/33252985/) | 2021 | RCT (post-hoc) | Am J Respir Crit Care Med | ETHOS trial: budesonide/glycopyrrolate/formoterol (BGF) triple therapy reduces all-cause mortality vs. dual therapy in COPD. |
| [30232048](https://pubmed.ncbi.nlm.nih.gov/30232048/) | 2018 | RCT | Lancet Respir Med | KRONOS trial: BGF triple therapy vs. dual therapies in moderate-to-very-severe COPD. |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL trial: once-daily triple therapy for COPD. |
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | RCT | NEJM | Novel START: as-needed budesonide-formoterol in mild asthma. |
| [29768147](https://pubmed.ncbi.nlm.nih.gov/29768147/) | 2018 | RCT | NEJM | SYGMA: as-needed budesonide-formoterol vs. maintenance budesonide in mild asthma. |
| [27916620](https://pubmed.ncbi.nlm.nih.gov/27916620/) | 2017 | RCT | Chest | Glycopyrrolate/formoterol MDI (co-suspension technology): efficacy and safety in COPD. |
| [31920296](https://pubmed.ncbi.nlm.nih.gov/31920296/) | 2019 | RCT (long-term extension) | Int J COPD | Long-term safety of BGF MDI in Japanese COPD patients. |
| [35230437](https://pubmed.ncbi.nlm.nih.gov/35230437/) | 2022 | Meta-analysis of RCTs | JAMA Netw Open | Budesonide-formoterol as maintenance-and-reliever therapy in poorly controlled asthma. |
| [41033330](https://pubmed.ncbi.nlm.nih.gov/41033330/) | 2025 | RCT | Lancet | CARE trial: budesonide-formoterol vs. salbutamol as reliever in children with mild asthma. |
| [31951778](https://pubmed.ncbi.nlm.nih.gov/31951778/) | 2020 | RCT/Review | Expert Rev Clin Pharmacol | Aclidinium bromide/formoterol fumarate for maintenance treatment of COPD. |

---

## Singapore Market Information

Formoterol currently holds **no product registration in Singapore** (0 licenses on file; market status: **not marketed**). No dosage-form or license-level detail is available in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information — key warnings and contraindications were not available in this dataset (Data Gap, DG001, flagged as **Blocking** for the S1 safety review stage).

A structured drug-drug interaction (DDI) database query returned **no matched records** (`query_status: not_found`). This reflects a data-source gap rather than confirmed absence of interactions — as a LABA, Formoterol carries well-known class-level interaction risks (e.g., other sympathomimetics, non-potassium-sparing diuretics, QT-prolonging agents, MAOIs/TCAs) that should be independently verified against the official package insert before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** — limited to the **Bronchitis / Obstructive Lung Disease / Asthma** cluster only. **Hold** on all other 7 predicted indications (respiratory malformation, Rienhoff syndrome, asthma-trait susceptibility, atopic eczema, compensatory emphysema, interstitial emphysema, hyperlucent lung).

**Rationale:**
- Three of ten TxGNN predictions are supported by L1-grade evidence (landmark Phase 3 RCTs: ETHOS, KRONOS, FULFIL, Novel START, SYGMA, CARE) and align mechanistically with Formoterol's known LABA pharmacology — but these represent confirmation of Formoterol's established therapeutic class rather than a novel repurposing signal.
- The top-scored candidate by TxGNN alone (respiratory malformation) and six others have **no supporting trial or literature evidence** and, in one case, explicit reviewer suspicion of knowledge-graph artifact contamination. These should not proceed without independent target validation.

**To proceed, the following is needed:**
- Official package insert / regulatory warnings and contraindications (DG001 — currently Blocking; required before any S1 safety review)
- DrugBank-verified mechanism-of-action record (DG002)
- Confirmation of original approved indication(s), since this dataset had no `original_indications` on file
- If genuine repurposing (vs. label-extension) is the goal, prioritize resources away from the seven Hold-status candidates and toward independent validation of any TxGNN signal not already explained by known LABA pharmacology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

