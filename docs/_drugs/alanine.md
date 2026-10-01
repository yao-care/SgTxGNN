---
layout: default
title: Alanine
parent: Low Evidence (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Alanine
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

# Alanine: From Parenteral Nutrition Amino Acid to Gastroparesis

## One-Sentence Summary

Alanine is a nutritional amino acid. In Singapore it is marketed as a component of intravenous amino acid infusion products; the registration records give no approved-indication text, so this use is inferred from the product names. The TxGNN model predicts it may be effective for **gastroparesis**, but the 7 clinical trials and 3 publications retrieved for this disease are keyword matches that do not test alanine. Evidence is at **L5 (model prediction only)**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records; likely amino acid supply in parenteral nutrition (inferred from product names) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, alanine is a non-essential amino acid supplied as part of multi-amino-acid infusion solutions (for example Aminoven, Nephrosteril and Aminoplasmal). Its role there is nutritional, not therapeutic for a specific disease.

The review of this prediction found no plausible alanine-specific mechanism for improving gastric motility. The high score (0.994) comes from graph-based similarity in the knowledge graph, not from clinical data. None of the retrieved trials tests alanine; they cover motilin agonists, cannabidiol, buspirone, aprepitant, traditional Chinese medicine and enteral feeding schedules. Some appear only because they mention gastroparesis or critical-care feeding.

The other nine ranked predictions (vitamin D deficiency, dyspepsia, prothrombin deficiency, and others) are also L5, except renal tubular acidosis at L4. The L4 rating rests on physiological studies of renal alanine and glutamine handling, which is context rather than treatment evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06452966](https://clinicaltrials.gov/study/NCT06452966) | N/A | Recruiting | 350 | Traditional Chinese medicine for organ failure in ICU patients; not an alanine study |
| [NCT02793154](https://clinicaltrials.gov/study/NCT02793154) | Phase 4 | Terminated | 4 | Albiglutide vs exenatide on gastric emptying in type 2 diabetes; not an alanine study |
| [NCT01602549](https://clinicaltrials.gov/study/NCT01602549) | Phase 2 | Completed | 58 | Motilin agonist GSK962040 on L-DOPA pharmacokinetics in Parkinson's disease with delayed gastric emptying; matched on disease term only |
| [NCT03941288](https://clinicaltrials.gov/study/NCT03941288) | Phase 2 | Completed | 92 | Cannabidiol for gastroparesis and functional dyspepsia; not an alanine study |
| [NCT01262898](https://clinicaltrials.gov/study/NCT01262898) | Phase 2 | Completed | 79 | Oral motilin agonist GSK962040 in diabetic gastroparesis; not an alanine study |
| [NCT03587142](https://clinicaltrials.gov/study/NCT03587142) | Phase 2 | Completed | 96 | Buspirone for early satiety and gastroparesis symptoms; different drug, no alanine link |
| [NCT01934192](https://clinicaltrials.gov/study/NCT01934192) | Phase 2 | Terminated | 91 | GSK962040 for enteral feed delivery in critically ill patients; alanine not involved |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Review | Advances in Renal Replacement Therapy | GI and hepatic disorders in end-stage renal disease; notes gastroparesis is more common in chronic renal failure. No alanine data |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | Review | Diabetic Medicine | Diabetic hepatosclerosis as a possible microvascular complication. Not related to alanine treatment |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | Case report | Cureus | Glycogen hepatopathy in a type 1 diabetic patient whose history included gastroparesis. Incidental mention only |

## Singapore Market Information

19 registrations exist. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16337P | AMINOVEN SOLUTION FOR INFUSION 15% | Infusion, solution | Not listed in record |
| SIN11682P | AMINOVEN SOLUTION FOR INFUSION 5% | Injection | Not listed in record |
| SIN11829P | AMINOVEN SOLUTION FOR INFUSION 10% | Injection | Not listed in record |
| SIN06299P | NEPHROSTERIL FOR INTRAVENOUS INFUSION | Injection | Not listed in record |
| SIN08352P | AMINOPLASMAL-15% INFUSION | Injection | Not listed in record |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the database query.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model output only. No retrieved study tests alanine in gastroparesis, and there is no plausible mechanism linking alanine to gastric motility. Alanine is already marketed in Singapore as a nutritional component, so there is no market barrier, but there is also no evidence to justify pursuing gastroparesis.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A specific, testable hypothesis for how alanine or amino acid infusion could affect gastric emptying, backed by preclinical or clinical data
- If a lead is wanted from this candidate set, consider reviewing renal tubular acidosis (L4), whose physiological rationale is the only indirect biological signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

