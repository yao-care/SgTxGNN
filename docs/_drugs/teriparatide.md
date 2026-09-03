---
layout: default
title: Teriparatide
parent: 僅模型預測 (L5)
nav_order: 959
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Pregnancy and Lactation-Associated Osteoporosis

## One-Sentence Summary

> Teriparatide is a recombinant human parathyroid hormone (PTH 1-34) approved for treating osteoporosis by stimulating new bone formation. Among the ten TxGNN-predicted indications reviewed, most top-ranked candidates (duodenal ulcer, esophageal malformation, duodenal obstruction, Worth syndrome, etc.) were screened out as knowledge-graph noise with no mechanistic or empirical support. The best-supported candidate is **Pregnancy and Lactation-Associated Osteoporosis (PLO)**, backed by **2 clinical trials** and **20 publications**, including several cohort studies that directly evaluate teriparatide in this population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (established use as an anabolic bone-forming agent; not derivable from Singapore market data since the drug is currently unregistered there) |
| Predicted New Indication | Pregnancy and Lactation-Associated Osteoporosis (PLO) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L3 (observational cohort studies + systematic review) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no structured MOA field is available for teriparatide (flagged as a High-severity data gap, DG002). However, the evidence pack's own repurposing rationale confirms teriparatide is a recombinant human parathyroid hormone fragment (PTH 1-34) that activates the PTH1 receptor to stimulate osteoblast activity and increase bone formation — the pharmacological basis for its established use in osteoporosis.

PLO is a rare, premenopausal form of osteoporosis driven by the substantial calcium and skeletal demands of late pregnancy and lactation, typically presenting as vertebral fragility fractures. Pathophysiologically it is a form of accelerated bone loss, placing it within the same disease category as the drug's original indication rather than requiring a cross-system mechanistic leap. Because teriparatide's anabolic action directly counters bone loss regardless of its trigger (menopause vs. pregnancy/lactation), the mechanistic rationale for use in PLO is strong and is reflected in real-world literature already treating PLO patients off-label with teriparatide.

By contrast, seven of the ten TxGNN-ranked candidates in this pack (duodenal ulcer, non-syndromic esophageal malformation, duodenal obstruction, duodenogastric reflux, Worth syndrome, autosomal dominant neovascular inflammatory vitreoretinopathy, succinyl-CoA:3-ketoacid CoA transferase deficiency) were explicitly assessed as having no biological plausibility and no supporting evidence — these are treated as embedding-based false positives and excluded from further consideration. A secondary hypothesis-generating candidate, amenorrhea (functional hypothalamic amenorrhea with bone loss), has only indirect literature support (L4, "Research Question" stage) and is not yet actionable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00277706](https://clinicaltrials.gov/study/NCT00277706) | Phase 1 | Completed | 40 | Evaluated PTH(1-34)/teriparatide's effect on oral bone regeneration after periodontal surgery; confirms direct osteo-anabolic effect but not in a PLO population (indirect mechanistic support). |
| [NCT02440581](https://clinicaltrials.gov/study/NCT02440581) | N/A | Completed | 141 | Studied renal osteodystrophy-related bone loss; provides background bone-metabolism data but weak relevance to PLO's pregnancy/lactation-driven pathophysiology. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34132853](https://pubmed.ncbi.nlm.nih.gov/34132853/) | 2021 | Cohort | Calcified Tissue International | Multicenter retrospective cohort (19 teriparatide vs. conventional care) showing teriparatide's effect on BMD and trabecular bone score in PLO patients. |
| [37708365](https://pubmed.ncbi.nlm.nih.gov/37708365/) | 2024 | Systematic Review/Meta-analysis | J Clin Endocrinol Metab | Comparative effectiveness of PLO therapeutic interventions, including teriparatide, across the current evidence base. |
| [35903718](https://pubmed.ncbi.nlm.nih.gov/35903718/) | 2022 | Cohort | Geburtshilfe und Frauenheilkunde | 47 PLO patients with vertebral fractures treated with teriparatide; assessed subsequent fracture risk and BMD outcomes. |
| [34037833](https://pubmed.ncbi.nlm.nih.gov/34037833/) | 2021 | Retrospective Cohort | Calcified Tissue International | Examined BMD trajectory after teriparatide discontinuation, with/without sequential antiresorptive therapy, in PLO. |
| [39008200](https://pubmed.ncbi.nlm.nih.gov/39008200/) | 2024 | Review | Endocrine | Reviews management strategies for PLO with specific focus on teriparatide use. |
| [40205203](https://pubmed.ncbi.nlm.nih.gov/40205203/) | 2025 | Systematic Review/Meta-analysis | Osteoporosis International | 35-study, 943-patient meta-analysis of PAO presentation, risk factors and treatment response (treatment data inconclusive due to limited data). |
| [33620518](https://pubmed.ncbi.nlm.nih.gov/33620518/) | 2022 | Review | Calcified Tissue International | Overview of PLO pathophysiology, presentation and management approaches. |
| [28084543](https://pubmed.ncbi.nlm.nih.gov/28084543/) | 2017 | Review | Zeitschrift für Rheumatologie | Reports teriparatide and bisphosphonates as the preferred treatment options for PLO based on ~100 published cases. |
| [39156353](https://pubmed.ncbi.nlm.nih.gov/39156353/) | 2024 | Case Report | Cureus | PLO patient treated aggressively with teriparatide who subsequently had a healthy second pregnancy without recurrence. |
| [30590363](https://pubmed.ncbi.nlm.nih.gov/30590363/) | 2019 | Review | Clinical Calcium | Discusses pharmacological treatment options for PLO, noting bisphosphonate and teriparatide use in severe cases. |

---

## Singapore Market Information

Teriparatide currently has **no marketing authorization in Singapore** (0 registrations, market status: Not Marketed). No product-level data is available for evaluation.

---

## Safety Considerations

**Data gap (Blocking):** Official HSA/TFDA label warnings, contraindications, and drug interaction data are not currently available for teriparatide in this evidence pack (DG001), which blocks a formal S1 safety review.

**Incidental literature safety signals** (identified during the broader search, not specific to the PLO indication):
- Osteoporosis-drug safety reviews flag potential concerns with long-term PTH analog use, including atrial fibrillation, osteonecrosis of the jaw, and atypical fractures (PMID [19412101](https://pubmed.ncbi.nlm.nih.gov/19412101/), [25118550](https://pubmed.ncbi.nlm.nih.gov/25118550/)).
- A case report describes worsening of calcinosis cutis in two patients with underlying autoimmune disease following teriparatide treatment (PMID [26992073](https://pubmed.ncbi.nlm.nih.gov/26992073/)).

Given that the PLO population is by definition pregnant or lactating, official prescribing information on use in pregnancy/lactation and fetal/infant exposure is essential before proceeding and should be sourced directly from the manufacturer's label.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple observational cohort studies and a systematic review/meta-analysis directly support teriparatide's use in PLO, with a strong and consistent mechanistic rationale (anabolic bone formation via PTH1 receptor activation). However, evidence is limited to observational/cohort designs (no RCTs, small rare-disease cohorts), and critical label-level safety data for use in a pregnant/lactating population is currently missing.

**To proceed, the following is needed:**
- Official HSA/manufacturer prescribing information, including pregnancy/lactation-specific contraindications and warnings (Blocking gap, DG001)
- Detailed mechanism of action documentation (DG002)
- Assessment of teriparatide excretion into breast milk and fetal/infant safety data
- Regulatory pathway analysis given teriparatide is currently unregistered in Singapore (e.g., named-patient or compassionate-use routes)
- Specialist/KOL input given the rarity of PLO and absence of RCT-level evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

