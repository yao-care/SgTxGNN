---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 1050
evidence_level: L5
indication_count: 10
---

# Velpatasvir
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

# Velpatasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Velpatasvir is the NS5A inhibitor component of combination regimens (sofosbuvir/velpatasvir, sofosbuvir/velpatasvir/voxilaprevir) used to cure chronic Hepatitis C Virus (HCV) infection. The TxGNN model's top prediction suggests possible efficacy in **Hepatitis B Virus (HBV) infection**, but **26 clinical trials** and **20 publications** were retrieved, none of which actually test Velpatasvir against HBV — and the drug's own mechanism (an HCV-specific NS5A inhibitor) provides no biological basis for activity against HBV, a genetically unrelated virus. This candidate should be treated as a model artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection, as part of combination regimens (e.g., sofosbuvir/velpatasvir) |
| Predicted New Indication | Hepatitis B Virus (HBV) infection |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only, no supporting direct study) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action (MOA) record is not available for Velpatasvir in this evidence pack. However, the evidence pack's own drug-disease rationale consistently and independently identifies Velpatasvir as a **direct-acting antiviral (DAA) that specifically inhibits the NS5A phosphoprotein of Hepatitis C Virus** — a Flaviviridae family, positive-strand RNA virus. It is never used as a monotherapy and has no approved indication outside HCV.

Critically, **this prediction does not hold up mechanistically**. HBV belongs to the Hepadnaviridae family and replicates via a reverse-transcriptase/cccDNA pathway that shares no structural or functional homology with HCV's NS5A protein. There is no known cross-reactivity, and the evidence pack's own rationale text explicitly states this: *"Velpatasvir 為 HCV NS5A 蛋白抑制劑…與 HBV…複製機制完全不同，無已知交叉抑制活性。機轉上不成立"* (mechanistically the link does not hold).

Consistent with this, **all 26 retrieved clinical trials are HCV treatment studies**, most graded "C" (low relevance) against the HBV hypothesis, with only one (NCT04997564) actually involving HBV co-infection — and even there, HBV is managed prophylactically with tenofovir (TAF), not Velpatasvir. This same pattern of mechanistic implausibility recurs across all 10 of this drug's top-ranked predictions in the evidence pack (HBV, HEV, HAV, "viral hepatitis, animal", Omsk hemorrhagic fever, Kyasanur forest disease, HIV, feline AIDS, simian immunodeficiency virus, and an unrelated rare neurodevelopmental disorder) — each carries an `evidence_level: L5` and `recommendation: Hold`. This strongly suggests the underlying signal is a **knowledge-graph embedding artifact** (likely driven by "hepatitis"/"viral infection" node proximity) rather than a genuine pharmacological hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | Completed | 228 | Generic VEL/SOF ± ribavirin in HIV/HCV-coinfected patients — treats HCV, not HBV (relevance: low) |
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | Completed | 15 | DAA kinetics in liver (SOF/VEL, SOF/VEL/VOX) for HCV — not HBV (relevance: low) |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Vosevi (SOF/VEL/VOX) in DAA-failure HCV patients — not HBV (relevance: low) |
| [NCT03086044](https://clinicaltrials.gov/study/NCT03086044) | Phase 4 | Unknown | 148 | HCV-positive organ transplantation safety trial — not HBV (relevance: low) |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | Large safety study of DAAs in HCV patients — not HBV (relevance: low) |
| [NCT03570112](https://clinicaltrials.gov/study/NCT03570112) | N/A | Completed | 40 | Natural history/vertical transmission of chronic HCV in pregnancy, treated postpartum with SOF/VEL — not HBV (relevance: low) |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | 12-week SOF/VEL regimen with prophylactic TAF for **HCV/HBV co-infected** patients — HBV managed by TAF, not Velpatasvir |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | Unknown | 25 | HIV regimen switch followed by SOF/VEL therapy for HCV — not HBV (relevance: low) |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | Completed | 268 | SOF/VEL FDC in HCV with Child-Pugh B cirrhosis — not HBV (relevance: low) |
| [NCT02994056](https://clinicaltrials.gov/study/NCT02994056) | Phase 2 | Completed | 32 | SOF/VEL + ribavirin in HCV with Child-Pugh C cirrhosis — not HBV (relevance: low) |

*Note: Across all 26 retrieved trials, essentially none evaluate Velpatasvir's efficacy against HBV; the single co-infection trial manages HBV with a separate agent (tenofovir alafenamide).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | RCT | Lancet Gastroenterol Hepatol | SOF/VEL safety/efficacy in treatment-naive HCV genotype 4 patients (Rwanda) — not HBV |
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | RCT | Lancet Gastroenterol Hepatol | SOF/VEL/VOX re-treatment for DAA-failure HCV genotype 4 (Rwanda) — not HBV |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case Report | J Med Case Rep | Reports **HBV reactivation** in an HBcAb-positive patient while receiving SOF/VEL *for HCV* — an adverse safety signal, not evidence of anti-HBV efficacy |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Reviews pediatric HBV and HCV management; DAAs (incl. velpatasvir) covered only under HCV treatment | 
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | General primary-care review of chronic HCV diagnosis/treatment — not HBV |
| [32405174](https://pubmed.ncbi.nlm.nih.gov/32405174/) | 2020 | Review | J Clin Exp Hepatol | SOF/VEL use in HCV patients with CKD/kidney transplant — not HBV |
| [38910758](https://pubmed.ncbi.nlm.nih.gov/38910758/) | 2024 | Cohort | Cureus | SOF/VEL efficacy in HCV patients with CKD — not HBV |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Cohort | J Gastroenterol Hepatol | Real-world SOF/VEL outcomes in HCV genotype 3 cohort — not HBV |
| [31360020](https://pubmed.ncbi.nlm.nih.gov/31360020/) | 2019 | Cohort | J Clin Exp Hepatol | Generic pan-genotypic SOF/VEL experience in HCV (Myanmar) — not HBV |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Cohort | J Viral Hepat | Simplified HCV treatment strategy; **HBV-coinfected participants were treated concurrently with tenofovir**, not velpatasvir |

*No literature identified provides direct evidence of Velpatasvir efficacy against HBV; the one HBV-specific finding (31542053) describes a reactivation risk during HCV therapy.*

---

## Singapore Market Information

No Singapore (HSA) registration records were found for Velpatasvir in this evidence pack — the drug is currently **not marketed** (`taiwan_regulatory.total_licenses: 0`). No license table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high raw TxGNN similarity score (99.87%), the predicted HBV indication has no mechanistic basis (Velpatasvir's NS5A target is HCV-specific and structurally unrelated to HBV replication machinery) and no supporting clinical or preclinical evidence — all 26 retrieved trials and 20 publications concern HCV treatment, not HBV. This pattern of mechanistic implausibility is consistent across all 10 of the drug's top-ranked predicted indications in this evidence pack, indicating the signal is likely a knowledge-graph artifact rather than a genuine repurposing opportunity. The drug is also not currently marketed in Singapore, and Blocking-severity safety data (TFDA warnings/contraindications) remain unavailable.

**To proceed, the following is needed:**
- In-vitro or preclinical evidence that Velpatasvir has any activity against HBV replication (currently absent)
- Resolution of Data Gap DG001 (TFDA/HSA warnings and contraindications) before any S1 safety screening
- Resolution of Data Gap DG002 (structured MOA record) to support mechanistic review
- If pursued further, re-evaluation of TxGNN scoring methodology given the consistent lack of biological plausibility across this drug's entire top-10 prediction list
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

