---
layout: default
title: Eribulin
parent: Low Evidence (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eribulin: predicted new indication Autosomal recessive familial Mediterranean fever (evidence level L5). Approved use: Liposarcoma"
monitor_inn: "Eribulin"
predicted_indications: ["autosomal recessive familial Mediterranean fever", "dermatofibrosarcoma protuberans", "pleural mesothelioma", "malignant peritoneal mesothelioma", "ovarian myxoid liposarcoma", "pleural adenomatoid tumor", "pleural biphasic mesothelioma", "fibroblastic neoplasm", "pleural epithelioid mesothelioma", "heart fibrosarcoma"]
---

# Eribulin
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

## Eribulin: From Liposarcoma to Autosomal Recessive Familial Mediterranean Fever
{: .text-alpha }

## One-Sentence Summary

Eribulin is a cytotoxic chemotherapy originally used to treat liposarcoma.
The TxGNN model predicts it may be effective for **autosomal recessive familial Mediterranean fever (FMF)**, with a very high score.
However, **no clinical trials and no publications** currently support this prediction, so it rests on the model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Liposarcoma |
| Predicted New Indication | Autosomal recessive familial Mediterranean fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eribulin inhibits microtubule dynamics, which blocks cell division. This makes it useful against rapidly proliferating tumours such as soft tissue sarcoma. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on the drug's known pharmacology.

FMF is a hereditary autoinflammatory disease. It is driven by dysregulation of the MEFV/pyrin inflammasome, not by uncontrolled cell growth. The only loose conceptual link is that colchicine, the standard FMF therapy, also acts on microtubules. That is a weak parallel. A cytotoxic chemotherapy is not a plausible treatment for a chronic, non-malignant inflammatory condition. The high TxGNN score (0.998) is most likely an artifact of the knowledge graph structure and not a real biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13917P | Halaven Solution for Injection 0.5mg/mL | Injection, solution | Not stated in the registration record |

The product is a valid single-ingredient registration.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (microtubule dynamics inhibitor) |
| Myelosuppression Risk | High (neutropenia and thrombocytopenia are listed among the drug's contraindicated conditions in the knowledge graph) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes (potassium, magnesium), ECG for QT interval, neurological assessment for peripheral neuropathy |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: long QT syndrome (including familial), thrombocytopenia, neutropenia, agranulocytosis, potassium deficiency, peripheral nervous system disease and peripheral neuropathy, and constipation disorder.
- **Drug Interactions**: 100 interactions were identified in total. The two rated **Major** are:
  - Dolasetron
  - Cisapride

  Both are likely related to QT prolongation. Many **Moderate** interactions were also found, including:
  - Antiemetics: ondansetron, palonosetron
  - Antibiotics: clarithromycin, levofloxacin, metronidazole, tinidazole
  - Statins: simvastatin, rosuvastatin
  - Laxatives and bowel-preparation agents: bisacodyl, lactulose, polyethylene glycol
  - Others: famotidine, loperamide

For full warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no trials or publications, and the biological rationale is weak. FMF is a non-malignant inflammatory disease, and eribulin is a toxic cytotoxic drug with significant myelosuppression, neuropathy and QT risks. The risk-benefit balance is unfavourable, and well-established, safer FMF therapies exist.

**To proceed, the following is needed:**
- Detailed mechanism of action data and a credible mechanistic link to pyrin/inflammasome biology
- Preclinical evidence in an FMF-relevant model
- Package insert warnings and contraindications from the Singapore regulator
- Approved indication text for the Singapore registration

**Note on other candidates:** Among the other predicted indications, **fibroblastic neoplasm** (rank 8) has the strongest support. It has a completed Phase 2 trial in advanced solitary fibrous tumour ([NCT03840772](https://clinicaltrials.gov/study/NCT03840772), n=16, no results in the data compiled), plus supporting preclinical literature. This direction is a more sensible research question than FMF and may deserve priority review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

