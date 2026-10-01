---
layout: default
title: Phenytoin
parent: Low Evidence (L5)
nav_order: 781
evidence_level: L5
indication_count: 10
---

# Phenytoin
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

# Phenytoin: From Seizure Control to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenytoin is an established antiseizure medicine, and the Singapore licence records list no approved indication text.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and only **5 publications**, none of which studies a neoplasm.
The prediction is model-only and should be treated as a graph artefact rather than a real signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (phenytoin is a known antiseizure drug) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Phenytoin is a sodium-channel blocker that limits repetitive neuronal firing, and it is used for seizures. That mechanism could relieve nerve pain or seizures, but it has no known antitumour effect.

The high graph score most likely reflects that the predicted disease sits close to trigeminal neuralgia and Sturge-Weber syndrome in the knowledge graph. Phenytoin has real links to both conditions. The five retrieved papers cover neuralgia and neurocutaneous syndromes, not neoplasm.

This prediction is therefore not mechanistically supported. Among the model's other predictions, **trigeminal neuralgia** (rank 9) has the strongest support, at L3, and is a much more plausible target than a tumour.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia. It is about neuralgia, not neoplasm. |
| [21751615](https://pubmed.ncbi.nlm.nih.gov/21751615/) | 2011 | Review / case report | J Assoc Physicians India | Sturge-Weber syndrome, a neurocutaneous condition with facial port-wine stain and seizures. Not a neoplasm. |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series (unclassified) | An Esp Pediatr | Experience with 14 Sturge-Weber cases over 25 years, covering clinical course and treatment response. |
| [4155965](https://pubmed.ncbi.nlm.nih.gov/4155965/) | 1971 | Not classified | Birth Defects Orig Artic Ser | Skin disorders in institutionalised people with intellectual disability, including drug-induced skin effects. Not relevant to this prediction. |
| [5514358](https://pubmed.ncbi.nlm.nih.gov/5514358/) | 1970 | Not classified | Trans Am Neurol Assoc | Nerve fibre size and pain conduction in the trigeminal root, and analgesia in trigeminal neuralgia. No abstract available. |

---

## Singapore Market Information

Five authorisations are on record. The approved indication text is blank in all of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN09208P | DILANTIN CAPSULE 100 mg | Capsule | Viatris Pharmaceuticals LLC |
| SIN13114P | Dilantin 125 (Phenytoin Oral Suspension, USP) 125mg/5ml | Suspension | Pharmacia and Upjohn Company LLC |
| SIN16560P | PHARMANIAGA PHENYTOIN SODIUM SOLUTION FOR INJECTION 250MG/5ML | Injection, solution | Pharmaniaga LifeScience Sdn. Bhd. |
| SIN08183P | DBL PHENYTOIN INJECTION BP 50 mg/ml | Injection | Siegfried Hameln GmbH |
| SIN06056P | DILANTIN CAPSULE 30 mg | Capsule | Viatris Pharmaceuticals LLC |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials and no neoplasm-specific literature. Phenytoin has no known antitumour mechanism, so the score most likely reflects proximity to neuralgia and neurocutaneous nodes in the graph.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that phenytoin acts on trigeminal nerve tumours (none exists in the current pack).
- The HSA package insert, to confirm the registered indications, warnings and contraindications.
- Mechanism of action data from DrugBank.
- Redirecting effort to **trigeminal neuralgia**, which is a better-supported candidate:
  - It is rated L3 and Proceed with Guardrails.
  - It has one completed small prospective study, [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) (n=15).
  - It has retrospective IV phenytoin series (PMIDs 35469475 and 32981076).
  - Phenytoin would be a rescue option for acute exacerbations, not first-line therapy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

