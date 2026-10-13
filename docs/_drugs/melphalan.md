---
layout: default
title: Melphalan
parent: High Evidence (L1-L2)
nav_order: 646
evidence_level: L2
indication_count: 10
---

# Melphalan
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Melphalan: From Ovarian Cancer to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is an alkylating chemotherapy drug, originally used for ovarian cancer.
The TxGNN model predicts it may be effective for **gonadal germ cell tumor**,
with **7 clinical trials** and **1 publication** currently listed for this direction. Most of the trials use melphalan as one part of a high-dose combination regimen.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Gonadal germ cell tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, melphalan is a bifunctional alkylating agent that cross-links DNA and blocks tumour cells from dividing.

Germ cell tumours are generally sensitive to DNA-damaging chemotherapy. Melphalan is already used against ovarian cancer, and the ovary is one of the main sites where germ cell tumours arise. High-dose melphalan with autologous stem cell rescue is therefore a plausible salvage strategy for relapsed, poor-prognosis disease. The very high TxGNN score fits this reasoning.

An important caveat: in the available trials melphalan is almost always given inside a multi-drug regimen. Its individual contribution cannot be separated out.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy (gemcitabine, docetaxel, melphalan, carboplatin, then ifosfamide, carboplatin, etoposide) in relapsed, poor-prognosis germ cell tumours |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with stem cell support and amifostine cytoprotection in cancer patients, including germ cell tumours |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens, with or without radiation, plus autologous transplant in haematologic malignancies and selected solid tumours |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan, melphalan and topotecan with autologous transplant in advanced or recurrent tumours |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | High-dose chemotherapy regimens, with or without total-body irradiation, before autologous transplant; heterogeneous malignancies |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for neoplastic meningitis; different setting and route, low relevance |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine chemoprotection with autologous transplant in paediatric solid and brain tumours; supportive-care focus |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Other (pharmacology report) | Acta - Unio Internationalis Contra Cancrum | Early report on the effect of hormonal and alkylating drugs on pituitary follicle-stimulating function; no abstract available and only indirect relevance |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11873P | ALKERAN FOR INJECTION 50 mg/vial | Injection | Not listed in the data |
| SIN11822P | ALKERAN TABLET 2 mg (Revised formula) | Film-coated tablet | Not listed in the data |

Both licences are valid single-ingredient products, covering injectable and oral routes.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (the knowledge graph links melphalan to neutropenia, leukopenia, thrombocytopenia and anaemia) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: kidney disease, thrombocytopenia, anaemia, leukopenia, neutropenia and agranulocytosis, hemolytic anemia, interstitial lung disease, pulmonary fibrosis, drug-induced liver injury, and vasculitis.
- **Drug Interactions**: 100 interactions were found in total. The listed ones include moderate interactions with amphotericin B (conventional and lipid formulations) and minor interactions with cimetidine, levofloxacin and zinc salts. Several others, such as proton pump inhibitors, metformin, prednisone and simvastatin, have an unclassified severity.
- **Long-term risk**: The literature notes that alkylating agents such as melphalan carry a high rate of second malignancies, mostly acute leukaemias.

Please refer to the package insert for full warnings and contraindications.

---

## Other Predicted Indications (Brief)

| Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|
| Ovarian primitive germ cell tumor | 99.75% | L3 | Small phase 1/2 trials and one case report |
| Female breast carcinoma | 99.67% | L2 | Many high-dose combination studies and a randomized trial versus vinorelbine, but modern alternatives and second-malignancy risk limit use |
| Choriocarcinoma of ovary, malignant non-epithelial ovarian tumor, and several mucinous adenocarcinomas (rectum, colon, gallbladder, cervix, endometrium) | 99.26–99.74% | L5 | Prediction only, with no trials or literature in the data; the mucinous predictions likely reflect histology labels rather than mechanism |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 2 trial (n=64) tests high-dose chemotherapy that includes melphalan directly in relapsed germ cell tumours. Several small transplant studies add support. Because melphalan is always combined with other drugs, and the toxicity (especially myelosuppression) is substantial, this is a research question rather than a ready-to-use new indication.

**To proceed, the following is needed:**
- Published results and outcomes of NCT00936936, and an assessment of melphalan's individual contribution within the combination
- Package insert warnings and contraindications from the Singapore regulator (HSA), which are currently missing
- Detailed mechanism of action data from DrugBank
- Approved indication text for the two Singapore licences
- A haematological and organ-function monitoring plan, plus a transplant-capable setting for high-dose use
- Comparison against current standard salvage regimens for germ cell tumours
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

