---
layout: default
title: Leuprolide
parent: Low Evidence (L5)
nav_order: 586
evidence_level: L5
indication_count: 10
---

# Leuprolide
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

# Leuprolide: From GnRH-Agonist Hormone Therapy to Osteoarthritis

## One-Sentence Summary

Leuprolide is a GnRH agonist that suppresses sex hormones. The Singapore registry data provided do not state its approved indications.
The TxGNN model predicts it may be effective for **Osteoarthritis** with a very high score, but only **1 clinical trial** (in prostate cancer) and **1 publication** (a case report) were retrieved, and neither studies osteoarthritis.
This is a model-only prediction with no direct supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registry data provided |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Leuprolide is known as a GnRH agonist that suppresses sex hormones. The linked evidence retrieved by the pipeline concerns prostate cancer, where hormone suppression is the therapeutic goal.

The relationship between hormone suppression and osteoarthritis is weak. Any effect on joint tissue would be indirect. Hypoestrogenism and bone loss are known adverse effects of GnRH-axis suppression, and they could worsen musculoskeletal outcomes rather than help them. The high TxGNN score (rank 4,627 in the model output) therefore looks like a statistical association in the knowledge graph, not a documented biological rationale.

Other predictions for this drug are also weak. Nine of the ten are at evidence level L5. The exception is arthropathy (L4), whose only tangential signal is a case report of endometriosis-associated joint pain that remitted with GnRH-agonist therapy. In that case the drug treated the underlying hormone-dependent condition and did not act directly on the joint.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002881](https://clinicaltrials.gov/study/NCT00002881) | Phase 3 | Completed | Not reported | Orchiectomy/LHRH analog plus flutamide, suramin and hydrocortisone in metastatic prostate cancer. It does not study osteoarthritis (relevance grade C), so it provides no support for this indication. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case report | Clinical Breast Cancer | Metastatic prostatic adenocarcinoma mimicking inflammatory breast carcinoma in a 78-year-old man. It is unrelated to osteoarthritis. |

## Singapore Market Information

Six licenses are registered. The five main ones are listed below. The registry data provided do not include approved indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14512P | ELIGARD® Powder and Solvent for Solution for Injection 22.5mg | Injection, powder, lyophilized, for suspension, extended release |
| SIN10742P | Lucrin Depot for Injection PDS 11.25mg | Injection, powder, for solution |
| SIN08862P | Lucrin Depot for Injection PDS 3.75mg | Injection, powder, for solution |
| SIN14004P | Lucrin Depot for Injection PDS 30mg | Injection, powder, for solution |
| SIN14513P | ELIGARD® Powder and Solvent for Solution for Injection 45mg | Injection, powder, lyophilized, for suspension, extended release |

## Safety Considerations

- **Bone loss and hypoestrogenism**: These are known adverse effects of GnRH-axis suppression. They could worsen musculoskeletal outcomes, which is directly relevant to a joint or bone indication.
- **Drug Interactions**: No interaction records were found in the DDI query.

Please refer to the package insert for further safety information, including formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. The only retrieved trial and paper concern prostate cancer, and there is no plausible mechanism linking GnRH agonism to osteoarthritis benefit. Known bone-loss effects point the other way.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications and approved indications). This is currently a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- A targeted literature search for GnRH agonists and osteoarthritis or joint outcomes, including preclinical work.
- An assessment of whether the musculoskeletal and bone-density risks outweigh any plausible benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

