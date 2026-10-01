---
layout: default
title: Voxilaprevir
parent: Low Evidence (L5)
nav_order: 1068
evidence_level: L5
indication_count: 10
---

# Voxilaprevir
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

# Voxilaprevir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Voxilaprevir is an HCV NS3/4A protease inhibitor, marketed in Singapore as part of the three-drug combination Vosevi (sofosbuvir/velpatasvir/voxilaprevir) for hepatitis C.
The TxGNN model predicts it may be effective for **Hepatitis B Virus Infection**, but **none of the 5 linked clinical trials and none of the 9 linked publications tests HBV efficacy**. All of them concern hepatitis C. This is a model prediction only, so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (inferred from the Vosevi program; the Singapore registration record contains no indication text) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (the Evidence Pack lists L4, but no HBV-specific preclinical or mechanistic study is present) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, voxilaprevir is part of the fixed-dose combination sofosbuvir/velpatasvir/voxilaprevir. Its efficacy in hepatitis C is well established, with sustained virologic response rates above 95% reported in the Phase 2/3 program and real-world cohorts.

A direct mechanistic link to HBV is **not supported**. Voxilaprevir targets the HCV NS3/4A serine protease, and HBV encodes no homologous protease. The high TxGNN score (0.998) most likely reflects proximity to other hepatitis-virus nodes in the knowledge graph rather than a real drug target.

The only clinical connection is indirect. In patients co-infected with HBV and HCV, clearing HCV with direct-acting antivirals can trigger HBV reactivation. That is a safety concern, not a therapeutic effect.

The other top predictions share the same weakness. They include hepatitis E, hepatitis A, HIV, Omsk hemorrhagic fever, Kyasanur forest disease, and several animal-disease nodes. All are L4-L5 with no supporting efficacy data.

## Clinical Trial Evidence

Titles for some trials are truncated in the source, so the HCV focus is inferred from the title text and the known Vosevi program.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | Completed | 15 | Liver and plasma sampling of HCV kinetics during sofosbuvir/velpatasvir ± voxilaprevir; no HBV endpoint |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Prospective cohort of Vosevi in HCV patients who failed prior DAA therapy; no HBV endpoint |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk after HCV eradication in HCV and HIV/HCV patients; not HBV-related |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Completed | 15 | Drug interaction study with a hormonal contraceptive; pharmacokinetics only, no HBV activity data |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | Completed | 281 | Randomized trial of ribavirin added to sofosbuvir/velpatasvir/voxilaprevir in chronic hepatitis C non-responders; the registry record should be checked for HBV co-infection data |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Single-arm trial | Lancet Gastroenterol Hepatol | Sofosbuvir/velpatasvir/voxilaprevir retreatment of HCV after DAA failure in Rwanda (SHARED-3) |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Cohort | J Gastrointestin Liver Dis | Real-world use in Romanian genotype 1b HCV patients who did not respond to earlier DAAs |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohort | J Clin Exp Hepatol | Resistance-associated substitutions and predictors of DAA failure in an Indian HCV elimination cohort |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment of HCV patients after DAA failure |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic considerations of HCV therapy |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Preclinical/virology | Hepatology | HCV protease inhibitor resistance variants and their persistence |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Rev | International Conference on Viral Hepatitis 2017: HBV and HCV burden and HCV direct-acting antivirals |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Economic analysis | Ann Hepatol | International price comparison of HBV and HCV antivirals |
| [31915372](https://pubmed.ncbi.nlm.nih.gov/31915372/) | 2020 | Review | Nat Rev Gastroenterol Hepatol | Viraemic organ transplantation and antiviral therapies (no abstract available) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15705P | VOSEVI Film-Coated Tablets 400mg/100mg/100mg | Tablet, film coated (oral) | Not stated in the registration record |

## Safety Considerations

- **Hepatitis B reactivation**: In HBV/HCV co-infected patients, clearing HCV with direct-acting antivirals can trigger HBV reactivation. This is a labeled safety concern, so HBV screening and monitoring are needed before Vosevi is used.
- **Other safety information**: Please refer to the package insert for warnings and contraindications. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on graph similarity alone. Voxilaprevir has no plausible HBV target, and none of the linked trials or publications reports an HBV efficacy endpoint. The only HBV-related signal is the reactivation risk during HCV treatment.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Verification of NCT04695769 and NCT06180590 registry records for HBV co-infection enrollment and HBV virologic outcomes
- Any in vitro or in vivo evidence of anti-HBV activity, which does not currently exist in the pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

