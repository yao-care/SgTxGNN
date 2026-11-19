---
layout: default
title: Sevoflurane
parent: Low Evidence (L5)
nav_order: 911
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Sevoflurane: predicted new indication Prinzmetal angina (evidence level L5). Approved use: General anaesthesia"
monitor_inn: "Sevoflurane"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "migraine disorder", "inclusion body myositis"]
---

# Sevoflurane
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

## Sevoflurane: From General Anaesthesia to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Sevoflurane is an inhaled general anaesthetic used for induction and maintenance of anaesthesia in a controlled perioperative setting.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anaesthesia (inhaled anaesthetic; the registered indication text is not available in the Singapore licence records) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 5 of 5) |
| Number of Registrations | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of sevoflurane as: Glycine receptor (alpha-1/beta) positive modulator; GABA-A receptor; anion channel positive allosteric modulator; Potassium channel subfamily K member 10 opener; Potassium channel subfamily K member 18 opener ([ChEMBL CHEMBL1200694 (sevoflurane): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200694), CC BY-SA 3.0; accessed 2026-11-19.) Based on general pharmacology, sevoflurane is a volatile anaesthetic that enhances GABA-A receptor activity and inhibits NMDA and nicotinic receptors. Volatile anaesthetics also have vasodilatory effects on vascular smooth muscle, partly through calcium channel modulation.

Prinzmetal angina is caused by coronary artery vasospasm. A vasodilatory effect could therefore, in theory, relate to this condition. However, no clinical or literature support was found for this link. Sevoflurane is given only in a controlled perioperative setting, so chronic or preventive use for vasospastic angina is not plausible. The prediction should be treated as a hypothesis, not as evidence of benefit.

Other high-scoring predictions, none of which has clinical trial evidence, are:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Tourette syndrome | 0.9950 | L5 | No studies; inhaled anaesthesia is impractical for a chronic condition |
| 3 | Fibromyalgia | 0.9942 | L4 | One case report on anaesthetic management only; indirect |
| 4 | Tendinitis | 0.9941 | L5 | Anaesthesia studies in tendon surgery; the link is a surgical context, not treatment |
| 5 | Myositis fibrosa | 0.9941 | L5 | No studies and no plausible mechanism |
| 6 | Idiopathic granulomatous myositis | 0.9941 | L5 | No studies |
| 7 | Nephrogenic syndrome of inappropriate antidiuresis | 0.9940 | L5 | No action on the V2 receptor pathway; nephrotoxicity concerns |
| 8 | Trichotillomania | 0.9933 | L5 | No studies; nonspecific CNS effects |
| 9 | Migraine disorder | 0.9923 | L5 | Only a paediatric MRI anaesthesia cohort; volatile agents can cause headache |
| 10 | Inclusion body myositis | 0.9909 | L4 | One case report on perioperative management only |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature is available for Prinzmetal angina.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN08264P | SEVORANE INHALATION | SOLUTION | Valid |
| SIN13741P | Sevoflurane Inhalation Anaesthetic Liquid 100% | INHALANT | Valid |
| SIN14780P | SOJOURN INHALATION ANAESTHETIC LIQUID 100% | INHALANT | Valid |
| SIN16819P | NOREVELL INHALATION ANAESTHETIC LIQUID 100% | INHALANT | Valid |
| SIN17305P | HEAREM SEVOFLURANE INHALATION ANAESTHETIC LIQUID 100% | INHALANT | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: the TxGNN knowledge graph lists contraindication links with epilepsy, kidney disease, pyoureter, liver disease, gallbladder disease, hypotensive disorder, malignant hyperthermia of anaesthesia, exercise-induced malignant hyperthermia, pseudotumor cerebri, intracranial hypertension, Duchenne muscular dystrophy, muscular dystrophy, Becker muscular dystrophy and proteinuria. These must be checked against the approved package insert. Hypotension is particularly relevant to a cardiovascular indication.
- **Drug Interactions**: 100 interactions were recorded; the first 20 retrieved are summarized here.
  - **Major**: epinephrine, dolasetron, cisapride.
  - **Moderate** (examples): morphine, ondansetron, palonosetron, clarithromycin, levofloxacin, famotidine, exenatide, loperamide and several laxatives and bowel-preparation agents.
  - **Minor**: metronidazole.

The package insert warnings and contraindications could not be retrieved and should be reviewed directly.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no clinical trials or supporting literature for Prinzmetal angina. Sevoflurane is a perioperative inhaled anaesthetic, so chronic or preventive use for vasospastic angina is impractical. Package insert safety data is also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA records, which is a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank) to support any analysis of a mechanistic link
- Preclinical or clinical evidence of an effect on coronary vasospasm
- A feasibility assessment of a practical route and setting of use, given that sevoflurane is an inhaled agent used only under controlled anaesthesia
- A review of the knowledge-graph contraindication signals, including hypotension and malignant hyperthermia, against the label

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1200694 (sevoflurane): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200694) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

