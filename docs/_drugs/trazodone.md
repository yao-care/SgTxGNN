---
layout: default
title: Trazodone
parent: Medium Evidence (L3-L4)
nav_order: 1016
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Trazodone: predicted new indication Obsessive-compulsive disorder (evidence level L3). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "Trazodone"
predicted_indications: ["obsessive-compulsive disorder", "schizoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "paranoid personality disorder", "benign paroxysmal torticollis of infancy", "agoraphobia", "dysthymic disorder", "phobic disorder", "Ohdo syndrome and variants"]
---

# Trazodone
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

## Trazodone: From Unipolar Depression to Obsessive-Compulsive Disorder
{: .text-alpha }

## One-Sentence Summary

Trazodone is an antidepressant originally used for depression (unipolar, endogenous and major depressive disorder) and anxiety disorder.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**,
but there are currently **no registered clinical trials**, and the support rests on **20 publications**, most of them small, older studies and case reports, including only one double-blind, placebo-controlled study.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (from the knowledge graph; the Singapore licence has no indication text recorded) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for trazodone is not available in the data compiled for this report. Based on general pharmacology, trazodone acts on serotonin pathways: it blocks 5-HT2A receptors and weakly inhibits serotonin reuptake. Serotonin is central to the pathophysiology of OCD, and the established OCD drugs (clomipramine, fluoxetine, fluvoxamine, paroxetine) are all serotonin reuptake inhibitors.

Depression and OCD often occur together and respond to overlapping serotonergic treatments, which makes the prediction biologically plausible. There is an important caveat: trazodone's active metabolite m-CPP has been reported to worsen OCD symptoms in some studies, so the net effect is uncertain. Review articles position trazodone as an adjunct or off-label option for OCD, not an established treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The table lists the most relevant publications, prioritising controlled studies, then open-label studies, then reviews and case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | RCT (double-blind, placebo-controlled) | J Clin Psychopharmacol | Controlled study testing trazodone's anti-obsessional efficacy in OCD; the only controlled study found, and it is old and small |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | Case series / open-label | Clin Neuropharmacol | Nine clomipramine-resistant OCD patients: mild overall improvement, 3 favourable responders whose symptoms returned on withdrawal |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | Cohort / open-label | Psychopathology | Treatment response in OCD correlated with changes in caudate glucose metabolism on PET |
| [8434675](https://pubmed.ncbi.nlm.nih.gov/8434675/) | 1993 | Case series / open-label | Am J Psychiatry | Trazodone treatment of OCD and trichotillomania |
| [3571943](https://pubmed.ncbi.nlm.nih.gov/3571943/) | 1986 | Open pilot study | Int Clin Psychopharmacol | Trazodone plus tryptophan in 11 patients: benefit marginal and poorly tolerated by several |
| [26088119](https://pubmed.ncbi.nlm.nih.gov/26088119/) | 2015 | Review | Curr Pharm Des | Off-label trazodone use, including OCD: evidence, benefits and risks |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Review | Postgrad Med | Review of trazodone in psychiatric and medical conditions |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | Case report | J Nerv Ment Dis | Two treatment-resistant OCD patients with depression improved on trazodone |
| [2589561](https://pubmed.ncbi.nlm.nih.gov/2589561/) | 1989 | Case report | Am J Psychiatry | Trazodone-fluoxetine combination for OCD |
| [29343875](https://pubmed.ncbi.nlm.nih.gov/29343875/) | 2017 | Case report | Riv Psichiatr | Prolonged-release trazodone in a patient with bipolar II disorder and OCD comorbidity |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10777P | TRITTICO TABLETS 50 mg | Tablet, film coated (oral) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Contraindications / conditions of concern (from knowledge graph associations, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, long QT syndrome (including familial), torsades de pointes, potassium deficiency, benign prostatic hyperplasia, blood coagulation disease, heart disease, cardiovascular disease, priapism, and inappropriate ADH secretion (including nephrogenic syndrome of inappropriate antidiuresis).
- **Drug Interactions**: 100 interactions were identified, and the first 20 retrieved are listed here. **Major** interactions include bupropion, lorcaserin, dolasetron, palonosetron, cisapride, dexfenfluramine and fenfluramine. Many of these involve serotonergic effects or QT prolongation. **Moderate** interactions include famotidine, loperamide, aprepitant, morphine, clarithromycin, dronabinol and eliglustat, as well as several laxatives and bowel-preparation agents.

The package insert warnings and contraindications could not be retrieved, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The OCD prediction has a high model score and some biological plausibility, but the clinical support is weak. There are no registered trials, one small and old placebo-controlled study, and otherwise open-label series and case reports. Some of the findings are mixed or negative (marginal benefit with tryptophan, possible symptom worsening via m-CPP). Safety screening cannot proceed because the label warnings are missing, and the knowledge graph flags cardiac (QT-related) concerns. Other high-scoring predictions have even less support: the personality-disorder predictions, benign paroxysmal torticollis of infancy and Ohdo syndrome rest on the model score alone.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications, and the approved indication text
- Detailed mechanism of action data (MOA)
- Full review of the 1992 double-blind study (design, sample size, results) and a systematic literature review, with comparison against first-line serotonin reuptake inhibitors
- A cardiac safety plan (QT risk, interacting drugs) and a defined role, such as add-on use in treatment-resistant OCD
- Registration of a properly controlled trial if development is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

