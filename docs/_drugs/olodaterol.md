---
layout: default
title: Olodaterol
parent: 僅模型預測 (L5)
nav_order: 729
evidence_level: L5
indication_count: 10
---

# Olodaterol
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

# Olodaterol: From COPD Maintenance Bronchodilation to Bronchitis

## One-Sentence Summary

Olodaterol is a long-acting β2-adrenergic agonist (LABA), delivered via the Respimat inhaler and marketed globally (including in fixed-dose combination with tiotropium as Spiolto/Stiolto Respimat) as a once-daily maintenance bronchodilator for chronic obstructive pulmonary disease (COPD). The TxGNN model predicts it may be effective for **Bronchitis**, with **3 clinical trials** and **2 publications** currently associated with this prediction — though the underlying evidence largely reflects olodaterol's already-established COPD/chronic bronchitis use rather than a genuinely new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; internationally indicated as once-daily maintenance bronchodilator therapy for COPD (per literature evidence, e.g. PMID 25773742, 31119643) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L1 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap. Based on the available literature within this evidence pack, olodaterol is a long-acting β2-adrenoceptor agonist (LABA) delivered via the Respimat inhaler, indicated as once-daily maintenance bronchodilator therapy in COPD, and also marketed as a fixed-dose combination with the LAMA tiotropium (Spiolto®/Stiolto® Respimat) for long-term COPD maintenance.

Chronic bronchitis is one of the two classic clinical phenotypes of COPD (alongside emphysema), and airflow obstruction in chronic bronchitis responds to the same β2-agonist-mediated bronchial smooth muscle relaxation that underlies olodaterol's approved COPD use. This is reflected directly in the evidence pack's own rationale: bronchitis is described as "essentially the same core indication as olodaterol's known/original approved use, not an independent new indication" — the drug's largest supporting trial (NCT02850978) explicitly enrolled COPD patients with chronic bronchitis and emphysema phenotypes.

Because of this overlap, the mechanistic plausibility is high, but the "repurposing novelty" is low — this is best understood as confirmatory evidence for an already-related use rather than a genuinely new therapeutic direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A | Completed | 1,335 | Post-marketing surveillance of long-term safety/effectiveness of tiotropium+olodaterol FDC (Spiolto) in Japanese COPD patients (chronic bronchitis, emphysema) in real-world practice |
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A | Completed | 11,316 | Health care resource utilization and clinical outcomes comparing tiotropium/olodaterol vs. fluticasone furoate/umeclidinium/vilanterol in COPD maintenance therapy |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completed | 22,155 | Drug utilization study of aclidinium bromide (a different LAMA, not olodaterol) in COPD patients — included only via disease-category overlap; low direct relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Review | American Journal of Health-System Pharmacy | Reviews pharmacology, pharmacokinetics, efficacy, and safety of once-daily LABA olodaterol for COPD |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline/Review | Basic & Clinical Pharmacology & Toxicology | Finnish national COPD guideline covering diagnosis, assessment, and pharmacotherapy of stable COPD |

---

## Singapore Market Information

Olodaterol is currently not marketed in Singapore — no HSA registration records exist (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Olodaterol has a well-established global safety and efficacy profile as a COPD bronchodilator, and the "bronchitis" prediction is mechanistically sound but substantially overlaps with its existing approved use rather than representing a novel therapeutic direction — this tempers the strategic value of pursuing it as a distinct repurposing candidate. The drug is also not currently registered in Singapore, meaning any pathway forward requires a market entry assessment in addition to clinical evidence review.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert data (warnings, contraindications) — currently a **Blocking** data gap preventing S1 safety pre-screening
- DrugBank-sourced mechanism of action detail to confirm receptor-level rationale
- Clarification of whether "bronchitis" as a TxGNN-labeled indication is clinically distinct from olodaterol's existing COPD/chronic bronchitis approval, to determine true repurposing novelty
- Singapore market entry/registration strategy, since the drug currently has no local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

