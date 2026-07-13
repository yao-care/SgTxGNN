---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: From ALK-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

Lorlatinib (Lorbrena) is a brain-penetrant, third-generation inhibitor of ALK and ROS1 tyrosine kinases, globally approved for the treatment of ALK-positive metastatic non-small cell lung cancer (NSCLC). The TxGNN model ranks **Gingival Fibromatosis** as its highest-scoring new indication candidate (99.81%), yet this prediction is supported by **0 clinical trials** and **0 publications** and lacks biological plausibility due to the absence of any known ALK/ROS1 pathway involvement in this disease. The recommended decision is **Hold**; however, TxGNN's rank-5 node maps to genuine Phase 3 RCT evidence for ALK-positive NSCLC (lorlatinib's established indication), and a separate pediatric neuroblastoma repurposing signal (rank 6) represents the most actionable novel finding in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive metastatic non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Gingival Fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lorlatinib's mechanism of action is not formally documented in this Evidence Pack (data gap DG002), but the body of literature collected during evidence retrieval makes its pharmacology unambiguous. Lorlatinib is a macrocyclic, highly potent, brain-penetrant, third-generation inhibitor of ALK (anaplastic lymphoma kinase) and ROS1 receptor tyrosine kinases. It was rationally designed to overcome the resistance mutations — most notably the G1202R solvent-front mutation — that emerge after treatment with first-generation (crizotinib) and second-generation ALK inhibitors (alectinib, brigatinib, ceritinib). Its superior CNS penetration enables intracranial activity that earlier agents cannot match, and its broad coverage of compound resistance mutations makes it the current first-line standard of care for ALK-positive NSCLC.

Gingival fibromatosis is a rare condition characterised by slow, progressive fibrous overgrowth of the gingival tissue. The molecular pathogenesis is driven by gain-of-function mutations in **SOS1** (a Ras guanine nucleotide exchange factor), **CTNNB1** (β-catenin), or **REST** — genes involved in fibroblast proliferation and connective tissue homeostasis. None of these pathways converge on ALK or ROS1 kinase signalling. Lorlatinib has no known inhibitory activity on SOS1, Wnt/β-catenin, or REST-regulated transcriptional networks. There is no preclinical model, published hypothesis, or mechanism study suggesting that ALK/ROS1 inhibition would suppress gingival fibroblast proliferation.

This TxGNN prediction is most likely a **knowledge graph false positive** arising from phenotypic clustering. In the TxGNN disease ontology (UMLS/MONDO), gingival fibromatosis may be co-located with other fibrotic or proliferative tissue conditions that share graph-level proximity with cancer-related nodes. Because lorlatinib has rich associations with lung neoplasm nodes in the graph, that signal may propagate through ontological edges to nearby "proliferative" disease nodes regardless of mechanistic relevance. Without a biological link between ALK/ROS1 inhibition and fibroblastic gingival dysregulation, this prediction does not warrant further investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for lorlatinib in gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for lorlatinib in gingival fibromatosis.

---

## Singapore Market Information

Lorlatinib has no registered products with Singapore's Health Sciences Authority (HSA) and is not commercially available in Singapore. There are no authorization records on file.

---

## Cytotoxicity

Lorlatinib is an antineoplastic agent (targeted therapy: ALK/ROS1 tyrosine kinase inhibitor). Its primary indication — ALK-positive metastatic NSCLC — and its pharmacological class confirm inclusion in this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — third-generation ALK/ROS1 tyrosine kinase inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low — not associated with clinically significant bone marrow suppression in Phase 3 trials |
| Emetogenicity Classification | Low |
| Monitoring Items | Fasting lipid panel (cholesterol, triglycerides — class-specific metabolic effect), body weight, CNS/neuropsychiatric status (cognitive function, mood, speech), blood pressure, liver function, renal function |
| Handling Protection | Oral tablet (100 mg once daily); institutional antineoplastic handling precautions apply per local cytotoxic drug handling policy |

---

## Safety Considerations

Please refer to the package insert for complete safety information. Formal warning and contraindication data were not available for this Evidence Pack (data gap DG001).

Published clinical data provide the following key safety signals from Phase 3 and Phase 1/2 lorlatinib trials:

- **Metabolic effects** (most distinctive from other ALK TKIs): hypercholesterolaemia and hypertriglyceridaemia are very common and frequently require lipid-lowering therapy; weight gain is also reported. A real-world pharmacovigilance analysis ([PMID 40287137](https://pubmed.ncbi.nlm.nih.gov/40287137/)) using FAERS data (2013–2024) confirms metabolic adverse events as the dominant safety signal.
- **CNS adverse events**: cognitive changes (memory, concentration), mood disorders (depression, anxiety), speech effects, and peripheral neuropathy occur with higher frequency than other ALK inhibitors, consistent with lorlatinib's superior CNS penetration.
- **Oedema**: peripheral and facial oedema reported across clinical programmes.
- **Pulmonary toxicity**: rare but serious — acute respiratory distress syndrome reported ([PMID 31985497](https://pubmed.ncbi.nlm.nih.gov/31985497/)); pulmonary toxicity also observed in combination with anti-GD2 therapy in neuroblastoma patients ([PMID 40551396](https://pubmed.ncbi.nlm.nih.gov/40551396/)).
- **Nephrotic syndrome / hyperlipidaemia mechanism**: case reports suggest minimal change disease as a secondary cause of lorlatinib-induced hyperlipidaemia ([PMID 33789526](https://pubmed.ncbi.nlm.nih.gov/33789526/), [PMID 39537504](https://pubmed.ncbi.nlm.nih.gov/39537504/)).

A pragmatic adverse event management guide is available ([PMID 38554546](https://pubmed.ncbi.nlm.nih.gov/38554546/), *Lung Cancer*, 2024).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN rank-1 prediction for lorlatinib — gingival fibromatosis — has no biological mechanism linking ALK/ROS1 inhibition to this fibroblastic gingival condition, is unsupported by any clinical trial or published literature, and is assessed as a knowledge graph false positive.

---

**Full Predicted Indication Landscape Summary:**

| Rank | Disease | Score | Evidence Level | Decision | Key Note |
|------|---------|-------|----------------|----------|----------|
| 1 | Gingival Fibromatosis | 99.81% | L5 | Hold | No ALK/ROS1 pathway; false positive |
| 2 | Fibroma of Lung | 99.75% | L5 | Hold | No mechanistic link; ALK+ IMT is a distinct entity |
| 3 | Hamartoma of Lung | 99.75% | L5 | Hold | Developmental benign lesion; false positive |
| 4 | Lung Hilum Carcinoma | 99.74% | L4 | Research Question | 1 case report: neoadjuvant lorlatinib → pCR in ALK+ central NSCLC ([PMID 37934724](https://pubmed.ncbi.nlm.nih.gov/37934724/)) |
| **5** | **Lung Benign Neoplasm** | **99.74%** | **L1** | **Proceed with Guardrails** | **TxGNN node maps ALK+ NSCLC literature — CROWN Phase 3 RCT; this is lorlatinib's approved indication** |
| **6** | **Lung Germ Cell Tumor** | **99.73%** | **L3** | **Research Question** | **Ontology maps to ALK-driven neuroblastoma; Phase 1 pediatric trial ([PMID 37012551](https://pubmed.ncbi.nlm.nih.gov/37012551/)) — genuine repurposing signal** |
| 7 | Pulmonary Sulcus Neoplasm | 99.73% | L5 | Hold | Pancoast NSCLC subtype; indirect ALK link, no dedicated evidence |
| 8 | IBMPFD | 99.72% | L5 | Hold | VCP mutation disease; no ALK/ROS1 pathway intersection |
| 9 | Junctional Epidermolysis Bullosa | 99.72% | L5 | Hold | Structural basement membrane disease; no kinase target |
| 10 | Leukomelanoderma Syndrome | 99.69% | L5 | Hold | Literature maps only lorlatinib safety/metabolic data; no efficacy rationale |

---

**Most Actionable Finding in This Evidence Pack:**

The **rank-6 node** ("lung germ cell tumor") represents the most genuinely novel repurposing signal. Its associated literature maps to **ALK-driven neuroblastoma**, where a pediatric Phase 1 trial ([PMID 37012551](https://pubmed.ncbi.nlm.nih.gov/37012551/), *Nature Medicine* 2023) demonstrates safety and preliminary efficacy of lorlatinib in children with refractory/relapsed ALK-mutant neuroblastoma. ALK activating mutations (F1174L, R1275Q) are present in ~8–10% of neuroblastomas and are generally resistant to crizotinib, creating a biological rationale for lorlatinib's stronger ALK-inhibitory profile. This extends beyond lorlatinib's approved NSCLC indication and represents a true repurposing opportunity in a paediatric oncology setting.

---

**To proceed further, the following is needed:**

- **Biological mechanism data**: Confirm ALK/SOS1/ROS1 pathway expression in gingival fibromatosis tissue (currently absent; likely will not be found)
- **Ontology audit**: Review TxGNN UMLS/MONDO node assignments to distinguish true repurposing predictions from disease-ontology proximity artifacts
- **MOA documentation**: Query DrugBank API for lorlatinib's full target profile (data gap DG002)
- **Neuroblastoma repurposing pathway**: Monitor Phase 1 trial NCT03107988 outcomes; evaluate Phase 2 feasibility for ALK-aberrant paediatric solid tumours
- **Singapore regulatory pathway**: Assess HSA requirements for lorlatinib approval; note that lorlatinib (Lorbrena) holds FDA, EMA, and PMDA approvals for ALK+ NSCLC — the Singapore pathway may reference these existing approvals
- **Package insert review**: Obtain and parse HSA/FDA package insert for full warning and contraindication data (data gap DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

