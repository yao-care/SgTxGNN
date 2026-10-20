---
layout: default
title: Vilanterol
parent: High Evidence (L1-L2)
nav_order: 1066
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Vilanterol: predicted new indication Obstructive lung disease (evidence level L1). Approved use: COPD, asthma, bronchitis, pulmonary emphysema"
monitor_inn: "Vilanterol"
predicted_indications: ["hyperlucent lung", "tracheal stenosis", "bronchial neoplasm (disease)", "respiratory malformation", "tracheal calcification", "laryngotracheitis"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Vilanterol: From COPD and Asthma to Obstructive Lung Disease

## One-Sentence Summary

Vilanterol is a long-acting beta2-agonist bronchodilator, originally used for chronic obstructive pulmonary disease (COPD) and asthma.
The TxGNN model predicts it may be effective for **obstructive lung disease**, but this is an umbrella category that already covers its approved uses, so it is a confirmation of existing indications rather than a true new repurposing signal.
The data compiled for this report include **29 clinical trials** and **19 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COPD, asthma, bronchitis, pulmonary emphysema (the regulatory indication text is blank in the Singapore records, so these come from the knowledge graph) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Vilanterol is a long-acting beta2-adrenergic agonist. It relaxes airway smooth muscle through cAMP-mediated bronchodilation, giving 24-hour activity with once-daily dosing. It is used in combination with fluticasone furoate (an inhaled corticosteroid) and with umeclidinium (a long-acting muscarinic antagonist). Detailed mechanism-of-action data are not available in the compiled data, so this description is based on established pharmacology.

"Obstructive lung disease" is the umbrella category for vilanterol's existing indications (COPD, asthma, bronchitis, emphysema). The high score therefore reflects on-label use. The other predicted indications are much weaker. Hyperlucent lung, interstitial emphysema, compensatory emphysema and congenital lobar emphysema are inferred only from network proximity to emphysema. Tracheal stenosis, tracheal calcification, laryngotracheitis and respiratory malformation have no clear mechanistic link to bronchodilation. Bronchial neoplasm is only indirectly related, through perioperative COPD management in lung cancer patients. None of these has supporting clinical evidence for vilanterol.

## Clinical Trial Evidence

Of the 29 trials, the 10 most relevant are listed below (completed Phase 3 trials with direct evidence first).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03162055](https://clinicaltrials.gov/study/NCT03162055) | Phase 3 | Completed | 1119 | Glycopyrronium/formoterol vs umeclidinium/vilanterol over 24 weeks in moderate to very severe COPD (AERISTO) |
| [NCT02094937](https://clinicaltrials.gov/study/NCT02094937) | Phase 3 | Completed | 430 | Fluticasone furoate step-down from FF/VI 100/25 mcg in well-controlled asthma (Japanese patients) |
| [NCT01134042](https://clinicaltrials.gov/study/NCT01134042) | Phase 3 | Completed | 587 | FF/VI vs FF alone vs fluticasone propionate in persistent asthma over 24 weeks |
| [NCT01686633](https://clinicaltrials.gov/study/NCT01686633) | Phase 3 | Completed | 1040 | FF/VI 200/25 and 100/25 mcg vs FF 100 mcg in moderate to severe persistent asthma |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | Completed | 4233 | 12-month open-label effectiveness study of FF/VI vs usual maintenance therapy in asthma |
| [NCT02301975](https://clinicaltrials.gov/study/NCT02301975) | Phase 3 | Completed | 1526 | Once-daily FF/VI vs twice-daily FP/salmeterol in controlled persistent asthma (non-inferiority) |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Phase 3 | Completed | 905 | Umeclidinium/vilanterol vs tiotropium over 24 weeks in COPD (trough FEV1) |
| [NCT01342913](https://clinicaltrials.gov/study/NCT01342913) | Phase 3 | Completed | 528 | 24-hour lung function of FF/VI once daily vs salmeterol/FP twice daily in COPD |
| [NCT05062304](https://clinicaltrials.gov/study/NCT05062304) | N/A | Completed | 17281 | Real-world replication of the IMPACT trial: once-daily triple vs dual therapy in COPD |
| [NCT04265105](https://clinicaltrials.gov/study/NCT04265105) | Phase 2/3 | Completed | 18 | Pilot superiority trial of as-needed fluticasone-vilanterol in mild asthma (small, underpowered) |

Some other trials were withdrawn with no enrolment (NCT04671355, NCT01435902, NCT02731846), and several are Phase 1 pharmacokinetic studies that provide no efficacy data. One trial of perioperative dual bronchodilators in lung cancer patients with COPD ([NCT04536675](https://clinicaltrials.gov/study/NCT04536675), Phase 3, 204 participants) is still active and not yet reported, and it may not contain vilanterol.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | IMPACT: once-daily single-inhaler triple therapy vs dual therapy in COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL: once-daily triple therapy vs ICS/LABA in COPD |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | Lancet Respir Med | CAPTAIN: FF/UMEC/VI vs FF/VI in inadequately controlled asthma (Phase 3A) |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT post hoc analysis | Am J Respir Crit Care Med | Reduced all-cause mortality with FF/UMEC/VI in COPD (IMPACT) |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network meta-analysis | Adv Ther | Comparative efficacy of FF/UMEC/VI vs other triple and dual therapies in COPD |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic review / meta-analysis | BMC Pulm Med | Umeclidinium/vilanterol vs other bronchodilators in COPD |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Systematic review | Clin Respir J | Fixed-dose umeclidinium/vilanterol in COPD |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohort study | BMJ | Comparison of single-inhaler triple therapies in routine COPD practice |
| [39731707](https://pubmed.ncbi.nlm.nih.gov/39731707/) | 2025 | Cohort study | Adv Ther | Real-world comparison of FF/UMEC/VI and BUD/GLY/FORM in US COPD patients |
| [23232038](https://pubmed.ncbi.nlm.nih.gov/23232038/) | 2013 | Phase 1 study | Pulm Pharmacol Ther | Vilanterol well tolerated, with prolonged bronchodilation in asthma and COPD |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14737P | RELVAR ELLIPTA INHALATION POWDER 200MCG/25MCG | Powder, metered | Not recorded in the data compiled for this report |
| SIN14736P | RELVAR ELLIPTA INHALATION POWDER 100MCG/25MCG | Powder, metered | Not recorded in the data compiled for this report |
| SIN14838P | ANORO ELLIPTA INHALATION POWDER 62.5 MCG/25 MCG | Powder, metered | Not recorded in the data compiled for this report |

All three licences are valid and held by GlaxoSmithKline entities.

## Safety Considerations

**Drug Interactions**: The interaction screening returned 100 interacting drugs. Examples, by level:
- **Moderate**: antidiabetic agents (acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin), clarithromycin, cisapride, dolasetron, and sympathomimetics (diethylpropion, ephedrine, epinephrine).
- **Minor**: corticosteroids (beclomethasone, betamethasone, budesonide, dexamethasone).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs and large pivotal trials (IMPACT, FULFIL, CAPTAIN) support vilanterol-containing regimens in COPD and asthma. The "obstructive lung disease" prediction essentially confirms existing indications rather than identifying a new use. The other predicted indications have no clinical evidence and should stay on Hold, and bronchial neoplasm is at most a research question.

**To proceed, the following is needed:**
- Singapore package insert text, including approved indications, warnings and contraindications
- Detailed mechanism-of-action data
- Confirmation that the Singapore labelled indications match the evidence (COPD and asthma, by product)
- Review of the moderate interactions, especially with other sympathomimetics and clarithromycin, which may need monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

