---
layout: default
title: Magnesium Sulfate
parent: High Evidence (L1-L2)
nav_order: 625
evidence_level: L1
indication_count: 10
---

# Magnesium Sulfate
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Magnesium Sulfate: From Established Injectable and Laxative Use to Preeclampsia/Eclampsia

## One-Sentence Summary

Magnesium sulfate is registered in Singapore as an injectable and as a purgative syrup, but the registry records list no approved indication text.
The TxGNN model predicts it may be effective for **preeclampsia/eclampsia**, and about a dozen of the **50 retrieved clinical trials** directly test magnesium sulfate for this condition, alongside **20 retrieved publications**.
This is mostly a confirmation of long-standing standard of care, not a new repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (Singapore products are an injection and a purgative syrup) |
| Predicted New Indication | Preeclampsia/eclampsia |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available. Based on the retrieved literature, magnesium sulfate is an established anticonvulsant for preventing and treating eclamptic seizures. Its likely mechanisms are NMDA receptor antagonism, cerebral vasodilation and calcium channel blockade. A 1989 review (PMID 2672428) also proposes that magnesium counteracts calcium-dependent cerebral arterial constriction (vasospasm), which is thought to contribute to eclampsia.

The original indication is missing from the Singapore records, so the link to the new indication cannot be compared directly. The high score is consistent with what is already known: magnesium sulfate has been the drug of choice for eclampsia for decades. The Magpie Trial (a large placebo-controlled RCT, PMID 12057549) and a Cochrane review (PMID 21069663) support this. Both appear under the synonym entry "toxemia of pregnancy" in the evidence pack.

## Clinical Trial Evidence

Only the trials most relevant to preeclampsia/eclampsia are listed. The other retrieved trials were keyword-only matches, such as anesthesia, IVF or iodine studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | NA | Completed | 2000 | Nimodipine vs magnesium sulfate for preventing eclamptic seizures in severe preeclampsia |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | Completed | 1114 | Postpartum magnesium sulfate for 24 h vs none, after more than 8 h of treatment before delivery |
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | Postpartum protocol of 6 h vs 24 h when less than 8 h of treatment was given before delivery |
| [NCT01846156](https://clinicaltrials.gov/study/NCT01846156) | Phase 3 | Completed | 240 | Comparison of magnesium sulfate protocols in severe preeclampsia |
| [NCT04576364](https://clinicaltrials.gov/study/NCT04576364) | NA | Completed | 280 | 12-hour vs 24-hour postpartum magnesium sulfate |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | Completed | 222 | 1 g vs 2 g per hour maintenance dose in severe preeclampsia |
| [NCT02091401](https://clinicaltrials.gov/study/NCT02091401) | Phase 4 | Completed | 200 | Repeat-bolus regimen with the Springfusor pump vs continuous infusion (equivalence of serum magnesium levels) |
| [NCT00344058](https://clinicaltrials.gov/study/NCT00344058) | NA | Completed | 200 | 12-hour vs 24-hour postpartum seizure prophylaxis in mild preeclampsia |
| [NCT01408979](https://clinicaltrials.gov/study/NCT01408979) | Phase 4 | Completed | 120 | Short-course postpartum prophylaxis in severe preeclampsia |
| [NCT05283473](https://clinicaltrials.gov/study/NCT05283473) | N/A | Completed | 64 | Serum magnesium concentrations reached during therapy in severe preeclampsia (dosing/pharmacokinetics) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38865319](https://pubmed.ncbi.nlm.nih.gov/38865319/) | 2024 | RCT | PLoS One | Springfusor pump vs standard care for magnesium sulfate administration in preeclampsia and eclampsia (acceptability) |
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstet Gynecol | Efficacy, benefits and risks of magnesium sulfate seizure prophylaxis |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstet Gynecol Surv | Cerebral hemodynamics in preeclampsia and the rationale for alternatives to magnesium sulfate |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review/Opinion | Am J Obstet Gynecol | Argues magnesium sulfate is the ideal anticonvulsant in preeclampsia-eclampsia |
| [2672428](https://pubmed.ncbi.nlm.nih.gov/2672428/) | 1989 | Review | Stroke | Proposes a mechanism through relief of cerebral vasospasm |
| [17441885](https://pubmed.ncbi.nlm.nih.gov/17441885/) | 2007 | Observational | J Obstet Gynaecol Res | Ionized and total magnesium levels in severe preeclampsia-eclampsia patients receiving magnesium sulfate |
| [36413336](https://pubmed.ncbi.nlm.nih.gov/36413336/) | 2023 | Observational | Biol Trace Elem Res | Incidence and risk factors of critical hypermagnesemia under magnesium sulfate therapy |
| [31527059](https://pubmed.ncbi.nlm.nih.gov/31527059/) | 2019 | Implementation report | Glob Health Sci Pract | Magnesium sulfate for eclampsia prevention needs a well-functioning health system in resource-limited settings |
| [39110688](https://pubmed.ncbi.nlm.nih.gov/39110688/) | 2024 | Qualitative | PLoS One | Nurse-midwives in Tanzania report limited knowledge of dosing and toxicity assessment |
| [26105883](https://pubmed.ncbi.nlm.nih.gov/26105883/) | 2013 | Preclinical | Pregnancy Hypertens | Effects of IV magnesium sulfate on seizures in a rat preeclampsia/eclampsia model |

The synonym entry "toxemia of pregnancy" adds stronger evidence for the same indication: the Magpie Trial ([12057549](https://pubmed.ncbi.nlm.nih.gov/12057549/), RCT, 2002), a Cochrane review ([21069663](https://pubmed.ncbi.nlm.nih.gov/21069663/), 2010), and meta-analyses of postpartum duration ([34187284](https://pubmed.ncbi.nlm.nih.gov/34187284/), [35271534](https://pubmed.ncbi.nlm.nih.gov/35271534/)).

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05860P | DBL Magnesium Sulfate Concentrated Injection 49.3% | Injection | Not stated in registry records |
| SIN02748P | Lemon Sweet Purgative Syrup | Syrup | Not stated in registry records |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were retrieved.

From the literature, critical hypermagnesemia can occur in severely preeclamptic women on magnesium sulfate (PMID 36413336). Monitoring of reflexes, respiratory rate and urine output, and dose adjustment in renal impairment, are standard precautions.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Magnesium sulfate has strong, long-standing evidence for eclampsia prevention and treatment, including a large placebo-controlled RCT (Magpie), a Cochrane review and several Phase 2/3 and Phase 3 dosing and duration trials. This is standard of care rather than a novel repurposing finding. The Singapore records do not show whether the injectable's label covers eclampsia.

**To proceed, the following is needed:**
- The HSA package insert for SIN05860P, to confirm the labelled indications, warnings and contraindications
- Mechanism of action data from DrugBank
- A defined dosing and postpartum duration protocol, guided by the duration meta-analyses
- Toxicity monitoring (reflexes, respiratory rate, urine output) and renal dose-adjustment guidance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

