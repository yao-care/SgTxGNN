---
layout: default
title: Diltiazem
parent: Medium Evidence (L3-L4)
nav_order: 331
evidence_level: L4
indication_count: 10
---

# Diltiazem
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

# Diltiazem: From Hypertension and Arrhythmia to Cerebrovascular Disorder

## One-Sentence Summary

Diltiazem is a calcium channel blocker originally used for hypertension, atrial fibrillation, Prinzmetal angina and ventricular tachycardia.
The TxGNN model predicts it may be effective for **cerebrovascular disorder**, but the supporting evidence is weak: **1 clinical trial** (with no demonstrated link to diltiazem) and **20 publications**, mostly general reviews and drug-interaction studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, Prinzmetal angina, ventricular tachycardia (the Singapore licence records contain no indication text) |
| Predicted New Indication | Cerebrovascular disorder (the top-ranked prediction, obsolete susceptibility to ischemic stroke, has no supporting evidence; this report focuses on the highest-ranked prediction that has some evidence) |
| TxGNN Prediction Score | 97.63% (cerebrovascular disorder); the top-ranked prediction scored 99.08% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, diltiazem is an L-type calcium channel blocker. Its efficacy in hypertension and in heart rate and rhythm control is established, and mechanistically it may be applicable to cerebrovascular disease through blood pressure control and effects on vascular tone.

The link to cerebrovascular disorder is indirect. Blood pressure management is relevant to stroke prevention, and an old animal study (PMID 4056906) examined verapamil and diltiazem in acute stroke in cats. However, lowering blood pressure or dilating vessels during acute infarction could also be harmful. Other predictions in the list illustrate the limits of the model output:

- **Obsolete susceptibility to ischemic stroke and brain stem infarction**: no trials or literature; vasodilation in acute infarction may be harmful.
- **Obsolete bundle branch block**: a safety concern rather than an opportunity, since diltiazem slows AV nodal conduction.
- **Malignant hypertensive renal disease and malignant renovascular hypertension**: plausible, but they sit close to the existing hypertension use and look more like an extension of the approved use than a new indication.
- **Pulmonary hypertension (lung disease/hypoxia)**: preclinical papers describe calcium-dependent hypoxic pulmonary vasoconstriction, but calcium channel blockers are generally not recommended here because they can worsen gas exchange.
- **ABri amyloidosis and Braddock syndrome**: no plausible mechanistic link; likely graph-association artifacts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03529149](https://clinicaltrials.gov/study/NCT03529149) | Phase 4 | Unknown | 90 | Transcranial Doppler (TCD)-guided blood pressure control after endovascular thrombectomy; the data do not show that diltiazem is a study arm, so the link to this drug is weak and indirect |

## Literature Evidence

Most of the publications are indirect (atrial fibrillation reviews, drug-interaction studies, calcium channel blocker adverse effects). None is a randomised trial of diltiazem in cerebrovascular disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4056906](https://pubmed.ncbi.nlm.nih.gov/4056906/) | 1985 | Preclinical | J Neurosurg | Verapamil and diltiazem infusions in a cat model of acute middle cerebral artery occlusion (the most directly relevant item) |
| [11002856](https://pubmed.ncbi.nlm.nih.gov/11002856/) | 2000 | Review | Drugs | Calcium antagonists lower blood pressure effectively; morbidity and mortality trials needed to show reduction of vascular injury |
| [7903243](https://pubmed.ncbi.nlm.nih.gov/7903243/) | 1993 | Review | Eur Heart J | Beta-blockers and calcium channel blockers in acute myocardial infarction |
| [40326046](https://pubmed.ncbi.nlm.nih.gov/40326046/) | 2026 | Meta-analysis | Ann Pharmacother | Diltiazem or verapamil with DOACs; raises DOAC levels and may raise bleeding risk, with contradictory findings across studies |
| [41730211](https://pubmed.ncbi.nlm.nih.gov/41730211/) | 2026 | Cohort | Ann Intern Med | Bleeding risk in AF patients taking apixaban or rivaroxaban with diltiazem versus metoprolol |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohort | BMC Med | DOACs with interacting antiarrhythmic drugs and risk of stroke and bleeding in non-valvular AF |
| [40670662](https://pubmed.ncbi.nlm.nih.gov/40670662/) | 2025 | Systematic review | Eur J Clin Pharmacol | Observational studies of DOAC and antiarrhythmic co-use |
| [35861836](https://pubmed.ncbi.nlm.nih.gov/35861836/) | 2022 | Observational | J Am Heart Assoc | Diltiazem with DOACs and bleeding risk in AF across kidney function levels |
| [17309423](https://pubmed.ncbi.nlm.nih.gov/17309423/) | 2007 | Review | Med J Aust | AF management; verapamil and diltiazem control heart rate better than digoxin during exercise |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with thalamic hemorrhagic stroke |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06791P | HERBESSER 90 SR CAPSULE 90 mg | Capsule | Not stated in the available record |
| SIN10061P | HERBESSER R200 CAPSULES 200 mg | Capsule | Not stated in the available record |
| SIN00428P | HERBESSER TABLET 30 mg | Tablet | Not stated in the available record |
| SIN10062P | HERBESSER R100 CAPSULES 100 mg | Capsule | Not stated in the available record |
| SIN00430P | HERBESSER 60 TABLET 60 mg | Tablet | Not stated in the available record |

All five licences are valid single-ingredient oral products.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: conditions linked to contraindication or caution include aortic stenosis, hypotensive disorder, hypertrophic cardiomyopathy, atrioventricular block, sick sinus syndrome, Wolff-Parkinson-White syndrome, Lown-Ganong-Levine syndrome, ventricular tachycardia, kidney disease, liver disease, angioedema (including hereditary forms), neutropenia and agranulocytosis. These come from graph edges and should be checked against the package insert.
- **Drug Interactions**: 100 interactions were recorded. Among those listed, the major one is **loperamide**. Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), pioglitazone, bupropion, aprepitant, morphine, aspirin, canagliflozin and several calcium salts. Published studies also show diltiazem inhibits CYP3A4 and P-glycoprotein, which can raise DOAC levels and may increase bleeding risk.
- **Relevance to the predicted indication**: lowering blood pressure or vasodilation in acute cerebral infarction could be harmful, and conduction-system effects matter in patients with conduction disease.

Please refer to the package insert for key warnings and labelled contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score with no supportive human evidence. The only trial does not show diltiazem as an intervention, and the literature is indirect. The higher-ranked predictions have no evidence at all, and several are obsolete terms, close extensions of the existing hypertension use, or carry safety concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA
- Mechanism of action data (e.g. from DrugBank)
- Clinical studies in which diltiazem is the actual intervention in cerebrovascular disease (RCTs or well-designed observational studies)
- Safety assessment of blood pressure lowering and conduction effects in acute stroke
- Review of the interacting drugs, especially anticoagulants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

