---
layout: default
title: Methyl Salicylate
parent: 僅模型預測 (L5)
nav_order: 654
evidence_level: L5
indication_count: 10
---

# Methyl Salicylate
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

Using the evidence pack, I note it contains **10** TxGNN-ranked candidates for the same drug, not one — and the pack's own `repurposing_rationale` text flags the #1-ranked hit (gout) as a keyword/embedding false positive with no real mechanistic support. The only candidate reaching Evidence Level L3 with an S2 "Proceed with Guardrails" call is **osteoarthritis** (rank 6), so I built the report around that indication rather than mechanically taking `predicted_indications[0]`, and added a short screening note for transparency. Report below.

---

# Methyl Salicylate: From Topical Analgesic Use to Knee Osteoarthritis

## One-Sentence Summary

Methyl salicylate is a salicylate ester long used in OTC topical analgesic/counterirritant products (liniments, patches, sprays) for muscle and joint pain. Among 10 TxGNN-predicted indications screened for this drug, **Osteoarthritis (knee)** is the only candidate supported by real clinical evidence — **9 publications including 2 RCTs and 1 systematic review/meta-analysis** — while the model's top-ranked hit (gout) was assessed as a false positive with no relevant evidence.

## Screening Context

TxGNN scored 10 candidate indications (0.94–0.99). Eight of them — gout, bronchitis, exostosis, congestive heart failure, osteoarthritis susceptibility, acute pulmonary heart disease, pseudoachondroplasia, and multiple exostoses — returned zero or irrelevant literature/trial hits and are scored **L5 / Hold**. Two candidates had real supporting evidence: **osteoarthritis** (L3, Proceed with Guardrails) and **rheumatoid arthritis** (L3, Research Question, evidence mostly from natural methyl salicylate glycosides/plant extracts rather than the parent compound). This report focuses on osteoarthritis as the most defensible candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (data gap); known OTC use as topical analgesic/counterirritant |
| Predicted New Indication | Osteoarthritis (knee) |
| TxGNN Prediction Score | 95.63% (rank 25,138) |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for methyl salicylate is not available (DrugBank data gap, DG002). Based on known information, methyl salicylate is a salicylate ester widely formulated into OTC topical products (e.g., Bengay-type liniments, Salonpas-type patches, sports sprays) for musculoskeletal and joint pain, where its efficacy is well documented.

Mechanistically, topical salicylates act through local COX inhibition plus a counterirritant (sensory distraction) effect — the same principle already exploited commercially for generalized "muscle and joint pain," which substantially overlaps with osteoarthritis symptom management. This is not a novel biological hypothesis so much as a formal recognition of an existing off-label/OTC use pattern.

The literature base largely mirrors this: most supporting studies evaluate topical NSAID/salicylate delivery formats (patches, phonophoresis, sprays) for knee OA pain relief, rather than a distinct disease-modifying mechanism. Treatment effect should be understood as **symptomatic pain relief**, not disease modification.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32773325](https://pubmed.ncbi.nlm.nih.gov/32773325/) | 2021 | RCT | J Orthop Sci | Crossover, double-blind RCT (n=168) on anti-inflammatory drug plasters for knee OA; examined efficacy and patient usability/preference |
| [27434280](https://pubmed.ncbi.nlm.nih.gov/27434280/) | 2016 | RCT | Technol Health Care | Compared isometric vs. proprioceptive exercise on pain/stiffness in knee OA patients |
| [36552010](https://pubmed.ncbi.nlm.nih.gov/36552010/) | 2022 | Systematic Review/Meta-analysis | Biomedicines | Meta-analysis of NSAID phonophoresis for knee OA pain relief |
| [19332972](https://pubmed.ncbi.nlm.nih.gov/19332972/) | 2009 | Review | Postgraduate Medicine | Topical NSAIDs give OA pain relief similar to oral NSAIDs with fewer systemic (GI/CV/renal) adverse events |
| [13279278](https://pubmed.ncbi.nlm.nih.gov/13279278/) | 1956 | Clinical evaluation | Maryland State Med J | Early clinical evaluation of a topical methyl salicylate compound in chronic rheumatic disease |
| [1921829](https://pubmed.ncbi.nlm.nih.gov/1921829/) | 1991 | Clinical study | Medical Journal of Australia | Aerosol methyl-salicylate-based spray evaluated for arthritis pain |
| [37555294](https://pubmed.ncbi.nlm.nih.gov/37555294/) | 2023 | Preclinical (animal) | Advanced Science | Nano-enabled acupuncture-needle delivery of methyl-salicylate-modified cyclodextrin tested in a mouse knee OA model |
| [18091121](https://pubmed.ncbi.nlm.nih.gov/18091121/) | 2008 | Case report/Review | Clinical Nurse Specialist | Warns of unrecognized salicylate toxicity risk from OTC "sports cream"/arthritis rubs |
| [2778785](https://pubmed.ncbi.nlm.nih.gov/2778785/) | 1989 | Case report | J Royal Society of Medicine | Topical methylsalicylate ointment potentiated warfarin anticoagulation in a patient |

## Singapore Market Information

Methyl salicylate currently has **no marketing authorization on file** in Singapore (0 registrations, market status: not marketed). No license records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information — no structured `key_warnings`, `contraindications`, or DDI records were found (DDI query: not found; TFDA/HSA label data is a **Blocking** data gap, DG001).

That said, the literature surfaced in this pack (not from the structured safety database) flags two concrete signals worth carrying forward into any evaluation:
- **Salicylate toxicity** from unrecognized cumulative topical absorption, including fatality reports (PMID 18091121)
- **Warfarin potentiation** by topical methylsalicylate, increasing bleeding risk (PMID 2778785); a related general review of NSAID–warfarin interactions was also surfaced under the (unrelated/false-positive) CHF candidate (PMID 8672833)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two RCTs and a systematic review/meta-analysis support topical salicylate-based delivery formats for short-term knee OA pain relief, consistent with methyl salicylate's established OTC counterirritant use — but this is symptomatic relief only, and known salicylate-toxicity and anticoagulant-interaction signals require explicit guardrails before any formal indication claim.

**To proceed, the following is needed:**
- TFDA/HSA package insert data (warnings, contraindications) — currently a Blocking data gap
- Formal MOA and pharmacokinetic characterization (DrugBank data gap)
- Completed DDI screening (current query status: not found)
- Singapore marketing authorization pathway, given 0 current registrations
- Confirmation of topical dosage form/route compatibility for a knee OA indication
- If pursued, monitoring protocol for cumulative salicylate exposure and concomitant anticoagulant use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

