---
layout: default
title: Gefitinib
parent: Low Evidence (L5)
nav_order: 471
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "Gefitinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
description: "Gefitinib: predicted new indication Fibromatosis, gingival (evidence level L5). In Singapore: 5 HSA registrations (5 valid)"
---

# Gefitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Gefitinib: Fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Gefitinib is an oral EGFR tyrosine kinase inhibitor, originally used to treat non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 5 of 5) |
| Number of Registrations | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for gefitinib: "The epidermal growth factor receptor (EGFR) is expressed on the cell surface of both normal and cancer cells and plays a role in the processes of cell growth and proliferation. Some EGFR activating mutations (exon 19 deletion or exon 21 point mutation L858R) within NSCLC cells have been identified as contributing to the promotion of tumor cell growth, blocking of apoptosis, increasing the production of angiogenic factors and facilitating the processes of metastasis. […] Gefitinib reversibly inhibits the kinase activity of wild-type and certain activating mutations of EGFR, preventing autophosphorylation of tyrosine residues associated with the receptor, thereby inhibiting further downstream signaling and blocking EGFR-dependent proliferation." ([DailyMed: Iressa (gefitinib) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41), label version 2023-02-28; accessed 2026-11-19.) Based on known information, gefitinib is a selective EGFR tyrosine kinase inhibitor whose efficacy in EGFR-mutant NSCLC is well established. The literature compiled for other predictions describes it as blocking EGFR signalling, which limits cell proliferation and survival.

A possible link to gingival fibromatosis is EGFR/ERBB signalling in fibroblast proliferation. This is speculative: no trial or publication in the compiled data supports it. Gingival fibromatosis is a benign overgrowth of gum tissue, quite different from a lung malignancy, so the high score (rank 2108 overall) should be treated as a hypothesis to test, not as evidence of benefit.

Other top-ranked predictions show the same weakness. Several are lung neoplasm subtypes that largely overlap with the existing approved use (lung hilum carcinoma, pulmonary sulcus neoplasm). Others, such as the VCP-related myopathy and junctional epidermolysis bullosa, have no evident mechanistic connection, and gefitinib is known to cause skin toxicity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN15984P | HOVID GEFITINIB TABLETS 250 MG | TABLET, FILM COATED | Valid |
| SIN16030P | VEIASU FILM-COATED TABLETS 250 MG | TABLET, FILM COATED | Valid |
| SIN16055P | INGEFITINIB FILM COATED TABLET 250MG | TABLET, FILM COATED | Valid |
| SIN16130P | GEFTINAT FILM COATED TABLETS 250 MG | TABLET, FILM COATED | Valid |
| SIN16722P | GEFITINIB-TEVA FC TABLET 250MG | TABLET, FILM COATED | Valid |

<!-- licenses:end -->

All five registrations are valid single-ingredient oral products.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: liver disease, gallbladder disease, interstitial lung disease, pulmonary fibrosis, and postinflammatory pulmonary fibrosis.
- **Safety signals in the literature**: published reports describe acute gefitinib-induced pneumonitis or interstitial lung disease (including a fatal case), QT prolongation through hERG channel blockade, a case of recurrent myocardial infarction, and cutaneous toxicities such as acneiform eruption.
- **Drug Interactions**: 100 interactions were identified; the 18 listed with a severity grade are all Moderate, and two more (calcitriol, glimepiride) have unknown severity. The main groups are:
  - Acid-suppressing drugs: famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole
  - CYP-related agents: clarithromycin, miconazole, clotrimazole, aprepitant, dexamethasone
  - Others: naltrexone, troglitazone

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no trials or literature for gingival fibromatosis. The mechanistic link is speculative. Gefitinib also carries known serious risks (interstitial lung disease, hepatic effects, QT prolongation), which are hard to justify for a benign condition without supporting data.

**To proceed, the following is needed:**
- Preclinical or case-level evidence that EGFR inhibition affects gingival fibroblast proliferation or fibrosis
- Detailed mechanism of action data
- Singapore package insert warnings, contraindications and approved indication text
- A risk-benefit assessment for a benign condition, including whether topical or local delivery is feasible (the registered products are oral tablets only)
- If a more evidence-supported direction is desired, review the other ranked predictions; the current top ten show no clinical trial support for a new indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Iressa (gefitinib) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

