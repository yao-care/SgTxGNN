---
layout: default
title: Cariprazine
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Cariprazine
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

# Cariprazine: From Schizophrenia & Bipolar Disorder to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Cariprazine (marketed as Vraylar in the US and Reagila in the EU) is an atypical antipsychotic approved internationally for schizophrenia and bipolar disorder (manic, mixed, and depressive episodes), but is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**, with a prediction score of **98.70%**.
Currently, there are **no registered clinical trials** for this pairing, and the 15 retrieved publications are general ophthalmological papers — none of which directly study Cariprazine in the context of retinal dystrophy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Bipolar disorder (manic/mixed/depressive episodes) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 98.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from the local regulatory dossier is not available for this analysis. Based on published pharmacology, Cariprazine is a dopamine D3/D2 receptor partial agonist with preferential affinity for the D3 receptor, and additionally acts as a partial agonist at 5-HT1A receptors. Its proven clinical utility lies in modulating dopaminergic and serotonergic neurotransmission in psychiatric conditions.

There is a theoretical connection worth noting: dopamine does play a modulatory role in the retina. Retinal ganglion cells and photoreceptors express D2 and D3 receptors, and dopaminergic signalling influences light adaptation, retinal circuitry, and — in animal models — the pace of eye-axial elongation. This topological proximity in the TxGNN knowledge graph likely explains the high prediction score.

However, the connection does not translate to a plausible therapeutic mechanism for hereditary retinal dystrophy. These conditions are caused by mutations in photoreceptor-specific genes (e.g., *RPGR*, *PROM1*, *CEP290*), and their pathology is irreversible structural degeneration driven by gene-dosage loss-of-function effects. Modulating D3/D2 receptor activity addresses none of these upstream genetic causes. The high TxGNN score most likely reflects Cariprazine's broad neighbourhood within the "neurological disease" supercluster in the knowledge graph, rather than a direct biological relationship with photoreceptor dystrophy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 15 publications retrieved were identified by keyword matching on "extraocular anomalies" and are predominantly general ophthalmological reviews and case reports. **None directly investigate Cariprazine in the context of retinal dystrophy.** They are listed here for completeness and transparency.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Five-stage classification of orbital cellulitis secondary to sinusitis; extraocular motility limitation as a clinical sign |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Systematic evaluation of diplopia; differential diagnosis across ocular, neurological, and extraocular muscle disorders |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monatsbl Augenheilkd | Congenital ptosis: levator muscle fibrosis causing restricted upgaze, associated with refractive errors and binocular vision disturbance |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital lens shape anomalies; association with anterior segment dysgenesis beginning from 22nd day of gestation |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | Unilateral cryptophthalmia: absent extraocular muscles and optic nerve, deformed bony orbit, systemic anomalies in two patients |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuroophthalmol | Rare congenital trochlear-oculomotor synkinesis — a congenital cranial dysinnervation disorder (CCDD) subtype |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome: vitreoretinal degeneration with myopia, optically empty vitreous, and retinal detachment |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Differential diagnosis of paediatric ocular lesions including retinopathy of prematurity, Coats disease, coloboma, and congenital developmental anomalies |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Ther Adv Ophthalmol | Eye involvement in inherited metabolic disorders: retinal, corneal, lens dislocation, and extraocular muscle manifestations across multiple disorders |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Research Article | Int J Mol Sci | Optic nerve and retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM) arising from KIF21A/TUBB3 mutations |

---

## Singapore Market Information

Cariprazine has no current regulatory registrations in Singapore. No authorisation numbers, product names, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Cariprazine are rare congenital or genetic disorders — retinal dystrophy, structural brain malformations (hydranencephaly, polymicrogyria), chromosomal syndromes, and inherited neuropathies — for none of which is there any clinical trial evidence or direct Cariprazine literature. The mechanistic link between D3/D2 partial agonism and photoreceptor gene-mutation-driven degeneration is not established, and the drug is not registered in Singapore. This is a model-prediction-only scenario (L5) with an S0 decision stage (blocked at initial triage).

**To proceed, the following is needed:**
- Register Cariprazine in Singapore or confirm a regulatory pathway before any local development activity
- Obtain TFDA/regulatory package insert to extract key warnings and contraindications (DG001 — currently blocking safety screening at S0)
- Retrieve full MOA data from DrugBank to enable mechanistic analysis (DG002)
- Conduct a targeted literature search combining "Cariprazine" with "retinal dystrophy", "photoreceptor degeneration", or "retinitis pigmentosa" — the 15 retrieved papers address keyword co-occurrence only, not the drug-disease pairing
- Before advancing further, assess whether any preclinical evidence (animal or cell-based models of photoreceptor degeneration) exists for D3 agonism; absent such data, this candidate does not warrant clinical development priority
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

