---
layout: default
title: Vonoprazan
parent: Low Evidence (L5)
nav_order: 1065
evidence_level: L5
indication_count: 10
---

# Vonoprazan
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

# Vonoprazan: From Acid Suppression to Active Peptic Ulcer Disease

## One-Sentence Summary

Vonoprazan is a potassium-competitive acid blocker (P-CAB) that is marketed in Singapore as VOCINTI tablets. The Singapore licence records do not state an approved indication.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, supported by **2 registered clinical trials** and **17 retrieved publications**, including published randomized trials and meta-analyses.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (see caveat below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record. The literature describes vonoprazan as a P-CAB that reversibly blocks the gastric H+/K+-ATPase (the proton pump). It gives stronger and faster acid suppression than proton pump inhibitors (PPIs). Gastric and duodenal ulcers are acid-dependent, so suppressing acid promotes healing and prevents recurrence.

The prediction fits the known pharmacology. Published sources describe vonoprazan 20 mg once daily for gastroduodenal ulcer in Japan, and 10 mg once daily for secondary prevention of NSAID- or low-dose-aspirin-induced ulcer.

**Caveat:** Because no original indication is recorded, this may not be true repurposing. Peptic ulcer may already be a labeled use in some markets. Check the Singapore label before treating it as a new indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03214952](https://clinicaltrials.gov/study/NCT03214952) | N/A (post-marketing surveillance) | Completed | 3,183 | Real-world safety and effectiveness of vonoprazan (Takecab) in gastric ulcer, duodenal ulcer and reflux esophagitis. Observational with no comparator, so not efficacy-grade evidence. |
| [NCT03116841](https://clinicaltrials.gov/study/NCT03116841) | Phase 4 | Completed | 3 | Exploratory study of vonoprazan 20 mg on sleep disturbance in reflux esophagitis. The population and endpoint do not match peptic ulcer, and the sample is too small to inform efficacy. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28988197](https://pubmed.ncbi.nlm.nih.gov/28988197/) | 2018 | RCT | Gut | Randomized, lansoprazole-controlled non-inferiority study of vonoprazan for preventing recurrence of NSAID-induced peptic ulcer, with a single-blind extension on long-term safety. |
| [28267236](https://pubmed.ncbi.nlm.nih.gov/28267236/) | 2017 | RCT | Digestive Endoscopy | Prospective randomized trial of vonoprazan for healing artificial gastric ulcers after endoscopic submucosal dissection. |
| [38976448](https://pubmed.ncbi.nlm.nih.gov/38976448/) | 2025 | RCT (indirect) | Am J Gastroenterol | Phase 3 trial of zastaprazan, a different P-CAB, versus esomeprazole in erosive esophagitis. Class-level support only. |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Network meta-analysis (indirect) | Am J Gastroenterol | Compares P-CABs with PPIs for grade C/D esophagitis. Class-level support, not ulcer-specific. |
| [39156336](https://pubmed.ncbi.nlm.nih.gov/39156336/) | 2024 | Review | Cureus | Reviews vonoprazan efficacy and safety in GERD, peptic ulcer disease and H. pylori infection. |
| [26369775](https://pubmed.ncbi.nlm.nih.gov/26369775/) | 2016 | Review (PK/PD) | Clin Pharmacokinet | Describes the pharmacokinetics and pharmacodynamics of the first-in-class P-CAB, including the Japanese dosing for gastroduodenal ulcer. |
| [37066678](https://pubmed.ncbi.nlm.nih.gov/37066678/) | 2023 | PK/PD analysis | Aliment Pharmacol Ther | Translational PK/PD support for vonoprazan dosing in erosive esophagitis and H. pylori infection. |
| [32998241](https://pubmed.ncbi.nlm.nih.gov/32998241/) | 2020 | Review | Pharmaceuticals | Potential benefits of vonoprazan in H. pylori eradication, which lowers ulcer recurrence. |
| [36660052](https://pubmed.ncbi.nlm.nih.gov/36660052/) | 2023 | Guideline/Review | JGH Open | H. pylori management, including testing and treatment in patients with peptic ulcer. |
| [22512618](https://pubmed.ncbi.nlm.nih.gov/22512618/) | 2012 | Preclinical | J Med Chem | Discovery of TAK-438 (vonoprazan). The compound is more potent and longer-acting than PPIs in vivo. |

Several other retrieved publications are unrelated to vonoprazan and were not used.

The evidence packs for other predicted indications also contain directly relevant vonoprazan work:
- A vonoprazan vs lansoprazole Phase 3 pair in gastric and duodenal ulcer (PMID 27891632).
- Meta-analyses of vonoprazan vs PPI in ulcer disease (PMIDs 39294424, 39301419).

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15444P | VOCINTI FILM-COATED TABLET 20MG | Tablet, film coated | Takeda Pharmaceutical Company Limited (Hikari Plant) |
| SIN15445P | VOCINTI FILM-COATED TABLET 10MG | Tablet, film coated | Takeda Pharmaceutical Company Limited (Hikari Plant) |

Both products are oral. The records do not include approved indication text.

## Safety Considerations

Please refer to the package insert for safety information.

The literature also reports long-term effects of vonoprazan. These include gastric mucosal changes, raised serum gastrin, and a case of severe rebound acid hypersecretion after 6 years of use (PMID 39712905).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism fits, and published randomized trials in ulcer populations support the indication. L1 rests on these publications, not on the two registered trials, which are observational or off-target. The Singapore label and safety data are not yet confirmed, so the recommendation is conditional.

**To proceed, the following is needed:**
- Download and review the HSA package insert for warnings and contraindications. This is a blocking gap.
- Confirm the approved indication on the Singapore label to decide whether this is a true new use.
- Obtain detailed mechanism of action data from DrugBank.
- Confirm H. pylori status and NSAID/aspirin use in the target population.
- Plan monitoring for long-term acid-suppression effects, including rebound acid hypersecretion.

The other nine predicted indications are weaker. Most are rated Hold or Research Question, and several rest on the knowledge-graph score alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

