---
layout: default
title: Ceftaroline Fosamil
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Ceftaroline Fosamil
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

# Ceftaroline Fosamil: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Ceftaroline fosamil is a fifth-generation cephalosporin antibiotic approved internationally for community-acquired bacterial pneumonia (CABP) and acute bacterial skin and skin structure infections (ABSSSI), though it is not registered in Singapore.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** as the top-ranked indication (score 98.2%), yet this prediction is mechanistically implausible — ceftaroline's sole mechanism is bacterial cell wall inhibition via PBP2a, with no known activity against the autoimmune inflammatory pathways that drive RA.
There are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Community-acquired bacterial pneumonia (CABP); acute bacterial skin and skin structure infections (ABSSSI) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ceftaroline fosamil is a prodrug that is hydrolysed in vivo to its active form, ceftaroline. Its mechanism of action is selective inhibition of penicillin-binding proteins (PBPs), with unique high affinity for PBP2a — the altered transpeptidase expressed by methicillin-resistant *Staphylococcus aureus* (MRSA). This makes ceftaroline the first cephalosporin with meaningful anti-MRSA activity. Its pharmacological action is entirely confined to disruption of bacterial peptidoglycan cross-linking; it has no known interaction with any mammalian signalling pathway.

Rheumatoid arthritis is a chronic autoimmune inflammatory disease driven by dysregulation of the adaptive immune system — specifically the TNF-α/IL-6 cytokine axis, Th17/Treg imbalance, and progressive synovial pannus formation. These pathways have no mechanistic overlap with ceftaroline's target: PBP2a is a prokaryotic protein entirely absent in human cells. While certain antibiotics such as minocycline possess secondary immunomodulatory properties that have shown modest benefit in RA, ceftaroline has no documented anti-inflammatory activity.

The TxGNN prediction score of 98.2% almost certainly reflects a knowledge graph artefact rather than a genuine biological signal. The underlying graph likely connects ceftaroline to musculoskeletal disease nodes through shared "infection / joint inflammation" hub nodes — for example, septic arthritis, prosthetic joint infection, or osteoarticular infections — creating spurious traversal paths to RA. This is a recognised limitation of graph-based repurposing models when an antibiotic's infection-related edges share graph neighbourhoods with inflammatory rheumatic disease nodes.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ceftaroline fosamil in rheumatoid arthritis.

---

## Literature Evidence

Currently no related literature available for ceftaroline fosamil in rheumatoid arthritis.

---

## Singapore Market Information

Ceftaroline fosamil has no product registrations with the Health Sciences Authority (HSA). The drug is not currently marketed in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for ceftaroline fosamil in rheumatoid arthritis is mechanistically implausible — the drug's sole pharmacological action (PBP2a inhibition) has no relevance to RA pathophysiology, and there is zero supporting clinical evidence. The elevated TxGNN score (98.2%) most likely reflects a knowledge graph co-occurrence artefact from shared infection–musculoskeletal nodes rather than any true therapeutic signal.

**To proceed, the following is needed:**

- **Reassess all 10 predicted indications**: none across the full candidate list has risen above evidence level L5 or received a recommendation above "Hold"; the prediction cluster is dominated by musculoskeletal and rare genetic diseases, all mechanistically inconsistent with an antibacterial agent
- **Obtain complete drug profile**: retrieve the full package insert and MOA documentation via DrugBank API (DG002 remediation) to formally document the PBP2a mechanism and ensure no secondary pharmacology has been overlooked
- **Resolve the Singapore registration gap**: confirm whether HSA registration is planned; no market pathway exists at present
- **Redirect investigation to on-mechanism applications**: if ceftaroline fosamil repurposing is to be explored at all, the only biologically coherent direction is infectious bone and joint disease (osteoarticular infections, prosthetic joint infections), where limited real-world cohort data already exists (PMID [27530754](https://pubmed.ncbi.nlm.nih.gov/27530754/), [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/)) — a distinct clinical question from the non-infectious indications generated by TxGNN
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

