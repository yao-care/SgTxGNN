---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
---

# Ipilimumab
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

# Ipilimumab: From Melanoma to Choroideremia

## One-Sentence Summary

Ipilimumab (Yervoy) is an anti-CTLA-4 monoclonal antibody checkpoint inhibitor, globally approved for the treatment of unresectable or metastatic melanoma and other cancers.
The TxGNN model ranks **Choroideremia** as its top predicted new indication with a prediction score of 99.06%; however, **no clinical trials or literature** currently support this direction.
This prediction is assessed as a likely **model false positive** — choroideremia is an X-linked genetic retinal dystrophy with no plausible immunological connection to anti-CTLA-4 mechanisms.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Melanoma (globally approved; not registered in Singapore) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known clinical information, Ipilimumab is an anti-CTLA-4 monoclonal antibody that blocks the CTLA-4/B7 co-inhibitory interaction, releasing the brake on T-cell activation and amplifying anti-tumour immune responses. It is globally approved for unresectable or metastatic melanoma (cutaneous, uveal, and mucosal subtypes), non-small cell lung cancer, renal cell carcinoma, and several other indications — most often in combination with nivolumab (anti-PD-1).

Choroideremia, by contrast, is an X-linked recessive inherited retinal dystrophy caused by loss-of-function mutations in the *CHM* gene, resulting in deficiency of Rab escort protein-1 (REP-1). Disease progression is driven by progressive photoreceptor and retinal pigment epithelium degeneration — a purely genetic, non-immune-mediated process. Anti-CTLA-4 blockade has no known mechanistic target relevant to REP-1 deficiency, Rab GTPase trafficking dysfunction, or photoreceptor apoptosis.

The TxGNN score of 0.9906 for choroideremia is almost certainly a **model false positive**, most likely arising from knowledge-graph structural artefacts or cross-disease embedding overlap. This interpretation is strongly supported by the fact that all nine remaining top-ranked predictions (ranks 2–10) are melanoma subtypes — a biologically coherent cluster entirely consistent with Ipilimumab's known pharmacology — making the rank-1 choroideremia prediction an anomalous outlier.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ipilimumab in Choroideremia.

---

## Literature Evidence

Currently no related literature available for Ipilimumab in Choroideremia.

---

## Singapore Market Information

Ipilimumab has no products registered with the Health Sciences Authority (HSA) in Singapore and is currently not marketed locally. Clinicians requiring access would need to apply through the HSA's Special Access Route (SAR) or similar compassionate-use pathway.

---

## Cytotoxicity

Ipilimumab is an antineoplastic agent (immunotherapy class). The cytotoxicity profile differs fundamentally from conventional chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Anti-CTLA-4 checkpoint inhibitor (IgG1κ monoclonal antibody) |
| Myelosuppression Risk | Low (not a myelosuppressive agent; immune-related haematological events are rare but possible) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (ALT, AST, bilirubin), thyroid function (TSH, free T4), adrenal function (cortisol, ACTH), CBC with differential, renal function, blood glucose; routine immune-related adverse event (irAE) surveillance |
| Handling Protection | Standard monoclonal antibody/biological handling procedures; dedicated cytotoxic drug handling regulations not typically required, but institutional policies should be followed |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Ipilimumab carries well-characterised immune-related adverse events (irAEs) including immune-mediated colitis, hepatitis, dermatitis, endocrinopathies (hypophysitis, thyroiditis, adrenal insufficiency), and pneumonitis, which may be severe or fatal. Full prescribing information and REMS/risk minimisation materials (e.g., YERVOY Risk Minimisation Tools, NCT02224768) should be reviewed before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 TxGNN prediction of choroideremia for Ipilimumab is mechanistically implausible and unsupported by any clinical trial or published literature; this prediction should not be advanced as a drug repurposing candidate.

**To proceed, the following is needed:**

- **Shift evaluation focus to rank-2 indication (Non-Cutaneous Melanoma):** This indication carries L2 evidence, 50+ clinical trials, 5 publications, and a "Proceed with Guardrails" recommendation — representing a far more actionable and biologically coherent target for repurposing review.
- **Obtain MOA data from DrugBank:** Query DrugBank API for DB06186 to complete the mechanism-of-action analysis and enable full mechanistic link scoring.
- **Obtain Singapore-specific safety information:** As the drug is unregistered in Singapore, download the EMA/FDA package insert for Ipilimumab and review key warnings, contraindications, and monitoring requirements prior to any clinical evaluation.
- **No further investigation of choroideremia** as a repurposing target is recommended unless novel immune-mediated pathophysiology specific to this disease is identified and validated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

