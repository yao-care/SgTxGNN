---
layout: default
title: Hesperidin
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Hesperidin
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

# Hesperidin: From Natural Citrus Flavonoid to Myeloproliferative Neoplasm

## One-Sentence Summary

Hesperidin is a naturally occurring flavonoid glycoside abundant in citrus fruits, traditionally used as a dietary supplement with antioxidant and anti-inflammatory properties rather than as a formally approved pharmaceutical agent.
The TxGNN model predicts it may be effective for **Myeloproliferative Neoplasm (MPN)**,
with **0 clinical trials** and **2 publications** currently supporting this direction — both at the preclinical (in silico / in vitro) stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formally registered indication; Hesperidin is a naturally occurring citrus bioflavonoid supplement |
| Predicted New Indication | Myeloproliferative Neoplasm |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L4 (preclinical studies: in silico molecular docking + in vitro cell assays) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for Hesperidin (DB04703). Based on known information from the literature, Hesperidin is a flavanone glycoside (flavonoid class) derived from citrus fruits. After oral ingestion, gut microbiota cleave its rutinoside sugar moiety at the C7 position, converting it to its active aglycone **Hesperetin**, which exhibits superior membrane permeability and biological activity. This metabolic activation step is pharmacologically critical — the glycosylated parent compound (Hesperidin) itself has attenuated pro-apoptotic activity compared to Hesperetin.

Myeloproliferative neoplasms are clonal hematopoietic stem cell disorders driven by constitutively activated tyrosine kinases (notably BCR-ABL in CML, JAK2-V617F in PV/ET/MF). The TxGNN prediction is mechanistically grounded by one in silico study (PMID 31759365) demonstrating that Hesperidin can dock into the ATP-binding pocket of the BCR kinase domain, occupying the same region as imatinib despite a structurally distinct scaffold — suggesting potential as a natural BCR kinase inhibitor with a different resistance profile. A complementary in vitro study (PMID 40751800) shows that Hesperetin (Hesperidin's active metabolite) modulates membrane progesterone receptor expression and reduces ROS in myeloid leukemia cells, addressing the oxidative stress that contributes to CML disease progression and drug resistance.

The biological plausibility is further bolstered by broader mechanistic evidence from related myeloid leukemia research: Hesperidin has been shown to downregulate Mcl-1 (an anti-apoptotic BCL-2 family protein overexpressed in MPN), activate the mitochondrial intrinsic apoptosis pathway (cytochrome c release, caspase-3/9 activation), and exhibit synergistic activity with standard AML agents (cytarabine, azacitidine). However, all evidence remains preclinical, and no MPN-specific in vivo studies or clinical trials have been conducted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Hesperidin in myeloproliferative neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31759365](https://pubmed.ncbi.nlm.nih.gov/31759365/) | 2019 | In Silico | Asian Pacific J Cancer Prev | Molecular docking demonstrates Hesperidin binds the BCR kinase ATP-binding pocket in CML; predicted to inhibit BCR-ABL and Grb-2 (a non-kinase target upstream of BCR-ABL), offering a potential strategy to overcome TKI resistance |
| [40751800](https://pubmed.ncbi.nlm.nih.gov/40751800/) | 2025 | In Vitro | Medical Oncology | Hesperetin (Hesperidin's active metabolite) increases membrane progesterone receptor (mPR) expression and reduces reactive oxygen species (ROS) in human myeloid leukemia cells, addressing oxidative stress-driven disease progression and drug resistance in CML |

---

## Singapore Market Information

Hesperidin (DB04703) is **not registered** in Singapore. No marketing authorisations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data, warnings, or contraindications are currently available in the Evidence Pack for Hesperidin.

> **Note:** Hesperidin is widely consumed as a dietary supplement with a generally favourable safety profile. However, pharmaceutical-grade safety data (formal contraindications, interactions with anticoagulants, haematological toxicity at therapeutic doses) have not been systematically compiled for this candidate. This represents a critical data gap before any clinical development consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Hesperidin in myeloproliferative neoplasm is limited to two preclinical studies (L4) — one in silico docking study and one in vitro cell study using Hesperetin (the active metabolite, not Hesperidin itself) — with no clinical trials registered globally. Additionally, Hesperidin is not marketed in Singapore, and all safety data is absent, meeting criteria for a "Hold" pending foundational research.

**To proceed, the following is needed:**

- **MOA clarification**: Confirm whether the pharmacologically active species in vivo is Hesperidin or its gut-derived metabolite Hesperetin, as the C7-rutinoside attenuates apoptotic activity; reformulation as Hesperetin may be more appropriate
- **In vivo proof-of-concept**: Mouse xenograft or MPN transgenic model (e.g., JAK2-V617F knock-in) studies to confirm anti-MPN efficacy at pharmacologically achievable concentrations
- **BCR kinase inhibition validation**: Biochemical kinase assay to confirm Hesperidin/Hesperetin IC₅₀ against BCR-ABL, and selectivity panel vs. other kinases
- **Pharmacokinetic profiling**: Oral bioavailability data, plasma concentration achievable at the doses required for anti-tumour effect vs. dietary supplement levels
- **Safety dossier**: TFDA package insert review, formal DDI assessment (particularly with anticoagulants and CYP3A4 substrates), and haematological toxicity data
- **Formulation strategy**: If Hesperetin is confirmed as the active species, a decision on whether to develop Hesperidin (as a prodrug) or Hesperetin directly as the clinical candidate is needed

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

