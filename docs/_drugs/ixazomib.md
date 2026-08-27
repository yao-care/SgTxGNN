---
layout: default
title: Ixazomib
parent: 僅模型預測 (L5)
nav_order: 557
evidence_level: L5
indication_count: 10
---

# Ixazomib
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

# Ixazomib: From Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Ixazomib (Ninlaro) is the world's first oral proteasome inhibitor, approved for the treatment of relapsed/refractory multiple myeloma (RRMM) in combination with lenalidomide and dexamethasone.
The TxGNN model predicts it may be effective for **Indolent Plasma Cell Myeloma (Smoldering Multiple Myeloma)**, supported by **2 real-world cohort studies** from the broader multiple myeloma spectrum and a strong mechanistic rationale shared between active and indolent disease subtypes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory multiple myeloma (IRd regimen, TOURMALINE-MM1 Phase 3) |
| Predicted New Indication | Indolent plasma cell myeloma (Smoldering MM) |
| TxGNN Prediction Score | 96.17% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known published information, ixazomib is the world's first oral proteasome inhibitor (boronic acid class). It selectively and reversibly inhibits the chymotrypsin-like activity of the β5 subunit of the 20S proteasome. Blocking proteasome function causes accumulation of misfolded and ubiquitinated proteins within plasma cells, triggering the unfolded protein response (UPR) and ultimately apoptosis. In the landmark TOURMALINE-MM1 Phase 3 trial, the all-oral IRd triplet (ixazomib + lenalidomide + dexamethasone) significantly improved progression-free survival in RRMM, establishing proteasome inhibition as a backbone of myeloma therapy.

Multiple myeloma and indolent plasma cell myeloma (smoldering MM, SMM) share identical cellular origin — clonal bone marrow plasma cells that overproduce immunoglobulins. Both subtypes are intrinsically dependent on continuous proteasome activity to handle the burden of excess immunoglobulin light chains. The biological distinction between SMM and active MM is primarily defined by clinical thresholds (CRAB criteria, SLiM criteria) rather than a fundamental difference in underlying molecular machinery. This means the proteasome inhibition mechanism is equally relevant at the indolent disease stage.

The TxGNN prediction score of 96.17% reflects this tight mechanistic continuity. Parallel evidence from bortezomib (an intravenous proteasome inhibitor) in high-risk SMM has already demonstrated that early proteasome inhibition can delay progression to symptomatic MM. Ixazomib's oral bioavailability and favourable tolerability profile make it a compelling candidate for this lower-intensity, pre-emptive treatment setting. Multiple real-world studies confirm that IRd achieves outcomes consistent with clinical trial data in RRMM, further validating the class effect.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registering ixazomib for indolent plasma cell myeloma have been identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38558233](https://pubmed.ncbi.nlm.nih.gov/38558233/) | 2024 | Real-world retrospective-prospective cohort | *Cancer Medicine* | Northern Italy multi-centre experience with IRd in RRMM; real-world efficacy and safety profiles were consistent with the TOURMALINE-MM1 trial, supporting generalisability of the oral proteasome inhibitor approach |
| [32193630](https://pubmed.ncbi.nlm.nih.gov/32193630/) | 2020 | Real-world retrospective cohort | *Annals of Hematology* | Multi-site Israeli registry study confirming IRd real-world outcomes in RRMM; demonstrates that ixazomib-based combinations translate from controlled trials to routine clinical practice across diverse patient populations |

> **Note:** Both studies address RRMM broadly. No study has yet specifically targeted indolent/smoldering MM with ixazomib. The evidence represents class-level and regimen-level support rather than direct indication-specific proof.

---

## Singapore Market Information

Ixazomib is currently **not registered in Singapore**. No marketing authorisation records are available. Access would require special compassionate use or clinical trial enrolment pathways.

---

## Cytotoxicity

Ixazomib is an antineoplastic agent (proteasome inhibitor) indicated for haematological malignancy; cytotoxicity assessment applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — oral proteasome inhibitor (boronic acid class) |
| Myelosuppression Risk | Moderate — thrombocytopenia is the most clinically significant haematological toxicity (most nadir occurring around Day 14–21 of cycle); neutropenia and anaemia also reported |
| Emetogenicity Classification | Low to moderate (oral agent; nausea and vomiting reported but generally manageable without routine prophylaxis) |
| Monitoring Items | CBC with differential and platelet count (each cycle, especially early cycles); liver function tests; renal function (ixazomib exposure increases in severe renal impairment); peripheral neuropathy assessment (clinical neurological examination each cycle) |
| Handling Protection | Standard cytotoxic oral drug handling precautions required; capsules should not be crushed or opened |

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, drug interactions) was not available in the current evidence pack. Please refer to the Ninlaro (ixazomib) package insert and the Medicines.org.uk/MIMS database for complete prescribing information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ixazomib shares the same validated proteasome inhibition mechanism as bortezomib, which has already demonstrated clinical benefit in high-risk smoldering MM; the TxGNN score of 96.17% and the biological continuity between indolent and active plasma cell myeloma provide a compelling mechanistic basis for this repurposing direction, even though direct clinical trial evidence for indolent plasma cell myeloma specifically is still lacking.

**To proceed, the following is needed:**
- Prospective clinical trial data specifically targeting indolent/smoldering MM with ixazomib (Phase 2 exploratory trial recommended)
- Full package insert review to document key warnings, contraindications, and dose adjustments for SMM patient population (typically treatment-naïve, lower disease burden)
- Comprehensive drug-drug interaction assessment (especially CYP3A inducers/inhibitors relevant to the oral route)
- Singapore regulatory pathway evaluation — formal application to HSA or Named Patient Programme access given current non-registered status
- Risk stratification framework: restrict initial use to high-risk SMM (per 20/2/20 model) where benefit-risk ratio is most favourable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

