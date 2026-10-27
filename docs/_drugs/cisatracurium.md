---
layout: default
title: Cisatracurium
parent: Low Evidence (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cisatracurium: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the Singapore registration data compiled for this repor…"
monitor_inn: "Cisatracurium"
predicted_indications: ["cauda equina syndrome", "preeclampsia", "obsolete neurogenic bladder (disease)", "migraine disorder", "thrombotic disease", "irritable bowel syndrome", "migraine with brainstem aura", "mild pre-eclampsia", "severe pre-eclampsia", "neurocirculatory asthenia"]
---

# Cisatracurium
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

## Cisatracurium: From Neuromuscular Blockade in Anaesthesia to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Cisatracurium is a non-depolarising neuromuscular blocker, marketed in Singapore as an injectable (Nimbex), and used as a muscle relaxant during anaesthesia.
The TxGNN model predicts it may be effective for **cauda equina syndrome** with a very high score, but **no clinical trials and no publications** support this prediction.
The prediction rests on knowledge-graph proximity only and has no plausible mechanistic basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration data compiled for this report (the drug is known as a neuromuscular blocker used in anaesthesia) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, cisatracurium is a non-depolarising neuromuscular blocker. It antagonises nicotinic acetylcholine receptors at the neuromuscular junction, producing skeletal muscle relaxation during surgery and mechanical ventilation.

Cauda equina syndrome is a compressive neurological emergency that requires surgical decompression. No plausible mechanistic link between neuromuscular blockade and treating this condition is evident. The high TxGNN score is a graph-based prediction only, so this prediction should be regarded as **weak and unsupported**.

Other top-ranked predictions are similarly unsupported:

- **Preeclampsia (mild and severe forms):** Neuromuscular blockade does not address placental or endothelial pathology. The two publications retrieved concern anaesthesia for caesarean section, where cisatracurium is at most an incidental adjunct.
- **Thrombotic disease:** The single retrieved paper describes anaesthetic care in paediatric liver transplantation. Thrombosis is peri-operative context, not a therapeutic target.
- **Migraine disorder and migraine with brainstem aura:** Botulinum toxin works at the same junction but acts presynaptically, so the analogy is weak.
- **Obsolete neurogenic bladder, irritable bowel syndrome and neurocirculatory asthenia:** No credible mechanism, and no clinical data. The neurogenic bladder term is also flagged as obsolete in the ontology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked prediction, cauda equina syndrome.

For other predicted indications, a few publications were retrieved. None shows therapeutic efficacy of cisatracurium:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41103680](https://pubmed.ncbi.nlm.nih.gov/41103680/) | 2025 | Cohort/comparative | Anesthesiology and Pain Medicine | Serum IL-6, leptin and adiponectin after caesarean section under general vs spinal anaesthesia (related to preeclampsia prediction) |
| [18383970](https://pubmed.ncbi.nlm.nih.gov/18383970/) | 2008 | Case series (12 cases) | Rev Esp Anestesiol Reanim | Remifentanil bolus for haemodynamic control in high-risk caesarean patients ineligible for spinal anaesthesia (related to preeclampsia prediction) |
| [12565113](https://pubmed.ncbi.nlm.nih.gov/12565113/) | 2002 | Clinical experience report | J Clin Anesth | Anaesthetic care in paediatric living-related liver transplantation (related to thrombotic disease prediction) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14310P | Nimbex Forte Injection 150 mg/30 ml | Injection, solution | Not stated in the data compiled |
| SIN14309P | Nimbex Injection 2 mg/ml | Injection, solution | Not stated in the data compiled |

Both products are valid single-ingredient registrations, manufactured by GlaxoSmithKline Manufacturing S.p.A.

## Safety Considerations

- **Drug Interactions:** 61 interactions were recorded. The following are the main ones in the data compiled:
  - **Major:** kanamycin, neomycin, paromomycin, polymyxin B, streptomycin (aminoglycoside and polymyxin antibiotics, which may potentiate neuromuscular blockade)
  - **Moderate:** amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), neomycin (topical), tetracycline, doxycycline, minocycline, vancomycin, magnesium chloride, magnesium sulfate, mannitol, metoclopramide
  - **Minor:** ranitidine, ranitidine (bismuth citrate)
- **Clinical note:** Magnesium sulfate, used in severe preeclampsia, potentiates non-depolarising blockers. This is a relevant safety concern for any obstetric use.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but it is not backed by any clinical trial or relevant publication, and there is no credible mechanism linking neuromuscular blockade to cauda equina syndrome or to the other top predictions. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, as safety screening cannot proceed without them
- Approved indication text for the Singapore registrations
- Detailed mechanism-of-action data and a pharmacological rationale for the predicted indication
- Any preclinical or clinical studies of cisatracurium in the predicted conditions
- A review of route and setting compatibility, since the drug is an injectable used under anaesthetic supervision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

