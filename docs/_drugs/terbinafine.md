---
layout: default
title: Terbinafine
parent: 僅模型預測 (L5)
nav_order: 956
evidence_level: L5
indication_count: 10
---

# Terbinafine
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

# Terbinafine: From Dermatophyte Infections to Creeping Myiasis (Multi-Candidate Evidence Review)

## One-Sentence Summary

> Terbinafine is not currently registered or marketed in Singapore, so no local approved-indication data exists in this dataset; it is widely known as an oral/topical allylamine antifungal for dermatophyte infections.
> TxGNN's **top-ranked** prediction is **Creeping Myiasis** (score **96.74%**), but this candidate has **zero clinical trials and zero literature** support, and the model's own rationale flags it as mechanistically unrelated to terbinafine's antifungal action.
> Across all **10 predicted indications** in this pack, only **2 candidates** (Superficial Mycosis, Tinea Manuum) have RCT-level evidence — and both represent known antifungal-spectrum extensions rather than genuine repurposing; the rest range from early-stage (Cutaneous Candidiasis, Blastomycosis) to unsupported (myiasis variants, Toxoplasmosis, Echinococcosis).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this dataset (drug not registered in Singapore; no license records). Generally known as an antifungal (dermatophyte infections) |
| Predicted New Indication (TxGNN Rank 1) | Creeping Myiasis |
| TxGNN Prediction Score | 96.74% |
| Evidence Level | L5 (no supporting clinical trials or literature) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

⚠️ Note: TxGNN's top score does not translate into supporting evidence for this candidate. See "All Candidate Indications" below for the full 10-candidate picture, including two better-supported alternatives.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for terbinafine is not available in this dataset ([Data Gap] — DG002). Based on information embedded in the evidence pack's rationale fields, terbinafine is described as an allylamine antifungal that inhibits **squalene epoxidase**, blocking ergosterol synthesis in fungal cell membranes — a mechanism specific to fungal biology.

For the top-ranked candidate, **Creeping Myiasis**, the mechanistic link is explicitly assessed as weak: myiasis is caused by fly larvae infestation (an entomological/parasitic condition), which has no relationship to fungal ergosterol synthesis. No clinical trials or literature were found supporting this candidate — the high TxGNN score appears to be a pure model-similarity signal (likely driven by shared "skin infection" category proximity) rather than a biologically grounded prediction.

By contrast, several lower-ranked candidates in this pack are mechanistically coherent because they target other fungal pathogens that also depend on ergosterol synthesis (e.g., Candida, Blastomyces/Paracoccidioides). These are discussed below.

---

## All Candidate Indications (Full Ranking)

Given this is a multi-candidate evidence pack, all 10 TxGNN-predicted indications are summarized here for context:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Evidence |
|------|---------|-------------|-----------------|-----------------|--------------|
| 1 | Creeping myiasis | 96.74% | L5 | Hold | No evidence; mechanistically unrelated |
| 2 | Furuncular myiasis | 96.74% | L5 | Hold | 1 case report (differential diagnosis only, not treatment) |
| 3 | Wound myiasis | 96.74% | L5 | Hold | 2 case reports; no treatment evidence |
| 4 | Myiasis | 96.21% | L5 | Hold | 3 case reports (chromoblastomycosis/furuncle comorbid with myiasis); no treatment evidence |
| 5 | Cutaneous candidiasis | 95.04% | L3 | Research Question | 20 literature items; in vitro fungistatic activity against Candida established, but weaker/less reliable than azoles |
| 6 | Toxoplasmosis | 94.79% | L5 | Hold | No mechanistic plausibility (protozoan, no ergosterol pathway); literature unrelated |
| 7 | Blastomycosis | 91.76% | L4 | Research Question | Case report: paracoccidioidomycosis (South American blastomycosis) successfully treated with terbinafine |
| 8 | Tinea manuum | 90.11% | L3 | Proceed with Guardrails | Known dermatophyte spectrum; small RCT-level clinical study (1991) |
| 9 | Echinococcus granulosus infection | 86.06% | L5 | Hold | No evidence; no mechanistic plausibility (cestode) |
| 10 | Superficial mycosis | 84.47% | L2 | Proceed with Guardrails | Completed Phase 1 RCT (NCT05578950, n=100) vs. itraconazole; extensive supporting literature |

**Key observation:** the two best-evidenced candidates (Tinea Manuum, Superficial Mycosis) are explicitly noted in the rationale as *known* antifungal-spectrum extensions rather than true novel repurposing — terbinafine is already the class-standard treatment for dermatophyte infections. The candidates that would represent genuinely *new* indications (Cutaneous Candidiasis, Blastomycosis) sit at lower evidence tiers (L3–L4, case reports/in vitro only).

---

## Clinical Trial Evidence (Top Candidate: Creeping Myiasis)

Currently no related clinical trials registered.

**Supplementary — best trial evidence found across all candidates:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05578950](https://clinicaltrials.gov/study/NCT05578950) | Phase 1 | Completed | 100 | Comparative RCT: continuous oral terbinafine vs. pulse itraconazole for onychomycosis/superficial mycosis |

---

## Literature Evidence (Top Candidate: Creeping Myiasis)

Currently no related literature available.

**Supplementary — most relevant literature across better-evidenced candidates:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10886159](https://pubmed.ncbi.nlm.nih.gov/10886159/) | 2000 | Case report | British Journal of Dermatology | First reported successful treatment of paracoccidioidomycosis (South American blastomycosis) with terbinafine 250mg BID x6 months |
| [9593126](https://pubmed.ncbi.nlm.nih.gov/9593126/) | 1998 | In vitro susceptibility study | Antimicrobial Agents and Chemotherapy | Terbinafine active in vitro against 350 clinical Candida albicans/yeast isolates; clinically active in cutaneous candidiasis |
| [1911319](https://pubmed.ncbi.nlm.nih.gov/1911319/) | 1991 | Clinical study | British Journal of Dermatology | 2-week oral terbinafine effective for moccasin tinea pedis and tinea manuum (28 evaluable patients) |
| [19942790](https://pubmed.ncbi.nlm.nih.gov/19942790/) | 2009 | Guideline | Jpn J Med Mycology | Diagnosis/treatment guideline for mucocutaneous candidiasis |
| [38623728](https://pubmed.ncbi.nlm.nih.gov/38623728/) | 2024 | Review | Expert Opinion on Pharmacotherapy | Rising antifungal resistance in dermatophytosis, including terbinafine-resistant strains |
| [25016125](https://pubmed.ncbi.nlm.nih.gov/25016125/) | 2014 | Case report | Turkiye Parazitolojii Dergisi | Furuncular cutaneous myiasis case — terbinafine used empirically among multiple failed therapies, no efficacy shown (differential diagnosis case, not evidence of efficacy) |

---

## Singapore Market Information

Currently no registration records — Terbinafine is not marketed in Singapore under this dataset (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: This is a Blocking data gap — DG001: TFDA/HSA package insert warnings and contraindications could not be retrieved, which prevents this candidate from entering formal S1 safety screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN top-ranked prediction (Creeping Myiasis, 96.74%) has no clinical trial or literature support and is mechanistically implausible against terbinafine's antifungal MOA. Among the 9 alternative candidates, the only ones with solid evidence (Tinea Manuum, Superficial Mycosis) are not genuine repurposing — they fall within terbinafine's already-known antifungal spectrum — while the more novel candidates (Cutaneous Candidiasis, Blastomycosis) remain at case-report/in-vitro level (L3–L4). Combined with a Blocking safety data gap (no TFDA/HSA label data available) and zero Singapore market presence, this candidate is not ready to advance.

**To proceed, the following is needed:**
- Retrieve terbinafine's official MOA documentation from DrugBank (DG002)
- Retrieve TFDA/HSA package insert warnings and contraindications (DG001, Blocking — required before any S1 safety screening)
- If pursuing a genuine new-indication angle, prioritize further validation of **Blastomycosis/deep mycoses** or **Cutaneous Candidiasis** rather than the top TxGNN-ranked myiasis/parasitic candidates
- Re-evaluate market entry rationale given terbinafine has zero current registration in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

