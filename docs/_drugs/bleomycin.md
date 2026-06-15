---
layout: default
title: Bleomycin
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Bleomycin
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

# Bleomycin: From Lymphoma and Germ Cell Tumours to Cauda Equina Neoplasm

## One-Sentence Summary

Bleomycin is a cytotoxic glycopeptide antibiotic used globally as a core component of combination regimens for Hodgkin lymphoma (ABVD) and germ cell tumours (BEP), though it is currently unregistered in Singapore.
The TxGNN model ranks **Cauda Equina Neoplasm** as its top predicted new indication, backed by **0 clinical trials** and only **3 indirect publications** — placing it at evidence level L5.
Notably, within the same prediction set, **Reticulum Cell Sarcoma** (rank 3) carries L1 Phase 3 RCT evidence and warrants separate priority review.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hodgkin lymphoma, testicular germ cell tumours, squamous cell carcinomas (global use; no Singapore registration found) |
| Predicted New Indication (Rank 1) | Cauda Equina Neoplasm |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, bleomycin is a glycopeptide antibiotic that generates free radicals upon DNA binding, causing single- and double-strand DNA breaks with selective G2/M phase cytotoxicity. Its efficacy in Hodgkin lymphoma and germ cell tumours is well proven, and this DNA-damaging mechanism is theoretically non-histotype-specific — meaning it could, in principle, be applied to any rapidly proliferating malignancy including those arising at or spreading to the cauda equina.

Cauda equina neoplasms are a heterogeneous group: primary tumours include myxopapillary ependymoma, meningioma, and schwannoma, while secondary involvement may arise from lymphoma or metastatic germ cell tumours. The three supporting literature entries all concern scenarios where haematological or germ cell malignancies involve the cauda equina region — contexts in which bleomycin-containing regimens (BEP, ABVD) were already in use for systemic disease, not for the cauda equina tumour itself.

The TxGNN model likely inferred this association through knowledge-graph edges linking bleomycin to haematological and germ cell cancers that can secondarily involve the cauda equina. There is no direct preclinical evidence, no in vitro study of bleomycin against primary cauda equina tumour cells, and no clinical trial targeting this entity. The prediction is mechanistically plausible only in the narrow context of systemic lymphoma or GCT with cauda equina extension.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bleomycin in Cauda Equina Neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Retrospective | J Clin Oncol | Radiation salvage for CNS germinoma relapsed after PEB (carboplatin + etoposide + bleomycin); bleomycin was part of the prior chemotherapy backbone, not a direct cauda equina treatment |
| [1720278](https://pubmed.ncbi.nlm.nih.gov/1720278/) | 1991 | Retrospective | Am J Clin Oncol | CNS involvement in 277 aggressive NHL patients; one case had cauda equina involvement at autopsy — epidemiological context only, no bleomycin therapy described for this site |
| [31142709](https://pubmed.ncbi.nlm.nih.gov/31142709/) | 2019 | Case Report | Rinsho Shinkeigaku | 17-year-old with Hodgkin lymphoma presenting as paraneoplastic sensory neuropathy with cauda equina MRI enhancement; IVIg was used, bleomycin not mentioned in treatment |

> **Note:** All three references are indirect background literature. None directly investigates bleomycin as a treatment for cauda equina neoplasm. Evidence level remains L5.

---

## Singapore Market Information

Bleomycin is currently **not registered in Singapore** (0 marketing authorisations on record). No product registration table is available.

---

## Cytotoxicity

Bleomycin is an antineoplastic glycopeptide antibiotic; this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Glycopeptide antibiotic — DNA strand-break inducer) |
| Myelosuppression Risk | Low — bleomycin is notably marrow-sparing, which is why it is combined with myelosuppressive agents such as doxorubicin and cyclophosphamide in ABVD and BEP |
| Emetogenicity Classification | Low |
| Monitoring Items | Pulmonary function (DLCO, FVC) at baseline and every 2 cycles; chest HRCT if respiratory symptoms develop; cumulative lifetime dose tracking (do not exceed 400 IU total); renal function before each cycle (dose reduction required for CrCl < 50 mL/min); skin and mucous membrane assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations; closed-system transfer devices recommended; biohazard disposal required |

> **Critical Safety Warning:** Bleomycin pulmonary toxicity (BPT) is the dose-limiting adverse effect, occurring in 10–40% of patients and potentially fatal (pulmonary fibrosis). Risk is significantly elevated in elderly patients, those with pre-existing lung disease, cumulative doses > 400 IU, concurrent or subsequent high-concentration oxygen exposure, and prior or concurrent thoracic radiation. This toxicity is especially critical when considering indications with pulmonary involvement (e.g., rank 4: Primary Pulmonary Lymphoma).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Warnings, contraindications, and drug interaction data were not available in the current Evidence Pack (all listed as data gaps). Given bleomycin's well-characterised toxicity profile — pulmonary fibrosis, cutaneous reactions, and risk of fatal hyperpyrexic reactions on first administration — a complete review of the prescribing information is mandatory before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The L5 evidence for cauda equina neoplasm reflects indirect background associations with no clinical or preclinical basis for initiating a bleomycin study specifically targeting this entity. Furthermore, bleomycin is not registered in Singapore, and pursuing an unregistered drug for a model-only indication is not justified by the available data.

**To proceed with this specific prediction, the following is needed:**
- Identification of a histologically defined cauda equina tumour subtype with a biological rationale for bleomycin sensitivity (e.g., germ cell tumour with cauda equina extension, in which BEP would already be standard of care)
- Preclinical in vitro or in vivo data on bleomycin activity in the specific tumour histology
- MOA confirmation (DrugBank API query pending; currently a high-severity data gap)
- Singapore HSA regulatory pathway assessment for unregistered cytotoxic use
- Full prescribing information review for safety profiling

---

> **Supplementary Note — Higher-Priority Predictions in This Data Pack:**
> While cauda equina neoplasm holds the highest TxGNN model score (99.30%), the clinically actionable findings are found in higher-ranked evidence predictions:
>
> | Rank | Disease | Evidence Level | Decision |
> |------|---------|---------------|---------|
> | 3 | Reticulum Cell Sarcoma | **L1** (2 completed Phase 3 RCTs) | **Proceed with Guardrails** |
> | 8 | Interdigitating Dendritic Cell Sarcoma | **L3** (multiple ABVD case reports with CR) | Research Question |
> | 4 | Primary Pulmonary Lymphoma | **L2** (Phase 3 completed, n=500) | Research Question ⚠️ Pulmonary toxicity alert |
> | 2 | Adult Astrocytic Tumour | **L3** (Phase I intratumoral bleomycin) | Research Question |
>
> **Reticulum Cell Sarcoma is recommended as the priority target for a separate full-depth report.** It has the strongest evidence base (PMID 1699653: RCT directly testing bleomycin addition to CHOP; NCT00002565/NCT00002835: completed Phase 3 RCTs with bleomycin-containing alternating triple therapy) and a clear mechanistic link. Bleomycin is unregistered in Singapore and would require regulatory clearance regardless of indication.

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

