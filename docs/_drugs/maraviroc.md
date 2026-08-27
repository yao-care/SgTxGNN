---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 630
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From CCR5 Antagonism (HIV-1 Infection) to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc's original mechanism of action is not formally recorded in this evidence pack (flagged as data gap **DG002**), but contextual references embedded in the mechanistic rationales throughout this pack consistently describe it as a **CCR5 antagonist / HIV-1 entry inhibitor**. This is a **multi-candidate TxGNN screen** covering 10 predicted indications for Maraviroc; the top-ranked candidate, **Multiple Endocrine Neoplasia**, has a TxGNN score of 99.82% but **zero supporting clinical trials or literature**, and the pack's own mechanistic analysis flags it as likely knowledge-graph co-occurrence noise. A more scientifically grounded secondary signal exists further down the ranking — **HER2-positive breast carcinoma** (rank 10), supported by a preclinical mechanistic study on CCL5/CCR5-mediated trastuzumab resistance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (CCR5 antagonist) — inferred from context within this evidence pack; formal record is a data gap (DG002) |
| Predicted New Indication | Multiple Endocrine Neoplasia (top-ranked of 10 candidates screened) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Maraviroc is not available as a verified DrugBank field in this evidence pack (data gap DG002). However, multiple candidate rationales in this same batch independently and consistently describe Maraviroc as a **CCR5 (C-C chemokine receptor type 5) antagonist**, used in the context of **HIV-1 antiretroviral therapy** — this appears in the reasoning for the candidiasis (rank 7) and cytomegalovirus infection (rank 9) entries, both of which discuss HIV/ART-related immune context. This gives reasonable internal confidence in the drug's pharmacological class even though the formal `original_moa` field itself is empty.

For the **top-ranked candidate, Multiple Endocrine Neoplasia (MEN)**, the evidence pack's own mechanistic assessment is explicit that **no known pathophysiological link exists**: MEN is a hereditary endocrine tumor syndrome driven by germline mutations in *RET* (MEN2) or *MEN1*, with no established connection to CCR5 or chemokine receptor signaling. The rationale text itself concludes the high TxGNN score is "very likely knowledge-graph co-occurrence noise, with no mechanistic basis" — meaning the highest-scoring prediction in this screen should not be read as a strong biological signal.

Looking across the full batch is more informative than the top rank alone. The most mechanistically credible candidate in this pack is **HER2-positive breast carcinoma (rank 10)**, supported by a preclinical study showing that autocrine **CCL5** — a primary CCR5 ligand — drives trastuzumab resistance via ERK pathway activation in HER2-positive breast cancer. This provides a direct, receptor-specific mechanistic rationale (not merely family-level or population-co-occurrence inference) for testing CCR5 blockade as a resistance-reversal strategy, though it remains an in-vitro/mechanistic finding with no human trial data yet.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for any of the 10 candidate indications screened in this pack. This was confirmed via both ClinicalTrials.gov and WHO ICTRP queries for every candidate disease (see `query_log`), all returning zero results.

---

## Literature Evidence

For the top-ranked candidate, **Multiple Endocrine Neoplasia**, currently no related literature is available.

Literature was found for five of the other nine candidates screened in this batch:

| Indication | PMID | Year | Type | Journal | Key Findings |
|------|------|-----|------|------|---------|
| HER2 positive breast carcinoma (rank 10) | [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/) | 2020 | Preclinical Mechanistic Study | Molecular Cancer Therapeutics | Autocrine CCL5 (a CCR5 ligand) activates ERK signaling and mediates trastuzumab resistance in HER2-positive breast cancer — the most direct CCR5-pathway-specific mechanistic evidence in this batch |
| Primary cutaneous T-cell lymphoma (rank 3) | [37006247](https://pubmed.ncbi.nlm.nih.gov/37006247/) | 2023 | Review | Frontiers in Immunology | Review of ACKR1 (not CCR5) targeting in cancer; only an indirect, same-receptor-family analogy — not direct evidence for Maraviroc or CCR5 |
| Primary cutaneous T-cell non-Hodgkin lymphoma (rank 5) | [37006247](https://pubmed.ncbi.nlm.nih.gov/37006247/) | 2023 | Review | Frontiers in Immunology | Same ACKR1 review as above; overlapping disease classification with rank 3 |
| Cytomegalovirus infection (rank 9) | [26960018](https://pubmed.ncbi.nlm.nih.gov/26960018/) | 2016 | Review | Viral Immunology | General review of HIV immune responses; no CMV- or Maraviroc-specific data |
| Cytomegalovirus infection (rank 9) | [25397464](https://pubmed.ncbi.nlm.nih.gov/25397464/) | 2014 | Cohort | Journal of the International AIDS Society | Innate immune/metabolic marker correlations in ART-treated HIV+ patients with undetectable viral load; population-overlap evidence only, not CMV-specific |
| Candidiasis (rank 7) | [21671545](https://pubmed.ncbi.nlm.nih.gov/21671545/) | 2011 | Review | American Family Physician | Reviews common adverse effects of HIV antiretroviral therapy, including opportunistic candidiasis in immunosuppressed patients — a "same population, not causal treatment" association (confounding by indication), not evidence that CCR5 blockade treats candidiasis |

No literature was found for Multiple Endocrine Neoplasia (rank 1), acne (rank 2), pediatric systemic lupus erythematosus (rank 4), primary cutaneous B-cell lymphoma (rank 6), or complement component 4a deficiency (rank 8, still unscored/pending in this pipeline pass).

---

## Safety Considerations

No package-insert-level warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack. This is flagged internally as a **Blocking** data gap (DG001) — safety pre-assessment (Stage S1) cannot proceed until HSA/TFDA label data or equivalent DrugBank warning data is obtained. Please refer to the official package insert for safety information in the interim.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-ranked candidate (Multiple Endocrine Neoplasia) has no supporting clinical trials or literature, and the evidence pack's own mechanistic review flags it as likely prediction noise rather than a real signal. Maraviroc is also not currently registered or marketed in Singapore (0 licenses), and safety/label data is a **Blocking** gap (DG001) that prevents even an initial safety screen — so no candidate from this batch can advance past S0/S1 today, regardless of mechanistic plausibility.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings, contraindications, and DDI data (DG001 — Blocking; required before any S1 safety pre-assessment)
- DrugBank-verified original mechanism of action and indication record for Maraviroc (DG002), to replace the context-inferred CCR5/HIV-1 attribution used in this report
- Preclinical/in-vivo validation of CCR5 blockade reversing CCL5-driven trastuzumab resistance in HER2-positive breast cancer (rank 10) — currently the most mechanistically credible candidate in this batch and worth tracking as a distinct research question separate from the top TxGNN rank
- CCR5-specific (rather than family-level ACKR1-proxy) literature searches for the cutaneous T-cell lymphoma candidates (ranks 3 and 5) to close the indirect-evidence gap
- A Singapore registration pathway assessment, since Maraviroc currently holds zero local licenses and any repurposing pathway would require a new registration rather than an indication extension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

