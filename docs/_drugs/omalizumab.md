---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 731
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

Using the report template supplied in the prompt (this is a self-contained content-generation task, not a coding/debugging task, so no additional skill applies).

One judgment call up front: the evidence pack contains **10** TxGNN-predicted indications, not one. Rank 1 by raw score ("bronchitis") is explicitly flagged in its own `repurposing_rationale` as a likely **ontology-confusion artifact** (asthma vs. bronchitis embedding proximity) and is scored `Hold`/L4. The strongest, most clinically defensible candidate is rank 3, **"obstructive lung disease"** (L1 evidence, `Proceed with Guardrails`). I built the main report around that candidate and added a closing table listing why the others were not selected, rather than mechanically reporting the top raw score.

Also: `drug.original_indications` and `taiwan_regulatory.licenses` are both empty (0 SG registrations), so I did not fabricate a Singapore-approved original indication — I stated the gap directly and sourced the "internationally approved for allergic asthma" claim from the literature evidence itself (not external knowledge).

---

# Omalizumab: From Allergic Asthma to Broader Obstructive Lung Disease (Including COPD)

## One-Sentence Summary

Omalizumab is a humanized anti-IgE monoclonal antibody internationally established for moderate-to-severe allergic asthma, but it currently holds **no marketing registration in Singapore**. Of 10 TxGNN-predicted indications, the most defensible is **Obstructive Lung Disease** (a category extension covering allergen-sensitized COPD alongside classic allergic asthma), supported by **50 clinical trials** (including multiple completed Phase 3 RCTs) and **20 publications**, several of which are systematic reviews or comparative-effectiveness cohorts.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Singapore's regulatory dataset — Omalizumab has 0 licenses/registrations in Singapore. Internationally (per literature in this evidence pack, e.g. PMID 21401438, 11496232), it is approved for moderate-to-severe allergic asthma and chronic spontaneous urticaria. |
| Predicted New Indication | Obstructive Lung Disease (broadened beyond classic allergic asthma to include allergen-sensitized COPD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from the DrugBank field in this evidence pack (flagged as data gap DG002). However, the mechanism is consistently described across the pack's own literature evidence: Omalizumab is a recombinant humanized monoclonal antibody that binds free serum IgE and blocks its interaction with the high-affinity FcεRI receptor on mast cells and basophils, downregulating receptor expression and interrupting the IgE-mediated allergic inflammatory cascade (PMID 11270941, 15753888, 28189435).

Allergic asthma — the drug's established, internationally approved use — is itself a core subtype within the broader "obstructive lung disease" category. The TxGNN prediction essentially recognizes that IgE-driven airway inflammation and bronchoconstriction, the drug's proven mechanism, extends mechanistically to other allergen-sensitized obstructive airway phenotypes.

What makes this more than a trivial restatement of the existing asthma indication is the emerging evidence for extending use into allergen-sensitized **COPD**, a distinct obstructive lung disease phenotype historically outside Omalizumab's label. An actively recruiting Phase 2 trial (NCT07059091, "COPD-OMA," n=334) is directly testing this hypothesis, and it is graded "A" relevance in the evidence pack. This represents genuine indication broadening rather than merely re-confirming asthma efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00232050](https://clinicaltrials.gov/study/NCT00232050) | Phase 3 | Completed | 327 | Safety and efficacy of omalizumab in moderate-to-severe bronchial asthma |
| [NCT07059091](https://clinicaltrials.gov/study/NCT07059091) | Phase 2 | Recruiting | 334 | COPD-OMA: omalizumab in allergen-sensitized/exposed individuals with COPD |
| [NCT02654145](https://clinicaltrials.gov/study/NCT02654145) | Phase 4 | Completed | 145 | OSMO study: switching from omalizumab to mepolizumab in severe eosinophilic asthma inadequately controlled on omalizumab |
| [NCT01202903](https://clinicaltrials.gov/study/NCT01202903) | Phase 3 | Completed | 616 | Omalizumab vs placebo in Chinese patients with moderate-to-severe persistent allergic asthma uncontrolled on GINA Step 4 therapy |
| [NCT00079937](https://clinicaltrials.gov/study/NCT00079937) | Phase 3 | Completed | 628 | 1-year efficacy, safety, PK/PD of omalizumab in children (6–<12y) with inadequately controlled allergic asthma |
| [NCT00046748](https://clinicaltrials.gov/study/NCT00046748) | Phase 3 | Completed | 484 | 28-week efficacy/safety/tolerability of SC omalizumab in adults/adolescents with severe persistent allergic asthma |
| [NCT00500539](https://clinicaltrials.gov/study/NCT00500539) | Phase 3 | Completed | 155 | Safety and immunogenicity of liquid-formulation omalizumab in adolescents/adults with persistent allergic asthma |
| [NCT01976208](https://clinicaltrials.gov/study/NCT01976208) | Phase 2/3 | Completed | 630 | Safety and efficacy of a recombinant humanized anti-IgE mAb in allergic asthma |
| [NCT00264849](https://clinicaltrials.gov/study/NCT00264849) | Phase 4 | Completed | 406 | Persistency of response to omalizumab over 32 weeks as add-on to optimized asthma therapy |
| [NCT01007149](https://clinicaltrials.gov/study/NCT01007149) | Phase 3 | Completed | 79 | Effect of omalizumab on FcεRI expression on basophils/dendritic cells in severe non-atopic asthma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36740144](https://pubmed.ncbi.nlm.nih.gov/36740144/) | 2023 | Cohort (target trial emulation) | J Allergy Clin Immunol | Comparative effectiveness of omalizumab, mepolizumab, and dupilumab in asthma |
| [36581073](https://pubmed.ncbi.nlm.nih.gov/36581073/) | 2023 | Systematic Review/Meta-analysis | J Allergy Clin Immunol Pract | Omalizumab in allergic bronchopulmonary aspergillosis |
| [39186985](https://pubmed.ncbi.nlm.nih.gov/39186985/) | 2024 | Cohort | J Allergy Clin Immunol | Real-world ADVANTAGE study: dupilumab vs omalizumab on exacerbations and steroid use |
| [38235607](https://pubmed.ncbi.nlm.nih.gov/38235607/) | 2024 | Systematic Review/Meta-analysis | Ther Adv Respir Dis | Effects of omalizumab on lung function in moderate-to-severe allergic asthma |
| [41033334](https://pubmed.ncbi.nlm.nih.gov/41033334/) | 2025 | Phase 4 RCT | Lancet Respir Med | EVEREST head-to-head trial: dupilumab vs omalizumab in CRSwNP with coexisting asthma |
| [11496232](https://pubmed.ncbi.nlm.nih.gov/11496232/) | 2001 | Registrational efficacy report | J Allergy Clin Immunol | Foundational efficacy data for omalizumab in severe allergic asthma |
| [21401438](https://pubmed.ncbi.nlm.nih.gov/21401438/) | 2011 | Review | Expert Opin Drug Saf | Long-term safety of omalizumab in asthma |
| [15753888](https://pubmed.ncbi.nlm.nih.gov/15753888/) | 2005 | Mechanistic study | J Allergy Clin Immunol | Anti-inflammatory effects confirming central role of IgE in allergic inflammation |
| [25404353](https://pubmed.ncbi.nlm.nih.gov/25404353/) | 2014 | Review | Paediatr Drugs | Omalizumab use and current indications in pediatric patients |
| [27824606](https://pubmed.ncbi.nlm.nih.gov/27824606/) | 2016 | RCT | Eur Respir J | Omalizumab reduces bronchial mucosal IgE and improves lung function in non-atopic asthma |

---

## Singapore Market Information

Omalizumab currently holds **no marketing authorization or registration in Singapore** — the regulatory dataset lists 0 licenses. There is no local product, dosage form, or approved-indication text on file to report.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are not populated in this evidence pack — flagged as data gap DG001, "Blocking" severity, which must be resolved before any S1 safety review can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (e.g., NCT00232050, NCT01202903, NCT00079937, NCT00046748) already establish omalizumab's efficacy in allergic asthma, the dominant subtype of "obstructive lung disease," giving this candidate L1 evidence strength. The genuinely novel extension — allergen-sensitized COPD — is still supported only by a single ongoing Phase 2 trial (NCT07059091), so the guardrail is specifically around the COPD-extension claim, not the asthma-core claim.

**To proceed, the following is needed:**
- DrugBank-sourced MOA record (DG002) to formally document mechanism instead of relying on literature-embedded descriptions
- TFDA/HSA-equivalent package insert warnings, contraindications, and DDI data (DG001 — currently blocking any safety review)
- Confirmation of whether Singapore intends to pursue a first-time registration for omalizumab, since there is currently no local regulatory pathway or precedent on file
- Results from the ongoing COPD-OMA trial (NCT07059091, est. completion 2031-05) before extending any claim beyond allergic asthma to allergen-sensitized COPD
- Disease-ontology validation of the TxGNN "obstructive lung disease" node to confirm it isn't conflating asthma, COPD, and bronchitis subtypes (see note below on rejected candidates)

---

### Other Candidate Indications Screened (Not Selected)

TxGNN's raw top-ranked prediction by score was **not** obstructive lung disease — it was "bronchitis" (score 99.999%). It is listed here for transparency, along with the other 8 predictions, none of which met the bar for a primary recommendation:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Why Not Selected |
|------|---------|------|------|------|------|
| 1 | Bronchitis | 99.9992% | L4 | Hold | Pack's own rationale flags likely KG ontology confusion (asthma vs. bronchitis embedding proximity); trial/literature evidence is asthma-specific, not bronchitis-specific |
| 2 | Atopic Eczema | 99.97% | L2 | Research Question | Mixed evidence — IgE's role in AD pathology is secondary to Th2/IL-4/IL-13; source literature itself titled "evidence for and against its use" |
| 4 | Dermatitis | 99.97% | L2 | Research Question | Near-duplicate of atopic eczema evidence set; one case report shows omalizumab may paradoxically trigger dermatitis (PMID 37988298) |
| 5 | Bronchial Neoplasm | 99.95% | L5 | Hold | No oncology-specific evidence; retrieved trials/literature are all asthma-related — likely KG embedding proximity, not a real signal |
| 3, 6–10 | Obstructive Lung Disease (selected above), Acne Keloid, Acrodermatitis Chronica Atrophicans, Hydroa Vacciniforme (familial), Neonatal Dermatomyositis, Secondary Childhood ILD | 99.92–99.97% | L5 (except selected) | Hold | Zero clinical trials, zero literature — model-score-only predictions with no mechanistic basis provided |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

