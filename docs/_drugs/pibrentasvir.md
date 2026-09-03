---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 782
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Pibrentasvir is an NS5A inhibitor combined with glecaprevir (Glecaprevir/Pibrentasvir, "ABT-493/ABT-530") for chronic hepatitis C virus (HCV) infection. TxGNN predicts a **99.84% score** for hepatitis B virus (HBV) infection as a new indication, but all **14 clinical trials** and **20 publications** returned as supporting evidence describe HCV treatment — none study HBV — indicating this prediction likely reflects a knowledge-graph label confusion rather than genuine mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore regulatory data. Per literature within this evidence pack, Pibrentasvir (as part of Glecaprevir/Pibrentasvir) is indicated for chronic hepatitis C virus (HCV) genotype 1–6 infection |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (see caveat below — supporting trials/literature address HCV, not HBV) |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

`original_moa` is marked as a data gap in this evidence pack. However, the literature evidence collected under this candidate (e.g., PMID 30090878, PMID 31537106) independently identifies pibrentasvir as an **NS5A inhibitor**, co-formulated with glecaprevir (an NS3/4A protease inhibitor) into the fixed-dose combination Glecaprevir/Pibrentasvir, approved for chronic HCV genotypes 1–6.

The core problem with this specific prediction is a **mismatch between the predicted disease label and the supporting evidence**: all 14 clinical trials and 20 publications attached to "hepatitis B virus infection" are in fact hepatitis C virus (HCV) studies — trial titles explicitly reference "Chronic Hepatitis C Virus (HCV) Infection," HCV genotypes, sustained virologic response (SVR12), etc. There is no trial or publication in this set that treats or discusses HBV.

This pattern is consistent with what this same evidence pack documents for several *lower-ranked* predictions for pibrentasvir (hepatitis E, hepatitis A, animal hepatitis, HIV, Omsk hemorrhagic fever, feline AIDS, SIV) — each flagged internally as likely knowledge-graph noise arising from shared "hepatitis"/viral-infection nodes rather than true pharmacological relevance. HBV (Hepadnaviridae, DNA virus with reverse transcriptase) and HCV (Flaviviridae, RNA virus) do not share the NS5A drug target, so there is no established mechanistic basis for pibrentasvir's activity against HBV. **This prediction should be treated as a candidate requiring label/ontology verification, not as evidence-backed repurposing.**

---

## Clinical Trial Evidence

**Caveat: All trials below study chronic hepatitis C virus (HCV) infection, not hepatitis B (HBV). They are listed here because they were returned as the top evidence for this predicted indication in the source data; none directly support an HBV indication.**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | ENDURANCE-3: Glecaprevir/pibrentasvir vs sofosbuvir+daclatasvir in HCV genotype 3 |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Completed | 141 | Glecaprevir/pibrentasvir ± ribavirin in HCV patients who failed prior DAA therapy |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Completed | 177 | Glecaprevir/pibrentasvir ± ribavirin in HCV GT1 previously treated with NS5A inhibitor + sofosbuvir |
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | Completed | 694 | SURVEYOR-II: efficacy/safety in HCV genotypes 2, 3, 4, 5, 6 |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Completed | 174 | SURVEYOR-I: efficacy/safety/PK in HCV genotypes 1, 4, 5, 6 |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Completed | 295 | CERTAIN-1: efficacy/safety in Japanese adults with chronic HCV |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Completed | 384 | Long-term follow-up of SVR durability and DAA resistance after glecaprevir/pibrentasvir |
| [NCT02296905](https://clinicaltrials.gov/study/NCT02296905) | Phase 1 | Completed | 24 | PK/safety of glecaprevir/pibrentasvir in hepatic impairment |
| [NCT02723084](https://clinicaltrials.gov/study/NCT02723084) | Phase 3 | Completed | 136 | CERTAIN-2: glecaprevir/pibrentasvir vs sofosbuvir+ribavirin in HCV genotype 2 |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | Completed | 100 | Efficacy/safety of glecaprevir/pibrentasvir in treatment-naïve Brazilian adults, HCV GT1–6 |

---

## Literature Evidence

**Caveat: All entries below concern hepatitis C (or general viral hepatitis) topics; none specifically studies HBV treatment with pibrentasvir.**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | Lancet Gastroenterol Hepatol | HCV infection in children/adolescents; DAA treatment landscape |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | J Viral Hepat | Real-world glecaprevir/pibrentasvir in HCV patients with severe renal impairment (Taiwan) |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Basic Science | Hepatology | HCV protease-inhibitor resistance-associated substitutions |
| [34344581](https://pubmed.ncbi.nlm.nih.gov/34344581/) | 2021 | Case Report | J Infect Chemother | Glecaprevir/pibrentasvir for HCV flare during daratumumab-based myeloma therapy |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | Chronic HCV diagnosis and treatment overview |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Pediatric viral hepatitis (HBV and HCV) management advances |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment of HCV after DAA failure |
| [35431505](https://pubmed.ncbi.nlm.nih.gov/35431505/) | 2022 | Cohort | World J Gastroenterol | Real-world DAA effectiveness in HIV/HCV genotype 6 co-infection |
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Commentary | Lancet Infect Dis | HBV vaccination after HCV treatment completion |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | PK/PD update on HCV DAA regimens including glecaprevir/pibrentasvir |

---

## Singapore Market Information

Pibrentasvir is currently **not marketed in Singapore (未上市)**, and no HSA registrations exist for this evidence pack (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (hepatitis B virus infection) is not supported by any of its associated clinical trials or literature, all of which describe hepatitis C virus treatment. Combined with pibrentasvir's known NS5A mechanism (HCV-specific target with no HBV relevance) and the fact that this same drug's other predictions (HIV, HEV, HAV, animal hepatitis, veterinary retroviral diseases) are independently flagged as likely knowledge-graph noise, this candidate should not proceed without confirming the prediction is not a disease-label artifact.

**To proceed, the following is needed:**
- Formal MOA and DrugBank category confirmation (currently a data gap, DG002)
- TFDA/HSA-equivalent label, warnings, and contraindications (currently a data gap, DG001 — blocking for safety pre-assessment)
- Verification of the disease ontology mapping used by TxGNN to rule out HBV/HCV node confusion in the knowledge graph
- If mapping is confirmed correct, dedicated in vitro/in vivo evidence of pibrentasvir activity against HBV before any further clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

