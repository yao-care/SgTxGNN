---
layout: default
title: Amphotericin B
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Amphotericin B
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

# Amphotericin B: From Systemic Fungal Infections to Paranasal Sinus Neoplasm

## One-Sentence Summary

Amphotericin B is a gold-standard polyene antifungal agent, long used as first-line therapy for life-threatening invasive fungal infections including aspergillosis, mucormycosis, cryptococcal meningitis, and candidiasis.
The TxGNN model predicts it may be effective for **Paranasal Sinus Neoplasm** with a score of 97.45%, supported by **0 clinical trials** and **12 publications** — yet all 12 publications describe fungal sinus infections rather than tumours, indicating this prediction is a knowledge graph (KG) annotation artefact rather than a genuine repurposing signal.
Across the 10 predicted indications in this Evidence Pack, **Chronic Rhinosinusitis** (rank 2, L1 evidence) and **Fungal Endocarditis** (rank 9, L3 evidence) represent the only scientifically substantiated hypotheses worthy of further consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious systemic fungal infections (invasive aspergillosis, mucormycosis, cryptococcosis, candidiasis) |
| Predicted New Indication | Paranasal Sinus Neoplasm |
| TxGNN Prediction Score | 97.45% |
| Evidence Level | L4 — KG annotation artefact; no antitumour evidence exists |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Amphotericin B is a polyene macrolide derived from *Streptomyces nodosus* that exerts antifungal activity by selectively binding to **ergosterol** — a sterol unique to fungal cell membranes and absent in mammalian cells. This binding creates transmembrane pores, causing leakage of intracellular ions and fungal cell death. Lipid formulations (liposomal AmB, AmB lipid complex, AmB colloidal dispersion) were developed to reduce the dose-limiting nephrotoxicity of the conventional deoxycholate preparation, allowing higher cumulative doses.

Paranasal sinus neoplasms are malignant or benign tumours arising from the mucosal lining of the maxillary, ethmoid, frontal, and sphenoid sinuses. Human tumour cells do not contain ergosterol; consequently, Amphotericin B has no direct cytotoxic or antitumour mechanism applicable to neoplastic disease. No experimental data, case reports, or credible mechanistic hypothesis has ever linked Amphotericin B to anticancer activity in any solid tumour type.

**⚠️ KG Annotation Artefact Warning:** Every one of the 12 retrieved publications actually describes *fungal infections* of the paranasal sinuses — rhinocerebral mucormycosis, invasive Aspergillus sinusitis, and related conditions — not sinus neoplasms. The high TxGNN score (97.45%) most likely arises from structural proximity between "paranasal sinus pathology" nodes in the knowledge graph (where both fungal disease and neoplasm sit near the same anatomical region), rather than any genuine drug–tumour biological association. This prediction should be classified as a **false positive** and flagged for KG correction prior to any further computational analysis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Amphotericin B in paranasal sinus neoplasm.

---

## Literature Evidence

All 12 publications retrieved under "Amphotericin B + paranasal sinus neoplasm" describe **fungal sinus infections**, not tumour pathology. They are listed below for transparency; none constitutes evidence for antineoplastic activity.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31181136](https://pubmed.ncbi.nlm.nih.gov/31181136/) | 2019 | Systematic Review | J Pediatric Infect Dis Soc | Paediatric mucormycosis (2008–2017): predominantly rhinocerebral presentation; AmB backbone of treatment |
| [30338581](https://pubmed.ncbi.nlm.nih.gov/30338581/) | 2019 | Retrospective Study | Mycoses | Invasive mucormycosis in paediatric oncology patients; AmB + surgical debridement as standard approach |
| [27832748](https://pubmed.ncbi.nlm.nih.gov/27832748/) | 2016 | Epidemiologic Study | BMC Infect Dis | European/non-European registry of paediatric mucormycosis; high fatality without timely AmB |
| [23058177](https://pubmed.ncbi.nlm.nih.gov/23058177/) | 2013 | Surgical Case Series | J Craniomaxillofac Surg | Rhinocerebral mucormycosis surgical management combined with systemic AmB |
| [12229280](https://pubmed.ncbi.nlm.nih.gov/12229280/) | 2002 | Case Series | Investigacion Clinica | Three mucormycosis cases including rhinocerebral form in diabetic ketoacidosis patients |
| [12218600](https://pubmed.ncbi.nlm.nih.gov/12218600/) | 2002 | Case Report | J Pediatr Hematol Oncol | Rhinocerebral mucormycosis in child with relapsed ALL; long-term survival with prolonged AmB therapy |
| [7689184](https://pubmed.ncbi.nlm.nih.gov/7689184/) | 1993 | Case Report | Neurol Med Chir | Rhinocerebral mucormycosis in diabetic male; orbital apex involvement, AmB treatment |
| [2195371](https://pubmed.ncbi.nlm.nih.gov/2195371/) | 1990 | Case Report | Neuro-Chirurgie | Aspergillus cerebral granuloma extending from paranasal sinuses; treated with AmB |
| [8567925](https://pubmed.ncbi.nlm.nih.gov/8567925/) | 1995 | Case Report | J Clin Microbiol | Cutaneous phaeohyphomycosis in an immunosuppressed patient; AmB in vitro activity reported |
| [10340559](https://pubmed.ncbi.nlm.nih.gov/10340559/) | 1999 | Case Report | Survey Ophthalmol | Lung cancer presenting with proptosis; paranasal sinus disease was ruled out — AmB not administered |

---

## Singapore Market Information

Amphotericin B is currently **not registered** with the Health Sciences Authority (HSA) in Singapore. No product licences are on record. Any clinical use in Singapore would require special access via the Compassionate Use Scheme (CUS) or a Clinical Trial Authorisation (CTA).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinician Note (from published literature):** Although formal safety data is absent from this Evidence Pack, Amphotericin B carries a well-characterised toxicity profile documented across decades of clinical use:
> - **Nephrotoxicity:** Dose-limiting with conventional deoxycholate formulation; significantly reduced with lipid-based formulations (liposomal AmB preferred)
> - **Infusion-related reactions:** Fever, rigors, chills, nausea, and headache are common; premedication (paracetamol, antihistamine, hydrocortisone) is standard practice
> - **Electrolyte disturbances:** Hypokalaemia and hypomagnesaemia require active monitoring and supplementation
> - **Haematological:** Normocytic normochromic anaemia with prolonged use
>
> Drug interactions with nephrotoxic agents (aminoglycosides, cisplatin, cyclosporin) are of particular concern and require careful co-prescription review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 prediction for paranasal sinus neoplasm is a KG annotation artefact — all supporting literature describes fungal sinusitis rather than tumour pathology, and Amphotericin B has no established or plausible antineoplastic mechanism. This indication must not be advanced.

**More Clinically Meaningful Predictions in This Evidence Pack:**

| Rank | Indication | Evidence Level | Recommendation | Summary |
|------|-----------|---------------|----------------|---------|
| 2 | Chronic Rhinosinusitis | L1 | Research Question | 1 completed Phase 3 RCT (n=300) + Cochrane review + 2 meta-analyses; results mixed/negative — topical AmB not currently endorsed by guidelines |
| 3 | Chronic Ethmoidal Sinusitis (fungal) | L3 | Research Question | Multiple case series supporting AmB + surgical debridement for invasive fungal disease; anatomically high-risk site |
| 9 | Fungal Endocarditis | L3 | Proceed with Guardrails | ESCMID 2012 guideline-endorsed; systematic review of Candida endocarditis supports liposomal AmB as salvage therapy |

**To proceed with any Amphotericin B repurposing programme, the following steps are required:**
- **Correct the KG annotation:** Reclassify rank-1 from "paranasal sinus neoplasm" to "paranasal sinus fungal infection" to reflect actual evidence
- **Resolve Data Gap DG001:** Retrieve HSA-registered package insert for formal warnings and contraindications
- **Resolve Data Gap DG002:** Obtain complete MOA data from DrugBank API (DB00681)
- **For Chronic Rhinosinusitis (rank 2):** Review the Cochrane systematic review (PMID [30199594](https://pubmed.ncbi.nlm.nih.gov/30199594/)) and the 2015 meta-analysis (PMID [25217082](https://pubmed.ncbi.nlm.nih.gov/25217082/)) to assess whether topical AmB offers net clinical benefit before committing to further development; current evidence does not favour advancement
- **For Fungal Endocarditis (rank 9):** Develop a protocol aligned with ESCMID guidelines; liposomal formulation preferred; surgical valve replacement remains an essential co-intervention
- **Singapore registration pathway:** Evaluate feasibility of HSA registration or expanded access scheme if a specific fungal indication (e.g., invasive fungal rhinosinusitis or fungal endocarditis) is selected as the primary development target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

