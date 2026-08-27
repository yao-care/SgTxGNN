---
layout: default
title: Indomethacin
parent: 僅模型預測 (L5)
nav_order: 526
evidence_level: L5
indication_count: 10
---

# Indomethacin
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

# Indomethacin: From Inflammatory Arthritis to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Indomethacin is a potent non-steroidal anti-inflammatory drug (NSAID) with decades of clinical history, originally used to treat inflammatory conditions including rheumatoid arthritis, ankylosing spondylitis, and gouty arthritis. The TxGNN model predicts it may be effective for **Juvenile Idiopathic Arthritis (JIA)** — the most evidenced actionable candidate among 10 predicted indications — supported by **0 registered clinical trials** and **20 publications**. Among all predicted indications, JIA (Rank 8) carries the strongest mechanistic grounding and achieves the highest evidence level (L2) with a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory arthritis and pain conditions (rheumatoid arthritis, ankylosing spondylitis, gout) — no Singapore registration on record |
| Predicted New Indication | Juvenile Idiopathic Arthritis (JIA) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note:** This is a multi-indication evaluation pack (10 predictions total). Ranks 1–7 and 9–10 all carry L4–L5 evidence with "Hold" recommendations, primarily due to KG topology bias around rare skeletal/developmental diseases (brachydactyly-syndactyly, brachyolmia, colobomatous microphthalmia, etc.) where Indomethacin has no plausible mechanistic rationale. JIA (Rank 8) is the sole indication with genuine clinical evidence and is therefore the primary focus of this report.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on well-established pharmacology, Indomethacin is one of the most potent non-selective NSAIDs, acting by inhibiting cyclooxygenase-1 (COX-1) and cyclooxygenase-2 (COX-2) enzymes. This reduces synthesis of prostaglandins — in particular prostaglandin E2 (PGE2) — the central mediators of pain, fever, and joint inflammation. Its anti-inflammatory potency is broadly regarded as superior to most other NSAIDs in its class.

The pathological core of JIA is prostaglandin-driven synovial inflammation, joint swelling, and progressive cartilage destruction. Since PGE2 directly promotes synovial hyperplasia and leukocyte recruitment in inflamed joints, COX inhibition aligns precisely with JIA's underlying pathophysiology. This is not a novel hypothesis: historically, Indomethacin was one of the standard first-line therapies for JIA (then termed "juvenile rheumatoid arthritis" or JRA) and remains particularly noted for its efficacy in controlling systemic-onset JIA fever.

In the pre-biologic era, NSAIDs including Indomethacin formed the cornerstone of JIA management. While IL-1, IL-6, and TNF inhibitors have shifted the treatment paradigm for moderate-to-severe JIA, NSAIDs including Indomethacin remain relevant for symptom control, especially in milder oligoarticular disease. The TxGNN prediction is therefore mechanistically grounded and historically validated. The primary constraint for Singapore is the absence of any HSA product registration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Indomethacin in Juvenile Idiopathic Arthritis on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [362571](https://pubmed.ncbi.nlm.nih.gov/362571/) | 1978 | Double-blind RCT | South African Medical Journal | Ketoprofen vs. indomethacin in 30 children with juvenile chronic arthritis; both drugs proved safe and effective; indomethacin emerged as the preferred drug in this head-to-head comparison |
| [28418334](https://pubmed.ncbi.nlm.nih.gov/28418334/) | 2017 | Review | Balkan Medical Journal | Comprehensive overview of JIA subtypes, epidemiology, clinical features, and management strategies including NSAID use as initial therapy |
| [1379157](https://pubmed.ncbi.nlm.nih.gov/1379157/) | 1992 | Review | Drugs | Pharmacological management of JRA: goals of suppressing synovitis and controlling systemic inflammation; NSAIDs including indomethacin described as core first-line agents |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Review | British Journal of Rheumatology | NSAIDs in paediatric rheumatic diseases; indomethacin and salicylates used for systemic JCA fever, though noted as more toxic than ibuprofen and diclofenac for joint symptom control |
| [22573189](https://pubmed.ncbi.nlm.nih.gov/22573189/) | 2012 | Review/Cohort | Swiss Medical Weekly | Systemic-onset JIA (Still's disease): disease characteristics unique from other JIA subtypes; discusses long-term outcomes and role of conventional therapy including NSAIDs |
| [5632159](https://pubmed.ncbi.nlm.nih.gov/5632159/) | 1967 | Case Series | Arzneimittel-Forschung | Early long-term clinical experience with indomethacin specifically in juvenile rheumatoid arthritis and Still's disease; one of the earliest primary-use reports |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Review | Clinical Pharmacokinetics | Pharmacokinetics of drugs used in juvenile arthritis including NSAIDs; reviews indomethacin dosing characteristics relevant to pediatric populations |
| [7417361](https://pubmed.ncbi.nlm.nih.gov/7417361/) | 1980 | Comparative Cohort | Arthritis and Rheumatism | Cross-national JRA comparison (USSR vs. USA); documents therapeutic diversity including indomethacin and aspirin as contemporaneous NSAID options |
| [28086918](https://pubmed.ncbi.nlm.nih.gov/28086918/) | 2017 | Cohort | Pediatric Rheumatology Online Journal | Atypical monoarthritis presentations in oligoarticular JIA; documents clinical heterogeneity and management challenges in this most common JIA subtype |
| [23312448](https://pubmed.ncbi.nlm.nih.gov/23312448/) | 2013 | Research Article | Cytotherapy | Mesenchymal stromal cells from children with systemic JIA suppress innate and adaptive immune responses — provides immunological context for JIA pathogenesis |

---

## Singapore Market Information

Indomethacin is currently **not registered** with Singapore's Health Sciences Authority (HSA). No product authorizations are on record. Any clinical use or repurposing development in Singapore would require full HSA registration, including submission of product dossiers covering safety, quality, and efficacy.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields in this evidence pack are data gaps: TFDA prescribing information warnings and contraindications have not been retrieved, and the DDI query returned no results. These are classified as blocking data gaps that must be resolved before proceeding to regulatory submission.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Indomethacin's efficacy in JIA is mechanistically well-grounded (COX inhibition → reduced PGE2 → suppression of prostaglandin-driven synovitis) and historically documented, including a direct double-blind RCT in juvenile chronic arthritis (PMID 362571) and multiple clinical reviews confirming its role in the pre-biologic JIA treatment landscape. The TxGNN score of 99.84% and L2 evidence level support advancing this candidate — but the complete absence of Singapore HSA registration and unresolved safety data gaps require structured remediation before proceeding.

**To proceed, the following is needed:**

- **Regulatory pathway:** Initiate HSA product registration; no Singapore marketing authorization currently exists
- **Safety data (Blocking):** Retrieve and review full prescribing information warnings, contraindications, and special population precautions (pediatric dosing, hepatic/renal considerations)
- **MOA documentation:** Retrieve DrugBank MOA record to complete mechanistic rationale for regulatory dossier
- **DDI profile:** Re-query drug interaction databases (e.g., DrugBank DDI, Lexicomp) — current query returned no results, which is likely a data issue rather than absence of interactions
- **Comparative effectiveness:** Evaluate positioning relative to current JIA biologics (anakinra, tocilizumab, etanercept); define the patient population where Indomethacin adds value (mild oligoarticular disease, systemic fever control, adjunctive use)
- **Pediatric PK/PD:** Confirm appropriate dosing and safety monitoring parameters for the Singapore pediatric JIA population

---

*This report is for research reference only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

