---
layout: default
title: Ledipasvir
parent: 僅模型預測 (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
---

# Ledipasvir
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

# Ledipasvir: From Chronic Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

> Ledipasvir is an NS5A inhibitor developed as part of the Ledipasvir/Sofosbuvir fixed-dose combination (Harvoni®) for chronic Hepatitis C virus (HCV) infection.
> The TxGNN model predicts it may also be effective for **Hepatitis B Virus (HBV) Infection**,
> with **21 clinical trials** and **20 publications** currently associated with this direction — though most of this evidence monitors HBV reactivation safety during HCV treatment rather than confirming direct anti-HBV efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (product not marketed); per global approval history and the clinical trial evidence in this pack, Ledipasvir is used in combination with Sofosbuvir for chronic genotype 1 Hepatitis C virus (HCV) infection |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.91% (rank 1899) |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Ledipasvir is not available in this evidence pack (flagged as data gap DG002, High severity). Based on known information, Ledipasvir is the NS5A-inhibitor component of the Ledipasvir/Sofosbuvir combination, whose efficacy against chronic HCV genotype 1 infection is well established. There is no known or reported direct inhibitory activity of Ledipasvir against the HBV polymerase (reverse transcriptase), so a specific anti-HBV mechanism cannot be confirmed from the data provided.

The bulk of the clinical trial and literature evidence gathered for this indication comes from patients coinfected with HCV and HBV who received Ledipasvir/Sofosbuvir to treat their HCV — with HBV DNA and HBsAg monitored as a **safety** endpoint (reactivation risk) rather than as a primary efficacy endpoint. This is an important distinction: most of the 21 trials and 20 publications are not testing Ledipasvir as an HBV therapy.

The one notable exception is a Phase 2, open-label pilot study (NCT03312023, reported in PMID 36045503) that directly enrolled HBV mono-infected (not HCV-coinfected) subjects and observed a modest decline in HBsAg and HBV DNA after 12 weeks of Ledipasvir/Sofosbuvir. This is a genuine, if preliminary, signal — but its underlying mechanism is unclear. It may reflect a non-specific antiviral or host immune-reconstitution effect following suppression of a co-circulating virus, rather than a direct pharmacological action on HBV. Given the small sample size (n=21), absence of a confirmed mechanism, and the fact that HBV reactivation (rather than suppression) has also been reported in some coinfected patients on this regimen, this should be treated as a research hypothesis rather than an established repurposing rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label pilot study of Ledipasvir/Sofosbuvir for 12 weeks in HBV mono-infected (non-HCV) subjects — the only trial testing this predicted indication directly, aiming for HBsAg/HBV DNA decline |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3b | Completed | 111 | Taiwan-based open-label study of LDV/SOF efficacy, safety, and tolerability in adults with chronic genotype 1/2 HCV and HBV coinfection; primary endpoint is HCV clearance, with HBV status monitored as a safety concern |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study on incidence, morbidity, mortality and risk factors for HBV reactivation during direct-acting antiviral treatment of HCV/HBV coinfection |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Phase 2 | Completed | 40 | Multicenter single-arm study of interferon-free LDV/SOF (genotype 1/4) in HCV-associated indolent B-cell lymphomas; enrollment criteria linked to HBV coinfection status |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | RCT (Phase 2, open-label) | Journal of Medical Virology | Only prospective study testing LDV/SOF directly in HBV mono-infected subjects; reports modest HBsAg/HBV DNA decline at Week 12 — the primary efficacy signal behind this prediction |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort (follow-up) | Clinical Infectious Diseases | 108-week follow-up of Taiwanese HCV/HBV coinfected patients after LDV/SOF treatment for HCV; evaluates HBV reactivation risk, not HBV treatment efficacy |
| [29174546](https://pubmed.ncbi.nlm.nih.gov/29174546/) | 2018 | Cohort | Gastroenterology | Prospective study of risks and outcomes of HBV reactivation in coinfected patients undergoing LDV/SOF treatment for HCV |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort (retrospective) | Journal of Clinical Gastroenterology | Examined incidence of HBV reactivation among actively infected or previously exposed patients during/after LDV/SOF treatment for HCV |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Cohort (safety signal) | Journal of Viral Hepatitis | Prospective study of HBV reactivation risk during DAA treatment for HCV in cancer patients with HBV/HCV coinfection |
| [27486112](https://pubmed.ncbi.nlm.nih.gov/27486112/) | 2016 | Cohort | Clinical Infectious Diseases | Analysis of 173 Taiwan/Korea trial participants (103 previously HBV-infected); found no evidence of HBV reactivation during LDV/SOF treatment for HCV |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | Cohort | Journal of Viral Hepatitis | Examined HBV DNA in 25 HBV-coinfected and 765 resolved-HBV patients during interferon-free anti-HCV therapy (incl. LDV/SOF); found low incidence of reactivation |
| [28294955](https://pubmed.ncbi.nlm.nih.gov/28294955/) | 2018 | Case report/Cohort (unspecified, abstract unavailable) | Antiviral Therapy | Reports on hepatitis B reactivation in chronic hepatitis C patients during treatment with ledipasvir and sofosbuvir |
| [28585404](https://pubmed.ncbi.nlm.nih.gov/28585404/) | 2017 | Cohort (prospective) | Hepatology Research | Japanese prospective cohort analyzing frequency and risk factors of HBV reactivation in HCV patients on all-oral DAA (incl. LDV/SOF) therapy |
| [27367295](https://pubmed.ncbi.nlm.nih.gov/27367295/) | 2016 | Review | Antiviral Therapy | Pilot evaluation of whether LDV/SOF can suppress HCV in HBV-coinfected patients; notes the lack of all-oral regimens addressing both viruses simultaneously |

---

## Safety Considerations

Structured safety data (key warnings, contraindications, drug-drug interactions) were not available for Ledipasvir in this evidence pack, and the associated data gap (DG001 — TFDA/HSA labeling warnings and contraindications) is flagged as **Blocking**, meaning a formal safety pre-assessment (S1 stage) cannot yet be completed.

That said, the literature evidence gathered above surfaces an important safety signal that should not be overlooked: **HBV reactivation** — including at least one reported case of acute fulminant hepatitis B (PMID 28366615, found under the related "chronic hepatitis B" indication entry in this evidence pack) — has been documented in HCV/HBV coinfected patients receiving Ledipasvir/Sofosbuvir for HCV treatment. This means that, for any patient population with current or past HBV exposure, HBV virological status should be assessed and monitored throughout treatment, regardless of which indication is being treated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence is preliminary (L3): only one small (n=21), single-arm Phase 2 trial directly tests Ledipasvir/Sofosbuvir in HBV mono-infected patients, and the underlying mechanism for any anti-HBV effect is not established. The remaining 20 trials and most of the literature examine HBV reactivation risk during HCV treatment rather than confirming therapeutic benefit against HBV — in some cases suggesting HBV reactivation (a risk, not a benefit) can occur on this regimen.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank to clarify whether any anti-HBV activity is plausible (data gap DG002)
- TFDA/HSA package insert warnings and contraindications, currently blocking formal safety pre-assessment (data gap DG001)
- A larger, controlled replication of the HBV mono-infection trial (NCT03312023 / PMID 36045503) to confirm the preliminary efficacy signal
- Mechanistic studies distinguishing a direct antiviral effect from a non-specific/immune-mediated effect
- A dedicated risk assessment for HBV reactivation vs. suppression before any further development guardrails can be defined
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

