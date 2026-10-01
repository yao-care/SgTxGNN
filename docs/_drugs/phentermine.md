---
layout: default
title: Phentermine
parent: Low Evidence (L5)
nav_order: 777
evidence_level: L5
indication_count: 10
---

# Phentermine
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

# Phentermine: From Obesity (Weight Management) to Hypervitaminosis

## One-Sentence Summary

Phentermine is a sympathomimetic amine (a noradrenergic appetite suppressant) used for weight management. The Singapore licence records supplied do not state an approved indication.
The TxGNN model's top-ranked prediction is **hypervitaminosis** (score 99.57%), but there are **0 clinical trials** and **0 publications** behind it, and no plausible mechanism links the two.
Among the other predictions, only **fatty liver disease** has meaningful support (**2 clinical trials** and **15 publications**), and that support is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA licence data; the pack describes phentermine's use as weight loss (obesity) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Phentermine is known as a noradrenergic appetite suppressant, and its use in weight management is established.

The link to hypervitaminosis is weak. Phentermine has no known role in vitamin metabolism or clearance. The high graph-based score (0.996) is not supported by any trial or publication, so it most likely reflects a knowledge-graph artefact rather than a real therapeutic signal.

Several other top-scoring predictions are similarly implausible:
- Proximal 16p11.2 microdeletion syndrome is associated with obesity, so the link to weight loss is speculative.
- Obsolete hypertelorism, frontorhiny and Boissel-type lethal polymalformative syndrome are craniofacial or congenital malformation conditions with no pharmacological rationale.

The most credible candidate is **fatty liver disease** (rank 7, score 77.7%, evidence level L3, "Research Question"). Phentermine promotes weight loss, and weight loss lowers intrahepatic fat in obesity-associated MASLD/NAFLD. Any liver benefit is therefore probably secondary to weight loss, not a liver-specific mechanism.

---

## Clinical Trial Evidence

For the top-ranked prediction (hypervitaminosis): Currently no related clinical trials registered.

For fatty liver disease, the most evidence-supported alternative prediction:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03849729](https://clinicaltrials.gov/study/NCT03849729) | Phase 4 | Completed | 92 | Phentermine to reduce intrahepatic fat, adipose tissue and postoperative complications in bariatric surgery patients. Results and randomisation design are not in the provided data. |
| [NCT07058155](https://clinicaltrials.gov/study/NCT07058155) | Phase 4 | Recruiting | 70 | TIPS with interval metabolic surgery for advanced liver disease with portal hypertension and severe obesity. Focus is surgical, so phentermine's role is unclear. |

---

## Literature Evidence

For the top-ranked prediction (hypervitaminosis): Currently no related literature available.

For fatty liver disease (15 publications retrieved; the 8 most relevant are shown):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41025003](https://pubmed.ncbi.nlm.nih.gov/41025003/) | 2025 | Systematic review/Meta-analysis | World J Gastroenterol | Efficacy and safety of anti-obesity drugs in MASLD/MASH; notes safety and hepatotoxicity concerns given altered hepatic metabolism |
| [32153507](https://pubmed.ncbi.nlm.nih.gov/32153507/) | 2020 | Systematic review | Front Endocrinol | Hepatic effects of weight-loss drugs; GLP-1 agonists are best studied |
| [35501557](https://pubmed.ncbi.nlm.nih.gov/35501557/) | 2022 | Review | Curr Obes Rep | Effect of anti-obesity medications on NAFLD, focusing on hepatic histology |
| [36120448](https://pubmed.ncbi.nlm.nih.gov/36120448/) | 2022 | Review | Front Endocrinol | Choice of anti-obesity agent in NAFLD; limited data |
| [30502373](https://pubmed.ncbi.nlm.nih.gov/30502373/) | 2019 | Review | Metabolism | Obesity and NAFLD from pathophysiology to therapeutics |
| [36059008](https://pubmed.ncbi.nlm.nih.gov/36059008/) | 2022 | Drug approval review | Paediatr Drugs | Phentermine/topiramate (Qsymia) pediatric approval; NASH listed among development targets |
| [35430025](https://pubmed.ncbi.nlm.nih.gov/35430025/) | 2022 | Expert roundtable | J Clin Lipidol | Obesity, diabetes and liver disease in relation to cardiovascular risk; discusses phentermine/topiramate |
| [39604664](https://pubmed.ncbi.nlm.nih.gov/39604664/) | 2025 | Cohort | Dig Dis Sci | Mood or anxiety disorders did not affect weight-management success in MASLD |

Two other predictions have a small amount of literature, both of which argue against a benefit from phentermine:
- **Postural orthostatic tachycardia syndrome:** one 2016 case report ([26968177](https://pubmed.ncbi.nlm.nih.gov/26968177/)) shows stimulant medication can mimic or aggravate POTS tachycardia, which points to an adverse effect, not a therapeutic one.
- **Migraine disorder:** the literature is confounded by topiramate, the migraine-active component of the phentermine/topiramate combination. Phentermine appears only as a co-component or as an add-on in one case report ([25911503](https://pubmed.ncbi.nlm.nih.gov/25911503/)).

---

## Singapore Market Information

The approved indication text is empty in all four records, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN05315P | PANBESY CAPSULE 15 MG | Capsule | OSMOPHARM SA / Tjoapack Netherlands B.V. |
| SIN05113P | PANBESY CAPSULE 30 mg | Capsule | OSMOPHARM SA / Tjoapack Netherlands B.V. |
| SIN01256P | DUROMINE CAPSULE 30 mg | Capsule | Douglas Manufacturing Ltd |
| SIN01255P | DUROMINE CAPSULE 15 mg | Capsule | Douglas Manufacturing Ltd |

All products are oral capsules.

---

## Safety Considerations

Please refer to the package insert for safety information. The HSA package insert warnings and contraindications have not been retrieved, and no drug interaction records were found.

From the retrieved literature only:
- **Cardiovascular:** stimulants such as phentermine may aggravate tachycardia and orthostatic symptoms (POTS case report).
- **Heart valve disorder:** it has been reported with the fenfluramine plus phentermine combination.
- **Liver disease:** safety and hepatotoxicity concerns apply to anti-obesity medications in MASLD/MASH.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hypervitaminosis, is a model score only. It has no trials, no literature and no plausible mechanism. The other high-scoring predictions are also unsupported. Fatty liver disease is the only indication worth pursuing, as a research question, and any benefit is likely secondary to weight loss.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications, since safety screening cannot proceed without them (blocking gap)
- Phentermine's mechanism of action data from DrugBank
- The results and design of NCT03849729. If it was a randomised controlled trial with a positive hepatic fat endpoint, the fatty liver evidence could move from L3 to L2.
- The Singapore approved indication text for the four registrations
- Confirmation that cardiovascular safety in patients with fatty liver disease has been considered

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

