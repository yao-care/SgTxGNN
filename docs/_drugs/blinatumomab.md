---
layout: default
title: Blinatumomab
parent: Low Evidence (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Blinatumomab
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

# Blinatumomab: From B-cell Precursor Acute Lymphoblastic Leukemia to Primary Release Disorder of Platelets

## One-Sentence Summary

Blinatumomab is a CD19×CD3 bispecific T-cell engager, developed for B-cell precursor acute lymphoblastic leukemia (ALL).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but the evidence is weak: **2 clinical trials** were linked, both in ALL and not in platelet disorders, and **0 publications** were found.
The high score is most likely a knowledge-graph artifact, and the prediction may even be harmful.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | B-cell precursor acute lymphoblastic leukemia (the Singapore license record gives no indication text; this is inferred from the linked trials) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 95.20% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Blinatumomab is a CD19×CD3 bispecific T-cell engager: it redirects T cells to kill CD19-positive B cells. Its use in B-cell leukemia follows directly from this mechanism.

The predicted indication does not follow from it. Primary release disorder of platelets is a defect in platelet granule secretion. Platelets do not express CD19, so there is no plausible pathway by which B-cell depletion or T-cell redirection would correct it. Cytopenias, including thrombocytopenia, are labeled adverse effects of blinatumomab, so use in a platelet disorder could be harmful.

The other nine top-ranked predictions also lack support:
- **Platelet and bleeding disorders** (Glanzmann thrombasthenia, pseudo-von Willebrand disease, constitutional thrombocytopenia, collagen receptor defect): each involves a defect that blinatumomab does not act on.
- **Other conditions** (drug-induced osteoporosis, diabetic retinopathy, psoriasis, Ledderhose disease, penile fibromatosis): no supporting mechanism or evidence was found.

---

## Clinical Trial Evidence

Both linked trials were graded "C" (not direct evidence for this indication). Neither studied a platelet disorder.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04524455](https://clinicaltrials.gov/study/NCT04524455) | Phase 1 | Completed | 17 | Safety, tolerability and MTD/RP2D of blinatumomab plus AMG 404 in adults with relapsed/refractory B-ALL. No platelet disorder population. |
| [NCT03476239](https://clinicaltrials.gov/study/NCT03476239) | Phase 3 | Completed | 121 | Open-label study of the hematological response (CR/CRh*) to blinatumomab in Chinese adults with relapsed/refractory B-precursor ALL. Leukemia endpoints only, so it does not support the predicted indication. |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15103P | BLINCYTO POWDER FOR INFUSION 35 MCG/VIAL | Injection, powder, lyophilized, for solution | Not provided in the registry record |

Manufacturers: Boehringer Ingelheim Pharma GmbH & Co. KG and Amgen Technology (Ireland) Unlimited Company. The only route is injectable.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (bispecific T-cell engager), not a conventional cytotoxic |
| Myelosuppression Risk | Cytopenias, including thrombocytopenia, are labeled adverse effects. Please refer to the package insert for grading. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with platelet count) is essential given the cytopenia risk. Please refer to the package insert for the full monitoring schedule. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Key Warnings**: Cytopenias, including thrombocytopenia, are labeled adverse effects. Blinatumomab's T-cell activation carries a risk of cytokine release syndrome. Both are relevant to the predicted platelet and autoimmune-type indications.

No DDI records were found, and structured warnings and contraindications are unavailable. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). The two linked trials are in ALL, and no literature exists. The mechanism has no plausible link to platelet release disorders, and thrombocytopenia is a known adverse effect, so the prediction may be harmful. The same holds for the other nine top-ranked predictions.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (currently blocking safety screening)
- Mechanism-of-action data from DrugBank
- A credible biological rationale linking CD19-directed T-cell redirection to platelet granule secretion, plus any preclinical or clinical evidence in this population
- A safety assessment of thrombocytopenia and cytokine release syndrome risk in non-oncology patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

