---
layout: default
title: Norepinephrine
parent: Medium Evidence (L3-L4)
nav_order: 721
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Norepinephrine: predicted new indication Obstructive lung disease (evidence level L4). Approved use: Asthma, bronchitis, hypotensive disorder, pulmonary emphysema…"
monitor_inn: "Norepinephrine"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome", "transient ischemic attack (disease)", "food-dependent exercise-induced anaphylaxis", "anaphylaxis", "tracheal stenosis"]
---

# Norepinephrine
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

## Norepinephrine: From Asthma and Hypotensive Disorders to Obstructive Lung Disease
{: .text-alpha }

## One-Sentence Summary

Norepinephrine is an adrenergic vasopressor, listed in the knowledge graph for asthma, bronchitis, emphysema, bronchiectasis and hypotensive disorder.
The TxGNN model predicts it may be effective for **obstructive lung disease**, but there is **1 clinical trial** (only tangentially related) and **no direct therapeutic literature** supporting this direction, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, hypotensive disorder, pulmonary emphysema, bronchiectasis (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, norepinephrine acts on adrenergic receptors: alpha-1 receptors drive vasoconstriction, and beta receptors contribute to cardiac stimulation and some airway effects. It also takes part in airway sympathetic and neuroimmune signalling.

The model likely links the drug to obstructive lung disease because its listed indications (asthma, bronchitis, emphysema, bronchiectasis) are all airway or lung conditions. The retrieved literature describes airway innervation, adrenergic signalling in asthma and COPD, and norepinephrine as a stress or prognostic marker. None of it shows norepinephrine working as a treatment.

The rationale is weak. Norepinephrine is a non-selective vasoconstrictor given by infusion, and selective beta-2 agonists are safer and better targeted for airway disease. The prediction therefore looks like a knowledge-graph association rather than a credible new therapeutic use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular function, exercise and skeletal muscle feedback in hypertension rehabilitation. It does not test norepinephrine as a treatment for lung disease (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Review | Pneumologie | Airway nerves, including norepinephrine-releasing sympathetic fibres, contribute to airway narrowing in asthma and COPD |
| [29696025](https://pubmed.ncbi.nlm.nih.gov/29696025/) | 2018 | Review | Front Immunol | Adrenergic signalling at the interface of allergic asthma and viral infections |
| [41601146](https://pubmed.ncbi.nlm.nih.gov/41601146/) | 2026 | Review | Ann Med | Neuroimmune circuits in respiratory disease and possible therapeutic targets |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Review | Crit Care Clin | Catecholamines (norepinephrine, epinephrine, dopamine) in critical care |
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | Cohort | Am J Physiol Heart Circ Physiol | Muscle alpha-adrenergic responsiveness during exercise in COPD patients |
| [11099681](https://pubmed.ncbi.nlm.nih.gov/11099681/) | 2000 | Cohort | Am J Med | Hormones including norepinephrine and blood pressure in COPD with acute respiratory failure |
| [3966494](https://pubmed.ncbi.nlm.nih.gov/3966494/) | 1985 | Cohort | Am J Med | Hypoxaemia and sodium and water excretion in chronic obstructive lung disease |
| [35870527](https://pubmed.ncbi.nlm.nih.gov/35870527/) | 2022 | Panel study | Environ Pollut | Stress hormones and air pollution exposure in people with and without COPD |
| [40870471](https://pubmed.ncbi.nlm.nih.gov/40870471/) | 2025 | Narrative review | Medicina (Kaunas) | Anxiety and depression as comorbidities in COPD |
| [10951892](https://pubmed.ncbi.nlm.nih.gov/10951892/) | 2000 | Review | Allergy Asthma Proc | Stress, neuroendocrine mediators and immune regulation in asthma |

No randomised controlled trial of norepinephrine in obstructive lung disease was found.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16622P | Noradrenaline Sintetica Concentrate for Solution for Infusion 1 mg/ml | Infusion, solution concentrate | Not listed in the data compiled for this report |
| SIN16733P | Norepinephrine Kalceks Concentrate for Solution for Infusion 1 mg/ml | Infusion, solution concentrate | Not listed in the data compiled for this report |
| SIN05754P | Levophed Injection 1 mg/ml | Injection | Not listed in the data compiled for this report |
| SIN15593P | Noradrenaline Aguettant 1 mg/ml Concentrate for Solution for Infusion | Infusion, solution concentrate | Not listed in the data compiled for this report |

All four products are injectable single-ingredient products with valid status. There are no inhaled or oral formulations on the Singapore market.

---

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease relationships, not label text): hypertensive disorder, hypertension and thrombotic disease.
- **Drug interactions**: 70 interactions were identified, and the 20 reviewed are all Moderate. They mainly involve antidiabetic drugs: acarbose, metformin, pioglitazone, repaglinide, insulins (aspart, degludec, detemir), GLP-1 agonists (semaglutide, dulaglutide, albiglutide), DPP-4 inhibitors (sitagliptin, linagliptin, saxagliptin, alogliptin) and SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin). Phentermine and diethylpropion also appear. Blood glucose monitoring is advisable when these are combined with norepinephrine.

Please refer to the package insert for warnings and contraindications. The label information was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.84%), but the evidence is only indirect: reviews and observational studies on adrenergic physiology in COPD and asthma, and one unrelated Phase 1 trial. Norepinephrine is a non-selective vasoconstrictor with cardiovascular risks, and safer selective airway drugs already exist. No data show a therapeutic benefit in obstructive lung disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, to complete safety screening (currently a blocking gap)
- Detailed mechanism of action data from DrugBank
- Any direct preclinical or clinical evidence of benefit in obstructive lung disease, and a justification for an injectable route in a chronic airway condition

**Other predicted indications, for reference:**
- **Anaphylaxis** (score 98.30%, evidence level L4): reviews and case reports describe norepinephrine as a second-line option in epinephrine-refractory anaphylactic shock. This is already accepted critical-care practice rather than new repurposing, though the role could be studied as a research question.
- **COPD** (score 98.50%, L4): the evidence is indirect and observational, with no therapeutic support.
- **Respiratory malformation, Rienhoff syndrome, asthma-related traits, food-dependent exercise-induced anaphylaxis, tracheal stenosis, interstitial emphysema** (L5): no credible mechanistic or clinical support.
- **Transient ischaemic attack** (L5): only animal and pathophysiology studies, and induced vasoconstriction or hypertension could be harmful in cerebrovascular disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

