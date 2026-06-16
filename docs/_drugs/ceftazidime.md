---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Ceftazidime
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

# Ceftazidime: From Gram-negative Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Ceftazidime is a broad-spectrum third-generation cephalosporin antibiotic with potent activity against Gram-negative pathogens — including *Pseudomonas aeruginosa* — established for the treatment of serious bacterial infections.
The TxGNN model predicts a potential role in managing **Hyperamylasemia**, supported by **0 clinical trials** and **1 publication** examining antibiotic prophylaxis as a means to attenuate ERCP-associated pancreatic injury.
The mechanistic link is indirect and the available evidence insufficient for active repurposing development at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Serious Gram-negative bacterial infections (no Singapore registration on record) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory dataset. Based on known pharmacological information, Ceftazidime is a third-generation cephalosporin β-lactam antibiotic with particularly strong anti-*Pseudomonas* activity. Its antibacterial efficacy against serious Gram-negative infections is well-established in clinical practice; it exerts its effect by binding to penicillin-binding proteins (PBPs) and inhibiting bacterial cell wall peptidoglycan synthesis, ultimately leading to bacterial lysis, and mechanistically may be applicable to infection-associated inflammatory conditions where bacterial burden drives tissue injury.

Hyperamylasemia — elevation of serum amylase — most commonly arises as a secondary phenomenon following pancreatic insult, including post-ERCP pancreatitis. The sole supporting publication (PMID 11985972) investigates whether routine antibiotic prophylaxis reduces the incidence of ERCP-associated pancreatitis, based on the hypothesis that bacterial translocation during the procedure may trigger pancreatic inflammation. If this mechanism is valid, antibiotics capable of suppressing bacterial translocation could indirectly attenuate procedure-associated hyperamylasemia.

It is critical to recognise, however, that this represents a derived, secondary effect — Ceftazidime has no direct pharmacological action on amylase synthesis or secretion pathways. Hyperamylasemia is a laboratory marker arising from numerous causes (trauma, ductal obstruction, systemic inflammation), not a disease entity with a primary bacteriological aetiology. The TxGNN prediction most likely reflects a correlative association captured in the knowledge graph rather than a therapeutically actionable relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11985972](https://pubmed.ncbi.nlm.nih.gov/11985972/) | 2001 | Clinical / Prophylaxis trial | Journal of Gastrointestinal Surgery | Prospective study evaluating whether routine antibiotic prophylaxis during ERCP reduces post-procedure pancreatitis and cholangitis; explores the hypothesis that bacterial translocation drives ERCP-associated pancreatic injury — does not specifically assess Ceftazidime's effect on serum amylase levels |

---

## Singapore Market Information

Ceftazidime currently has **no product authorizations** in Singapore. No registration records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Ceftazidime and hyperamylasemia is entirely indirect — resting on the unproven premise that antibiotic prophylaxis during ERCP attenuates pancreatic inflammation and secondarily lowers serum amylase. With only one non-specific prophylaxis trial and no clinical trials targeting hyperamylasemia directly, this TxGNN prediction does not meet the threshold for active drug repurposing investigation. The absence of Singapore market registration is an additional regulatory barrier.

**To proceed, the following is needed:**
- Direct clinical evidence (observational studies or RCTs) specifically demonstrating that Ceftazidime reduces serum amylase levels as a primary or secondary endpoint
- A plausible direct mechanistic pathway beyond the indirect ERCP prophylaxis hypothesis
- Mechanism of action (MOA) data from DrugBank to support or refute the biological plausibility
- Full safety review including package insert warnings, contraindications, and drug interaction profile (currently unavailable)
- Singapore regulatory registration as a prerequisite for any clinical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

