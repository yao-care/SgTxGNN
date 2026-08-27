---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 660
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

Using the report structure below to generate the requested evaluation report.

# Minoxidil: From Hypertension/Androgenetic Alopecia (Background) to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Minoxidil's original indication data is not present in this evidence pack (drug is not currently licensed in Singapore); it is generally known as an antihypertensive vasodilator that was later established as a topical treatment for androgenetic (pattern) hair loss. The TxGNN model's top-ranked prediction for Minoxidil is **Hypotrichosis Simplex of the Scalp**, a rare hereditary hair-loss disorder, currently supported only by **0 clinical trials** and **3 case-report publications**. Note that among the ten candidate indications in this evidence pack, a lower-ranked candidate — diffuse alopecia areata — actually carries substantially stronger evidence (see appendix below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Singapore regulatory data (drug not locally licensed). For background only: Minoxidil is generally known as an oral antihypertensive vasodilator, later repurposed topically for androgenetic alopecia — this context is not sourced from the evidence pack. |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Minoxidil is not available in this evidence pack (flagged as data gap DG002, High severity, impacting mechanistic-relevance analysis). Based on generally known pharmacology, Minoxidil is a potassium (K⁺) channel opener with direct vasodilatory activity; topically, it is thought to prolong the anagen (growth) phase of the hair cycle and increase hair-follicle papilla blood flow, which underlies its established use in androgenetic alopecia.

Hypotrichosis simplex of the scalp (HSS) is a different disease category — a rare, hereditary, monogenic disorder (commonly linked to genes such as *CDSN*) involving abnormal hair follicle development and cycling, rather than androgen-driven follicle miniaturization. Per the model's own rationale: *"Minoxidil's anagen-prolonging, follicular-blood-flow-promoting mechanism could theoretically partially compensate for the disease process, but the genetic etiology of HSS does not map directly onto Minoxidil's primary sebaceous/dermal-papilla K⁺ channel pathway — the mechanistic link is an indirect extension rather than a direct pathway match."*

In other words, the prediction is biologically plausible (both conditions involve hair follicle growth/cycling and Minoxidil is already an established hair-growth stimulant) but the connection to this specific rare hereditary disorder is inferential rather than directly demonstrated, which is consistent with the modest, case-report-only evidence base described below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case Report | Dermatologic therapy | Oral minoxidil combined with growth factors used to treat hereditary hypotrichosis simplex of the scalp. |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case Report | Frontiers in genetics | Familial case of an 8-year-old boy with *CDSN*-mutation hypotrichosis simplex, treated with a combination of botanic extracts and minoxidil; case describes clinical improvement in hair growth. |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case Report | The Journal of dermatological treatment | A 14-year-old patient with hereditary hypotrichosis simplex successfully treated with platelet-rich plasma injection combined with topical minoxidil 2%. |

All three publications are single case reports (Tier 3); none are controlled trials.

---

## Singapore Market Information

Minoxidil is currently **not marketed** in Singapore under this evidence pack, and no product license/authorization records are available (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack — notably DG001, "Product label warnings/contraindications," which is classified as a Blocking severity gap, meaning this candidate cannot yet proceed to a formal S1 safety pre-assessment until label data is obtained.)*

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic rationale is plausible but indirect, and current evidence is limited to three low-tier case reports with no clinical trials. This does not yet meet the bar for progressing beyond a research question, and a Blocking-severity data gap (missing product label safety data) also prevents formal safety pre-assessment (S1) at this time.

**To proceed, the following is needed:**
- Obtain official product label warnings/contraindications (data gap DG001, Blocking) to enable S1 safety pre-assessment
- Obtain a documented mechanism-of-action source (e.g., DrugBank) for Minoxidil (data gap DG002, High)
- Additional case series or a pilot prospective study specifically in genetically confirmed hypotrichosis simplex patients, since existing literature is limited to isolated case reports
- Confirm original indication/registration status once local (Singapore/regional) licensing data becomes available, to properly frame this as "repurposing" versus a first-in-market indication

---

## Appendix: Other Candidate Indications in This Evidence Pack (For Reference)

This evidence pack (`TW-DB00350-multi`) scored 10 candidate indications for Minoxidil. Notably, one lower-ranked candidate has considerably stronger evidence than the top-ranked prediction above and may warrant its own dedicated evaluation:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|------------|-----------------|-----------------|-----------------|
| 3 | Diffuse alopecia areata | 99.9998% | **L2** | **S2** | **Proceed with Guardrails** |
| 1 | Hypotrichosis simplex of the scalp | 99.9999% | L4 | S1 | Research Question |
| 5 | Pulmonary arterial hypertension | 99.9167% | L3 | S1 | Research Question |
| 2 | Congenital hypotrichosis milia | 99.9999% | L5 | S0 | Hold |
| 4 | Pseudopelade of Brocq | 99.9236% | L4 | S0 | Hold (evidence mismatch — retrieved literature is all androgenetic alopecia, none specific to this scarring alopecia) |
| 6 | Pulmonary arteriovenous malformation | 99.8823% | L5 | S0 | Hold |
| 7 | PAH associated with congenital heart disease | 99.8760% | L5 | S0 | Hold |
| 8 | Primary hereditary glaucoma | 99.8545% | L5 | S0 | Hold |
| 9 | PAH associated with HIV infection | 99.8484% | L5 | S0 | Hold |
| 10 | PAH associated with connective tissue disease | 99.8484% | L5 | S0 | Hold |

**Diffuse alopecia areata** (rank 3) is backed by a completed Phase 2 RCT (NCT01900041, n=74, minoxidil-containing arm) plus a European expert consensus statement (PMID 38169088) that includes Minoxidil (often alongside JAK inhibitors) as an established off-label adjunct therapy — a materially stronger evidence base than the top-ranked prediction. If the goal is to identify the most actionable repurposing opportunity for Minoxidil rather than strictly the highest TxGNN score, this candidate is recommended for a dedicated follow-up evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

