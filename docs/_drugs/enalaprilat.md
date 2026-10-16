---
layout: default
title: Enalaprilat
parent: Low Evidence (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Enalaprilat: predicted new indication Primary hereditary glaucoma . Highest-evidence candidate: acute pulmo… (evidence level L5). Approved use: Hypertensive disorder, hypertension, congestive heart f…"
---

# Enalaprilat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Enalaprilat: From Hypertension and Heart Failure to Acute Pulmonary Heart Disease

## One-Sentence Summary

Enalaprilat is an intravenous ACE inhibitor, originally used for hypertensive disorders and heart failure.
The TxGNN model predicts it may be effective for **acute pulmonary heart disease**, supported by **0 registered clinical trials** and **13 publications** (only indirectly relevant; most concern acute left-heart failure, pulmonary edema, or hypertensive crisis rather than acute cor pulmonale).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure, heart failure (the Singapore licence record contains no approved indication text) |
| Predicted New Indication | Primary hereditary glaucoma (rank 1, prediction only). Highest-evidence candidate: acute pulmonary heart disease (rank 3), which is the focus of this report |
| TxGNN Prediction Score | 99.09% (primary hereditary glaucoma); 98.32% (acute pulmonary heart disease) |
| Evidence Level | L3 (acute pulmonary heart disease); L5 for the rank 1 prediction |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold (acute pulmonary heart disease is classed as a research question) |

> Note: The top-ranked TxGNN prediction (primary hereditary glaucoma) has no trials or literature, so this report focuses on acute pulmonary heart disease, the highest-ranked prediction with meaningful supporting literature.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, enalaprilat is the active diacid metabolite of enalapril and the intravenous form of an ACE inhibitor. It blocks angiotensin-converting enzyme (ACE), reducing angiotensin II-mediated vasoconstriction and thereby lowering preload and afterload.

The retrieved literature shows haemodynamic benefit of IV enalaprilat in acute or refractory heart failure, acute pulmonary oedema and hypertensive crisis. This overlaps with the physiology of acute heart strain, which is why the model links the drug to acute pulmonary heart disease.

The match is indirect, however. The evidence concerns acute left-heart failure and hypertensive emergencies, not acute cor pulmonale (for example from pulmonary embolism). Only the title and abstract-level information was available, so the strength of the link cannot be confirmed.

Other predictions are weaker. Glaucoma (ranks 1–2) rests on a hypothesised ocular renin-angiotensin system, but enalaprilat is polar and IV-only with poor ocular penetration. The hair disorders (ranks 4 and 6) have no plausible mechanism and are likely knowledge-graph artefacts. Chronic kidney disease (rank 7) is mechanistically plausible for the drug class, but the enalaprilat-specific evidence is mostly pharmacokinetic or preclinical.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Prioritised for acute pulmonary heart disease (RCTs first, then reviews and other studies):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8822986](https://pubmed.ncbi.nlm.nih.gov/8822986/) | 1996 | RCT | Circulation | Placebo-controlled, double-blind study of a single 2-hour IV infusion of enalaprilat (1 mg) in acute cardiogenic pulmonary oedema; evaluated efficacy and safety, including renal function and electrolytes |
| [10393397](https://pubmed.ncbi.nlm.nih.gov/10393397/) | 1999 | RCT | Cardiology | Bolus vs continuous low-dose IV enalaprilat in 20 patients with acutely decompensated congestive heart failure; compared haemodynamic and oxygenation effects |
| [39799613](https://pubmed.ncbi.nlm.nih.gov/39799613/) | 2025 | Review | Am J Emerg Med | Emergency medicine update on sympathetic crashing acute pulmonary oedema (SCAPE) in heart failure exacerbation |
| [9704248](https://pubmed.ncbi.nlm.nih.gov/9704248/) | 1998 | Review | Drug Safety | Comparative tolerability of hypertensive crisis treatments |
| [11836639](https://pubmed.ncbi.nlm.nih.gov/11836639/) | 2002 | Review | Int J Mol Med | Review of pulmonary capillary endothelium-bound ACE activity and its measurement in humans |
| [8205829](https://pubmed.ncbi.nlm.nih.gov/8205829/) | 1994 | Cohort | Crit Care Med | Before-after trial of IV enalaprilat infusion in critically ill patients with intractable heart failure after myocardial infarction |
| [8383028](https://pubmed.ncbi.nlm.nih.gov/8383028/) | 1993 | Cohort | Clin Cardiol | 1.25 mg IV enalaprilat in 20 elderly patients with severe CHF and mitral regurgitation; reduced systemic vascular resistance |
| [7722147](https://pubmed.ncbi.nlm.nih.gov/7722147/) | 1995 | Cohort (animal) | J Am Coll Cardiol | Effect of low-dose aspirin on the haemodynamic response to enalaprilat in a canine model of severe heart failure |
| [8395876](https://pubmed.ncbi.nlm.nih.gov/8395876/) | 1993 | Preclinical | Cardiovasc Drugs Ther | Haemodynamic response to IV dobutamine, nitroprusside, enalaprilat and digoxin in a canine chronic heart failure model |
| [8205828](https://pubmed.ncbi.nlm.nih.gov/8205828/) | 1994 | Not classified | Crit Care Med | Cardiopulmonary actions of IV enalaprilat in hypertensive trauma patients |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14265P | KORANDIL TABLET 20MG (Remedica Ltd.) | Tablet | Not stated in the registration record |

> Note: The only registered Singapore product is an oral tablet. The IV-only enalaprilat form that the literature studied is not represented, which matters for acute-care use.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: angioedema, including acquired angioedema, renin-angiotensin-aldosterone system blocker-induced angioedema, non-histaminic angioedema, hereditary angioedema, and hereditary angioedema with C1 inhibitor deficiency.
- **Drug Interactions**: The only record is the pharmacological target, angiotensin-converting enzyme (ACE). It is not a drug-drug interaction, and no specific interacting drugs were identified.
- **Related literature signals**: Enalaprilat accumulates in renal failure (PMID 11881130), so dose adjustment is needed. The first dose in heart failure may cause a considerable fall in blood pressure (PMID 10393397). For the renovascular hypertension prediction, ACE inhibitors carry a risk of acute renal function decline in bilateral renal artery stenosis or a solitary kidney.

For other warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold** (acute pulmonary heart disease: research question)

**Rationale:**
The highest-ranked predictions (glaucoma, hair disorders) are prediction-only with weak or implausible mechanisms. Acute pulmonary heart disease has the most supporting literature, including two small RCTs, but it addresses acute left-heart failure and pulmonary oedema, not acute cor pulmonale. The indirect evidence, absence of registered trials, and missing safety and mechanism data do not support advancing yet.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Full-text review of PMID 8822986 and PMID 10393397 to judge applicability to acute right-heart strain or pulmonary embolism
- Clarification of route compatibility, since the Singapore product is an oral tablet while the evidence is for IV use
- Safety plan covering angioedema, hypotension, and renal impairment, including renal artery stenosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

