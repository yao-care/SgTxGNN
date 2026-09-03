---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 759
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib: From Renal Cell Carcinoma & Soft Tissue Sarcoma to Liposarcoma

## One-Sentence Summary

Pazopanib is an oral multi-target tyrosine kinase inhibitor already used as standard-of-care for advanced clear-cell renal cell carcinoma and non-adipocytic soft tissue sarcoma. The TxGNN model predicts it may also be effective for **liposarcoma**, and this direction is already supported by **9 clinical trials** (3 of them liposarcoma-specific Phase 2 studies) and **20 publications**, including a published single-arm Phase 2 trial and a randomized Phase 2 study. Note: this evidence pack bundles 10 TxGNN-ranked disease candidates for pazopanib — liposarcoma is featured here because it carries the strongest, most directly matched evidence; two other well-supported candidates (dermatofibrosarcoma protuberans and fibroblastic neoplasm/desmoid tumor) are summarized at the end.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced/metastatic clear-cell renal cell carcinoma; non-adipocytic soft tissue sarcoma (per literature in this pack; not a formally recorded field in `drug.original_indications`) |
| Predicted New Indication | Liposarcoma (unresectable / metastatic) |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is flagged as a data gap in this pack (DG002, High severity — pending DrugBank API lookup). Based on the mechanistic information embedded in the trial and literature evidence, pazopanib is a multi-target tyrosine kinase inhibitor acting on VEGFR-1/2/3, PDGFR-α/β, and c-KIT, giving it antiangiogenic and antitumor activity. This mechanism is already the basis of its established use in renal cell carcinoma and non-adipocytic soft tissue sarcoma (approved via the PALETTE trial pathway referenced repeatedly in the literature evidence).

Liposarcoma is a highly vascularized, angiogenesis-dependent tumor, and the dedifferentiated subtype in particular carries PDGFRA amplification — a preclinical xenograft study in this pack (PMID 30060824) shows pazopanib directly regressing a PDGFRA-amplified pleomorphic liposarcoma model. This gives a specific molecular rationale beyond the general "TKI works in sarcoma" argument.

Clinically, this is not a purely theoretical extension: pazopanib is already used off-label/on NCCN guidance as a later-line option across non-adipocytic soft tissue sarcoma, and three trials in this pack (NCT01506596, NCT01692496, NCT01532687) were designed specifically for liposarcoma, with results published in *Cancer* (PMID 28832986) and further supported by a randomized Phase 2 (PAPAGEMO, PMID 33355646). The prediction therefore represents a plausible extension of an already-adjacent, mechanistically related indication rather than a speculative leap.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | Completed | 42 | Single-agent pazopanib in unresectable/metastatic liposarcoma — direct efficacy/safety evaluation |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | Completed | 52 | Pazopanib activity/tolerability in relapsed or refractory advanced/metastatic liposarcoma |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 (randomized, double-blind) | Completed | 54 | Gemcitabine ± pazopanib in refractory soft tissue sarcoma, including liposarcoma |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | Completed | 178 | Pazopanib + oral topotecan in metastatic/non-resectable soft tissue and bone sarcomas |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Active, not recruiting | 140 | Neoadjuvant chemoradiation ± pazopanib in non-rhabdomyosarcoma soft tissue sarcoma (includes liposarcoma) |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | Recruiting | 139 | Risk-adapted maintenance pazopanib + dose-escalated radiotherapy + selinexor in NRSTS |
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | Regorafenib (not pazopanib) vs. placebo post-anthracycline STS, liposarcoma cohort — indirect comparator evidence |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: oral regorafenib (not pazopanib) in selected sarcoma subtypes — indirect, cites pazopanib activity precedent |
| [NCT06263231](https://clinicaltrials.gov/study/NCT06263231) | Phase 3 | Active, not recruiting | 333 | Intratumoral INT230-6 (not pazopanib) vs. US standard of care in liposarcoma/UPS/leiomyosarcoma — comparator trial, not direct evidence |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28832986](https://pubmed.ncbi.nlm.nih.gov/28832986/) | 2017 | Phase 2 trial (primary results) | Cancer | Prospective, single-arm, multicenter Phase 2 study establishing activity/safety of single-agent pazopanib in unresectable/metastatic liposarcoma |
| [33355646](https://pubmed.ncbi.nlm.nih.gov/33355646/) | 2021 | RCT (Phase 2) | JAMA Oncology | PAPAGEMO trial final results: pazopanib ± gemcitabine in anthracycline/ifosfamide-refractory soft tissue sarcoma |
| [36890471](https://pubmed.ncbi.nlm.nih.gov/36890471/) | 2023 | Randomized Phase 2 protocol | BMC Cancer | JCOG1802 (2ND-STEP): second-line trabectedin vs. eribulin vs. pazopanib in advanced STS |
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Phase 2 trial report | Expert Opinion on Investigational Drugs | Liposarcoma-specific review of pazopanib as a multi-target TKI with antiangiogenic/antitumorigenic activity |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Phase 2 trial | British Journal of Cancer | Pazopanib + oral topotecan in metastatic/non-resectable soft tissue and bone sarcomas |
| [34356494](https://pubmed.ncbi.nlm.nih.gov/34356494/) | 2021 | Translational cohort | Biology | GISG-04/NOPASS: molecular/pathological profiling of neoadjuvant pazopanib-treated high-risk STS samples |
| [25500074](https://pubmed.ncbi.nlm.nih.gov/25500074/) | 2014 | Preclinical | Translational Oncology | Pazopanib suppresses tumor growth via antiangiogenesis in dedifferentiated liposarcoma xenograft models |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | Case report (PDX model) | Tissue & Cell | Doxorubicin-resistant PDGFRA-amplified pleomorphic liposarcoma regressed by pazopanib in patient-derived xenograft |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncology Research and Treatment | Established and experimental systemic treatment options for advanced liposarcoma |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Review | Current Treatment Options in Oncology | Systemic therapy landscape for dedifferentiated liposarcoma, including TKI options |

## Singapore Market Information

Pazopanib currently holds **no marketing authorization in Singapore** (0 registrations recorded). No authorization number, product name, or approved indication text is available in this evidence pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — multi-target tyrosine kinase inhibitor (VEGFR-1/2/3, PDGFR-α/β, c-KIT), not a conventional cytotoxic agent |
| Myelosuppression Risk | Not specified in this evidence pack; TKI-class agents generally carry lower myelosuppression risk than cytotoxic chemotherapy, but combination regimens (e.g., + gemcitabine, + topotecan) seen in the trial evidence above are expected to increase this risk — please refer to the package insert |
| Emetogenicity Classification | Not specified in this evidence pack — refer to package insert |
| Monitoring Items | Liver function tests, blood pressure, urinalysis (proteinuria), and CBC are standard for this TKI class; specific monitoring schedule not provided in this pack |
| Handling Protection | Not specified in this evidence pack — as an oral oncolytic, confirm institutional hazardous-drug handling requirements against current NIOSH/local guidance |

## Safety Considerations

Please refer to the package insert for safety information. (`safety.key_warnings`, `safety.contraindications`, and DDI query all returned no data in this evidence pack; DG001 — TFDA/HSA label warnings — is flagged as a Blocking gap.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Liposarcoma has L2 evidence: three dedicated Phase 2 trials (including a published single-arm pivotal study and a randomized PAPAGEMO trial) plus a specific molecular rationale (PDGFRA amplification in dedifferentiated liposarcoma). This is meaningfully stronger than a model-only prediction, but Singapore-specific regulatory and safety data are still missing.

**To proceed, the following is needed:**
- TFDA/HSA label warnings and contraindications (DG001, Blocking) — required before any S1 safety pre-assessment
- Full mechanism-of-action data via DrugBank API (DG002, High)
- A Singapore marketing-authorization pathway assessment, since pazopanib is not currently registered there
- Subtype-level stratification of efficacy/safety data (dedifferentiated vs. myxoid/round-cell vs. pleomorphic liposarcoma), since PDGFRA amplification — the strongest mechanistic link — is not universal across subtypes

---

### Other Candidate Indications in This Bundle

This evidence pack scored pazopanib against 10 diseases; two others also reached L2/actionable evidence levels and may warrant their own dedicated reports:

| Disease | Evidence Level | Decision Stage | Recommendation | Key Support |
|------|------|------|------|------|
| Dermatofibrosarcoma protuberans | L2 | S3 | Proceed with Guardrails | Dedicated multicenter Phase 2 (PMID 32956651, JID 2021); strong mechanistic fit via COL1A1-PDGFB fusion driving PDGFR-β activation |
| Fibroblastic neoplasm (incl. desmoid tumor / solitary fibrous tumor) | L2 | S2 | Research Question | Multiple subtype-specific Phase 2 studies (e.g., PMID 30578023, Lancet Oncology) and real-world registries, but "fibroblastic neoplasm" is a heterogeneous umbrella term requiring subtype-specific follow-up |

The remaining candidates (Xp11.2-translocation RCC, unclassified RCC, RCC with neuroblastoma, childhood RCC, ovarian myxoid liposarcoma, heart fibrosarcoma, kidney fibrosarcoma) have L3–L5 evidence with weak or no direct clinical/literature support and remain at **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

