---
layout: default
title: Miconazole
parent: Medium Evidence (L3-L4)
nav_order: 671
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-28
description: "Miconazole: predicted new indication Acne (disease) (evidence level L3). Approved use: Tinea pedis, tinea corporis, cutaneous candidiasis, tinea unguium…"
monitor_inn: "Miconazole"
predicted_indications: ["acne (disease)"]
---

# Miconazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Miconazole: acne (disease)
{: .text-alpha }

## One-Sentence Summary

Miconazole is a topical azole antifungal, originally used for tinea (athlete's foot, ringworm, nail infection), cutaneous candidiasis, pityriasis versicolor and vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **acne**, with **no registered clinical trials** and **4 publications** (one review, two small clinical studies, one in vitro study) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, cutaneous candidiasis, tinea unguium, pityriasis versicolor, vulvovaginal candidiasis (from the knowledge graph; no approved-indication text is recorded in the Singapore licence data) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L3 |
| Singapore Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, miconazole is an imidazole antifungal that is understood to inhibit fungal ergosterol synthesis (CYP51). Its efficacy in superficial fungal skin infections is well established, and a historical review (PMID 16597199) notes it may also inhibit fungal peroxidases.

For acne, the link is indirect but plausible in three ways:
- **In vitro antibacterial activity:** Imidazole antifungals have been tested against *Propionibacterium acnes* (*Cutibacterium acnes*), the bacterium associated with acne vulgaris (PMID 20045949). This is attractive given rising antibiotic resistance.
- **Anti-*Malassezia* activity:** *Malassezia* causes Pityrosporum folliculitis, which is frequently misdiagnosed as acne (PMID 8593718). Miconazole may help in these look-alike cases, but that is a different condition from true acne.
- **Possible anti-inflammatory effect:** A review of miconazole's effects on skin disorders (PMID 18627330) and a small split-face study in catamenial (period-related) acne (PMID 15536660) suggest possible benefit.

The evidence is limited to small studies and laboratory data, so this should be treated as a hypothesis rather than an established use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | Overview of miconazole's multiple effects on skin disorders beyond its antifungal action |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical study (split-face, small) | Skin Res Technol | Clinical and instrument-based assessment in mild inflammatory catamenial acne; suggests possible benefit |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Clinical study | Clin Exp Dermatol | Pityrosporum folliculitis (62 patients) is often mistaken for acne vulgaris; diagnosis and therapeutic trials reported |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biol Pharm Bull | Azole antifungals tested for activity against *P. acnes* from acne patients, motivated by antibiotic resistance |

---

## Singapore Market Information

Miconazole has 20 valid single-ingredient registrations in Singapore, none cancelled. No approved-indication text is recorded for these products. Five main authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02028P | Daktarin Cream 20 mg/g (Janssen Pharmaceutica NV) | Cream | Not recorded |
| SIN10561P | Decozol Cream 2% w/w | Cream | Not recorded |
| SIN10022P | Fungitop Gel 2% w/w | Gel | Not recorded |
| SIN10836P | Resolve Solution 2% w/w | Solution | Not recorded |
| SIN11180P | Neo-Penotran Pessary | Suppository | Not recorded |

Other registered forms include a powder (Minazol) and several creams, including combination-named products such as Micon-H and Zaricort. All are classified as single-ingredient licences in the data.

---

## Safety Considerations

- **Disease-level cautions (knowledge graph):** Liver disease and gallbladder disease are flagged as contraindication-related conditions. These come from a knowledge graph, not from label text, and should be verified against the package insert.
- **Drug Interactions:** 100 interactions are recorded. Most are Moderate, a few are Minor, and none of those listed is Major. Examples of moderate interactions include paclitaxel, fentanyl, alfentanil, hydrocodone, acalabrutinib, nifedipine, amlodipine, amiodarone, amitriptyline, alprazolam, alfuzosin, aliskiren, alosetron, ethinylestradiol and estradiol. Many of these likely reflect CYP3A4 inhibition and are most relevant with systemic exposure. Topical use gives low systemic absorption, but interaction risk should still be considered, particularly in patients on warfarin-like or CYP3A4-sensitive drugs.

Package insert warnings and contraindications were not available. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9954), but there are no registered clinical trials and the supporting evidence is one review, two small clinical studies and one in vitro study. Some of this literature concerns Malassezia folliculitis, a different condition from acne. The idea is mechanistically plausible and the drug is already widely marketed topically in Singapore, but the data are not yet enough to support moving forward with a clinical programme.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A controlled trial (ideally randomised) of topical miconazole in acne vulgaris, with comparison against standard therapy
- Clear separation of true acne from Malassezia folliculitis in any study population
- Review of liver-related cautions and interaction risks, especially if systemic exposure is considered
- Assessment of formulation and route suitability for acne (not yet evaluated)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

