---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 693
evidence_level: L5
indication_count: 10
---

# Natalizumab
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab is a monoclonal antibody that blocks α4-integrin (VLA-4) to inhibit leukocyte migration across the blood-brain barrier; literature in this evidence pack repeatedly documents its established use in relapsing-remitting multiple sclerosis (and, per one review, Crohn's disease), though structured original-indication data was not provided for this candidate. The TxGNN model predicts a possible new indication of **Bronchitis**, but this is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (relapsing-remitting), inferred from literature evidence in this pack — structured field not available |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap for this candidate (DG002, High severity). Based on information embedded elsewhere in this evidence pack, natalizumab is a humanized monoclonal antibody that blocks α4-integrin (VLA-4), inhibiting leukocyte trans-endothelial migration — a mechanism relevant to autoimmune/inflammatory conditions such as multiple sclerosis and Crohn's disease.

For bronchitis specifically, no mechanistic rationale connecting α4-integrin blockade to the infectious/inflammatory pathways of bronchitis is described in the evidence pack, and no clinical trial or literature evidence exists for this pairing. The prediction rationale explicitly states this is a pure model score with no supporting mechanistic or empirical basis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Natalizumab currently has no marketing authorization on file in Singapore (0 licenses; market status: Not Marketed).

## Safety Considerations

Structured safety fields (key warnings, contraindications, drug interactions) are not available for this candidate (see meta.data_gaps DG001, Blocking severity — TFDA/HSA label data required before this candidate can enter safety pre-screening).

Separately, literature attached to other predicted indications for this same drug in this evidence pack repeatedly and consistently flags progressive multifocal leukoencephalopathy (PML), a serious JC virus–related CNS infection, as a known risk associated with natalizumab (e.g., PMID [20298966](https://pubmed.ncbi.nlm.nih.gov/20298966/), [19647202](https://pubmed.ncbi.nlm.nih.gov/19647202/), [24136456](https://pubmed.ncbi.nlm.nih.gov/24136456/)), along with infusion hypersensitivity and delayed allergic reactions (PMID [17846274](https://pubmed.ncbi.nlm.nih.gov/17846274/), [18541818](https://pubmed.ncbi.nlm.nih.gov/18541818/)). These signals are not specific to the bronchitis indication under review here but are material context for any repurposing decision involving this molecule.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (bronchitis) has zero supporting clinical trials or literature and no described mechanistic link — it is a model-score-only (L5) signal. Combined with the Blocking-severity data gap on TFDA/HSA label information (DG001) and missing original-indication/MOA data, this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) to close Blocking gap DG001
- Confirmed original indication(s) and MOA via DrugBank API (DG002)
- Primary literature or trial data specifically evaluating natalizumab in bronchitis (none currently exists)
- If pursuing repurposing for this drug at all, consider that other candidates in the same output (e.g., dermatitis, psoriasis) have more literature volume but the evidence direction is largely adverse-reaction-driven (drug-induced psoriasis/dermatitis, PML), not therapeutic — these would need separate, dedicated review rather than being treated as supportive of repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

