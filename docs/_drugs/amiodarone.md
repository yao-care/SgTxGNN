---
layout: default
title: Amiodarone
parent: Medium Evidence (L3-L4)
nav_order: 89
evidence_level: L4
indication_count: 10
---

# Amiodarone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Amiodarone: From Arrhythmia Treatment to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is an antiarrhythmic drug, and the Singapore registration records do not state its approved indication text.
The TxGNN model predicts it may be effective for **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, but **no clinical trials** and only **10 publications** (cohort studies, reviews and case reports, none showing amiodarone efficacy) are available.
The high prediction score is a model output, not clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (amiodarone is an antiarrhythmic agent) |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Based on general pharmacology, amiodarone blocks several ion channels (potassium, sodium and calcium) and has beta-adrenergic antagonism. It could therefore plausibly suppress ventricular arrhythmia triggered by catecholamines, which is the trigger in CPVT.

The mechanistic fit is only partial, though. CPVT is driven by calcium-handling defects (RYR2 or CASQ2 mutations). The retrieved literature points to beta-blockers and flecainide as the effective agents, not amiodarone. No amiodarone-specific efficacy data were found, so the prediction remains hypothesis-level.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below reports amiodarone efficacy in CPVT.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review (cohort data) | Life (Basel) | Clinical characteristics, genetics and arrhythmic outcomes of CPVT patients from China; no amiodarone-specific efficacy data |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Retrospective cohort | Rev Cardiovasc Med | CPVT clinical features, genetics, healthcare use and costs in a Chinese city |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | General review of antiarrhythmic drugs for ventricular arrhythmias, not CPVT-specific |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Six-year delayed CPVT diagnosis (RYR2 mutation) in a 9-year-old child |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Arsivi | Sudden cardiac arrest as the presentation of CPVT in a 2-year-old |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Front Cardiovasc Med | CPVT resolved by right cardiac sympathetic denervation after left denervation in a teenager |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in CPVT (flecainide, not amiodarone) |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case report | BMJ Case Rep | Young child with cardiac arrest and recurrent VT/VF needing 40 shocks; diagnostic dilemma |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case report | Rev Esp Cardiol | Arrhythmic storm induced by defibrillator discharge in a CPVT patient |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case report (off-target) | Anesth Analg | Neonate with long QT syndrome and refractory VT treated with lidocaine, esmolol and amiodarone; not CPVT |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15782P | DIOLUX Concentrate for Solution for Injection 50 mg/ml (Gland Pharma) | Injection, solution, concentrate | Not stated in the record |
| SIN09784P | CORDARONE Tablet 200 mg (Sanofi Winthrop Industrie) | Tablet | Not stated in the record |
| SIN00852P | CORDARONE Injection 150 mg/3 ml (Sanofi Winthrop Industrie / Sanofi S.r.l.) | Injection | Not stated in the record |

## Safety Considerations

Please refer to the package insert for safety information.

The DDI query returned no results. This is likely a data limitation and should not be read as "no interactions". Amiodarone is known for pulmonary, thyroid, hepatic and ocular toxicity, QT prolongation and many drug interactions. These points come from general pharmacology, not from a label in the input.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The CPVT prediction has no registered trials and no amiodarone-specific efficacy data. The literature describes the disease, and where it discusses treatment it names beta-blockers and flecainide rather than amiodarone. The evidence level is L4, and the high TxGNN score is a prediction only.

**To proceed, the following is needed:**
- Amiodarone-specific efficacy or safety data in CPVT (registered trials, or cohort data comparing it with beta-blockers and flecainide)
- Singapore package insert warnings, contraindications and approved indication text
- Mechanism of action data and a DDI check
- Note: the same run also predicts *ventricular tachycardia* (L1, with Phase 3/4 RCTs). This is likely an existing clinical use rather than a new one, and it should be reviewed separately.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

