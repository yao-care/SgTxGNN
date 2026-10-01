---
layout: default
title: Chlorpheniramine
parent: Medium Evidence (L3-L4)
nav_order: 239
evidence_level: L3
indication_count: 10
---

# Chlorpheniramine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Chlorpheniramine: From Allergic Conditions to Allergic Urticaria

## One-Sentence Summary

Chlorpheniramine is a first-generation H1 antihistamine, widely used for allergic conditions and cold symptoms. The TxGNN model predicts it may be effective for **allergic urticaria**. Currently **3 clinical trials** and **20 publications** are linked to this prediction, but none of the trials tests chlorpheniramine directly in urticaria. The prediction is best read as a class-level match with an established use rather than a novel repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Chlorpheniramine belongs to the alkylamine class of first-generation H1-receptor antagonists (inverse agonists) and has been used since the 1950s. Its registered indication text is also missing from the Singapore records, so the original indication is inferred from the literature, which describes broad use in allergic conditions.

Urticaria is driven by mast cell degranulation and histamine release, which produces wheal, flare and itching. Blocking the H1 receptor is the established basis of antihistamine therapy for urticaria. The high TxGNN score matches this class-level mechanism.

Because the original indication is unknown, this is probably a labelled or guideline-supported use rather than true repurposing. The evidence below is mostly class-level or indirect. A 2024 review lists chronic urticaria among chlorpheniramine's clinical uses.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01293201](https://clinicaltrials.gov/study/NCT01293201) | Phase 3 | Completed | 290 | Double-blind, placebo-controlled study of STAHIST (pseudoephedrine + chlorpheniramine + low-dose atropine) in seasonal allergic rhinitis. It is not a urticaria trial. Whether chlorpheniramine was the tested arm is unconfirmed |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | NA | Completed | 75 | Randomized, double-blind trial of adding a short corticosteroid burst to conventional H1-antihistamine therapy. Antihistamine is background treatment, so chlorpheniramine is not tested directly |
| [NCT02082054](https://clinicaltrials.gov/study/NCT02082054) | Phase 2 | Unknown | 125 | Atropine dose-ranging with pseudoephedrine and chlorpheniramine in seasonal allergic rhinitis. No clear urticaria link |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Randomised phase I trial | Eur J Pharm Sci | Compared oral bilastine, parenteral dexchlorpheniramine and a new parenteral bilastine on histamine-induced wheal and flare |
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Review | Curr Rev Clin Exp Pharmacol | Comprehensive review of chlorpheniramine; lists chronic urticaria among its reported clinical uses |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Loratadine was as effective as chlorpheniramine and other antihistamines in controlled comparative studies |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine was effective in chronic urticaria and allergic rhinitis in double-blind trials |
| [1683523](https://pubmed.ncbi.nlm.nih.gov/1683523/) | 1991 | Review | Ann Allergy | Comparative efficacy of H1 antihistamines; second-generation agents are less sedating |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Cetirizine in allergic rhinitis, pollen-induced asthma and chronic urticaria |
| [8808167](https://pubmed.ncbi.nlm.nih.gov/8808167/) | 1996 | Review | Drugs | Ebastine improved symptoms in chronic idiopathic urticaria and allergic rhinitis |
| [2873823](https://pubmed.ncbi.nlm.nih.gov/2873823/) | 1986 | Cohort | Asian Pac J Allergy Immunol | Descriptive study of 142 Thai children with urticaria |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Case report | Medicine | Two cases of chlorpheniramine-induced anaphylaxis plus a pharmacovigilance database review |
| [26240795](https://pubmed.ncbi.nlm.nih.gov/26240795/) | 2015 | Case report | Asia Pac Allergy | Chlorpheniramine-induced anaphylaxis diagnosed by basophil activation test |

## Singapore Market Information

Approved indication text is not stated in the registry records. Other registered dosage forms include syrup, spray, capsule and suspension.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN10511P | AXCEL CHLORPHENIRAMINE TABLETS 4 mg | Tablet |
| SIN02632P | CHLORAMINE TABLET 4 mg | Tablet |
| SIN10028P | PIRIMAT INJECTION 10 mg/ml | Injection |
| SIN03442P | CHLORPYRIMINE TABLET 4 mg | Tablet |
| SIN02658P | ANTAMIN TABLET 4 mg | Tablet |

## Safety Considerations

Please refer to the package insert for safety information.

The literature retrieved also reports rare immediate hypersensitivity and anaphylaxis to chlorpheniramine (2015 and 2019 case reports). As a first-generation agent, it carries a sedation and anticholinergic burden, and second-generation alternatives are available.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism (H1 blockade of histamine-mediated wheal, flare and itch) is well established, and chlorpheniramine is widely marketed in Singapore. However, none of the three linked trials tests chlorpheniramine in urticaria, and most literature concerns other antihistamines.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmation of the registered Singapore indications, to determine whether urticaria is already labelled
- Verification of whether chlorpheniramine was the tested agent in NCT01293201
- Urticaria-specific chlorpheniramine efficacy data, since current support is class-level
- Detailed MOA data from DrugBank
- A comparison against second-generation antihistamines, given the sedation and anticholinergic burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

