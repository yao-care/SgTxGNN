---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma / Eyelash Hypotrichosis to Alopecia

## One-Sentence Summary

Bimatoprost (Lumigan / Latisse) is a synthetic prostamide F2α analogue originally approved for treating ocular hypertension and open-angle glaucoma, with a secondary FDA approval for eyelash hypotrichosis arising from an observed side effect in glaucoma patients.
The TxGNN model predicts it may be effective for **Alopecia** (hair loss) — an anatomically adjacent extension of its already-approved eyelash indication —
with **11 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ocular hypertension / Open-angle glaucoma; Eyelash hypotrichosis (FDA-approved Latisse) |
| Predicted New Indication | Alopecia (hair loss, including androgenetic alopecia and alopecia areata) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Bimatoprost acts as a synthetic prostamide F2α analogue with high affinity for the FP (prostaglandin F) receptor. In the eye, FP receptor activation reduces aqueous humour production and lowers intraocular pressure — the mechanism underlying its use in glaucoma. An unexpected but consistent finding in glaucoma patients receiving bimatoprost eyedrops was increased eyelash length, thickness, and pigmentation. This observation was systematically studied and led to the FDA approval of Latisse (bimatoprost 0.03%) for eyelash hypotrichosis — the first and only FDA-approved treatment for this indication.

The connection to scalp alopecia is mechanistically direct. Hair follicles throughout the body share the same FP receptor pathway. Bimatoprost promotes the transition of follicles from telogen (resting) into anagen (active growth) phase and extends the duration of anagen. This is precisely the mechanism disrupted in androgenetic alopecia (AGA), where DHT progressively shortens anagen and miniaturises follicles, and in alopecia areata, where immune-mediated attack disrupts the hair cycle. The FP-receptor route operates independently of the androgen pathway, making bimatoprost a potentially complementary or alternative option to finasteride and minoxidil.

Critically, this is not merely theoretical. Three large completed Phase 2 trials — two with over 300 participants each, covering both male AGA and female pattern hair loss — directly tested topical bimatoprost on the scalp. The mechanistic leap from eyelash to scalp represents an anatomical extension rather than a fundamentally new biological question, which is why TxGNN assigns a near-perfect score and why the clinical evidence base has grown significantly over the past decade.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | Three doses of bimatoprost solution vs vehicle and open-label minoxidil 5% in male AGA; the largest and most pivotal bimatoprost scalp efficacy trial |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | Mirror design to NCT01325337 in women with female pattern hair loss (FPHL); bimatoprost vs vehicle and minoxidil 2% — together these two trials provide the broadest gender coverage |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy of bimatoprost in male AGA; a second core Phase 2 efficacy dataset confirming the dose-response relationship |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | CO2 fractional laser combined with bimatoprost 0.03% in alopecia areata; evaluated whether bimatoprost augments hair regrowth following laser-induced immune disruption |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Mechanistic investigation of bimatoprost on androgen-dependent scalp follicles; provided biological marker data supporting FP-receptor-mediated anagen promotion |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | N/A | Completed | 14 | Randomised comparison of latanoprost vs bimatoprost ophthalmic solution for eyelash regrowth in alopecia areata; early proof-of-concept for PGF2α analogues in AA |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Post-marketing safety and efficacy of bimatoprost 0.03% for eyelash hypotrichosis in children; confirms paediatric tolerability of the core eyelash indication |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Scalp pharmacokinetics and tolerability of two bimatoprost formulations over 14 days in male AGA; characterised dermal absorption profile |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety, tolerability, and PK of a new bimatoprost topical formulation in alopecia patients; supported formulation development for scalp delivery |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminated | 53 | Dose-escalation safety and PK study in male AGA; terminated early without completing full efficacy data collection |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | RCT / Clinical Study | Archives of Dermatological Research | CO2 fractional laser + bimatoprost significantly enhanced hair regrowth in alopecia areata compared with laser alone; supports bimatoprost as an adjunct in AA |
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Systematic Review | J Dermatological Treatment | Network meta-analysis of all non-surgical AGA treatments in men and women; bimatoprost included and compared against minoxidil, finasteride, and other agents |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Prospective Non-Randomised | Indian Dermatology Online Journal | Bimatoprost vs clobetasol propionate in scalp alopecia areata; bimatoprost showed comparable hair regrowth with a favourable safety profile |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Prospective Cohort | Dermatologic Therapy | Prospective study of bimatoprost ophthalmic solution for eyelash loss in alopecia totalis and universalis; 16/19 evaluable patients showed clinically meaningful regrowth |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opinion on Investigational Drugs | Comprehensive review of bimatoprost for eyelash, eyebrow, and scalp alopecia; covers mechanism, clinical evidence, and positioning relative to standard of care |
| [23104985](https://pubmed.ncbi.nlm.nih.gov/23104985/) | 2013 | Mechanistic / Case Series | FASEB Journal | Foundational paper proposing prostamide-related therapy for scalp alopecias; demonstrated bimatoprost effects on human scalp follicles ex vivo |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | Review | Indian Dermatology Online Journal | Overview of bimatoprost in dermatology; documents the pathway from glaucoma side effects to purposeful use in eyelashes, scalp alopecia, and vitiligo |
| [37185388](https://pubmed.ncbi.nlm.nih.gov/37185388/) | 2023 | Review | Current Oncology | Prevention and treatment of chemotherapy-induced alopecia; bimatoprost noted as an emerging topical option for CIA |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Clinical Guideline | Journal of Dermatology | Japanese 2017 guidelines for male/female pattern hair loss; includes review of emerging therapies including PGF2α analogues |
| [27377163](https://pubmed.ncbi.nlm.nih.gov/27377163/) | 2016 | Case Report | Pediatric Dermatology | Steroid-resistant multifocal scalp AA in a child successfully treated with topical bimatoprost; supports off-label use in paediatric refractory AA |

---

## Singapore Market Information

Bimatoprost is currently **not registered with HSA Singapore**. No product licences were identified as of the data cutoff (2026-06-01).

For reference, bimatoprost is available internationally under the following brand names:

| Brand Name | Indication | Regulatory Status |
|-----------|-----------|------------------|
| Lumigan (Allergan/AbbVie) | Glaucoma / Ocular hypertension | FDA-approved (USA); approved in EU, Japan, and many other markets |
| Latisse (Allergan/AbbVie) | Eyelash hypotrichosis | FDA-approved (USA, 2008) |

Registration in Singapore via HSA would be required before any local clinical use.

---

## Safety Considerations

Detailed local safety data (HSA-registered package insert warnings and contraindications) are not available for Singapore as the drug is not registered. Based on the internationally approved prescribing information, the following are known considerations:

- **Known ocular side effects (ophthalmic use):** Conjunctival hyperaemia, gradual iris pigmentation change (irreversible), periorbital fat atrophy, and eyelid ptosis with prolonged periocular application
- **Respiratory caution:** Systemic prostaglandin activity may trigger bronchospasm; use with caution in patients with asthma or COPD
- **Pigmentation effects:** Increased skin and hair pigmentation at application sites reported; relevant for scalp applications

Please refer to the full Lumigan and Latisse prescribing information for complete safety details before clinical use.

---

## Appendix: Other TxGNN-Predicted Indications

The TxGNN model returned 10 predictions for bimatoprost. The table below summarises all ranked predictions with their evidence status:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Notes |
|------|---------------------|-------------|---------------|---------------|-------|
| 1 | Malformation syndrome with periodontal component | 99.997% | L5 | Hold | No bimatoprost-specific evidence; 20 general periodontal papers; likely graph false positive via indirect prostaglandin–periodontium nodes |
| 2 | Syndrome with Dandy-Walker malformation | 99.997% | L5 | Hold | Congenital posterior fossa malformation; no known FP-receptor connection; 0 trials, 0 papers |
| 3 | Isolated genetic hair shaft abnormality | 99.997% | L5 | Hold | Structural keratin/desmoplakin gene defect; bimatoprost cannot correct protein structure; 0 evidence |
| 4 | Ambras-type hypertrichosis universalis congenita | 99.997% | L5 | Hold | Congenital excessive hair growth — bimatoprost would worsen the condition; mechanistically contraindicated |
| 5 | Hypotrichosis simplex of the scalp | 99.996% | L3 | Research Question | Mechanistically plausible extension of Latisse indication to scalp; no dedicated trials yet |
| 6 | Congenital hypotrichosis with milia | 99.995% | L5 | Hold | Genetic skin appendage developmental defect; unclear whether growth-phase promotion can overcome developmental gene defects |
| 7 | Diffuse alopecia areata | 99.993% | L3 | Research Question | Plausible via FP-receptor anagen promotion; trials on patchy AA exist (NCT05600673) but diffuse subtype needs specific validation |
| **8** | **Alopecia** | **99.993%** | **L2** | **Proceed with Guardrails** | **Best-evidenced prediction; 11 clinical trials including 3 Phase 2 trials (n > 250 each); see main report above** |
| 9 | Genetic alopecia | 99.966% | L3 | Research Question | Androgenetic alopecia is polygenic; bimatoprost provides a non-androgenic (FP receptor) complementary pathway |
| 10 | Pulmonary arteriovenous malformation | 99.955% | L5 | Hold | Vascular structural anomaly (HHT/ALK1 pathway); no overlap with FP receptor signalling; graph false positive |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 2 trials enrolling over 850 participants collectively have evaluated topical bimatoprost in androgenetic alopecia and female pattern hair loss. The mechanism — FP receptor-mediated anagen promotion — is a direct, anatomically adjacent extension of Latisse's FDA-approved eyelash indication, making this the most scientifically credible repurposing candidate in the dataset. However, Phase 2 results for scalp AGA have shown mixed primary endpoint outcomes, and no Phase 3 trial has been completed for scalp indications.

**To proceed, the following is needed:**

- **Regulatory pathway:** Register bimatoprost with HSA Singapore; no local approval currently exists
- **Formulation development:** Standard 0.03% ophthalmic solution has suboptimal scalp bioavailability; enhanced permeation formulations (e.g., spanlastics, co-solvent systems) are under preclinical investigation and should be prioritised
- **Target population definition:** Clearly delineate between AGA (androgenetic alopecia), alopecia areata subtypes (patchy, diffuse, totalis/universalis), and chemotherapy-induced alopecia — each may require different dosing and endpoints
- **Phase 3 evidence:** No Phase 3 trial for scalp AGA has been completed; this is the key evidence gap before regulatory submission for a new indication
- **Safety data package:** Obtain full HSA-relevant safety dossier including DDI data, contraindications, and local labelling requirements
- **Mechanistic action data (MOA):** Formal DrugBank/SmPC documentation of the FP-receptor mechanism should be retrieved to support any regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

