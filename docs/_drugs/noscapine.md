---
layout: default
title: Noscapine
parent: 僅模型預測 (L5)
nav_order: 718
evidence_level: L5
indication_count: 10
---

# Noscapine
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

# Noscapine: Original Indication Not on Record → Scalp Dermatosis (Low-Confidence Signal)

## One-Sentence Summary

Noscapine's originally approved indication is not captured in this evidence pack — DrugBank matched the compound, but no indication text or mechanism of action was returned (both flagged as data gaps). TxGNN's top-ranked prediction is **Scalp Dermatosis** (score 98.5%), but the model's own generated rationale describes this specific link as likely knowledge-graph embedding noise, and **zero clinical trials or publications** currently support it. Across all 10 predicted indications in this batch, only one (Eye Disease, rank 8) reaches even a weak literature-supported tier (L4); the rest remain unsupported model output (L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (DrugBank record found, but no indication text on file) |
| Predicted New Indication | Scalp Dermatosis |
| TxGNN Prediction Score | 98.52% (rank 14,046 of full candidate pool) |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Market Status | ✗ Not Marketed (0 registrations) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for noscapine in this evidence pack. Historical pharmacology literature in the pack (e.g., PMID 13864787, a 1962 double-blind antitussive comparison) suggests noscapine has long been used as a cough suppressant, but this is inferred from a single tangential citation, not from a confirmed `original_moa` or `original_indications` record — it should not be treated as verified regulatory history.

For the top-ranked prediction itself, the evidence pack's own generated rationale is explicit that the link is not mechanistically grounded: *"No identifiable pharmacological mechanistic link; this disease name is likely TxGNN knowledge-graph embedding noise, recommended as an exclusion candidate."* No clinical trials, ICTRP registrations, or PubMed literature were found connecting noscapine to scalp dermatosis in any of the four source queries run against it (ClinicalTrials.gov, ICTRP, PubMed, DDI). This prediction should be read as a raw model score with no corroborating evidence, not as a validated repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Ranked Candidates (Not Analyzed in Detail)

This evidence pack scored 10 candidate indications for noscapine; all but one carry the same "no evidence found" profile as the top-ranked candidate above. Presented here for transparency:

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Note |
|------|---------|-------------|-----------------|----------|------|
| 1 | Scalp Dermatosis | 98.52% | L5 | Hold | Rationale flags as likely embedding noise |
| 2 | RAAS-blocker-induced Angioedema | 98.44% | L5 | Hold | Mechanism (bradykinin) unrelated to noscapine's known pharmacology |
| 3 | Rheumatoid Arthritis | 97.13% | L5 | Hold | Weak theoretical link via tubulin/anti-angiogenic activity; no direct evidence |
| 4 | Atopic Eczema | 96.20% | L5 | Hold | No pharmacologic rationale beyond historical antihistamine co-formulation |
| 5 | Colobomatous Microphthalmia–Rhizomelic Dysplasia Syndrome | 95.57% | L5 | Hold | Congenital syndrome, not a drug-treatable target; likely noise |
| 6 | Nephrotic Syndrome | 95.41% | L5 | Hold | No known mechanistic overlap |
| 7 | Brachydactyly-Syndactyly Syndrome | 95.37% | L5 | Hold | Congenital skeletal syndrome, not a drug-treatable target; likely noise |
| 8 | Eye Disease | 95.19% | **L4** | **Research Question** | See literature below (sigma-receptor hypothesis) |
| 9 | Autoimmune Hemolytic Anemia | 95.05% | L5 | Hold | No immunomodulatory mechanism known for noscapine |
| 10 | Recurrent Idiopathic Neuroretinitis | 95.04% | L5 | Hold | Same sigma-receptor theme as rank 8, but no literature of its own |

**Rank 8 (Eye Disease) supporting literature** — the only candidate in this batch with any literature hits:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10562963](https://pubmed.ncbi.nlm.nih.gov/10562963/) | 1999 | Review/Pharmacology | Nihon Yakurigaku Zasshi | Discusses sigma-receptor ligands (not noscapine-specific) in regulation of cough, GI, and retinal function; noscapine is a known sigma-receptor ligand, but the paper does not test noscapine directly against eye disease |
| [13864787](https://pubmed.ncbi.nlm.nih.gov/13864787/) | 1962 | Animal/clinical antitussive comparison | Praxis | Double-blind comparison of noscapine hydrochloride vs. dihydrocodeine as antitussives; no abstract on file, unrelated to eye disease |
| [13340902](https://pubmed.ncbi.nlm.nih.gov/13340902/) | 1956 | Methodology (paper chromatography) | Archiv der Pharmazie | Separation method for narcotine/papaverine; no abstract on file, not disease-relevant |

None of these three papers directly studies noscapine in an ophthalmic disease context — the link is a mechanistic extrapolation (sigma-receptor involvement in retinal function) rather than direct evidence, which is why this candidate is scored "Research Question" rather than a stronger tier.

## Singapore Market Information

Noscapine currently has no market authorizations on file (0 licenses, status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data are currently on file for noscapine; a DDI database query returned no results, and TFDA/HSA label data has not yet been retrieved (flagged as a **Blocking** data gap — DG001).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Scalp Dermatosis) has no supporting clinical trial or literature evidence and is explicitly flagged by the evidence pack's own rationale as likely model noise. No candidate in this 10-item batch clears even a single completed trial or systematic review; the best case (Eye Disease) rests on three decades-old, indirectly relevant papers. Combined with the absence of MOA data, absence of market presence, and a blocking gap on regulatory safety labeling, there is no basis to advance any of these candidates past screening.

**To proceed, the following is needed:**
- Retrieve noscapine's mechanism of action from DrugBank API (data gap DG002)
- Retrieve TFDA/HSA package insert warnings and contraindications (blocking gap DG001)
- Re-run TxGNN ranking with noise filtering, since 8 of 10 top candidates in this batch (including congenital syndromes with no drug-treatable target) appear to be embedding artifacts
- If pursuing the Eye Disease/sigma-receptor hypothesis further, commission a targeted literature search specifically on noscapine (not general sigma-receptor ligands) and retinal/ophthalmic outcomes before any trial design work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

