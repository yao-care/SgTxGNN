---
layout: default
title: Tigecycline
parent: 僅模型預測 (L5)
nav_order: 980
evidence_level: L5
indication_count: 10
---

# Tigecycline
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

# Tigecycline: From Complicated Bacterial Infections to Disorder of Tyrosine Metabolism

## One-Sentence Summary

Tigecycline is a glycylcycline antibiotic, internationally indicated for complicated skin/skin-structure infections and complicated intra-abdominal infections. The TxGNN model's top-ranked prediction is **disorder of tyrosine metabolism**, but the only supporting clinical trial and literature actually concern chronic myeloid leukemia (CML) and mitochondrial metabolism — not tyrosine metabolism — suggesting this ranking is likely a **knowledge-graph label mismatch** rather than a genuine, disease-specific signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (drug not marketed); internationally approved for complicated skin/skin-structure and intra-abdominal infections |
| Predicted New Indication | Disorder of tyrosine metabolism |
| TxGNN Prediction Score | 95.76% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for tigecycline is not available in this evidence pack ([Data Gap] — see DG002). Based on the drug's known pharmacology and the repurposing rationale supplied with this prediction, tigecycline's off-target repurposing mechanism is **mitoribosome inhibition**, which suppresses oxidative phosphorylation (OXPHOS). This gives it selective cytotoxicity against leukemia/myeloma stem cells and, in dermatological studies, an effect on melanocyte metabolism.

However, this mechanism has **no established causal link** to "disorder of tyrosine metabolism," which refers to congenital amino-acid metabolic diseases such as tyrosinemia. The single associated clinical trial (NCT02883036) actually studies tigecycline's mitochondrial effects in **chronic myeloid leukemia (CML)**, and three of the four associated publications concern CML/lung adenocarcinoma stem-cell OXPHOS biology, with the fourth examining melanocyte and fibroblast homeostasis — not tyrosine metabolism pathology.

The most plausible explanation is that TxGNN's high score arises from graph proximity between tyrosinase/melanocyte-pathway nodes and mitochondrial-metabolism nodes in the knowledge graph, rather than a true disease-mechanism match. This prediction should therefore be treated as a **candidate for ontology/label verification**, not as direct mechanistic evidence for tyrosine metabolism disorders.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02883036](https://clinicaltrials.gov/study/NCT02883036) | N/A | Unknown | 100 | In vitro study of tigecycline's effect on mitochondrial biogenesis and metabolic characteristics in chronic myeloid leukemia (CML) — not related to tyrosine metabolism disorder; relevance graded C (label mismatch) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28920959](https://pubmed.ncbi.nlm.nih.gov/28920959/) | 2017 | Preclinical/Mechanistic | Nature Medicine | Tigecycline + imatinib disrupts mitochondrial OXPHOS to eradicate therapy-resistant CML leukemic stem cells |
| [31765940](https://pubmed.ncbi.nlm.nih.gov/31765940/) | 2020 | Preclinical/Mechanistic | Neoplasia | SIRT1/OXPHOS-targeted eradication of EGFR-TKI-resistant lung adenocarcinoma stem cells |
| [41009505](https://pubmed.ncbi.nlm.nih.gov/41009505/) | 2025 | In vitro study | Int J Mol Sci | Tigecycline's effect on human epidermal melanocyte and fibroblast homeostasis (pigmentary/phototoxicity context) |
| [29404396](https://pubmed.ncbi.nlm.nih.gov/29404396/) | 2018 | Commentary | Mol Cell Oncol | Author commentary on the 2017 Nature Medicine CML-OXPHOS study |

None of the above directly studies tyrosine metabolism disorders; all are mechanistically adjacent (mitochondrial/melanocyte metabolism) rather than disease-matched.

---

## Singapore Market Information

Tigecycline is **not currently marketed in Singapore** — no license records are available in the regulatory dataset (0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/manufacturer label warnings and contraindications are a **blocking data gap (DG001)** — this must be resolved before any S1 safety review can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction ("disorder of tyrosine metabolism") is not supported by matching evidence — the sole clinical trial and most literature actually pertain to CML and mitochondrial OXPHOS biology, indicating a probable disease-label mismatch rather than a genuine repurposing signal. Combined with the drug not being marketed in Singapore and a blocking safety-data gap, evidence is insufficient to advance.

**To proceed, the following is needed:**
- Verify/correct the disease ontology mapping behind this TxGNN prediction (label-mismatch investigation)
- Obtain tigecycline's original MOA (DG002) and TFDA/manufacturer label warnings & contraindications (DG001, blocking)
- If pursuing a genuine mitochondrial-OXPHOS repurposing hypothesis, consider evaluating **monoclonal gammopathy** (rank 10 in this evidence pack), which has two in vitro myeloma studies with a mechanistically consistent rationale (evidence level L4, "Research Question")
- Confirm regulatory pathway status, given the drug is not currently registered in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

