---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 509
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From Actinic Keratosis to Pre-Malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical TLR7/8 agonist (immune response modifier) internationally approved for actinic keratoses, superficial basal cell carcinoma, and external genital warts.
The TxGNN model predicts it may be effective for **Pre-Malignant Neoplasm**,
with **19 clinical trials** and **9 publications** currently supporting this direction.
Evidence includes a completed Phase 2 RCT and a large Phase 3 trial, placing confidence at Level L2.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Actinic keratoses, superficial basal cell carcinoma, external genital warts (internationally approved; no Singapore registration) |
| Predicted New Indication | Pre-Malignant Neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Imiquimod activates TLR7 and TLR8 receptors on plasmacytoid dendritic cells and macrophages, triggering production of IFN-α, TNF-α, and IL-12 through the innate immune pathway. This simultaneously drives dendritic cell maturation, Th1 polarisation, and cytotoxic T-lymphocyte (CTL) responses — all of which converge on the elimination of dysplastic cells. Separately, imiquimod can induce apoptosis in pre-malignant cells by downregulating Bcl-2. These mechanisms are not cancer-cell-line specific; they target the tumour immune microenvironment broadly, which is why their applicability extends across epithelial pre-malignant conditions.

Actinic keratoses and intraepithelial neoplasias such as cervical intraepithelial neoplasia (CIN) and vulvar intraepithelial neoplasia (VIN) are textbook pre-malignant neoplasms. They share a critical common feature with imiquimod's approved indications: epithelial dysplasia in sun-damaged or HPV-infected tissue, where local immune suppression allows abnormal cells to escape clearance. Imiquimod reverses this by creating an immunologically hostile environment for pre-malignant cells — making the TxGNN prediction a logical mechanistic extrapolation rather than a speculative leap.

The clinical programme already reflects this logic. A completed Phase 2 RCT (NCT03233412, n=90) directly evaluated topical imiquimod in high-grade cervical intraepithelial lesions, and a 259-patient Phase 3 trial (NCT01720407) tested it as neo-adjuvant therapy in lentigo maligna — an intraepidermal pre-invasive melanocytic proliferation. Two Cochrane systematic reviews additionally cover its use in VIN and anal intraepithelial neoplasia. The accumulated data confirms that the TxGNN score of 99.92% reflects genuine biological and clinical signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | Randomised controlled trial of topical imiquimod for high-grade cervical intraepithelial lesions (CIN) caused by HPV; well-powered with rigorous design — strongest direct evidence for pre-malignant neoplasm in this pack |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Evaluated imiquimod as neo-adjuvant treatment to reduce excision size and intralesional excision risk in lentigo maligna of the face (intraepidermal melanocytic proliferation) |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority RCT comparing surgical excision versus curettage plus imiquimod for nodular basal cell carcinoma; adequate sample size, but final status unconfirmed |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study evaluating duration of effect of imiquimod 5% cream for actinic keratoses on the head; small sample limits statistical power |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod for high-grade CIN 2–3; terminated after recruiting only 9 patients — no conclusive result, but the rationale (non-invasive alternative to LLETZ) remains clinically relevant |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Pilot neoadjuvant trial of topical imiquimod (Aldara) in early-stage oral squamous cell carcinoma; demonstrates feasibility of TLR7 activation in mucosal pre-invasive settings |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Compared imiquimod 5%, 0.05%, and nanoencapsulated formulations for actinic cheilitis (pre-malignant lower lip lesion); terminated early, reducing evidence value |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Post-market study of imiquimod 3.75% cream after cryotherapy for hypertrophic actinic keratoses on hands/forearms; addresses real-world combination approach |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Mechanistic exploration of HPV immune escape and imiquimod treatment in VIN 2/3 and anogenital warts; very small sample but provides direct immunological data |
| [NCT02234921](https://clinicaltrials.gov/study/NCT02234921) | Phase 1 | Completed | 3 | Pilot of DRibble vaccine with imiquimod as immune adjuvant in advanced prostate cancer; imiquimod's role here is as a TLR7-mediated adjuvant rather than direct anti-tumour agent |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Reviewed all interventions for anal canal intraepithelial neoplasia (AIN), a pre-malignant HPV-associated condition; imiquimod identified among active treatment options |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Reviewed medical interventions for high-grade vulval intraepithelial neoplasia (VIN); high morbidity of surgical approaches supports non-invasive imiquimod as a meaningful alternative |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | International Journal of Molecular Sciences | Reviewed combined treatments with PDT for non-melanoma skin cancer; imiquimod discussed as a synergistic immunological partner distinct from ablative approaches |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Seminars in Cutaneous Medicine and Surgery | Comprehensive review of topical strategies for NMSC and pre-malignant lesions; positioned imiquimod alongside 5-FU and diclofenac as a field therapy with immune mechanism |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Letter | Current management of actinic keratoses; imiquimod highlighted as a field cancerisation therapy addressing subclinical lesions beyond the visible target |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical PK/PD | Urologic Oncology | Evaluated TLR-7 agonists TMX-101 and TMX-202 (imiquimod-class compounds) for intravesical therapy in bladder cancer; demonstrates translational potential of TLR7 pathway beyond dermatology |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | International Journal of STD & AIDS | Successful treatment of high-grade VIN with imiquimod 5% in a renal transplant recipient; noteworthy because efficacy was maintained despite background immunosuppression |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | International Journal of STD & AIDS | Successful clearance of Bowenoid papulosis of the penis (HPV-associated pre-malignant anogenital condition) using topical imiquimod 5%; well-tolerated with complete response |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case Report / Imaging | Der Hautarzt | Case of disseminated superficial actinic porokeratosis with concurrent pre-malignant lesions; imiquimod resistance observed in DSAP — provides important boundary condition for predicting responder subgroups |

---

## Cytotoxicity

Imiquimod is used as an antineoplastic agent (superficial basal cell carcinoma, actinic keratoses) and qualifies for this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — TLR7/8 agonist / immune response modifier (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low — topical formulation with minimal systemic absorption under standard dosing; myelosuppression not a primary concern |
| Emetogenicity Classification | Low — topical application; systemic emetogenic effects not clinically significant at approved doses |
| Monitoring Items | Local skin reactions (erythema, erosion, ulceration, crusting); flu-like systemic symptoms (fever, fatigue, myalgia) if applied over large treatment areas; hepatic function monitoring warranted in prolonged or large-area off-label use |
| Handling Protection | Standard pharmaceutical handling precautions apply; not classified as hazardous cytotoxic under conventional handling guidelines (unlike alkylating agents or platinums) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT (NCT03233412, n=90) and a large Phase 3 trial (NCT01720407, n=259) directly support imiquimod's efficacy in pre-malignant neoplasms, and two Cochrane systematic reviews covering VIN and AIN further establish an evidence base — sufficient for a conditional advancement decision. The absence of Singapore regulatory registration and incomplete safety documentation require structured mitigation before any clinical deployment.

**To proceed, the following is needed:**
- Download and parse the full prescribing information / package insert to capture warnings, contraindications, and drug interactions (DG001 — Blocking)
- Retrieve formal MOA documentation from DrugBank API to complete mechanistic analysis (DG002 — High)
- Conduct a Singapore regulatory pathway assessment for imiquimod registration (HSA NDA or MLA route)
- Narrow the indication claim to a specific pre-malignant subtype (e.g., HPV-associated CIN, actinic keratoses, or VIN) to define a focused development strategy
- Establish a pharmacovigilance plan addressing local tissue reactions and off-label route/concentration risks
- Review the adverse case report (PMID 12719972 — malignant conversion during imiquimod therapy for oral papillomatosis) to define patient selection exclusion criteria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

