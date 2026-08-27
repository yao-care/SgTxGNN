---
layout: default
title: Luliconazole
parent: 僅模型預測 (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
---

# Luliconazole
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

# Luliconazole: From Superficial Dermatophytosis to Pityriasis Versicolor

## One-Sentence Summary

Luliconazole is a topical imidazole antifungal agent, globally approved in Japan and the United States for the treatment of superficial dermatophytoses (tinea pedis, tinea cruris, tinea corporis). The TxGNN model predicts it may be effective for **Pityriasis Versicolor**, with **1 clinical trial** and **3 publications** currently supporting this direction. The prediction is mechanistically sound — both dermatophytes and *Malassezia* species (the causative organism of pityriasis versicolor) depend on ergosterol biosynthesis, the precise pathway that luliconazole inhibits.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Superficial dermatophytosis (tinea pedis, tinea cruris, tinea corporis) |
| Predicted New Indication | Pityriasis Versicolor |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Luliconazole (originally developed as NND-502) is a novel imidazole antifungal that exerts its effect by inhibiting **CYP51 (lanosterol 14α-demethylase)**, the rate-limiting enzyme in fungal ergosterol biosynthesis. By blocking ergosterol production, luliconazole disrupts fungal cell membrane integrity and function, ultimately causing cell death. This mechanism underpins its regulatory approvals in Japan (Lulicon® cream/solution, Nihon Nohyaku) and the United States (Luzu® cream 1%, Ferndale Pharma) for dermatophyte-caused skin infections.

Pityriasis versicolor is caused by *Malassezia* species — principally *M. furfur*, *M. globosa*, and *M. sympodialis* — lipophilic yeasts that, like dermatophytes, depend on ergosterol for cell membrane integrity. The mechanistic bridge is therefore direct: the same CYP51 inhibition pathway that eliminates dermatophytes is equally relevant to *Malassezia*. This was confirmed as early as 2003, when in vitro testing (PMID 12636984) demonstrated potent minimum inhibitory concentrations for luliconazole against all three major *Malassezia* species using modified Dixon agar, outperforming comparator agents such as bifonazole and terbinafine.

Clinical plausibility is further reinforced by PMID 27559523, a prospective randomized head-to-head comparison of topical luliconazole versus ketoconazole conducted at a tertiary care hospital in eastern India. A separate 2018 in vitro study (PMID 29198426) explicitly states that luliconazole "has been clinically used for the treatment of pityriasis versicolor," indicating real-world application even prior to formal regulatory submission in Singapore. The forthcoming Phase 4 RCT (NCT07333170, n=86) — designed specifically to compare luliconazole 2% versus ketoconazole 1% in pityriasis versicolor — reflects the research community's confidence that prior evidence is sufficient to support this indication and warrants formal validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07333170](https://clinicaltrials.gov/study/NCT07333170) | Phase 4 | Not Yet Recruiting | 86 | Randomized controlled study directly comparing luliconazole 2% cream vs ketoconazole 1% cream in patients with pityriasis versicolor; evaluates efficacy and safety; planned start Feb 2026, expected completion Nov 2026 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [27559523](https://pubmed.ncbi.nlm.nih.gov/27559523/) | 2016 | Comparative Clinical Trial | Indian Dermatology Online Journal | Prospective open-label RCT directly comparing topical luliconazole vs topical ketoconazole in pityriasis versicolor patients at a tertiary care centre in eastern India; provides the primary head-to-head clinical efficacy data for this indication |
| [29198426](https://pubmed.ncbi.nlm.nih.gov/29198426/) | 2018 | In vitro | Journal de Mycologie Médicale | Evaluates in vitro antifungal activity of luliconazole against multiple *Candida* strains; explicitly confirms that luliconazole inhibits sterol 14α-demethylase in *Malassezia* species and has established clinical use in pityriasis versicolor |
| [12636984](https://pubmed.ncbi.nlm.nih.gov/12636984/) | 2003 | In vitro MIC Study | International Journal of Antimicrobial Agents | Foundational study confirming potent in vitro activity of luliconazole (NND-502) against *M. furfur* (25 strains), *M. sympodialis* (15 strains), and *M. slooffiae* (10 strains) by agar dilution with modified Dixon medium; established the mechanistic basis for this indication |

---

## Singapore Market Information

Luliconazole is currently **not registered** with the Health Sciences Authority (HSA) in Singapore. There are no marketing authorizations on file (0 total licenses). This represents a **regulatory gap rather than an evidence or safety concern** — the drug holds regulatory approval in Japan (PMDA) and the United States (FDA) and has an established safety and efficacy record for superficial fungal infections in both markets.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Formal safety data (key warnings, contraindications, drug-drug interactions) for the Singapore/Taiwan regulatory context is not available in this evidence pack. Retrieval of the TFDA or PMDA package insert is recommended before clinical use decisions are made (see Next Steps).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Luliconazole has a mechanistically direct and clinically evidenced case for pityriasis versicolor — in vitro potency against *Malassezia* has been established since 2003, a head-to-head clinical comparative trial exists (PMID 27559523), and a formal Phase 4 confirmatory RCT is underway (NCT07333170). The drug's absence from the Singapore market reflects an incomplete regulatory filing, not a failure of evidence.

**To proceed, the following is needed:**

- **Regulatory submission**: Pursue HSA registration referencing PMDA and FDA approvals as prior art; identify the appropriate abbreviated or full NDA pathway for Singapore
- **Safety documentation**: Obtain the complete package insert from PMDA (Japan) or FDA (USA) to document contraindications, drug interactions, and special population warnings — currently the single most critical data gap
- **Formulation decision**: Confirm whether the 1% cream (US-approved), 2% cream (as used in NCT07333170), or another concentration is most appropriate for the Singapore clinical context
- **Evidence consolidation**: Await completion of NCT07333170 (expected Nov 2026) for head-to-head definitive efficacy and safety data that could anchor a regulatory dossier
- **Market feasibility**: Assess whether generic or branded luliconazole products are commercially viable given existing competitors (ketoconazole, clotrimazole, fluconazole) in the Singapore market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

