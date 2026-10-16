---
layout: default
title: Posaconazole
parent: Medium Evidence (L3-L4)
nav_order: 809
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Posaconazole: predicted new indication Pneumocystosis (evidence level L4). Approved use: Invasive and superficial fungal infections (e.g., aspergillosis…"
monitor_inn: "Posaconazole"
predicted_indications: ["pneumocystosis", "vulvovaginal candidiasis", "leprosy", "multibacillary leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "syndrome with a Dandy-Walker malformation as major feature", "hypertrichosis (disease)", "paucibacillary leprosy"]
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Posaconazole: From Invasive Fungal Infections to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal originally used for fungal infections such as aspergillosis, candidiasis, histoplasmosis and sporotrichosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but the evidence is very weak: **1 related Phase 3 trial** (which tests a different drug) and **5 publications** (guidelines, reviews and a retrospective cohort, none showing posaconazole efficacy in this disease).
The mechanistic review in the data compiled for this report points to a likely model artifact rather than a true repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive and superficial fungal infections (e.g., aspergillosis, candidiasis, histoplasmosis, sporotrichosis, fusariosis, mycetoma). The Singapore licence records contain no approved indication text. |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general knowledge, posaconazole is a triazole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase) and blocks ergosterol synthesis. This is the basis of its activity against *Aspergillus*, *Candida* and other moulds and yeasts.

Pneumocystosis is a fungal-classified lung infection, which probably explains the high model score through the general association of "antifungal" with "fungal disease". Mechanistically, however, the link is weak: *Pneumocystis jirovecii* lacks ergosterol in its cell membrane and uses cholesterol instead, so the azole target is largely absent. The standard treatment is trimethoprim-sulfamethoxazole. The high score likely reflects the drug's class association rather than a true mechanistic fit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Rezafungin vs the standard antimicrobial regimen for preventing invasive fungal disease after allogeneic blood and marrow transplantation (ReSPECT). Posaconazole may be part of the comparator regimen, but the trial gives no direct evidence of posaconazole efficacy against pneumocystosis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Med Wkly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and Pneumocystis pneumonia. Notes that mould-active posaconazole prophylaxis reduced invasive fungal infections in high-risk haemato-oncology patients. |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guideline | Lancet Infect Dis | British Society for Medical Mycology 2025 update on diagnosing serious fungal diseases. Diagnostic focus, no posaconazole efficacy data. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Zhonghua Jie He He Hu Xi Za Zhi | Chinese guidelines (2025) for diagnosing and managing invasive pulmonary fungal disease. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid (pharmacokinetics only). |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transpl Infect Dis | Retrospective study of infectious complications in acute graft-versus-host disease after liver transplantation. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13654P | NOXAFIL ORAL SUSPENSION 40 mg/ml | Suspension | Not specified in the available records |
| SIN15045P | NOXAFIL TABLET 100MG | Delayed-release tablet | Not specified in the available records |
| SIN15897P | POSACONAZOLE SANDOZ GASTRO-RESISTANT TABLETS 100MG | Delayed-release tablet | Not specified in the available records |
| SIN16477P | SINOTRX POSACONAZOLE DELAYED RELEASE TABLET 100MG | Delayed-release tablet | Not specified in the available records |
| SIN17200P | POSATIF POSACONAZOLE GASTRO-RESISTANT TABLETS 100MG | Delayed-release tablet | Not specified in the available records |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. Examples of **Major** interactions include loperamide, triamcinolone and budesonide. Examples of **Moderate** interactions include acid-suppressing drugs (famotidine, ranitidine, rabeprazole, omeprazole, cimetidine), corticosteroids (hydrocortisone, dexamethasone, betamethasone), aprepitant, clarithromycin, saxagliptin, and several bowel-preparation laxatives (bisacodyl, picosulfuric acid, polyethylene glycol).
- **Developmental toxicity**: Teratogenic signals in animal studies are noted in the review of the related predicted indications. This weighs against use in developmental or congenital conditions.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a class-level association. *Pneumocystis* lacks ergosterol, so posaconazole's mechanism is not expected to work. The only trial found tests another drug, and the literature contains no efficacy evidence. Trimethoprim-sulfamethoxazole is the established standard of care.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently missing, and this blocks safety screening)
- Detailed mechanism of action data
- Preclinical or clinical data showing posaconazole activity against *Pneumocystis*
- Comparative evidence against trimethoprim-sulfamethoxazole

**Other predictions reviewed:** The remaining nine predictions were also rated Hold. Vulvovaginal candidiasis has a plausible mechanism but is effectively an existing candidiasis indication, with only in vitro and epidemiology literature and cheaper alternatives available. The leprosy variants (the bacterial pathogen has no ergosterol pathway) and the genetic or congenital conditions (hypertrichosis, hair shaft abnormalities, Dandy-Walker and dental malformation syndromes) have no mechanistic link and no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

