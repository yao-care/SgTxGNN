---
layout: default
title: Benzoic Acid
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Benzoic Acid
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

# Benzoic Acid: From Antimicrobial Preservative to Bronchitis

## One-Sentence Summary

Benzoic acid is a small-molecule organic acid historically used as an antimicrobial preservative and topical antifungal agent (e.g., Whitfield's ointment), with no formal registered indications in Singapore.
The TxGNN model predicts it may be effective for **Bronchitis**, with a prediction score of **99.98%**.
However, **no clinical trials** and only **2 incidentally related publications** currently support this direction — making this a model-only prediction requiring substantial further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formally registered indication (used as antimicrobial preservative / topical antifungal component) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for benzoic acid as a therapeutic agent. Based on known information, benzoic acid is a simple aromatic carboxylic acid with established antimicrobial properties — it inhibits the growth of bacteria and fungi by disrupting cell membrane function and interfering with intracellular pH homeostasis. It has historically been paired with salicylic acid in Whitfield's ointment for topical fungal infections, and is widely used as a food preservative (E210).

From a mechanistic standpoint, there is a theoretically plausible link to bronchitis: benzoic acid has demonstrated weak antimicrobial activity against respiratory pathogens including *Streptococcus* and *Haemophilus influenzae*, organisms frequently implicated in acute bacterial bronchitis. Additionally, some benzoic acid derivatives have shown NF-κB inhibitory activity, which could theoretically attenuate airway inflammation. However, these are indirect and extrapolated properties — no systematic respiratory pharmacology studies exist for benzoic acid itself.

Importantly, the two retrieved literature items do not directly study benzoic acid in bronchitis. One describes repaglinide (a *carbamoylmethyl benzoic acid derivative*), and the other investigates a soluble epoxide hydrolase inhibitor in COPD. Neither constitutes evidence for benzoic acid in bronchitis treatment. The TxGNN prediction likely reflects knowledge graph proximity between benzoic acid's antimicrobial node and respiratory infection nodes, rather than direct biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 2 retrieved publications are **contextually related but do not directly study benzoic acid for bronchitis**. They are included for completeness.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Review | *Drugs* | Review of repaglinide, a **carbamoylmethyl benzoic acid derivative**, for type 2 diabetes — demonstrates that benzoic acid scaffold derivatives have pharmacological activity, but no connection to bronchitis |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Animal/Preclinical | *Am J Respir Cell Mol Biol* | Soluble epoxide hydrolase inhibitor shows anti-inflammatory effects in tobacco smoke-induced COPD/bronchitis rat model — relevant to bronchitis pathology but does not involve benzoic acid |

---

## Singapore Market Information

Benzoic acid (DrugBank ID: DB03793) has **no registered pharmaceutical products** in Singapore. It is not approved as a standalone therapeutic agent and carries no Health Sciences Authority (HSA) marketing authorizations.

---

## Safety Considerations

Please refer to the package insert and relevant regulatory sources for safety information. No formal warning, contraindication, or drug interaction data was available in this evidence pack.

> **Note:** Although no DDI data was returned, benzoic acid is known to be metabolized via glycine conjugation to hippuric acid. Clinicians should be aware of potential interactions with drugs relying on glycine pathway or renal organic acid transporters. This warrants further pharmacokinetic investigation before any therapeutic development proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications for benzoic acid are rated L5 (model prediction only), and the top indication — bronchitis — is supported by zero direct clinical or preclinical evidence. The retrieved literature items are incidentally retrieved background papers with no therapeutic relevance to benzoic acid in respiratory disease. With no Singapore market presence, no registered indications, and no MOA data, this candidate does not meet the minimum evidentiary threshold to proceed.

**To proceed, the following is needed:**

- **Establish basic pharmacology:** Confirm benzoic acid's anti-inflammatory and antimicrobial activity in respiratory cell/animal models (in vitro MIC studies against *H. influenzae*, *S. pneumoniae*; NF-κB inhibition assay in bronchial epithelial cells)
- **Resolve MOA data gap (DG002):** Query DrugBank API for full mechanistic profile of DB03793
- **Resolve safety data gap (DG001):** Review available toxicology literature and any relevant regulatory monographs (e.g., FDA GRAS status, EMA assessments) to establish a safety baseline
- **Assess drug-like properties:** Evaluate PK/PD suitability for pulmonary delivery — benzoic acid is primarily used topically/as preservative; its systemic or inhaled pharmacology is poorly characterised
- **Investigate KG prediction artifact:** The cluster of high-scoring fibromatosis indications (ranks 5–7, scores 0.9975–0.9977) strongly suggests knowledge graph node-cluster effects. A graph-level review of benzoic acid's neighbourhood in TxGNN is recommended to distinguish genuine biological signal from topological artifacts before acting on any of the top-10 predictions
- **Preclinical proof-of-concept study** before any clinical development consideration

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

