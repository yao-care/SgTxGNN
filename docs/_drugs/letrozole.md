---
layout: default
title: Letrozole
parent: High Evidence (L1-L2)
nav_order: 583
evidence_level: L1
indication_count: 10
---

# Letrozole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Letrozole: From Established Breast Cancer Use to Female Breast Carcinoma

## One-Sentence Summary

Letrozole is a nonsteroidal aromatase inhibitor that lowers estrogen production, and it is already marketed for hormone-receptor-positive breast cancer.
The TxGNN model predicts it is effective for **Female Breast Carcinoma**. This confirms an existing use rather than a true repurposing, and it is backed by **50 clinical trials** and **20 publications**, including several large Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Letrozole blocks aromatase, the enzyme that makes estrogen in peripheral tissue. Hormone-receptor-positive breast tumours depend on estrogen to grow, so lowering estrogen slows them down. The DrugBank mechanism-of-action field is empty in the Evidence Pack. The mechanism above comes from the repurposing rationale in the record.

Breast cancer is already an established, marketed use of letrozole, so this prediction confirms an existing indication. The trial evidence shows letrozole as a backbone endocrine therapy in the adjuvant, neoadjuvant and advanced settings. It is paired with CDK4/6 inhibitors (palbociclib, ribociclib), PI3K inhibitors (alpelisib) and others.

The prediction applies only to hormone-receptor-positive disease. That means postmenopausal women, or premenopausal women who also receive ovarian suppression. It should not be extended to ER-negative tumours.

---

## Clinical Trial Evidence

The table lists 10 of the 50 retrieved trials. Most are Phase 3 or large trials with direct relevance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | Completed | 666 | Double-blind trial of palbociclib + letrozole vs placebo + letrozole as first-line treatment for ER+/HER2- advanced breast cancer in postmenopausal women (PALOMA-2) |
| [NCT02278120](https://clinicaltrials.gov/study/NCT02278120) | Phase 3 | Completed | 672 | Ribociclib vs placebo added to an aromatase inhibitor (or tamoxifen) plus goserelin in premenopausal HR+/HER2- advanced breast cancer |
| [NCT00754845](https://clinicaltrials.gov/study/NCT00754845) | Phase 3 | Completed | 1918 | Letrozole vs placebo after 5 years of adjuvant aromatase inhibitor therapy (extended adjuvant use) |
| [NCT02338310](https://clinicaltrials.gov/study/NCT02338310) | Phase 3 | Active, not recruiting | 4486 | POETIC: perioperative aromatase inhibitor before standard adjuvant therapy in postmenopausal HR+ early breast cancer |
| [NCT00310180](https://clinicaltrials.gov/study/NCT00310180) | Phase 3 | Active, not recruiting | 10273 | TAILORx: hormone therapy alone vs hormone therapy plus chemotherapy, guided by Oncotype DX score |
| [NCT00171340](https://clinicaltrials.gov/study/NCT00171340) | Phase 3 | Completed | 1065 | Upfront vs delayed zoledronic acid to prevent bone loss in women on adjuvant letrozole |
| [NCT00171704](https://clinicaltrials.gov/study/NCT00171704) | Phase 3 | Completed | 263 | Effects of letrozole and tamoxifen on bone and lipids in postmenopausal women with early breast cancer |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | Completed | 131 | Palbociclib + letrozole access study in Latin America for HR+/HER2- advanced breast cancer (single-arm) |
| [NCT03056755](https://clinicaltrials.gov/study/NCT03056755) | Phase 2 | Completed | 383 | BYLieve: alpelisib + fulvestrant or letrozole in PIK3CA-mutant HR+/HER2- advanced breast cancer (non-comparative) |
| [NCT05163106](https://clinicaltrials.gov/study/NCT05163106) | Phase 2 | Completed | 85 | NEOLETRIB: presurgical ribociclib + letrozole in locally advanced breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | N Engl J Med | Letrozole vs tamoxifen as adjuvant treatment in postmenopausal women with hormone-receptor-positive early breast cancer (BIG 1-98) |
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT (Phase 2) | Breast Cancer Res Treat | PALOMA-1 overall survival: palbociclib + letrozole vs letrozole alone as first-line treatment for ER+/HER2- advanced breast cancer. Progression-free survival was significantly longer (median 20.2 vs 10.2 months) |
| [31838010](https://pubmed.ncbi.nlm.nih.gov/31838010/) | 2020 | RCT (Phase 2) | Lancet Oncol | CORALLEEN: neoadjuvant ribociclib + letrozole vs chemotherapy in postmenopausal luminal B breast cancer |
| [41519129](https://pubmed.ncbi.nlm.nih.gov/41519129/) | 2026 | Trial analysis | Cell Rep Med | NeoPAL: neoadjuvant letrozole-palbociclib vs chemotherapy (103 patients) reduced proliferation scores similarly in both arms |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | Cohort | Comput Math Methods Med | Efficacy, safety and prognosis of tamoxifen-then-letrozole sequence vs letrozole alone |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sci | Pharmacology, toxicity and therapeutic uses of letrozole in adjuvant, neoadjuvant and metastatic HR+ breast cancer |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast | Development of letrozole and its use in advanced and neoadjuvant breast cancer |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Pharmacodynamics, pharmacokinetics, efficacy and safety of letrozole |
| [17544670](https://pubmed.ncbi.nlm.nih.gov/17544670/) | 2007 | Review | Breast | Prescribing extended adjuvant letrozole, based on the MA-17 trial |
| [27235140](https://pubmed.ncbi.nlm.nih.gov/27235140/) | 2016 | Preclinical | Med Oncol | Letrozole changes carcinoma-associated fibroblasts, which may influence endocrine therapy efficacy |

---

## Singapore Market Information

The Evidence Pack lists 11 registrations. The first 5 are shown below. The pack has no approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN09915P | Femara Tablet 2.5 mg | Film-coated tablet | Novartis Pharma Stein AG / Novartis Farma S.p.A. |
| SIN13916P | Letrozole Mevon Tablets 2.5 mg | Film-coated tablet | Atlas Pharm, S.A. |
| SIN14406P | Lotuserm Film-Coated Tablets 2.5 mg | Film-coated tablet | Genepharm S.A. |
| SIN14470P | Letara Film Coated Tablet 2.5 mg | Film-coated tablet | Douglas Manufacturing Ltd |
| SIN15739P | Zatrolex Film-Coated Tablet 2.5 mg | Film-coated tablet | Genepharm S.A. |

---

## Cytotoxicity

Letrozole is an antineoplastic drug, but it is hormonal therapy rather than conventional cytotoxic chemotherapy. The Evidence Pack has no toxicity data for this section, so the ratings below reflect the drug class only.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted endocrine therapy (nonsteroidal aromatase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Low (drug-class expectation) |
| Emetogenicity Classification | Low (drug-class expectation) |
| Monitoring Items | Bone mineral density and lipids, which the retrieved Phase 3 trials examined; also liver function as clinically indicated |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

The retrieved trials point to these issues:
- **Bone loss**: several Phase 3 trials tested zoledronic acid to prevent bone loss in women on letrozole (NCT00171340, NCT00171314, NCT00376740).
- **Lipid effects**: NCT00171704 compared bone and lipid effects of letrozole and tamoxifen.
- **Musculoskeletal and hair symptoms**: trials on aromatase-inhibitor joint symptoms (NCT03384095) and alopecia (NCT01300871) reflect known tolerability concerns.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Letrozole has L1 evidence in breast cancer, including several completed Phase 3 RCTs, and is already marketed in Singapore. This is a confirmation of an existing use rather than new repurposing. The guardrail is to use it only in hormone-receptor-positive disease, in postmenopausal women or with ovarian suppression in premenopausal women.

Other predictions in the same set:
- ER-positive breast cancer: same conclusion as above (Proceed with Guardrails).
- ER-negative breast cancer: **Hold**, because letrozole is not expected to work without estrogen-driven tumour growth.
- Ehrlich tumour carcinoma, breast fibrocystic disease and benign mammary dysplasia: **Hold**, because of preclinical-only or no supporting evidence.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- HSA-approved indication text for the Singapore registrations
- DrugBank mechanism-of-action data
- A bone density and lipid monitoring plan, plus confirmation of receptor status and menopausal status before use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

