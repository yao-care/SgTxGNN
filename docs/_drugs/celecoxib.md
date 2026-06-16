---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Arthritis & Inflammatory Pain to Inflammatory Spondylopathy

## One-Sentence Summary

Celecoxib is a selective COX-2 inhibitor (coxib) with established global approvals for osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis, though it is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** (encompassing ankylosing spondylitis and axial spondyloarthritis),
with **19 clinical trials** — including multiple completed Phase 3 RCTs that directly studied Celecoxib in this indication — and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoarthritis, rheumatoid arthritis, ankylosing spondylitis (global approvals; not currently registered in Singapore) |
| Predicted New Indication | Inflammatory Spondylopathy |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on Celecoxib's well-characterised pharmacological profile, it is a selective cyclooxygenase-2 (COX-2) inhibitor — the first coxib to reach clinical practice — that blocks the conversion of arachidonic acid to prostaglandin E2 (PGE2), thereby reducing inflammation, pain, and fever while sparing the gastric-protective COX-1 pathway. COX-2 is markedly upregulated at sites of synovial and entheseal inflammation, which are hallmark features of spondyloarthritis.

In inflammatory spondylopathy (including ankylosing spondylitis and axial spondyloarthritis), COX-2–driven PGE2 production at the sacroiliac joints and vertebral end-plates is the central driver of inflammatory back pain, morning stiffness, and progressive bony ankylosis. NSAIDs — and coxibs in particular — have been first-line pharmacotherapy for this condition for over two decades. Celecoxib is approved for ankylosing spondylitis by the FDA and EMA, which independently validates the TxGNN model's prediction for this mechanistic connection.

What makes Celecoxib especially compelling beyond symptom control is emerging evidence of a potentially unique disease-modifying effect. A 2025 systematic analysis (PMID 39757202) demonstrated that Celecoxib — unlike non-selective NSAIDs such as diclofenac — inhibited radiographic bone progression in spondyloarthritis. The proposed mechanism involves suppression of Dickkopf-1 (DKK-1) and Sclerostin, key negative regulators of the Wnt/β-catenin pathway that governs syndesmophyte (bony bridge) formation. This bone-protective signal appears independent of COX inhibition per se, positioning Celecoxib as the only NSAID with credible disease-modification potential in this condition — a finding with direct implications for Singapore patients currently without access to this agent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week RCT comparing Celecoxib 200 mg QD, 200 mg BID, and Diclofenac 75 mg SR BID in ankylosing spondylitis — core pivotal efficacy and safety data for this indication |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | 6-week RCT in Chinese AS patients comparing Celecoxib 200 mg QD vs Diclofenac SR, followed by a 6-week extension on Celecoxib 400 mg QD — confirms efficacy in an East Asian population |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: Celecoxib + Golimumab (anti-TNF) vs Golimumab alone over 2 years in radiographic axSpA — evaluated whether adding an NSAID to biologic therapy slows structural spinal progression |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Celecoxib 200 mg BID vs Etanercept 50 mg QW vs combination in active AS over 54 weeks — MRI SPARCC scoring of sacroiliac joints; establishes Celecoxib's positioning in the biologic era |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | 12-week confirmatory RCT: Celecoxib 200 mg QD vs 400 mg QD vs Diclofenac TID in AS — designed to confirm results of a prior 6-week trial |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | MRI assessment of NSAID effects on sacroiliac joint inflammatory lesions in axSpA — small imaging pilot study |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials comparing selective COX-2 inhibitors vs non-selective COX inhibitors in axSpA for disease activity and HRQoL; terminated before full enrolment |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminated | 9 | Pilot RCT of 4 NSAIDs (including Celecoxib) in axSpA comparing pain score change at 4 vs 6 weeks; terminated due to severe under-recruitment — evidence value limited |
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | TNF inhibitor dose reduction in stable AS — NSAIDs used as background therapy; Celecoxib is not the primary study intervention |
| [NCT02456363](https://clinicaltrials.gov/study/NCT02456363) | Phase 2 | Unknown | 300 | Adalimumab + NSAIDs vs Adalimumab alone in AS — observational registry design; limited Celecoxib-specific efficacy data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Systematic Review / Meta-analysis | BMB Reports | Celecoxib is the only NSAID shown to inhibit bone progression in SpA; proposes a unique mechanism via DKK-1 and Sclerostin suppression, independent of COX inhibition |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | RCT | Clinical Rheumatology | Imrecoxib vs Celecoxib in axSpA: both drugs reduced sacroiliac joint inflammation via modulation of bone metabolism markers and angiogenesis, with clinical efficacy correlated to biomarker changes |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Medical Science Monitor | Imrecoxib vs Celecoxib 200 mg BID in axSpA (n=51, 12 weeks): comparable efficacy; DKK-1 serum levels correlated with MRI imaging score improvements |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT (CONSUL trial publication) | Annals of the Rheumatic Diseases | Full publication of CONSUL trial: Celecoxib + Golimumab vs Golimumab monotherapy in r-axSpA — detailed radiographic spinal progression outcomes over 2 years |
| [38832489](https://pubmed.ncbi.nlm.nih.gov/38832489/) | 2024 | RCT | Scandinavian Journal of Rheumatology | Iguratimod + Celecoxib vs placebo + Celecoxib in active axSpA: randomised, double-blind, placebo-controlled assessment of iguratimod add-on efficacy and safety |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Retrospective Cohort | Scandinavian Journal of Rheumatology | Nationwide study comparing CVD and gastrointestinal bleeding risk between Celecoxib and non-selective NSAIDs specifically in AS patients — finds comparable safety profiles |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Umbrella Review | Drugs | Systematic synthesis of all meta-analyses reporting Celecoxib safety in chronic musculoskeletal conditions — most comprehensive safety overview available |
| [25623277](https://pubmed.ncbi.nlm.nih.gov/25623277/) | 2015 | Retrospective Cohort | Arthritis Care & Research | Swedish national population-based cohort: rates of GI, renovascular, and CVD adverse events with etoricoxib, celecoxib, and nsNSAIDs in AS/SpA patients vs unexposed controls |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Narrative Review | Drugs | Comprehensive review of Celecoxib in OA, RA, and AS: established analgesic/anti-inflammatory efficacy and GI tolerability advantage vs nonselective NSAIDs |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | RCT | Journal of Rheumatology | Celecoxib is efficacious and well tolerated in treating signs and symptoms of ankylosing spondylitis — one of the early pivotal AS-specific efficacy studies |

---

## Singapore Market Information

Celecoxib is currently **not registered in Singapore** and has no Health Sciences Authority (HSA) product licences. No product entries are available for tabulation.

> **Context:** Globally, Celecoxib (brand name Celebrex®) is approved by the FDA and EMA for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, juvenile idiopathic arthritis (patients ≥2 years), acute pain in adults, and primary dysmenorrhoea. Its absence from the Singapore market represents a regulatory gap, not a lack of evidence.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note from known drug profile:** Celecoxib carries class-wide COX-2 inhibitor warnings for increased risk of serious cardiovascular events (myocardial infarction, stroke) — particularly relevant for AS patients who already carry elevated cardiovascular risk. Key contraindications from global labelling include sulfonamide hypersensitivity, aspirin/NSAID allergy (including aspirin-exacerbated respiratory disease), severe heart failure, and post-CABG use. Long-term AS therapy also requires monitoring of renal and hepatic function. These should be confirmed against full prescribing information before any Singapore regulatory submission.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Celecoxib has the strongest evidence profile of all predictions in this pack: two completed Phase 3 RCTs (n=458 and n=240), multiple completed Phase 4 RCTs, and over 20 supporting publications including a 2025 umbrella review and a novel systematic finding that Celecoxib may be the only NSAID to slow structural bone progression in spondyloarthritis. The TxGNN model's prediction is entirely consistent with established global regulatory approvals — making this a high-confidence repurposing candidate specifically for the Singapore market, where Celecoxib is currently inaccessible.

**To proceed, the following is needed:**

- **Regulatory pathway**: Determine HSA registration route for Celecoxib in Singapore (new drug application or mutual recognition pathway from FDA/EMA approval)
- **Full prescribing information**: Obtain and review complete package insert to populate safety warnings, contraindications, and drug interaction sections (currently data gaps)
- **Cardiovascular risk assessment**: Define patient eligibility criteria given COX-2 inhibitor class cardiovascular warnings and the elevated baseline CV risk in AS patients
- **Gastrointestinal risk management plan**: Evaluate co-prescription of proton pump inhibitors for at-risk patients
- **Mechanism of action documentation**: Retrieve Celecoxib's DrugBank MOA entry to complete the evidence dossier
- **Paediatric use assessment**: If JIA indication is sought alongside AS, confirm paediatric dosing (FDA-approved for ≥2 years) is appropriate for the Singapore context
- **Local clinical expert consultation**: Engage Singapore rheumatologists to assess unmet need and current prescribing practice for AS patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

