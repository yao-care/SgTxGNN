---
layout: default
title: Phenylalanine
parent: 僅模型預測 (L5)
nav_order: 778
evidence_level: L5
indication_count: 10
---

# Phenylalanine
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

# Phenylalanine: From Essential Amino Acid to Sclerosing Cholangitis

## One-Sentence Summary

Phenylalanine (DrugBank DB00120) is an essential amino acid with no approved therapeutic indication on record in Singapore. The TxGNN model's top prediction suggests possible relevance to **Sclerosing Cholangitis**, but this is supported by **0 clinical trials** and only **4 publications**, most of which involve unrelated compounds (a bacterial chemotactic peptide and tyrosine) rather than phenylalanine itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no approved indication on record (essential amino acid, not marketed as a therapeutic in Singapore) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for phenylalanine in this context is not available (Data Gap). Phenylalanine is a naturally occurring essential amino acid and metabolic precursor to tyrosine; it has no established pharmacological indication for hepatobiliary disease.

Reviewing the supporting literature for this specific prediction raises concerns rather than confirming plausibility. Of the four associated publications, one is an animal model of cholangitis induced by **fMLP (N-formyl-methionyl-leucyl-phenylalanine)** — a bacterial chemotactic peptide that merely contains a phenylalanine residue, not free phenylalanine itself — and a related paper on enterohepatic circulation of the same bacterial peptide. The remaining two concern tyrosine levels in primary biliary cirrhosis/PSC patients and a cholangiocarcinoma metabolomics study, neither of which demonstrates a therapeutic role for phenylalanine.

Taken together, this pattern is consistent with an **embedding/name-similarity confound** (phenylalanine ↔ fMLP peptide ↔ tyrosine) rather than a genuine mechanistic signal. No clinical trials exist to counterbalance this concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined plasma tyrosine (not phenylalanine) concentration and its relation to fatigue in PBC/PSC patients — an association study, not an interventional signal |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort/Metabolomics | J Clin Exp Hepatol | Serum metabolomic profiling in cholangiocarcinoma vs. benign hepatobiliary disease; amino acids appear only as incidental biomarkers |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Animal (fMLP-induced, not phenylalanine itself) | J Gastroenterology | Rectal fMLP (a bacterial chemotactic tripeptide containing phenylalanine) induced small duct cholangitis in rats with colitis — a disease model, not a treatment |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Basic Research | J Gastroenterol Hepatol | Enterohepatic circulation of bacterial chemotactic peptides (F-met-oligopeptides) in humans; unrelated to free phenylalanine therapy |

---

## Singapore Market Information

Phenylalanine is not marketed in Singapore; no HSA registration records are available (total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Sclerosing Cholangitis) rests on Evidence Level L5 with zero clinical trials, and the four supporting publications appear to be confounded matches driven by name/embedding similarity (fMLP peptide, tyrosine) rather than evidence of phenylalanine's own therapeutic effect. All other TxGNN-predicted indications for this compound (ranks 2–10, including congenital prothrombin deficiency, epiglottitis, hypophosphatemic rickets, laryngitis, cholecystolithiasis, and diabetic nephropathy) were similarly flagged as Hold due to unrelated trial drugs (e.g., Nitisinone, RAS blockers) or confounded literature (e.g., levodopa-related studies mismatched to phenylalanine). No candidate in this evidence pack currently supports advancement.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent label safety data — warnings and contraindications (blocking gap, DG001)
- Verified mechanism of action data from DrugBank (DG002)
- Confirmation of the original approved indication(s), if any exist in another jurisdiction
- Phenylalanine-specific (not fMLP- or tyrosine-derived) preclinical or clinical evidence directly addressing sclerosing cholangitis before any further evaluation stage is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

