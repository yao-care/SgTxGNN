---
layout: default
title: Econazole
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
---

# Econazole
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

# Econazole: From Superficial Antifungal to Majocchi Granuloma

## One-Sentence Summary

Econazole is a broad-spectrum imidazole antifungal agent used globally for superficial dermatomycoses and cutaneous candidiasis, but currently holds no marketing authorization in Singapore.
The TxGNN model predicts it may be effective for **Majocchi Granuloma**, with **0 clinical trials** and **0 publications** directly supporting this specific indication.
Across the full top-10 prediction set, notably stronger evidence exists for related fungal indications: **vulvovaginal candidiasis** (rank 7, L2) is supported by at least **5 direct RCTs** featuring econazole, and **superficial mycosis** (rank 4, L3) carries **19 supporting publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally established for superficial dermatomycoses and cutaneous candidiasis |
| Predicted New Indication | Majocchi Granuloma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only; no direct clinical studies identified) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known information, Econazole is an imidazole-class antifungal that inhibits CYP51 (lanosterol 14α-demethylase), blocking ergosterol biosynthesis and disrupting fungal membrane integrity. Its broad-spectrum fungistatic and fungicidal activity against dermatophytes (*Trichophyton*, *Microsporum*, *Epidermophyton*), yeasts (*Candida* spp.), and dimorphic fungi has been established in both in vitro and clinical settings over decades.

Majocchi granuloma is a rare deep dermatophyte infection — predominantly caused by *Trichophyton rubrum* — in which organisms invade the hair follicle below the infundibulum and into the deep dermis and subcutis, provoking a perifollicular granulomatous response. Because econazole's CYP51 inhibition mechanism is directly active against *T. rubrum*, the mechanistic link to Majocchi granuloma is biologically sound.

The critical constraint, however, is tissue penetration. Majocchi granuloma lesions are located in the deep dermis — well beyond the reach of conventional topical econazole preparations. Clinical guidelines consistently require systemic antifungals (oral terbinafine or itraconazole) for this condition; topical imidazoles are regarded as insufficient as monotherapy. The high TxGNN score likely reflects the tight mechanistic alignment between econazole and dermatophyte biology at a knowledge-graph level, rather than a currently actionable clinical opportunity with available formulations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Econazole in Majocchi Granuloma.

---

## Literature Evidence

Currently no related literature available for Econazole in Majocchi Granuloma.

---

## Singapore Market Information

Econazole is currently not registered in Singapore. No product authorizations are on record (total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or published literature evidence supports econazole for Majocchi granuloma, and the route-of-administration mismatch — topical formulation versus a deep tissue infection requiring systemic penetration — makes this prediction clinically impractical with existing dosage forms.

**To proceed, the following is needed:**

- **MOA and susceptibility data**: Confirm econazole's CYP51 inhibition profile and minimum inhibitory concentration (MIC) data against *T. rubrum* to formally characterize the mechanistic link
- **Novel formulation research**: Evaluate whether nanoparticle-based or lipid-carrier econazole delivery systems (see PMID [26883854](https://pubmed.ncbi.nlm.nih.gov/26883854/) on imprinted textile delivery) could achieve therapeutic concentrations in deep dermal tissue
- **Case reports or observational data**: Identify any case series where econazole was used adjunctively in Majocchi granuloma, including combination with systemic therapy
- **Safety profile retrieval**: Obtain full prescribing information (warnings, contraindications, DDIs) from a reference market where econazole is licensed, to complete the S1 safety assessment
- **Consider prioritizing a higher-evidence indication**: Within this Evidence Pack, **vulvovaginal candidiasis** (rank 7, L2 evidence, ≥5 direct econazole RCTs dating from 1976–2011, recommendation: Proceed with Guardrails) and **vulvovaginitis** (rank 8, L2, similar RCT base) represent significantly more actionable repurposing candidates for Singapore regulatory evaluation — both have direct econazole clinical data and an established formulation route (vaginal pessary/cream)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

