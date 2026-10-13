---
layout: default
title: Binimetinib
parent: Low Evidence (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Binimetinib
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

# Binimetinib: From Metastatic Melanoma to Choroideremia

## One-Sentence Summary

Binimetinib is an oral MEK inhibitor originally used to treat metastatic melanoma.
The TxGNN model's top-ranked prediction is **Choroideremia** (score 98.6%), but this prediction has **0 clinical trials** and **0 publications** behind it. The only prediction with meaningful supporting evidence is a group of melanoma subtypes (non-cutaneous, mucosal, acral), where **6 clinical trials** (mostly Phase 1/2) and **1 case report** exist.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

Note: The other nine predictions are mostly melanoma subtypes. Three of them reach L2 (non-cutaneous melanoma, mucosal melanoma, acral lentiginous melanoma), and these are discussed below as the more realistic research directions.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, binimetinib inhibits MEK1/2, which sit downstream of BRAF/RAS in the MAPK pathway. Its efficacy in BRAF V600-mutant melanoma has been established, usually in combination with encorafenib.

**Choroideremia (top prediction):** The mechanistic link is weak. Choroideremia is an X-linked retinal degeneration caused by loss of function of the CHM/REP1 gene, and MEK inhibition has no established connection to this process. The high score of 0.986 is most likely driven by network proximity in the knowledge graph rather than by biology. It should be treated as a model artefact until proven otherwise.

**Melanoma subtypes (more plausible):** Most other predictions are melanoma variants, which are biologically close to the original indication:
- **Non-cutaneous melanoma and mucosal melanoma:** BRAF V600 mutations are less common than in cutaneous melanoma (KIT, NRAS and NF1 alterations are more frequent). Uveal melanoma is typically GNAQ/GNA11-driven and less BRAF-dependent. MAPK inhibition is plausible mainly in BRAF- or NRAS-mutant cases.
- **Acral lentiginous melanoma:** BRAF V600 frequency is lower, so benefit would be mutation-dependent.
- **Superficial spreading, scrotal and eyelid melanoma:** These are cutaneous or site-specific variants where MAPK inhibition is plausible, but any benefit would be an extrapolation from the approved indication.
- **Lentigo maligna melanoma and CDK4-linked melanoma:** The rationale is weaker. BRAF V600 is less frequent in lentigo maligna melanoma, and CDK4 variants act through the cell-cycle pathway, which is distinct from MEK.

---

## Clinical Trial Evidence

No clinical trials are registered for choroideremia. The trials below were identified for the melanoma-related predictions (mainly non-cutaneous, mucosal and acral melanoma).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04511013](https://clinicaltrials.gov/study/NCT04511013) | Phase 2 | Recruiting | 112 | Randomized: encorafenib + binimetinib + nivolumab vs ipilimumab + nivolumab in BRAF V600-mutant melanoma with brain metastases. No results yet. |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EBIN: 12 weeks of encorafenib + binimetinib followed by ipilimumab + nivolumab vs immunotherapy alone in BRAF V600-mutant melanoma. Population likely predominantly cutaneous. |
| [NCT04045691](https://clinicaltrials.gov/study/NCT04045691) | N/A | Recruiting | 750 | BERING-MELANOMA: non-interventional, real-world study of encorafenib + binimetinib in unresectable or metastatic BRAF V600-mutant melanoma. |
| [NCT05355701](https://clinicaltrials.gov/study/NCT05355701) | Phase 1 | Active, not recruiting | 103 | PF-07799933 alone or in combination in advanced BRAF-altered solid tumours. Binimetinib's role is unclear. |
| [NCT04913285](https://clinicaltrials.gov/study/NCT04913285) | Phase 1/1b | Recruiting | 400 | KIN-2787 in BRAF/NRAS-mutated solid tumours. Relevance to this drug is unclear. |
| [NCT04543188](https://clinicaltrials.gov/study/NCT04543188) | Phase 1 | Terminated | 65 | PF-07284890 alone or with binimetinib in BRAF V600-mutant solid tumours, with and without brain involvement. Limited interpretable evidence. |

None of these trials has reported results, and none is specific to a non-cutaneous, mucosal or acral subtype.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case report | Pigment Cell & Melanoma Research | Molecular profiling diagnosed epidermotropic metastatic melanoma in a patient who presented with eruptive primary-like melanomas. It contains no binimetinib efficacy data. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16826P | MEKTOVI FILM-COATED TABLET 15MG | Tablet, film coated | Not stated in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions:** The interaction screening returned 100 interacting drugs. Examples from the 20 listed:
- **Major:** deferasirox, ibritumomab tiuxetan, tositumomab, tositumomab (I-131), drotrecogin alfa
- **Moderate:** omeprazole, dexamethasone, clarithromycin, eliglustat, fidaxomicin, naloxone, naltrexone, rolapitant, simvastatin, tolbutamide, cobicistat, fostamatinib, eltrombopag, ticagrelor, albendazole

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, choroideremia, rests on model score alone. It has no trials or literature and no plausible biological link between MEK inhibition and CHM/REP1 loss of function.
- The melanoma subtypes (non-cutaneous, mucosal, acral) have limited support from ongoing Phase 2 trials without results. They are best treated as research questions rather than candidates for immediate repurposing.

**To proceed, the following is needed:**
- Mechanism of action data for binimetinib
- Package insert warnings and contraindications, which are required for safety screening
- The approved indication text for the Singapore registration
- Results from NCT04511013 and NCT03235245, and subtype-specific data (mutation profile) for mucosal, acral and non-cutaneous melanoma
- For choroideremia: preclinical evidence of a mechanistic link before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

