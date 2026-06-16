---
layout: default
title: Epoprostenol
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Epoprostenol
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

# Epoprostenol: From Pulmonary Arterial Hypertension to Trigeminal Autonomic Cephalalgia

## One-Sentence Summary

Epoprostenol (prostacyclin, PGI₂) is a synthetic prostaglandin vasodilator established globally for pulmonary arterial hypertension, with no current registration in Singapore.
The TxGNN model predicts it may be effective for **Trigeminal Autonomic Cephalalgia (TAC)** with a prediction score of **98.41%**, but this is supported by only **0 clinical trials** and **2 publications** — and critically, the available mechanistic evidence points in the opposite direction of a therapeutic use.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore (established globally for pulmonary arterial hypertension) |
| Predicted New Indication | Trigeminal Autonomic Cephalalgia |
| TxGNN Prediction Score | 98.41% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, Epoprostenol is a synthetic prostacyclin (PGI₂) that binds IP (prostacyclin) receptors to elevate intracellular cAMP, producing vasodilation and antiplatelet effects. Its established clinical use — in pulmonary arterial hypertension — exploits this vasodilatory property to reduce pulmonary vascular resistance.

Trigeminal Autonomic Cephalalgia (TAC) is a family of severe unilateral headache disorders (including cluster headache, paroxysmal hemicrania, and SUNCT), characterised by autonomic features such as lacrimation, rhinorrhoea, and ptosis. The TxGNN model assigns a high score of 98.41%, which most likely reflects the well-documented co-occurrence of PGI₂ and headache disorders in the biomedical literature and knowledge graph — not a genuine therapeutic signal.

**⚠️ Reverse Mechanism Warning:** Research from the 1980s observed elevated PGI₂ metabolites during cluster headache attacks. The sole directly relevant publication (PMID 7026501) explored the effect of infused prostacyclin in cluster headache patients — with results suggesting PGI₂ may precipitate rather than relieve attacks. There is no evidence that exogenous Epoprostenol ameliorates TAC. The TxGNN score of 98.41% is assessed as a false positive driven by disease-drug co-occurrence in the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Epoprostenol in trigeminal autonomic cephalalgia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7026501](https://pubmed.ncbi.nlm.nih.gov/7026501/) | 1981 | Clinical Study / Case Series | Headache | Examined the effect of infused prostacyclin in migraine and cluster headache patients; results do not support a therapeutic benefit and may reflect a precipitating effect |
| [3937967](https://pubmed.ncbi.nlm.nih.gov/3937967/) | 1985 | Review / Mechanistic | Neurologia i neurochirurgia polska | Investigated pathomechanisms of Horton's cluster headache using nitroglycerin provocation and indomethacin (COX inhibitor) blockade; discusses PGI₂ as part of attack pathogenesis rather than treatment |

---

## Singapore Market Information

Epoprostenol is not currently registered with the Health Sciences Authority (HSA) in Singapore. There are no active product licences, authorisations, or approved indications on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The available literature consistently positions PGI₂ (Epoprostenol) as a headache-precipitating agent rather than a therapeutic agent in trigeminal autonomic cephalalgia; the high TxGNN score reflects knowledge graph co-occurrence and is assessed as a false positive.

**To proceed further, the following is needed:**

- Retrieve full mechanism of action data from DrugBank (flagged as a High-severity data gap: DG002) to determine whether any downstream IP-receptor pathway could be selectively modulated for TAC benefit
- Review emerging literature on prostacyclin receptor antagonism (blocking, not activating, the IP pathway) in primary headache disorders, which would represent a conceptually different intervention
- Prioritise evaluation of the **Rank 9 prediction — Respiratory Failure (Evidence Level L1, "Proceed with Guardrails")** — which has multiple completed Phase 2–3 trials of inhaled Epoprostenol, including a double-blind RCT (NCT04452669) and a large multicentre RCT (NCT00159861, n = 267), representing the strongest actionable repurposing candidate for this drug within this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

