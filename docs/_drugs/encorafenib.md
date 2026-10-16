---
layout: default
title: Encorafenib
parent: Low Evidence (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Encorafenib: predicted new indication Choroideremia . The most credible prediction is non-cutaneous melanoma (evidence level L5). Approved use: Metastatic melanoma"
---

# Encorafenib
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

# Encorafenib: From Metastatic Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Encorafenib is a BRAF inhibitor originally used to treat metastatic melanoma.
The TxGNN model predicts it may be effective for **non-cutaneous melanoma** (the most clinically plausible of the top predictions), with **3 clinical trials** and **1 publication** currently supporting this direction.
The evidence is indirect: the trials mainly enrol cutaneous BRAF V600-mutant melanoma, and the one publication is a case report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma |
| Predicted New Indication | Choroideremia (rank 1 by TxGNN score; no biological support, see below). The most credible prediction is non-cutaneous melanoma (rank 2) |
| TxGNN Prediction Score | 97.10% (choroideremia); 96.55% (non-cutaneous melanoma) |
| Evidence Level | L5 for choroideremia; L2 for non-cutaneous melanoma |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails (non-cutaneous melanoma, BRAF V600-mutant patients only); Hold for choroideremia |

> The registered original indication text is blank in the HSA licence records. The original indication shown here comes from the TxGNN knowledge graph.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, encorafenib is a BRAF V600 kinase inhibitor acting on the MAPK pathway. It is used with binimetinib in BRAF V600-mutant melanoma, and mechanistically it may be applicable to other BRAF-mutant melanomas.

**Top-ranked prediction (choroideremia) is not credible.** Choroideremia is an X-linked retinal degeneration caused by loss of CHM (REP1) function, with defective Rab prenylation. This is unrelated to the MAPK pathway. The high score looks like a network-based artefact, and no trials or publications exist. The same applies to central areolar choroidal dystrophy (rank 6).

**Non-cutaneous melanoma (rank 2) is more reasonable.** Mucosal and other non-cutaneous melanomas carry BRAF V600 mutations in a subset of cases, though less often than cutaneous melanoma. Where the mutation is present, the same MAPK inhibition applies. Uveal melanoma is typically driven by GNAQ/GNA11 rather than BRAF, so efficacy depends on mutation status.

Other melanoma-subtype predictions (epithelioid cell, eyelid, scrotum, superficial spreading, acral lentiginous, amelanotic, lentigo maligna) share the same logic: plausible only for BRAF V600-mutant cases. Lentigo maligna and acral lentiginous melanoma are less often BRAF-mutant.

## Clinical Trial Evidence

Trials for non-cutaneous melanoma (rank 2):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04045691](https://clinicaltrials.gov/study/NCT04045691) | N/A (observational) | Recruiting | 750 | BERING-MELANOMA: real-world effectiveness, quality of life and safety of encorafenib + binimetinib in BRAF V600-mutant unresectable or metastatic melanoma (Germany, Austria, Switzerland) |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EBIN: encorafenib + binimetinib followed by ipilimumab + nivolumab vs immunotherapy alone in BRAF V600-mutant melanoma |
| [NCT02857270](https://clinicaltrials.gov/study/NCT02857270) | Phase 1 | Completed | 210 | Safety of the ERK1/2 inhibitor LY3214996 alone or combined with other agents (including encorafenib) in advanced cancer; indirect evidence |

Trial for acral lentiginous melanoma (rank 8):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04511013](https://clinicaltrials.gov/study/NCT04511013) | Phase 2 | Recruiting | 112 | Randomised trial of encorafenib + binimetinib + nivolumab vs ipilimumab + nivolumab in BRAF V600-mutant melanoma with brain metastases |

No clinical trials are registered for the other predicted indications.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case report | Pigment Cell & Melanoma Research | Molecular profiling diagnosed epidermotropic metastatic melanoma presenting as eruptive primary melanomas (non-cutaneous melanoma; superficial spreading melanoma) |
| [33877099](https://pubmed.ncbi.nlm.nih.gov/33877099/) | 2021 | Case report | Recenti Progressi in Medicina | Amelanotic acral melanoma treated first-line with encorafenib + binimetinib: complete response lasting 37 months, then ongoing partial response on anti-PD-1 therapy |
| [31804055](https://pubmed.ncbi.nlm.nih.gov/31804055/) | 2021 | Case report | Italian Journal of Dermatology and Venereology | Mutational analysis of second primary melanomas arising under BRAF inhibitors, likely through paradoxical MAPK activation (epithelioid cell melanoma) |
| [38590555](https://pubmed.ncbi.nlm.nih.gov/38590555/) | 2024 | Review | Advances in Ophthalmology Practice and Research | Personalised treatment concepts in extraocular (periocular) cancer; indirect evidence (eyelid melanoma) |
| [40878071](https://pubmed.ncbi.nlm.nih.gov/40878071/) | 2025 | Case report | South Dakota Medicine | Malignant melanoma developing during encorafenib + cetuximab therapy; a safety signal, not efficacy evidence |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16824P | BRAFTOVI HARD CAPSULE 75MG | Capsule | Not stated in the licence record |
| SIN16825P | BRAFTOVI HARD CAPSULE 50MG | Capsule | Not stated in the licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BRAF kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; regular skin examination is advisable, because BRAF inhibitors are associated with new cutaneous malignancies (see the case reports above) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified (20 listed in the data compiled for this report). Major-level interactions include:
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Dolasetron
  - Cisapride

  Moderate-level interactions include famotidine, metformin, loperamide, bisacodyl, picosulfuric acid, polyethylene glycol, saxagliptin, eliglustat, empagliflozin, linagliptin, castor oil, fidaxomicin, glyburide, glycerin and granisetron.
- **Skin monitoring**: Case reports describe new melanomas arising during BRAF inhibitor therapy, so patients should be monitored for new or changing skin lesions.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (non-cutaneous melanoma, BRAF V600-mutant patients only). **Hold** for choroideremia and the other predictions with no clinical or mechanistic support.

**Rationale:**
- Encorafenib is already marketed in Singapore, and its BRAF/MAPK mechanism plausibly extends to BRAF V600-mutant non-cutaneous melanoma.
- Supporting evidence is a Phase 2 trial and a large observational study, both mainly in cutaneous melanoma, plus case reports.
- Choroideremia has no mechanistic link to encorafenib, and the high score is likely a model artefact.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (HSA), which are blocking for safety screening
- Mechanism of action data (DrugBank)
- BRAF V600 mutation testing to select patients, since uveal and some other non-cutaneous melanomas are rarely BRAF-mutant
- Subtype-specific efficacy data in non-cutaneous melanoma
- Review of the Major drug interactions (aprepitant, dexamethasone, clarithromycin, dolasetron, cisapride) and a skin monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

