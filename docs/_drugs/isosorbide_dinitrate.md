---
layout: default
title: Isosorbide Dinitrate
parent: Low Evidence (L5)
nav_order: 556
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Isosorbide Dinitrate: predicted new indication Alopecia (evidence level L5). Approved use: Not stated in the licence data"
monitor_inn: "Isosorbide dinitrate"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "pulmonary hypertension", "diffuse alopecia areata", "vascular disease", "hypertrichosis (disease)", "visceral calciphylaxis", "venous thoracic outlet syndrome"]
---

# Isosorbide Dinitrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Isosorbide Dinitrate: From Its Licensed Use to Alopecia (Top Prediction), with Pulmonary Hypertension as the Best-Supported Candidate

## One-Sentence Summary

Isosorbide dinitrate (ISDN) is an oral nitric oxide (NO) donor and vasodilator. Its Singapore licences do not list an approved indication in the data compiled for this report.
The TxGNN model's top-ranked prediction is **alopecia**, but it has **no clinical trials and no publications**.
The best-supported candidate among the top 10 predictions is **pulmonary hypertension** (**20 publications**, no registered trials).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (no approved indication text recorded) |
| Predicted New Indication | Alopecia (rank 1); pulmonary hypertension is the best-supported candidate (rank 4) |
| TxGNN Prediction Score | 99.99% (alopecia); 99.98% (pulmonary hypertension) |
| Evidence Level | L5 for alopecia (prediction only); L3 for pulmonary hypertension |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold (alopecia). Pulmonary hypertension is a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. ISDN is a well-known organic nitrate. It releases NO, which activates guanylate cyclase and raises cGMP, relaxing smooth muscle and dilating veins and arteries.

**Alopecia.** The link is plausible but unproven. NO-mediated vasodilation might increase scalp perfusion to hair follicles, by analogy with minoxidil. No trials or literature support this. The score likely reflects proximity to other hair-related diseases in the knowledge graph rather than a real mechanistic signal. The related predictions (congenital hypotrichosis milia, hypotrichosis simplex of the scalp, diffuse alopecia areata, hypertrichosis) are in the same position. Alopecia areata is autoimmune, so vasodilation does not address its mechanism. Hypertrichosis would be an adverse effect rather than a therapeutic use.

**Pulmonary hypertension.** The mechanistic case is much stronger. NO-cGMP signalling is the same pathway targeted by PDE5 inhibitors and sGC stimulators. Small older haemodynamic studies in COPD-associated pulmonary hypertension, end-stage cardiomyopathy and interstitial lung fibrosis report reduced pulmonary pressures. Limiting concerns include systemic hypotension, ventilation/perfusion mismatch with possible worse oxygenation, and nitrate tolerance. Recent work on bolus (2025) and intratracheal (2017, rat model) delivery suggests renewed interest in targeted administration.

---

## Clinical Trial Evidence

**Alopecia:** Currently no related clinical trials registered.

**Pulmonary hypertension:** Currently no related clinical trials registered.

For reference, the broader "vascular disease" prediction (rank 6) has registered trials. It overlaps heavily with existing cardiovascular uses, so it is not a distinct repurposing signal.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02789033](https://clinicaltrials.gov/study/NCT02789033) | Phase 3 | Completed | 68 | ISDN spray plus chitosan in diabetic foot ulcers. Most directly relevant, but the combination design confounds the ISDN-specific effect |
| [NCT02135315](https://clinicaltrials.gov/study/NCT02135315) | N/A | Completed | 1500 | Intensive vs standard blood pressure treatment in non-ST elevation acute coronary syndrome. Tests a strategy, not ISDN alone |
| [NCT00000478](https://clinicaltrials.gov/study/NCT00000478) | Phase 3 | Completed | Not reported | Asymptomatic Cardiac Ischemia Pilot study. Anti-ischemic strategies with nitrate therapy as a component |
| [NCT00803634](https://clinicaltrials.gov/study/NCT00803634) | Phase 3 | Completed | 117 | Blood pressure control in acute heart failure (clevidipine vs standard IV agents). Small and not ISDN-specific |
| [NCT01513070](https://clinicaltrials.gov/study/NCT01513070) | Phase 4 | Completed | 120 | Traditional Chinese medicine formula vs ISDN in moderate coronary stenosis. Indirect relevance |
| [NCT03011775](https://clinicaltrials.gov/study/NCT03011775) | Phase 4 | Completed | 43 | Pioglitazone in coronary heart disease. ISDN is not the focus |

---

## Literature Evidence

Pulmonary hypertension (rank 4), listing the most relevant publications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [373940](https://pubmed.ncbi.nlm.nih.gov/373940/) | 1979 | Randomised double-blind haemodynamic study | Clin Pharmacol Ther | Oral ISDN vs placebo (11 vs 7 patients) in COPD with pulmonary hypertension, with and without oxygen |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Clinical haemodynamic study | Bull Eur Physiopathol Respir | In 27 COPD patients, sublingual ISDN and nitroglycerin lowered pulmonary arterial pressure and cardiac output; only nitroglycerin reduced pulmonary vascular resistance |
| [39164577](https://pubmed.ncbi.nlm.nih.gov/39164577/) | 2025 | Clinical study | Heart Vessels | Bolus ISDN and its effect on mean pulmonary arterial pressure and blood pressure in pulmonary hypertension with cardiopulmonary comorbidities |
| [3409916](https://pubmed.ncbi.nlm.nih.gov/3409916/) | 1988 | Clinical study | Eur Heart J | In 18 patients with interstitial lung fibrosis, ISDN gave sustained haemodynamic improvement over two years where blood gases were preserved |
| [8908227](https://pubmed.ncbi.nlm.nih.gov/8908227/) | 1996 | Clinical haemodynamic study | Acta Anaesthesiol Scand | Pulmonary vascular effects of nitroglycerin and ISDN in end-stage cardiomyopathy |
| [7125407](https://pubmed.ncbi.nlm.nih.gov/7125407/) | 1982 | Clinical study | Ann Intern Med | In primary pulmonary hypertension, ISDN was the only drug to produce any reduction in pulmonary pressure, while a substantial fall in resistance required sublingual isoproterenol (alone or with ISDN) |
| [2868878](https://pubmed.ncbi.nlm.nih.gov/2868878/) | 1986 | Review | Drugs | Drug treatment of primary pulmonary hypertension; adequate trials are lacking |
| [28810603](https://pubmed.ncbi.nlm.nih.gov/28810603/) | 2017 | Preclinical (rat) | Exp Ther Med | Intratracheal ISDN improved pulmonary artery pressure and ventricular remodelling after myocardial infarction |
| [2498122](https://pubmed.ncbi.nlm.nih.gov/2498122/) | 1989 | Preclinical (rat) | Exp Mol Pathol | ISDN compared with prednisolone, indomethacin and elastase in monocrotaline-induced pulmonary hypertension |
| [6530750](https://pubmed.ncbi.nlm.nih.gov/6530750/) | 1984 | Case report | Jpn Heart J | Sustained improvement in primary pulmonary hypertension with prazosin plus ISDN |

Most of this literature is small, old and haemodynamic. It is supportive but not definitive.

**Alopecia:** Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00055P | AA PHARMA ISDN TABLET 10 mg | Tablet | Not recorded |
| SIN01139P | APO-ISDN TABLET 5 mg | Tablet | Not recorded |

Both are valid single-ingredient oral products from Apotex Inc.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for safety information.

- **Contraindication signals from the knowledge graph** (not label text): hypotensive disorder, hypertrophic cardiomyopathy, coronary artery disease, myocardial infarction, cerebral infarction and stroke disorders, intracerebral hemorrhage, intracranial hypertension and pseudotumor cerebri, anaemias and haemoglobinopathy, and hyperthyroidism (Graves disease, thyrotoxicosis). These should be verified against the label.
- **Drug interactions:** 100 interactions were identified. The main ones listed are of moderate severity: bupropion, morphine, opium, dronabinol, nabilone, sapropterin, rosiglitazone, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Omeprazole is minor.
- **Repurposing-specific concerns:** systemic hypotension, worsened oxygenation from V/Q mismatch in lung disease, nitrate tolerance, and hypotension risk in dialysis patients (visceral calciphylaxis).

---

## Conclusion and Next Steps

**Decision: Hold** (for alopecia and the other hair-related and prediction-only candidates)

**Rationale:**
- Alopecia and the other top-ranked hair disorders rest on model score alone (L5), with no trials, no literature and a speculative mechanism. The very high scores likely reflect graph proximity rather than pharmacology.
- Pulmonary hypertension (L3) is the most credible direction, supported by 20 mostly small, older haemodynamic studies. It should be treated as a research question rather than an approval-ready indication, given tolerance and oxygenation concerns and the absence of registered trials.

**To proceed, the following is needed:**
- HSA package insert warnings, contraindications and approved indications. This is a blocking gap for safety screening.
- Mechanism-of-action data from DrugBank.
- For pulmonary hypertension: a controlled trial design, ideally of targeted (inhaled or bolus) delivery, with attention to oxygenation, blood pressure and tolerance.
- Route compatibility assessment. Singapore products are oral tablets only, and targeted delivery would need a different formulation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

