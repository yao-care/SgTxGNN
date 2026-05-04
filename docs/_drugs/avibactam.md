---
layout: default
title: Avibactam
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Avibactam
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

# Avibactam: From Resistant Gram-negative Infections to Streptococcal Pneumonia

## One-Sentence Summary

Avibactam is a non-β-lactam β-lactamase inhibitor, approved globally (as ceftazidime-avibactam) for serious multi-drug resistant gram-negative bacterial infections, but not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Streptococcal Pneumonia**, yet **0 clinical trials** and **0 publications** currently support this direction.
Mechanistic review classifies this as a **biologically implausible false positive**: *Streptococcus pneumoniae* confers β-lactam resistance through PBP mutations — not serine β-lactamase production, which is avibactam's sole target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally used as ceftazidime-avibactam combination for resistant Gram-negative infections |
| Predicted New Indication | Streptococcal Pneumonia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Avibactam is a diazabicyclooctane (DBO)-class, non-β-lactam β-lactamase inhibitor that forms a covalent yet reversible bond with the active-site serine residue of class A, C, and selected class D serine β-lactamases (including KPC, CTX-M, AmpC, and OXA-48). When paired with a β-lactam partner — most notably ceftazidime (Avycaz) — it restores antibacterial potency against carbapenem-resistant Enterobacteriaceae (*Klebsiella pneumoniae*, *Escherichia coli*) and certain non-fermenters (*Pseudomonas aeruginosa*). Avibactam itself carries no intrinsic antibacterial activity.

**This prediction does not hold up under mechanistic scrutiny.** *Streptococcus pneumoniae* is a Gram-positive organism. Its resistance to β-lactam antibiotics is mediated exclusively by mutations in penicillin-binding proteins (PBPs), not by serine β-lactamase hydrolysis. Because avibactam acts only on serine β-lactamases, it has no mechanistic pathway to overcome PBP-mediated resistance and cannot potentiate antibiotic activity against *S. pneumoniae*. No published evidence of avibactam activity-enhancement against any Gram-positive pathogen currently exists.

The TxGNN score of 99.70% most likely reflects graph traversal noise: the knowledge graph may link *avibactam → β-lactam antibiotic → respiratory infection → pneumococcal pneumonia* through shared edge weights without capturing organism-level mechanistic constraints. This is a recognised limitation of graph-embedding models, where topological proximity in a knowledge graph does not always reflect biological plausibility. Notably, this prediction ranks 4,629th among all disease nodes in the model's global output — indicating it is far from a high-confidence prediction even within the model's own hierarchy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Avibactam targets serine β-lactamases expressed by Gram-negative bacteria and has no known mechanism of action against *Streptococcus pneumoniae*, whose β-lactam resistance is driven by PBP mutations. With zero supporting clinical or pre-clinical evidence, this prediction is an L5 model-only hypothesis that fails mechanistic plausibility screening at the earliest stage.

**To proceed, the following would be needed:**
- Demonstration of serine β-lactamase expression in clinically relevant *S. pneumoniae* strains (not currently documented in the literature)
- Pre-clinical in vitro data showing any avibactam-mediated potentiation of β-lactam activity against *S. pneumoniae*
- Complete MOA data from DrugBank or package insert to identify any secondary mechanisms not currently captured
- Singapore regulatory pathway assessment, as avibactam is not registered locally

---

## Appendix: All Predicted Indications Summary

This is a multi-candidate evaluation report (TW-DB09060-multi). The table below summarises all 10 TxGNN-ranked predictions.

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Publications | Decision | Mechanistic Assessment |
|------|---------|-------------|----------------|--------|--------------|----------|------------------------|
| 1 | Streptococcal Pneumonia | 99.70% | L5 | 0 | 0 | Hold | ❌ False positive — PBP-mediated resistance, not β-lactamase |
| 2 | Influenza, Severe | 99.28% | L5 | 0 | 0 | Hold | ❌ False positive — viral target; no bacterial β-lactamase pathway |
| 3 | Ureter Tuberculosis | 99.11% | L5 | 0 | 0 | Hold | ⚠️ Theoretical basis via *M. tuberculosis* BlaC inhibition; no evidence for this anatomical site |
| 4 | Urinary Schistosomiasis | 99.06% | L5 | 0 | 0 | Hold | ❌ False positive — helminthic parasite; no cell wall or β-lactamase target |
| 5 | Hyperamylasemia | 99.01% | L5 | 0 | 0 | Hold | ❌ False positive — metabolic marker; graph embedding confuses "enzyme inhibitor" semantic nodes |
| 6 | Polyclonal Hyperviscosity Syndrome | 99.01% | L5 | 0 | 0 | Hold | ❌ False positive — haematological/immunological disease; no mechanistic link |
| 7 | Staphylococcus aureus Infection | 98.97% | L4 | 2 | 20 | Hold | ⚠️ Limited mechanistic basis (PC1 β-lactamase inhibition); in vitro ceftaroline-avibactam data exist, but no direct clinical outcome evidence |
| 8 | Renal Tuberculosis | 98.93% | L5 | 0 | 1 | Hold | ⚠️ Theoretical BlaC basis; sole matched publication is on CRE infections — a false-match |
| 9 | Squamous Cell Lung Carcinoma | 98.86% | L5 | 0 | 0 | Hold | ❌ False positive — oncological disease; no antineoplastic mechanism |
| 10 | Congenital Analbuminemia | 98.84% | L5 | 0 | 0 | Hold | ❌ False positive — PK protein-binding parameter misinterpreted as therapeutic relationship |

### Key Findings

- **All 10 predictions are rated "Hold"** — none meet the threshold for advancing to structured clinical exploration.
- **8 of 10 predictions are mechanistically implausible** false positives, spanning viral, parasitic, oncological, haematological, and metabolic conditions for which avibactam has no conceivable mechanism.
- **Rank 7 (Staphylococcus aureus infection)** is the most evidence-supported candidate (L4, 2 observational trials, 20 publications) and carries the most plausible theoretical rationale (ceftaroline-avibactam vs. MRSA/MSSA via PC1 β-lactamase), yet remains "Hold" because existing evidence does not directly test avibactam's clinical contribution to *S. aureus* infection outcomes.
- **Ranks 3 and 8 (Ureter/Renal Tuberculosis)** share a theoretical mechanistic foundation via *M. tuberculosis* BlaC inhibition (supported by Soroka et al. 2015), but lack any evidence specific to genitourinary TB, and the single matched publication for renal TB is a mismatch about CRE infections.
- **Singapore regulatory barrier**: Avibactam is not registered in Singapore. Any repurposing programme would require a full regulatory submission prior to clinical use.

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

