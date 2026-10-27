---
layout: default
title: Anagrelide
parent: Medium Evidence (L3-L4)
nav_order: 99
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Anagrelide: predicted new indication Reactive thrombocytosis (evidence level L4). Approved use: Thrombocythemia"
monitor_inn: "Anagrelide"
predicted_indications: ["reactive thrombocytosis", "inverse Klippel-Trenaunay syndrome", "dermatofibrosarcoma protuberans", "rheumatoid arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "juvenile idiopathic arthritis", "osteoarthritis", "pseudoachondroplasia", "rheumatoid nodulosis", "juvenile chronic polyarthritis"]
---

# Anagrelide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Anagrelide: From Thrombocythemia to Reactive Thrombocytosis
{: .text-alpha }

## One-Sentence Summary

Anagrelide is a platelet-lowering drug, originally used to treat thrombocythemia and familial thrombocytosis.
The TxGNN model predicts it may be effective for **reactive thrombocytosis**, but there are **no registered clinical trials** and the **10 publications** retrieved are mostly reviews and case reports, largely about essential thrombocythemia rather than reactive thrombocytosis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thrombocythemia; familial thrombocytosis (taken from the knowledge-graph indication data, because the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Reactive thrombocytosis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, anagrelide lowers platelet counts by inhibiting megakaryocyte maturation. It is thought to disrupt post-mitotic megakaryocyte differentiation and so reduce platelet production. Its efficacy in essential thrombocythemia and familial thrombocytosis is established.

The high TxGNN score probably reflects the close phenotypic overlap between these primary thrombocytosis conditions and reactive thrombocytosis. The clinical fit is weak, however. Reactive (secondary) thrombocytosis is driven by an underlying cause such as inflammation, iron deficiency or splenectomy, and it is generally managed by treating that cause. Platelet-lowering therapy is rarely needed. The mechanistic fit therefore does not translate into a clear clinical rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Rev Anticancer Ther | Update on anagrelide's mechanisms of action and therapeutic potential in clonal thrombocytosis; notes that reactive thrombocytosis does not require therapy |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leuk Lymphoma | Critical review of anagrelide in essential thrombocythemia and related disorders; clonal thrombocytosis may need cytoreduction, while reactive thrombocytosis is often inconsequential |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Med J Aust | Essential thrombocythaemia review; diagnosis requires excluding reactive thrombocytosis |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leuk Res | Case-based review of thrombocytapheresis for extreme thrombocytosis in myeloproliferative neoplasms |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | Am J Med Sci | Clinical spectrum of thrombocytosis and thrombocythemia |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Rinsho Ketsueki | Diagnosis and treatment of essential thrombocythemia, including anagrelide among platelet-suppressing drugs |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective case series | Pediatr Blood Cancer | 12 paediatric cases comparing essential and reactive thrombocythemia |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case report | Eur J Case Rep Intern Med | Acute myocardial infarction in a patient with essential thrombocythaemia treated with anagrelide |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case report | Srp Arh Celok Lek | Essential thrombocythemia with ankylosing spondylitis treated with anagrelide, DMARDs and etanercept |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case report | Medicine | Digit replantation in a patient with thrombocytosis after splenectomy |

No randomised controlled trial of anagrelide in reactive thrombocytosis was found.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12525P | AGRYLIN CAPSULE 0.5 mg | Capsule | Not stated in the licence record |
| SIN17118P | ANAGRELIDE MEVON CAPSULES 0.5 MG | Capsule | Not stated in the licence record |

Both licences are valid single-ingredient oral products.

---

## Cytotoxicity

Anagrelide is not a conventional cytotoxic agent, so this section is not applicable.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not package insert text):** liver failure, liver disease, kidney disease, gallbladder disease, thrombocytopenia, blood coagulation disease, heart disease, cardiovascular disease, anaemia, macrocytic anaemia, interstitial lung disease, eosinophilic pneumonia, pulmonary eosinophilia, high output heart failure. These are model-derived signals and need confirmation against the package insert.
- **Drug Interactions:** 100 interactions were found. Of the 20 listed, the following are rated **Major**: cisapride, clarithromycin, dolasetron, granisetron and levofloxacin. Many of these are QT-prolonging agents, so the concern is likely cardiac. This reading is an inference and should be confirmed against the source data. Moderate interactions include acetylsalicylic acid, famotidine, cimetidine, aprepitant, alosetron, loperamide, fenfluramine and several laxatives.

The package insert warnings and contraindications were not available, so please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is driven mainly by similarity to anagrelide's established use in primary thrombocytosis. Reactive thrombocytosis is normally managed by treating its cause, with platelet-lowering therapy rarely needed. No clinical trials exist, and the literature is mostly reviews and case reports. The cardiovascular signals in the safety data add further caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (currently a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- Evidence that a defined reactive thrombocytosis subgroup (for example, extreme or refractory thrombocytosis with thrombotic risk) would benefit from platelet-lowering therapy
- A cardiovascular risk assessment, given the knowledge-graph flags and QT-related interactions
- Confirmation of the approved indication wording on the Singapore licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

