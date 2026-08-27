---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 583
evidence_level: L5
indication_count: 10
---

# Letrozole
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

# Letrozole: From ER-Positive Breast Cancer to Female Breast Carcinoma *(Confirmatory Signal)*

## One-Sentence Summary

Letrozole is an aromatase inhibitor whose established real-world use — per the evidence pack's own mechanistic notes — is hormone-receptor (ER)-positive breast cancer in postmenopausal women; a formal original-indication record could not be pulled from Singapore's registry or DrugBank in this evidence pack (data gap). The TxGNN model's top-ranked prediction, **Female Breast Carcinoma** (99.98% confidence), is backed by an unusually large evidence base — **50 clinical trials** and **20 publications** — but this evidence overlaps almost entirely with letrozole's already-approved use rather than pointing to a genuinely new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Singapore licensing records (drug unlicensed locally) or DrugBank MOA field — both flagged as data gaps (DG001/DG002). The evidence pack's own analysis identifies letrozole's established use as hormone-receptor (ER)-positive breast cancer in postmenopausal women. |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text was not returned for this evidence pack (data gap DG002). Based on the mechanistic reasoning captured elsewhere in this same evidence pack, letrozole is a third-generation, non-steroidal **aromatase inhibitor**: it blocks the enzyme that converts adrenal androgens into estrogen, cutting off the estrogen supply that drives growth in estrogen-receptor (ER)-positive breast tumors.

The relationship between the "original" and "predicted" indication here is unusually direct — arguably too direct to count as repurposing. The evidence pack's own rationale for this candidate states that "Female Breast Carcinoma" is a broadly-labeled variant of the same disease letrozole already treats, and that the underlying trial and literature base is a near-total overlap with its known, approved use (e.g., PALOMA-2, MONALEESA-2/3, BIG 1-98). In other words, this is a **confirmatory finding, not a novel repurposing hypothesis**: the knowledge graph is correctly recognizing letrozole's core pharmacology, but the practical "so what" for a repurposing program is limited.

**Data-quality note:** Two other high-scoring predictions in this pack deserve caution rather than action. "Estrogen-receptor negative breast cancer" (rank 3, score 99.75%) is flagged in the pack's own analysis as a likely **knowledge-graph mislabeling** — the cited trials (e.g., PALOMA, MONALEESA) actually enrolled ER-*positive* patients, which contradicts letrozole's mechanism (it has no rationale in ER-negative disease). This should be treated as a data-linkage artifact, not a signal, and is a candidate for manual review of the underlying KG edge. By contrast, rank 6, "hormone-resistant breast carcinoma" (L2, "Research Question"), is a more genuinely interesting angle — it reflects real combination strategies (with CDK4/6 or mTOR inhibitors) used to overcome acquired endocrine resistance, though this is a combination-therapy strategy rather than a standalone new indication for letrozole itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | Completed | 131 | Expanded access to palbociclib + letrozole for HR+/HER2- postmenopausal advanced breast cancer in Latin America |
| [NCT02338310](https://clinicaltrials.gov/study/NCT02338310) | Phase 3 | Active, not recruiting | 4,486 | Large perioperative aromatase-inhibitor trial (POETIC) evaluating whether perioperative AI therapy improves outcomes and whether Ki67 change predicts recurrence |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | Completed | 666 | PALOMA-2 pivotal trial: palbociclib + letrozole vs. placebo + letrozole as first-line therapy for ER+/HER2- advanced breast cancer |
| [NCT05163106](https://clinicaltrials.gov/study/NCT05163106) | Phase 2 | Completed | 85 | NEOLETRIB: presurgical ribociclib + letrozole in locally advanced (stage III) breast cancer |
| [NCT00171704](https://clinicaltrials.gov/study/NCT00171704) | Phase 3 | Completed | 263 | Letrozole vs. tamoxifen — effects on bone and lipid metabolism in postmenopausal ER+ early breast cancer |
| [NCT00754845](https://clinicaltrials.gov/study/NCT00754845) | Phase 3 | Completed | 1,918 | Extended adjuvant letrozole vs. placebo after prior aromatase-inhibitor/tamoxifen therapy |
| [NCT02296801](https://clinicaltrials.gov/study/NCT02296801) | Phase 2 | Completed | 307 | Palbociclib + letrozole as neoadjuvant therapy in ER+ primary breast cancer, evaluating biological and clinical effects |
| [NCT00171340](https://clinicaltrials.gov/study/NCT00171340) | Phase 3 | Completed | 1,065 | Zoledronic acid for prevention of letrozole-associated bone loss in the adjuvant setting |
| [NCT00369850](https://clinicaltrials.gov/study/NCT00369850) | Phase 3 | Completed | 458 | IBCSG-1-98 substudy assessing bone density/bone loss under adjuvant letrozole |
| [NCT01872260](https://clinicaltrials.gov/study/NCT01872260) | Phase 1/2 | Active, not recruiting | 255 | Ribociclib + alpelisib + letrozole combination regimens in advanced ER+ breast cancer |

*50 clinical trials were retrieved in total for this indication; the table above lists the 10 most clinically informative.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT | Breast Cancer Res Treat | Final overall-survival analysis of PALOMA-1/TRIO-18: palbociclib + letrozole vs. letrozole alone as first-line therapy for ER+/HER2- advanced breast cancer |
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | New England Journal of Medicine | BIG 1-98: letrozole vs. tamoxifen as adjuvant therapy for postmenopausal ER+ early breast cancer |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | RCT | Comput Math Methods Med | Efficacy, safety, and prognosis of letrozole alone vs. sequential tamoxifen→letrozole for breast carcinoma |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sciences | Comprehensive review of letrozole pharmacology, toxicity, and potential therapeutic effects |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Review of letrozole pharmacodynamics/pharmacokinetics and clinical efficacy/safety |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast (Edinburgh) | Development of letrozole and its use in advanced and neoadjuvant breast cancer |
| [17696797](https://pubmed.ncbi.nlm.nih.gov/17696797/) | 2007 | Review | Expert Opin Pharmacother | Letrozole's present and future role in breast cancer treatment |
| [27235140](https://pubmed.ncbi.nlm.nih.gov/27235140/) | 2016 | Preclinical | Med Oncol | Letrozole-induced changes in carcinoma-associated fibroblasts and their influence on endocrine-therapy efficacy |
| [15328175](https://pubmed.ncbi.nlm.nih.gov/15328175/) | 2004 | Preclinical | Clin Cancer Res | Comparison of tamoxifen vs. letrozole effects on hormones and bone in a preclinical tumor model |
| [26774555](https://pubmed.ncbi.nlm.nih.gov/26774555/) | 2016 | Phase I trial | Clin Breast Cancer | Panobinostat + letrozole in postmenopausal metastatic breast cancer |

*20 publications were retrieved in total; the table above prioritizes RCTs and reviews.*

---

## Singapore Market Information

Letrozole currently holds **no marketing authorization in Singapore** — market status is "Not Marketed" with **0 registered licenses** in this evidence pack. No product name, dosage form, or approved-indication text is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug-drug interaction data were all returned as data gaps in this evidence pack — DDI query status: not found, 0 interactions on record.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The top-ranked prediction ("Female Breast Carcinoma," L1, 99.98%) is backed by an exceptionally deep evidence base (50 trials including multiple completed Phase 3 RCTs; 20 publications including landmark trials such as BIG 1-98 and PALOMA-2), meeting the bar for guarded proceeding on evidentiary grounds alone.
- However, this is **not a novel repurposing signal** — it recapitulates letrozole's already-established indication. The genuine value of this evidence pack lies less in acting on rank 1, and more in (a) closing the regulatory/MOA data gaps needed for any Singapore market activity, and (b) treating lower-ranked, lower-evidence candidates (e.g., rank 6, "hormone-resistant breast carcinoma," L2) as true research questions rather than action-ready findings.
- Rank 3 ("estrogen-receptor negative breast cancer") should be treated as a likely knowledge-graph data-quality issue, not a pharmacological signal, since it contradicts letrozole's mechanism and its cited trials actually enrolled ER-positive patients.

**To proceed, the following is needed:**
- Original Singapore/HSA-equivalent product labeling (warnings, contraindications) to close data gap DG001 — currently blocking any formal safety pre-assessment (S1).
- Confirmed DrugBank/manufacturer mechanism-of-action text to close data gap DG002.
- Manual review of the TxGNN knowledge-graph edge underlying the "ER-negative breast cancer" prediction (rank 3) to determine whether it reflects a labeling/mapping error.
- If pursuing the endocrine-resistance angle (rank 6) as a distinct research question, a targeted evidence review of letrozole-based combination regimens (CDK4/6i, mTOR inhibitors) in confirmed endocrine-resistant populations, rather than treating it as supporting evidence for the rank-1 indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

