---
layout: default
title: Adenosine
parent: Low Evidence (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Adenosine: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Ventricular tachycardia"
monitor_inn: "Adenosine"
predicted_indications: ["obsolete bundle branch block", "periodic paralysis with transient compartment-like syndrome", "arrhythmogenic right ventricular cardiomyopathy", "primary hereditary glaucoma", "attention deficit hyperactivity disorder, inattentive type", "open-angle glaucoma", "specific developmental disorder", "angle-closure glaucoma"]
---

# Adenosine
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

# Adenosine: From Ventricular Tachycardia to Obsolete Bundle Branch Block

## One-Sentence Summary

Adenosine is an injectable drug originally used to treat ventricular tachycardia and related arrhythmias.
The TxGNN model predicts it may be effective for **obsolete bundle branch block** (an outdated disease term), but there are **0 clinical trials** and **0 publications** for this specific prediction.
The evidence is model prediction only, so the top-ranked prediction should be treated with caution. A more plausible follow-up is **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, which has some case-level and mechanistic support (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular tachycardia (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, adenosine slows conduction through the atrioventricular (AV) node, which is why it is used to terminate certain tachyarrhythmias.

For the top-ranked prediction, the mechanistic link is weak. Bundle branch block is a conduction defect below the AV node, so there is no clear reason adenosine would treat it. The disease term is also marked "obsolete", which suggests the high score (0.999) may be an ontology artifact rather than a real biological signal.

Other predictions have more reasonable rationales:
- **Catecholaminergic polymorphic ventricular tachycardia (CPVT, rank 2, score 99.42%)**: CPVT is triggered by catecholamines. Adenosine has antiadrenergic effects and suppresses cAMP-mediated triggered activity. One case report (PMID 18313614) describes adenosine triphosphate (a related compound, not adenosine itself) terminating bidirectional VT in a CPVT patient. This is indirect evidence.
- **Open-angle glaucoma (rank 8, score 95.12%)**: Adenosine receptors and ATP signalling are involved in regulating intraocular pressure. The evidence is preclinical or mechanistic, and intravenous adenosine is not a realistic route for a chronic eye disease. Any follow-up would involve ocular, receptor-selective agents.
- **Arrhythmogenic right ventricular cardiomyopathy (rank 5)**: Preclinical work (PMID 30568602) shows that *blocking* the adenosine A2A receptor mitigates disease. This raises a possible direction-of-effect concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (obsolete bundle branch block), nor for any of the other nine predicted indications in the data compiled for this report.

---

## Literature Evidence

No literature is available for the top-ranked prediction. The most relevant publications come from the second-ranked prediction, CPVT:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case report | Heart Rhythm | Adenosine triphosphate terminated bidirectional ventricular tachycardia in a CPVT patient (related compound, not adenosine itself) |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Review (consensus statement) | Europace | European and international consensus on pharmacological provocation testing in cardiac electrophysiology; may be relevant to diagnostic use |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | J Assoc Physicians India | Recognition and management of ventricular tachycardia in structurally normal hearts |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Review | Paediatr Anaesth | Overview of pediatric arrhythmias for anaesthesiologists |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Case series/Observational | Heart Rhythm | Abnormal repolarization after pacing in CPVT with a ryanodine receptor mutation |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclinical | Cardiovasc Res | PDE2A and PDE4B gene therapy improved heart failure and arrhythmias in mice through cAMP compartmentation |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Preclinical | Sci Transl Med | Sarcoplasmic reticulum calcium leak contributes to arrhythmia but not heart failure progression |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | Preclinical (in vitro) | J Physiol | Cardiac-neural microtissues suggest CPVT also involves sympathetic neurons |

All of this evidence is indirect, case-level or preclinical. No randomised trial supports adenosine for CPVT.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16391P | CADEN SOLUTION FOR INJECTION 6 MG / 2 ML | Injection, solution | Not stated in the data compiled for this report |
| SIN07679P | ADENOCOR INJECTION 3MG/ML | Injection | Not stated in the data compiled for this report |

Both licences are valid single-ingredient products, and both are injectables.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: The knowledge graph links adenosine to the following conditions as contraindications:
  - Respiratory: chronic obstructive pulmonary disease (including severe early-onset), asthma (intrinsic and allergic), pulmonary emphysema, respiratory failure
  - Cardiac conduction and rhythm: atrioventricular block, sick sinus syndrome (including familial)
  - Valvular and structural: aortic stenosis (including aortic valve stenosis, aortic valve disease and supravalvular aortic stenosis), mitral valve stenosis, pulmonary valve insufficiency, pericarditis
  - Ischaemic and haemodynamic: acute coronary syndrome, coronary artery disease, hypotensive disorder
  - Autonomic: autonomic nervous system disease, Horner syndrome
- **Drug Interactions**: The interaction screen found 100 records in total. Among the 20 listed, the **Major** interactions are with **cisapride, dolasetron and papaverine**. **Moderate** interactions include famotidine, clarithromycin, granisetron, levofloxacin, ondansetron and palonosetron. Many of these are drugs that prolong the QT interval, so combined use warrants rhythm monitoring.

Official package insert warnings and contraindications were not available for this report. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on a model score alone. There are no trials or literature, there is no mechanistic rationale, and the disease term is obsolete. The most credible direction in this candidate list is CPVT, but its evidence is limited to one case report with a related compound plus mechanistic papers. Adenosine's existing arrhythmia use and the knowledge-graph cardiac and respiratory contraindication signals call for caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- Review of whether "obsolete bundle branch block" maps to a current disease term; if not, drop it from consideration
- If CPVT is pursued: a focused literature review of adenosine itself, including diagnostic provocation use, and clinical input on whether any therapeutic role is plausible
- For ocular indications: assessment of ocular, adenosine-receptor-selective agents, since systemic intravenous adenosine is not suitable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

