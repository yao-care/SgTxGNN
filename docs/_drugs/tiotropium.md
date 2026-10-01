---
layout: default
title: Tiotropium
parent: High Evidence (L1-L2)
nav_order: 983
evidence_level: L1
indication_count: 10
---

# Tiotropium
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Tiotropium: From Established Bronchodilator Use to Obstructive Lung Disease

## One-Sentence Summary

Tiotropium is an inhaled long-acting muscarinic antagonist (LAMA) already marketed in Singapore as Spiriva Respimat and Spiolto Respimat. The TxGNN model predicts it for **obstructive lung disease**, which in practice is the drug's established COPD and asthma add-on use rather than a new indication. This direction is supported by **44 clinical trials** and **20 publications**, including multiple completed Phase 3 trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the HSA licence text (the data is empty) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Tiotropium is a long-acting M3 muscarinic antagonist. It blocks acetylcholine at airway smooth muscle, which causes bronchodilation and reduces cholinergic tone. This is the established mechanism in obstructive airway disease. Detailed DrugBank mechanism-of-action text is not available in this evidence pack.

The prediction is a rediscovery of a known use, not true repurposing. COPD and asthma add-on therapy are already marketed uses of tiotropium. The empty "original indication" field comes from a data gap in the Singapore licence record, not from an absence of approved use. The model's high score reflects that the drug sits very close to obstructive airway disease in the knowledge graph.

Other predictions in the list (ranks 2–10) are much weaker. They include respiratory malformation, Rienhoff syndrome, hyperlucent lung, interstitial and compensatory emphysema, tracheal stenosis and a CD8α-related immunodeficiency. Most have no supporting trials or literature, and several are likely artifacts of graph proximity to COPD terms. They are not recommended for follow-up at this stage.

## Clinical Trial Evidence

Many of these trials test other drugs and use tiotropium as the active comparator or background therapy.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00239460](https://clinicaltrials.gov/study/NCT00239460) | Phase 3 | Completed | 196 | 12-week, placebo-controlled study of tiotropium capsules in COPD, assessing trough FEV1 and cardiac effects (Holter/ECG) |
| [NCT01525615](https://clinicaltrials.gov/study/NCT01525615) | Phase 3 | Completed | 404 | Tiotropium + olodaterol vs placebo on exercise endurance in COPD over 12 weeks |
| [NCT00846586](https://clinicaltrials.gov/study/NCT00846586) | Phase 3 | Completed | 1134 | Indacaterol added to tiotropium vs tiotropium alone in moderate-to-severe COPD |
| [NCT01316900](https://clinicaltrials.gov/study/NCT01316900) | Phase 3 | Completed | 846 | Umeclidinium/vilanterol vs vilanterol and vs tiotropium over 24 weeks in COPD |
| [NCT01294787](https://clinicaltrials.gov/study/NCT01294787) | Phase 3 | Completed | 85 | QVA149 on exercise endurance in COPD, with tiotropium as the active control |
| [NCT00793624](https://clinicaltrials.gov/study/NCT00793624) | Phase 3 | Completed | 906 | 48-week olodaterol study in COPD (tiotropium is not the test drug) |
| [NCT01316380](https://clinicaltrials.gov/study/NCT01316380) | Phase 3 | Completed | 465 | Tiotropium Respimat (2.5 and 5 µg) vs placebo over 12 weeks in mild persistent asthma |
| [NCT01634139](https://clinicaltrials.gov/study/NCT01634139) | Phase 3 | Completed | 403 | Tiotropium Respimat vs placebo over 48 weeks in children aged 6–11 with moderate persistent asthma |
| [NCT00949975](https://clinicaltrials.gov/study/NCT00949975) | Phase 2 | Completed | 838 | Dose-ranging study of AZD9668 in COPD patients on tiotropium (add-on study) |
| [NCT05402020](https://clinicaltrials.gov/study/NCT05402020) | N/A | Completed | 17018 | Taiwan NHI claims study of tiotropium/olodaterol vs ICS/LABA in COPD |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | Tested long-term tiotropium on lung function and its decline in mild-to-moderate (early-stage) COPD |
| [29605624](https://pubmed.ncbi.nlm.nih.gov/29605624/) | 2018 | RCT | Lancet Respir Med | DYNAGITO: tiotropium + olodaterol vs tiotropium alone for preventing COPD exacerbations |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Systematic review | Cochrane Database Syst Rev | Tiotropium vs placebo in COPD, updated to include Respimat soft mist inhaler trials |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Systematic review | Cochrane Database Syst Rev | Tiotropium vs ipratropium bromide in stable COPD |
| [16844726](https://pubmed.ncbi.nlm.nih.gov/16844726/) | 2006 | Meta-analysis | Thorax | Efficacy of tiotropium on clinical events, symptoms, lung function and adverse events in stable COPD |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respir Res | Review of tiotropium's clinical development in COPD; LAMA monotherapy is recommended initial treatment for GOLD groups B, C and D |
| [29670674](https://pubmed.ncbi.nlm.nih.gov/29670674/) | 2018 | Review | Can Respir J | Tiotropium as add-on therapy for asthma, with a focus on patient selection |
| [28808948](https://pubmed.ncbi.nlm.nih.gov/28808948/) | 2017 | Review | Paediatr Drugs | Safety and efficacy of tiotropium in children and adolescents with asthma |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | Cohort | Int J Chron Obstruct Pulmon Dis | Real-world comparison of three LABA/LAMA combinations, including tiotropium/olodaterol, in Taiwanese COPD patients |
| [32274526](https://pubmed.ncbi.nlm.nih.gov/32274526/) | 2020 | Meta-analysis | Eur J Clin Pharmacol | Association between tiotropium use and cardiovascular events in COPD (a safety question) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15885P | SPIRIVA® RESPIMAT® Re-usable Solution for Inhalation 2.5 microgram | Solution | Not listed in registry record |
| SIN15890P | SPIOLTO® RESPIMAT® Re-usable Solution for Inhalation 2.5 microgram / 2.5 microgram | Solution | Not listed in registry record |

Both products are made by Boehringer Ingelheim. Spiolto is the tiotropium/olodaterol combination.

## Safety Considerations

Please refer to the package insert for safety information. The DDI query returned no records.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Many completed Phase 3 trials and several RCTs and systematic reviews support tiotropium in obstructive airway disease, and it is already marketed in Singapore. However, this is a rediscovery of a known use, not a new indication, and the Singapore licence records contain no indication or safety text to verify against.

**To proceed, the following is needed:**
- HSA package insert (indications, warnings, contraindications), which is currently blocking the safety screening
- Approved indication text for SIN15885P and SIN15890P to confirm what is already labelled
- Mechanism of action data from DrugBank
- A decision on whether this candidate should be reclassified as an existing indication rather than repurposing
- No further work is recommended on ranks 2–10 unless new evidence emerges

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

