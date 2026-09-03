---
layout: default
title: Prochlorperazine
parent: 僅模型預測 (L5)
nav_order: 819
evidence_level: L5
indication_count: 10
---

# Prochlorperazine
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

# Prochlorperazine: From Nausea/Vomiting and Psychotic Disorders to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

> Prochlorperazine is a phenothiazine-class dopamine D2 antagonist, internationally used as an antiemetic and antipsychotic; it is **not currently marketed in Singapore**.
> The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**,
> but with **0 clinical trials** and **no literature directly evaluating prochlorperazine for this indication** — the evidence base is currently limited to the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; internationally known for nausea/vomiting and psychotic disorders (general pharmacological classification, not from this evidence pack) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.9998% (rank 85 of candidates) |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (MOA marked as a data gap). Based on general drug knowledge, prochlorperazine is a phenothiazine derivative that blocks dopamine D2 receptors (and to a lesser extent histaminergic and muscarinic receptors), which underlies its established use in nausea/vomiting and psychotic disorders. This mechanism has no established or literature-documented link to retinal photoreceptor/pigment epithelium biology, which is the pathophysiological basis of inherited retinal dystrophies.

The retrieved literature for this candidate consists of general ophthalmology and clinical genetics reviews/case reports (orbital infections, congenital ptosis, cryptophthalmia, synkinesis, metabolic eye disease, etc.). None of the abstracts mention prochlorperazine, phenothiazines, or any pharmacological intervention for retinal dystrophy — they appear to have been retrieved through disease-term overlap ("extraocular," "congenital," "retinal") rather than genuine drug-disease evidence. This pattern is consistent with the broader candidate list: 7 of the top 10 TxGNN-ranked predictions for this drug are ultra-rare monogenic/developmental disorders (hydranencephaly, congenital disorder of glycosylation, X-linked myopia, Charcot-Marie-Tooth type 1G, polymicrogyria syndromes) with **zero** supporting trials or literature, and one of these (Charcot-Marie-Tooth 1G) has already been explicitly scored L5/Hold with the note "no known mechanistic link to phenothiazine pharmacology." This strongly suggests the high TxGNN score for retinal dystrophy reflects network-topology confidence rather than a biologically grounded repurposing signal.

By contrast, the rank-10 candidate (manic bipolar affective disorder) is mechanistically more plausible given prochlorperazine's dopamine-antagonist/antipsychotic activity and is supported by older psychiatric literature — but per the evidence pack's ranking, retinal dystrophy remains the top-ranked candidate and is the subject of this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

⚠️ **Note:** None of the publications below discuss prochlorperazine or drug therapy for retinal dystrophy. They are general ophthalmology/genetics reviews and case reports retrieved via disease-term matching; their relevance to this drug-disease pairing has not been confirmed (classification status: pending in source data).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review (unclassified) | Pediatric Radiology | Imaging review of pediatric ocular pathologies including congenital/developmental lesions; no drug therapy discussion |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review (unclassified) | Taiwan Journal of Ophthalmology | Overview of congenital lens shape anomalies; developmental biology focus, no pharmacotherapy |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Case study (unclassified) | Intl J Molecular Sciences | Optic nerve/retinal abnormalities in congenital fibrosis of extraocular muscles (genetic, KIF21A/TUBB3-related) |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review (unclassified) | Ther Adv Ophthalmology | Eye involvement in inherited metabolic disorders; no drug-specific evidence |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Review (unclassified) | Neuroradiology | Neuroradiological features of ophthalmoplegia; diagnostic imaging focus |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review (unclassified) | J Binocular Vision & Ocular Motility | Overview of congenital cranial dysinnervation disorders |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Case study (unclassified) | American Journal of Ophthalmology | Pathogenesis/treatment of maculopathy with cavitary optic disc anomalies (surgical, not pharmacologic) |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report (unclassified) | J Neuro-Ophthalmology | Single case of congenital trochlear-oculomotor synkinesis |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review (unclassified) | Klinische Monatsblätter für Augenheilkunde | Overview of congenital ptosis and levator muscle fibrosis |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review (unclassified) | Seminars in Neurology | Clinical approach to diplopia; general diagnostic guidance |

---

## Singapore Market Information

Prochlorperazine currently has **no marketing authorization in Singapore** (market status: Not Marketed, 0 registrations). No product-level information (dosage form, indication text) is available for this drug in the local regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in the current evidence pack; a DDI query returned no results. Note this is flagged as a **Blocking** data gap in the evidence pack (missing HSA/TFDA label warnings and contraindications), meaning safety screening cannot be completed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no clinical trial support, and the associated literature does not directly address prochlorperazine's use in retinal dystrophy — evidence quality corresponds to L5 (model prediction only). Combined with the drug's absence from the Singapore market and unresolved blocking safety data gaps, there is currently insufficient basis to advance this candidate beyond a research-flag stage.

**To proceed, the following is needed:**
- Retrieve HSA/TFDA label warnings and contraindications (Blocking gap, DG001) via official regulatory source
- Obtain confirmed mechanism-of-action data via DrugBank API (High-priority gap, DG002) to properly assess mechanistic plausibility
- Manual full-text review of the 10 retrieved publications to confirm (or rule out) any genuine connection to prochlorperazine
- Preclinical/mechanistic evidence linking dopamine-receptor pharmacology to retinal dystrophy pathophysiology, if this candidate is to be pursued further
- If pursuing repurposing signals for this drug more broadly, consider prioritizing the mechanistically plausible rank-10 candidate (manic bipolar affective disorder) over the top-ranked but mechanistically unsupported rare genetic disease predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

