---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Paroxysmal Nocturnal Hemoglobinuria to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab is a humanized monoclonal antibody that inhibits complement protein C5, currently approved globally for paroxysmal nocturnal hemoglobinuria (PNH), atypical hemolytic uremic syndrome (aHUS), and generalized myasthenia gravis (gMG).
The TxGNN model predicts it may be effective for **Cyclic Hematopoiesis** (also known as cyclic neutropenia),
however **0 clinical trials** and **0 directly relevant publications** currently support this indication — the evidence base is model-prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Paroxysmal nocturnal hemoglobinuria (PNH), atypical hemolytic uremic syndrome (aHUS), generalized myasthenia gravis (gMG) — established globally; **not registered in Singapore** |
| Predicted New Indication | Cyclic Hematopoiesis (cyclic neutropenia) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed (0 registrations) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eculizumab is a humanized IgG2/4κ monoclonal antibody that binds selectively to complement C5, blocking its cleavage into the pro-inflammatory C5a and the membrane attack complex (MAC) initiator C5b. By halting the terminal complement cascade, eculizumab prevents complement-mediated cell lysis and inflammatory signalling. This mechanism underpins its efficacy in PNH (where GPI-anchor deficiency leaves red cells unprotected from complement attack), aHUS (driven by dysregulation of the alternative complement pathway), and gMG (where complement-mediated destruction of the neuromuscular junction is AChR-antibody-dependent).

Cyclic hematopoiesis is caused by autosomal dominant mutations in the **ELANE** gene, which encodes neutrophil elastase. These mutations trigger endoplasmic reticulum stress and unfolded protein response (UPR) in myeloid precursors, producing an oscillatory pattern of granulopoiesis with a cycle of approximately 21 days. The pathophysiology is intrinsic to the bone marrow and driven by a cell-autonomous granulocyte maturation defect — not by complement-mediated destruction of circulating cells.

The TxGNN graph model may have identified a topological connection between eculizumab's drug node and the cyclic hematopoiesis disease node through shared immune pathway neighbours (e.g., C5a receptor signalling influences neutrophil recruitment and could theoretically modulate inflammatory oscillations). However, no mechanistic studies, animal models, or clinical reports support the hypothesis that C5 inhibition corrects the ELANE-driven oscillatory cycle. The biological plausibility is speculative at best. The prediction should be treated as a hypothesis-generating signal requiring dedicated experimental validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Eculizumab in cyclic hematopoiesis.

---

## Literature Evidence

Currently no related literature directly addressing Eculizumab in cyclic hematopoiesis is available.

---

## Singapore Market Information

Eculizumab (Soliris®) is **not registered** with the Health Sciences Authority (HSA) of Singapore. There are no active product licences on record as of the data cutoff (2026-06-16).

---

## Safety Considerations

Detailed warning and contraindication data from local regulatory submissions is not available for this report. Based on the established global safety profile of eculizumab, clinicians should be aware of the following key concerns from international labelling:

- **Black Box Warning**: Eculizumab increases susceptibility to serious, life-threatening, and fatal meningococcal infections (*Neisseria meningitidis*). All patients must be vaccinated against meningococcal disease at least 2 weeks before initiating treatment. Patients who cannot be vaccinated require antibiotic prophylaxis.
- **Serious Infections**: Risk of serious infections caused by encapsulated bacteria (*Streptococcus pneumoniae*, *Haemophilus influenzae*) is elevated.
- **Infusion Reactions**: Serious hypersensitivity reactions, including anaphylaxis, have been reported.

Please refer to the current approved package insert (e.g., EMA/FDA labelling) for complete warnings, contraindications, and monitoring requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high algorithmic score (99.97%) to cyclic hematopoiesis, but this prediction is entirely unsupported by clinical trials, mechanistic studies, or disease-specific literature. The known mechanism of eculizumab (terminal complement inhibition) does not intersect with the established pathophysiology of cyclic hematopoiesis (ELANE-mutation-driven UPR and myeloid precursor apoptosis). Furthermore, eculizumab is not registered in Singapore, and local safety data is unavailable.

**To proceed beyond Hold, the following would be needed:**

- **Mechanistic evidence**: Preclinical studies (cell line or animal models of cyclic neutropenia) demonstrating a role for C5a or the terminal complement cascade in driving neutrophil cycle oscillations.
- **MOA clarification**: Retrieval of full DrugBank pharmacology data and Singapore HSA / global regulatory labelling to complete the safety profile.
- **Regulatory pathway assessment**: Confirmation of the feasibility of an investigational use or Named Patient Programme application given the absence of any Singapore registration.
- **Expert consultation**: Input from a haematologist specialising in congenital bone marrow failure syndromes to independently assess biological plausibility before any resource commitment.
- **Alternative approaches**: G-CSF remains the standard of care for cyclic neutropenia; any repurposing investigation would need to demonstrate a clear unmet need or superiority rationale over existing therapy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

