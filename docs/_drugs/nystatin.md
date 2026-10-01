---
layout: default
title: Nystatin
parent: Medium Evidence (L3-L4)
nav_order: 720
evidence_level: L3
indication_count: 10
---

# Nystatin
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

# Nystatin: From Antifungal Use to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal, but the Singapore registration data do not record its approved indications.
The TxGNN model predicts it may be effective for **Vulvovaginitis**, with **0 registered clinical trials** and **20 publications** (mostly reviews, plus in vitro, animal and observational work).
The evidence points to established antifungal use for Candida vulvovaginitis rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration data (nystatin is a polyene antifungal) |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The DrugBank mechanism field was not populated for this record. The mechanism below comes from the evidence assessment. Nystatin binds ergosterol in fungal cell membranes and forms pores, causing leakage and cell death. This fits Candida-driven vulvovaginitis directly. Candida albicans accounts for 85–90% of vulvovaginal candidiasis cases, and vaginal use gives high local exposure with minimal systemic absorption.

The literature shows nystatin already used for vulvovaginal candidiasis, including in fluconazole-resistant disease and in fixed combinations with other vaginal agents. The prediction therefore largely restates established use. Local labelling should be checked before this is classed as repurposing.

Vulvovaginitis has several causes, and an antifungal only addresses the fungal component. Bacterial or mixed vaginitis needs different or combined treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No randomized controlled trials were found among the 20 publications. The table lists the 10 most relevant items, in priority order. PMID 8193418 (metronidazole hypersensitivity) was retrieved but is not about nystatin, so it is excluded.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | Vulvovaginal candidiasis is the second most common cause of vaginitis after bacterial vaginosis. C. albicans causes 85–90% of cases. |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Management of fluconazole-resistant vulvovaginal candidiasis. Nystatin is among the alternatives discussed, alongside boric acid, oteseconazole and ibrexafungerp. |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Womens Health | Recurrent vulvovaginal candidiasis is hard to manage. Non-albicans Candida species are more resistant to azoles. |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Review | Ceska Gynekologie | Mixed and miscellaneous vulvovaginal infections treated with combined vaginal products containing nifuratel and nystatin. |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstet Gynecol Clin North Am | Nystatin was introduced in the 1950s for vulvovaginal candidiasis. Imidazoles and triazoles have since become first choice. |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | 287 Candida isolates from 283 patients with complicated vulvovaginal candidiasis. In vitro fluconazole and nystatin susceptibility was correlated with clinical outcome. |
| [21918792](https://pubmed.ncbi.nlm.nih.gov/21918792/) | 2012 | Observational study | Acta Derm Venereol | Fluconazole and nystatin efficacy compared in Brazilian women with vaginal Candida (932 women screened, 114 culture-positive). |
| [31969236](https://pubmed.ncbi.nlm.nih.gov/31969236/) | 2019 | Clinical study | Acta Dermatovenerol Croat | GENIE study (189 subjects). The oxytetracycline plus nystatin vaginal tablet was reported beneficial in unspecific and mixed vulvovaginal infections. |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Animal study | BMC Microbiology | In a rat model, nystatin enhanced the vaginal immune response to C. albicans and protected the epithelial ultrastructure. |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | In vitro | Infect Drug Resist | Antifungal activity of ZnO nanoparticles and nystatin against fluconazole-resistant C. albicans from vulvovaginal candidiasis. |

---

## Singapore Market Information

The registration data list no approved indication text for any of the 4 licences.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN05499P | PMS-NYSTATIN SUSPENSION 500,000 u/5 ml | Suspension | Pendopharm / Halo Pharmaceutical Canada Inc. |
| SIN06750P | NYSTATIN VAGINAL TABLET 100,000 units | Tablet | Yung Shin Pharmaceutical Ind Co Ltd |
| SIN03798P | FLAGYSTATIN VAGINAL OVULE | Suppository | PT Kalventis Sinergi Farma |
| SIN07745P | POLYGYNAX VAGINAL CAPSULE | Capsule | Catalent France Beinheim SA / Swiss Caps AG / Innothera Chouzy |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism fits Candida vulvovaginitis well, and Singapore already has vaginal nystatin products on the market. However, the support is review-level and observational evidence at L3, with no registered trials and no Phase 3 RCTs. The other nine predicted indications are weakly supported. Vulvitis (L4) is a research question, and the rest are Hold with no supporting evidence.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is currently missing and blocks safety screening
- Confirmation of the approved indication on the local labels, to decide whether this is repurposing or existing use
- Diagnostic distinction of Candida from bacterial or mixed vaginitis
- Consideration of azole-resistant or non-albicans Candida species
- DrugBank mechanism-of-action data to complete the mechanistic analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

