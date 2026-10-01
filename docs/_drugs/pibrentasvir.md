---
layout: default
title: Pibrentasvir
parent: Low Evidence (L5)
nav_order: 782
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Pibrentasvir is a hepatitis C virus (HCV) NS5A inhibitor, marketed in Singapore as part of the glecaprevir/pibrentasvir tablet (MAVIRET).
The TxGNN model predicts it may be effective for **hepatitis B virus (HBV) infection**, but the 12 clinical trials and 20 publications retrieved are all about HCV, and **none tests HBV efficacy**.
The high score most likely reflects the closeness of hepatitis-virus nodes in the knowledge graph, not a real drug-target link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (inferred from the trial and product data; the HSA record has no indication text) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only; no HBV-specific studies) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the record. Based on known information, pibrentasvir is an HCV NS5A inhibitor, used together with the NS3/4A protease inhibitor glecaprevir. Its efficacy in chronic HCV is well established across the Phase 2/3 programme.

HBV and HCV are both hepatotropic viruses and both cause chronic hepatitis. That shared "hepatitis" context is probably why the model ranks HBV so highly. Mechanistically, however, the link is weak. HBV is a DNA virus that replicates through reverse transcription and has no NS5A homolog, and no HBV antiviral activity for pibrentasvir appears in the data. The score is therefore best read as graph proximity, not evidence of activity.

The only HBV-related signals are indirect. HBV reactivation is a known risk during HCV direct-acting antiviral therapy, and one commentary (PMID 29485084) discusses HBV vaccination after HCV treatment. Neither supports an HBV treatment indication.

---

## Clinical Trial Evidence

All listed trials are HCV studies, and none reports an HBV efficacy endpoint.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | ENDURANCE-3: glecaprevir/pibrentasvir vs sofosbuvir + daclatasvir in HCV genotype 3 |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Completed | 141 | Efficacy and PK in HCV patients who failed a prior DAA regimen, with or without ribavirin |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Completed | 177 | Pragmatic study in HCV genotype 1 patients previously treated with an NS5A inhibitor + sofosbuvir |
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | Completed | 694 | SURVEYOR-II: HCV genotypes 2–6, with or without ribavirin |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Completed | 174 | SURVEYOR-I: HCV genotypes 1, 4, 5 and 6, including compensated cirrhosis (genotype 1) |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Completed | 295 | CERTAIN-1: Japanese adults with HCV, DAA-naïve and DAA-experienced |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Completed | 384 | Long-term follow-up of resistance and durability of response after glecaprevir/pibrentasvir |
| [NCT02296905](https://clinicaltrials.gov/study/NCT02296905) | Phase 1 | Completed | 24 | PK and safety in normal vs impaired hepatic function |
| [NCT02723084](https://clinicaltrials.gov/study/NCT02723084) | Phase 3 | Completed | 136 | CERTAIN-2: glecaprevir/pibrentasvir vs sofosbuvir + ribavirin in Japanese genotype 2 HCV |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk after HCV cure in HIV/HCV coinfection |

---

## Literature Evidence

No randomised trials were found. The publications below are reviews, cohorts and case reports, mostly about HCV. The two with HBV content are the first two rows.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Review/Commentary | Lancet Infect Dis | Vaccination against hepatitis B after hepatitis C treatment (no abstract available) |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Pediatric viral hepatitis: HCV treatment has advanced, while HBV treatment is described as far from curative |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Multicentre retrospective analysis | J Viral Hepat | Real-world glecaprevir/pibrentasvir in 108 Taiwanese HCV patients with CKD stage 4 or 5 |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | Lancet Gastroenterol Hepatol | HCV infection in children and adolescents; DAA regimens have transformed treatment |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic update on HCV therapies, including glecaprevir/pibrentasvir |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | Practical overview of chronic hepatitis C diagnosis and treatment |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment of HCV patients after DAA failure |
| [34344581](https://pubmed.ncbi.nlm.nih.gov/34344581/) | 2021 | Case report | J Infect Chemother | Glecaprevir/pibrentasvir used for hepatitis exacerbation in a patient with HCV on daratumumab-based therapy |
| [31129632](https://pubmed.ncbi.nlm.nih.gov/31129632/) | 2019 | Case report | BMJ Case Rep | Glecaprevir/pibrentasvir-associated acute liver injury in HCV without HBV co-infection |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Rev | International Conference on Viral Hepatitis 2017; HBV and HCV burden and treatment |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15603P | MAVIRET FILM-COATED TABLET 100MG/40MG | Tablet, film coated (oral) | Not stated in the registration record |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no direct support. Every trial and most of the literature concern HCV, the mechanism (NS5A inhibition) has no HBV counterpart, and the score most likely reflects graph proximity between hepatitis viruses. The other nine predictions (including HIV, HEV and HAV) are also rated Hold.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (blocking; needed for safety screening)
- Mechanism-of-action data from DrugBank
- In vitro or preclinical evidence of anti-HBV activity for pibrentasvir
- If HBV is still of interest, a review of HBV reactivation risk during HCV DAA therapy, which is a safety question rather than a repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

