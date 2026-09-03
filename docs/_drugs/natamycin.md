---
layout: default
title: Natamycin
parent: 僅模型預測 (L5)
nav_order: 694
evidence_level: L5
indication_count: 10
---

# Natamycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Natamycin: From Antifungal Therapy to Vulvovaginal Candidiasis

## One-Sentence Summary

Natamycin is a polyene antifungal historically used topically and vaginally (e.g., as Pimafucin) against Candida infections, though it currently holds **no drug registration in Singapore**. The TxGNN model predicts it is highly applicable to **Vulvovaginal Candidiasis (VVC)**, supported by **1 completed Phase 3 RCT (n=218)** and **20 identified publications** spanning 1959–2025. Efficacy evidence is solid, but safety/labeling data needed for a formal risk assessment is currently missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in Singapore (no HSA license on file); globally known as a topical/vaginal antifungal (e.g., Pimafucin) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 (1 completed Phase 3 RCT) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in our structured DrugBank extract (data gap, pending DrugBank API query). Based on known pharmacology, Natamycin is a polyene macrolide antifungal that binds ergosterol in the fungal cell membrane, forming pores that cause leakage of cell contents and fungal death. This is the standard mechanism of action against *Candida* species — the causative organism of VVC — and the mechanistic link is direct and well established.

Natamycin's antifungal spectrum has historically supported vaginal, dermal, ophthalmic, and oral use against candidal infections. Vaginal natamycin formulations (branded Pimafucin) have already been approved in multiple countries specifically for VVC, which strongly corroborates the TxGNN prediction rather than representing a novel mechanistic hypothesis — the primary open question here is one of **local (Singapore) market registration**, not biological plausibility.

The strongest piece of supporting evidence is a completed, international, randomized, controlled Phase 3 trial (NCT06411314) testing a Natamycin + Lactulose combination against standard Natamycin (Pimafucin) monotherapy in non-pregnant adult women with VVC — directly matching both the population and treatment modality relevant to this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) | Phase 3 | Completed | 218 | International RCT comparing Natamycin 100mg + Lactulose 300mg vaginal suppositories vs. Pimafucin (Natamycin 100mg alone) vs. Lactulose alone in non-pregnant adult women with VVC; evaluated superiority efficacy and safety of the combination. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | RCT | BMC Women's Health | Published results of the Natamycin + Lactulose vaginal suppository RCT (same trial as NCT06411314) in adult women with VVC. |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | Comparative | Medical Journal of Australia | Comparative trial of amphotericin B (fungilin) vs. natamycin (pimafucin) pessaries for vaginal candidiasis. |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | Cohort | Acta Obstet Gynecol Scand | 33 patients treated with natamycin vaginal tablets ± partner treatment; cure rate 94% (partner treated) vs. 88% (placebo), not significantly different. |
| [1082689](https://pubmed.ncbi.nlm.nih.gov/1082689/) | 1975 | Clinical experience | Zentralblatt für Gynäkologie | Oral metronidazole + vaginal natamycin (Pimafucin) combination in mixed urogenital infections; 89% clinical cure of vaginal Candida mycoses. |
| [41412769](https://pubmed.ncbi.nlm.nih.gov/41412769/) | 2025 | Review/Survey | Ceska a Slovenska farmacie | Survey of 408 women in Lviv, Ukraine on VVC management; lifetime prevalence 72.6%. |
| [18288724](https://pubmed.ncbi.nlm.nih.gov/18288724/) | 2008 | Formulation study | Journal of Pharmaceutical Sciences | Natamycin–γ-cyclodextrin inclusion complex developed to improve solubility/stability for vaginal mucoadhesive formulations; MIC90 below 0.0313 µg/mL. |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | Comparative | Ceska Gynekologie | Compared natamycin vs. clotrimazole for diagnosis and treatment of chronic vaginal candidiasis. |
| [6972554](https://pubmed.ncbi.nlm.nih.gov/6972554/) | 1981 | Clinical study | Przeglad Dermatologiczny | Effectiveness of different natamycin formulations in cutaneous and mucosal multifocal candidiasis. |
| [4545913](https://pubmed.ncbi.nlm.nih.gov/4545913/) | 1972 | Clinical experience | Lekarske Fakulty Karlovy University | Clinical experience treating gynecological candidiasis and trichomoniasis. |
| [6767924](https://pubmed.ncbi.nlm.nih.gov/6767924/) | 1980 | Clinical experience | MMW Munchener Medizinische Wochenschrift | Treatment of vaginal candidiasis/mixed infections with a pimafucin-containing cream using a new application method. |

---

## Singapore Market Information

Natamycin currently holds **no HSA drug registration in Singapore** (0 licenses on file, market status: Not Marketed). No product listings, dosage forms, or approved indication text are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not currently available in our records (DDI query returned no results), and this is flagged as a **Blocking** data gap for formal safety evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (n=218) plus decades of consistent clinical literature support Natamycin's efficacy in VVC, and the mechanism (ergosterol-binding, membrane disruption) is well matched to the target pathogen. However, the drug is unregistered in Singapore and structured safety/labeling data is entirely absent, so guardrails are needed before further action.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed structured MOA data via DrugBank API (DG002)
- A completed drug-drug interaction (DDI) screen (current query: not found)
- Assessment of a Singapore market registration pathway, since Natamycin has 0 existing local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

