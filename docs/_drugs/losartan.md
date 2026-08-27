---
layout: default
title: Losartan
parent: 僅模型預測 (L5)
nav_order: 611
evidence_level: L5
indication_count: 10
---

# Losartan
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

# Losartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Losartan is an angiotensin II type 1 receptor (AT1R) blocker widely used as a first-line antihypertensive agent globally, though it currently holds no regulatory registration in Singapore.
The TxGNN model's highest-ranked prediction is **Malignant Renovascular Hypertension** (score 99.73%), supported by 2 publications; notably, **Chronic Pulmonary Heart Disease** (rank #9) carries the strongest clinical evidence across all 10 predictions, backed by a completed Phase 4 RCT (NCT00720226, n=106) and 19 publications — making it the most immediately actionable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (approved globally; not registered in Singapore) |
| Predicted New Indication | Malignant Renovascular Hypertension (Rank #1 by TxGNN) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (safety stratification required before advancing) |

---

## Why is This Prediction Reasonable?

Losartan belongs to the angiotensin II type 1 receptor antagonist (ARB) class. Although detailed mechanistic data is unavailable from the current evidence pack (Data Gap DG002), Losartan's core mechanism is well-established in the literature: it competitively and selectively blocks the AT1 receptor, preventing angiotensin II from exerting its vasoconstrictive, pro-fibrotic, and pro-inflammatory effects through the renin-angiotensin-aldosterone system (RAAS).

Malignant renovascular hypertension is driven precisely by pathological over-activation of the RAAS. Critical renal artery stenosis causes the kidney to interpret reduced perfusion as systemic hypotension, triggering a surge in renin secretion and consequently elevated angiotensin II. AT1R blockade is therefore mechanistically central — Losartan directly addresses the angiotensin II excess that perpetuates this hypertensive crisis.

**A critical safety caveat applies to this indication.** In patients with *bilateral* renal artery stenosis (or stenosis affecting a solitary kidney), ARBs remove the efferent arteriolar tone that maintains glomerular filtration pressure. This can precipitate acute renal failure. Confirming unilateral versus bilateral stenosis is a mandatory safety prerequisite before considering this use. This safety risk is the primary reason the recommendation is **Hold** despite strong mechanistic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for malignant renovascular hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10667645](https://pubmed.ncbi.nlm.nih.gov/10667645/) | 2000 | Case Report | Angiology | Enalapril + losartan combination successfully controlled refractory malignant hypertension in a Takayasu's arteritis patient with renal artery stenosis unresponsive to conventional therapy; combination improved endogenous nitric oxide release |
| [22294399](https://pubmed.ncbi.nlm.nih.gov/22294399/) | 2009 | Animal Model | Current Protocols in Pharmacology | Describes validated antihypertensive measurement protocols in SHR, DOCA-salt, and Goldblatt (renovascular) hypertension models; provides methodological framework for ARB efficacy assessment in renovascular disease |

---

## Singapore Market Information

Losartan is not currently registered in Singapore. No product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Specific safety signal for renovascular indications (Rank #1 and Rank #2):** PMID 11256525 documents a case of transient anuria following a single 50 mg dose of losartan in a hypertensive patient with a solitary kidney and chronic renal insufficiency — reinforcing the importance of renal anatomy screening prior to ARB use in any renovascular indication.

---

## Additional Predicted Indications — Overview

The TxGNN model generated 10 candidate indications. Most predictions are mechanistically plausible but evidence-limited. The exception is **Rank #9**, which stands out as uniquely actionable:

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
|------|---------|-------------|----------------|--------|-------------|----------------|
| 1 | Malignant Renovascular Hypertension | 99.73% | L4 | 0 | 2 | Research Question |
| 2 | Malignant Hypertensive Renal Disease | 99.73% | L4 | 0 | 1 | Research Question |
| 3 | Pulmonary Hypertension (multifactorial, unclear) | 99.71% | L5 | 0 | 0 | Hold |
| 4 | Pulmonary Hypertension (lung disease/hypoxia) | 99.71% | L5 | 0 | 20* | Hold |
| 5 | Braddock Syndrome | 99.61% | L5 | 0 | 0 | Hold |
| 6 | Prinzmetal Angina | 99.45% | L5 | 0 | 0 | Hold |
| 7 | Familial Hematuria–Retinal Arteriolar Tortuosity Syndrome | 99.39% | L5 | 0 | 0 | Hold |
| 8 | Brain Small Vessel Disease 1 (± ocular anomalies) | 99.37% | L4 | 0 | 18* | Hold |
| **9** | **Chronic Pulmonary Heart Disease** | **98.59%** | **L2** | **4** | **19** | **Proceed with Guardrails ★** |
| 10 | Intracerebral Hemorrhage | 97.30% | L4 | 2* | 20* | Research Question |

\* Literature matches contain substantial false positives (keyword overlap, off-topic content). \
★ Strongest evidence across all predictions — see detailed analysis below.

**Notes on Hold decisions:**
- **Rank #3–4 (Pulmonary hypertension subtypes)**: The 20 matched publications for rank #4 are general hypoxia biology reviews (brain aging, cancer, immunity) with no direct Losartan–PH connection; classified as false-positive keyword matches.
- **Rank #5 (Braddock syndrome)**: Rare genetic developmental disorder; no documented AT1R pathway involvement.
- **Rank #6 (Prinzmetal angina)**: Core mechanism is coronary artery vasospasm via calcium channel over-activation — calcium channel blockers are standard treatment; AT1R blockade has no established role.
- **Rank #7**: Rare autosomal dominant syndrome; no literature connecting AT1R/RAS to the causative gene.
- **Rank #8**: Of 18 matched publications, the vast majority concern congenital ocular anomalies (coloboma, megalocornea, optic disc defects); only PMID 34351870 is partially relevant to hypertensive cerebral small vessel disease.

---

## Spotlight: Chronic Pulmonary Heart Disease (Rank #9)

This indication carries the most mature clinical evidence of all 10 predictions and warrants priority development attention.

### Mechanistic Rationale

Losartan supports this indication through three converging mechanisms:

1. **AT1R blockade** — Angiotensin II is a potent pulmonary vasoconstrictor; AT1R antagonism attenuates hypoxic pulmonary vasoconstriction and reduces pulmonary artery pressure.
2. **TGF-β pathway inhibition** — Losartan suppresses TGF-β signalling, attenuating pulmonary fibrosis and right ventricular (RV) remodeling in COPD-driven cor pulmonale.
3. **Airway mucociliary restoration** — Losartan has shown activity in reversing cigarette smoke–induced ion channel and mucociliary dysfunction in bronchial epithelial cells.

PMID 33577434 directly demonstrated that AT1R mediates inhaled nicotine–induced pulmonary hypertension and RV remodeling in mice, and that AT1R blockade reversed these changes.

### Clinical Trials

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00720226](https://clinicaltrials.gov/study/NCT00720226) | Phase 4 | **Completed** | 106 | Directly tested Losartan for preventing COPD progression; animal data showed Losartan reverses smoking-induced lung inflammation and damage |
| [NCT02416102](https://clinicaltrials.gov/study/NCT02416102) | Phase 4 | Terminated | 31 | Evaluated Losartan on airway mucociliary dysfunction in COPD/chronic bronchitis; terminated due to recruitment difficulties — provides safety and feasibility data |
| [NCT05619653](https://clinicaltrials.gov/study/NCT05619653) | Phase 3 | Active, Not Recruiting | 279 | Placebo-controlled RCT for myocardial protection in post-COVID-19 inflammatory cardiac involvement (PASC-CVS); intervention drug to be confirmed |
| [NCT04715568](https://clinicaltrials.gov/study/NCT04715568) | Phase 4 | Recruiting | 100 | Double-blind RCT of losartan to improve cardiopulmonary outcomes in pre-COPD individuals with prolonged secondhand smoke exposure |

### Key Literature

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29750475](https://pubmed.ncbi.nlm.nih.gov/29750475/) | 2018 | RCT | Experimental Physiology | Losartan altered chemoreflex sympathetic control and cardiorespiratory regulation in obstructive sleep apnoea; both losartan and allopurinol reduced sympathetic hyperactivity associated with intermittent hypoxia |
| [15040844](https://pubmed.ncbi.nlm.nih.gov/15040844/) | 2004 | Clinical Study | Japanese Journal of Physiology | 16-week losartan treatment improved ventilatory efficiency (VE/VCO₂ slope) and neurohormonal profiles in 10 chronic heart failure patients |
| [33577434](https://pubmed.ncbi.nlm.nih.gov/33577434/) | 2021 | Animal/Mechanistic | AJP Heart and Circulatory Physiology | AT1R mediates nicotine-induced pulmonary hypertension and RV remodeling in mice; ARB treatment reversed both structural and functional changes |
| [9059545](https://pubmed.ncbi.nlm.nih.gov/9059545/) | 1997 | Clinical Study | Cardiovascular Research | AT1R blockade with losartan evaluated for haemodynamic and endocrine effects in patients with hypoxaemic cor pulmonale; attenuated acute hypoxic pulmonary vasoconstriction |
| [16117431](https://pubmed.ncbi.nlm.nih.gov/16117431/) | 2005 | Clinical Study | Klinicheskaia Meditsina | Losartan in 53 chronic cor pulmonale (COPD) patients improved pyruvic acid content and glucose-6-phosphate dehydrogenase activity in erythrocytes, enhancing gas transport |
| [15332584](https://pubmed.ncbi.nlm.nih.gov/15332584/) | 2004 | Clinical Study | Terapevticheskii Arkhiv | Losartan evaluated as combined treatment for secondary pulmonary hypertension in chronic obstructive bronchitis patients |
| [25795458](https://pubmed.ncbi.nlm.nih.gov/25795458/) | 2015 | Animal Study | JRAAS | RAAS is activated in lung tissue of smoking-induced PAH rats; establishes mechanistic basis for ARB therapy in smoking-related pulmonary hypertension |
| [24067600](https://pubmed.ncbi.nlm.nih.gov/24067600/) | 2013 | Experimental | International Journal of Cardiology | Eplerenone + losartan combination studied for RV remodeling in experimental pressure-overload RV failure; RAAS inhibition less effective in RV than LV failure — important safety context |
| [18416173](https://pubmed.ncbi.nlm.nih.gov/18416173/) | 2007 | Clinical Study | Likars'ka Sprava | Losartan improved cardiohemodynamics and vascular endothelial function in 90 COPD patients; Doppler ultrasonography assessment |
| [11220879](https://pubmed.ncbi.nlm.nih.gov/11220879/) | 2000 | Clinical Study | Terapevticheskii Arkhiv | Complete RAAS blockade safety and efficacy studied in COPD patients with right ventricular failure |

---

## Conclusion and Next Steps

### Decision for Primary Prediction (Rank #1 — Malignant Renovascular Hypertension): **Hold**

**Rationale:**
Evidence is limited to 1 case report and 1 animal model methodology paper, with no registered clinical trials. While the mechanistic rationale is strong (RAAS over-activation is the core pathology), the bilateral renal artery stenosis safety risk is a blocking concern requiring prospective safety stratification prior to any clinical development.

**To advance, the following is needed:**
- Safety stratification protocol to exclude bilateral renal artery stenosis before ARB use
- Detailed Losartan MOA data from DrugBank [Data Gap DG002]
- Singapore-specific prescribing information / package insert [Data Gap DG001]
- Prospective pilot study in confirmed unilateral renovascular hypertension patients

---

### Decision for Priority Recommendation (Rank #9 — Chronic Pulmonary Heart Disease): **Proceed with Guardrails**

**Rationale:**
A completed Phase 4 RCT (NCT00720226, n=106) directly evaluated Losartan for COPD progression, and multiple clinical studies support AT1R blockade for pulmonary hypertension and RV remodeling. Three additional active or recruiting trials provide further evidence momentum. The mechanistic triple-pathway rationale (vasoconstriction, fibrosis, mucociliary function) is well-supported.

**To proceed, the following is needed:**
- Retrieve published results of NCT00720226 (completed August 2016) — this is the most critical data gap for this indication
- Confirm the intervention agent in NCT05619653 is Losartan (trial title was truncated in this evidence pack)
- Obtain Singapore package insert / TFDA label for safety warnings [Data Gap DG001]
- Establish renal and electrolyte monitoring plan (serum creatinine, potassium, BUN)
- Define target population: COPD-associated cor pulmonale vs. other etiologies of chronic pulmonary heart disease
- Assess whether right ventricular failure patients require modified dosing given evidence of reduced RAAS efficacy in RV vs. LV failure (PMID 24067600)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

