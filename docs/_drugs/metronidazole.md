---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 662
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic/Protozoal Infections to Pneumocystosis

## One-Sentence Summary

> Metronidazole is a long-established antiprotozoal/antibacterial agent (per the supporting literature, used for amoebic infections, trichomoniasis, and anaerobic bacterial disease). The TxGNN model's top-ranked prediction is efficacy against **Pneumocystosis** (Pneumocystis pneumonia), but of the **23 clinical trials** and **9 publications** retrieved, none actually test metronidazole against this indication — the evidence pack's own relevance review flags this as a likely keyword/co-occurrence artifact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore registry data provided (no licenses on file); literature citations describe classic use for anaerobic bacterial and protozoal infections (e.g., amoebic colitis, trichomoniasis) |
| Predicted New Indication | Pneumocystosis (Pneumocystis pneumonia) |
| TxGNN Prediction Score | 99.99% (rank #345 of all candidates) |
| Evidence Level | L4 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for metronidazole is not available in this evidence pack (`original_moa: [Data Gap]`). Based on the supporting literature that *was* retrieved, metronidazole's established pharmacology is as a nitroimidazole active against **anaerobic bacteria and select protozoa** (e.g., *Entamoeba histolytica*, *Trichomonas vaginalis*, *Giardia*) — it works by disrupting DNA in organisms with low-redox-potential metabolism.

This mechanism does not extend to *Pneumocystis jirovecii*, the causative organism of pneumocystosis, which is a **fungus**, not an anaerobic bacterium or protozoan. The evidence pack's own repurposing rationale is explicit on this point: *"機轉不合理...metronidazole 無抗 Pneumocystis 活性，標準治療為 TMP-SMX"* (mechanistically unreasonable; metronidazole has no anti-*Pneumocystis* activity; standard treatment is TMP-SMX).

Consistent with this, the retrieved literature consists of general reviews of AIDS-related opportunistic infections and case reports where a patient happened to receive metronidazole for an *unrelated* condition (e.g., amoebic dysentery, diarrhea) and **separately** developed PCP as a co-infection — not studies demonstrating metronidazole treats pneumocystosis. This pattern is characteristic of a knowledge-graph/literature co-occurrence artifact rather than a pharmacologically grounded signal, which is why the evidence pack itself scores this pairing L4 with a **Hold** recommendation despite the very high TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02972203](https://clinicaltrials.gov/study/NCT02972203) | N/A | Completed | 87 | Mindfulness-based intervention pilot in primary care — **not related to metronidazole or pneumocystosis** (relevance grade C: keyword mismatch) |
| [NCT05892666](https://clinicaltrials.gov/study/NCT05892666) | N/A | Recruiting | 4000 | Value-based comparison of walk-in clinic vs. ED care models — **not a drug treatment trial** (grade C) |
| [NCT03826758](https://clinicaltrials.gov/study/NCT03826758) | N/A | Unknown | 8000 | Clinical decision-support trial for chronic kidney disease detection — **unrelated to this indication** (grade C) |
| [NCT04418232](https://clinicaltrials.gov/study/NCT04418232) | Phase 1 | Completed | 243 | Dementia service-access program for Latino patients in primary care — **unrelated**, despite the "Phase 1" label (grade C) |
| [NCT06594133](https://clinicaltrials.gov/study/NCT06594133) | N/A | Completed | 68 | Retrospective study of lung microbiota in transplant recipients with *Nocardia* infection — an observational microbiome study, **not a metronidazole treatment trial** (grade C, from the related nocardiosis prediction) |
| [NCT02571673](https://clinicaltrials.gov/study/NCT02571673) | N/A | Completed | 65 | Head & neck cancer survivorship tool feasibility study — pending relevance review, but unrelated on its face |
| [NCT01909076](https://clinicaltrials.gov/study/NCT01909076) | N/A | Completed | 53 | Opioid risk-reduction strategies in primary care — pending relevance review, unrelated on its face |
| [NCT05256303](https://clinicaltrials.gov/study/NCT05256303) | N/A | Completed | 160 | Hospital-level care at home for acutely ill rural adults — pending relevance review, unrelated on its face |

**Note:** Of the 23 clinical trials retrieved for the metronidazole–pneumocystosis pairing, every trial reviewed to date has been graded **"C" (irrelevant/keyword mismatch)** or remains "pending" review; **none** are interventional trials of metronidazole for pneumocystosis. No trial in this set should be read as supporting evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Confirms metronidazole's established role for amebic colitis, extraintestinal amebiasis, and trichomoniasis — TMP-SMX (not metronidazole) is listed as the drug of choice for Pneumocystis pneumonia |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clinical Pharmacokinetics | General review of antiprotozoal pharmacokinetics; does not address metronidazole for pneumocystosis |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | General overview of HIV-related opportunistic infections; mentions PCP as a disease category, not a metronidazole indication |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Reviews AIDS infectious complications, listing PCP as most common; no metronidazole-PCP treatment link |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | American Review of Respiratory Disease | Patient treated with metronidazole for an unrelated diarrheal illness subsequently developed Pneumocystis carinii pneumonia — a co-occurrence, not evidence of treatment efficacy |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | AIDS patient treated with metronidazole for amebic dysentery/liver abscess, who separately developed PCP — again a co-occurrence, not a treatment finding |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formosan Medical Association | Case of amoebic colitis and CMV colitis in an HIV patient; unrelated to pneumocystosis |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Reviews of Infectious Diseases | General critique of antimicrobial prophylaxis trials; not specific to metronidazole or pneumocystosis |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | General review of antiprotozoal drugs (abstract not available) |

**Note:** All nine publications are reviews or case reports discussing metronidazole and pneumocystosis only as **co-occurring, unrelated clinical facts** (e.g., a patient on metronidazole for a separate infection who also had PCP). No publication reports metronidazole being used to treat, or tested against, pneumocystosis.

---

## Singapore Market Information

Metronidazole has **no registered products on file** in the Singapore regulatory data provided (`total_licenses: 0`, `market_status: 未上市`). No authorization numbers, product names, or approved-indication text are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug–drug interaction data were retrievable in this evidence pack — DDI query returned `not_found`, and TFDA/HSA label data is flagged as a **Blocking** data gap [DG001] pending retrieval from the regulatory source.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanism of *Pneumocystis jirovecii* infection (a fungal pathogen) falls entirely outside metronidazole's known antibacterial/antiprotozoal spectrum, and the evidence pack's own mechanistic review independently reaches the same conclusion.
- None of the 23 clinical trials or 9 publications retrieved provide direct evidence of metronidazole treating pneumocystosis — the literature hits are co-occurrence artifacts (patients who received metronidazole for an unrelated condition and separately had PCP), and the trials are unrelated primary-care/health-services studies caught by keyword matching.
- The drug also has zero registered licenses in Singapore, adding a regulatory barrier on top of the scientific one.

**To proceed, the following is needed:**
- Resolve data gap DG002 (metronidazole MOA from DrugBank) to formally document the mechanistic mismatch in the safety/efficacy file.
- Resolve data gap DG001 (TFDA/HSA package insert — warnings and contraindications), which is currently a **Blocking** gap for any Stage 1 safety review, regardless of which indication is pursued.
- If pursuing a metronidazole repurposing program at all, consider redirecting to the other candidates in this same evidence batch that already carry more direct, mechanistically coherent support and a **"Research Question"** decision stage rather than Hold: **ulcerative proctosigmoiditis** (rank 3, anaerobic-overgrowth rationale in IBD), **cap polyposis** (rank 9, direct case-level literature on metronidazole efficacy), and **ulceration of vulva** (rank 10, direct evidence for cutaneous/vulvar amoebiasis and off-label Crohn's-related use).

---
*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

