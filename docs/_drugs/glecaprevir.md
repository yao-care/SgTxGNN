---
layout: default
title: Glecaprevir
parent: 僅模型預測 (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
---

# Glecaprevir
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

# Glecaprevir: From Hepatitis C to HIV Infectious Disease

## One-Sentence Summary

Glecaprevir is an HCV NS3/4A serine protease inhibitor, co-formulated with pibrentasvir (Mavyret/Maviret), approved globally for the treatment of chronic Hepatitis C virus (HCV) infection across all genotypes.
The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with **15 clinical trials** and **20 publications** retrieved — however, all trials document HCV treatment in HIV/HCV co-infected patients, not direct anti-HIV antiviral activity, and the mechanistic basis for this prediction is critically weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis C virus infection (all genotypes, GT1–6) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current dataset. Based on known pharmacological information, Glecaprevir is an HCV NS3/4A serine protease inhibitor, combined with pibrentasvir (an NS5A inhibitor) in the fixed-dose combination Mavyret/Maviret. Together, they achieve >97% sustained virological response (SVR12) across HCV genotypes 1–6, including in patients with compensated cirrhosis, severe renal impairment, and HIV/HCV co-infection.

The predicted repurposing to HIV infectious disease faces a fundamental mechanistic barrier. HIV-1 replication depends on an **aspartyl protease** — structurally and catalytically distinct from HCV's NS3/4A serine protease. Glecaprevir has no known cross-inhibitory activity against HIV protease, reverse transcriptase, or integrase. The existing evidence base consists entirely of trials treating **HCV** in HIV/HCV co-infected patients, with HIV status as a baseline covariate rather than a therapeutic target.

This prediction most likely reflects a knowledge graph artefact: the frequent clinical co-occurrence of HIV and HCV in real-world patient datasets may have created an associative node linkage in TxGNN's training graph, generating a high-confidence but pharmacologically unsupported prediction. The repurposing rationale is assessed as weak.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | Completed | 153 | EXPEDITION-2: G/P efficacy and safety in adults with chronic HCV (GT1–6) and HIV-1 co-infection; primary endpoint was HCV SVR12, not anti-HIV activity |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) | Phase 3 | Completed | 33 | MAGELLAN-3: G/P + sofosbuvir + ribavirin in HCV/HIV co-infected patients with prior virologic failure in AbbVie studies; provides G/P safety data in HIV-positive patients |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV/HCV co-infected vs. HIV mono-infected controls; indirect safety signal for G/P use in HIV-positive patients |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | Completed | 546 | Large Asian HCV trial (GT1–6) with or without HIV co-infection; evaluated G/P efficacy and safety across both populations |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | Completed | 45 | PURGE-C: 4-week G/P for acute HCV infection with or without HIV-1 co-infection |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | Completed | 160 | G/P in Asian HCV-infected patients (GT1–6) with compensated cirrhosis, with or without HIV co-infection |
| [NCT04189627](https://clinicaltrials.gov/study/NCT04189627) | N/A | Completed | 99 | DETI-2: Real-world G/P effectiveness in Russian adolescents aged 12–17 with HCV, including HIV/HCV co-infected subgroup |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | Completed | 83 | Pilot study of G/P (and paritaprevir-based regimens) for recently acquired HCV infection with or without HIV co-infection |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | Not Yet Recruiting | 30 | Pharmacokinetics and safety of G/P initiated during pregnancy in women with HCV with or without HIV; includes infant safety follow-up |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | N/A | Completed | 17 | Telemedicine at needle exchanges: combined HCV treatment, HIV PrEP, and opioid use disorder medication delivered to syringe service program attendees |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | Cohort/Real-world | Clinical and Experimental Hepatology | Real-life G/P efficacy and safety in HIV/HCV co-infected patients receiving bictegravir/emtricitabine/tenofovir alafenamide; confirms ARV compatibility and HCV SVR in HIV-positive patients |
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohort/Real-world | Journal of Antimicrobial Chemotherapy | Real-world G/P response in HIV/HCV co-infected patients in clinical practice; HIV status associated with lower SVR rates vs. mono-infected in some DAA regimens |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | Case Report | Clinical Journal of Gastroenterology | Successful G/P treatment of a Japanese hemophilia patient co-infected with HIV and HCV genotype 4a; demonstrates utility in complex HIV/HCV co-infected patients on antiretrovirals |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Systematic Review | International Journal of Antimicrobial Agents | Meta-analysis of 13 studies (n=3,082): overall SVR12 rate of 97.8% with G/P across HCV GT1–6; includes subgroup data from HIV co-infected populations |
| [29845496](https://pubmed.ncbi.nlm.nih.gov/29845496/) | 2018 | Review | Hepatology International | G/P expands HCV treatment reach with shorter duration and broader population coverage, including HIV/HCV co-infected patients previously considered difficult to treat |
| [35877601](https://pubmed.ncbi.nlm.nih.gov/35877601/) | 2022 | Review | PLoS ONE | Comparative analysis of drug approval timelines for TB, HIV, and HCV; contextualizes G/P within the broader DAA development and regulatory landscape |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opinion on Pharmacotherapy | HCV NS3/4A protease inhibitor therapy overview; discusses G/P use in HIV co-infected patients and key drug-drug interaction considerations with antiretrovirals |
| [32754824](https://pubmed.ncbi.nlm.nih.gov/32754824/) | 2020 | Cohort/Real-world | Advances in Therapy | Real-world 8-week G/P in treatment-naïve compensated cirrhosis patients; validates EXPEDITION-8 findings with heterogeneous real-world population |
| [38367631](https://pubmed.ncbi.nlm.nih.gov/38367631/) | 2024 | Review | The Lancet Gastroenterology & Hepatology | Global registration and reimbursement data for HCV DAA therapies including G/P across 160+ countries; policy and access landscape |
| [30090878](https://pubmed.ncbi.nlm.nih.gov/30090878/) | 2018 | Review | Drugs of Today | Comprehensive G/P pharmacology, pharmacokinetics, efficacy, and safety review; first approved 8-week pangenotypic HCV regimen for adults |

---

## Singapore Market Information

Glecaprevir (as the fixed-dose combination Mavyret/Maviret with pibrentasvir) is currently **not registered with HSA Singapore**. No product licences are on record in this dataset.

> **Note for context**: Glecaprevir/pibrentasvir has received regulatory approval from the US FDA (August 2017), EMA (July 2017), and TGA (Australia) for chronic HCV infection across all genotypes. Singapore market entry has not been confirmed in the current data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.87%), the mechanistic foundation for using Glecaprevir against HIV infectious disease is absent. Glecaprevir inhibits HCV NS3/4A **serine protease**, while HIV-1 replication requires an entirely different enzyme class (**aspartyl protease**), with no structural homology or known cross-inhibitory activity. Every trial and publication in this evidence pack documents HCV treatment outcomes in HIV/HCV co-infected patients — not anti-HIV efficacy. This is a likely false-positive prediction driven by clinical co-occurrence in knowledge graph training data.

**To proceed, the following is needed:**
- **In vitro anti-HIV activity screen**: Direct testing of Glecaprevir against HIV-1 replication in cell culture (e.g., MT-4 or PBMC assay) and against HIV-1 protease enzyme
- **Mechanistic data gap resolution**: Obtain full DrugBank MOA entry and structural analysis comparing Glecaprevir binding conformation with HIV protease active site
- **Singapore HSA registration**: Evaluate feasibility pathway if repurposing evidence ever emerges
- **Deprioritisation if in vitro negative**: Should no anti-HIV activity be demonstrated in preclinical screening, this indication should be formally removed from the repurposing candidate list and flagged as a knowledge graph artefact

---

> ⚠️ **Research Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

