---
layout: default
title: Protein C
parent: 僅模型預測 (L5)
nav_order: 830
evidence_level: L5
indication_count: 10
---

# Protein C
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

Using no skill (this is a direct content-generation task per explicit template instructions in the prompt, not a coding/debugging/brainstorming task) — proceeding directly per the CLAUDE.md prompt spec.

---

# Protein C: From Congenital Protein C Deficiency to Inherited Thrombophilia

*(Multi-candidate evaluation — TxGNN screened 10 predicted indications for this drug; see screening summary below for why 9 of 10 were rejected.)*

## One-Sentence Summary

Protein C (DrugBank DB11312) is a vitamin K–dependent anticoagulant protein whose known therapeutic role is replacement therapy in **congenital Protein C deficiency**; it currently has **no marketing authorization in Singapore**. TxGNN generated 10 candidate indications for this drug, but the **highest-scoring prediction (Glanzmann thrombasthenia, 98.6%) and eight others are bleeding/platelet disorders where an anticoagulant would worsen, not treat, the disease** — none of these are supported by relevant trials or literature. The only mechanistically and clinically credible candidate, **inherited thrombophilia (ranked #8, score 90.0%)**, is backed by **2 completed trials directly testing Protein C concentrate** plus a post-marketing registry — but this reflects Protein C's already-established biology rather than a genuinely new indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not present in this evidence pack (`original_indications` empty; Singapore: unregistered). Publicly, Protein C concentrate (e.g., Ceprotin) is used for congenital Protein C deficiency. |
| Predicted New Indication | Inherited thrombophilia (rank #8 of 10) — the only candidate with supporting evidence; not a genuinely novel indication (see rationale below) |
| TxGNN Prediction Score | 90.01% (rank #8). Note: the top-ranked candidate by score, Glanzmann thrombasthenia, scored 98.60% but was mechanistically rejected (see Screening Summary) |
| Evidence Level | L2 (inherited thrombophilia); **L5 for all other 9 candidates** |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** on novel repurposing overall; **Proceed with Guardrails** applies only to inherited thrombophilia, which confirms known biology rather than opening a new indication |

---

## TxGNN Screening Summary — Why 9 of 10 Candidates Were Rejected

| Rank | Predicted Disease | Score | Trials / Lit | Mechanistic Assessment | Recommendation |
|------|-------------------|-------|--------------|------------------------|-----------------|
| 1 | Glanzmann thrombasthenia | 98.60% | 0 / 2 (unrelated) | Congenital bleeding disorder from GPIIb/IIIa defect; anticoagulant would worsen bleeding | Hold |
| 2 | Primary release disorder of platelets | 98.59% | 50 (unrelated) / 5 | Platelet granule-release defect (bleeding); opposite mechanism needed | Hold |
| 3 | Pseudo-von Willebrand disease | 98.12% | 1 (unrelated) / 0 | GPIbα gain-of-function bleeding disorder; opposite mechanism | Hold |
| 4 | Hemorrhagic disorder due to constitutional thrombocytopenia | 95.44% | 3 (unrelated) / 1 | Bleeding disorder requiring pro-hemostatic therapy | Hold |
| 5 | Bleeding diathesis due to collagen receptor defect | 95.39% | 1 (unrelated) / 0 | GPVI-type bleeding disorder | Hold |
| 6 | Scott syndrome | 95.04% | 31 (unrelated) / 0 | Phospholipid-scramblase bleeding disorder | Hold |
| 7 | Platelet-type bleeding disorder | 91.03% | 50 (unrelated, incl. antiplatelet studies) / 0 | Bleeding disorder; some "hits" are actually antiplatelet drug trials (opposite direction) | Hold |
| **8** | **Inherited thrombophilia** | **90.01%** | **2 direct (Grade A) + 1 analogous (Grade B)** / **20 reviews/guidelines** | **Protein C deficiency is a defined cause of inherited thrombophilia; direct mechanistic match** | **Proceed with Guardrails** |
| 9 | Fetal/neonatal alloimmune thrombocytopenia | 89.97% | 0 / 0 | Immune-mediated platelet destruction; unrelated mechanism, zero evidence | Hold |
| 10 | "Flood factor deficiency" | 89.56% | 0 / 0 | Likely a disease-ontology naming error/artifact (possibly intended as a coagulation factor deficiency); no evidence, entity needs verification before any further review | Hold |

**Pattern observed:** TxGNN clustered this drug's embedding near "hemostasis/coagulation" disease terms, but 9 of 10 hits are bleeding disorders — the pharmacological opposite of what an anticoagulant protein should treat. This looks like semantic-neighbor noise in the knowledge graph rather than genuine repurposing signal. Rank #8 is the exception because it is mechanistically concordant, not because of graph proximity.

---

## Why is This Prediction Reasonable? (Inherited Thrombophilia, Rank #8)

`original_moa` is marked as a data gap in this evidence pack. However, the evidence pack's own rationale field for this candidate documents the mechanism (sourced from DrugBank/public product information): Protein C is a **vitamin K–dependent zymogen** that is activated by the thrombin–thrombomodulin complex into **Activated Protein C (APC)**. APC, together with Protein S, proteolytically inactivates coagulation Factors Va and VIIIa, thereby down-regulating thrombin generation.

Inherited thrombophilia is, by definition, a state of insufficient natural anticoagulation — commonly caused by deficiencies in antithrombin, Protein C, or Protein S, or by gain-of-function mutations such as Factor V Leiden. **Congenital Protein C deficiency is one of the classic subtypes of inherited thrombophilia.** Replacing the deficient protein with Protein C concentrate is therefore not a speculative "new use" in the repurposing sense — it directly restores the missing physiological function. This is corroborated by:

- A completed Phase II/III trial (NCT00157118) testing Protein C Concentrate specifically in **severe congenital Protein C deficiency**, covering acute-episode treatment, short-term prophylaxis, and long-term infant prophylaxis.
- The Ceprotin Treatment Registry (NCT01127529), a long-term real-world safety/outcomes dataset.
- An ongoing Japanese post-marketing all-case surveillance study (NCT06590974).

By contrast, the other 9 candidates all describe **bleeding phenotypes** (platelet defects, receptor defects, granule-release disorders, immune platelet destruction). Administering an anticoagulant to a patient with a bleeding disorder is mechanistically contraindicated, not therapeutic — which is exactly what each candidate's own `repurposing_rationale` in the evidence pack concludes.

---

## Clinical Trial Evidence (Inherited Thrombophilia)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00157118](https://clinicaltrials.gov/study/NCT00157118) | Phase 2/3 | Completed | 18 | Direct efficacy/safety study of Protein C Concentrate in severe congenital Protein C deficiency, across acute treatment, short-term and long-term prophylaxis arms |
| [NCT01127529](https://clinicaltrials.gov/study/NCT01127529) | N/A (Registry) | Completed | 43 | Ceprotin Treatment Registry — long-term real-world treatment, safety, and outcomes data |
| [NCT06590974](https://clinicaltrials.gov/study/NCT06590974) | N/A (Post-marketing surveillance) | Recruiting | 7 | Japan all-case surveillance of Ceprotin IV 1000IU for congenital Protein C deficiency |
| [NCT00110513](https://clinicaltrials.gov/study/NCT00110513) | Phase 3 | Completed | 18 | Analogous natural-anticoagulant replacement (Antithrombin Alfa) in hereditary antithrombin deficiency at high thrombosis risk — supports the replacement-therapy class rationale, not the same drug |
| [NCT00161720](https://clinicaltrials.gov/study/NCT00161720) | N/A | Completed | 11 | Retrospective dosing/outcome data for Protein C concentrate under Emergency Use IND in severe congenital Protein C deficiency |

*Note: this candidate's evidence set also contained many co-occurring but unrelated trials (e.g., hemophilia A, swim training, thalassemia coagulation markers); only entries with a direct or class-level mechanistic link to Protein C replacement are shown.*

---

## Literature Evidence (Inherited Thrombophilia)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37334488](https://pubmed.ncbi.nlm.nih.gov/37334488/) | 2023 | Guideline | BJOG | RCOG Green-top Guideline recommends thrombophilia testing (including Protein C) in recurrent miscarriage work-up |
| [35163742](https://pubmed.ncbi.nlm.nih.gov/35163742/) | 2022 | Review | Int J Mol Sci | Severe inherited thrombophilia (incl. Protein C deficiency) carries high thrombosis risk and affects anticoagulation duration decisions |
| [38733983](https://pubmed.ncbi.nlm.nih.gov/38733983/) | 2024 | Review | Semin Thromb Hemost | Discusses selective vs. indiscriminate thrombophilia screening strategy |
| [24739277](https://pubmed.ncbi.nlm.nih.gov/24739277/) | 2014 | Review | J Pharm Pract | Overview of inherited thrombophilia incl. Protein C/S and antithrombin deficiencies, clinical management |
| [32860294](https://pubmed.ncbi.nlm.nih.gov/32860294/) | 2021 | Cohort | Am J Reprod Immunol | Large cohort study on thrombophilia prevalence in recurrent miscarriage patients |
| [37393002](https://pubmed.ncbi.nlm.nih.gov/37393002/) | 2023 | Molecular study | J Thromb Haemost | Molecular basis of inherited Protein C deficiency via PROC signal/propeptide mutations |
| [26271270](https://pubmed.ncbi.nlm.nih.gov/26271270/) | 2016 | Review | Thromb Haemost | Reviews natural anticoagulant deficiencies (antithrombin, Protein C, Protein S) as VTE risk factors |
| [16574555](https://pubmed.ncbi.nlm.nih.gov/16574555/) | 2006 | Review | Crit Rev Clin Lab Sci | Comprehensive review of inherited thrombophilia pathophysiology |
| [22082521](https://pubmed.ncbi.nlm.nih.gov/22082521/) | 2011 | Review | Crit Care Clin | Hypercoagulable states, inherited vs. acquired, including Protein C pathway |
| [31025650](https://pubmed.ncbi.nlm.nih.gov/31025650/) | 2019 | Review | Kardiol Pol | Inherited thrombophilia and myocardial infarction risk — evidence and uncertainties |

---

## Singapore Market Information

Protein C currently has **no HSA marketing authorization in Singapore** (`total_licenses: 0`, `licenses: []`). No product listing table can be produced from the available data.

---

## Safety Considerations

Please refer to the package insert for safety information. *(All safety fields in this evidence pack — key warnings, contraindications, and DDI query — are marked as data gaps; DG001 in the input flags this as a **Blocking** gap that must be resolved before any formal safety evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold** (for genuine repurposing purposes) — with **Proceed with Guardrails** applicable narrowly to inherited thrombophilia, which is confirmatory rather than novel.

**Rationale:**
- 9 of the 10 TxGNN-predicted indications are bleeding/platelet disorders that are mechanistically incompatible with an anticoagulant protein — including the single highest-scoring prediction (Glanzmann thrombasthenia). No trial or literature evidence supports any of these 9.
- The one candidate with real supporting evidence (inherited thrombophilia, L2) is not a new discovery — it reflects Protein C's already-known role in treating Protein C–deficiency thrombophilia (e.g., Ceprotin). It does not represent an actionable *new* market opportunity distinct from the drug's existing approved use.
- Rank #10 ("flood factor deficiency") appears to be a disease-ontology naming artifact and should not be evaluated further until the entity is verified.

**To proceed, the following is needed:**
- Resolve **DG001** (blocking): obtain TFDA/HSA label warnings and contraindications before any S1 safety screening.
- Resolve **DG002**: confirm formal MOA record via DrugBank API (currently inferred only from the rationale text, not from a structured `original_moa` field).
- If commercial interest exists in Singapore, a fresh HSA registration pathway would be required, as the drug is currently unregistered (`未上市`).
- Verify the "flood factor deficiency" disease entity against standard ontologies (e.g., MONDO/UMLS) before deciding whether it warrants re-evaluation.
- If further repurposing screening is desired for this drug, consider constraining the TxGNN candidate set to disease categories consistent with anticoagulant/anti-thrombotic mechanisms (e.g., other thrombophilic or pro-thrombotic conditions) rather than the hemostasis-disorder cluster returned here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

