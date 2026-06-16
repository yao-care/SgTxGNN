---
layout: default
title: Dextromethorphan
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
---

# Dextromethorphan
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

# Dextromethorphan: From Cough Suppression to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan (DXM) is a widely used antitussive (cough suppressant), acting primarily through NMDA receptor antagonism in the brainstem cough centre and Sigma-1 receptor modulation.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **1 clinical trial** (currently recruiting, for a different indication) and **no direct publications** supporting this specific direction.
The mechanistic hypothesis is biologically plausible, but dedicated clinical evidence for nasal cavity disease remains absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cough suppression (antitussive) — no Singapore registration on file |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 ⚠️ (see note below) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> ⚠️ **Evidence Level Note:** The scoring of L1 reflects the existence of a Phase 3 RCT involving DXM (NCT06958692); however, that trial targets **Major Depressive Disorder**, not nasal cavity disease. For the specific predicted indication of nasal cavity disease, the effective evidence level is closer to **L5** (model prediction only). This distinction is critical for downstream decision-making.

---

## Why is This Prediction Reasonable?

Dextromethorphan is a morphinan-class compound with two well-characterised pharmacological targets. First, it acts as an **NMDA receptor (NMDAr) antagonist** in the medullary cough centre, suppressing cough reflexes — its primary approved use. Second, it is a **Sigma-1 receptor (Sigma-1r) agonist**, which carries broader implications for neurological modulation and, more recently, immunological regulation. These dual mechanisms provide a biological basis for exploring applications beyond simple cough suppression.

The link to nasal cavity disease is indirect but plausible. Many nasal conditions (e.g., allergic rhinitis, non-allergic rhinitis, sinusitis) drive cough reflexes through post-nasal drip and mucosal irritation — pathways directly modulated by DXM's NMDAr antagonism. Additionally, Sigma-1r agonism has been proposed to modulate inflammatory signalling in mucosal tissues, which could theoretically reduce airway inflammation contributing to nasal cavity pathology. An in vitro study on DXM's effect on ciliary beat frequency (PMID 2255670, cited under tracheal disease) further hints at direct effects on respiratory mucosal physiology.

However, it is important to acknowledge that TxGNN's high score may partly reflect **graph topological proximity** — DXM's drug node sits close to upper respiratory disease nodes in the knowledge graph due to its established antitussive role — rather than a confirmed direct therapeutic mechanism for nasal cavity disease specifically. Dedicated mechanistic and clinical studies would be needed to validate this prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Multicenter, randomised, double-blind, placebo-controlled trial evaluating DXM + bupropion sustained-release tablets in Chinese adult patients with **Major Depressive Disorder**. Estimated completion December 2026. ⚠️ This trial targets MDD, not nasal cavity disease. |

---

## Literature Evidence

Currently no related clinical literature available specifically for nasal cavity disease.

---

## Singapore Market Information

Dextromethorphan currently has **no registered products** in Singapore. There are 0 marketing authorisations on file, and the drug is classified as **not marketed** in the Singapore regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety data fields (key warnings, contraindications, and drug–drug interactions) are currently unavailable in this Evidence Pack. A complete safety review from the package insert and DrugBank is required before any clinical repurposing decision can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
TxGNN assigns a high confidence score (99.98%) for nasal cavity disease, and DXM's established antitussive mechanism provides a biologically plausible — if indirect — connection to upper airway pathology. However, the sole clinical trial cited (NCT06958692) is for Major Depressive Disorder and is still recruiting, meaning **no clinical evidence directly supports the nasal cavity disease indication**. Proceeding requires a structured evidence-generation plan rather than reliance on existing data.

**To proceed, the following is needed:**

- **Preclinical evidence**: Dedicated in vitro/in vivo studies confirming DXM's activity in nasal cavity disease models (e.g., allergic rhinitis, chronic sinusitis, nasal polyp inflammation)
- **Literature deep-dive**: Systematic search for any publications on DXM and nasal mucosal effects, Sigma-1r and upper airway inflammation, or DXM use in rhinitis/sinusitis management
- **MOA documentation**: Full mechanism of action profile from DrugBank (currently a data gap), especially Sigma-1r immunomodulatory data
- **Safety profile**: Retrieval and review of full prescribing information including warnings, contraindications, and drug–drug interactions (all currently data gaps)
- **Route of administration assessment**: Evaluation of whether oral DXM dosing achieves adequate nasal mucosal concentrations, or whether an intranasal formulation would be required
- **Singapore regulatory pathway**: Formal assessment for product registration, given zero current authorisations in Singapore
- **Indication alignment review**: Clarify whether the Phase 3 trial (NCT06958692) for MDD has any secondary endpoints or subgroup analyses relevant to nasal/upper respiratory outcomes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

