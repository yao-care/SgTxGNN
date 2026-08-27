---
layout: default
title: Methionine
parent: 僅模型預測 (L5)
nav_order: 650
evidence_level: L5
indication_count: 10
---

# Methionine
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

# Methionine: From No Registered Indication to Predicted Acne (Disease) Treatment

## One-Sentence Summary

> Methionine's original approved indication is not documented in this Evidence Pack — the drug currently holds **no marketing registration in Singapore**, and both its original indication list and mechanism of action are recorded as data gaps.
> The TxGNN model predicts it may be effective for **Acne (disease)**, with a prediction score of **99.9996%**,
> but this is currently supported only by **0 clinical trials** and **4 publications**, all indirect or observational in nature, placing the evidence level at **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore registration on file; `original_moa` and `original_indications` are both data gaps |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

> **Note on alternative candidates**: Acne ranks #1 by TxGNN score but has the *weakest* literature support of the top-10 predictions. Several lower-ranked candidates — **cortical cataract** (#6), **nuclear senile cataract** (#7), **mature cataract** (#9), and **diabetic cataract** (#10) — carry a higher Evidence Level (**L4**, decision stage "Research Question") because they are backed by mechanistic literature directly involving methionine's biochemistry (transsulfuration, glutathione synthesis, methionine sulfoxide reductase). These may be more scientifically promising research directions than the top-ranked acne signal, even though their raw TxGNN scores are marginally lower.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Methionine is not available, and no original approved indication is on file for this product in the Singapore regulatory dataset. This means the standard "original MOA → new indication" bridging argument cannot be constructed from registration data alone.

For the top-ranked prediction, **acne (disease)**, the supporting literature does not describe a direct mechanistic link between methionine and acne. The four retrieved publications instead show: (1) elevated homocysteine — a downstream product of methionine metabolism — in patients undergoing isotretinoin therapy for cystic acne; (2) a case report of an MTHFR mutation (an enzyme in the methionine/homocysteine pathway) presenting with neonatal acne among other findings; and (3–4) case studies of neutrophil/chemotactic activity in acne-related inflammatory skin conditions. None of these directly test or observe methionine's effect on acne pathophysiology — the association is indirect, drawn largely from shared metabolic pathway involvement rather than an interventional or observational signal on the drug itself.

By contrast, several lower-ranked predictions have a clearer biochemical rationale: methionine is a precursor for S-adenosylmethionine (SAM), homocysteine, cysteine, and ultimately glutathione (GSH) — a key antioxidant in the eye lens. Literature associated with **cortical cataract**, **nuclear senile cataract**, **mature cataract**, and **diabetic cataract** consistently shows that methionine oxidation, GSH depletion, and methionine sulfoxide reductase (MsrB1) activity are involved in lens crystallin damage and cataract formation. This is mechanistically coherent with methionine's known biochemical role, though all such evidence currently derives from animal, in vitro, or ex vivo human tissue models — none from human interventional trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Evidence below is for the top-ranked predicted indication, **acne (disease)**.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort/Observational | International Journal of Dermatology | Elevated plasma homocysteine (a downstream methionine metabolite) observed in cystic acne patients on isotretinoin therapy |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Reports | Neonate with MTHFR mutation (methionine/homocysteine pathway enzyme) presenting with neonatal acne, hair loss, and marfanoid features |
| [3859500](https://pubmed.ncbi.nlm.nih.gov/3859500/) | 1985 | Case study | Journal of the American Academy of Dermatology | Increased plasma chemoattractant activity in a patient with Sweet's syndrome and cystonodular acne |
| [3161955](https://pubmed.ncbi.nlm.nih.gov/3161955/) | 1985 | Clinical/laboratory study | Journal of Investigative Dermatology | Neutrophil chemotactic/functional changes studied across infectious and inflammatory skin diseases, including acne conglobata |

---

## Singapore Market Information

Methionine currently has **no marketing authorization on file in Singapore** (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No product registration table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (acne) is supported only by indirect, low-tier literature (case reports and observational studies on downstream metabolites, not methionine itself) with zero clinical trials — an evidence level of L5. Combined with the fact that Methionine has no current Singapore marketing registration and both its original indication and mechanism of action are unresolved data gaps, there is not yet sufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Resolution of the blocking data gap (DG001): TFDA/HSA package insert warnings and contraindications, required before any safety (S1) evaluation can begin
- Resolution of the mechanism-of-action data gap (DG002) via DrugBank API query, to properly assess mechanistic plausibility
- Documentation of Methionine's original approved indication(s), currently absent from the registry data
- Direct interventional or observational studies linking methionine specifically to acne, rather than inference from shared metabolic pathways
- If prioritizing scientific plausibility over raw TxGNN score, consider evaluating the cataract-related candidates (ranks #6, #7, #9, #10) instead, though these would require translation from current animal/in vitro evidence (L4) toward human clinical data before advancing further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

