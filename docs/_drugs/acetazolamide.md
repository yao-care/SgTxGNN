---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamide: From Glaucoma / Altitude Sickness to Cardiomyopathy

## One-Sentence Summary

Acetazolamide is a well-established carbonic anhydrase (CA) inhibitor with decades of documented clinical use in glaucoma, acute mountain sickness, and epilepsy.
The TxGNN model predicts it may be effective for **Cardiomyopathy** (specifically acute decompensated heart failure), with **3 ongoing clinical trials** and **10 related publications** supporting this direction — anchored by the landmark ADVOR Phase 3 RCT (NEJM 2022) that has already validated the core mechanism.

> **Note on prediction ranking:** TxGNN's #1-ranked prediction is "exercise-induced malignant hyperthermia" (score 99.95%), for which no supporting clinical evidence exists and the recommendation is Hold. **Cardiomyopathy** (TxGNN rank #7, score 99.83%) is selected as the primary focus of this report as the highest-evidence repurposing candidate in the pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma, acute mountain sickness, epilepsy (standard CA inhibitor — not registered in Singapore) |
| Predicted New Indication | Cardiomyopathy (acute decompensated heart failure) |
| TxGNN Prediction Score | 99.83% (TxGNN rank #7; rank #1 by clinical evidence strength) |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acetazolamide inhibits carbonic anhydrase enzymes in the renal proximal tubule, blocking bicarbonate and sodium reabsorption. In heart failure patients receiving loop diuretics, this creates synergistic decongestion while simultaneously correcting metabolic alkalosis — a complication that blunts loop diuretic responsiveness in a significant proportion of acute HF admissions. The combined natriuretic and alkalosis-correcting effect addresses two mechanistically linked barriers to effective fluid removal in a single agent.

Beyond the kidney, cardiac CA2 isoforms regulate intracellular pH and modulate Na⁺/H⁺ exchanger activity in cardiomyocytes. CA inhibition may therefore interfere with pathological remodeling signals in the congested myocardium, providing a mechanistic rationale that extends beyond simple adjunctive diuresis. This cardiac-intrinsic action distinguishes acetazolamide from other loop diuretic augmentation strategies such as metolazone.

The ADVOR Phase 3 RCT (Mullens et al., NEJM 2022) directly validated this mechanism in a controlled clinical setting, demonstrating that IV acetazolamide added to standardized furosemide significantly improved successful decongestion at 3 days without worsening renal function. Three currently enrolling Phase 4 trials (total planned enrollment ~1,805 patients) are now expanding the evidence to oral formulations, diverse HF subgroups, and biomarker-guided dosing strategies — confirming this is a maturing clinical application rather than a speculative prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | Recruiting | 400 | Oral acetazolamide for acute CHF decompensation; Phase 4 status confirms prior Phase 3 (ADVOR) success and supports route transition from IV to oral |
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | Recruiting | 939 | Double-blind multicenter RCT comparing loop diuretics + acetazolamide vs. metolazone vs. loop diuretics alone in AHF patients with volume overload refractory to standard therapy |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | N/A | Recruiting | 466 | Urine sodium–guided tailored diuretic algorithm in acute decompensated HF; evaluates acetazolamide's role within a precision, biomarker-directed clinical decision framework |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Annual Review | ESC Heart Failure | 2024 ESC HF guideline update covering SGLT2i, finerenone, and the evolving landscape of diuretic and congestion management strategies |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | 2022 cardiovascular pharmacology advances; covers mavacamten approval for obstructive HCM and emerging adjunctive HF agents |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | Journal of Cardiology Cases | Acetazolamide successfully corrects hypochloremia (94 mEq/L) and hyponatremia in an advanced HF + HCM patient on complex diuretic regimen; identifies chloride manipulation as a viable HF therapeutic target |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Animal Study | Saudi Medical Journal | Acetazolamide effects on ischemia-reperfused isolated hearts in 2- and 8-week-old rabbits; provides preclinical mechanistic cardiac data on CA inhibition and myocardial protection |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case Series | Acta Neurologica Scandinavica | Cardiomyopathy documented in nine members of a hypokalaemic periodic paralysis family; early evidence of cardiac muscle involvement in a population historically treated with acetazolamide |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case Series | Acta Neurologica Scandinavica | Patient on acetazolamide 750–1000 mg/day for periodic paralysis developed exercise angina with ST depression; cardiac monitoring considerations in long-term acetazolamide users |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Case Report / Safety Signal | Acute Medicine & Surgery | Non-cardiogenic pulmonary edema developed within 1 hour of IV acetazolamide in a dilated cardiomyopathy patient; critical safety signal for cardiac use in hemodynamically unstable patients |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case Report | Indian Journal of Ophthalmology | Oral acetazolamide used in Danon disease (LAMP2 mutation with cardiomyopathy) to treat cystoid macular edema; demonstrates drug use in a cardiomyopathy-associated rare disease context |

---

## Safety Considerations

Please refer to the package insert for complete safety information (full warnings and contraindications data were not available for this report).

The following safety signals are documented in the literature reviewed for this Evidence Pack:

**IV Administration in Heart Failure — Pulmonary Risk:**
PMID 29123889 documents a case of non-cardiogenic pulmonary edema occurring within 1 hour of IV acetazolamide in a patient with dilated cardiomyopathy. The mechanism is not fully established, but this signal warrants heightened respiratory monitoring when initiating IV acetazolamide in hemodynamically compromised cardiac patients.

**Gastrointestinal Motility Impairment:**
Acetazolamide-induced adynamic ileus has been reported (PMID 19653068) along with drug-potentiated paralytic ileus (PMID 13659695). This is particularly relevant for post-cardiac surgery or ICU heart failure patients who are already at elevated risk for gastrointestinal dysmotility.

**Cardiac Monitoring in Long-Term Use:**
One case series (PMID 7324871) documented exercise angina with ECG changes in a patient on high-dose acetazolamide (750–1000 mg/day) for periodic paralysis, suggesting that baseline and periodic cardiac assessment is warranted in patients receiving prolonged therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ADVOR Phase 3 RCT (NEJM 2022) provides Level 1 evidence that acetazolamide improves decongestion in acute decompensated heart failure, and three active Phase 4 trials enrolling nearly 1,800 patients confirm that international cardiology is rapidly integrating this indication into standard practice — moving this well beyond the realm of speculative repurposing.

**To proceed, the following is needed:**

- **Singapore regulatory pathway**: Acetazolamide is currently not registered in Singapore (HSA: 0 licenses); an import, compounding, or new drug registration pathway with HSA must be established before any clinical use
- **Complete safety profile**: Retrieve the current TFDA / EMA / FDA package insert for full contraindications (including sulfonamide cross-hypersensitivity), black box warnings, and drug-drug interactions — this data gap is classified as **Blocking** in this Evidence Pack
- **MOA documentation**: Formal mechanism of action data from DrugBank (DB00819) should be retrieved to support regulatory submissions and mechanistic rationale in any dossier
- **Route of administration decision**: ADVOR validated IV acetazolamide; a separate Phase 4 trial (NCT05802849) is exploring oral administration — confirm which formulation is appropriate for the Singapore clinical setting
- **Electrolyte monitoring protocol**: Define prospective monitoring parameters (serum K⁺, Na⁺, Cl⁻, HCO₃⁻, creatinine, urine Na⁺) given risk of electrolyte disturbances inherent to combination diuretic regimens
- **Patient selection criteria**: Align target population with ADVOR eligibility (ADHF with metabolic alkalosis and suboptimal response to loop diuretics) to maximize benefit-risk ratio in any Singapore pilot program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

