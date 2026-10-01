---
layout: default
title: Vilanterol
parent: High Evidence (L1-L2)
nav_order: 1056
evidence_level: L1
indication_count: 10
---

# Vilanterol
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Vilanterol: From Inhaled Combination Bronchodilator Use to Obstructive Lung Disease

## One-Sentence Summary

Vilanterol is a long-acting beta2-agonist (LABA) marketed in Singapore only inside fixed-dose inhaler combinations (Relvar Ellipta, Anoro Ellipta).
The TxGNN model predicts it may be effective for **obstructive lung disease**, with **50 clinical trials** and **20 publications** linked to this direction.
This is essentially an established use: vilanterol-containing products are already used for COPD, so the prediction is not a novel repurposing finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore registration data (indication text is empty for all 3 licences); products are inhaled LABA-containing combinations |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known pharmacology, vilanterol is a long-acting beta2-adrenergic agonist. It relaxes airway smooth muscle through the cAMP pathway and produces sustained bronchodilation. That is directly relevant to the airflow limitation seen in COPD, the main condition under "obstructive lung disease".

The trial portfolio supports this. Vilanterol is studied as part of fluticasone furoate/vilanterol (FF/VI), umeclidinium/vilanterol (UMEC/VI) and fluticasone furoate/umeclidinium/vilanterol (FF/UMEC/VI). These are marketed COPD regimens, so the model's prediction reflects an existing use rather than a new one.

The other nine predicted indications were rated Hold with L4–L5 evidence. They are structural or developmental conditions (e.g. tracheal stenosis, congenital lobar emphysema, respiratory malformation) or non-treatable findings (hyperlucent lung). Bronchodilation has no plausible mechanism for them, and the linked trials are mostly COPD, asthma, pharmacokinetic or safety studies mapped by ontology proximity.

## Clinical Trial Evidence

The 10 most relevant trials are shown below. The pack provides trial designs and objectives, not results.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02729051](https://clinicaltrials.gov/study/NCT02729051) | Phase 3 | Completed | 1055 | 24-week double-blind study comparing single-inhaler FF/UMEC/VI with open triple therapy (FF/VI + UMEC) on trough FEV1 (non-inferiority) |
| [NCT01316900](https://clinicaltrials.gov/study/NCT01316900) | Phase 3 | Completed | 846 | 24-week study of UMEC/VI vs vilanterol alone vs tiotropium in COPD |
| [NCT02119286](https://clinicaltrials.gov/study/NCT02119286) | Phase 3 | Completed | 620 | Adding UMEC (62.5 or 125 mcg) vs placebo to open-label FF/VI in COPD |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | Completed | 1811 | 24-week FF/UMEC/VI once daily vs budesonide/formoterol twice daily on lung function and health status |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Phase 3 | Completed | 905 | 24-week UMEC/VI vs tiotropium; primary endpoint trough FEV1 |
| [NCT02105974](https://clinicaltrials.gov/study/NCT02105974) | Phase 3 | Completed | 1621 | 12-week FF/VI 100/25 vs vilanterol 25 mcg alone, assessing the FF contribution to trough FEV1 |
| [NCT01706328](https://clinicaltrials.gov/study/NCT01706328) | Phase 3 | Completed | 828 | 24-hour lung function profile of FF/VI once daily vs fluticasone propionate/salmeterol twice daily |
| [NCT01376245](https://clinicaltrials.gov/study/NCT01376245) | Phase 3 | Completed | 646 | 24-week FF/VI vs placebo in COPD patients of Asian ancestry |
| [NCT03034915](https://clinicaltrials.gov/study/NCT03034915) | Phase 4 | Completed | 2696 | 24-week UMEC/VI vs UMEC vs salmeterol in COPD |
| [NCT03662711](https://clinicaltrials.gov/study/NCT03662711) | Phase 4 | Terminated | 843 | Long-acting bronchodilator with or without ICS in frail elderly COPD patients after a hospitalised exacerbation; early termination limits interpretability |

## Literature Evidence

The 10 most relevant publications are shown below. Findings reflect what the abstracts state.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | IMPACT trial: once-daily single-inhaler triple therapy vs dual therapy in COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL trial: once-daily triple therapy vs dual ICS/LABA therapy in COPD |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT (follow-up analysis) | Am J Respir Crit Care Med | All-cause mortality with FF/UMEC/VI vs UMEC/VI in IMPACT, including patients originally censored for incomplete vital status |
| [31281061](https://pubmed.ncbi.nlm.nih.gov/31281061/) | 2019 | RCT (post hoc analysis) | Lancet Respir Med | IMPACT analysis of how blood eosinophils and smoking status modify response to triple vs dual therapy |
| [31666084](https://pubmed.ncbi.nlm.nih.gov/31666084/) | 2019 | RCT | Respir Res | EMAX: UMEC/VI vs UMEC and salmeterol monotherapies in symptomatic COPD patients not on ICS |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Meta-analysis | BMC Pulm Med | Systematic review and meta-analysis of RCTs comparing UMEC/VI with other bronchodilators in COPD |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network meta-analysis | Adv Ther | FF/UMEC/VI vs other triple and dual therapies in COPD |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Systematic review | Clin Respir J | Fixed-dose UMEC/VI combination for COPD |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohort | BMJ | New-user cohort comparing FF/UMEC/VI with budesonide-glycopyrrolate-formoterol in routine practice |
| [37213116](https://pubmed.ncbi.nlm.nih.gov/37213116/) | 2023 | Cohort | JAMA Intern Med | COPD exacerbations and pneumonia hospitalisations among new users of LAMA-LABA vs ICS-LABA inhalers |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14737P | Relvar Ellipta Inhalation Powder 200mcg/25mcg | Powder, metered |
| SIN14736P | Relvar Ellipta Inhalation Powder 100mcg/25mcg | Powder, metered |
| SIN14838P | Anoro Ellipta Inhalation Powder 62.5mcg/25mcg | Powder, metered |

All three are held by Glaxo Operations UK Ltd (trading as Glaxo Wellcome Operations) with GlaxoSmithKline LLC. Approved-indication text is not captured in the registration data.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials and several RCT-based publications support vilanterol-containing regimens in COPD, which gives L1 evidence for the top prediction. However, this is an established use rather than a repurposing discovery. The HSA package-insert safety data is missing, so safety cannot yet be screened.

**To proceed, the following is needed:**
- Download and review the HSA package inserts for warnings, contraindications and approved indications
- Correct the empty original-indication field upstream and confirm the current labelled COPD and asthma indications
- Obtain mechanism-of-action data from DrugBank to complete the mechanistic-link analysis
- Treat the nine lower-ranked predictions as Hold; do not pursue them without new clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

