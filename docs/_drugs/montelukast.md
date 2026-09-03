---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 679
evidence_level: L5
indication_count: 10
---

# Montelukast
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

# Montelukast: From Asthma to Bronchitis

## One-Sentence Summary

Montelukast is a cysteinyl leukotriene receptor 1 (CysLT1) antagonist originally established for the maintenance treatment of **asthma**. The TxGNN model separately flags **Bronchitis** (a broad node spanning viral bronchiolitis, bronchiolitis obliterans syndrome (BOS), and eosinophilic bronchitis) as a candidate repurposing target, supported by **23 clinical trials** and **20 publications**. Evidence quality is uneven across the sub-conditions bundled under this label, so this is best framed as an open research question rather than a ready-to-act signal.

> **Note on this evidence pack:** the model's rank-3 hit ("asthma", score 99.5%) is Montelukast's known, already-approved indication — not a new use — and functions here as an internal validation check that the model correctly recovers known drug–disease links. Rank-2 ("atopic eczema") has already been tested in multiple Phase 4 RCTs and systematic reviews with a **negative** result (no significant benefit over placebo), so it is excluded from further consideration below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (established leukotriene receptor antagonist; formal Taiwan/Singapore label text not available in this dataset) |
| Predicted New Indication | Bronchitis (bundles viral bronchiolitis, bronchiolitis obliterans syndrome, and eosinophilic bronchitis) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available from DrugBank for this evidence pack. Based on well-established pharmacology, Montelukast is a selective, orally active **CysLT1 receptor antagonist** — it blocks cysteinyl leukotriene–mediated bronchoconstriction, mucus secretion, and eosinophilic airway inflammation. This mechanism is the basis of its approved use in asthma and allergic rhinitis.

The "bronchitis" prediction is mechanistically plausible for a subset of conditions where leukotriene-driven eosinophilic inflammation plays a documented role: **bronchiolitis obliterans syndrome (BOS)** after lung or hematopoietic stem cell transplantation (a form of small-airway fibro-inflammatory injury), **non-asthmatic eosinophilic bronchitis (NAEB)**, and **RSV-induced viral bronchiolitis** in infants (where cys-LT levels rise during acute infection). These are pathologically distinct entities that happen to share a coarse ontology label in this dataset.

Because the disease node mixes conditions with very different pathophysiology (autoimmune/fibrotic BOS vs. viral bronchiolitis vs. eosinophilic bronchitis vs. neutrophilic chronic bronchitis), the aggregate evidence level (L2) understates how strong the signal is for BOS specifically — where dedicated Phase 2 and Phase 4 RCTs exist — and overstates it for sub-conditions with only mechanistic or observational support. We recommend the disease node be split before final evidence grading.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | Completed | 1,125 | Large multicenter RCT of montelukast (MK-0476) vs. placebo for respiratory symptoms of RSV-induced bronchiolitis in children 3–24 months |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | N/A (RCT) | Completed | 51 | Double-blind, placebo-controlled trial of montelukast in acute RSV bronchiolitis; evaluated clinical progress and cytokine profiles |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A (RCT) | Completed | 141 | Randomized, double-blind, placebo-controlled trial of daily montelukast on duration of acute illness in first-time bronchiolitis |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | Randomized, double-blind, placebo-controlled trial of montelukast to slow progression of BOS after lung transplantation |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Prospective study of montelukast for BOS following allogeneic/autologous stem cell transplant |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | Completed | 36 | Fluticasone + azithromycin + montelukast (FAM) combination for BOS after stem cell transplant (single-arm; montelukast contribution not isolated) |
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Phase 4 | Unknown | 100 | Effectiveness of montelukast in treatment/prevention of recurrent obstructive bronchitis in children aged 1–7 |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completed | 146 | Montelukast for acute bronchiolitis and post-bronchiolitis viral-induced wheezing in infants 3–12 months |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | Add-on montelukast to inhaled budesonide for non-asthmatic eosinophilic bronchitis (cough severity, airway eosinophilia) |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Phase 4 | Completed | 49 | Montelukast vs. prednisolone response in chronic cough, using feNO to differentiate underlying eosinophilic disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | RCT | Chinese Medical Journal | Add-on montelukast to budesonide improved life quality, airway eosinophilia, and cough remission in NAEB |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Phase 2 single-arm trial | Biol Blood Marrow Transplant | FAM (fluticasone/azithromycin/montelukast) with brief steroid pulse tested to avert progression of new-onset BOS post-HCT |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Phase 2 trial | Transplantation and Cellular Therapy | Prospective trial of montelukast for BOS after hematopoietic cell transplant; investigated pathogenesis |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Cohort/Comparative | Respiratory Research | Budesonide/formoterol + montelukast + N-acetylcysteine evaluated as BOS treatment after allogeneic HSCT |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Review | Ther Adv Respir Dis | Reviews therapeutic potential and possible mechanisms of montelukast in BOS after lung/stem cell transplant |
| [20442434](https://pubmed.ncbi.nlm.nih.gov/20442434/) | 2010 | Mechanistic (animal) | Am J Respir Crit Care Med | Montelukast during primary RSV infection prevented airway hyperresponsiveness and inflammation on reinfection |
| [20171653](https://pubmed.ncbi.nlm.nih.gov/20171653/) | 2010 | RCT | The Journal of Pediatrics | Randomized intervention of montelukast post-RSV bronchiolitis; effect on eosinophil degranulation and recurrent wheeze |
| [22819521](https://pubmed.ncbi.nlm.nih.gov/22819521/) | 2012 | Pilot study | Respiratory Medicine | Add-on montelukast vs. double-dose budesonide in non-asthmatic eosinophilic bronchitis |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | General overview of bronchiolitis management in infants (background evidence, not montelukast-specific) |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Animal study | J Cardiothoracic Surgery | LTB4 and montelukast roles investigated in a rat model of transplantation-related bronchiolitis obliterans |

---

## Singapore Market Information

Montelukast currently has **no registered license and is not marketed** in Singapore under this dataset (`market_status: 未上市`, 0 total licenses). No product-level authorization details are available to tabulate.

---

## Safety Considerations

No structured warnings, contraindications, or drug–drug interaction data were returned for Montelukast in this evidence pack (DDI query: not found).

For context, several of the literature items surfaced during evidence collection for other predicted indications (asthma/COPD nodes) reference the FDA boxed warning on **neuropsychiatric adverse events** (e.g., agitation, sleep disturbance, suicidal ideation) issued for montelukast in 2020, based on systematic reviews and nationwide cohort studies. This is a known, labeled class-level safety signal for the drug generally and should be factored into any repurposing risk assessment, even though it was not captured in the structured `safety` fields of this pack.

Please refer to the official package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The "bronchitis" node aggregates pathologically distinct conditions with uneven evidence — dedicated Phase 2/4 RCTs support montelukast in bronchiolitis obliterans syndrome and RSV-related bronchiolitis, but the aggregate L2 rating does not reflect this heterogeneity, and no data confirm feasibility for the Singapore market (drug is currently unregistered).

**To proceed, the following is needed:**
- Split the "bronchitis" disease node into its clinically distinct sub-conditions (BOS, viral bronchiolitis, NAEB) and re-score evidence per sub-condition
- Obtain Montelukast's formal mechanism-of-action and labeled warnings/contraindications from DrugBank/regulatory sources
- Confirm HSA registration pathway and feasibility, since the drug is currently not marketed in Singapore
- Assess the FDA neuropsychiatric boxed warning against the target populations (children, transplant patients) for the sub-indication ultimately pursued

*This report is for research reference only and does not constitute medical advice. Any repurposing candidate requires clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

