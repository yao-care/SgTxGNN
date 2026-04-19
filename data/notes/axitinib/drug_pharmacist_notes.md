# Axitinib: From Advanced Renal Cell Carcinoma to Renal Carcinoma

## One-Sentence Summary

Axitinib (Inlyta®, DB06626) is a second-generation selective VEGFR inhibitor approved in the United States, EU, and Japan for second-line advanced renal cell carcinoma (RCC), but currently holding no registration with Singapore's Health Sciences Authority (HSA).
The TxGNN model predicted 10 new indications; the highest-evidence finding is **Renal Carcinoma** (TxGNN score 99.85%, ranked #6 overall), supported by **≥50 registered clinical trials** and **20 publications** — including at least four completed Phase 3 RCTs that now define the global standard of care for advanced RCC.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced renal cell carcinoma — second-line after failure of one prior systemic therapy (FDA-approved January 2012; not registered in Singapore) |
| Predicted New Indication | Renal Carcinoma (highest-evidence among 10 TxGNN-predicted indications) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not retrieved from the DrugBank API in this assessment cycle. Based on published literature, axitinib is a potent and selective inhibitor of all three VEGF receptor isoforms (VEGFR1/2/3) with an IC₅₀ approximately 10-fold lower than first-generation TKIs such as sorafenib. It also inhibits PDGFR-β and c-KIT, contributing to dual anti-angiogenic and anti-tumour stromal effects. Its high selectivity for VEGFR distinguishes it from earlier multi-kinase agents and underpins its more predictable toxicity profile.

The mechanistic rationale for RCC is exceptionally well established. In clear-cell RCC — the most common histological subtype — biallelic inactivation of the *VHL* tumour suppressor gene causes constitutive stabilisation of HIF-1α, leading to overproduction of VEGF and PDGF. These factors drive pathological neovascularisation through VEGFR signalling, sustaining tumour growth and metastatic spread. Axitinib directly blocks this cascade at all three VEGFR isoforms, providing highly targeted anti-angiogenic activity. This mechanism was formally validated in the AXIS Phase 3 trial (NCT00678392; n = 723), which demonstrated superior progression-free survival versus sorafenib in the second-line setting and served as the basis for FDA approval.

The TxGNN prediction score of 99.85% for renal carcinoma reflects the deep biological alignment between axitinib's mechanism and RCC's core oncogenic driver. Since the AXIS trial, axitinib has been repositioned as the VEGFR-targeting backbone in multiple IO+TKI combination regimens. KEYNOTE-426 (pembrolizumab + axitinib) and JAVELIN Renal 101 (avelumab + axitinib) both established superiority over sunitinib as first-line therapy, with 5-year follow-up data published in *Nature Medicine* in 2025 confirming durable survival benefit — cementing axitinib's role across the full disease continuum of advanced RCC.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678392](https://clinicaltrials.gov/study/NCT00678392) | Phase 3 | Completed | 723 | AXIS trial: axitinib superior to sorafenib in median PFS (6.7 vs. 4.7 months) for second-line mRCC; pivotal basis for FDA 2012 approval |
| [NCT00835978](https://clinicaltrials.gov/study/NCT00835978) | Phase 2 | Completed | 213 | Dose-titration study: personalised escalation above standard 5 mg BID associated with improved ORR and acceptable tolerability in mRCC |
| [NCT02133742](https://clinicaltrials.gov/study/NCT02133742) | Phase 1 | Completed | 52 | Phase 1b pembrolizumab + axitinib combination; established PK compatibility and early efficacy signal; foundational study for KEYNOTE-426 |
| [NCT02493751](https://clinicaltrials.gov/study/NCT02493751) | Phase 1 | Completed | 55 | Phase 1b avelumab + axitinib; defined recommended Phase 2 dose and confirmed tolerability; led directly to JAVELIN Renal 101 Phase 3 trial |
| [NCT01599754](https://clinicaltrials.gov/study/NCT01599754) | Phase 3 | Terminated | 724 | Adjuvant axitinib after nephrectomy in high-risk RCC; terminated at interim analysis — no disease-free survival benefit observed, negative result |
| [NCT03494816](https://clinicaltrials.gov/study/NCT03494816) | Phase 2 | Completed | 24 | NAXIVA: neoadjuvant axitinib for clear-cell RCC with venous tumour thrombus; 35% VTT down-staging rate achieved; biomarker sub-analysis published in *Nature Communications* 2025 |
| [NCT05738694](https://clinicaltrials.gov/study/NCT05738694) | Phase 2 | Recruiting | 298 | Neoadjuvant axitinib + PD-1 antibody vs. surgery alone in high-risk RCC (T2G3-4/T3-4/N1); primary endpoint: disease-free survival |
| [NCT05817903](https://clinicaltrials.gov/study/NCT05817903) | Phase 2 | Recruiting | 118 | AxIn Study: axitinib intensification added to nivolumab after nivolumab + ipilimumab induction without complete response in mRCC |
| [NCT04033991](https://clinicaltrials.gov/study/NCT04033991) | N/A (Observational) | Completed | 684 | Large-scale UK real-world retrospective of sunitinib (first-line) → axitinib (second-line) sequence; population-level PFS and safety data |
| [NCT05808608](https://clinicaltrials.gov/study/NCT05808608) | Phase 1/2 | Recruiting | 33 | AK104 (PD-1/CTLA-4 bispecific antibody) + axitinib as first-line therapy for special pathological subtypes of advanced/metastatic RCC |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | Phase 3 RCT | N Engl J Med | KEYNOTE-426: pembrolizumab + axitinib superior to sunitinib in OS, PFS, and ORR across all IMDC risk groups as first-line therapy for advanced RCC |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | Phase 3 RCT | N Engl J Med | JAVELIN Renal 101: avelumab + axitinib demonstrated significantly longer PFS versus sunitinib in previously untreated advanced RCC |
| [37872020](https://pubmed.ncbi.nlm.nih.gov/37872020/) | 2024 | Phase 3 RCT | Ann Oncol | RENOTORCH: toripalimab + axitinib superior to sunitinib for intermediate-/poor-risk first-line advanced clear-cell RCC (China Phase 3 data) |
| [37500340](https://pubmed.ncbi.nlm.nih.gov/37500340/) | 2023 | Phase 3 Follow-up | Eur Urol | KEYNOTE-426 43-month final protocol-specified analysis: sustained OS and PFS benefit confirmed; pembrolizumab + axitinib remains standard of care |
| [40750932](https://pubmed.ncbi.nlm.nih.gov/40750932/) | 2025 | Phase 3 Long-term | Nature Medicine | KEYNOTE-426 5-year survival analysis: durable OS benefit maintained with ≥5 years follow-up; key predictive biomarkers identified |
| [39706335](https://pubmed.ncbi.nlm.nih.gov/39706335/) | 2025 | Phase 3 RCT | Ann Oncol | JAVELIN Renal 101 final analysis: avelumab + axitinib demonstrated sustained long-term OS benefit over sunitinib at definitive readout |
| [28276433](https://pubmed.ncbi.nlm.nih.gov/28276433/) | 2017 | Review | Nat Rev Dis Primers | Comprehensive RCC disease primer: VHL pathway biology, molecular subtypes (including clear-cell, papillary, chromophobe), and treatment landscape evolution |
| [29033542](https://pubmed.ncbi.nlm.nih.gov/29033542/) | 2017 | Review | Drug Des Dev Ther | Axitinib clinical development in RCC: pharmacology, dose optimisation strategy, and evidence base positioning across lines of therapy |
| [32293937](https://pubmed.ncbi.nlm.nih.gov/32293937/) | 2020 | Review | Expert Rev Anticancer Ther | Avelumab + axitinib safety and efficacy review; practical guidance on adverse event management and patient selection |
| [39326645](https://pubmed.ncbi.nlm.nih.gov/39326645/) | 2024 | Review | Crit Rev Oncol Hematol | Narrative review of axitinib outcomes across children, young adults, and adults with RCC; highlights pharmacokinetic differences and evidence gaps in paediatric populations |

---

## Singapore Market Information

Axitinib currently holds **no product registrations** with the Health Sciences Authority (HSA) of Singapore. There are no licensed products, approved indications, or registered dosage forms on record.

An initial product registration application would be required under HSA's New Drug Application (NDA) or abridged NDA pathway before axitinib can be marketed, distributed, or prescribed in Singapore. This represents the primary regulatory gap for patient access.

---

## Cytotoxicity

Axitinib is an antineoplastic agent targeting renal cell carcinoma and meets criteria for inclusion in this section (anticancer indication; tyrosine kinase inhibitor drug class).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective oral VEGFR 1/2/3 tyrosine kinase inhibitor (second-generation TKI; non-conventional, non-myeloablative cytotoxic) |
| Myelosuppression Risk | Low to moderate (substantially less myelosuppressive than conventional cytotoxics; anaemia, neutropenia, and thrombocytopenia have been reported, but severe haematological toxicity is uncommon) |
| Emetogenicity Classification | Low (oral TKI; nausea and vomiting possible but high-grade emesis is uncommon; minimal prophylactic antiemetic requirement per MASCC/ASCO oral chemotherapy guidelines) |
| Monitoring Items | Blood pressure weekly during the first month then periodically (hypertension is the primary class effect), CBC with differential, liver function tests (ALT/AST/bilirubin), serum creatinine, urine protein (dipstick, with 24-hour urine protein if 2+ or greater), thyroid-stimulating hormone (TSH), serum electrolytes |
| Handling Protection | Must follow institutional cytotoxic drug handling regulations for oral antineoplastic agents; tablets should not be crushed or split; wear appropriate PPE (gloves, eye protection) during dispensing and preparation; dispose as cytotoxic pharmaceutical waste per local regulations |

---

## Safety Considerations

Please refer to the package insert for complete safety information.

Automated queries for Singapore/Taiwan product insert warnings, contraindications, and drug–drug interaction data returned no results for this assessment. For clinical decision-making, consult the **Inlyta® US Prescribing Information (USPI)** or the **EMA Summary of Product Characteristics** for complete guidance on: arterial and venous thromboembolic events, haemorrhage, cardiac failure, hypertensive crisis, thyroid dysfunction, hepatotoxicity, wound healing complications, posterior reversible encephalopathy syndrome (PRES), and CYP3A4/CYP1A2-based drug interactions (notably, strong CYP3A4 inhibitors such as ketoconazole may significantly increase axitinib plasma levels).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Axitinib holds one of the most robust evidence bases among targeted oncology agents, with at least four completed Phase 3 RCTs — AXIS (second-line monotherapy), KEYNOTE-426 and JAVELIN Renal 101 (first-line combinations), and RENOTORCH (first-line in Asian populations) — establishing its efficacy and safety across the full advanced RCC treatment spectrum. Despite this global evidence, axitinib has no Singapore HSA registration, creating a tangible patient access gap in a disease area with measurable incidence in the Asia-Pacific region.

**To proceed, the following is needed:**

- **HSA registration pathway**: Initiate NDA or abridged NDA submission with pivotal trial data (AXIS + KEYNOTE-426 as minimum core dossier); evaluate eligibility for HSA's expedited review (Innovative Medicines pathway) given breakthrough designation history
- **Full safety dossier**: Retrieve complete prescribing information (SmPC / USPI) to characterise black-box warnings, contraindications (hepatic impairment, uncontrolled hypertension, recent arterial thromboembolic events), and CYP3A4 drug interaction profile
- **Asian population pharmacokinetic data**: Available from KEYNOTE-426 Asian sub-analyses, RENOTORCH (China), and Japanese JAVELIN Renal 101 real-world observational studies — essential for HSA submission
- **Risk management plan**: Develop a Singapore-specific risk minimisation programme addressing hypertension management, hand-foot syndrome, hepatotoxicity monitoring, and thyroid function surveillance
- **Formulary positioning strategy**: Define whether Singapore registration targets second-line axitinib monotherapy, first-line pembrolizumab + axitinib, first-line avelumab + axitinib, or all indications; align with existing National Cancer Centre Singapore or MOH treatment protocols
- **Paediatric use protocol**: NCT02164838 provides Phase 1 paediatric maximum tolerated dose (MTD) data; supplementary paediatric assessment required under HSA's guidelines for medicines in paediatric populations