---
layout: default
title: Imiquimod
parent: High Evidence (L1-L2)
nav_order: 522
evidence_level: L2
indication_count: 10
---

# Imiquimod
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Imiquimod: From Topical Skin Lesion Treatment to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical immune-response-modifying cream, marketed in Singapore as Aldara 5% cream. The TxGNN model predicts it may be effective for **pre-malignant neoplasm**, with **19 clinical trials** and **9 publications** retrieved for this direction. Only a few of these trials directly test imiquimod in pre-malignant lesions, so the evidence is moderate rather than strong.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record (the approved indication text is blank) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this drug. Based on general pharmacology, imiquimod activates Toll-like receptor 7 (TLR7). This triggers local release of interferon-alpha, TNF-alpha and IL-12 and stimulates innate and adaptive immune responses. This mechanism is not taken from the supplied data.

Pre-malignant lesions such as actinic keratosis, vulvar, cervical and anal intraepithelial neoplasia, and actinic cheilitis are dysplastic epithelium, often HPV-driven or UV-driven. Local immune activation could plausibly clear such tissue. The high TxGNN score is consistent with this, and the retrieved trials and reviews include topical imiquimod in several of these lesion types.

"Pre-malignant neoplasm" is a broad label. It covers different lesion sites with different biology, so it should be split into specific lesion types before any recommendation. Ranks 2 to 10 of the model's predictions are much weaker. Only benign oral neoplasm (rank 2, mostly preclinical and case-level evidence) and odontogenic cyst (rank 4, indirect evidence tied to Gorlin syndrome) have any literature. Ranks 3 and 6 to 10 have no retrieved evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | Randomized trial of topical imiquimod in high-grade cervical intraepithelial lesions (HPV-related pre-invasive state) |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomized trial of topical imiquimod for high-grade cervical intraepithelial neoplasia versus standard excision. Stopped with only 9 participants, so it is underpowered |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Explorative study of imiquimod in vulvar intraepithelial neoplasia 2/3 and anogenital warts, including immune mechanisms |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Imiquimod 3.75% cream after cryotherapy for hypertrophic actinic keratoses on hands and forearms |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label, single-arm study of imiquimod 5% cream for actinic keratoses on the head. Small, and it looks at duration of effect |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Randomized comparison of 5%, 0.05% and nanoencapsulated 0.05% imiquimod in actinic cheilitis. Terminated early |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Imiquimod as neo-adjuvant treatment before excision of facial lentigo maligna (intraepidermal melanocytic proliferation) |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Curettage plus imiquimod versus surgical excision in nodular basal cell carcinoma. This is a malignant, not pre-malignant, setting |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Pilot of neoadjuvant topical imiquimod (Aldara) in early-stage oral squamous cell carcinoma |

The other 10 retrieved trials use imiquimod as a vaccine adjuvant or combination component in malignant settings (glioma, melanoma, prostate and lung cancer, solid tumours). They are not direct evidence for pre-malignant lesions and are omitted here.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia, a pre-malignant HPV-associated condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia, where surgery has high morbidity and relapse |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical options for non-melanoma skin cancer and precursor lesions: fluorouracil, diclofenac, imiquimod and photodynamic therapy |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, a pre-malignant lesion that can progress to squamous cell carcinoma, including topical field therapies |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | Int J STD AIDS | Successful treatment of high-grade vulval intraepithelial neoplasia with imiquimod 5% in a renal transplant recipient |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | Int J STD AIDS | Bowenoid papulosis of the penis cleared with topical imiquimod 5%, well tolerated |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical | Urol Oncol | Rat pharmacokinetics of two investigational TLR7 agonists, noting TLR7 agonists are used topically for (pre)malignant skin lesions |

The retrieved literature has no RCT. It consists of reviews, two Cochrane reviews (their abstracts as retrieved do not state imiquimod-specific results), case reports and a preclinical study.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10105P | ALDARA CREAM 5% | Cream | Not stated in the registration record |

Manufacturers: 3M Health Care Limited and Ensign Laboratories Pty Ltd. The only registered route is topical.

## Safety Considerations

Drug interaction query: no records found.

Safety signals seen in the retrieved literature for other predicted indications:
- A case report describes malignant conversion of florid oral and labial papillomatosis during topical imiquimod therapy. A 2024 review also questions the safety of off-label use in oral lesions.
- Case reports describe erythema multiforme and lichen planopilaris after imiquimod 5% cream in patients with Gorlin syndrome.

Please refer to the package insert for warnings and contraindications, which are not available in the supplied data.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed randomized Phase 2 trial (NCT03233412) tests topical imiquimod directly in a pre-malignant setting (high-grade cervical intraepithelial lesions), which supports L2. Larger direct evidence is missing. The Phase 3 cervical trial was terminated at 9 participants, most other trials are small or single-arm, and the retrieved literature has no RCT.

**To proceed, the following is needed:**
- Split "pre-malignant neoplasm" into specific lesion types (e.g., actinic keratosis, cervical, vulvar and anal intraepithelial neoplasia) and assess each separately
- Obtain the results of NCT03233412 and NCT01720407 to confirm efficacy and design
- Obtain the HSA package insert to fill the warnings, contraindications and approved indication gaps
- Retrieve DrugBank mechanism of action data
- Define a safety monitoring plan for mucosal and off-label sites, given the reported oral malignant conversion and skin adverse reactions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

