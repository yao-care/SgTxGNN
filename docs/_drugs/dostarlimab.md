---
layout: default
title: Dostarlimab
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Dostarlimab
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

# Dostarlimab: From Endometrial Cancer to Tendinopathy

## One-Sentence Summary

Dostarlimab (Jemperli) is a humanised monoclonal antibody targeting the PD-1 checkpoint receptor, approved in multiple markets for mismatch repair-deficient (dMMR) / microsatellite instability-high (MSI-H) endometrial cancer and other solid tumours.
The TxGNN model ranks **tendinopathy** as its top predicted new indication, with a prediction score of **50.00%** and a model rank of **#51,903** — placing it near the bottom of all candidate diseases.
There are currently **0 clinical trials** and **0 publications** supporting this direction, and the mechanistic rationale is not only absent but actively contradictory.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mismatch repair-deficient (dMMR) / MSI-H endometrial cancer; dMMR/MSI-H recurrent or advanced solid tumours |
| Predicted New Indication (Rank 1) | Tendinopathy |
| TxGNN Prediction Score | 50.00% (Model Rank #51,903) |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Dostarlimab is a PD-1 (programmed cell death protein 1) checkpoint inhibitor. It works by blocking the interaction between PD-1 on T cells and its ligands (PD-L1/PD-L2) expressed on tumour cells, thereby releasing the immune "brake" and restoring anti-tumour T cell activity. This mechanism of **immune activation** is the cornerstone of its efficacy in dMMR/MSI-H cancers, which are immunologically "hot" tumours with high neoantigen burden.

Tendinopathy is a degenerative or overuse-related structural injury to tendons, with a variable inflammatory component. Importantly, the inflammatory component in tendinopathy — where it exists — is characterised by local tissue remodelling rather than adaptive immune suppression. Releasing PD-1-mediated immune brakes provides no mechanistic pathway to promote tendon healing or reduce degenerative collagen remodelling.

The mechanistic link is not merely absent — it may be harmful. Checkpoint inhibitor-related musculoskeletal immune-related adverse events (irAEs), including inflammatory arthritis and tendinitis, are already well-documented clinical phenomena. This means Dostarlimab's immune-activating mechanism could theoretically **worsen** tendon inflammation rather than treat it. The high model rank (#51,903) and borderline score (50.00%) suggest this is most likely a knowledge graph artefact rather than a biologically grounded prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Dostarlimab has no registered products in Singapore at this time. The drug is therefore not available through local regulatory channels for any indication.

---

## Cytotoxicity

Dostarlimab is an antineoplastic agent (PD-1 immune checkpoint inhibitor). The following summary applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — Checkpoint inhibitor (anti-PD-1 monoclonal antibody); NOT conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low (not a direct myelosuppressive agent; immune-related cytopenias are uncommon but reported as irAEs) |
| Emetogenicity Classification | Minimal (intravenous biological, not classified as emetogenic per MASCC/ESMO guidelines) |
| Monitoring Items | Thyroid function (TSH/free T4), liver enzymes (ALT/AST), renal function (creatinine), blood glucose, full blood count, adrenal function as clinically indicated; monitor for irAEs at each infusion cycle |
| Handling Protection | Biological/monoclonal antibody — standard aseptic preparation required; conventional cytotoxic handling precautions are not mandated, but institutional biohazard protocols for large-volume IV preparations apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Dostarlimab carry L5 evidence (model prediction only, zero supporting clinical trials or publications), and critically, the mechanistic direction of a PD-1 immune activator is **contraindicated or irrelevant** for every predicted disease — including tendinopathy, autoimmune retinopathy, anaphylaxis variants, metabolic disorders, and epilepsy syndromes. The top prediction rank of #51,903 further confirms that the model did not generate confident candidates; these predictions are near the floor of the ranked output and are most likely knowledge graph false-positive connections.

**To proceed, the following is needed:**

- **Mechanistic alignment review**: Any future repurposing screen for Dostarlimab should focus on **immune-suppressed or tumour-immune-evasion** contexts (e.g., autoimmune-associated malignancies, viral oncogenesis), not conditions where immune activation is harmful or irrelevant
- **MOA documentation**: Obtain formal DrugBank MOA record to populate the mechanism field and enable proper mechanistic filtering in the prediction pipeline
- **Singapore regulatory pathway**: Since the drug is not registered in Singapore, any indication expansion would require full HSA registration or a clinical trial import authorisation (CTA)
- **Model calibration signal**: The uniform score of 0.5 across all 10 predicted indications suggests a possible scoring artefact or edge-case in the TxGNN pipeline for this drug — flagging for model team review is recommended
- **irAE risk profile documentation**: Before any exploratory use outside oncology, a comprehensive irAE (immune-related adverse event) risk assessment should be completed, given that many predicted disease contexts (autoimmune conditions, allergic conditions) represent active contraindications for PD-1 inhibitor use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

