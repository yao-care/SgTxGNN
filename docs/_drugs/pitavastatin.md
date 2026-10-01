---
layout: default
title: Pitavastatin
parent: Medium Evidence (L3-L4)
nav_order: 793
evidence_level: L4
indication_count: 10
---

# Pitavastatin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pitavastatin: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pitavastatin is a statin (HMG-CoA reductase inhibitor) marketed in Singapore as Livalo for lowering cholesterol.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**, but **no clinical trials** and only **2 publications** are linked, and neither directly supports this use.
The high model score reflects proximity in the knowledge graph, not clinical proof.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA licence records (pitavastatin is a statin used for primary hyperlipidemia/dyslipidemia) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Pitavastatin inhibits HMG-CoA reductase, the rate-limiting enzyme in cholesterol synthesis. This lowers LDL-C mainly by upregulating LDL receptors (LDLR) in the liver. Cholesterol-lowering is its established use, and HoFH is a severe form of the same problem (very high LDL-C), so the model links the two.

The mechanism also explains the limits. HoFH involves severe loss of LDLR function, and statins depend on residual receptor activity. Response is therefore expected to be limited, especially in patients with null/null genotypes. The two linked papers do not close this gap (see below), and the pack does not include detailed mechanism-of-action data from DrugBank.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (Phase 4, INTREPID) | The Lancet HIV | Pitavastatin vs pravastatin in adults with HIV-1 and dyslipidaemia. Population mismatch: not an HoFH study. |
| [39532566](https://pubmed.ncbi.nlm.nih.gov/39532566/) | 2025 | Case report | Journal of Clinical Lipidology | Rapid lipid-lowering response in two cases of autosomal recessive hypercholesterolemia (LDLRAP1 variants), a phenotype clinically similar to HoFH. Only two patients, and not HoFH itself. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15859P | LIVALO Film-Coated Tablets 2 mg (Kowa Company, Ltd., Nagoya Factory) | Tablet, film coated | Not stated in the record |
| SIN15860P | LIVALO Film-Coated Tablets 4 mg (Kowa Company, Ltd., Nagoya Factory) | Tablet, film coated | Not stated in the record |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug in the pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials exist for HoFH. The two linked papers are an HIV dyslipidaemia RCT and a two-patient case report of a related recessive condition. The mechanism suggests limited benefit when LDL receptor function is severely lost. The 99.996% score reflects graph proximity, not clinical evidence.

**To proceed, the following is needed:**
- HoFH-specific clinical data, ideally stratified by LDLR genotype (residual receptor activity vs null/null)
- The current HSA package insert (warnings, contraindications, approved indications)
- Detailed mechanism-of-action data from DrugBank
- Evidence-based context from other predicted indications for this drug: cardiovascular prevention in people with HIV (REPRIEVE, a completed Phase 3 trial in 7,769 participants) and heterozygous familial hypercholesterolemia have much stronger support than HoFH
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

