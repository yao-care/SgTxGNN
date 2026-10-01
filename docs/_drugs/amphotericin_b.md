---
layout: default
title: Amphotericin B
parent: Medium Evidence (L3-L4)
nav_order: 96
evidence_level: L4
indication_count: 10
---

# Amphotericin B
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Amphotericin B: From Fungal Infections to Paranasal Sinus Neoplasm

## One-Sentence Summary

Amphotericin B is an antifungal drug, and in Singapore it is registered as the liposomal injection AmBisome. The TxGNN model predicts it may be useful for **paranasal sinus neoplasm**, but there are **0 clinical trials** and **12 publications** for this prediction. The publications are almost all about fungal sinus infection (mucormycosis) in cancer patients, not about treating a tumour, so the evidence does not support the prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source data (the HSA indication text is empty). Antifungal use is inferred from the drug class. |
| Predicted New Indication | Paranasal sinus neoplasm |
| TxGNN Prediction Score | 97.45% (model rank 19,524) |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, amphotericin B binds ergosterol in fungal cell membranes and damages them. This is an antifungal mechanism, not an antitumour one.

The prediction is not mechanistically supported. The retrieved literature describes invasive rhinocerebral mucormycosis and aspergillosis of the sinuses, often in patients with leukaemia or other cancers. In several reports, the fungal mass mimicked a tumour. The graph link most likely reflects co-occurrence of fungal sinus infection and malignancy, not tumour treatment. This is a disease-label mismatch, not a repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Every paper below concerns fungal disease, not neoplasm treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [31181136](https://pubmed.ncbi.nlm.nih.gov/31181136/) | 2019 | Systematic review | J Pediatric Infect Dis Soc | 10-year review of paediatric mucormycosis cases, covering characteristics, diagnosis, management and outcome |
| [30338581](https://pubmed.ncbi.nlm.nih.gov/30338581/) | 2019 | Retrospective cohort | Mycoses | Invasive mucormycosis in children with cancer; frequently fatal, with unfavourable outcome in 22–59% of patients |
| [27832748](https://pubmed.ncbi.nlm.nih.gov/27832748/) | 2016 | Epidemiologic cohort | BMC Infect Dis | Two-registry study of paediatric invasive mucormycosis, a rare and often fatal fungal disease |
| [23058177](https://pubmed.ncbi.nlm.nih.gov/23058177/) | 2013 | Review | J Cranio-Maxillo-Facial Surg | Surgical management of rhinocerebral mucormycosis, a rapidly progressive disease in immunocompromised patients |
| [12218600](https://pubmed.ncbi.nlm.nih.gov/12218600/) | 2002 | Case report | J Pediatr Hematol Oncol | Boy with relapsed leukaemia and rhinocerebral mucormycosis; long-term survival with systemic antifungal treatment |
| [12229280](https://pubmed.ncbi.nlm.nih.gov/12229280/) | 2002 | Case series | Investigacion Clinica | Three mucormycosis cases from Caracas, two with diabetes |
| [7689184](https://pubmed.ncbi.nlm.nih.gov/7689184/) | 1993 | Case report | Neurol Med Chir | Diabetic man with an invasive orbital apex mass caused by rhinocerebral mucormycosis; the differential included a paranasal-sinus carcinomatous lesion (abstract truncated) |
| [10340559](https://pubmed.ncbi.nlm.nih.gov/10340559/) | 1999 | Case report | Surv Ophthalmol | Orbital apex syndrome in a lung cancer patient on chemotherapy and radiation (abstract truncated) |
| [1057138](https://pubmed.ncbi.nlm.nih.gov/1057138/) | 1975 | Case report | Oral Surg Oral Med Oral Pathol | Two cases of rhinocerebral mucormycosis, with extremely high morbidity and mortality |
| [2195371](https://pubmed.ncbi.nlm.nih.gov/2195371/) | 1990 | Case report | Neuro-Chirurgie | Cerebral aspergillus granuloma that mimicked a meningioma, a brain tumour |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12021P | AMBISOME FOR INJECTION 50 mg/vial | Injection, powder, for solution | Not provided in source data |

## Safety Considerations

Please refer to the package insert for safety information. The drug-interaction query returned no records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is high (97.45%), but there are no trials and no mechanism linking amphotericin B to tumour treatment. The literature shows fungal infection mistaken for, or occurring alongside, cancer. This is a label artifact, not a repurposing candidate.

**Other predictions in the same pack:**
- **Chronic rhinosinusitis (L1, Hold):** This is the best-supported direction. It has a completed Phase 3 RCT (NCT00425620, n=300, results not provided) and several RCTs and meta-analyses of topical amphotericin B. The 2018 Cochrane review and other trials show no consistent benefit and note local irritation, so the direction is largely negative or inconclusive.
- **Endocarditis (L3, Research Question):** Applies to fungal endocarditis only, based on case-based evidence.
- **Chronic ethmoidal sinusitis (L4, Research Question):** Applies to invasive fungal disease only, based on case reports and small series.
- **Bacterial pneumonia, meningococcal infection, bacterial arthritis and pneumocystosis (Hold):** Not supported. Amphotericin B has no antibacterial activity, and its effect on *Pneumocystis* is not clinically useful.
- **Endocardial fibroelastosis and punctate epithelial keratoconjunctivitis (Hold):** Model prediction only, or a single indirect 1975 paper.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications), which is currently a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Confirmation of the intervention and outcomes of NCT00425620 if chronic rhinosinusitis is pursued
- A decision on whether to reframe the fungal indications (fungal endocarditis, fungal arthritis, pulmonary mucormycosis) as separate candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

