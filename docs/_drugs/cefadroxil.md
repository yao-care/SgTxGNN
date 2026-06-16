---
layout: default
title: Cefadroxil
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Cefadroxil
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

# Cefadroxil: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Cefadroxil is a first-generation cephalosporin antibiotic, used clinically to treat common bacterial infections including urinary tract infections, skin and soft tissue infections, and pharyngitis/tonsillitis.
The TxGNN model ranks **Polyclonal Hyperviscosity Syndrome** as the top predicted new indication with a score of **98.60%**, however this prediction is currently supported by **0 clinical trials** and **0 publications**.
Mechanistic analysis indicates this is highly likely a graph topology false signal rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (urinary tract, skin/soft tissue, pharyngitis/tonsillitis) — first-generation cephalosporin |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacology, Cefadroxil belongs to the first-generation cephalosporin class of β-lactam antibiotics. Its mechanism involves inhibiting bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), which disrupts peptidoglycan cross-linking and ultimately causes bacterial cell lysis. It is effective primarily against gram-positive organisms and some gram-negative bacteria that possess cell walls.

Polyclonal hyperviscosity syndrome is caused by abnormal overproduction of multiple immunoglobulin classes (as opposed to the monoclonal form seen in Waldenström's macroglobulinaemia). The resulting increased plasma viscosity leads to circulatory compromise. Standard treatment centres on plasmapheresis and management of the underlying condition driving immunoglobulin overproduction — not antimicrobial therapy.

The mechanistic disconnect is substantial: Cefadroxil has no anti-immunoglobulin activity, no plasma viscosity-lowering properties, and no immunomodulatory effects. The most plausible explanation for this TxGNN prediction is an **indirect graph topology pathway** — the knowledge graph likely contains edges linking "bacterial infection" → "immune activation" → "hypergammaglobulinaemia" → "hyperviscosity," and the model traversed this indirect route without pharmacological grounding. This prediction should be treated as a false positive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cefadroxil in Polyclonal Hyperviscosity Syndrome.

---

## Literature Evidence

Currently no related literature available for Cefadroxil in Polyclonal Hyperviscosity Syndrome.

---

## Singapore Market Information

Cefadroxil is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product authorisations are on record.

> **Note for procurement/access planning:** If clinical use were ever considered, a Special Access Route (SAR) application to HSA would be required prior to importation or supply.

---

## Safety Considerations

Safety-specific data (package insert warnings, contraindications, and drug-drug interactions) were not retrievable through the automated evidence pipeline for this evaluation.

Please refer to the package insert for safety information.

> **General class considerations** (from established pharmacology, not retrieved data): As a β-lactam antibiotic, Cefadroxil carries a known risk of hypersensitivity reactions including anaphylaxis, particularly in patients with penicillin allergy (cross-reactivity rate ~1–2%). It is renally excreted and dose adjustment is required in renal impairment. Clostridium difficile-associated diarrhoea has been reported across all antibiotic classes. These points require formal verification against the approved product information before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numerical score (98.60%) to this prediction, but score magnitude alone does not indicate mechanistic plausibility — it reflects structural proximity in the knowledge graph. Cefadroxil is a cell-wall–active antibiotic with no pharmacological activity relevant to immunoglobulin overproduction or plasma viscosity. The prediction is best classified as a graph topology artefact. Furthermore, Cefadroxil is not registered in Singapore, and all 10 top-ranked predicted indications in this evidence pack are rated L5 with a uniform "Hold" recommendation.

**To proceed, the following would be needed:**

- Formal mechanism of action documentation confirming whether any pleiotropic effects (e.g., immunomodulatory, anti-inflammatory) exist beyond cell-wall synthesis inhibition
- Singapore HSA registration or an established Special Access Route before any clinical use
- TFDA package insert retrieval to complete the safety profile (Blocking data gap — DG001)
- Reconsideration of the TxGNN knowledge graph edge paths linking Cefadroxil to haematological/viscosity-related nodes, to determine whether graph pruning or edge-weight recalibration would suppress these false-positive signals
- If exploratory interest in any infectious indication is retained (e.g., gonococcal urethritis at rank 9, L4), a targeted resistance surveillance review against current Singapore *N. gonorrhoeae* susceptibility data would be the minimum starting point — though even there, WHO/CDC guidelines favour injectable ceftriaxone and the clinical bar for first-generation oral cephalosporins is very high
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

