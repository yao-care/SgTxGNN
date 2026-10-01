---
layout: default
title: Sofosbuvir
parent: Medium Evidence (L3-L4)
nav_order: 915
evidence_level: L4
indication_count: 10
---

# Sofosbuvir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Sofosbuvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Sofosbuvir is a nucleotide-analog antiviral used to treat chronic hepatitis C (HCV).
The TxGNN model predicts it may be effective for **hepatitis B virus infection** (score 99.77%).
Although the candidate lists dozens of trials and 19 publications, almost all are HCV studies. Only a small Phase 2 pilot (21 patients) tests sofosbuvir in HBV, so this is a **model-driven prediction with very limited direct evidence**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (the registry text is empty; inferred from the registered products Epclusa, Harvoni and Vosevi, which are HCV regimens) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Sofosbuvir is a nucleotide-analog inhibitor of the HCV NS5B RNA-dependent RNA polymerase. The DrugBank mechanism field is not available, so this description comes from the evidence pack's rationale.

The mechanistic link to HBV is weak. HBV is a DNA virus that replicates through a reverse transcriptase, so sofosbuvir has no plausible direct target. The very high TxGNN score most likely reflects closeness in the knowledge graph between HCV and other viral hepatitis nodes, not a pharmacological reason.

The data contain no clear anti-HBV efficacy signal beyond one small Phase 2 pilot (ledipasvir/sofosbuvir in HBV mono-infection) whose results were not provided. The data do contain a **safety signal**: HBV reactivation after DAA treatment of HCV in HBV-coinfected patients. In coinfection, sofosbuvir treats the HCV component, not HBV.

## Clinical Trial Evidence

The evidence pack lists 48 matched trials. The most relevant are shown below. Most were matched to HBV by terminology only and study HCV populations.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Ledipasvir/sofosbuvir for 12 weeks in HBV infection. It tests whether HBsAg declines, as seen in earlier HBV/HCV coinfected patients. This is the only direct HBV efficacy study. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Direct-acting antivirals in HCV/HBV coinfection. It measures how often HBV reactivates during anti-HCV treatment. |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL for 12 weeks with prophylactic TAF in HCV/HBV coinfection in China. It evaluates HBV reactivation prevention. |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | Large DAA safety study in HCV. It may inform HBV reactivation safety but does not test an HBV indication. |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | Glecaprevir/pibrentasvir vs sofosbuvir + daclatasvir in HCV genotype 3. No HBV efficacy endpoint. |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Sofosbuvir/velpatasvir/voxilaprevir cohort after DAA failure. The population is HCV. |
| [NCT01939197](https://clinicaltrials.gov/study/NCT01939197) | Phase 2/3 | Completed | 318 | Non-sofosbuvir HCV regimen in HCV/HIV coinfection. Terminology match only. |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | Completed | 268 | Sofosbuvir/velpatasvir in HCV with Child-Pugh B cirrhosis. The population is HCV. |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | Completed | 228 | Generic velpatasvir + sofosbuvir in HCV, with or without HIV coinfection. The population is HCV. |
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | Completed | 15 | HCV kinetics under sofosbuvir/velpatasvir with or without voxilaprevir. The population is HCV. |

## Literature Evidence

No randomized controlled trials were found. Summaries are based on the abstracts provided.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 single-arm | J Med Virol | Ledipasvir/sofosbuvir for 12 weeks in HBV mono-infection. It was prompted by a modest HBsAg reduction seen in HBV/HCV coinfected patients. The primary endpoint is HBsAg decline. |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Trans R Soc Trop Med Hyg | Sofosbuvir/daclatasvir therapy for HCV and HCV/HBV coinfected patients in Egypt. |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Clinical study | Clin Infect Dis | Ledipasvir/sofosbuvir in HCV/HBV coinfected patients in Taiwan. It evaluates HBV reactivation over 108 weeks of follow-up. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Clinical study | J Clin Gastroenterol | Risk of HBV reactivation in patients treated with ledipasvir-sofosbuvir for HCV. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report + review | Medicine | HBV reactivation after successful sofosbuvir/ribavirin treatment of HCV. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Clinical study | Infect Drug Resist | Role of HBV antiviral therapy in HCV/HBV coinfected patients with HBV reactivation after DAA treatment. |
| [25253190](https://pubmed.ncbi.nlm.nih.gov/25253190/) | 2014 | Review | Minerva Pediatr | Treatment of hepatitis B and C in children. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antivirals for hepatitis B and C and their effects on kidney function. |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Epidemiological modelling | Lancet Gastroenterol Hepatol | Global HBV prevalence, cascade of care and prophylaxis coverage. Background only. |
| [39914746](https://pubmed.ncbi.nlm.nih.gov/39914746/) | 2025 | Epidemiological analysis | J Hepatol | HCV treatment numbers in 2014–2023 and lessons for new HBV and HDV therapies. Background only. |

## Singapore Market Information

The registry data do not include approved-indication text. The three products are known HCV regimens.

| Authorization Number | Product Name | Dosage Form | Active Ingredients (strength) |
|---------|------|------|-----------|
| SIN15351P | EPCLUSA | Film-coated tablet | Sofosbuvir/velpatasvir (400 mg/100 mg) |
| SIN14920P | HARVONI | Film-coated tablet | Ledipasvir/sofosbuvir (90 mg/400 mg) |
| SIN15705P | VOSEVI | Film-coated tablet | Sofosbuvir/velpatasvir/voxilaprevir (400 mg/100 mg/100 mg) |

All three are oral. The manufacturer for each is Gilead Sciences Ireland UC, with Patheon Inc. and Hovione among the manufacturing sites.

## Safety Considerations

- **HBV reactivation (from the literature):** Several publications report HBV reactivation after DAA treatment of HCV in HBV-coinfected or previously exposed patients, including one case of acute fulminant hepatitis B (PMIDs 33031326, 29334502, 34864948, 31632097). This matters directly for any HBV-related use of sofosbuvir.

No warnings, contraindications or drug interaction data were available in the evidence pack. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no plausible direct mechanism against HBV, and only one small single-arm Phase 2 pilot (n=21) tests sofosbuvir in HBV. The 48 matched trials are almost all HCV studies that match HBV only by terminology. The most reliable HBV-related signal is a safety concern, HBV reactivation after HCV treatment.

**To proceed, the following is needed:**
- Full results of NCT03312023 / PMID 36045503 (HBsAg and HBV DNA change), and confirmation of the populations and endpoints in the coinfection studies
- The HSA package insert warnings and contraindications, which are currently a blocking gap
- DrugBank mechanism-of-action data
- If HCV/HBV coinfection is the practical use case in Singapore, an HBV screening and monitoring plan before DAA therapy

Among the other predicted indications for sofosbuvir, hepatitis E virus infection has a more plausible mechanism and a small Phase 2 pilot (NCT03282474). It is rated L2 and flagged as a research question, so it may merit a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

