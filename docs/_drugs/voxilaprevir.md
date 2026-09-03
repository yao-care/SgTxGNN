---
layout: default
title: Voxilaprevir
parent: 僅模型預測 (L5)
nav_order: 1068
evidence_level: L5
indication_count: 10
---

# Voxilaprevir
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

# Voxilaprevir: From Hepatitis C (Inferred) to Hepatitis B Virus Infection

## One-Sentence Summary

> Voxilaprevir is described throughout the evidence pack as an HCV NS3/4A protease inhibitor, the third component of the Sofosbuvir/Velpatasvir/Voxilaprevir ("Vosevi") combination used to retreat chronic hepatitis C.
> TxGNN's top prediction assigns **Hepatitis B virus infection** a score of **99.84%**, supported nominally by **5 clinical trials** and **9 publications** — but every trial and paper in the evidence pack is actually about hepatitis C, not hepatitis B.
> The evidence pack's own mechanistic analysis concludes there is **no pharmacological basis** for this prediction, and recommends **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in the evidence pack (`drug.original_indications` is empty). Contextual evidence across all 10 candidates consistently describes Voxilaprevir as an HCV NS3/4A protease inhibitor, co-formulated in Sofosbuvir/Velpatasvir/Voxilaprevir (Vosevi) for chronic hepatitis C. |
| Predicted New Indication | Hepatitis B Virus Infection (rank 1 of 10) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (as scored in the evidence pack) — but the underlying trials/literature are about HCV, not HBV |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no structured mechanism-of-action record exists for Voxilaprevir in this evidence pack (`original_moa: [Data Gap]`). However, the repurposing rationale attached to every one of the 10 predicted indications independently and consistently describes Voxilaprevir as an **HCV NS3/4A serine protease inhibitor**, active only against Hepatitis C virus polyprotein processing.

Based on this mechanistic description, the predicted new indication is **not** pharmacologically plausible. Hepatitis B is a DNA virus that replicates via reverse transcriptase/polymerase and has no NS3/4A-homologous target; there is no structural or functional basis for cross-activity. The evidence pack's own reviewer explicitly flags this: all five "supporting" clinical trials and the majority of the nine "supporting" publications are HCV treatment studies (including the Vosevi Phase 2/3 program itself), which appear to have been attached to the "hepatitis B" label through loose disease-name matching rather than genuine HBV outcome data.

This pattern repeats across all 10 ranked candidates in the pack (Hepatitis E, animal viral hepatitis, Hepatitis A, Omsk hemorrhagic fever, Kyasanur forest disease, HIV, chronic HBV, SIV, feline AIDS) — most trace back to the same underlying HCV/Vosevi trial pool, or have zero evidence at all. This is most consistent with a knowledge-graph clustering artifact around the semantic neighborhood of "hepatitis"/"viral infection"/"immunodeficiency" nodes, rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | Completed | 15 | deLIVER study: HCV viral kinetics under 2-drug (SOF/VEL) vs 3-drug (SOF/VEL/VOX) DAA regimens — HCV patients, not HBV |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Cohort study of Vosevi (SOF/VEL/VOX) in HCV patients who failed prior DAA therapy — HCV-specific |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular outcomes after HCV cure in HIV/HCV co-infected and HCV-monoinfected patients — unrelated to HBV |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Completed | 15 | Drug-interaction study of SOF/VEL/VOX with a hormonal contraceptive in healthy volunteers — not an HBV trial |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | Completed | 281 | RCT of ribavirin + SOF/VEL/VOX in chronic HCV non-responders; despite the term "chronic hepatitis" in the title, the studied disease is HCV, not HBV |

**Note:** All five trials were flagged Relevance Grade "C" (low relevance) by the pipeline's own reviewer — none actually enrolled or treated HBV patients.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Cohort | Lancet Gastroenterol Hepatol | SOF/VEL/VOX retreatment trial for HCV genotype 4 DAA-failure patients in Rwanda — not HBV |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Cohort | J Gastrointestin Liver Dis | Real-world SOF/VEL/VOX efficacy/safety in Romanian genotype-1b HCV non-responders — not HBV |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Cohort | Semin Liver Dis | Review of retreatment strategies for HCV patients who failed DAA therapy — not HBV |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohort | J Clin Exp Hepatol | Resistance-associated substitutions and predictors of DAA treatment failure in an HCV elimination cohort — not HBV |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | Cohort | Voprosy Virusologii | Prevalence/phylogenetics of HIV, HBV and HCV markers among dental patients — mentions HBV only as a co-screened marker, not a Voxilaprevir treatment endpoint |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Review | Hepatology | Evolutionary pathways of HCV protease-inhibitor resistance variants — not HBV |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | PK/PD review of HCV DAA regimens including SOF/VEL/VOX — not HBV |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Review | AIDS Reviews | Conference report on viral hepatitis (both HBV and HCV epidemiology discussed), but no Voxilaprevir-HBV treatment data |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Review | Ann Hepatol | Global drug pricing comparison for HBV and HCV antivirals — pricing analysis only, no efficacy data |

**Note:** No publication in this list reports Voxilaprevir being administered to, or showing efficacy in, HBV-infected patients.

---

## Singapore Market Information

Voxilaprevir currently has **no marketing authorization in Singapore** (`total_licenses: 0`, market status: 未上市 / Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack's own mechanistic analysis finds no plausible connection between Voxilaprevir (an HCV NS3/4A protease inhibitor) and hepatitis B virus infection, and every supporting trial and paper listed for this and the other 9 ranked candidates (HEV, HAV, HIV, animal hepatitis, hemorrhagic fevers, SIV, feline AIDS) traces back to HCV/Vosevi treatment studies rather than genuine evidence for the predicted disease. The high TxGNN score (99.84%) most likely reflects graph-embedding proximity between "hepatitis"-family disease nodes rather than a real repurposing signal. The drug is also not marketed in Singapore, and two blocking/high-severity data gaps (TFDA/HSA label warnings — DG001; formal MOA record — DG002) remain unresolved.

**To proceed, the following is needed:**
- Resolve the apparent disease-label mismatch in the underlying trial/literature tagging pipeline before this candidate (or any of the other 9 in this batch) can be re-scored
- Obtain a formal MOA record for Voxilaprevir from DrugBank (closing DG002)
- Obtain TFDA/HSA label warnings and contraindications (closing DG001, Blocking for S1 safety review)
- If pursuing further, seek independent HBV-specific in vitro or clinical evidence before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

