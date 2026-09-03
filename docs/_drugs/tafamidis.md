---
layout: default
title: Tafamidis
parent: 僅模型預測 (L5)
nav_order: 939
evidence_level: L5
indication_count: 10
---

# Tafamidis
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

# Tafamidis: From Transthyretin Amyloidosis to Primary Amyloidosis

## One-Sentence Summary

Tafamidis is a transthyretin (TTR) stabilizer whose established clinical use — evident from the literature attached to this pack — is transthyretin amyloid cardiomyopathy and polyneuropathy (ATTR-CM/ATTR-PN); however, this evidence pack's formal registry fields for original indication, MOA, and Taiwan/Singapore licensing are all empty (data gaps).
TxGNN's algorithmic top-ranked output, **primary release disorder of platelets** (score 89.27%), was explicitly flagged by the evidence reviewers as a likely knowledge-graph false positive with **no** supporting trials, literature, or mechanistic rationale.
The only candidate in this pack with substantial evidence is **Primary Amyloidosis** (rank 5, 18 trials, 20 publications), but the attached evidence describes transthyretin (ATTR) rather than light-chain (AL) amyloidosis — suggesting this is most likely tafamidis's already-known indication resurfacing, not a genuinely new one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in registry data (data gap). Literature within this pack indicates established use in transthyretin amyloid cardiomyopathy/polyneuropathy (ATTR-CM/ATTR-PN) |
| Predicted New Indication | Primary Amyloidosis (evidence-based selection; TxGNN's rank-1 output "primary release disorder of platelets," score 89.27%, was excluded — flagged as a likely false positive, see note below) |
| TxGNN Prediction Score | 85.00% (rank 5 by score, but rank 1 by evidence quality) |
| Evidence Level | L2 (1 completed pivotal Phase 3 RCT — ATTR-ACT/NEJM 2018 — plus multiple Phase 2/4 and observational studies) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

> **Note on candidate selection:** Of the 10 TxGNN-ranked candidates in this pack, ranks 1–4, 7, 9, and 10 (platelet release disorder, thrombocytopenic purpura, pseudo-von Willebrand disease, Glanzmann thrombasthenia, primary hyperoxaluria, biotin metabolic disease, mixed-type autoimmune hemolytic anemia) all carry **zero clinical/literature evidence** and are explicitly annotated as mechanistically implausible knowledge-graph noise. Rank 8 ("dermis disease") has one trial, but its content (long-term ATTR-PN safety extension) does not match the disease label — flagged as a probable ontology/mapping error. Only ranks 5 and 6 (both amyloidosis-related) carry real evidence, which is why this report centers on rank 5.

---

## Why is This Prediction Reasonable?

Detailed structured MOA data is not available in this pack (data gap). However, the attached literature (PMID 34999558, PMID 38031770) consistently describes tafamidis as a small molecule that binds the thyroxine-binding sites of transthyretin (TTR) with negative cooperativity, kinetically stabilizing the native tetramer and preventing its dissociation into monomers that misfold and aggregate into amyloid fibrils. This mechanism is disease-agnostic with respect to the *site* of amyloid deposition — the same stabilized TTR tetramer is relevant whether fibrils accumulate in the myocardium (cardiomyopathy) or peripheral nerves (polyneuropathy).

The predicted indication "primary amyloidosis" and the related rank-6 candidate "acquired amyloid peripheral neuropathy" are consistent with this mechanism — but the supporting evidence (PMID 30145929, the pivotal ATTR-ACT NEJM trial; PMID 26662359; PMID 31407119) is specific to **transthyretin (ATTR)** amyloidosis, not **light-chain (AL)** amyloidosis, which is what "primary amyloidosis" typically refers to clinically. This strongly suggests a disease-label/ontology overlap in the knowledge graph rather than a genuinely novel therapeutic hypothesis: TxGNN and the evidence pipeline are most likely recovering tafamidis's **already-established** ATTR indication under an imprecise disease term, rather than identifying a new repurposing opportunity.

---

## Clinical Trial Evidence

*(Evidence shown for "Primary Amyloidosis," the only substantively evidenced candidate in this pack)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04828993](https://clinicaltrials.gov/study/NCT04828993) | Phase 4 | Completed | 15 | Tafamidis meglumine 20 mg oral once-daily for 72 weeks in ATTR-PN patients in China; efficacy/safety/pharmacodynamics |
| [NCT00630864](https://clinicaltrials.gov/study/NCT00630864) | Phase 2 | Completed | 21 | Fx-1006A (tafamidis) TTR stabilization and clinical outcomes in non-V30M ATTR amyloidosis |
| [NCT05489523](https://clinicaltrials.gov/study/NCT05489523) | Phase 4 | Recruiting | 25 | Safety, efficacy, PK of tafamidis in ATTR-CA patients post orthotopic heart transplant |
| [NCT07298044](https://clinicaltrials.gov/study/NCT07298044) | Phase 4 | Not yet recruiting | 50 | Serum TTR levels with acoramidis in ATTR-CM patients previously treated with tafamidis |
| [NCT06251778](https://clinicaltrials.gov/study/NCT06251778) | N/A | Recruiting | 200 | Real-world prospective registry of ATTRwt patients on tafamidis 61 mg |
| [NCT00628745](https://clinicaltrials.gov/study/NCT00628745) | N/A | Completed | 6,718 | THAOS — global longitudinal observational survey of ATTR (hereditary and wild-type) natural history |
| [NCT04801329](https://clinicaltrials.gov/study/NCT04801329) | N/A | Active, not recruiting | 110 | Korean post-marketing surveillance of Vyndamax (tafamidis) for ATTR-CM safety/effectiveness |
| [NCT06086353](https://clinicaltrials.gov/study/NCT06086353) | N/A | Completed | 6 | Post-marketing safety surveillance of VyndaMx (tafamidis 61 mg) in ATTR-CM patients, India |
| [NCT05374564](https://clinicaltrials.gov/study/NCT05374564) | Phase 1 | Completed | 12 | Novel 18F-flutemetamol PET imaging in ATTR cardiomyopathy |
| [NCT04535349](https://clinicaltrials.gov/study/NCT04535349) | N/A | Recruiting | 35 | SPECT-CT myocardial radiotracer uptake at baseline and during tafamidis treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30145929](https://pubmed.ncbi.nlm.nih.gov/30145929/) | 2018 | RCT (ATTR-ACT, pivotal) | New England Journal of Medicine | Tafamidis binds TTR, prevents tetramer dissociation/amyloidogenesis; reduced mortality and CV hospitalization in ATTR-CM |
| [41334760](https://pubmed.ncbi.nlm.nih.gov/41334760/) | 2025 | Propensity-weighted cohort | J Am Heart Assoc | Tafamidis reduces death and acute HF hospitalization in octogenarians with ATTR-CM |
| [38958150](https://pubmed.ncbi.nlm.nih.gov/38958150/) | 2024 | Real-world cohort | J Am Heart Assoc | Real-world outcomes of tafamidis-treated ATTR-CA patients stratified by NYHA class |
| [41282536](https://pubmed.ncbi.nlm.nih.gov/41282536/) | 2025 | Network meta-analysis | European Heart Journal Open | Comparative efficacy of tafamidis, acoramidis, patisiran, and vutrisiran in ATTR-CA |
| [32633805](https://pubmed.ncbi.nlm.nih.gov/32633805/) | 2020 | Systematic Review | JAMA | Systemic amyloidosis recognition, prognosis, and therapy overview |
| [38441582](https://pubmed.ncbi.nlm.nih.gov/38441582/) | 2024 | Review | JAMA | Cardiac amyloidosis due to transthyretin protein |
| [31986086](https://pubmed.ncbi.nlm.nih.gov/31986086/) | 2020 | Review | Annual Review of Medicine | Cardiac amyloidosis: overlooked, underappreciated, and treatable |
| [26662359](https://pubmed.ncbi.nlm.nih.gov/26662359/) | 2015 | Review | Neurology and Therapy | Tafamidis mechanism and efficacy in TTR-related amyloidosis |
| [31407119](https://pubmed.ncbi.nlm.nih.gov/31407119/) | 2019 | Review | Clinical Autonomic Research | Tafamidis for autonomic neuropathy in hereditary ATTR amyloidosis |
| [38031770](https://pubmed.ncbi.nlm.nih.gov/38031770/) | 2024 | Systematic Review | Cardiovasc Hematol Agents Med Chem | Chemistry, biological properties, and bioanalysis of tafamidis |

---

## Singapore Market Information

Tafamidis is currently **not registered/marketed** in Singapore under this evidence pack (0 licenses on file). No dosage form, brand name, or approved-indication text is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in this pack (flagged as a **Blocking** data gap — DG001), which prevents any S1 safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No genuinely novel, evidence-supported indication was identified in this pack. TxGNN's top-scoring outputs (platelet disorders, purpura, hyperoxaluria, biotin metabolism, hemolytic anemia) are explicitly annotated as mechanistically implausible false positives with zero supporting evidence. The one candidate with substantial evidence, "primary amyloidosis," appears to reflect tafamidis's already-established transthyretin amyloidosis use rather than a new repurposing signal, and a blocking safety data gap (TFDA/HSA warnings and contraindications) precludes any safety pre-assessment regardless.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications, DDI) to close the Blocking data gap (DG001)
- DrugBank MOA record to confirm/replace the current data gap (DG002)
- Original indication and regulatory license text (Taiwan/Singapore or reference market) to establish a true baseline for "new vs. already-approved" comparison
- Clarification of whether "primary amyloidosis" and "acquired amyloid peripheral neuropathy" fall within tafamidis's existing approved label — if so, both should be excluded as non-novel
- Ontology/mapping review for the rank-8 "dermis disease" candidate, whose only supporting trial (NCT00791492) describes an unrelated ATTR-PN safety extension study — likely a disease-label mapping error worth flagging to the KG/evidence pipeline maintainers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

