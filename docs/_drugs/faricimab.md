---
layout: default
title: Faricimab
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Faricimab
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

# Faricimab: From Neovascular Age-Related Macular Degeneration to Diabetic Retinopathy

## One-Sentence Summary

Faricimab (Vabysmo®) is a bispecific antibody simultaneously targeting VEGF-A and Angiopoietin-2, approved in the United States since January 2022 for neovascular age-related macular degeneration (nAMD) and diabetic macular edema (DME).
The TxGNN model identifies **Diabetic Retinopathy** as the highest-evidence prediction for this drug, supported by **25 clinical trials** and **20 publications** — yielding an evidence level of **L1**.
Note: The majority of the top-10 TxGNN-ranked predictions for this drug (ranks 1–5, 7, 9–10) are likely false positives arising from knowledge graph topology artefacts; the two clinically actionable signals are diabetic retinopathy (rank 8, L1) and severe non-proliferative diabetic retinopathy (rank 6, L2), which are the focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neovascular Age-Related Macular Degeneration (nAMD) — not registered in Singapore; based on US/EU approval context |
| Predicted New Indication | Diabetic Retinopathy (TxGNN Rank 8; highest evidence among all 10 predictions) |
| TxGNN Prediction Score | 96.75% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Faricimab is the first bispecific antibody engineered for intraocular use. It simultaneously and independently binds two targets: **VEGF-A**, the primary driver of pathological retinal neovascularization and vascular hyperpermeability; and **Angiopoietin-2 (Ang-2)**, which destabilizes the Tie2 signaling axis on retinal vascular endothelium, promoting vessel leakage, inflammatory cell recruitment, and microaneurysm formation. In diabetic retinopathy, both pathways are chronically dysregulated by hyperglycemia-driven oxidative stress and microangiopathy. Single-target anti-VEGF agents (ranibizumab, bevacizumab, aflibercept) leave the Ang-2 axis unaddressed — a mechanistic gap that explains why a clinically meaningful subset of patients shows incomplete anatomical response or requires high-frequency injections.

The dual-blockade strategy is well-suited to the full disease spectrum of diabetic retinopathy. In early non-proliferative stages (NPDR), rising VEGF-A and Ang-2 precede clinical edema; blocking both simultaneously could modify disease progression before irreversible structural damage occurs. In established DME, dual inhibition accelerates retinal drying and extends the dosing interval. In proliferative DR (PDR), suppressing Ang-2-mediated vascular instability complements anti-VEGF control of neovascularization. This mechanistic breadth is directly reflected in the clinical evidence: the co-pivotal YOSEMITE and RHINE Phase 3 RCTs demonstrated Faricimab's non-inferiority to aflibercept in DME, with approximately 60% of T&E patients achieving every-12- or 16-week dosing at 2 years — the primary durability advantage of dual blockade.

The ongoing MAGIC Phase 2 trial (NCT05681884) represents the genuinely novel repurposing frontier: treating severe NPDR before it progresses to PDR, using Faricimab as a disease-modifying agent targeting retinal non-perfusion. This "prevention-first" strategy has no current approved drug and would constitute a meaningful extension of the existing approved indication if Phase 2 data supports advancement.

> ⚠️ **Note on TxGNN Prediction Quality**: Among the top 10 predictions in this Evidence Pack, seven are likely false positives. Platelet release disorders (rank 1), pseudo-von Willebrand disease (rank 2), Glanzmann thrombasthenia (rank 3), FNAIT (rank 10), and RSV infection (rank 9) have no intersection with VEGF-A/Ang-2 biology. Drug-induced osteoporosis (rank 4) has theoretical VEGF-bone biology but systemic exposure from intravitreal dosing is negligible (plasma Cmax < 0.1 µg/mL). Esotropia (rank 5) reflects an adverse event association, not a therapeutic signal. HER2+ breast carcinoma (rank 7) has theoretical angiogenesis rationale but would require completely different formulation, route, and toxicology profiling. These ranks likely arise from shared vascular-node clustering in the knowledge graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03622593](https://clinicaltrials.gov/study/NCT03622593) | Phase 3 | Completed | 951 | RHINE: Faricimab vs. aflibercept Q8W in DME; evaluated efficacy, safety, and PK with personalized treat-and-extend dosing — co-pivotal trial supporting FDA approval |
| [NCT03622580](https://clinicaltrials.gov/study/NCT03622580) | Phase 3 | Completed | 940 | YOSEMITE: Faricimab vs. aflibercept Q8W in DME; primary endpoint visual acuity gain at 1 year — co-pivotal trial supporting FDA approval |
| [NCT04597918](https://clinicaltrials.gov/study/NCT04597918) | Phase 2b | Completed | 99 | ALTIMETER: Aqueous humor biomarkers and multimodal imaging in treatment-naïve DME; evaluated associations between biomarker patterns and clinical outcomes under Faricimab treat-and-extend |
| [NCT05681884](https://clinicaltrials.gov/study/NCT05681884) | Phase 2 | Active (not recruiting) | 179 | MAGIC: Faricimab for retinal non-perfusion in non-proliferative diabetic retinopathy (NPDR); key disease-modification trial evaluating prevention of progression to PDR |
| [NCT05224102](https://clinicaltrials.gov/study/NCT05224102) | Phase 4 | Active (not recruiting) | 218 | Post-marketing study in underrepresented DME populations (Black/African American, Hispanic/Latino, Native American, Asian Indian); long-term safety and efficacy monitoring |
| [NCT05610319](https://clinicaltrials.gov/study/NCT05610319) | Phase 4 | Active (not recruiting) | 446 | Treat-and-extend versus fixed dosing with Faricimab for DME; pragmatic open-label RCT assessing real-world dosing regimens |
| [NCT06191094](https://clinicaltrials.gov/study/NCT06191094) | Phase 4 | Enrolling by invitation | 100 | Perioperative Faricimab vs. sham for non-clearing vitreous hemorrhage secondary to proliferative DR; evaluating surgical outcome improvement |
| [NCT06790784](https://clinicaltrials.gov/study/NCT06790784) | Phase 3 | Recruiting | 426 | Faricimab + panretinal photocoagulation (PRP) vs. vitrectomy + endolaser for PDR; 3-year visual acuity and complication follow-up |
| [NCT05476926](https://clinicaltrials.gov/study/NCT05476926) | N/A (observational) | Active (not recruiting) | 6,000 | VOYAGER: Multi-national prospective real-world data for Faricimab in approved retinal indications including DME; effectiveness, safety, treatment patterns |
| [NCT06439576](https://clinicaltrials.gov/study/NCT06439576) | N/A (observational) | Recruiting | 1,000 | Farseeing Study: China real-world evidence for Faricimab in DME, RVO, and nAMD; long-term effectiveness and safety in Asian patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35085503](https://pubmed.ncbi.nlm.nih.gov/35085503/) | 2022 | Phase 3 RCT | Lancet | YOSEMITE/RHINE 1-year primary results: Faricimab T&E up to Q16W non-inferior to aflibercept Q8W in DME visual acuity outcomes; durability advantage established |
| [38158159](https://pubmed.ncbi.nlm.nih.gov/38158159/) | 2024 | Phase 3 RCT (2-yr follow-up) | Ophthalmology | YOSEMITE/RHINE 2-year T&E results: ~60% of Faricimab patients achieved Q12W or Q16W intervals; vision gains sustained without loss of durability |
| [30905643](https://pubmed.ncbi.nlm.nih.gov/30905643/) | 2019 | Phase 2 RCT | Ophthalmology | BOULEVARD: Faricimab vs. ranibizumab in DME; first Phase 2 evidence that dual VEGF-A/Ang-2 blockade produces superior central subfield thickness reduction vs. anti-VEGF monotherapy |
| [37751021](https://pubmed.ncbi.nlm.nih.gov/37751021/) | 2023 | Systematic Review & NMA | Advances in Therapy | Network meta-analysis of DME treatments: Faricimab T&E up to Q16W demonstrates favorable drying and durability profile versus anti-VEGF agents in flexible dosing regimens |
| [39362194](https://pubmed.ncbi.nlm.nih.gov/39362194/) | 2024 | Meta-Analysis | Ophthalmologica | Meta-analysis of Faricimab across nAMD, DME, and RVO: consistent BCVA improvement and retinal thickness reduction; safety profile comparable to anti-VEGF monotherapy |
| [38847896](https://pubmed.ncbi.nlm.nih.gov/38847896/) | 2024 | Translational Review | Graefe's Archive | Preclinical-to-Phase 3 narrative: mechanistic rationale for dual Ang-2/VEGF-A blockade, clinical pharmacology, and Phase 3 outcomes in DME and nAMD |
| [38852921](https://pubmed.ncbi.nlm.nih.gov/38852921/) | 2024 | Subgroup Analysis (Phase 3) | Ophthalmology | YOSEMITE/RHINE subgroup with baseline BCVA 20/50 or worse: Faricimab maintains efficacy advantage in patients with severe vision loss at entry |
| [36012690](https://pubmed.ncbi.nlm.nih.gov/36012690/) | 2022 | Comparative Review | Int J Mol Sci | Mechanistic and clinical comparison of Faricimab vs. aflibercept in nAMD and DME; discusses rationale for Ang-2 co-inhibition in incomplete VEGF responders |
| [35474059](https://pubmed.ncbi.nlm.nih.gov/35474059/) | 2022 | Drug Approval Review | Drugs | First approval summary for Faricimab (Vabysmo™): pharmacology, mechanism of dual blockade, pivotal trial results, and regulatory history for nAMD and DME |
| [41587134](https://pubmed.ncbi.nlm.nih.gov/41587134/) | 2026 | Phase 2 RCT Design | Ophthalmologica | MAGIC trial design and rationale: Faricimab for retinal non-perfusion in NPDR; assesses change in non-perfusion area as primary endpoint in disease-modification paradigm |

---

## Singapore Market Information

Faricimab is not registered in Singapore. No HSA product authorizations are on record.

| Item | Status |
|------|--------|
| HSA Registration | Not registered |
| Number of Product Licenses | 0 |
| Reference Markets with Approval | United States (FDA, January 2022), European Union (EMA), Japan (PMDA) |
| Approved Indications (reference) | Neovascular AMD and Diabetic Macular Edema (US/EU); additional indications (RVO) in some markets |

Clinicians in Singapore requiring access before local registration may consider the HSA Special Access Route (SAR) — Therapeutic Products pathway, using evidence from FDA/EMA approvals as supporting documentation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed local warnings and contraindications are not available in this Evidence Pack. As a class reference for intravitreal biologic agents, known risks include: **endophthalmitis**, **intraocular pressure elevation**, **retinal detachment**, **vitreous floaters**, and rare systemic thromboembolic events. Refer to the Vabysmo® (faricimab-svoa) US Prescribing Information or EU Summary of Product Characteristics for full prescribing details. No drug–drug interactions were identified in the database query.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Faricimab has robust L1 evidence for diabetic retinopathy (specifically DME), with two completed Phase 3 RCTs (YOSEMITE/RHINE, combined n ≈ 1,891), FDA approval since January 2022, and a strong mechanistic rationale based on dual VEGF-A/Ang-2 inhibition that directly addresses the pathophysiology of diabetic microangiopathy. The TxGNN model correctly identifies this mechanistic connection, validating the prediction signal even though Singapore has not yet approved the drug.

**To proceed, the following is needed:**

- **HSA registration**: Submit local registration application referencing FDA/EMA approval dossiers; consider HSA Special Access Route for urgent cases pending approval
- **Local safety data**: Obtain Singapore-applicable prescribing information; confirm no population-specific pharmacovigilance signals from Asian patient data (Farseeing Study results anticipated 2027)
- **Specialist governance**: Engage vitreoretinal ophthalmologists for clinical oversight; establish intravitreal injection protocols compliant with local infection control standards
- **Novel NPDR indication (Rank 6)**: Await MAGIC Phase 2 trial primary results (completion expected April 2026) before initiating any investigator-initiated protocol for disease-modification in non-proliferative DR
- **Pharmacoeconomic assessment**: Conduct cost-effectiveness analysis for Singapore context; reference Japanese cost-effectiveness data (PMID: [40078048](https://pubmed.ncbi.nlm.nih.gov/40078048/)) as a regional proxy while local data matures
- **False-positive signal review**: Disregard TxGNN predictions for platelet disorders (ranks 1–3, 10), RSV (rank 9), and esotropia (rank 5) — no mechanistic basis; no further evidence gathering recommended for these indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

