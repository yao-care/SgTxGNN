---
layout: default
title: Theophylline
parent: Low Evidence (L5)
nav_order: 980
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma, bronchitis, emphysema and other chronic lung diseases"
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis", "respiratory malformation", "massive neonatal aspiration syndrome"]
---

# Theophylline
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

# Theophylline: From Asthma and Chronic Lung Disease to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established bronchodilator, originally used for asthma, bronchitis, emphysema and other chronic airway diseases.
The TxGNN model predicts it may be effective for **thrombotic disease**, but **no clinical trials** and **no literature that tests theophylline as an antithrombotic** were found, so the prediction currently rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, emphysema and other chronic lung diseases (the registry lists no approved-indication text, so these come from the knowledge-graph indication list) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the compiled data. Theophylline is generally described as a non-selective phosphodiesterase (PDE) inhibitor and adenosine receptor antagonist. Its efficacy in airway disease is well established.

The mechanistic link to thrombosis is plausible but weak. PDE inhibition raises cAMP in platelets, which could in theory reduce platelet aggregation. However, adenosine itself inhibits platelets, so blocking adenosine receptors could counteract this effect. The two actions may therefore cancel each other.

The retrieved literature does not resolve this question. Most papers concern platelet biomarkers, blood-sample handling, pharmacokinetics of another drug (ticlopidine), or a theophylline detection sensor. None tests theophylline as a treatment for thrombosis. The high TxGNN score is a prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the retrieved publications is an RCT or tests theophylline for thrombosis. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clin Pharmacokinet | Pharmacokinetics of ticlopidine, an antiplatelet drug. Does not involve theophylline. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Role of prostaglandins and platelets in atherosclerosis. Prostacyclin acts by raising platelet cAMP, the pathway PDE inhibitors also influence. |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | Gen Pharmacol | Milrinone, another PDE inhibitor, reduced human platelet aggregation and interacted with adenosine. Does not test theophylline. |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Not classified | Minerva Cardioangiol | Theophylline-nicotinate derivative in chronic obliterating peripheral arteriopathy. No abstract available. |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | Not classified | Cardiologia Pratica | Cardiocirculatory effects of a theophylline nicotinate ester in cerebral and peripheral angiopathies. No abstract available. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Assay method | Br J Haematol | Platelet factor 4 radioimmunoassay. Theophylline is only an additive in the anticoagulant used for sample collection. |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Laboratory method | PLoS One | Optimized plasma preparation for platelet-stored molecules. Not a treatment study. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method (sensor) | Anal Chim Acta | Electrochemical sensor for detecting theophylline. Unrelated to thrombosis. |

## Singapore Market Information

There are 8 valid single-ingredient registrations in Singapore (no combination products, none cancelled). The registry provides no approved-indication text for any of them. The first 5 are shown below.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN11399P | NUELIN-SR 125 TABLET | Tablet |
| SIN10679P | NUELIN-SR 250 TABLET | Tablet |
| SIN03139P | THEOPHYLLINE TABLETS 100 mg | Tablet |
| SIN09668P | APO-THEO LA TABLET 200 mg | Tablet |
| SIN10158P | APO-THEO LA TABLET 100 mg | Tablet |

Other registered forms include a film-coated tablet (THEOLIN SR 250 mg), a syrup (NUELIN SYRUP) and APO-THEO LA 300 mg tablets.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not package-insert text)**: hypertension, liver failure and liver disease, epilepsy, anxiety and other mental disorders, porphyria, kidney disease, gallbladder disease, thrombocytopenia, neutropenia and agranulocytosis, hypothyroidism, peptic ulcer disease, open-angle glaucoma, diabetes mellitus and diabetic ketoacidosis, and benign prostatic hyperplasia. Thrombocytopenia is relevant to any thrombosis use.
- **Drug Interactions**: 100 interactions were identified. The only **Major** interaction among those displayed is with **bupropion**. **Moderate** interactions include:
  - H2 blockers and proton-pump inhibitors: famotidine, ranitidine, cimetidine, omeprazole and rabeprazole
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide and triamcinolone
  - Antibiotics: clarithromycin, doxycycline, tetracycline and minocycline
  - Bowel-preparation agents and activated charcoal
  
  Ephedrine is a **Minor** interaction.
- **Additional note**: Theophylline has a narrow therapeutic index and needs drug-level monitoring in its established uses.

Please refer to the package insert for key warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or relevant studies. The mechanism is conflicting, since PDE inhibition may reduce platelet aggregation while adenosine antagonism may oppose it. Theophylline's narrow therapeutic index and extensive interactions add risk without any demonstrated benefit.

**To proceed, the following is needed:**
- Mechanistic data on whether theophylline's net effect on platelet function is antithrombotic, such as in-vitro platelet aggregation studies
- Preclinical or early clinical evidence testing theophylline against thrombosis
- Detailed mechanism-of-action data and package-insert warnings and contraindications
- A safety plan covering therapeutic drug monitoring, thrombocytopenia and interactions with antiplatelet or anticoagulant drugs

Among the other predicted indications for theophylline, allergic rhinitis (a Phase 2 trial and a nasal challenge study) and obstructive lung disease have more supporting evidence. Obstructive lung disease overlaps the drug's existing uses, so it is not true repurposing. These may be better priorities for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

