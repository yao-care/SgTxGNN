---
layout: default
title: Nicotinamide
parent: 僅模型預測 (L5)
nav_order: 702
evidence_level: L5
indication_count: 10
---

# Nicotinamide
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

# Nicotinamide: From NAD+ Precursor Supplementation to Werner Syndrome

## One-Sentence Summary

> Nicotinamide (Vitamin B3 / niacinamide, DrugBank DB02701) is a NAD+ precursor with no marketed products currently registered in Singapore in this evidence pack.
> TxGNN screened 10 candidate indications for this drug; among them, **Werner Syndrome** — a rare premature-aging disorder caused by *WRN* gene mutations — is the only candidate supported by meaningful evidence,
> including **1 randomized controlled trial** and **6 mechanistic/review publications** linking NAD+ depletion to Werner syndrome pathology.
> *Note: TxGNN's numerically highest-ranked candidate ("zinc, elevated plasma," score 97.8%) was reviewed and found to have no clinical, mechanistic, or literature support — it is assessed as knowledge-graph noise and is not presented as the lead candidate.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available regulatory data (no marketed formulation in this pack). Nicotinamide is generically known as Vitamin B3, used for prevention/treatment of niacin (Vitamin B3) deficiency. |
| Predicted New Indication | Werner Syndrome (premature aging disorder) — selected as lead candidate based on evidence quality, not TxGNN rank order |
| TxGNN Prediction Score | 88.6% (rank #36,165 of candidate diseases; rank 4 of 10 candidates in this pack) |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nicotinamide is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, nicotinamide is a precursor in the NAD+ salvage pathway — it is converted intracellularly to nicotinamide mononucleotide (NMN) and then NAD+, a cofactor essential for mitochondrial energy metabolism, DNA repair, and mitophagy.

Werner syndrome is caused by loss-of-function mutations in the *WRN* DNA helicase gene, and multiple studies in this evidence pack (PMID 31754102, 40179319, 24757718) independently show that WRN-deficient cells exhibit depleted NAD+ and impaired mitophagy, driving the accelerated-aging phenotype. This gives a coherent mechanistic rationale: if NAD+ depletion is a driver of Werner syndrome pathology, NAD+ precursor supplementation is a biologically plausible intervention — and this is exactly the hypothesis tested in the pivotal 2025 RCT (PMID 40459998).

One important caveat: that RCT tested **nicotinamide riboside (NR)**, not nicotinamide (NAM) itself. Both are NAD+ precursors but use different salvage-pathway entry points and have different pharmacokinetics, so the RCT result cannot be directly extrapolated to nicotinamide without further study. Of the remaining 9 TxGNN-predicted indications for this drug (e.g., isolated congenital adermatoglyphia, Beare-Stevenson syndrome, oculocutaneous albinism), none have any supporting clinical trial or literature evidence and are assessed in the source data as knowledge-graph associations without biological plausibility — these are not carried forward in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for nicotinamide in Werner syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40459998](https://pubmed.ncbi.nlm.nih.gov/40459998/) | 2025 | RCT | Aging Cell | Double-blind randomized crossover placebo-controlled trial of nicotinamide riboside in Werner syndrome patients; NAD+ depletion linked to disease pathogenesis, supplementation showed clinical benefit (note: tested NR, not nicotinamide itself) |
| [31754102](https://pubmed.ncbi.nlm.nih.gov/31754102/) | 2019 | Preclinical/Mechanistic | Nature Communications | NAD+ augmentation restored mitophagy and limited accelerated aging phenotypes in Werner syndrome patient cells and WRN-deficient models |
| [34201700](https://pubmed.ncbi.nlm.nih.gov/34201700/) | 2021 | Review | Int J Mol Sci | Review of DNA damage-induced neurodegeneration in accelerated-ageing diseases including Werner syndrome, situating NAD+/DNA-repair pathways as therapeutic targets |
| [33353663](https://pubmed.ncbi.nlm.nih.gov/33353663/) | 2021 | Review | J Investigative Dermatology | Review of skin and mitochondrial abnormalities across DNA-repair-deficient premature aging disorders, including Werner syndrome |
| [24757718](https://pubmed.ncbi.nlm.nih.gov/24757718/) | 2014 | Preclinical | Aging Cell | WRN protein loss induces a metabolic shift compromising redox homeostasis, implicating NAD+/redox pathway dysfunction |
| [40179319](https://pubmed.ncbi.nlm.nih.gov/40179319/) | 2025 | Preclinical | Aging | Decreased mitochondrial NAD+ in WRN-deficient cells linked to dysfunctional proliferation and senescence |
| [38184705](https://pubmed.ncbi.nlm.nih.gov/38184705/) | 2024 | Preclinical | Cell & Bioscience | WRN loss accelerates abnormal adipocyte metabolism in Werner syndrome stem cell and zebrafish models |

---

## Singapore Market Information

No registered products found. Nicotinamide is currently **not marketed** in Singapore under this evidence pack (0 total registrations, market status: Not Marketed).

---

## Safety Considerations

No specific safety data (warnings, contraindications, or drug interactions) is available in this evidence pack — both key warnings and contraindications are marked as data gaps, and no drug-drug interaction records were found. Since nicotinamide is not currently marketed in Singapore, please refer to international reference sources (e.g., pharmacopoeial monographs, published nicotinamide/niacinamide labeling) for baseline safety information until local data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Werner syndrome is the only TxGNN-predicted indication in this pack with credible mechanistic and clinical support (L2, one RCT plus six corroborating mechanistic/review papers), but the pivotal trial tested nicotinamide riboside rather than nicotinamide itself, the drug is not currently marketed in Singapore, and mechanism-of-action and safety/contraindication data for nicotinamide remain blocking data gaps (DG001, DG002). This is not yet ready for a Go or Guardrails decision.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain package insert warnings/contraindications (or equivalent international labeling, since no Singapore registration exists)
- Resolve high-severity data gap DG002: retrieve nicotinamide's mechanism of action via DrugBank API
- Pharmacological comparison of nicotinamide (NAM) vs. nicotinamide riboside (NR) to determine whether the RCT findings can reasonably be extrapolated
- Assessment of a regulatory pathway for nicotinamide in Singapore, given it currently has zero registered products
- Consider whether a nicotinamide-specific clinical study in Werner syndrome patients is warranted before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

