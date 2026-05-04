---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Azithromycin is a broad-spectrum macrolide antibiotic widely used for respiratory tract infections, sexually transmitted diseases, and atypical pneumonias, with additional well-documented immunomodulatory properties. The TxGNN model predicts it may be relevant for **Hyperamylasemia** with a score of **99.81%**, however **no clinical trials** and **no supporting literature** were identified for this specific indication. Critically, mechanistic analysis reveals this prediction is a likely **false positive** — Azithromycin is a known causative agent of drug-induced pancreatitis, which itself elevates serum amylase levels.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, atypical pathogens, sexually transmitted infections) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Azithromycin is a macrolide antibiotic (azalide subclass) that exerts antibacterial effect by binding to the 50S ribosomal subunit and blocking peptide translocation. Beyond its antimicrobial activity, it possesses significant immunomodulatory properties — suppressing pro-inflammatory cytokines (IL-6, TNF-α, IL-8) and modulating neutrophil recruitment — which have driven interest in non-infectious indications such as chronic airway disease and autoimmune processes.

Hyperamylasemia refers to elevated serum amylase, most commonly associated with acute pancreatitis, salivary gland pathology, or metabolic disorders. There is no established pathway by which Azithromycin would therapeutically **reduce** serum amylase. In contrast, **Azithromycin is a documented cause of drug-induced pancreatitis** — a well-recognised adverse drug reaction in which pancreatic inflammation drives the very elevation of amylase that defines this predicted indication.

The high TxGNN score (99.81%) most likely reflects **knowledge graph co-occurrence noise**: Azithromycin and hyperamylasemia co-appear frequently in pharmacovigilance literature precisely because the drug causes elevated amylase, not because it treats it. Graph-based prediction models cannot inherently distinguish causative from therapeutic drug–disease associations. This prediction should be treated as a model artefact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Azithromycin currently has no registered products in Singapore. No HSA authorisation records were retrieved.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No registered products found |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Relevant to this prediction:** Azithromycin is a known cause of drug-induced pancreatitis (hyperamylasemia/hyperlipasaemia) and QTc interval prolongation. These adverse effects are directly pertinent to the predicted indication reviewed in this report, further supporting the false-positive assessment.

---

## All Predicted Indications — Portfolio Overview

This is a multi-indication evidence pack (TW-DB00207-multi). The table below summarises all 10 TxGNN predictions for Azithromycin:

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Mechanistic Assessment |
|------|---------|-------------|----------------|----------|------------------------|
| 1 | Hyperamylasemia | 99.81% | L5 | **Hold** | False positive — drug causes elevated amylase (pancreatitis ADR) |
| 2 | Polyclonal Hyperviscosity Syndrome | 99.81% | L5 | **Hold** | Immunoglobulin overproduction not modulated by macrolide antibiotics |
| 3 | Congenital Analbuminemia | 99.79% | L5 | **Hold** | Genetic (ALB gene mutation); antibiotics have no role in albumin synthesis |
| 4 | Punctate Epithelial Keratoconjunctivitis | 99.78% | L4 | **Research Question** | Microsporidia-related aetiology; in vitro anti-microsporidial activity reported; 1 case report ([PMID 32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/)) |
| 5 | Blood Group Incompatibility | 99.70% | L5 | **Hold** | ABO/Rh alloimmune complement activation; no drug mechanism applicable |
| 6 | Premalignant Hematological System Disease | 99.64% | L5 | **Hold** | Clonal haematopoiesis (MDS/MGUS); macrolides have no direct clone-suppressing evidence |
| 7 | Monoclonal Gammopathy | 99.61% | L4 | **Research Question** | Preclinical: Azithromycin blocks autophagy flux, sensitises myeloma cells to bortezomib ([PMID 23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/)) |
| 8 | Haematological Disease with Acquired Peripheral Neuropathy | 99.56% | L5 | **Hold** | Paraprotein-mediated myelin damage; no intervention pathway; QTc risk adds concern |
| 9 | Septicemic Plague | 99.52% | L4 | **Research Question** | In vitro MIC data vs *Y. pestis* ([PMID 8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/)); intracellular concentration advantage (tissue:plasma 10–100×) |
| 10 | Congenital Hematological Disorder | 99.40% | L4 | **Research Question** | Sickle Cell Disease / ACS: 2 withdrawn Phase 1/2 trials (NCT02630394, NCT02960503); immunomodulatory rationale well-supported |

### Indications with the Strongest Research Rationale

**Rank 10 — Congenital Hematological Disorder (Sickle Cell Disease)**
This is the most actionable prediction in the portfolio. Two formally registered clinical trials — NCT02630394 (Phase 1, Azithromycin prophylaxis for ACS in SCD) and NCT02960503 (Phase 1/2, macrolide therapy to improve FEV1 in SCD adults) — were specifically designed to test Azithromycin's anti-inflammatory effect on pulmonary complications of SCD. Both were withdrawn before enrolment, indicating research intent without execution data. The scientific hypothesis parallels established evidence from cystic fibrosis, where macrolide therapy demonstrably reduces exacerbations.

**Rank 7 — Monoclonal Gammopathy / Multiple Myeloma**
A 2013 in vitro study (PMID 23546223) found that Azithromycin blocks autophagy flux via LC3B-II and p62 accumulation, sensitising MM cell lines (U266, IM-9, RPMI8226) to bortezomib-induced ER stress and apoptosis. This positions Azithromycin as a potential combination sensitiser — not a monotherapy — in MM. Independent replication and an in vivo model are prerequisite before clinical translation.

**Rank 9 — Septicemic Plague (Alternative Therapy Niche)**
In vitro susceptibility data against *Yersinia pestis* exists (PMID 8540736, MIC values documented), and Azithromycin's pronounced intracellular tissue accumulation is mechanistically favourable for killing phagocytosed bacteria. Relevance is limited to scenarios where first-line agents (streptomycin, gentamicin, doxycycline) are unavailable or contraindicated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hyperamylasemia) is a false positive driven by pharmacovigilance co-occurrence noise in the TxGNN knowledge graph. The large majority of predictions (ranks 1–3, 5–6, 8) carry Hold recommendations with no supporting evidence and, in several cases, adverse mechanistic relationships. Azithromycin's genuine repurposing potential in this evidence pack lies in ranks 7, 9, and especially 10.

**To proceed, the following is needed:**

- **Reprioritise review** to Rank 10 (Sickle Cell Disease / ACS), which has the strongest scientific rationale and existing clinical trial precedent — investigate the reason for trial withdrawal (NCT02630394, NCT02960503) and assess feasibility of a new protocol
- **Obtain MOA data** from DrugBank API (data gap DG002) to enable full mechanistic linkage analysis across all 10 indications
- **Retrieve package insert safety data** from TFDA/HSA (data gap DG001) — QTc prolongation risk is critical for patient safety assessment in all cardiac-adjacent and haematological indications
- **For Rank 7 (Monoclonal Gammopathy):** Commission or identify a follow-up study replicating PMID 23546223 findings, with focus on Azithromycin + bortezomib synergy in a clinical-grade MM model
- **Singapore registration pathway:** Azithromycin currently has 0 HSA registrations in Singapore; regulatory filing would be required before any clinical use under any new indication

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

