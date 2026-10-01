---
layout: default
title: Luliconazole
parent: Medium Evidence (L3-L4)
nav_order: 614
evidence_level: L3
indication_count: 10
---

# Luliconazole
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

# Luliconazole: From Topical Antifungal Use (Nail Solution) to Pityriasis Versicolor

## One-Sentence Summary

Luliconazole is a topical imidazole antifungal. Its only Singapore product is a 5% nail solution, and the HSA record lists no approved indication text.
The TxGNN model predicts it may be effective for **pityriasis versicolor**, a Malassezia yeast skin infection.
Evidence is early: **1 registered clinical trial** (not yet recruiting), **1 published randomized trial** whose results could not be verified, and **2 in vitro studies**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA record. The registered product is a 5% nail solution, which is consistent with onychomycosis (inferred, not confirmed). |
| Predicted New Indication | Pityriasis versicolor |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset. Based on known class pharmacology, luliconazole is a topical imidazole. It inhibits lanosterol 14-alpha-demethylase (CYP51), which depletes ergosterol and disrupts the fungal cell membrane.

Pityriasis versicolor is caused by Malassezia yeasts, which are azole-susceptible. An in vitro study of NND-502, the development code for luliconazole, showed activity against the three major Malassezia species (PMID 12636984). Another paper notes luliconazole has been used clinically for pityriasis versicolor (PMID 29198426), though that paper is an in vitro study on Candida.

The link between the original and new indication is therefore fungal infection of the skin and nails. This is a reasonable extension, but it rests on class pharmacology and laboratory data rather than on confirmed human efficacy data in the pack.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07333170](https://clinicaltrials.gov/study/NCT07333170) | Phase 4 | Not yet recruiting | 86 | Randomized head-to-head comparison of luliconazole 2% cream vs ketoconazole 1% cream in pityriasis versicolor (planned 2026-02 to 2026-11). No results yet. |

This trial tests a **2% cream**, not the 5% nail solution registered in Singapore.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27559523](https://pubmed.ncbi.nlm.nih.gov/27559523/) | 2016 | Prospective open RCT (per title) | Indian Dermatol Online J | Compared topical ketoconazole and topical luliconazole in pityriasis versicolor at an Indian hospital. No abstract was available, so results, phase and design could not be verified. |
| [12636984](https://pubmed.ncbi.nlm.nih.gov/12636984/) | 2003 | In vitro | Int J Antimicrob Agents | NND-502 (luliconazole) was tested against M. furfur, M. sympodialis and M. slooffiae. Geometric mean MICs were about 1.4, 0.1 and 1.0 mg/l respectively. |
| [29198426](https://pubmed.ncbi.nlm.nih.gov/29198426/) | 2018 | In vitro | J Mycol Med | Luliconazole activity against Candida strains. The paper states that luliconazole has been used clinically for pityriasis versicolor, but it does not test Malassezia. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16428P | LUCONAC EXTERNAL SOLUTION FOR NAILS 5% w/w (Sato Pharmaceutical) | Solution | Not listed in the record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, and one comparative RCT has been published. However, the only registered trial has not started, the published RCT could not be verified, and the pack has no safety data. The pack labels this a "Research Question" at stage S1. The Singapore product (5% nail solution) also differs from the formulation being studied (2% cream).

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications, which are a blocking gap for safety screening
- Confirmation of the design and efficacy results of PMID 27559523
- Results from NCT07333170, expected after its planned 2026-11 completion
- A decision on formulation and route, since a cream or other skin-applied form for pityriasis versicolor is not in the Singapore registration
- Detailed mechanism of action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

