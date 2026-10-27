---
layout: default
title: Magnesium Chloride
parent: Medium Evidence (L3-L4)
nav_order: 628
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Magnesium Chloride: predicted new indication Congestive heart failure (evidence level L3). Approved use: Not stated in the Singapore licence records (products are dialysis…"
monitor_inn: "Magnesium chloride"
predicted_indications: ["congestive heart failure", "gout", "osteoarthritis", "acute pulmonary heart disease", "IgG4-related pachymeningitis", "osteoarthritis susceptibility", "epiglottitis", "dyspepsia", "IgG4-related aortitis", "IgG4-related mesenteritis"]
---

# Magnesium Chloride
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

## Magnesium Chloride: From Electrolyte/Dialysis Solution Component to Congestive Heart Failure
{: .text-alpha }

## One-Sentence Summary

Magnesium chloride is a magnesium salt used in Singapore as a component of dialysis, haemofiltration and electrolyte replacement solutions.
The TxGNN model predicts it may be useful for **congestive heart failure**,
with **no registered clinical trials** and **8 retrieved publications** (about 4 of them directly relevant, mostly small studies from 1988-1995).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (products are dialysis, haemofiltration and electrolyte solutions) |
| Predicted New Indication | Congestive heart failure |
| TxGNN Prediction Score | 97.07% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, magnesium chloride is a magnesium salt, mainly supplied in Singapore as a component of dialysis and electrolyte solutions. Magnesium acts as a cofactor for Na+/K+-ATPase and modulates calcium handling and vascular tone.

Magnesium depletion is common in heart failure, often related to loop diuretic use, and is associated with ventricular arrhythmia. Correcting the deficiency could plausibly provide antiarrhythmic and haemodynamic benefit. This is the main link between the drug and the predicted indication.

The supporting studies are small and old (1988-1995), and no registered trials were available. The prediction is therefore best viewed as a research question, not an established benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Only the publications relevant to heart failure are listed below. One retrieved paper (PMID 24831644, on sodium replacement in fish) is a false match and was excluded.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8237806](https://pubmed.ncbi.nlm.nih.gov/8237806/) | 1993 | Randomised, double-blind crossover trial (n=21) | Am J Cardiol | Long-term oral magnesium chloride replacement in stable heart failure from coronary artery disease on loop diuretics |
| [7508827](https://pubmed.ncbi.nlm.nih.gov/7508827/) | 1994 | Clinical study | Circulation | Effect of acute magnesium administration on ventricular arrhythmia frequency in heart failure |
| [8861138](https://pubmed.ncbi.nlm.nih.gov/8861138/) | 1995 | Review | Magnes Res | Critical review of the antiarrhythmic action of magnesium in heart failure |
| [3233812](https://pubmed.ncbi.nlm.nih.gov/3233812/) | 1988 | Haemodynamic study (n=15) | Clin Cardiol | IV magnesium chloride raised serum magnesium and lowered mean arterial pressure (~10%) and pulmonary artery pressure (~7%) in ischaemic heart disease with heart failure |
| [8230658](https://pubmed.ncbi.nlm.nih.gov/8230658/) | 1993 | Clinical study (indirect) | JPMA | Magnesium chloride 10 mmol/day for 4 months lowered blood pressure in 22 diuretic-treated patients (mostly hypertension) |
| [2111681](https://pubmed.ncbi.nlm.nih.gov/2111681/) | 1990 | Case report | Arch Mal Coeur Vaiss | Theophylline-induced ventricular tachycardia reversed with IV magnesium chloride |
| [576067](https://pubmed.ncbi.nlm.nih.gov/576067/) | 1979 | Physiological study | Int J Chronobiol | Diurnal rhythms of renal electrolyte excretion in heart failure (indirect) |

## Singapore Market Information

All 20 licences are valid single-ingredient products, and none lists an approved indication text. Five main authorisations are shown.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07943P | Haemodialysis Concentrate NKFS-02 (Acid) for Bicarbonate Dialysis | Solution | Not stated |
| SIN13265P | Balance 1.5% Glucose 1.25 mmol/L Calcium Peritoneal Dialysis Solution | Solution, sterile | Not stated |
| SIN06523P | Plasma-Lyte A Injection | Injection | Not stated |
| SIN11635P | Prismasol BO Solution | Solution | Not stated |
| SIN13890P | Sterofundin ISO Solution for Infusion | Infusion, solution | Not stated |

## Safety Considerations

Please refer to the package insert for label warnings and contraindications, which are not available in the data compiled for this report.

- **Contraindication signals (from a knowledge graph, not label text)**: kidney disease (including chronic and end-stage renal failure), anuria, hypercalcaemia, nephrocalcinosis, nephrolithiasis, heart disease and cardiovascular disease, atrioventricular block, digitalis poisoning, ventricular fibrillation, myotonia congenita, hyperkalaemic periodic paralysis, hypoaldosteronism, sarcoidosis and phenylketonuria. The heart disease and atrioventricular block signals deserve particular attention for a cardiac indication.
- **Drug Interactions**: 58 interactions were recorded. Major interactions include **dolutegravir** and **bictegravir**, probably through chelation that reduces absorption of the antiviral. Moderate interactions include tetracyclines (doxycycline, tetracycline, minocycline, omadacycline), fluoroquinolones (ciprofloxacin, delafloxacin), bisphosphonates (alendronic acid, risedronic acid, ibandronate), vitamin D analogues (cholecalciferol, calcifediol, calcitriol, doxercalciferol), cisatracurium, deferiprone, eltrombopag, baloxavir marboxil and magnesium oxide.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence consists only of small, older studies with no registered trials, and TxGNN's score is a model prediction. Magnesium deficiency in heart failure is a plausible link, but the benefit would come mainly from correcting deficiency. Safety data from the product label is missing, and the knowledge graph flags renal and cardiac conduction contraindications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA records
- Detailed mechanism of action data
- Current randomised trial evidence on magnesium supplementation in heart failure, with clinical endpoints such as arrhythmia and hospitalisation
- A defined route and formulation (oral or IV), since the licensed Singapore products are dialysis and infusion solutions
- A safety plan for patients with renal impairment, conduction block or on interacting drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

