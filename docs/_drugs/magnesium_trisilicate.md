---
layout: default
title: Magnesium Trisilicate
parent: 僅模型預測 (L5)
nav_order: 626
evidence_level: L5
indication_count: 10
---

# Magnesium Trisilicate
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

# Magnesium Trisilicate: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Magnesium trisilicate is a magnesium-based antacid; its specific original indication is not documented in this evidence pack, but it is generically known as an agent for symptomatic relief of gastric hyperacidity. The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, with **0 clinical trials** and **4 publications** currently associated with this direction — however, none of the four papers are direct controlled studies of magnesium trisilicate in this specific indication, so the supporting evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Singapore registration data (drug is generically classified as an antacid for hyperacidity/dyspepsia) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, magnesium trisilicate belongs to the antacid drug class, whose efficacy in relieving symptoms of gastric hyperacidity has been established through long-standing clinical use, and this mechanism may plausibly extend to active peptic ulcer disease.

Antacids act by chemically neutralizing gastric acid and raising intragastric pH. In theory, this can relieve symptoms associated with active peptic ulcer disease and may support mucosal healing by reducing the acid burden on the ulcerated surface — this is the mechanistic rationale underlying the TxGNN prediction.

However, the mechanistic plausibility is not yet matched by direct evidence. All four literature citations retrieved for this indication involve related but distinct agents or contexts — sucralfate/alginate compounds, a carbenoxolone-based drug (Duogastrone) tested against a placebo that happened to contain magnesium trisilicate, a general GERD treatment review, and an unrelated pharmacokinetic study — rather than controlled trials of magnesium trisilicate itself in active peptic ulcer disease. The prediction should therefore be read as mechanistically reasonable but currently unproven for this specific drug-indication pair.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2986275](https://pubmed.ncbi.nlm.nih.gov/2986275/) | 1985 | RCT (indirect — sucralfate vs. alginate/antacid, not magnesium trisilicate) | Scandinavian Journal of Gastroenterology | Randomized double-blind trial in reflux esophagitis comparing sucralfate vs. an alginate/antacid compound; ~70% of patients in both arms became symptom-free or improved, with 53% complete healing on sucralfate. |
| [4909818](https://pubmed.ncbi.nlm.nih.gov/4909818/) | 1970 | Clinical trial (indirect — Duogastrone/carbenoxolone; magnesium trisilicate used only as placebo control) | Gut | Double-blind trial in 14 active duodenal ulcer patients showed Duogastrone controlled symptoms and hastened healing versus a placebo containing magnesium trisilicate as the control substance. |
| [2877526](https://pubmed.ncbi.nlm.nih.gov/2877526/) | 1986 | Review | Zeitschrift für Gastroenterologie | General review of GERD medical therapy staging, noting antacid/alginate combinations as first-line (Phase I) options alongside acid suppressants and mucosal-protective agents. |
| [432256](https://pubmed.ncbi.nlm.nih.gov/432256/) | 1979 | PK study (unrelated — likely keyword mismatch) | Die Pharmazie | Investigated how antacid/adsorbent drugs used for peptic ulcer reduced dissolution of norethisterone acetate from oral contraceptive tablets; not related to ulcer treatment efficacy. |

---

## Singapore Market Information

Magnesium trisilicate is currently **not registered or marketed** in Singapore under this evidence pack (0 licenses on file). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (acid neutralization supporting ulcer symptom relief) is sound, but evidence is currently at the preclinical/mechanistic level (L4) — there are no registered clinical trials of magnesium trisilicate for active peptic ulcer disease, and the four available publications are indirect (testing other drugs, or unrelated to the indication). The drug also has no current Singapore market presence, adding a regulatory data gap on top of the efficacy gap.

**To proceed, the following is needed:**
- Direct clinical or trial evidence testing magnesium trisilicate itself (not comparator/placebo-control drugs) specifically in active peptic ulcer disease
- Mechanism of action (MOA) data, currently a documented gap — recommended source: DrugBank API query
- Official package insert / label data (warnings, contraindications), currently a documented **blocking** gap for safety assessment — recommended source: regulatory agency's official package insert download and parsing
- Consider also evaluating **gastrojejunal ulcer** (rank 3 in this evidence pack), which carries stronger direct evidence — a 1965 double-blind RCT (PMID 14248445) and multiple cohort studies testing magnesium trisilicate directly — and is already scored at evidence level L2 with a "Proceed with Guardrails" recommendation, making it a potentially more actionable repurposing target than the top-ranked TxGNN score alone would suggest
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

