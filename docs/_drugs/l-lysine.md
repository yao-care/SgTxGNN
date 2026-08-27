---
layout: default
title: L-Lysine
parent: 僅模型預測 (L5)
nav_order: 564
evidence_level: L5
indication_count: 10
---

# L-Lysine
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

# L-Lysine: From Nutritional Supplement to Gastroparesis

## One-Sentence Summary

L-Lysine is an essential amino acid with no approved drug indications in Singapore, primarily recognised as a nutritional supplement and protein-synthesis building block.
The TxGNN model predicts it may be effective for **Gastroparesis**,
however with **0 clinical trials** and only **1 tangentially related basic science publication**, the evidentiary foundation is essentially absent.
The high prediction score (99.77%) is suspected to reflect a knowledge graph false positive rather than a genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved drug indication on record (essential amino acid / nutritional supplement) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

L-Lysine is an essential amino acid that humans cannot synthesise endogenously. In normal physiology, it serves several biochemical roles: it is a structural component of collagens (cross-linked via lysyl oxidase), a precursor to carnitine biosynthesis (through trimethyllysine intermediates), and a key substrate in the lysine-catabolism pathway relevant to pyridoxine-dependent epilepsy. Detailed pharmacological mechanism of action data is currently unavailable from DrugBank for this candidate, so the analysis below relies on known biochemistry.

Gastroparesis is a gastric motility disorder characterised by delayed emptying without mechanical obstruction. The core pathology involves depletion of interstitial cells of Cajal (ICC) and enteric neuron dysfunction, leading to pyloric dysregulation and severe nausea/vomiting. The proposed mechanistic link to L-Lysine is extremely tenuous: L-Lysine's participation in collagen cross-linking through lysyl oxidase could theoretically influence gastric wall connective tissue, but no direct biochemical or pharmacological pathway has been described linking L-Lysine supplementation to ICC regeneration or gastric motility restoration.

The sole retrieved publication (PMID 29414870) investigates mesenchymal stem cell therapy delivered via a gelatin-alginate hydrogel scaffold in gastroparesis — a study completely unrelated to L-Lysine as a therapeutic agent. The high TxGNN score (0.998) therefore most likely reflects knowledge graph noise: a spurious co-occurrence of "lysine" terminology in gastroparesis-adjacent graph nodes, rather than a meaningful drug–disease relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Basic Science | Bioengineering (Basel, Switzerland) | Delivery of mesenchymal stem cells via gelatin-alginate hydrogel to restore ICC and enteric neurons in gastroparesis animal models — no involvement of L-Lysine as a pharmacological agent |

---

## Singapore Market Information

L-Lysine has no regulatory registrations with the Health Sciences Authority (HSA) of Singapore. No authorization numbers, brand names, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN score, the gastroparesis prediction is unsupported by any clinical trials and the single retrieved publication is entirely unrelated to L-Lysine as a therapy; the mechanistic link is non-existent under current evidence.

**Noteworthy finding across the full Top-10 prediction list:**
Of the 10 predicted indications evaluated, only **Vitamin Deficiency Disorder (Rank 6)** reaches a higher evidence tier (L4) and advances to decision stage S1 with a "Research Question" recommendation. This is supported by a biologically plausible mechanistic link — L-Lysine is a direct precursor in carnitine biosynthesis (requiring both L-Lysine and Vitamin C as cofactors), lysine-restriction is an established adjunct therapy in pyridoxine-dependent epilepsy (a Vitamin B6-related disorder), and secondary carnitine deficiency resulting from vitamin deficiencies is well-documented. Redirecting investigational focus to Vitamin Deficiency Disorder may yield a more productive repurposing hypothesis.

**To proceed on gastroparesis (current rank 1), the following is needed:**
- Evidence of a direct mechanistic pathway linking L-Lysine to gastric motility or ICC biology
- At minimum, in vitro or animal model studies specifically testing L-Lysine in gastroparesis
- MOA data retrieval from DrugBank API (currently a data gap)
- HSA package insert review for Singapore-relevant safety and contraindication data

**To advance the more promising Vitamin Deficiency Disorder hypothesis (rank 6), the following is needed:**
- Prospective clinical study protocol evaluating L-Lysine supplementation in patients with documented vitamin-associated carnitine deficiency
- Quantification of plasma L-Lysine and carnitine levels as pharmacodynamic endpoints
- Regulatory consultation on indication scope (dietary supplement vs. drug classification in Singapore)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

