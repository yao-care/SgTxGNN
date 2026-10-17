---
layout: default
title: Proparacaine
parent: Low Evidence (L5)
nav_order: 834
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Proparacaine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the registration data (ophthalmic topical anaesthetic)"
monitor_inn: "Proparacaine"
predicted_indications: ["cauda equina syndrome", "allergic asthma", "intrinsic asthma", "hypotensive disorder", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "pityriasis simplex", "asthma-related traits, susceptibility to", "lichen disease", "vertigo, benign recurrent, 2"]
---

# Proparacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Proparacaine: From Ocular Surface Anesthesia to Cauda Equina Syndrome

## One-Sentence Summary

Proparacaine is a topical ocular local anesthetic, registered in Singapore as a sterile ophthalmic solution.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this is a computational prediction only, with **no clinical trials** and **no publications** supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (ophthalmic topical anaesthetic) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 96.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, proparacaine is a topical ocular local anaesthetic of the same general class as lidocaine, and local anaesthetics generally work by blocking voltage-gated sodium channels.

In theory, sodium channel blockade could relate to neuropathic or radicular pain. However, cauda equina syndrome is a compressive surgical emergency, and a topical eye anaesthetic has no plausible disease-modifying role. The high score reflects network-based computational prediction rather than biological or clinical support. The prediction should be treated with considerable caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

For context, the other predicted indications also have very little support:
- **Allergic asthma (rank 2):** the only retrieved article ([28449552](https://pubmed.ncbi.nlm.nih.gov/28449552/), 2017, Clin Exp Otorhinolaryngol) is a preclinical mouse study of proparacaine in allergic rhinitis. It is a different disease and an animal model, so it is indirect evidence.
- **Hypotensive disorder (rank 4):** the retrieved articles are Cochrane reviews on non-antiepileptic drugs for trigeminal neuralgia ([24297506](https://pubmed.ncbi.nlm.nih.gov/24297506/), [21249658](https://pubmed.ncbi.nlm.nih.gov/21249658/), [16856027](https://pubmed.ncbi.nlm.nih.gov/16856027/)). They are off-topic and not relevant evidence for this indication.
- **Papillary conjunctivitis (rank 6):** the most anatomically plausible candidate, since proparacaine is already used on the ocular surface. It is used for anaesthesia, not for treating inflammation, and no studies support a therapeutic effect.
- The remaining predictions (intrinsic asthma, obsolete neurogenic bladder, pityriasis simplex, asthma-related traits, lichen disease, benign recurrent vertigo type 2) have no trials or literature.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04718P | ALCAINE STERILE OPHTHALMIC SOLUTION 0.5% | Solution | Not listed in the registration data |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The TxGNN knowledge graph links proparacaine to contraindication-type relationships with heart disease, cardiovascular disease, hyperthyroidism, Graves disease, thyrotoxicosis, uveitis, iris disease, ciliary body disease, panuveitis, eye infectious disease and conjunctivitis. These come from a computational knowledge graph rather than a package insert and should be verified against the official label.
- **Repeated ocular use:** Topical anaesthetics are associated with corneal toxicity on repeated use, which is a major concern for any chronic ocular indication.
- **Cardiovascular effects:** Local anaesthetics can have systemic cardiovascular effects at high doses, which could worsen hypotension.
- **Drug interactions:** No interaction records were found.

Please refer to the package insert for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. There are no clinical trials, and the only related literature is indirect or off-topic. A topical ocular anaesthetic has no credible role in a surgical compressive condition such as cauda equina syndrome. The highest-ranked predictions are also mechanistically implausible, and the route of administration does not match.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing
- Mechanism of action data from DrugBank
- Approved indication text for the Singapore registration
- Assessment of route compatibility between the ophthalmic formulation and any proposed indication
- Clinical or well-designed preclinical evidence specific to a chosen indication
- If any indication is pursued, a better-fitting candidate such as an ocular-surface condition should be evaluated first, with a corneal safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

