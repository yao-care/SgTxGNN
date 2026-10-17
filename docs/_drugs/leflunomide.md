---
layout: default
title: Leflunomide
parent: Low Evidence (L5)
nav_order: 584
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Leflunomide: predicted new indication Plasma cell myeloma (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "Leflunomide"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "indolent plasma cell myeloma", "plasma cell myeloma", "myeloid leukemia", "Meester-Loeys syndrome", "ganglioneuroblastoma (disease)", "WHIM syndrome", "scalp dermatosis", "vertebral anomalies and variable endocrine and T-cell dysfunction"]
---

# Leflunomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Leflunomide: From Rheumatoid Arthritis to Plasma Cell Myeloma

## One-Sentence Summary

Leflunomide is an oral immunomodulatory drug originally used for **rheumatoid arthritis** and **psoriatic arthritis**.
The TxGNN model predicts it may be effective for **plasma cell myeloma (multiple myeloma)**, supported by **5 clinical trials** (1 completed Phase 1/2, no randomised trials) and several preclinical and early clinical publications.
The evidence is early-stage, and efficacy has not yet been shown in controlled trials.

> **Note on candidate selection:** The two highest-scoring predictions (brachydactyly-syndactyly syndrome and colobomatous microphthalmia-rhizomelic dysplasia syndrome, both about 99.9%) have no trials, no literature and no plausible mechanism. Leflunomide is also known to be teratogenic, which argues against use in congenital conditions. This report therefore focuses on plasma cell myeloma, the highest-ranked prediction with direct clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis; psoriatic arthritis (from the knowledge-graph indication record, because Singapore registration entries list no indication text) |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 95.16% |
| Evidence Level | L2 (provisional; only early-phase trials exist, no completed Phase 2/3 RCT) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the compiled drug record. Based on the published literature, leflunomide is a prodrug. Its active metabolite, teriflunomide (A771726), inhibits **dihydroorotate dehydrogenase (DHODH)**, an enzyme needed to make pyrimidine nucleotides. In rheumatoid arthritis, this slows the proliferation of activated lymphocytes.

Myeloma cells are rapidly dividing plasma cells with a high demand for nucleotides. Laboratory studies show that DHODH is expressed in myeloma cell lines and primary myeloma cells, and that blocking it causes apoptosis and reduced proliferation. Teriflunomide also lowers c-Myc expression by targeting PIM kinases. In a mouse model, leflunomide combined with lenalidomide extended survival. Other work suggests a mitochondria-independent cytotoxic effect and a possible link to mitochondrial fusion pathways.

Both rheumatoid arthritis and myeloma involve over-active immune-lineage cells, so the same pyrimidine-depletion mechanism could apply. A Phase 1 study in relapsed/refractory myeloma supports feasibility in humans. The related prediction for **indolent (smoldering) plasma cell myeloma** (score 95.5%) is supported only indirectly, through trials matched to the broader disease term.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04508790](https://clinicaltrials.gov/study/NCT04508790) | Phase 2 | Recruiting | 29 | Leflunomide + pomalidomide + dexamethasone in relapsed/refractory myeloma; directly tests the repurposing hypothesis; no results yet |
| [NCT05014646](https://clinicaltrials.gov/study/NCT05014646) | Phase 2 | Active, not recruiting | 27 | Leflunomide in high-risk smoldering myeloma in African-American and European-American patients; no results yet |
| [NCT02509052](https://clinicaltrials.gov/study/NCT02509052) | Phase 1/2 | Completed | 12 | Dose-escalation of single-agent leflunomide in relapsed/refractory myeloma; corresponds to the published Phase 1 study (PMID 32268821) |
| [NCT04370483](https://clinicaltrials.gov/study/NCT04370483) | Early Phase 1 | Active, not recruiting | 1 | Pilot in high-risk smoldering myeloma; too small to be informative |
| [NCT03952832](https://clinicaltrials.gov/study/NCT03952832) | Phase 2 | Withdrawn | 0 | High-risk smoldering myeloma; no participants enrolled, so it provides no evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32268821](https://pubmed.ncbi.nlm.nih.gov/32268821/) | 2020 | Phase 1 trial | Leuk Lymphoma | Single-agent leflunomide in relapsed/refractory myeloma (≥3 prior therapies); no dose-limiting toxicities at 20 and 40 mg |
| [30940637](https://pubmed.ncbi.nlm.nih.gov/30940637/) | 2019 | Preclinical | Blood Adv | Teriflunomide lowers c-Myc via PIM kinase inhibition; leflunomide plus lenalidomide extended survival in a myeloma model |
| [19174558](https://pubmed.ncbi.nlm.nih.gov/19174558/) | 2009 | Preclinical | Mol Cancer Ther | DHODH is expressed in myeloma cells; A771726 induces apoptosis and reduces proliferation |
| [34577124](https://pubmed.ncbi.nlm.nih.gov/34577124/) | 2021 | Preclinical | Molecules | Teriflunomide is cytotoxic to RPMI-8226 myeloma cells through a mitochondria-independent mechanism |
| [40814067](https://pubmed.ncbi.nlm.nih.gov/40814067/) | 2025 | Preclinical | J Transl Med | MARCH5-MFN2 axis and mitochondrial fusion influence myeloma venetoclax sensitivity (mechanistic context) |
| [36996290](https://pubmed.ncbi.nlm.nih.gov/36996290/) | 2023 | Clinical (indirect) | J Immunol Sci | Two cancer patients with severe COVID-19 recovered on leflunomide; relevant only as human use in cancer patients |
| [16155443](https://pubmed.ncbi.nlm.nih.gov/16155443/) | 2005 | Review | Curr Opin Neurol | Toxic neuropathy overview (safety context) |

---

## Singapore Market Information

All four registrations are valid single-ingredient oral film-coated tablets. The registration records list no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15252P | Leflunomide Mevon Film-Coated Tablets 20 mg | Film-coated tablet | Pharmathen S.A. |
| SIN11400P | Arava Tablet 20 mg | Film-coated tablet | Opella Healthcare International SAS |
| SIN11401P | Arava Tablet 100 mg | Film-coated tablet | Opella Healthcare International SAS |
| SIN17108P | Bageda Film-Coated Tablet 20 mg | Film-coated tablet | World Medicine İlaç San. ve Tic. A.Ş. |

---

## Safety Considerations

Package-insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for authoritative safety information. The items below come from knowledge-graph and interaction databases, not label text.

- **Conditions flagged as contraindications in the knowledge graph:**
  - Liver: liver disease and liver failure, gallbladder disease, and chronic hepatitis B or C infection.
  - Kidney: kidney disease.
  - Blood: thrombocytopenia, neutropenia (including congenital forms), agranulocytosis, anaemia and pancytopenia.
  - Nervous system: peripheral neuropathy.
  - Lung: interstitial lung disease.
  - Infection: pneumocystosis and aspergillosis.
  - These are relevant to myeloma patients, who often have cytopenias, renal impairment and infection risk.
- **Teratogenicity:** Leflunomide is known to be teratogenic, so pregnancy must be excluded and contraception ensured in patients of childbearing potential.
- **Drug interactions:** 100 interactions were found. Those listed as **Major** include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, clarithromycin, minocycline, pioglitazone, acarbose, bupropion, naltrexone, oxandrolone, oxymetholone and chenodeoxycholic acid. **Moderate** interactions include metronidazole, chlorpropamide and acetohexamide.
- **Relevance to the proposed regimen:** Dexamethasone appears among the Major interactions, and it is part of the combination being tested in NCT04508790. This needs specific review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- A coherent DHODH-based mechanism, consistent preclinical data, and a completed Phase 1/2 study in relapsed/refractory myeloma support further investigation.
- No randomised efficacy data exist, and the active Phase 2 trials are small and unreported. The drug is already registered and marketed in Singapore for its original indications.

**To proceed, the following is needed:**
- Results from the ongoing Phase 2 trials (NCT04508790, NCT05014646) and the full Phase 1/2 dose and toxicity data from NCT02509052
- Package-insert warnings and contraindications, with a safety review covering hepatic, haematological, infection and pregnancy risks in myeloma patients
- A review of the interaction between leflunomide and dexamethasone-containing regimens
- A confirmed mechanism-of-action record for the drug
- A clear view of the preclinical counter-signal in leukaemia cells (PMID 16927021, low-dose leflunomide activating PI3K/Akt signalling), to check it does not apply to myeloma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

