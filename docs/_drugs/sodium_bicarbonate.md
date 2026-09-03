---
layout: default
title: Sodium Bicarbonate
parent: 僅模型預測 (L5)
nav_order: 908
evidence_level: L5
indication_count: 10
---

# Sodium Bicarbonate
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

# Sodium Bicarbonate: From Metabolic Acidosis to Bronchitis

## One-Sentence Summary

Sodium bicarbonate is a systemic alkalinizing agent traditionally used to correct metabolic acidosis and as an antacid; the evidence pack does not contain a confirmed original indication or Singapore license record for this drug. The TxGNN model predicts it may be effective for **Bronchitis**, but the supporting evidence base is currently thin — the retrieved clinical trials mostly involve unrelated compounds, and the literature is limited to a few small, decades-old observational reports.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not on file (traditionally used for metabolic acidosis / as a systemic alkalinizer — no Singapore license data available) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 97.91% |
| Evidence Level | L3 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sodium bicarbonate is a systemic alkalinizing agent, its efficacy in correcting metabolic acidosis and buffering excess acid has been proven, and mechanistically may be applicable to bronchitis via its historical use as an inhaled/endobronchial expectorant.

The proposed link to bronchitis rests on this older use: by alkalinizing airway secretions, bicarbonate may lower sputum viscosity and promote mucus clearance in chronic bronchitis. This is consistent with two 1988 observational reports on "endobronchial therapy" of chronic bronchitis, and with the broader CFTR/ion-channel dysfunction implicated in COPD pathophysiology.

That said, this remains an indirect, mechanism-based hypothesis rather than a proven treatment. None of the four clinical trials retrieved for this indication actually studied sodium bicarbonate — they involve unrelated investigational compounds (an HBV antisense drug, a JAK inhibitor, a CXCR2 antagonist, and a withdrawn urine-pH study) and were flagged as low relevance (Grade C) during triage. The only somewhat specific supporting evidence — two small Soviet-era cohort/clinical studies on endobronchial bicarbonate-type therapy — has not been replicated in any modern controlled trial.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02981602](https://clinicaltrials.gov/study/NCT02981602) | Phase 2 | Completed | 31 | IONIS-HBVRx (antisense oligonucleotide) in chronic HBV — unrelated compound; low relevance (Grade C) |
| [NCT01163253](https://clinicaltrials.gov/study/NCT01163253) | Phase 3 | Terminated | 2,867 | Long-term safety of CP-690,550 in plaque psoriasis — unrelated compound, trial terminated; low relevance (Grade C) |
| [NCT02469298](https://clinicaltrials.gov/study/NCT02469298) | Phase 2 | Completed | 45 | Danirixin (CXCR2 antagonist) ± oseltamivir for influenza — unrelated compound; low relevance (Grade C) |
| [NCT01421160](https://clinicaltrials.gov/study/NCT01421160) | Phase 1 | Withdrawn | 0 | Urinary pH regulation for chronic joint pain (citrate regimen) — wrong indication, withdrawn with 0 enrolled; low relevance (Grade C) |

**Note:** None of the retrieved trials directly investigated sodium bicarbonate for bronchitis; all were assessed as low relevance during evidence triage.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23934925](https://pubmed.ncbi.nlm.nih.gov/23934925/) | 2013 | Review | Am J Physiol Lung Cell Mol Physiol | CFTR dysfunction in COPD/chronic bronchitis pathogenesis — mechanistic background, not a bicarbonate treatment study |
| [2838916](https://pubmed.ncbi.nlm.nih.gov/2838916/) | 1988 | Cohort/Clinical | Sovetskaia meditsina | Endobronchial expectorant therapy of chronic bronchitis (historical report) |
| [2846955](https://pubmed.ncbi.nlm.nih.gov/2846955/) | 1988 | Cohort/Clinical | Klinicheskaia meditsina | Endobronchial therapy of patients with chronic bronchitis (historical report) |
| [778960](https://pubmed.ncbi.nlm.nih.gov/778960/) | 1976 | Physiology study | Respiration | Pulmonary vascular response to hypercapnic ventilation — background physiology, not a treatment study |
| [16424422](https://pubmed.ncbi.nlm.nih.gov/16424422/) | 2006 | Clinical (unrelated drug) | Chest | Albuterol enantiomers and airway secretions in intubated patients — unrelated compound |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on an indirect, decades-old mechanistic rationale (alkalinizing mucolytic effect) with no directly relevant modern clinical trials; all four retrieved trials involve unrelated compounds, leaving only two small 1988 observational reports as supporting literature (Evidence Level L3).

**To proceed, the following is needed:**
- TFDA/HSA label warnings and contraindications for sodium bicarbonate (currently a **blocking** data gap — required before any safety pre-assessment)
- Confirmed mechanism of action (MOA) data from DrugBank
- A modern, controlled trial (or at minimum a systematic review) specifically evaluating alkalinizing/bicarbonate-based mucolytic therapy in chronic bronchitis or COPD
- Clarification of Singapore regulatory status, since the drug currently has zero registered licenses and is not marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

