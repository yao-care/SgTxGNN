---
layout: default
title: Letermovir
parent: Low Evidence (L5)
nav_order: 588
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Letermovir: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Cytomegalovirus infection"
---

# Letermovir
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

# Letermovir: From Cytomegalovirus Infection to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is an antiviral that was originally used to treat and prevent cytomegalovirus (CMV) infection.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but **no clinical trials and no publications** currently support this prediction.
The mechanistic rationale is also weak, so this top-ranked prediction is most likely a network-prediction artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cytomegalovirus infection |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled dataset. From general pharmacology, letermovir inhibits the CMV terminase complex (pUL56/UL51/UL89), which cleaves and packages viral DNA into new virus particles. This target is specific to herpesviruses.

Vulvovaginal candidiasis is a fungal infection. Candida has no terminase complex comparable to the one in CMV, so there is no plausible mechanistic link between letermovir and this disease. The very high TxGNN score most likely reflects patterns in the knowledge network, not real biological activity. No trials or literature were found to support it.

**Other predictions worth noting:** Among the other predicted indications, most (for example tinea nigra, dermatophytosis, piedra, and several veterinary herpesvirus diseases) also lack any evidence or mechanistic basis. Two are more interesting as research questions:
- **AIDS (HIV-associated inflammation):** Letermovir does not act on HIV. The hypothesis is that suppressing low-level CMV replication in people living with HIV on antiretroviral therapy may reduce chronic inflammation and immune activation. Evidence level L2, with small trials as described below.
- **Varicella zoster infection:** VZV is a herpesvirus with its own terminase, so a class-level hypothesis is plausible. However, letermovir's activity against VZV has not been shown, and only in vitro data would be a reasonable first step. Evidence level L4.

## Clinical Trial Evidence

Currently no related clinical trials registered for vulvovaginal candidiasis.

For reference, the following trials relate to the HIV-associated inflammation direction (a separate predicted indication):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04840199](https://clinicaltrials.gov/study/NCT04840199) | Phase 2 | Terminated | 44 | Open-label randomized trial of letermovir's anti-inflammatory effect in people with HIV and asymptomatic CMV on suppressive ART, 48 weeks |
| [NCT05362916](https://clinicaltrials.gov/study/NCT05362916) | N/A | Completed | 33 | 3-month letermovir course and its effect on gut inflammation (blood LPS) in ART-treated, CMV-seropositive people with HIV |
| [NCT06626555](https://clinicaltrials.gov/study/NCT06626555) | Phase 2 | Not yet recruiting | 36 | Pilot open-label trial of letermovir's effect on T-cell immune activation in treated HIV-1 infection |

## Literature Evidence

Currently no related literature available for vulvovaginal candidiasis.

For the related "fungal infectious disease" prediction, the retrieved publications are indirect. They concern fungal infections in transplant recipients who receive letermovir prophylaxis, and do not show antifungal efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41371495](https://pubmed.ncbi.nlm.nih.gov/41371495/) | 2026 | Cohort | J Infect Chemother | Examines the relationship between letermovir prophylaxis and bacteremia or invasive fungal infection after allogeneic HCT |
| [42834112](https://pubmed.ncbi.nlm.nih.gov/42834112/) | 2026 | Cohort | Bone Marrow Transplant | Safety of letermovir-triazole co-administration regarding invasive fungal infection risk |
| [32245201](https://pubmed.ncbi.nlm.nih.gov/32245201/) | 2020 | Review | J Clin Med | Updates on preventing and managing infections in stem cell transplant recipients |
| [33965172](https://pubmed.ncbi.nlm.nih.gov/33965172/) | 2021 | Review | Transplant Cell Ther | Infection prophylaxis, monitoring and therapy guidelines in cord blood transplantation |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15757P | PREVYMIS FILM COATED TABLET 240MG | Tablet, film coated | Not available in the compiled data |
| SIN15758P | PREVYMIS FILM COATED TABLET 480MG | Tablet, film coated | Not available in the compiled data |
| SIN15759P | PREVYMIS CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/ML | Infusion, solution concentrate | Not available in the compiled data |

## Safety Considerations

- **Drug Interactions:** The interaction screen returned 100 interacting drugs. Examples of **Major** interactions include eliglustat, naloxegol and cisapride. Examples of **Moderate** interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), clarithromycin, omeprazole, lansoprazole, aprepitant, and several antidiabetic drugs (pioglitazone, glimepiride, saxagliptin, chlorpropamide).
- Clinically relevant interactions with triazole antifungals have also been discussed in the literature, which matters if letermovir were ever combined with antifungal therapy.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, vulvovaginal candidiasis, has no trials, no literature, and no plausible mechanism, because letermovir's target is a herpesvirus-specific terminase absent in fungi. The high TxGNN score alone is not sufficient to justify further investment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (from the HSA website), which are currently missing
- Mechanism of action data (for example from DrugBank)
- If any new direction is pursued, prioritize the HIV-associated inflammation hypothesis (results from NCT05362916 and the reasons for termination of NCT04840199) or in vitro activity testing against VZV, rather than antifungal indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

