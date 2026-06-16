---
layout: default
title: Dimethyl Fumarate
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
---

# Dimethyl Fumarate
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

# Dimethyl Fumarate: From Relapsing-Remitting Multiple Sclerosis to Progressive Multiple Sclerosis

## One-Sentence Summary

Dimethyl fumarate (DMF, marketed as Tecfidera®) is an oral immunomodulator globally approved for the treatment of relapsing-remitting multiple sclerosis (RRMS) in the US, EU, and Japan.
The TxGNN model predicts it may be effective for **Progressive Multiple Sclerosis**,
with **18 clinical trials** and **19 publications** currently supporting this direction, including a completed Phase 2 RCT that directly enrolled primary progressive MS patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsing-remitting multiple sclerosis (RRMS) |
| Predicted New Indication | Progressive Multiple Sclerosis |
| TxGNN Prediction Score | 90.67% |
| Evidence Level | L2 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

DMF's core mechanism operates through the Nrf2 (Nuclear factor erythroid 2-related factor 2) pathway: upon activation, Nrf2 induces antioxidant enzymes including HO-1 and NQO1, substantially reducing neuronal oxidative stress. Concurrently, DMF inhibits NF-κB signaling, suppresses pro-inflammatory cytokines (IL-6, TNF-α), and shifts the immune phenotype from Th1 toward Th2 while reducing circulating CD8+ T cell counts.

This mechanistic profile maps closely onto the pathological substrate of progressive MS. Unlike RRMS — which is dominated by episodic immune-mediated attacks on the myelin sheath — progressive MS (both primary and secondary forms) is characterized by sustained, smouldering oxidative neurodegeneration, mitochondrial dysfunction, and slowly expanding grey matter lesions in which acute inflammation plays a secondary role. DMF's Nrf2/antioxidant arm is theoretically well-positioned to address this pathway. However, since fewer acute inflammatory lesions are present in progressive disease, the immunomodulatory benefit expected in RRMS is anticipated to be attenuated.

A completed Phase 2 randomized placebo-controlled trial (NCT02959658, n=54) directly tested DMF in primary progressive MS. Although the trial did not meet its pre-specified primary endpoint (reduction in CSF neurofilament light chain concentration at 48 weeks), a subsequent open-label extension (PMID 36586351) and real-world observational cohort data (PMID 33996142) provide exploratory signals that DMF may still slow neurodegeneration in this population — supporting the biological plausibility of the TxGNN prediction and justifying further investigation with an adequately powered trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02959658](https://clinicaltrials.gov/study/NCT02959658) | Phase 2 | Completed | 54 | Randomized placebo-controlled trial directly in primary progressive MS (PPMS). Primary endpoint (CSF neurofilament light chain reduction) not met, but open-label extension (PMID 36586351) provides longer-term exploratory data. The only completed RCT of DMF specifically in PPMS. |
| [NCT03092544](https://clinicaltrials.gov/study/NCT03092544) | Phase 4 | Unknown | 57 | Investigates indirect neuroprotective mechanisms of Tecfidera® (DMF) in both RRMS and progressive MS patients, including gut microbiome interactions; directly supports the mechanistic rationale for progressive disease. |
| [NCT02430532](https://clinicaltrials.gov/study/NCT02430532) | Phase 3 | Terminated | 58 | BG00012 (DMF) vs placebo in secondary progressive MS (SPMS) to delay non-relapse-related disability progression. Terminated early due to slow enrollment; contextual importance remains high as the only Phase 3 attempt in SPMS. |
| [NCT02683863](https://clinicaltrials.gov/study/NCT02683863) | Phase 4 | Completed | 20 | Pharmacokinetic study examining whether DMF or its metabolite monomethyl fumarate (MMF) penetrates the CNS in SPMS patients via CSF sampling; addresses blood-brain barrier penetration relevant to neuroprotection claims. |
| [NCT07138833](https://clinicaltrials.gov/study/NCT07138833) | Phase 4 | Not Yet Recruiting | 50 | Prospective open-label evaluation of DMF enteric-coated capsules in relapsing MS including active secondary progressive MS (SPMS); trial start expected 2025. |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, Not Recruiting | 800 | DELIVER-MS: large comparative trial assessing whether early high-efficacy DMT (including DMF) improves long-term prognosis in RRMS; indirectly informs progressive MS prevention potential. |
| [NCT03193866](https://clinicaltrials.gov/study/NCT03193866) | N/A | Completed | 3526 | COMBAT-MS: population-based prospective cohort comparing DMF and other DMTs including rituximab over 5 years in RRMS; provides large-scale real-world effectiveness and safety benchmarks. |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Active, Not Recruiting | 900 | TREAT-MS: pragmatic trial comparing early aggressive therapy vs escalation approach for MS disability prevention; DMF serves as a reference comparator arm. |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | Enrolling by Invitation | 323 | STATURE: prospective multi-site study on treatment burden and adherence across six oral DMTs including DMF; informs real-world tolerability relevant to progressive MS populations. |
| [NCT02739542](https://clinicaltrials.gov/study/NCT02739542) | Phase 4 | Completed | 87 | ARISE: randomized double-blind trial of DMF in radiologically isolated syndrome (RIS) to delay conversion to clinical MS; provides data on DMF efficacy at the earliest identifiable disease stage. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34429340](https://pubmed.ncbi.nlm.nih.gov/34429340/) | 2021 | RCT (Phase 2) | Neurology® Neuroimmunology & Neuroinflammation | Primary publication of NCT02959658 RCT of DMF vs placebo in PPMS (n=54); primary endpoint (CSF NFL reduction) not met, but safety profile acceptable. The most directly relevant trial evidence for this repurposing. |
| [36586351](https://pubmed.ncbi.nlm.nih.gov/36586351/) | 2023 | Open-Label Extension | Multiple Sclerosis and Related Disorders | Open-label extension of the PPMS Phase 2 RCT; provides longer-term exploratory efficacy and safety data on DMF in primary progressive MS beyond the initial 48-week placebo-controlled phase. |
| [33996142](https://pubmed.ncbi.nlm.nih.gov/33996142/) | 2021 | Real-World Cohort | Multiple Sclerosis Journal – Experimental, Translational and Clinical | Retrospective cohort analysis of DMF effectiveness and safety specifically in the progressive MS population; limited sample size but directly addresses the repurposing question with real-world data. |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network Meta-Analysis | Cochrane Database of Systematic Reviews | Updated Cochrane NMA comparing all immunomodulators and immunosuppressants for RRMS; most comprehensive comparative efficacy reference for DMF positioning in the MS treatment landscape. |
| [38321317](https://pubmed.ncbi.nlm.nih.gov/38321317/) | 2024 | Systematic Review + Meta-Analysis | Drug Safety | Systematic review and meta-analysis of drug-induced PML including DMF; quantifies absolute risk and identifies key risk factors (lymphopenia, JC virus antibody status). Critical safety reference. |
| [29686116](https://pubmed.ncbi.nlm.nih.gov/29686116/) | 2018 | Clinical Practice Guideline | Neurology | AAN practice guideline on DMTs for adult MS; formally endorses DMF as first-line therapy for RRMS; provides regulatory and clinical context for expanding to progressive indications. |
| [25900414](https://pubmed.ncbi.nlm.nih.gov/25900414/) | 2015 | Cochrane Review | Cochrane Database of Systematic Reviews | Original Cochrane systematic review confirming DMF efficacy in RRMS (approved by FDA and EMA); establishes the evidence base from which progressive MS extrapolation is being attempted. |
| [33091427](https://pubmed.ncbi.nlm.nih.gov/33091427/) | 2021 | Literature Review | Pharmacology & Therapeutics | In-depth mechanistic review of DMF-induced lymphopenia and its molecular basis; explains why persistent grade ≥3 lymphopenia elevates PML risk. Essential for safety monitoring protocol design. |
| [32808554](https://pubmed.ncbi.nlm.nih.gov/32808554/) | 2022 | Case Series / Safety Study | Multiple Sclerosis (Houndmills) | Clinical characterization of 9 PML cases in DMF-treated MS patients; PML incidence estimated at 0.02 per 1,000 patients; sustained lymphopenia identified as the dominant risk factor. |
| [27433310](https://pubmed.ncbi.nlm.nih.gov/27433310/) | 2016 | Review | Therapeutic Advances in Chronic Disease | Comprehensive review of DMF after 2+ years of real-world use across >190,000 patients; covers post-marketing safety signals, subgroup efficacy analyses, and patient selection guidance. |

---

## Singapore Market Information

Dimethyl fumarate (DB08908) is currently **not registered** in Singapore. There are no product authorizations on record with HSA.

> For reference: DMF is approved internationally as **Tecfidera®** (Biogen) for RRMS in the US (FDA, March 2013), EU (EMA, January 2014), and Japan (PMDA, December 2016). Any Singapore deployment would require a new HSA New Drug Application submission.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Key risk identified from the evidence literature (independent of package insert data):**

- **Lymphopenia and PML risk**: DMF causes progressive, dose-dependent lymphopenia. Persistent grade ≥3 lymphopenia (absolute lymphocyte count <0.5 × 10⁹/L sustained for >6 months) substantially increases the risk of progressive multifocal leukoencephalopathy (PML) — a potentially fatal opportunistic CNS infection caused by JC virus reactivation. PML incidence in DMF-treated patients is estimated at 0.02 per 1,000 patients (PMID 32808554). Routine lymphocyte count monitoring is mandatory; treatment discontinuation should be considered at defined thresholds.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT and real-world cohort data directly addressing progressive MS provide L2-level evidence, and the Nrf2/antioxidant neuroprotective mechanism offers a scientifically plausible rationale for targeting the oxidative neurodegeneration central to progressive MS — even though the Phase 2 primary endpoint was not met. DMF's established safety profile in >560,000 RRMS patients globally is a meaningful asset for any progressive indication development.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate HSA Singapore new drug application process; DMF currently has no local market authorization
- **MOA documentation**: Resolve data gap by querying the DrugBank API for complete mechanism of action details (DB08908)
- **Safety monitoring protocol**: Establish mandatory lymphocyte count monitoring schedule (baseline → monthly for first 6 months → every 3 months thereafter) with pre-defined discontinuation thresholds; include JC virus antibody screening prior to initiation
- **Package insert review**: Obtain and parse the Tecfidera® US/EU SmPC or PMDA package insert for complete warnings and contraindications, to fill the current blocking data gap (DG001)
- **Trial design consideration**: The existing Phase 2 (n=54) was underpowered; a Phase 2b/3 trial in secondary progressive MS (SPMS) with disability progression as the primary endpoint and NfL as a validated surrogate is needed before regulatory filing for a progressive indication
- **Biomarker strategy**: Incorporate serum NfL monitoring (per PMID 35182510 methodology) as an early futility/efficacy signal in any prospective investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

