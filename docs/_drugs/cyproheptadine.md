---
layout: default
title: Cyproheptadine
parent: Low Evidence (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
---

# Cyproheptadine
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

# Cyproheptadine: Predicted Repurposing for Allergic Urticaria

## One-Sentence Summary

Cyproheptadine is a first-generation antihistamine, and no original approved indication is recorded in the source data. The TxGNN model predicts it may be effective for **allergic urticaria**. Only **2 loosely related clinical trials** and **18 publications** were retrieved, and these mostly concern other antihistamines, so direct evidence for this indication is thin.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (mechanistic and class-effect evidence only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cyproheptadine is a first-generation H1 receptor antagonist that also blocks 5-HT2 receptors and has anticholinergic activity. Urticaria wheals and itch are driven largely by histamine released from mast cells, so H1 blockade is a mechanistically coherent treatment. Detailed mechanism-of-action data are not available in the DrugBank record, so this reasoning rests on the drug's known pharmacology.

The supporting literature covers other antihistamines (loratadine, desloratadine, bilastine, rupatadine, fexofenadine, levocetirizine), which are established for urticaria and allergic rhinitis. That is a class-effect inference, not direct proof for cyproheptadine. The source record also lists no original indication, and cyproheptadine is widely labelled for allergic conditions. This may therefore be an existing use rather than true repurposing.

One direct cyproheptadine study exists in a related condition: a double-blind crossover comparison with ketotifen in 6 Thai children with cold urticaria (1995). Cold urticaria is a separate prediction with stronger direct evidence, discussed in the conclusion.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00762983](https://clinicaltrials.gov/study/NCT00762983) | N/A | Completed | 1003 | Post-marketing drug-use survey of loratadine (Claritin) in children, covering safety and symptom scores. Cyproheptadine not studied. |
| [NCT07101445](https://clinicaltrials.gov/study/NCT07101445) | Phase 4 | Recruiting | 94 | Methylprednisolone vs dexamethasone premedication to prevent allergic reactions to Aphexda in multiple myeloma. Not an urticaria efficacy study and does not involve cyproheptadine. |

Both trials were graded C for relevance. Neither tests cyproheptadine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Double-blind crossover study | Asian Pac J Allergy Immunol | Cyproheptadine vs ketotifen in 6 Thai children with cold urticaria. The only study here that tests cyproheptadine. |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review | Clin Exp Allergy | How to choose the best H1-antihistamine for urticaria, especially chronic spontaneous urticaria. |
| [20067329](https://pubmed.ncbi.nlm.nih.gov/20067329/) | 2010 | Post-marketing surveillance | Clin Drug Investig | Safety and efficacy of desloratadine 5 mg in seasonal allergic rhinitis and chronic urticaria, across four surveillance studies. |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine, a second-generation antihistamine, in allergic rhinitis and urticaria. |
| [27500993](https://pubmed.ncbi.nlm.nih.gov/27500993/) | 2016 | Review | Expert Opin Drug Saf | Global safety evaluation of rupatadine in allergic rhinitis and urticaria. |
| [18339040](https://pubmed.ncbi.nlm.nih.gov/18339040/) | 2008 | Review | Allergy | Rupatadine in allergic rhinitis and chronic urticaria. Histamine is central to both, and broader anti-inflammatory activity may add benefit. |
| [33198523](https://pubmed.ncbi.nlm.nih.gov/33198523/) | 2021 | Review | Expert Opin Pharmacother | Second-generation antihistamines in children over 2 years, with a focus on rupatadine. Most paediatric data are extrapolated from adults. |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Comparative pharmacokinetics and pharmacodynamics of desloratadine, fexofenadine and levocetirizine. |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine was effective and well tolerated in chronic urticaria and allergic rhinitis in double-blind trials. |
| [35396016](https://pubmed.ncbi.nlm.nih.gov/35396016/) | 2022 | Review | Profiles Drug Subst Excip Relat Methodol | Loratadine drug profile. It is widely used for allergic rhinitis, chronic urticaria and asthma. |

Apart from PMID 7488341, none of these publications studies cyproheptadine.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06637P | PILIAN TABLET 4 mg (Yung Shin Pharmaceutical Ind Co Ltd) | Tablet | Not listed in the record |

The only registered route is oral.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were found for this drug.

The evidence pack notes that first-generation antihistamines carry sedation and anticholinergic effects, which matter especially in children and older adults.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the evidence for allergic urticaria is class-effect only (L4). No retrieved trial tests cyproheptadine, and the package-insert safety data are missing, which blocks safety screening. Because the source record lists no original indication, it is unclear whether this is genuine repurposing or an existing labelled use.

The same evidence pack ranks **cold urticaria** second (score 99.76%). That prediction is supported by direct cyproheptadine studies, including a double-blind comparison with chlorpheniramine and placebo (PMID 334082). It reaches level L2 and a "Proceed with Guardrails" recommendation, so it is the stronger candidate to pursue first.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (blocking gap)
- Mechanism-of-action data from DrugBank
- Confirmation of cyproheptadine's approved indications in Singapore
- Direct cyproheptadine efficacy data in allergic or chronic urticaria, ideally compared with second-generation antihistamines
- A sedation and anticholinergic risk plan for children and older adults

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

