---
layout: default
title: Dapagliflozin
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Dapagliflozin
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

# Dapagliflozin: From Type 2 Diabetes / Heart Failure to Focal Stiff Limb Syndrome

## One-Sentence Summary

Dapagliflozin is a well-established SGLT2 (sodium-glucose cotransporter 2) inhibitor, globally approved for type 2 diabetes, heart failure with reduced ejection fraction, and chronic kidney disease, though it currently holds no Singapore HSA registration in this evidence pack.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**,
however there are **0 clinical trials** and **0 publications** directly supporting this direction — the prediction rests entirely on knowledge graph topology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore (HSA) registration on file; globally approved for T2DM / HFrEF / CKD |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Dapagliflozin is an SGLT2 inhibitor that reduces renal glucose reabsorption, induces glucosuria, and secondarily activates AMPK and exerts anti-inflammatory effects (NF-κB and NLRP3 inflammasome inhibition). These systemic metabolic and anti-inflammatory properties form the basis of its cardiovascular and renal protective effects.

Focal stiff limb syndrome sits within the stiff-person syndrome (SPS) spectrum. Its core pathology involves anti-GAD65 antibody-mediated loss of GABAergic inhibition in the spinal cord, resulting in persistent motor neuron excitation and painful muscle rigidity. This autoimmune-neurological mechanism has no known direct intersection with SGLT2 inhibition, AMPK activation, or the glucosuria pathway.

The biological plausibility of this pairing is therefore **extremely weak**. The TxGNN score of 98.20% most likely reflects indirect topological proximity in the knowledge graph — for instance, shared autoimmune or metabolic nodes — rather than a direct mechanistic link. No supporting clinical or preclinical experimental data exists to change this assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome.

---

## Singapore Market Information

Dapagliflozin currently has **no HSA-registered products** on file in this evidence pack. No authorisation table can be generated.

> Note: Dapagliflozin (brand names Farxiga / Forxiga) holds regulatory approvals in the United States (FDA), European Union (EMA), and numerous other markets. Singapore HSA registration data should be verified directly via the HSA Product Database.

---

## Safety Considerations

Please refer to the package insert for safety information. Complete Singapore regulatory safety data (key warnings, contraindications, drug interactions) was not available in this evidence pack and constitutes a blocking data gap before any further evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numerical score (98.20%) to focal stiff limb syndrome, but this is an artifact of knowledge graph topology rather than biological specificity. The pathology (anti-GAD65-mediated GABAergic deficit) has no known mechanistic intersection with SGLT2 inhibition, there are zero supporting clinical trials or publications, and the drug is not registered in Singapore. All evidence criteria for advancement are unmet.

**To proceed, the following is needed:**

- **Mechanistic evidence:** Identify any experimental (in vitro / in vivo) data linking SGLT2 inhibition or AMPK activation to GABAergic pathways or anti-GAD65 autoimmunity before reconsidering this pairing
- **Singapore regulatory baseline:** Confirm HSA registration status directly; obtain the full prescribing information (package insert) to complete the blocking safety gap (DG001)
- **DrugBank MOA data:** Retrieve the complete mechanism of action from DrugBank API (DG002) to enable a proper mechanistic linkage analysis
- **Disease re-prioritisation:** Consider evaluating higher-plausibility Dapagliflozin repurposing candidates from the same TxGNN output — the lipodystrophy cluster (ranks 5–8) has a modestly stronger AMPK/lipid metabolism rationale, and the pancreatic agenesis entry (rank 9) has at least one supporting animal study (PMID [33559163](https://pubmed.ncbi.nlm.nih.gov/33559163/)) worth closer review
- **Clinical feasibility assessment:** If any candidate advances past S0, a Singapore-specific patient population estimate and route-of-administration compatibility check (oral tablet vs. required delivery) should be completed

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application. Predictions generated by TxGNN are hypothesis-generating and must be interpreted in the context of available clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

