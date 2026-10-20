---
layout: default
title: Magnesium Oxide
parent: Medium Evidence (L3-L4)
nav_order: 630
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Magnesium Oxide: predicted new indication Calcium-alkali syndrome (evidence level L4). Approved use: Osteoporosis, postmenopausal osteoporosis, constipation, dyspepsia…"
monitor_inn: "Magnesium oxide"
predicted_indications: ["calcium-alkali syndrome", "primary bone dysplasia with defective bone mineralization", "gastroduodenitis", "potassium deficiency disease", "digitalis poisoning", "stomach disease", "hypophosphatemia (disease)", "autosomal dominant neovascular inflammatory vitreoretinopathy", "duodenogastric reflux"]
---

# Magnesium Oxide
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

# Magnesium Oxide: From Osteoporosis and Dyspepsia to Calcium-Alkali Syndrome

## One-Sentence Summary

Magnesium oxide is an oral magnesium and antacid agent, originally used for conditions such as osteoporosis, constipation and dyspepsia.
The TxGNN model predicts it for **calcium-alkali syndrome**, with **0 clinical trials** and **1 publication** (a case report) currently available.
That single report describes calcium-alkali syndrome as an **adverse effect** of magnesium oxide, so the prediction most likely reflects a causal link rather than a treatment opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis, postmenopausal osteoporosis, constipation, dyspepsia, hypercalcemia disease, nephrocalcinosis, phosphorus metabolism disease (from the knowledge graph; the Singapore licence has no indication text) |
| Predicted New Indication | Calcium-alkali syndrome |
| TxGNN Prediction Score | 97.998% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, magnesium oxide is an alkaline antacid that neutralises gastric acid and supplies magnesium, and it is often taken together with calcium and vitamin D.

This is the key problem with the prediction. The only retrieved publication (PMID 19185403) reports calcium-alkali syndrome **caused by** vitamin D plus magnesium oxide. The high score likely reflects a strong drug-disease association in the knowledge graph, not a therapeutic one. Using magnesium oxide to treat this condition would be clinically inappropriate and potentially harmful.

Other lower-ranked predictions have more plausible rationales:
- **Stomach disease, gastroduodenitis, duodenal ulcer, duodenogastric reflux**: acid neutralisation is mechanistically relevant and fits the existing dyspepsia use. Human evidence in the compiled data is limited, however.
- **Primary bone dysplasia with defective mineralisation**: linked to the original bone and mineral indications through magnesium's role in bone homeostasis, but computational only.
- **Potassium deficiency disease**: magnesium depletion accompanies hypokalaemia (for example in Gitelman syndrome), but magnesium corrects a coexisting deficit rather than the potassium deficiency itself.
- **Hypophosphatemia**: magnesium antacids bind dietary phosphate and could worsen it.
- **Digitalis poisoning**: any theoretical role applies to intravenous magnesium, not poorly absorbed oral magnesium oxide.
- **Autosomal dominant neovascular inflammatory vitreoretinopathy**: no plausible mechanistic link, likely a knowledge-graph artefact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (calcium-alkali syndrome):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19185403](https://pubmed.ncbi.nlm.nih.gov/19185403/) | 2009 | Case report | Am J Kidney Dis | Calcium-alkali syndrome caused by vitamin D and magnesium oxide administration (a safety signal, not efficacy) |

For context, the most relevant material for the gastric-related predictions (stomach disease, rank 6) includes:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11344624](https://pubmed.ncbi.nlm.nih.gov/11344624/) | 2000 | Open clinical study | Vnitrni lekarstvi | Low-dose aluminium/magnesium oxide antacid (Maalox) healed 65% (20/31) of NSAID-induced gastric erosions over 4 weeks |
| [6986240](https://pubmed.ncbi.nlm.nih.gov/6986240/) | 1980 | RCT | Dig Dis Sci | 167 patients; aluminium hydroxide/magnesium oxide was the control arm against sucralfate for preventing gastric ulcer recurrence |
| [906777](https://pubmed.ncbi.nlm.nih.gov/906777/) | 1977 | Mechanistic study | Acta Hepato-Gastroenterol | In 805 duodenal ulcer patients, magnesium did not significantly change gastric acid secretion |
| [38031523](https://pubmed.ncbi.nlm.nih.gov/38031523/) | 2023 | Veterinary clinical study | J Vet Sci | A magnesium oxide blend and equine squamous gastric disease in trotter horses (a blend, not magnesium oxide alone) |
| [31384293](https://pubmed.ncbi.nlm.nih.gov/31384293/) | 2019 | Case report | BioPsychoSocial Med | Iron deficiency anaemia associated with magnesium overuse (a safety signal) |
| [24904849](https://pubmed.ncbi.nlm.nih.gov/24904849/) | 2013 | Case report | Ann Pediatr Endocrinol Metab | Gitelman syndrome with growth hormone deficiency (indirect support for the potassium deficiency prediction) |

Many of the other retrieved articles are indirect, historical, veterinary, or unrelated (for example hamster carcinogenesis carrier dust and a stomach cancer epidemiology review).

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07893P | GERSKIN TABLET | Tablet (oral) | Not specified in the registration data |

## Safety Considerations

- **Disease-level cautions (knowledge graph, not label text)**: Contraindication links include kidney disease and impaired renal function, hypercalcemia, nephrocalcinosis, hyperparathyroidism, phosphorus metabolism disease, metabolic acidosis, nephrolithiasis, liver disease, peptic ulcer disease, diarrhoeal disease, epilepsy, bipolar disorder, sarcoidosis, hypotensive disorder, blood coagulation disease and rhabdomyolysis, among others.
- **Drug Interactions** (100 interactions found; main ones shown):
  - **Major**: Dolutegravir
  - **Moderate**: Acalabrutinib, Doxycycline, Alendronic acid, Risedronic acid, Cholecalciferol, Atazanavir, Baloxavir marboxil, Acetylsalicylic acid, Dextroamphetamine, Amphetamine
  - **Minor**: Famotidine, Ranitidine, Hydrocortisone, Dexamethasone, Triamcinolone, Atenolol, Acebutolol, Alprazolam, Axitinib
- **Case-report safety signals**: Calcium-alkali syndrome with vitamin D co-administration, and iron deficiency anaemia with magnesium overuse.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, calcium-alkali syndrome, is an adverse effect of magnesium oxide, not a treatable indication, and there are no clinical trials. The remaining predictions rest on weak or indirect evidence. Gastric acid-related conditions are the most plausible, but they largely overlap with the existing dyspepsia use and are supported mainly by veterinary and historical studies.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Removal or reclassification of calcium-alkali syndrome as a safety signal
- Human clinical evidence for gastric acid-related conditions (stomach disease, gastroduodenitis, duodenal ulcer, duodenogastric reflux) if pursuing this as a research question
- Review of renal function, calcium and vitamin D co-administration risks, and the interaction profile for any target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

