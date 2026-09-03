---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 915
evidence_level: L5
indication_count: 10
---

# Sofosbuvir
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

# Sofosbuvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

> Sofosbuvir is a nucleotide analogue NS5B/RNA-dependent RNA polymerase (RdRp) inhibitor established for the treatment of chronic **Hepatitis C Virus (HCV)** infection. TxGNN's top-ranked prediction proposes it may also be effective for **Hepatitis B Virus (HBV) infection** (score 99.77%), but critical review of the retrieved **50 clinical trials** and **18 publications** shows most are HCV-focused studies and one safety signal actually points in the opposite direction (HBV reactivation during HCV treatment) — so this specific candidate is **not currently actionable** and is recommended for **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection (based on trial/literature context; sofosbuvir is not registered in Singapore, so no local regulatory indication text exists) |
| Predicted New Indication | Hepatitis B Virus (HBV) infection |
| TxGNN Prediction Score | 99.77% (rank 3759) |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, a formally verified mechanism-of-action (MOA) record is not available for this candidate (data gap DG002, source: DrugBank API — not yet queried). Based on the descriptions embedded throughout the retrieved trial and literature evidence, sofosbuvir is consistently characterized as a nucleotide prodrug that is metabolized intracellularly to its active triphosphate form, which inhibits the HCV NS5B RNA-dependent RNA polymerase (RdRp) — the enzyme HCV uses to replicate its positive-strand RNA genome. This mechanism is the basis for sofosbuvir's approved efficacy in chronic HCV infection.

HBV, however, is a partially double-stranded **DNA virus** (family Hepadnaviridae) that replicates via an RNA intermediate using a **reverse transcriptase**, not an RdRp. There is no direct structural or enzymatic overlap between sofosbuvir's validated target and HBV's replication machinery, which weakens the biological plausibility of this specific repurposing hypothesis compared to sofosbuvir's other predicted RNA-virus indications (e.g., Hepatitis E virus, itself an RdRp-dependent RNA virus).

Consistent with this mechanistic gap, the majority of the 50 retrieved trials are standard HCV treatment studies that merely **co-enrolled or co-occurred with** HBV-coinfected patients (safety/reactivation monitoring), rather than testing sofosbuvir's efficacy against HBV itself. More importantly, several publications (e.g., PMID 33031326, PMID 29334502) report that direct-acting antivirals including sofosbuvir can **trigger HBV reactivation** during HCV treatment in coinfected patients — a safety signal moving in the *opposite* direction from a therapeutic claim. One dedicated Phase 2 open-label pilot study (NCT03312023 / PMID 36045503) did test ledipasvir/sofosbuvir directly in HBV mono-infected subjects (n=21), providing the only genuine efficacy-oriented data point for this indication, but it is small, uncontrolled, and insufficient on its own to support progression.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label pilot testing ledipasvir/sofosbuvir for 12 weeks in HBV mono-infected subjects; primary/secondary endpoints were HBsAg and HBV DNA decline — the only trial directly targeting HBV efficacy in this evidence set |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL for HCV treatment in HCV/HBV co-infected patients, with prophylactic TAF to *prevent* HBV reactivation — a reactivation-management design, not an HBV efficacy study |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of incidence/predisposing factors for HBV reactivation during direct-acting anti-HCV therapy in HCV/HBV coinfected patients — a safety surveillance study, not a treatment trial |
| [NCT01939197](https://clinicaltrials.gov/study/NCT01939197) | Phase 2/3 | Completed | 318 | TURQUOISE-I: HCV genotype 1/4 + HIV coinfection study; graded "B" relevance in the evidence pack but primary endpoint is HCV RNA suppression, not HBV |

*Note: The remaining ~46 trials retrieved for this candidate are conventional HCV treatment studies (sofosbuvir ± other DAAs, various populations) that co-occur with the "hepatitis" concept in the knowledge graph but do not test HBV efficacy; they are omitted here as not directly relevant.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label | Journal of Medical Virology | Ledipasvir/sofosbuvir for 12 weeks in HBV mono-infected subjects; evaluated HBsAg and HBV DNA decline (companion publication to NCT03312023) |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort (HCV/HBV coinfection) | Trans R Soc Trop Med Hyg | Sofosbuvir/daclatasvir therapy outcomes in chronic HCV and HCV/HBV coinfected Egyptian patients |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort, 108-week follow-up | Clinical Infectious Diseases | Taiwan cohort: HBV reactivation monitoring during and after ledipasvir/sofosbuvir treatment of HCV/HBV coinfected patients |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort (safety signal) | Journal of Clinical Gastroenterology | Examines risk of HBV reactivation among patients treated with ledipasvir/sofosbuvir for HCV — reactivation risk, not therapeutic benefit |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Case series | Infection and Drug Resistance | Management of HBV reactivation post-DAA treatment in HCV-HBV coinfected patients with pretreatment HBeAg seroconversion |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report (opposite-direction safety signal) | Medicine | HBV reactivation *after* successful HCV treatment with sofosbuvir and ribavirin |

---

## Singapore Market Information

Sofosbuvir is **not currently marketed in Singapore** — the evidence pack records 0 registrations and no license entries, so no Singapore-specific product or approved-indication information is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Formal Singapore/TFDA-sourced warnings and contraindications for sofosbuvir are recorded as a **Blocking** data gap — DG001 — pending retrieval and parsing of the official package insert.)

Separately, note that the literature review above identified a specific safety signal relevant to this candidate: several reports describe **HBV reactivation** occurring in HCV/HBV coinfected patients during or after sofosbuvir-containing DAA therapy. This should be treated as a safety consideration for any coinfected population, independent of the (unproven) hypothesis that sofosbuvir treats HBV directly.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for this candidate is weak — sofosbuvir targets HCV's RNA-dependent RNA polymerase, which has no direct counterpart in HBV's DNA-replication/reverse-transcriptase biology. Most of the retrieved trial and literature evidence reflects HCV treatment studies that happen to include HBV-coinfected patients for safety monitoring, and at least one recurring signal (HBV reactivation) points against, rather than for, a therapeutic effect. The single directly relevant trial (NCT03312023, n=21) is too small and uncontrolled to support progression on its own.

**To proceed, the following is needed:**
- Formal DrugBank MOA confirmation (DG002) to rigorously assess target compatibility with HBV biology
- TFDA/HSA package insert warnings and contraindications (DG001, Blocking) before any S1 safety pre-assessment can begin
- Larger controlled follow-up to NCT03312023/PMID 36045503 with virologic (HBsAg seroconversion) endpoints, if this indication is still to be pursued
- Given the mechanistic mismatch here, consider prioritizing **Hepatitis E virus infection** (rank 2 in this evidence pack, evidence level L2, decision stage S2 "Research Question") instead, as it has a biologically coherent RdRp-based rationale, in vitro confirmation, and an actual dedicated Phase 2 pilot trial (NCT03282474) testing sofosbuvir for HEV directly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

