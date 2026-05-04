---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Merkel Cell Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab is an anti-PD-L1 monoclonal antibody checkpoint inhibitor, approved internationally for Merkel cell carcinoma and urothelial carcinoma maintenance therapy.
The TxGNN model predicts it may be effective for **Human Herpesvirus 8 (HHV-8)-Related Tumors** (including Kaposi sarcoma and primary effusion lymphoma),
with **0 clinical trials** and **0 publications** in the current evidence pack supporting this specific direction — this remains a model-generated hypothesis only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Merkel cell carcinoma; urothelial carcinoma (first-line maintenance) *(Note: original_indications field is empty in source data; based on known international approvals)* |
| Predicted New Indication | Human Herpesvirus 8-Related Tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Avelumab is a fully human IgG1 anti-PD-L1 monoclonal antibody. By blocking PD-L1 on tumour cells, it prevents the PD-1/PD-L1 interaction that suppresses cytotoxic T cells, thereby restoring the immune system's ability to recognize and destroy cancer cells. Notably, as an IgG1 antibody, Avelumab also retains the ability to induce antibody-dependent cellular cytotoxicity (ADCC), which distinguishes it mechanistically from other checkpoint inhibitors.

HHV-8 causes oncogenesis primarily through viral proteins that upregulate cellular PD-L1 expression — particularly in Kaposi sarcoma (KS) and primary effusion lymphoma (PEL). This PD-L1 upregulation is a key mechanism by which HHV-8-infected tumour cells evade immune surveillance. On this basis, blocking PD-L1 with Avelumab is mechanistically plausible: restoring T-cell cytotoxicity against virus-transformed cells is conceptually sound.

The analogy to Merkel cell carcinoma (MCC) — Avelumab's primary approved indication — provides additional support. MCC is a virus-associated (Merkel cell polyomavirus) neuroendocrine skin tumour that also relies on PD-L1-mediated immune evasion, and checkpoint inhibition has proven highly effective. HHV-8-associated malignancies share this virus-driven, PD-L1-dependent immune escape biology, making the TxGNN prediction biologically coherent. However, it should be noted that the MOA data field is listed as a data gap in the source pack, and the connection currently rests on known pharmacology rather than data formally submitted to this pipeline.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Avelumab in human herpesvirus 8-related tumor.

> **Note:** External literature outside this evidence pack contains preliminary case reports on checkpoint inhibitors (including PD-1/PD-L1 blockade) in Kaposi sarcoma. A targeted PubMed search is recommended to supplement this gap before advancing to any decision stage.

---

## Literature Evidence

Currently no related literature available within this evidence pack for Avelumab in human herpesvirus 8-related tumor.

---

## Singapore Market Information

Avelumab has **no Singapore Health Sciences Authority (HSA) registrations**. The drug is not marketed in Singapore as of the data cutoff (2026-04-05).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| — | — | — | No registrations found |

---

## Cytotoxicity

Avelumab is an antineoplastic agent (immunotherapy class). The following applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Checkpoint inhibitor (anti-PD-L1 IgG1 monoclonal antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (direct myelosuppression is not a primary toxicity; immune-mediated haematological events such as immune thrombocytopenia are possible but uncommon) |
| Emetogenicity Classification | Minimal to low |
| Monitoring Items | CBC with differential; liver function tests (ALT, AST, bilirubin); thyroid function (TSH, free T4); renal function; blood glucose; adrenal function if clinically indicated; infusion reaction monitoring during administration |
| Handling Protection | Standard biologic/monoclonal antibody handling protocols apply; does not require cytotoxic chemotherapy-level containment procedures, but facility-specific biosafety guidelines for IV administration should be followed |

---

## Safety Considerations

Detailed TFDA package insert warnings and contraindications were not available in this evidence pack (Data Gap DG001). Known class-level safety considerations for PD-L1 checkpoint inhibitors include:

- **Immune-Related Adverse Events (irAEs):** Pneumonitis, colitis, hepatitis, endocrinopathies (thyroiditis, adrenal insufficiency, hypophysitis), nephritis, and dermatitis — any of which can be severe or life-threatening
- **Infusion-Related Reactions:** Premedication with antihistamine and paracetamol is recommended prior to the first four infusions
- **Special Populations:** Use in patients with active autoimmune disease, immunodeficiency, or those on systemic immunosuppressants requires individual risk-benefit assessment

Please refer to the full Bavencio® (Avelumab) international prescribing information for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.97%) driven by a mechanistically coherent hypothesis — HHV-8-driven PD-L1 upregulation as a target for Avelumab — but no clinical trials or peer-reviewed literature have been retrieved in this evidence pack to support advancement. This is a pure model-generated signal (Evidence Level L5) requiring hypothesis validation before any clinical or regulatory pathway can be considered.

**To proceed, the following is needed:**

- **Targeted PubMed search:** Search for case reports, retrospective series, or proof-of-concept studies on PD-1/PD-L1 checkpoint inhibitors in Kaposi sarcoma and primary effusion lymphoma (these likely exist outside the current pipeline's capture)
- **MOA data gap resolution (DG002):** Formally retrieve Avelumab's mechanism of action from DrugBank API to strengthen the mechanistic narrative
- **Safety data gap resolution (DG001):** Obtain and parse the TFDA or equivalent package insert PDF to complete the S1 safety screen
- **Singapore regulatory pathway assessment:** Given zero HSA registrations, an independent import/compassionate use or clinical trial IND pathway would be required for any local use
- **PD-L1 expression evidence in HHV-8 tumours:** Identify published biomarker studies confirming PD-L1 expression in Kaposi sarcoma or PEL tumour tissue to strengthen the translational rationale before escalating to Research Question status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

