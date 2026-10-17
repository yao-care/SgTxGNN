---
layout: default
title: Dronedarone
parent: Medium Evidence (L3-L4)
nav_order: 355
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Dronedarone: predicted new indication Stroke disorder (evidence level L4). Approved use: Atrial fibrillation"
monitor_inn: "Dronedarone"
predicted_indications: ["stroke disorder", "obsolete susceptibility to ischemic stroke", "ABri amyloidosis", "cerebrovascular disorder", "brain stem infarction", "sick sinus syndrome 2, autosomal dominant", "duodenal obstruction", "cerebral artery occlusion", "sarcoglycanopathy", "Wildervanck syndrome"]
---

# Dronedarone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Dronedarone: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dronedarone is an antiarrhythmic drug originally used to treat atrial fibrillation (AF).
The TxGNN model predicts it may be effective for **stroke disorder**,
but there are currently **no registered clinical trials** and only **indirect literature** (20 publications, mostly AF reviews, guidelines and comparative antiarrhythmic studies) supporting this direction. The link is most likely driven by the AF–stroke association rather than a proven independent therapeutic effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (the Singapore licence text carries no approved indication; the original indication comes from the knowledge graph) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dronedarone is a multichannel-blocking antiarrhythmic (it inhibits sodium, potassium and calcium currents) and is structurally related to amiodarone, but it is non-iodinated and has a shorter half-life. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description comes from the published literature.

Stroke is a major downstream complication of AF. Any link between dronedarone and stroke is therefore indirect: controlling rhythm may lower the risk of cardioembolic stroke. A post hoc analysis of the ATHENA trial suggested a lower stroke rate with dronedarone in paroxysmal or persistent AF, and a laboratory study reported anticoagulant and antiplatelet effects independent of its antiarrhythmic action. A preclinical review also describes possible protective effects on ischaemia/reperfusion injury in heart and brain.

There are important counter-signals. The PALLAS trial showed excess cardiovascular events in high-risk permanent AF, which limits any stroke-prevention rationale. The very high TxGNN score most likely reflects the AF–stroke association in the knowledge graph rather than an independent effect on stroke. The other nine predictions (for example obsolete susceptibility to ischaemic stroke, ABri amyloidosis, duodenal obstruction) have no trial or literature evidence and are mostly knowledge-graph artefacts; only cerebrovascular disorder (L3, indirect, AF-confounded evidence) has any supporting literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | N Engl J Med | Dronedarone in high-risk permanent AF; tested whether it reduces major vascular events (the trial showed excess cardiovascular events) |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | Secondary analysis of RCT | Clin Res Cardiol | Safety and efficacy of amiodarone and dronedarone for early rhythm control in EAST-AFNET 4 |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Post hoc RCT analysis | Eur J Heart Fail | ATHENA post hoc analysis in AF with preserved or mildly reduced ejection fraction heart failure |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Dronedarone vs sotalol in antiarrhythmic-drug-naive veterans with AF |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | Approval and efficacy of dronedarone; a post hoc ATHENA analysis suggested decreased stroke risk |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic study | Atherosclerosis | Dronedarone showed anticoagulant and antiplatelet effects independent of its antiarrhythmic action |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Retrospective cohort | J Atr Fibrillation | Risk of CV events, stroke, heart failure, interstitial lung disease and liver injury: dronedarone vs amiodarone and other antiarrhythmics |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | Overview of AF management, including stroke risk stratification and anticoagulation |
| [22433576](https://pubmed.ncbi.nlm.nih.gov/22433576/) | 2012 | Guideline | Can J Cardiol | Canadian Cardiovascular Society 2012 AF guideline update on stroke prevention and rate/rhythm control |
| [37777298](https://pubmed.ncbi.nlm.nih.gov/37777298/) | 2023 | Review | Am J Cardiol | Rate versus rhythm control in AF |

Additional literature found for the related prediction "cerebrovascular disorder":

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22149318](https://pubmed.ncbi.nlm.nih.gov/22149318/) | 2011 | Meta-analysis (post hoc ATHENA) | Am J Cardiovasc Drugs | Dronedarone and stroke incidence in paroxysmal or persistent AF; a post hoc analysis suggested reduced stroke risk |
| [22366819](https://pubmed.ncbi.nlm.nih.gov/22366819/) | 2012 | Preclinical review | Cardiovasc Drugs Ther | Pleiotropic effects of dronedarone on ischaemia/reperfusion injury in heart and brain |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohort | BMC Med | Concomitant DOAC and interacting antiarrhythmic use and stroke/bleeding risk in non-valvular AF |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13849P | MULTAQ® Film-coated Tablet 400mg | Film-coated tablet (oral) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, liver failure, potassium deficiency disease, atrioventricular block, sick sinus syndrome, familial sick sinus syndrome.
- **Clinical caution**: the literature notes that dronedarone is not suitable in permanent AF or in decompensated or recent heart failure because of excess cardiovascular events (PALLAS).
- **Drug Interactions**: 100 interactions were recorded; the first 20 reviewed include these **Major** ones: hydrocortisone, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), loperamide, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes) and dolasetron. **Moderate** ones include famotidine, alvimopan, aprepitant, dexamethasone, bisacodyl, budesonide, cimetidine, saxagliptin and castor oil. Many of these likely relate to QT prolongation or electrolyte disturbance. Interaction with direct oral anticoagulants is also a concern for any stroke-prevention use.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The stroke prediction rests on the AF–stroke association, with no registered trials and no studies of dronedarone as a stroke therapy. Dronedarone's own safety profile (PALLAS, heart failure, QT and conduction risks) and the lack of any stroke-specific evidence argue against advancing it now.

**To proceed, the following is needed:**
- The package insert warnings and contraindications from the HSA (currently missing, a blocking gap)
- Detailed mechanism-of-action data (for example from DrugBank)
- Prospective or well-designed observational data on stroke outcomes as a primary endpoint, separating dronedarone's effect from AF rhythm control and anticoagulation
- A safety analysis for patients on DOACs and for those with heart failure or permanent AF
- Clarification of the approved indication text for the Singapore licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

