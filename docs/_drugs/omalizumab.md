---
layout: default
title: Omalizumab
parent: Low Evidence (L5)
nav_order: 731
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

Omalizumab (Xolair) is an anti-IgE antibody used for IgE-mediated allergic asthma. The TxGNN model predicts it may be effective for **bronchitis**, but this looks like a knowledge-graph proximity effect rather than bronchitis-specific biology. Only **2 clinical trials** (neither a real efficacy test in bronchitis) and **8 publications** (mostly asthma-focused reviews) were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic asthma (the Singapore licence records carry no indication text, so this is taken from the literature and repurposing rationale in the Evidence Pack) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.999% (TxGNN rank 45) |
| Evidence Level | L4 (the only Phase 2/3 trial had 11 participants and an unclear link to bronchitis, so it does not meet the L2 bar) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, omalizumab is an anti-IgE monoclonal antibody. It binds free IgE and reduces FcεRI-mediated activation of mast cells and basophils, which drives allergic airway inflammation. Its efficacy in allergic asthma is well established, and mechanistically it may be applicable to airway conditions that share IgE-driven inflammation.

Bronchitis, however, is not generally an IgE-driven disease, so the link is indirect. It runs mainly through the asthma/COPD overlap, where chronic bronchitis is part of the smoking-related airway disease that coexists with asthma. One small trial also tested omalizumab in persistent eosinophilic bronchitis in patients with asthma.

The very high TxGNN score most likely reflects how close bronchitis sits to the approved asthma indication in the knowledge graph. It should not be read as evidence of bronchitis-specific benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Double-blind, placebo-controlled trial of omalizumab's steroid-sparing effect (prednisone reduction) in asthma with persistent eosinophilic bronchitis. The sample is too small to support any conclusion. |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Completed | 382 | Dose-finding study of QGE031 (a different anti-IgE agent) in chronic spontaneous urticaria, with omalizumab as the active comparator. Bronchitis is not the studied condition. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postepy Dermatol Alergol | Omalizumab in middle-aged or older patients with severe allergic asthma-COPD overlap; suggests biologics may help this phenotype |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Management of asthma with smoking-induced airway disease (chronic bronchitis, emphysema); smokers were excluded from most trials, so drug choice is uncertain |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | Preoperative management of patients with bronchial asthma or chronic bronchitis; notes omalizumab availability for severe allergic asthma |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Approval and post-approval experience of omalizumab in moderate-to-severe persistent asthma |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Safety review | Curr Med Res Opin | Pooled safety analysis of omalizumab in children with allergic asthma |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Review | Rev Mal Respir | French working-party review of adult asthma exacerbations (definition, pathophysiology, treatment) |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | Overview of monoclonal antibodies in paediatrics, including allergic disease |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | Rare case of plastic bronchitis after bronchial thermoplasty |

## Singapore Market Information

Six registrations exist; five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16115P | XOLAIR Solution for Injection in Pre-filled Syringe 75mg/0.5mL | Injection, solution | Not stated in the registry record |
| SIN17030P | XOLAIR Solution for Injection in Pre-filled Pen 75mg/0.5mL | Injection, solution | Not stated in the registry record |
| SIN17029P | XOLAIR Solution for Injection in Pre-filled Syringe 300mg/2.0mL | Injection, solution | Not stated in the registry record |
| SIN16116P | XOLAIR Solution for Injection in Pre-filled Syringe 150mg/1.0mL | Injection, solution | Not stated in the registry record |
| SIN17032P | XOLAIR Solution for Injection in Pre-filled Pen 300mg/2.0mL | Injection, solution | Not stated in the registry record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on a very high model score but almost no bronchitis-specific evidence. The one relevant trial enrolled 11 patients, and the literature is mainly about asthma. Bronchitis is not IgE-driven, so the link is indirect. Omalizumab's real repurposing signal in this Evidence Pack lies in COPD/obstructive lung disease (the Phase 2 COPD-OMA trial, NCT07059091, is recruiting), not in bronchitis.

**To proceed, the following is needed:**
- Adequately powered controlled trial data in a defined bronchitis phenotype (e.g., eosinophilic bronchitis or asthma-COPD overlap)
- Detailed mechanism of action data (MOA)
- Package insert warnings, contraindications and approved indication text from the Singapore HSA
- Results of the COPD-OMA trial as an adjacent signal

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

