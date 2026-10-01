---
layout: default
title: Velpatasvir
parent: Low Evidence (L5)
nav_order: 1050
evidence_level: L5
indication_count: 10
---

# Velpatasvir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Velpatasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Velpatasvir is an HCV NS5A inhibitor, marketed in Singapore as a component of fixed-dose combination tablets for hepatitis C.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but none of the **25 matched clinical trials** and **20 publications** tests velpatasvir against HBV.
The only HBV-specific signal is a case report of HBV reactivation during HCV treatment, which is a safety concern rather than evidence of efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (inferred from the trials and literature; the Singapore registry extract has no indication text) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 (indirect and mechanistic only; no HBV efficacy studies) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, velpatasvir is part of the sofosbuvir/velpatasvir (Epclusa) and sofosbuvir/velpatasvir/voxilaprevir (Vosevi) combinations. Its efficacy in hepatitis C is well established. All the retrieved evidence describes it as an NS5A inhibitor.

The mechanistic link to hepatitis B is weak. HBV is a DNA virus that replicates through reverse transcription and has no NS5A homolog. The high TxGNN score (0.9987) most likely reflects closeness between hepatotropic viruses in the knowledge graph, not a shared drug target.

The other top predictions (hepatitis E, hepatitis A, HIV, and several flaviviral diseases) show the same pattern. They have no direct trials or literature and rest only on network proximity.

---

## Clinical Trial Evidence

All matched trials are in hepatitis C. Only NCT04997564 involves HBV, and there HBV is a co-infection managed with prophylactic tenofovir alafenamide (TAF), not treated with velpatasvir.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | 12-week sofosbuvir/velpatasvir with prophylactic TAF in HCV/HBV co-infected adults in China, to prevent HBV reactivation |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | Completed | 228 | Generic velpatasvir + sofosbuvir ± ribavirin in HCV, comparing HIV-coinfected and HCV-monoinfected patients |
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | Completed | 15 | HCV kinetics in plasma and liver during sofosbuvir/velpatasvir ± voxilaprevir |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Vosevi in HCV patients who failed earlier DAA therapy |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | Adverse-event rates in HCV patients on DAAs versus untreated; gives only indirect context for HBV reactivation monitoring |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | Completed | 268 | Sofosbuvir/velpatasvir in HCV with Child-Pugh B cirrhosis |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Completed | 102 | Sofosbuvir/velpatasvir ± ribavirin in HCV with decompensated cirrhosis |
| [NCT02625909](https://clinicaltrials.gov/study/NCT02625909) | Phase 3 | Completed | 222 | Shortened sofosbuvir/velpatasvir for recently acquired HCV in people who inject drugs and people with HIV |
| [NCT03570112](https://clinicaltrials.gov/study/NCT03570112) | N/A | Completed | 40 | HCV in pregnancy, with postpartum sofosbuvir/velpatasvir |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Phase 2 | Completed | 40 | Sofosbuvir/velpatasvir for HCV-associated indolent B-cell lymphoma |

---

## Literature Evidence

No randomized controlled trials were found. All papers concern HCV, and several mention HBV only as a co-infection or a safety issue.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | J Med Case Reports | HBV reactivation, driven by an HBsAg immune-escape mutant, in an anti-HBc-positive patient on sofosbuvir/velpatasvir for HCV |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Clinical study | J Viral Hepat | Simplified HCV treatment in Myanmar; HBV co-infected patients also received tenofovir |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Real-world study | J Virus Eradication | Real-life sofosbuvir/velpatasvir effectiveness in Chinese patients, including HCV/HBV co-infection |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Cohort | J Gastroenterol Hepatol | Real-world sofosbuvir/velpatasvir ± ribavirin in genotype 3 HCV, including a Singapore-based cohort |
| [37286314](https://pubmed.ncbi.nlm.nih.gov/37286314/) | 2023 | Retrospective analysis | BMJ Open | Hepatitis C treatment effectiveness and side effects in prisons in Southern Taiwan |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | Practical overview of HCV diagnosis and treatment |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Pediatric viral hepatitis; HBV treatment is described as far from curative, while HCV DAAs are available |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospective study | Klin Mikrobiol Infekc Lek | Antiviral treatment of chronic hepatitis B and C in children in Ostrava |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Cross-sectional | Ann Hepatol | Global price comparison of HBV and HCV antivirals |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Rev | International Conference on Viral Hepatitis 2017, covering HBV and HCV burden and DAA expectations |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15351P | EPCLUSA TABLET 400MG/100MG (sofosbuvir/velpatasvir) | Film-coated tablet |
| SIN15705P | VOSEVI FILM-COATED TABLETS 400MG/100MG/100MG (sofosbuvir/velpatasvir/voxilaprevir) | Film-coated tablet |

Both products are oral tablets.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the database. One Phase 1 study (NCT03513393) reports that omeprazole reduces velpatasvir absorption by 26–56%, because velpatasvir absorption depends on pH.
- **HBV-specific concern**: A published case report (PMID 31542053) describes HBV reactivation in an anti-HBc-positive patient during sofosbuvir/velpatasvir therapy. Trial NCT04997564 uses prophylactic TAF in HCV/HBV co-infected patients for this reason. HBV screening and monitoring would be needed in any HBV-related use.

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Velpatasvir targets HCV NS5A, which HBV does not have. No retrieved trial or paper shows anti-HBV efficacy, and the only HBV-specific signal is a reactivation risk. The high TxGNN score appears to come from network proximity among hepatitis viruses.

**To proceed, the following is needed:**
- In vitro antiviral activity of velpatasvir against HBV (for example, HBV replication assays)
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the HSA, for safety screening
- A review of HBV reactivation monitoring practice in HCV DAA therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

