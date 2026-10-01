---
layout: default
title: Dostarlimab
parent: Low Evidence (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Dostarlimab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dostarlimab: From Cancer Immunotherapy (PD-1 Blockade) to Tendinopathy

## One-Sentence Summary

Dostarlimab is a PD-1 blocking antibody, a cancer immunotherapy, and is marketed in Singapore as an intravenous infusion.
The TxGNN model predicts it may be effective for **tendinopathy**, but the score is an uninformative 0.5.
There are **0 clinical trials** and **0 publications** supporting this direction, so the evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence record (PD-1 blocking antibody used in cancer immunotherapy) |
| Predicted New Indication | Tendinopathy |
| TxGNN Prediction Score | 50% (rank 51,903) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Dostarlimab blocks PD-1, which releases the brake on T cells so the immune system can attack tumour cells.

Tendinopathy is mainly a degenerative or overuse condition with only a minor inflammatory component. There is no known therapeutic rationale for immune checkpoint blockade here. A score of exactly 0.5 carries almost no information, and it is most likely a knowledge-graph artefact rather than a real signal.

The other nine top predictions, which include autoimmune retinopathy, several anaphylaxis types, metabolic epilepsy and other epilepsy syndromes, and a branched-chain amino acid disorder, share the same 0.5 score, L5 level and Hold status. For autoimmune retinopathy the direction is likely adverse, because checkpoint inhibitors can trigger autoimmune retinopathies. For the anaphylaxis and epilepsy predictions, safety concerns (hypersensitivity reactions, immune-mediated encephalitis and seizures) outweigh any prediction signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16623P | JEMPERLI Concentrate for Solution for Infusion 500 mg/10 mL | Infusion, solution concentrate | Not stated in the record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-1 checkpoint inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Low (not a typical effect of this class); please refer to the package insert |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert; immune-related adverse events (for example liver, thyroid, and other organ function) are the usual focus for this class |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

Class-level concerns noted in the prediction rationale:
- Monoclonal antibodies such as dostarlimab can cause infusion or hypersensitivity reactions.
- PD-1 blockade can trigger immune-mediated adverse events, including autoimmune retinopathy and neurological events such as encephalitis and seizures.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no mechanistic support, no trials, and no literature, and the TxGNN score of 0.5 is uninformative. Immune checkpoint blockade also carries safety risks in several of the predicted conditions.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (currently blocking safety screening)
- The approved indication text for SIN16623P
- Mechanism of action data from DrugBank
- Any supporting preclinical or clinical evidence linking PD-1 blockade to tendinopathy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

