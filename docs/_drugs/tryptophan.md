---
layout: default
title: Tryptophan
parent: 僅模型預測 (L5)
nav_order: 1024
evidence_level: L5
indication_count: 10
---

# Tryptophan
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

# Tryptophan: From Nutritional Amino Acid to Restless Legs Syndrome

## One-Sentence Summary

Tryptophan is an essential amino acid and metabolic precursor of serotonin; it has no approved drug indication on record in this evidence pack and is not currently marketed in Singapore. The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)**, but this direction is currently supported only by **0 registered clinical trials** and **8 publications**, most of which are decades-old, small, or indirect (associational) rather than confirmatory treatment trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered as a drug indication; historically used as a nutritional/dietary amino acid supplement |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for tryptophan is not available in this evidence pack (Data Gap DG002). Based on general pharmacology, tryptophan is the metabolic precursor of serotonin (5-HT), and downstream of that, melatonin. It has no formally registered therapeutic indication in the source data used here — it is generally used as a dietary/nutritional amino acid rather than an approved drug product, which is also consistent with its "not marketed" status in Singapore.

The mechanistic rationale for RLS is that the serotonergic system interacts with the dopaminergic system, and dopaminergic dysfunction is a well-established feature of RLS pathophysiology (dopamine agonists are a mainstay RLS treatment). A small direct treatment study of L-tryptophan in RLS was published as early as 1986, but the evidence base has not been meaningfully updated since — no modern, adequately powered, or controlled trial has re-tested this hypothesis. This makes the biological plausibility reasonable, but the clinical evidence remains dated and thin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3659737](https://pubmed.ncbi.nlm.nih.gov/3659737/) | 1987 | Comparative study | Sleep | Compared L-dopa, 5-hydroxytryptophan, and L-tryptophan effects on periodic leg movements |
| [3953904](https://pubmed.ncbi.nlm.nih.gov/3953904/) | 1986 | Open-label/small trial | Am J Psychiatry | Direct treatment study of L-tryptophan in restless legs syndrome |
| [33836477](https://pubmed.ncbi.nlm.nih.gov/33836477/) | 2021 | Systematic review | Sleep Medicine Reviews | RLS is common in chronic liver disease, potentially linked to elevated tryptophan, histamine, and altered dopamine turnover; associational, not treatment evidence |
| [1305630](https://pubmed.ncbi.nlm.nih.gov/1305630/) | 1992 | Review | Int J Neuroscience | Reviews serotonin's role across CNS functions, including motor behavior relevant to movement disorders |
| [2881477](https://pubmed.ncbi.nlm.nih.gov/2881477/) | 1987 | Review | Am Fam Physician | General review of insomnia diagnosis/treatment; not RLS-specific |
| [32546134](https://pubmed.ncbi.nlm.nih.gov/32546134/) | 2020 | Postmarketing pharmacovigilance | BMC Psychiatry | Evaluates antidepressant-associated movement disorders; not a direct tryptophan study |
| [1777530](https://pubmed.ncbi.nlm.nih.gov/1777530/) | 1991 | Case report | Biological Psychiatry | Describes lithium-induced RLS; indirect relevance to serotonergic/dopaminergic mechanism |
| [36897462](https://pubmed.ncbi.nlm.nih.gov/36897462/) | 2023 | Case report | Neurological Sciences | RLS in DNAJC12 deficiency, a genetic disorder impairing dopaminergic/serotoninergic neurotransmission |

---

## Singapore Market Information

Tryptophan currently has **no marketing authorization** on record in Singapore (0 registrations). No product license, dosage form, or approved indication data is available.

---

## Safety Considerations

**Historical Safety Signal:** In 1989, contaminated L-tryptophan dietary supplements were associated with Eosinophilia-Myalgia Syndrome (EMS), a serious systemic illness with reported fatalities, attributed to manufacturing impurities rather than tryptophan itself (documented in registry record NCT00001918). This underscores the importance of pharmaceutical-grade purity and manufacturing quality control for any therapeutic use of tryptophan.

Formal drug interaction, contraindication, and warning data could not be retrieved for this evidence pack (Data Gap DG001). Please refer to the package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RLS signal rests on one small, non-randomized 1986 human study and otherwise indirect/associational or case-level literature, with no active or completed modern clinical trials. Evidence level (L3) does not yet support proceeding to development or guardrail-based deployment.

**To proceed, the following is needed:**
- A modern, adequately powered RCT to re-test L-tryptophan's efficacy in RLS
- Mechanism of action (MOA) data (DG002)
- TFDA/HSA-equivalent label warnings and contraindications (DG001)
- A regulatory pathway assessment, since tryptophan currently has no marketing authorization in Singapore
- A manufacturing/purity quality plan addressing the 1989 EMS precedent before any clinical use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

