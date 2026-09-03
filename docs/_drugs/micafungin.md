---
layout: default
title: Micafungin
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
---

# Micafungin
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

# Micafungin: From Antifungal Therapy to Candida Urinary Tract Infection

## One-Sentence Summary

Micafungin is an echinocandin-class antifungal, originally developed to treat systemic/invasive fungal infections by inhibiting fungal cell wall synthesis.
The TxGNN model predicts it may be effective for **Candida-caused Urinary Tract Infection (candiduria)**,
with **0 clinical trials** but **13 supporting publications** (mostly case reports/series and one pharmacokinetic study) currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antifungal therapy (echinocandin class) — specific Singapore-approved indication text not available |
| Predicted New Indication | Urinary Tract Infection — specifically Candida spp. infection (candiduria), not bacterial UTI |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for Micafungin is currently flagged as a data gap pending confirmation via the DrugBank API. Based on information available in this evidence pack, Micafungin is an echinocandin-class antifungal that inhibits fungal 1,3-β-D-glucan synthase, disrupting fungal cell wall synthesis. This mechanism is fungicidal/fungistatic against *Candida* species, including azole-resistant strains such as *C. krusei*, *C. glabrata*, and the emerging multidrug-resistant *C. auris*.

The predicted new indication — urinary tract infection — overlaps with the drug's original antifungal use only where the causative organism is *Candida*, not bacteria. Echinocandins have historically been under-used for UTIs due to low urinary excretion, but the literature in this pack includes a dedicated pharmacokinetic study (PMID 27424599) showing that urinary micafungin concentrations are in fact sufficient to treat *Candida* UTIs, supporting the biological plausibility of this repurposing signal. Multiple retrospective cohorts and case series further describe real-world use of micafungin (including in pediatric, transplant, and neonatal patients) for candiduria refractory to fluconazole or amphotericin B.

It is important to note that of the 10 indications TxGNN predicted for Micafungin, only this one (Candida UTI) is mechanistically coherent and evidence-supported. The remaining nine — *Ureaplasma* urethritis, gonococcal urethritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis, three mesothelioma subtypes, and urogenital tuberculosis — involve bacteria, mycobacteria, or malignancies that lack the fungal glucan cell wall target and have no supporting clinical or literature evidence (all scored L5/Hold in this pack). This report therefore focuses on the top-ranked, evidence-backed prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | Pharmacokinetic Study | Int J Antimicrob Agents | Urinary micafungin levels shown sufficient to treat Candida UTI; TDM of urinary levels may optimize outcomes despite low urinary excretion |
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Cohort/Case Series (pediatric) | Pediatr Int | Outcomes of critically ill PICU patients treated with micafungin for hospital-acquired Candida UTI; success rates varied by species |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Retrospective Cohort | Int Urol Nephrol | Examined candiduria elimination rates among hospitalized patients treated with micafungin |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Multi-institutional Cohort Study | Antimicrob Agents Chemother | Retrospective cohort of 305 hospitalized patients characterizing candiduria management and antifungal overtreatment patterns |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case Report | Transplant Infect Dis | Successful eradication of chronic *C. krusei* UTI with increased-dose micafungin in a liver/kidney transplant recipient |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case Report | Front Pediatr | Micafungin used to treat *C. glabrata* urinary infection in a catheterized premature neonate |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case Report | Cureus | *Candida auris* UTI in a multi-comorbid nursing home patient |
| [39781278](https://pubmed.ncbi.nlm.nih.gov/39781278/) | 2025 | Epidemiological Survey/Review | Ther Adv Infect Dis | Distribution and antifungal susceptibility of *Candida* species causing UTI/vulvovaginal candidiasis in Vietnam, 2023 |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case Series | Med Mycol Case Rep | Five cases of candiduria treated with parenteral micafungin; fungal clearance achieved within 30 days |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case Report | Med Mycol Case Rep | Unilateral renal fungus ball from *C. glabrata*, sensitive to micafungin, managed with antifungal therapy plus endoscopic extraction |

---

## Singapore Market Information

Micafungin currently has no marketing authorization registered in Singapore (0 licenses on file; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Real-world cohort and case-series evidence, supported by a dedicated pharmacokinetic study, consistently shows micafungin achieves adequate urinary concentrations and clinical success against azole-resistant *Candida* UTIs (L3 evidence), but no RCTs exist and this applies only to fungal — not bacterial — UTI. Critically, HSA-equivalent label warnings/contraindications are a **Blocking** data gap that must be resolved before this candidate can enter safety review.

**To proceed, the following is needed:**
- Official label warnings and contraindications (currently a Blocking data gap; source: local regulatory label)
- Confirmed mechanism-of-action documentation from DrugBank (High-severity gap)
- Drug-drug interaction data (current query returned not_found)
- Confirmation that scope is limited to Candida-caused UTI, to prevent misapplication to bacterial UTI
- Singapore-specific regulatory pathway assessment, since the drug is currently unmarketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

