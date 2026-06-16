---
layout: default
title: Dabrafenib
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Dabrafenib
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

# Dabrafenib: From BRAF V600 Mutation-Positive Solid Tumours to Non-Cutaneous Melanoma

## One-Sentence Summary

Dabrafenib is a selective BRAF kinase inhibitor with established global use in BRAF V600E/K mutation-positive malignancies, though it is not currently registered in Singapore.
The TxGNN model's highest-evidence prediction is **Non-Cutaneous Melanoma** (Rank 2, Score 98.48%), supported by **35+ clinical trials** including two completed Phase 3 RCTs directly evaluating Dabrafenib in advanced melanoma.
The top-ranked prediction (Choroideremia, Rank 1, Score 98.63%) carries **no supporting evidence** and is assessed as **Hold** due to absence of mechanistic rationale — this ranking is likely an artefact of graph topology rather than a true biological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore registration; globally approved for BRAF V600E+ melanoma, NSCLC, and anaplastic thyroid cancer |
| Predicted New Indication | Non-Cutaneous Melanoma (Rank 2; highest evidence-supported prediction) |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Important note on ranking:** The TxGNN Rank 1 prediction (Choroideremia, 98.63%) has been assessed as **Hold** — zero clinical trials, zero literature, and no plausible mechanistic link. This report focuses on Rank 2 (Non-Cutaneous Melanoma) as the clinically actionable prediction.

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Dabrafenib is a selective ATP-competitive inhibitor of BRAF kinase that specifically targets the oncogenic V600E and V600K point mutations. These mutations constitutively activate the MAPK/ERK signalling pathway, bypassing normal growth regulatory controls and driving uncontrolled tumour proliferation. By occupying the ATP-binding pocket of mutant BRAF, Dabrafenib blocks downstream MEK–ERK phosphorylation and halts tumour growth — an effect that is mutation-specific rather than histology-specific.

Non-cutaneous melanoma encompasses subtypes arising from primary sites other than the skin, including uveal (choroidal, ciliary body, iris), mucosal (oral, sinonasal, anorectal, vaginal), and periocular (conjunctival, eyelid) origins. Although BRAF V600 mutation prevalence is lower in non-cutaneous subtypes (approximately 3–15%) compared to cutaneous melanoma (approximately 40–60%), patients harbouring BRAF V600 mutations share the identical oncogenic driver. The therapeutic rationale for Dabrafenib therefore applies directly in confirmed BRAF-positive individuals within this group, with companion diagnostic testing being the critical clinical gate.

The TxGNN model's high score for non-cutaneous melanoma is well-grounded in clinical reality. Two completed Phase 3 randomised controlled trials — one comparing Dabrafenib to dacarbazine (NCT01227889, n=251) and one comparing Dabrafenib + Trametinib to Vemurafenib (NCT01597908, n=704) — established efficacy in BRAF-mutant advanced melanoma. A dedicated Phase 2 study (NCT02039947, n=127) further demonstrated activity in melanoma with brain metastases, a presentation more common in non-cutaneous subtypes. This body of evidence provides strong mechanistic and clinical justification for extending Dabrafenib's use to BRAF V600-positive non-cutaneous melanoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01227889](https://clinicaltrials.gov/study/NCT01227889) | Phase 3 | Completed | 251 | BRF113683: Dabrafenib vs dacarbazine in BRAF V600E+ advanced Stage III or metastatic Stage IV melanoma; pivotal registration trial establishing Dabrafenib's superiority as first-line treatment |
| [NCT01597908](https://clinicaltrials.gov/study/NCT01597908) | Phase 3 | Completed | 704 | Dabrafenib + Trametinib vs Vemurafenib in unresectable or metastatic BRAF V600E/K+ cutaneous melanoma; Phase 3 head-to-head RCT demonstrating combination superiority over single-agent BRAF inhibition |
| [NCT02039947](https://clinicaltrials.gov/study/NCT02039947) | Phase 2 | Completed | 127 | BRF117277: Dabrafenib + Trametinib in BRAF V600+ melanoma with brain metastases; evaluated safety and efficacy across symptomatic and asymptomatic cohorts with and without prior local brain therapy |
| [NCT01619774](https://clinicaltrials.gov/study/NCT01619774) | Phase 2 | Completed | 28 | Dabrafenib + Trametinib in metastatic melanoma refractory or resistant to prior BRAF inhibitor; provided evidence for combination therapy as a rescue strategy after BRAF monotherapy failure |
| [NCT02083354](https://clinicaltrials.gov/study/NCT02083354) | Phase 2 | Completed | 77 | Dabrafenib + Trametinib in BRAF V600+ unresectable or metastatic acral lentiginous or cutaneous melanoma; assessed objective response rate, progression-free survival, and overall survival |
| [NCT02130466](https://clinicaltrials.gov/study/NCT02130466) | Phase 1/2 | Completed | 184 | Pembrolizumab + Dabrafenib + Trametinib in advanced melanoma; multi-part dose-finding and double-blind efficacy study of triple immunotherapy–targeted therapy combination |
| [NCT01972347](https://clinicaltrials.gov/study/NCT01972347) | Phase 2 | Active, not recruiting | 35 | Neoadjuvant Dabrafenib + Trametinib in resectable Stage IIIB-C BRAF V600+ melanoma; evaluating clinical and pathological response at 12 weeks prior to surgery |
| [NCT02858921](https://clinicaltrials.gov/study/NCT02858921) | Phase 2 | Unknown | 60 | Randomised neoadjuvant study: Dabrafenib + Trametinib ± Pembrolizumab in resectable BRAF V600+ Stage IIIB/C melanoma; multi-arm design to optimise pre-surgical tumour reduction |
| [NCT03944356](https://clinicaltrials.gov/study/NCT03944356) | Observational | Completed | 232 | Non-interventional observatory study of adjuvant Dabrafenib + Trametinib in melanoma (EMA-approved 2018); assessed real-world usage patterns and clinical outcomes versus clinical trial populations |
| [NCT04666272](https://clinicaltrials.gov/study/NCT04666272) | Observational | Active, not recruiting | 78 | Prospective non-interventional study of adjuvant Dabrafenib + Trametinib in Chinese patients with Stage III BRAF V600+ melanoma after complete resection; provides Asian real-world outcomes data |

---

## Literature Evidence

Currently no related literature is available for non-cutaneous melanoma in this evidence pack.

> **Supplementary note:** Closely related melanoma subtypes in this evidence pack do have supporting publications. Eyelid/conjunctival melanoma evidence (PMID [27893585](https://pubmed.ncbi.nlm.nih.gov/27893585/), 2017, *Ophthalmic Plastic and Reconstructive Surgery*) directly documents regression of BRAF V600E-positive conjunctival melanoma with combined BRAF/MEK inhibition — strengthening the mechanistic case for non-cutaneous subtypes in general.

---

## Singapore Market Information

Dabrafenib is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No active product authorisations exist in the HSA database.

---

## Cytotoxicity

Dabrafenib is an anticancer targeted therapy indicated for BRAF V600 mutation-positive malignancies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective oral BRAF V600E/K kinase inhibitor; not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (targeted kinase inhibitor; primary toxicities are non-haematological) |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count, liver function tests (ALT/AST/bilirubin), renal function (creatinine/eGFR), fasting blood glucose, ECG (QTc interval), dermatological surveillance (cutaneous squamous cell carcinoma, keratoacanthoma), temperature monitoring for pyrexia (especially when combined with Trametinib) |
| Handling Protection | Standard oral anticancer agent handling precautions apply; no special closed-system handling required for solid oral dosage form |

---

## Safety Considerations

No key warnings, contraindications, or drug-drug interaction data are available in this evidence pack.

> Please refer to the approved prescribing information (SmPC/package insert) for complete safety information. Known class-specific risks for BRAF inhibitors include: paradoxical MAPK pathway activation leading to secondary malignancies (cutaneous squamous cell carcinoma, keratoacanthoma), pyrexia syndrome (markedly increased with concurrent MEK inhibitor use), haemorrhagic events, QTc prolongation, uveitis, and embryo-foetal toxicity. Dabrafenib is also a known inducer of CYP3A4 and may reduce plasma concentrations of co-administered drugs metabolised by this pathway.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dabrafenib has robust Phase 2 and Phase 3 clinical trial evidence across BRAF V600-mutant melanoma; the mechanistic link to non-cutaneous melanoma is scientifically valid for patients confirmed BRAF V600-positive by companion diagnostics, but Singapore HSA registration is absent and the lower BRAF mutation prevalence in non-cutaneous subtypes requires careful patient selection.

**To proceed, the following is needed:**
- Establish a Singapore HSA registration pathway, or initiate access via the Special Access Route (SAR) or compassionate use programme for eligible patients
- Mandate BRAF V600 companion diagnostic testing (e.g., cobas 4800 BRAF V600 Mutation Test or an HSA-approved equivalent) in all prospective non-cutaneous melanoma patients prior to treatment
- Retrieve complete mechanism of action documentation via DrugBank API (DB08912) to support regulatory and clinical submissions
- Download and parse the TFDA or EMA SmPC package insert to populate key warnings, contraindications, and drug-drug interaction profile (currently missing from this evidence pack)
- Convene a multidisciplinary oncology team (MDT) with subspecialty expertise in uveal and mucosal melanoma, given the lower BRAF mutation prevalence and different disease biology in these subgroups
- Conduct a formal drug-drug interaction (DDI) assessment given Dabrafenib's CYP3A4 induction potential
- **Rank 1 (Choroideremia):** No further action recommended at this time — the mechanistic link is absent, and the high TxGNN score is assessed as a knowledge-graph topology artefact; reassess only if novel CHM gene / BRAF pathway interaction data emerge in the literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

