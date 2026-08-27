---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
---

# Metformin
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

# Metformin: From Type 2 Diabetes Mellitus to Ten TxGNN-Predicted Rare Disease Signals

## One-Sentence Summary

> Metformin (DrugBank DB00331) is a biguanide-class drug whose established use — confirmed throughout the literature returned in this evidence pack — is Type 2 Diabetes Mellitus.
> This evidence pack does **not** contain one strong new-indication signal; it contains **10 low-to-moderate confidence TxGNN candidates**, most of which the pack's own mechanistic analysis flags as probable embedding-similarity false positives.
> Only **1 of 10** candidates (Homozygous Familial Hypercholesterolemia) reaches a "Research Question" tier with any literature support (2 publications, no trials); the rest remain at model-prediction-only (L5) with **zero supporting trials or literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus *(not present in `taiwan_regulatory.licenses` — drug is unregistered in Singapore; inferred from the drug-disease context of the literature returned across this pack, e.g. PMID 15955371, 9506190, 10905481)* |
| Top-Ranked Predicted Indication (rank 1) | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score (rank 1) | 99.45% |
| Evidence Level (rank 1) | L5 (model prediction only, no trials/literature) |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** (all 10 candidates) |

⚠️ **Important caveat**: The table above reflects the #1-ranked candidate per the template's default rule, but this candidate is explicitly flagged in the evidence pack's own rationale as a likely **embedding-similarity false positive** (identical score to rank 2, no supporting evidence). It should **not** be read as the headline finding. The full 10-candidate ranking is below.

### Full Predicted Indications Ranking

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Focal Stiff Limb Syndrome | 99.45% | L5 | S0 | Hold |
| 2 | Classic Stiff Person Syndrome | 99.45% | L5 | S0 | Hold |
| 3 | Opsismodysplasia | 99.40% | L5 | S0 | Hold |
| 4 | Thiamine-Responsive Dysfunction Syndrome | 99.40% | L5 | S0 | Hold ⚠️ (safety flag, not opportunity — see below) |
| 5 | Drug-Induced Localized Lipodystrophy | 99.06% | L5 | S0 | Hold |
| 6 | Centrifugal Lipodystrophy | 98.99% | L5 | S0 | Hold |
| 7 | Pressure-Induced Localized Lipoatrophy | 98.96% | L5 | S0 | Hold |
| 8 | Pancreatic Agenesis | 98.91% | L4 | S1 | Hold |
| 9 | Idiopathic Localized Lipodystrophy | 98.90% | L5 | S0 | Hold |
| 10 | Homozygous Familial Hypercholesterolemia | 92.30% | L4 | S1 | **Research Question** |

---

## Why is This Prediction Reasonable?

**Mechanism of action.** `drug.original_moa` is marked as a data gap (DG002), but the mechanistic content embedded in this pack's own rationale fields is consistent and can be cited directly: Metformin is a **biguanide**. Its established mechanism is AMPK activation, suppression of hepatic gluconeogenesis, and improved peripheral insulin sensitivity — an insulin-*sensitizing* action, not an insulin-*secretagogue* action. This MOA is repeated verbatim across multiple candidate rationales in the pack (ranks 2, 4, 5, 8, 10).

**Why most of the 10 candidates do not hold up mechanistically.** Ranks 1–7 and 9 span three unrelated disease families — stiff-person-spectrum autoimmune neurological disease, a skeletal dysplasia (opsismodysplasia), a thiamine-transporter disorder, and four lipodystrophy variants. None of these pathologies involve the AMPK/insulin-sensitivity axis that defines Metformin's known pharmacology, and none returned any clinical trial or literature hits across ClinicalTrials.gov, ICTRP, or PubMed (see `query_log`). Ranks 1 and 2 share an identical TxGNN score and adjacent knowledge-graph ranks, which the pack's own analysis interprets as a single embedding artifact rather than two independent signals.

**The one candidate with a genuine (if weak) mechanistic thread.** Homozygous Familial Hypercholesterolemia (rank 10) is the only signal supported by literature that plausibly connects to Metformin: a 1988 in-vitro study (PMID 3377878) found Metformin reduced cholesterol synthesis in cultured human fibroblasts, suggesting an AMPK-mediated, LDL-receptor-independent effect on cholesterol metabolism. Since HoFH's core defect is LDLR loss-of-function, an LDLR-independent adjunct mechanism is at least conceptually compatible — but the evidence is one 38-year-old in-vitro study, not a disease-specific trial, so this remains a research hypothesis, not a clinical signal.

---

## Clinical Trial Evidence

No clinical trials were found for **any** of the 10 predicted indications in ClinicalTrials.gov or ICTRP (`query_log` entries 3–4, 6–7, 9–10, 12–13, 15–16, 18–19, 21–22, 24–25, 27–28, 30–31 all returned `result_count: 0`).

> Currently no related clinical trials registered for any of the 10 candidate indications.

---

## Literature Evidence

Literature was found for only 2 of the 10 candidates. All others returned zero PubMed hits.

### Pancreatic Agenesis (rank 8) — 20 hits found, but the pack's own analysis flags them as keyword co-occurrence noise ("pancreas + diabetes + metformin"), not disease-specific evidence. Most directly relevant items shown below:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40819996](https://pubmed.ncbi.nlm.nih.gov/40819996/) | 2025 | Review | Pancreatology | Names pancreatic agenesis as one cause of Type 3c diabetes (T3cDM), but the review is about T3cDM broadly, not Metformin therapy in agenesis specifically |
| [35898377](https://pubmed.ncbi.nlm.nih.gov/35898377/) | 2022 | Review | Cureus | T2DM–pancreatic cancer association; not agenesis-specific |
| [20376506](https://pubmed.ncbi.nlm.nih.gov/20376506/) | 2010 | Review | Acta Diabetologica | Epidemiology of diabetes-associated neoplasms; general T2DM context |
| [18038714](https://pubmed.ncbi.nlm.nih.gov/18038714/) | 2007 | Case Report | J Pediatr Endocrinol Metab | Metformin + rosiglitazone in a boy with Alström syndrome (a different genetic obesity/insulin-resistance syndrome, not pancreatic agenesis) |
| [14561576](https://pubmed.ncbi.nlm.nih.gov/14561576/) | 2003 | Case Report | Endocr Pract | Metformin-induced cholestatic hepatitis — an adverse-event report, unrelated to the indication |
| [18259965](https://pubmed.ncbi.nlm.nih.gov/18259965/) | 2008 | Case Report | Clin Toxicol | Metformin-induced lactic acidosis and acute pancreatitis in a polypharmacy patient — safety signal, not efficacy evidence |

*(14 additional hits — general T2DM pathophysiology reviews, animal studies, and unrelated antidiabetic drug reviews — omitted as non-specific to pancreatic agenesis; full list available in the evidence pack.)*

### Homozygous Familial Hypercholesterolemia (rank 10) — 2 hits found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37160786](https://pubmed.ncbi.nlm.nih.gov/37160786/) | 2023 | Review | Acta Diabetologica | Discusses adjuvant off-label GLP-1 analog (not Metformin) use in monogenic obesity/diabetes; contextual only |
| [3377878](https://pubmed.ncbi.nlm.nih.gov/3377878/) | 1988 | In-vitro Study | Atherosclerosis | Metformin decreased cholesterol, fatty acid, and triacylglycerol synthesis in cultured human fibroblasts (dose-dependent, 50% reduction at 5×10⁻⁴ M) — the only direct mechanistic link found |

---

## Singapore Market Information

No Singapore drug registrations are recorded in this evidence pack. `taiwan_regulatory.total_licenses = 0` and `market_status = 未上市 (Not Marketed)` — Metformin currently has no listed license entries to summarize in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information. *(All structured safety fields — key warnings, contraindications, and DDI query — returned as data gaps or "not found" in this pack; this is flagged as a Blocking data gap (DG001) in `meta.data_gaps`.)*

One mechanistic caution surfaced by the pack's own rationale deserves explicit note even though it is not sourced from the structured `safety` block: for **rank 4 (thiamine-responsive dysfunction syndrome)**, the rationale describes Metformin as a known competitive inhibitor of OCT1/OCT2 transporters, which mediate cellular and renal thiamine handling — meaning Metformin may *worsen* thiamine-deficiency states rather than treat them. This candidate should be tracked as a potential **safety interaction**, not a repurposing opportunity.

---

## Conclusion and Next Steps

**Decision: Hold** (all 10 candidates; rank 10 carries a secondary **Research Question** tag for exploratory tracking only)

**Rationale:**
- 8 of 10 candidates are at Evidence Level L5 (model prediction only, zero trials, zero literature), and two of those eight (ranks 1–2) are explicitly flagged by the pack's own analysis as a likely single embedding-similarity false positive.
- The 2 candidates that reach L4 (pancreatic agenesis, HoFH) are supported only by indirect or decades-old, non-disease-specific literature — not sufficient to justify clinical development.
- A Blocking data gap (DG001: Singapore/TFDA label warnings and contraindications) means this candidate cannot even complete the initial safety screening stage (S1) regardless of predicted-indication strength.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse the official product label (warnings/contraindications) — currently blocking
- Formalize DG002: structured MOA record from DrugBank API (the AMPK/gluconeogenesis/insulin-sensitivity mechanism is currently only available narratively within this pack's rationale text, not as a structured field)
- If pursuing rank 10 (HoFH) as a research question: seek contemporary, disease-specific data on Metformin's LDLR-independent cholesterol effect — the current evidence (PMID 3377878) is a single 1988 in-vitro study
- If pursuing rank 4 (thiamine-responsive dysfunction syndrome): treat as a pharmacovigilance/DDI investigation (Metformin–thiamine transporter competition), not a repurposing candidate
- Re-run DDI query (`safety.ddi.query_status = not_found`) — current DDI dataset returned no results, which is itself a gap requiring resolution before any Go decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

