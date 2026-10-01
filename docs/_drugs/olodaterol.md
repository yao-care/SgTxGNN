---
layout: default
title: Olodaterol
parent: Medium Evidence (L3-L4)
nav_order: 729
evidence_level: L3
indication_count: 10
---

# Olodaterol
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

# Olodaterol: From COPD to Bronchitis

## One-Sentence Summary

Olodaterol is a once-daily long-acting beta2-agonist (LABA) bronchodilator, sold in Singapore as part of the tiotropium/olodaterol inhaler Spiolto Respimat. It is used for chronic obstructive pulmonary disease (COPD).
The TxGNN model predicts it may be effective for **bronchitis**, with **3 clinical trials** and **2 publications** linked to this prediction. All of them concern COPD, and none tests bronchitis as a separate indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COPD (inferred from the trial evidence; the Singapore registration record has no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Olodaterol is known to be a long-acting beta2-agonist that relaxes airway smooth muscle and widens the airways. Its efficacy in COPD is well established, and mechanistically it may be applicable to bronchitis.

Chronic bronchitis is a clinical form of COPD, which is why the model links the two. The signal is therefore largely COPD-derived. It does not show that olodaterol works for bronchitis as its own condition. No evidence supports acute bronchitis at all.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A | Completed | 1335 | Japanese post-marketing surveillance of long-term tiotropium/olodaterol in COPD (chronic bronchitis, emphysema). Real-world safety data, not bronchitis efficacy. |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completed | 22155 | Drug utilisation safety study of aclidinium bromide in COPD. Olodaterol is not the studied drug, so relevance is indirect. |
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A | Completed | 11316 | Healthcare resource use and cost in COPD patients starting tiotropium/olodaterol versus a triple inhaler. No efficacy endpoint for bronchitis. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Review | Am J Health Syst Pharm | Reviews the pharmacology, pharmacokinetics, efficacy and safety of olodaterol in COPD. |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline | Basic Clin Pharmacol Toxicol | Finnish national guideline on diagnosis and drug treatment of stable COPD. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15890P | SPIOLTO® RESPIMAT® Re-usable Solution for Inhalation 2.5 microgram / 2.5 microgram | Solution |

The manufacturer is Boehringer Ingelheim Pharma GmbH & Co. KG.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis signal comes from COPD studies and does not establish a separate bronchitis indication. The three linked trials are observational or utilisation studies. The Singapore package insert warnings and contraindications are also missing, which blocks safety screening.

Olodaterol's strongest evidence is for COPD itself. That is the existing use, so it is not a repurposing claim. The other TxGNN-predicted conditions (interstitial and compensatory emphysema, tracheal stenosis, and others) have no trials or literature, and their mechanistic links are weak.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Bronchitis-specific efficacy studies, separating chronic from acute bronchitis
- Confirmation of the approved indication text for SIN15890P
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

