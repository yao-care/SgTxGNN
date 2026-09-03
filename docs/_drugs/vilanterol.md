---
layout: default
title: Vilanterol
parent: 僅模型預測 (L5)
nav_order: 1056
evidence_level: L5
indication_count: 10
---

# Vilanterol
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

# Vilanterol: From Combination Bronchodilator Therapy to Obstructive Lung Disease

## One-Sentence Summary

> Vilanterol is a long-acting beta2-agonist (LABA) that, per the underlying trial evidence, is only documented as a component of fixed-dose combination inhalers (Breo/Relvar Ellipta, Anoro Ellipta, Trelegy Ellipta) for COPD and asthma — no standalone indication is recorded in this evidence pack.
> The TxGNN model's top prediction is **Obstructive Lung Disease**, supported by an unusually large body of evidence: **50 clinical trials** and **20 publications**, including multiple Phase 3 RCTs and the landmark IMPACT trial (NCT05062304 / PMID 29668352).
> Because this predicted indication substantially overlaps with vilanterol's already-established combination-product use, this candidate should be read as **confirmatory evidence strengthening** rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not independently filed — per trial evidence, vilanterol is the LABA component of combination inhalers (FF/VI, UMEC/VI, FF/UMEC/VI) for COPD and asthma; no monotherapy indication is documented in this evidence pack |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for vilanterol in this evidence pack (DG002). Based on the clinical trial descriptions collected, vilanterol is a long-acting β2-adrenoceptor agonist (LABA) formulated exclusively in fixed-dose combinations — with the inhaled corticosteroid fluticasone furoate (FF/VI, "Breo/Relvar Ellipta"), with the LAMA umeclidinium (UMEC/VI, "Anoro Ellipta"), or as triple therapy (FF/UMEC/VI, "Trelegy Ellipta"). Its bronchodilator mechanism (smooth-muscle relaxation via β2-receptor activation) is pharmacologically well suited to airflow-limiting disease.

The predicted indication, "obstructive lung disease," is not a distant new disease area — it is the broad disease category that already encompasses COPD and asthma, the conditions these combination products are developed and tested for. This means the TxGNN signal here largely reflects and reinforces existing, well-established clinical use rather than identifying an unexpected new application. That said, the sheer volume and quality of supporting evidence (large completed Phase 3/4 RCTs, including the 17,281-patient IMPACT trial) makes this one of the best-substantiated predictions this pipeline can produce, and it validates the underlying KG/DL methodology even if it is not "novel" in the strict repurposing sense.

Because vilanterol has no standalone regulatory record here and is not currently marketed in Singapore, any practical use of this evidence would need to route through one of its approved combination products rather than vilanterol monotherapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01376245](https://clinicaltrials.gov/study/NCT01376245) | Phase 3 | Completed | 646 | FF/VI vs. placebo over 24 weeks in Asian-ancestry COPD patients |
| [NCT02105974](https://clinicaltrials.gov/study/NCT02105974) | Phase 3 | Completed | 1621 | FF/VI 100/25mcg vs. VI 25mcg alone — isolates vilanterol's contribution to lung function in COPD |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Phase 3 | Completed | 905 | UMEC/VI vs. tiotropium 18mcg over 24 weeks in COPD, spirometric (trough FEV1) endpoint |
| [NCT01316900](https://clinicaltrials.gov/study/NCT01316900) | Phase 3 | Completed | 846 | UMEC/VI vs. VI alone vs. tiotropium over 24 weeks in COPD |
| [NCT02257385](https://clinicaltrials.gov/study/NCT02257385) | Phase 3 | Completed | 967 | UMEC/VI vs. indacaterol + tiotropium in moderate-to-very-severe COPD |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | Completed | 1811 | FF/UMEC/VI once daily vs. budesonide/formoterol twice daily, 24-week (52-week extension) COPD trial |
| [NCT02729051](https://clinicaltrials.gov/study/NCT02729051) | Phase 3B | Completed | 1055 | "Closed" triple therapy (FF/UMEC/VI) vs. "open" triple (FF/VI + UMEC) on lung function in COPD |
| [NCT03474081](https://clinicaltrials.gov/study/NCT03474081) | Phase 4 | Completed | 800 | Single-inhaler triple therapy (FF/UMEC/VI) vs. tiotropium monotherapy on lung function/symptoms in COPD |
| [NCT05062304](https://clinicaltrials.gov/study/NCT05062304) | N/A (real-world replication) | Completed | 17281 | Real-world replication of the IMPACT RCT — once-daily single-inhaler triple vs. dual therapy in COPD |
| [NCT01498679](https://clinicaltrials.gov/study/NCT01498679) | Phase 3 | Completed | 311 | FF/VI vs. placebo, 12 weeks, in Asian-ancestry adolescents/adults with asthma |

*40 additional trials (Phase 1–4, spanning COPD and asthma) are available in the underlying evidence pack but omitted here for brevity.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | IMPACT trial — once-daily single-inhaler triple therapy vs. dual therapy in COPD |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT (secondary analysis) | Am J Respir Crit Care Med | FF/UMEC/VI reduces all-cause mortality vs. UMEC/VI in COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL trial — once-daily triple therapy vs. dual ICS/LABA in COPD |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT (Phase 3A) | Lancet Respir Med | CAPTAIN trial — FF/UMEC/VI vs. FF/VI in inadequately controlled asthma |
| [31281061](https://pubmed.ncbi.nlm.nih.gov/31281061/) | 2019 | RCT sub-analysis | Lancet Respir Med | IMPACT trial — blood eosinophils predict treatment response to triple vs. dual therapy |
| [32299860](https://pubmed.ncbi.nlm.nih.gov/32299860/) | 2020 | RCT sub-analysis | Eur Respir J | IMPACT trial — effect of exacerbation history on outcomes |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network meta-analysis | Advances in Therapy | FF/UMEC/VI vs. other triple/dual therapies across RCTs in COPD |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Observational (new-user cohort) | BMJ | Real-world comparative effectiveness/safety of single-inhaler triple therapies in COPD |
| [39731707](https://pubmed.ncbi.nlm.nih.gov/39731707/) | 2025 | Observational | Advances in Therapy | Comparative effectiveness of FF/UMEC/VI vs. BUD/GLY/FORM in US COPD patients |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic review & meta-analysis | BMC Pulmonary Medicine | UMEC/VI vs. other bronchodilators in COPD management |

*10 additional publications (pharmacology reviews, PK/safety studies) are available in the underlying evidence pack but omitted here for brevity.*

---

## Singapore Market Information

Vilanterol currently has **no registered licenses in Singapore** (market status: not marketed, 0 registrations recorded). Any clinical use would depend on registration of one of its combination products (e.g., Trelegy Ellipta, Anoro Ellipta, Relvar Ellipta) rather than vilanterol as a standalone entity.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (source: TFDA label parsing — flagged as a **blocking** data gap, DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The efficacy evidence base is exceptionally strong (L1, 50 trials including multiple large completed Phase 3 RCTs and the IMPACT trial), but the predicted "obstructive lung disease" indication largely overlaps with vilanterol's existing combination-product use rather than representing a novel repurposing opportunity. Critically, TFDA label safety data is missing (a blocking gap that prevents S1 safety screening), and the drug has no current Singapore registration.

**To proceed, the following is needed:**
- TFDA/product label warnings, contraindications, and DDI data (DG001 — blocking)
- Mechanism-of-action documentation from DrugBank (DG002)
- Clarification of Singapore regulatory pathway, since vilanterol has zero current local registrations
- A review specifically distinguishing which fraction of the "obstructive lung disease" evidence reflects genuinely new signal versus reconfirmation of already-approved combination-product indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

