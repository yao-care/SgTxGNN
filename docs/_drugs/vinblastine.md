---
layout: default
title: Vinblastine
parent: 僅模型預測 (L5)
nav_order: 1058
evidence_level: L5
indication_count: 10
---

# Vinblastine
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

# Vinblastine: From Cytotoxic Chemotherapy to Rhabdomyosarcoma

## One-Sentence Summary

Vinblastine is a vinca alkaloid cytotoxic chemotherapy agent; the evidence pack does not provide a specific original indication text or approved label from the Singapore regulatory data (the drug is not currently registered/marketed there).
The TxGNN model predicts it may be effective for **Rhabdomyosarcoma**,
with **0 dedicated clinical trials** and **16 pieces of literature** (mostly case reports, mechanistic studies, and vinorelbine/vinca-alkaloid class evidence) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug not registered in Singapore; no `approved_indication_text` in evidence pack |
| Predicted New Indication | Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, vinblastine is a vinca alkaloid that binds tubulin and blocks microtubule polymerization, arresting cells in mitosis and inducing apoptosis. This mechanism is particularly effective against highly proliferative tumours, and rhabdomyosarcoma — a fast-growing embryonal soft-tissue sarcoma of skeletal muscle origin — fits this profile.

The repurposing rationale is largely extrapolated from the vinca alkaloid drug class rather than vinblastine-specific trial data: vinorelbine, a close analogue, is already incorporated into standard and metronomic paediatric sarcoma regimens (e.g., vinorelbine + low-dose cyclophosphamide protocols cited in the SFCE and pilot European rhabdomyosarcoma studies). Vinblastine itself appears in several historical combination regimens for rhabdomyosarcoma (e.g., cisplatin-vinblastine-bleomycin for prostatic rhabdomyosarcoma, and a 2023 case report where vinblastine-containing therapy produced a partial response in perianal rhabdomyosarcoma), and preclinical xenograft studies confirm differential vinca-alkaloid sensitivity across paediatric rhabdomyosarcoma cell lines.

Overall, the mechanistic plausibility is strong (microtubule inhibition against a highly mitotic embryonal tumour), and class-level clinical precedent exists, but direct vinblastine-specific prospective trial evidence in rhabdomyosarcoma is currently lacking.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase II (vinorelbine) | Eur J Cancer | Vinorelbine + low-dose oral cyclophosphamide showed good tolerance and efficacy in relapsed/refractory rhabdomyosarcoma (SFCE study) |
| [41216926](https://pubmed.ncbi.nlm.nih.gov/41216926/) | 2026 | Cooperative Group Study | Pediatr Blood Cancer | CWS-96/CWS-2002P trials evaluated chemotherapy regimens across soft tissue sarcoma risk groups, informing paediatric sarcoma treatment stratification |
| [22156656](https://pubmed.ncbi.nlm.nih.gov/22156656/) | 2011 | Pilot Study | Oncotarget | Pilot study of a pediatric metronomic 4-drug regimen (including vinca alkaloid) as an alternative strategy against resistant paediatric cancer |
| [15378498](https://pubmed.ncbi.nlm.nih.gov/15378498/) | 2004 | Pilot Study (vinorelbine) | Cancer | Vinorelbine + low-dose cyclophosphamide pilot study informing the upcoming European Rhabdomyosarcoma Protocol |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Clinical Study (vinorelbine) | Cancer | Demonstrated evidence of vinorelbine activity specifically in rhabdomyosarcoma among previously treated advanced paediatric sarcomas |
| [38050209](https://pubmed.ncbi.nlm.nih.gov/38050209/) | 2023 | Case Report | Medicine | Adult perianal rhabdomyosarcoma achieved partial response after nivolumab, dacarbazine, cisplatin, and **vinblastine** combination therapy |
| [2451411](https://pubmed.ncbi.nlm.nih.gov/2451411/) | 1987 | Case Report/Review | Hinyokika Kiyo | Refractory prostatic rhabdomyosarcoma in a child: cisplatin + **vinblastine** + peplomycin (PVP) regimen rapidly reduced pelvic tumour mass |
| [3329524](https://pubmed.ncbi.nlm.nih.gov/3329524/) | 1987 | Mechanistic/In vitro | Anti-Cancer Drug Design | Vinca alkaloid (including vinblastine) therapeutic selectivity examined in human rhabdomyosarcoma xenograft models |
| [26024389](https://pubmed.ncbi.nlm.nih.gov/26024389/) | 2015 | Mechanistic/In vitro | Cell Death Differ | Identified synthetic lethality between PLK1 inhibitors and microtubule-destabilizing drugs (vinca-alkaloid class) in preclinical rhabdomyosarcoma models |
| [16302215](https://pubmed.ncbi.nlm.nih.gov/16302215/) | 2007 | Case Report | Pediatr Blood Cancer | Vinorelbine/low-dose cyclophosphamide regimen "claimed to be effective for rhabdomyosarcoma" also showed response in desmoplastic small round cell tumor |

---

## Singapore Market Information

Vinblastine is currently not registered or marketed in Singapore (0 authorizations recorded in the evidence pack).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid class — tubulin polymerization inhibitor) |
| Myelosuppression Risk | High — vinca alkaloids are classically dose-limiting for neutropenia; literature confirms myelosuppressive effects of vinblastine (e.g., studies on modifying agents for vinblastine-induced myelosuppression) |
| Emetogenicity Classification | Low to Moderate (typical for vinca alkaloid class) |
| Monitoring Items | CBC with differential, liver function (hepatic metabolism/clearance), neurological exam (peripheral neuropathy), injection-site monitoring (vesicant — risk of extravasation injury) |
| Handling Protection | Must follow cytotoxic drug handling regulations; vesicant precautions required during administration |

---

## Safety Considerations

Please refer to the package insert for safety information. No specific warnings, contraindications, or drug interaction data were available in the evidence pack (a data gap flagged as **Blocking** for safety pre-screening — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (rhabdomyosarcoma) sits at Evidence Level L3, supported mainly by case reports, mechanistic/preclinical studies, and class-level (vinorelbine) clinical data rather than vinblastine-specific prospective trials. This is compounded by a **Blocking** data gap — the absence of TFDA/HSA label warnings and contraindications — which prevents completion of the S1 safety pre-screening, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (Blocking gap — required for S1 safety screening)
- DrugBank-sourced mechanism of action detail for formal mechanistic-link analysis
- Vinblastine-specific (not vinorelbine) clinical trial data in rhabdomyosarcoma to raise evidence level beyond L3
- Route compatibility and dosing feasibility assessment given the drug is not locally registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

