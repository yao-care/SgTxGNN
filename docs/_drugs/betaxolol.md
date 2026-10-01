---
layout: default
title: Betaxolol
parent: Low Evidence (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Betaxolol
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

# Betaxolol: From an Unrecorded Original Indication to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a beta-1 selective blocker. The Singapore registration record does not list an approved indication, so its original use is not documented in this dataset.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials or publications** were found for this specific subtype.
Closely related open-angle glaucoma predictions have **2 Phase 3 trials** and **20 publications**, but that evidence does not carry over directly to the hereditary subtype.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text in the Singapore licence is empty) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only; the related open-angle glaucoma predictions are graded L1) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known pharmacology, betaxolol is a beta-1 selective blocker. It lowers intraocular pressure (IOP) by reducing aqueous humour production in the ciliary epithelium. Lowering IOP is the established treatment target across glaucoma, which is why the model scores this prediction so highly.

The link is plausible but unproven for this subtype. Primary hereditary glaucoma is a congenital or early-onset condition, and the retrieved evidence comes from adult open-angle glaucoma. Any benefit would be an extrapolation.

There is also a route mismatch. The only Singapore product is an oral film-coated tablet, while the glaucoma evidence concerns topical eye drops. Route compatibility has not been assessed.

## Clinical Trial Evidence

No clinical trials are registered for primary hereditary glaucoma itself. The two trials below were retrieved for the related open-angle glaucoma predictions and are shown for context only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02617459](https://clinicaltrials.gov/study/NCT02617459) | Phase 3 | Completed | 366 | Randomised, open-label, positive-controlled trial of levobetaxolol eye drops in primary open-angle glaucoma or ocular hypertension (Chinese patients). Levobetaxolol is the S-enantiomer of betaxolol, so this is not direct betaxolol evidence. |
| [NCT00000132](https://clinicaltrials.gov/study/NCT00000132) | Phase 3 | Unknown | Not listed | Early Manifest Glaucoma Trial: immediate IOP-lowering treatment vs late or no treatment in newly detected open-angle glaucoma. The evidence pack notes the treatment arm reportedly combined betaxolol with laser trabeculoplasty (unverified), so betaxolol's effect alone cannot be isolated. |

## Literature Evidence

No literature was retrieved for primary hereditary glaucoma. The publications below were retrieved for open-angle glaucoma and are shown for context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [12365904](https://pubmed.ncbi.nlm.nih.gov/12365904/) | 2002 | RCT | Arch Ophthalmol | EMGT results: lowering IOP slows progression of newly detected open-angle glaucoma. |
| [10571351](https://pubmed.ncbi.nlm.nih.gov/10571351/) | 1999 | RCT (design/baseline) | Ophthalmology | EMGT design and baseline data in early, untreated open-angle glaucoma. |
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Systematic review / network meta-analysis | Ophthalmology | Comparative effectiveness of first-line medications for primary open-angle glaucoma. |
| [11039742](https://pubmed.ncbi.nlm.nih.gov/11039742/) | 2000 | RCT | J Glaucoma | Brimonidine 0.2% vs betaxolol 0.25%: clinical success rates and quality of life in open-angle glaucoma or ocular hypertension. |
| [11755834](https://pubmed.ncbi.nlm.nih.gov/11755834/) | 2002 | RCT | Am J Ophthalmol | Double-masked comparison of unoprostone with timolol and betaxolol over 6 months. |
| [7639651](https://pubmed.ncbi.nlm.nih.gov/7639651/) | 1995 | RCT | Arch Ophthalmol | One-year double-masked comparison of dorzolamide, timolol and betaxolol. |
| [3518464](https://pubmed.ncbi.nlm.nih.gov/3518464/) | 1986 | RCT | Am J Ophthalmol | Betaxolol vs timolol in 38 patients: median IOP was consistently lower with timolol. |
| [2898859](https://pubmed.ncbi.nlm.nih.gov/2898859/) | 1988 | RCT | Acta Ophthalmol | Betaxolol vs timolol in 41 patients: both lowered IOP significantly, with no difference in change from baseline. |
| [2202584](https://pubmed.ncbi.nlm.nih.gov/2202584/) | 1990 | Review | Drugs | Topical betaxolol 0.5% lowers IOP by 13–30%, comparable to timolol. The main adverse effect is transient local stinging. |
| [33126804](https://pubmed.ncbi.nlm.nih.gov/33126804/) | 2020 | Review / meta-analysis | Ceska Slov Oftalmol | Betaxolol, brimonidine and carteolol in normal-tension glaucoma. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12621P | BETAC FILM COATED TABLET 20 mg | Tablet, film coated (oral) | Not stated in the record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, primary hereditary glaucoma, rests on a model score alone, with no trials or literature. The available evidence concerns adult open-angle glaucoma and topical use, while the registered Singapore product is an oral tablet. Because the original indication and safety data are also missing, the evidence pack cannot move this candidate past the first screening stage.

The open-angle glaucoma predictions (ranks 2–3) have the strongest support, graded L1 with a "Proceed with Guardrails" recommendation. The pack itself suggests these may reflect an existing ophthalmic use rather than true repurposing, which is likely a labelling or data-gap issue.

Predictions ranked 4–10 (malignant hypertension, pulmonary hypertension, closed-angle glaucoma and others) have no direct supporting evidence and remain on Hold or as research questions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (currently a blocking gap)
- Mechanism of action and original indication data (DrugBank query)
- Evidence specific to primary hereditary or congenital glaucoma
- Confirmation that the Singapore oral tablet is relevant to an ophthalmic indication, or identification of a topical formulation
- Confirmation of the levobetaxolol trial's comparator arm and the exact intervention, and of the betaxolol component in the EMGT
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

