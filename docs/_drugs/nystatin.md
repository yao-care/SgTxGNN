---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 720
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: From Candidiasis to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal traditionally used to treat *Candida* (fungal) infections of the skin, mouth, and gastrointestinal tract. The TxGNN model predicts it may also be effective for **Vulvovaginitis** — specifically Candida-driven vulvovaginal infection — a use already well recognized in clinical practice, supported by **20 publications** and **no dedicated clinical trials** identified in this search.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Candidiasis (fungal infections of skin, mucosa, GI tract) — general pharmacological knowledge; no Singapore-specific approved indication text available (drug not currently registered) |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data was not available for this evidence pack. Based on well-established pharmacology, Nystatin is a polyene antifungal that binds ergosterol in the fungal cell membrane, forming pores that cause leakage of cellular contents and fungal cell death. This mechanism has made it a mainstay topical/oral antifungal against *Candida* species for decades.

Vulvovaginitis, when caused by *Candida albicans* (vulvovaginal candidiasis), is mechanistically the same target organism and pathology that Nystatin already treats elsewhere in the body — it is in fact a long-standing, traditional treatment option for this exact indication (vaginal Nystatin tablets/suppositories have historical clinical use, though they have since been largely surpassed by azole antifungals as first-line therapy). This is therefore less a "novel" repurposing signal and more a case of TxGNN correctly recognizing an already-known mechanistic and clinical relationship.

The supporting literature consistently frames Nystatin as an established, if now second-line, agent for vulvovaginal candidiasis — including in fluconazole-resistant cases, where it is cited as one of the few remaining effective alternatives.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Reviews management of fluconazole-resistant vulvovaginal candidiasis; identifies Nystatin (alongside boric acid, oteseconazole, ibrexafungerp) as an alternative therapy. |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | Reviews boric acid for recurrent VVC; notes non-albicans *Candida* resistance to azoles as context for alternative agents like Nystatin. |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | 287 *Candida* isolates from 283 patients with complicated VVC; correlated in vitro fluconazole/Nystatin susceptibility with clinical treatment outcome. |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Cohort | Ceska gynekologie | Evaluated combined vaginal Nystatin + nifuratel therapy for mixed/miscellaneous vulvovaginal infections. |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | In-vivo (rat model) | BMC Microbiology | Nystatin enhanced mucosal immune response and protected vaginal epithelial ultrastructure in a rat model of VVC. |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | Overview of vulvovaginal candidiasis as the second most common cause of vaginitis; *C. albicans* accounts for 85–90% of cases. |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | General clinical review of vulvovaginal candidiasis diagnosis and treatment. |
| [4919155](https://pubmed.ncbi.nlm.nih.gov/4919155/) | 1970 | Review | Med Clin North America | Early historical review of Nystatin's antifungal use. |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | In-vitro | Infection and Drug Resistance | Nystatin (and ZnO nanoparticles) showed antifungal activity and downregulated virulence gene expression in fluconazole-resistant *C. albicans* from VVC cases. |
| [37023426](https://pubmed.ncbi.nlm.nih.gov/37023426/) | 2023 | Comparative in-vitro | J Infect Dev Ctries | Compared tea tree oil (5%, 10%) and Nystatin inhibition zones against vaginal *Candida* isolates in pregnancy. |

---

## Singapore Market Information

Nystatin has no current registration record in Singapore (market status: Not Marketed, 0 licenses on file). No product/authorization details are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted use aligns with a well-established mechanism and decades of clinical precedent for Nystatin in *Candida*-driven vulvovaginitis, but evidence here is limited to observational/review-level literature with no supporting clinical trials, and the drug is currently unregistered in Singapore.

**To proceed, the following is needed:**
- Package insert / label safety data (key warnings, contraindications) — currently a blocking data gap for safety pre-assessment
- Formal mechanism-of-action documentation from DrugBank or equivalent source
- Confirmation of Singapore registration pathway, since the drug is not currently marketed locally
- Drug-drug interaction data (current query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

