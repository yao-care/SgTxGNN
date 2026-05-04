---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: From Plaque Psoriasis to Ulcerative Colitis

## One-Sentence Summary

Guselkumab (Tremfya) is a selective anti–IL-23p19 monoclonal antibody, globally established for moderate-to-severe plaque psoriasis and psoriatic arthritis, but currently not registered in Singapore for any indication.
The TxGNN model predicts it may be effective for **Ulcerative Colitis** — a signal strongly supported by **17 clinical trials** and **20 publications**, including a landmark Phase 3 RCT (QUASAR) published in *The Lancet* in 2025 and an FDA approval in 2024, representing the most compelling repurposing opportunity in this evidence pack.
The model also generates 8 additional predictions (all L5, Hold) and validates its own accuracy by ranking **Psoriasis (rank #3, L1)** — guselkumab's globally established primary indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Moderate-to-severe plaque psoriasis (globally approved since 2017; **not registered in Singapore**) |
| Primary Repurposing Target | Ulcerative Colitis (TxGNN rank #6) |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not available from the Singapore regulatory record (no Singapore registration exists). Based on published clinical literature, guselkumab is a fully human IgG1λ monoclonal antibody that selectively binds the **p19 subunit of interleukin-23 (IL-23)**, blocking its binding to the IL-23 receptor. This selectivity is clinically important: because IL-23 and IL-12 share a common p40 subunit, guselkumab's p19-specific approach preserves IL-12–mediated immune surveillance — unlike the earlier IL-12/IL-23 inhibitor ustekinumab. A unique additional feature is guselkumab's ability to bind **CD64 (FcγRI)** expressed on macrophages and monocytes, enabling cell-surface neutralisation of membrane-bound IL-23 and potentially enhancing local tissue effects.

The mechanistic link to ulcerative colitis is well-grounded. In UC, mucosal overproduction of IL-23 drives pathological Th17/Th1 cell differentiation, releasing TNF-α, IL-17, and IL-22, which break down the intestinal epithelial barrier and sustain chronic inflammation. Genome-wide association studies have identified polymorphisms in the IL-23 receptor (*IL23R*) gene as UC susceptibility loci, directly implicating this pathway in disease pathogenesis. Selective IL-23p19 blockade addresses this root driver while sparing the systemic immunity conferred by IL-12 — an important safety advantage.

This mechanistic rationale has been confirmed in clinical reality. The QUASAR Phase 2b study (2023, *Gastroenterology*) and the QUASAR Phase 3 study (2025, *The Lancet*) demonstrated that guselkumab significantly outperformed placebo for both induction and maintenance of remission in patients with moderate-to-severe UC. The 2024 AGA Living Clinical Practice Guideline now lists guselkumab as a recommended therapeutic option for moderate-to-severe UC, and the FDA approved the UC indication in 2024. The TxGNN prediction thus accurately identifies a disease for which guselkumab has since achieved the highest level of regulatory validation.

---

## Clinical Trial Evidence (Ulcerative Colitis)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04033445](https://clinicaltrials.gov/study/NCT04033445) | Phase 2b/3 | Active, Not Recruiting | 1,064 | Core QUASAR platform study evaluating guselkumab vs. placebo in moderate-to-severe UC; Phase 3 arm results published in *The Lancet* 2025 — primary endpoints met for clinical remission and endoscopic response |
| [NCT05528510](https://clinicaltrials.gov/study/NCT05528510) | Phase 3 | Active, Not Recruiting | 418 | Evaluates subcutaneous guselkumab induction therapy vs. placebo in moderate-to-severe UC; primary endpoint is clinical remission at Week 12 |
| [NCT05242484](https://clinicaltrials.gov/study/NCT05242484) | Phase 2b | Active, Not Recruiting | 577 | Combination therapy platform: guselkumab + golimumab (dual biologic) vs. monotherapy in UC with inadequate prior response to advanced therapy |
| [NCT03662542](https://clinicaltrials.gov/study/NCT03662542) | Phase 2 | Completed | 214 | Proof-of-concept study for guselkumab + golimumab combination in UC; Phase 2a results informed the design of Phase 2b/3 combination studies |
| [NCT06663332](https://clinicaltrials.gov/study/NCT06663332) | Phase 3 | Recruiting | 196 | Pediatric long-term safety extension study covering UC, Crohn's disease, and juvenile psoriatic arthritis; through 2031 |
| [NCT06260163](https://clinicaltrials.gov/study/NCT06260163) | Phase 3 | Active, Not Recruiting | 112 | Pediatric Phase 3: efficacy, pharmacokinetics, and safety of guselkumab in pediatric patients with moderate-to-severe UC |
| [NCT06408935](https://clinicaltrials.gov/study/NCT06408935) | Phase 3b | Recruiting | 112 | Transmural healing endpoint study in Crohn's disease using MRI-based scoring (MaRIA); broadens IBD evidence base for guselkumab |
| [NCT07302360](https://clinicaltrials.gov/study/NCT07302360) | Real-world | Recruiting | 200 | Multicenter prospective real-world effectiveness study in bio-naive UC patients in China; addresses effectiveness outside trial populations |
| [NCT07242248](https://clinicaltrials.gov/study/NCT07242248) | Real-world | Recruiting | 220 | UK-based real-world clinical outcomes study in UC and Crohn's disease patients treated with guselkumab across lines of therapy |
| [NCT07102368](https://clinicaltrials.gov/study/NCT07102368) | Real-world | Recruiting | 400 | Real-world evidence generation in IBD; captures patient-reported outcomes including fatigue, quality of life, and work productivity |

---

## Literature Evidence (Ulcerative Colitis)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39706209](https://pubmed.ncbi.nlm.nih.gov/39706209/) | 2025 | Phase 3 RCT | *The Lancet* | QUASAR Phase 3: guselkumab significantly superior to placebo for induction and maintenance in moderate-to-severe UC; primary endpoints met across both study periods |
| [37659673](https://pubmed.ncbi.nlm.nih.gov/37659673/) | 2023 | Phase 2b RCT | *Gastroenterology* | QUASAR Phase 2b induction: dose-response established; guselkumab met clinical remission and endoscopic endpoints in UC patients with inadequate response to prior advanced therapy |
| [39572132](https://pubmed.ncbi.nlm.nih.gov/39572132/) | 2024 | Clinical Practice Guideline | *Gastroenterology* | AGA 2024 Living Clinical Practice Guideline for moderate-to-severe UC; guselkumab incorporated as a recommended pharmacological option |
| [39425738](https://pubmed.ncbi.nlm.nih.gov/39425738/) | 2024 | Network Meta-analysis | *Gastroenterology* | AGA 2024 comparative efficacy evidence synthesis of advanced therapies for UC; systematic review and network meta-analysis underpinning the AGA guideline |
| [40407729](https://pubmed.ncbi.nlm.nih.gov/40407729/) | 2025 | Network Meta-analysis | *Alimentary Pharmacology & Therapeutics* | Network meta-analysis of all approved biologics and small molecules as UC maintenance therapy; guselkumab ranks among the most effective agents |
| [40113101](https://pubmed.ncbi.nlm.nih.gov/40113101/) | 2025 | Phase 3 RCT | *Gastroenterology* | GRAVITI study: guselkumab subcutaneous induction and maintenance in moderate-to-severe Crohn's disease; demonstrates breadth of IL-23 inhibition across IBD spectrum |
| [39367678](https://pubmed.ncbi.nlm.nih.gov/39367678/) | 2024 | Network Meta-analysis | *Alimentary Pharmacology & Therapeutics* | Network meta-analysis evaluating histologic and histo-endoscopic remission endpoints in UC; guselkumab demonstrates favorable deep remission rates |
| [37069321](https://pubmed.ncbi.nlm.nih.gov/37069321/) | 2023 | Review | *Nature Reviews Gastroenterology & Hepatology* | Comprehensive review of IL-12/IL-23 inhibition in IBD; mechanistic rationale for selective IL-23p19 blockade in UC and Crohn's disease |
| [41324615](https://pubmed.ncbi.nlm.nih.gov/41324615/) | 2025 | Expert Review | *Expert Opinion on Biological Therapy* | Post-approval evaluation of guselkumab for UC; summarises clinical evidence and pharmacologic profile following FDA approval |
| [35553666](https://pubmed.ncbi.nlm.nih.gov/35553666/) | 2022 | Review | *Journal of Crohn's & Colitis* | Pipeline review of IL-23 blockade in IBD; covers guselkumab's Phase 2 evidence and positions it among selective IL-23p19 inhibitors entering IBD development |

---

## Singapore Market Information

Guselkumab is **not registered with the Singapore Health Sciences Authority (HSA)**. No marketing authorisations or approved indications exist in Singapore as of April 2026.

For reference, the drug has received regulatory approvals in the following jurisdictions:

| Jurisdiction | Approved Indications | Year |
|---|---|---|
| FDA (USA) | Moderate-to-severe plaque psoriasis; Psoriatic arthritis; Ulcerative colitis | 2017 / 2020 / 2024 |
| EMA (Europe) | Moderate-to-severe plaque psoriasis; Psoriatic arthritis | 2017 / 2021 |
| Japan (PMDA) | Plaque psoriasis | 2018 |

**Formulation**: Tremfya, 100 mg/mL subcutaneous injection (prefilled syringe or autoinjector). IV formulation also used for UC induction per QUASAR protocol.

---

## Safety Considerations

No Singapore package insert is available. Based on an integrated analysis of 11 Phase 2/3 clinical studies in psoriasis and psoriatic arthritis (PMID: 37906417, >14,000 patient-years exposure), the following safety profile has been characterised:

- **Infections**: Upper respiratory tract infections are the most common adverse event (~20%); serious infection rates are low and comparable to placebo (~2–3%). No increased risk of tuberculosis or opportunistic infections relative to comparators was observed.
- **Injection site reactions**: Generally mild and transient; reported in approximately 5% of patients.
- **Malignancy**: No increase in overall malignancy or specific cancer types was detected in controlled or long-term follow-up studies.
- **Immunogenicity**: Rates of anti-drug antibody formation are very low and have not been associated with clinically meaningful reductions in efficacy.
- **Drug interactions**: A completed Phase 1 CYP probe substrate study (NCT02397382, n=16) demonstrated that guselkumab at 200 mg SC does not meaningfully alter the activity of CYP3A4, CYP2C9, CYP2C19, CYP2D6, or CYP1A2, indicating a low pharmacokinetic drug-drug interaction risk.

Full contraindications and warnings (including active tuberculosis screening and live vaccine guidance) are detailed in the FDA- and EMA-approved product monographs and must be reviewed prior to clinical use.

---

## All TxGNN Predicted Indications — Ranked Summary

The evidence pack generated 10 ranked predictions. Predictions at ranks 1, 2, 4, 5, 7–10 are all L5 (model prediction only, no supporting clinical data) and are recommended to **Hold**. The two predictions with actionable L1 evidence are psoriasis (existing global approval) and ulcerative colitis (recently approved new indication).

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Comment |
|------|-----------|-------------|----------------|---------|---------|
| 1 | Drug-induced osteoporosis | 99.84% | L5 | **Hold** | IL-23→RANKL hypothesis is plausible but entirely unvalidated; no trials or literature |
| 2 | Severe nonproliferative diabetic retinopathy | 99.80% | L5 | **Hold** | Primary drivers are chronic hyperglycaemia and VEGF, not IL-23; likely topological noise in KG |
| **3** | **Psoriasis** | **99.75%** | **L1** | **Proceed with Guardrails** | **Globally approved indication — validates model accuracy; primary indication for Singapore introduction** |
| 4 | Diabetic retinopathy | 99.74% | L5 | **Hold** | Same mechanistic concern as rank 2; no clinical data |
| 5 | Renal osteodystrophy | 99.73% | L5 | **Hold** | Root pathology is PTH/FGF-23/VitD dysregulation; IL-23 blockade cannot address this |
| **6** | **Ulcerative colitis** | **99.70%** | **L1** | **Proceed with Guardrails** | **FDA-approved 2024; Phase 3 RCT in Lancet 2025; primary repurposing target for Singapore** |
| 7 | Congenital hypotrichosis with juvenile macular dystrophy | 99.67% | L5 | **Hold** | CDH3 mutation-driven developmental disorder; no immunological mechanistic link |
| 8 | Primary release disorder of platelets | 99.61% | L5 | **Hold** | Platelet δ/α granule secretion defect; IL-23 biology is irrelevant to this pathology |
| 9 | Glanzmann thrombasthenia | 99.60% | L5 | **Hold** | Integrin αIIbβ3 loss-of-function; genetic disorder with no IL-23 connection; likely network artefact |
| 10 | Non-renal secondary hyperparathyroidism | 99.55% | L5 | **Hold** | Calcium/phosphate metabolic disorder; IL-23 contribution is indirect and clinically insufficient |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Guselkumab has achieved the highest level of clinical evidence (L1) for two indications: plaque psoriasis (globally approved since 2017, with over 30 Phase 2–4 studies completed) and ulcerative colitis (FDA approved in 2024, Phase 3 RCT published in *The Lancet* 2025). Neither indication has Singapore registration, representing a meaningful gap in access to a well-characterised biologic therapy. The remaining 8 TxGNN predictions are speculative L5 signals with no supporting evidence and should not be pursued without preclinical data.

**To proceed, the following is needed:**

- **HSA Registration**: Prepare a regulatory submission package leveraging existing FDA and EMA approval dossiers; explore HSA's Expedited Pathway for drugs with established approval in major reference countries
- **Obtain Full Package Insert**: The FDA- and EMA-approved prescribing information must be reviewed for complete contraindications, boxed warnings, and special population guidance (pregnancy, renal/hepatic impairment, elderly)
- **Indication Sequencing**: File for plaque psoriasis as the initial indication (longer post-marketing safety record, broader physician familiarity), followed by UC and psoriatic arthritis
- **UC Dosing Protocol**: Confirm local infrastructure for IV induction (200 mg IV at Weeks 0, 4, 8 per QUASAR) before transitioning to SC maintenance (100 mg SC every 8 weeks); assess day-infusion capacity at relevant institutions
- **Tropical Infectious Disease Screening**: Develop Singapore-specific tuberculosis and endemic fungal infection screening protocols, given the regional epidemiology
- **Health Technology Assessment**: Commission a cost-effectiveness analysis for psoriasis and UC indications to support Singapore formulary and subsidy decisions
- **Pharmacovigilance Plan**: Establish a local post-marketing surveillance plan aligned with HSA requirements, particularly for infection monitoring in a high-humidity, high-exposure tropical environment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

