---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Denosumab
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

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a fully human monoclonal antibody targeting RANKL, approved internationally for osteoporosis, bone loss associated with cancer treatment, and bone metastases.
The TxGNN model's highest-ranked prediction (score 99.63%) is **Severe Nonproliferative Diabetic Retinopathy**, followed by diabetic retinopathy, dermatitis, and diabetic cataract.
However, **no clinical trials and no published literature** directly support the top-ranked indication, placing it at evidence level L5 — prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis; bone loss due to cancer treatment; bone metastases; giant cell tumour of bone |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Denosumab is a fully human IgG2 monoclonal antibody that binds and neutralises RANKL (Receptor Activator of Nuclear Factor kappa-B Ligand) — a cytokine essential for osteoclast differentiation, function, and survival. By blocking RANKL, Denosumab effectively reduces bone resorption. This mechanism underpins its approved uses in osteoporosis, cancer treatment-induced bone loss, bone metastases, and giant cell tumour of bone.

The theoretical link to severe nonproliferative diabetic retinopathy (NPDR) rests on RANKL's potential role in retinal microvascular biology. RANKL signalling has been identified in retinal pericytes and Müller cells, where it may participate in inflammatory signalling and microvascular integrity. Separately, a 2024 real-world cohort study with meta-analysis (PMID 38899553) reported that Denosumab use was associated with a reduced incidence of type 2 diabetes and its microvascular complications — providing an indirect upstream biological rationale.

However, this connection is purely speculative for the severe NPDR indication specifically. The high TxGNN score reflects topological proximity within the knowledge graph, not direct clinical or experimental evidence. No preclinical model, observational study, or clinical trial has tested Denosumab for this indication. The prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

---

## Literature Evidence

Currently no related literature available for severe nonproliferative diabetic retinopathy.

---

## Singapore Market Information

Denosumab is currently **not marketed in Singapore** (0 HSA registrations). No product authorisation data is available.

> **Note for reviewers:** Denosumab is marketed globally under two brand names — **Prolia** (osteoporosis, 60 mg/mL SC every 6 months) and **Xgeva** (oncology indications, 120 mg/1.7 mL SC every 4 weeks). Neither has an HSA registration as of the data cut-off date. Regulatory pathway assessment will be required should any repurposing candidate advance to clinical evaluation in Singapore.

---

## Cytotoxicity

Denosumab is used in oncology for prevention of skeletal-related events from bone metastases and for treatment of unresectable giant cell tumour of bone. It is classified as a targeted biological therapy, not a conventional cytotoxic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — anti-RANKL monoclonal antibody (IgG2); not a cytotoxic chemotherapy agent |
| Myelosuppression Risk | Low (RANKL inhibition does not directly suppress haematopoiesis; monitor for hypocalcaemia and infection risk) |
| Emetogenicity Classification | Minimal (subcutaneous administration; not associated with significant chemotherapy-induced nausea/vomiting) |
| Monitoring Items | Serum calcium and phosphate (hypocalcaemia is the most common adverse effect); renal function; dental examination prior to initiation; CBC if used in combination regimens |
| Handling Protection | Standard biologic handling applies; no cytotoxic drug special handling requirements |

---

## Safety Considerations

Safety data (warnings, contraindications, and drug interactions) are not available in this Evidence Pack. Please refer to the official product package insert (Prolia or Xgeva) for full safety information.

> **Known safety signals from retrieved literature:** The dermatitis-related literature (see Indication Rank 3) documents several cutaneous adverse events attributed to Denosumab, including Acute Generalised Exanthematous Pustulosis (AGEP), DRESS syndrome, lichenoid drug eruption, c-ANCA vasculitis, and erythema nodosum. These are rare but clinically significant. Any repurposing proposal should account for these immune-mediated risks, particularly for indications involving inflammatory or autoimmune dermatological conditions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.63%), the complete absence of clinical trials, preclinical studies, and published literature for Denosumab in severe nonproliferative diabetic retinopathy makes advancement impossible at this stage. This is a pure model-derived hypothesis with no independent evidence base.

**To proceed, the following is needed:**

- **Preclinical proof of concept:** In vitro and in vivo (rodent model) studies evaluating RANKL/RANK expression in retinal pericytes and Müller cells under hyperglycaemic conditions, and the effect of RANKL inhibition on retinal microvascular integrity
- **Mechanistic clarification:** Full MOA data from DrugBank to confirm biological plausibility; determine whether RANKL inhibition has protective or detrimental effects on retinal vasculature (given observed paradoxical immune effects in skin)
- **Epidemiological signal validation:** Deeper analysis of PMID 38899553 to determine whether the reported reduction in microvascular complications specifically includes retinopathy endpoints, and whether this extends to the severe NPDR subgroup
- **Safety baseline:** Obtain official prescribing information (Prolia/Xgeva package inserts) to characterise known adverse effects in diabetic patients; assess risk of hypocalcaemia in patients with T2DM and renal impairment
- **Singapore regulatory pathway:** Denosumab has no HSA registration; a parallel regulatory strategy (new indication application or compassionate use framework) would need to be mapped if clinical development is pursued
- **Evidence re-assessment trigger:** If a preclinical study demonstrates retinal pericyte protection via RANKL inhibition, this candidate should be re-evaluated at that time to potentially upgrade from Hold to Research Question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

