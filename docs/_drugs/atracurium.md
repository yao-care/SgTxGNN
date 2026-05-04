---
layout: default
title: Atracurium
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
---

# Atracurium
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

# Atracurium: From Neuromuscular Blockade to Myofascial Pain Syndrome

## One-Sentence Summary

Atracurium is a non-depolarizing neuromuscular blocking agent (NMBA) used in surgical settings to induce skeletal muscle relaxation and facilitate endotracheal intubation.
The TxGNN model predicts it may be effective for **Myofascial Pain Syndrome** with a score of 94.10%, yet **no clinical trials** and **no publications** directly support this direction.
All 10 predicted indications across this evaluation are rated **L5** (model prediction only), and the overall recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neuromuscular blockade for surgical procedures (general anesthesia adjunct) |
| Predicted New Indication | Myofascial Pain Syndrome |
| TxGNN Prediction Score | 94.10% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in this Evidence Pack. Based on established pharmacological knowledge, Atracurium is a competitive antagonist at peripheral nicotinic acetylcholine receptors (nAChR) at the neuromuscular junction. It causes complete and reversible skeletal muscle paralysis by blocking acetylcholine-mediated depolarization. Its effect is entirely peripheral and requires ventilatory support in clinical use.

Myofascial pain syndrome (MPS) is characterised by persistent regional musculoskeletal pain driven by myofascial trigger points and a pathological pain–spasm–pain cycle. Theoretically, complete skeletal muscle relaxation could interrupt this cycle. However, this logic breaks down entirely when translated to clinical practice: achieving this effect with Atracurium requires full general anaesthesia and mechanical ventilation, making it wholly disproportionate to MPS management, which is safely and effectively addressed by local trigger-point injections, physiotherapy, and oral analgesics.

Furthermore, Atracurium's well-known propensity for histamine release introduces additional risk. The TxGNN model's high score for this indication most likely reflects a non-specific graph connection between "NMBA" and "musculoskeletal disorder" nodes in the knowledge graph, rather than a true pharmacological rationale. There is no plausible clinical pathway from Atracurium's mechanism to meaningful, safe, and feasible MPS treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for myofascial pain syndrome.

---

## Singapore Market Information

Atracurium is **not registered** with the Health Sciences Authority (HSA) in Singapore. No product licences are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|------------|-------------------|
| — | — | — | No registrations found |

> **Note:** Atracurium is widely available internationally as an IV injection for intraoperative use (e.g., Tracrium®). The absence of HSA registration means that any future clinical study or compassionate use would require additional regulatory engagement.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Two data gaps were flagged during evidence collection:
> - **DG001 (Blocking):** Singapore/TFDA package insert warnings and contraindications have not been retrieved. This prevents formal S1-level safety screening.
> - **DG002 (High):** Formal MOA data from DrugBank has not been retrieved, limiting mechanistic analysis.
>
> From general pharmacological knowledge, key safety signals for Atracurium include: histamine release (risk of bronchospasm and hypotension), potential for prolonged paralysis in patients with pseudocholinesterase abnormalities, laudanosine accumulation in renal/hepatic failure (central nervous system excitation), and absolute requirement for airway management and ventilation support during administration.

---

## Comprehensive Indication Review

All 10 TxGNN-predicted indications for Atracurium were evaluated. The table below summarises findings across the full ranked list.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Literature | Key Mechanistic Issue |
|------|---------------------|------------|---------------|----------|----------------------|
| 1 | Myofascial pain syndrome | 94.10% | L5 | None | Requires full GA/ventilation; clinically infeasible for MPS |
| 2 | Nephrogenic syndrome of inappropriate antidiuresis (NSIAD) | 93.90% | L5 | None | AVPR2 gain-of-function; no intersection with nAChR antagonism |
| 3 | Methemoglobinemia | 92.63% | L5 | 1 (adverse signal) | Literature (PMID [7653798](https://pubmed.ncbi.nlm.nih.gov/7653798/)) describes Atracurium as a **co-exposure** worsening MetHb — a safety concern, not a therapeutic signal |
| 4 | Common cold | 92.56% | L5 | 1 (irrelevant) | Literature (PMID [25902325](https://pubmed.ncbi.nlm.nih.gov/25902325/)) is a perioperative hypersensitivity study; unrelated to viral URTI |
| 5 | Conjunctivitis | 90.08% | L5 | None | Systemic NMBA; no ocular local application feasibility; histamine release may worsen allergic conjunctivitis |
| 6 | Idiopathic granulomatous myositis | 88.71% | L5 | None | Autoimmune; requires immunomodulation (steroids/DMARDs); no immunomodulatory mechanism |
| 7 | Myositis fibrosa | 88.71% | L5 | None | Fibrotic process (TGF-β/collagen deposition); no mechanistic link to nAChR antagonism |
| 8 | Tendinitis | 88.27% | L5 | None | Local inflammation; systemic NMBA risk–benefit ratio does not support use |
| 9 | Methemoglobinemia, alpha type (hereditary) | 88.24% | L5 | None | NADH-cytochrome b5 reductase deficiency; enzyme-replacement/redox mechanism required; irrelevant |
| 10 | Fibromyalgia | 88.00% | L5 | 1 (perioperative context) | Literature (PMID [9095707](https://pubmed.ncbi.nlm.nih.gov/9095707/)) addresses defasciculation pre-treatment, not fibromyalgia pathophysiology (central sensitisation) |

> **Pattern observed:** Ranks 6–10 are dominated by musculoskeletal/pain disorders (myositis, tendinitis, fibromyalgia), suggesting the TxGNN knowledge graph is generating high scores via non-specific "skeletal muscle" node connectivity rather than specific pharmacological relevance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Across all 10 TxGNN-predicted indications, there is zero supporting clinical trial evidence and no directly relevant literature. The mechanistic analysis consistently reveals either implausible clinical application (e.g., requiring full anaesthesia for MPS) or complete absence of mechanistic overlap (e.g., NSIAD, MetHb, viral infections). Three literature records retrieved are either adverse-signal reports or entirely off-topic perioperative studies. Atracurium is also not registered in Singapore, adding a regulatory barrier. None of the predicted indications reaches L4 or above.

**To proceed (if further evaluation is warranted), the following is needed:**

- **Retrieve DG001:** Download and parse the TFDA/HSA package insert PDF to complete S1-level safety screening and identify formal contraindications and warnings
- **Retrieve DG002:** Query DrugBank API for formal MOA, pharmacodynamics, and toxicity data to support mechanistic analysis
- **Re-evaluate with stronger candidates:** Consider whether TxGNN should be re-run with refined disease ontology mappings to reduce non-specific musculoskeletal node connections
- **Explore cisatracurium (metabolite/congener) separately:** Cisatracurium (lower histamine release) may have a distinct risk profile if any musculoskeletal indication were to be pursued; evaluate as a separate candidate
- **Scientific advisory review:** Given the universal Hold outcome and mechanistic implausibility across all indications, consider a formal scientific advisory board review before committing further evidence-collection resources to this drug

---

> ⚠️ **Disclaimer:** This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This prediction is generated by the TxGNN model and has not been clinically verified.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

