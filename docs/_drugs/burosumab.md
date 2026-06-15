---
layout: default
title: Burosumab
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Burosumab
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

# Burosumab: From X-linked Hypophosphatemia to Renal Osteodystrophy

## One-Sentence Summary

Burosumab (Crysvita®) is a fully human anti-FGF23 monoclonal antibody approved internationally for X-linked hypophosphatemia (XLH) and tumor-induced osteomalacia (TIO), but not yet registered in Singapore.
The TxGNN model predicts it may be effective for **Renal Osteodystrophy** — a metabolic bone disorder complicating chronic kidney disease — with **0 clinical trials** and **1 review publication** directly supporting this direction.

> ⚠️ **Critical Interpretation Note:** Renal osteodystrophy ranks #1 by TxGNN prediction score (96.93%), but this reflects AI network topology rather than clinical evidence priority. The strongest clinical evidence belongs to **bone remodeling disease** (rank #4, L1), which is backed by 2 completed Phase 3 RCTs and represents burosumab's actual regulatory approval basis. The score ranking should not be read as a clinical readiness ranking.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | X-linked hypophosphatemia (XLH); Tumor-induced osteomalacia (TIO) |
| Predicted New Indication | Renal Osteodystrophy |
| TxGNN Prediction Score | 96.93% |
| Evidence Level | L4 (for renal osteodystrophy) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from local regulatory sources. Based on published information, burosumab is a fully human IgG1 monoclonal antibody that binds to and inhibits fibroblast growth factor 23 (FGF23). In X-linked hypophosphatemia, loss-of-function mutations in the *PHEX* gene cause excess circulating FGF23, which suppresses renal tubular phosphate reabsorption and reduces 1,25-dihydroxyvitamin D₃ synthesis. The result is chronic hypophosphatemia and defective bone mineralization (osteomalacia/rickets). By neutralizing FGF23, burosumab restores phosphate homeostasis and corrects skeletal mineralization — a mechanism that has been validated in two Phase 3 RCTs and underpins its FDA and EMA approvals.

Renal osteodystrophy (ROD) is a complex spectrum of bone pathology arising in chronic kidney disease (CKD), driven by interrelated disturbances: phosphate retention, reduced 1,25(OH)₂D₃ synthesis, secondary hyperparathyroidism, and defective bone mineralization. The FGF23–KLOTHO axis is central to ROD pathophysiology — FGF23 rises early in CKD as the body attempts to compensate for phosphate overload. This draws a mechanistic parallel to XLH, where FGF23 is also the primary driver of mineral dysregulation, and gives TxGNN a plausible topological basis for predicting burosumab efficacy in ROD.

However, this parallel is mechanistically double-edged and clinically hazardous without further study. In XLH, FGF23 is inappropriately elevated and pathological; in CKD, FGF23 elevation is a compensatory response. Blocking FGF23 in the CKD context may paradoxically worsen hyperphosphatemia — a leading driver of vascular calcification and cardiovascular mortality in this population. Until prospective studies directly address this safety-efficacy trade-off, renal osteodystrophy must remain a research question rather than an actionable repurposing target.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for renal osteodystrophy.

---

### Supplementary: Bone Remodeling Disease (Rank #4) — Strongest Evidence Cluster

Although renal osteodystrophy is TxGNN's top-scored prediction, **bone remodeling disease** (score 95.49%, Evidence Level L1) carries by far the strongest clinical evidence, including the pivotal Phase 3 trials that secured burosumab's global regulatory approvals. This section is included to provide a complete picture of where the evidence actually stands.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02526160](https://clinicaltrials.gov/study/NCT02526160) | Phase 3 | Completed | 134 | Pivotal randomized double-blind placebo-controlled trial in adults with XLH. Demonstrated significant serum phosphorus normalization and bone biopsy-confirmed improvement in mineralization lag time — the primary evidence supporting FDA and EMA approval of burosumab |
| [NCT02537431](https://clinicaltrials.gov/study/NCT02537431) | Phase 3 | Completed | 14 | Open-label single-arm trial evaluating burosumab (KRN23) in adults with XLH-associated osteomalacia. Primary endpoint: improvement in osteoid volume/bone volume (OV/BV) on bone biopsy — directly supported the TIO indication approval |
| [NCT03993821](https://clinicaltrials.gov/study/NCT03993821) | Early Phase 1 | Unknown | 1 | Single-patient trial in Cutaneous Skeletal Hypophosphatemia Syndrome (CSHS). Proof-of-concept signal only; status unknown and evidence weight negligible |

**Also identified for Impaired Renal Function (Rank #2):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | NA | Not Yet Recruiting | 65 | ³¹P-MRS spectroscopy study measuring ATP concentration in phosphate diabetes (XLH and acquired causes). Diagnostic/biomarker design — not a burosumab intervention trial, but relevant to phosphate metabolism background in renal disease |

---

## Literature Evidence

### For Renal Osteodystrophy (Rank #1, Primary Prediction)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37927073](https://pubmed.ncbi.nlm.nih.gov/37927073/) | 2024 | Review | Current Pediatric Reviews | Reviews diagnosis and management of hypophosphatasia and XLH in children; highlights diagnostic delays, complex calcium-phosphate pathophysiology, and emerging treatments — does not directly assess burosumab in ROD but provides mechanistic background |

### For Bone Remodeling Disease (Rank #4, Strongest Evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37180412](https://pubmed.ncbi.nlm.nih.gov/37180412/) | 2022 | Narrative Review | Therapeutic Advances in Rare Disease | Comprehensively reviews burosumab benefits versus conventional therapy in adult XLH; covers improvement in bone pain, osteomalacia healing, enthesopathies, fracture repair, and quality of life — strongest review-level evidence for FGF23 blockade in bone disease |
| [37843399](https://pubmed.ncbi.nlm.nih.gov/37843399/) | 2024 | Cohort/Observational | J Clin Endocrinol Metab | Reassuring cardiovascular data in adults with XLH on conventional therapy; contextualizes long-term safety monitoring needs given elevated FGF23 and cardiovascular risk associations |
| [35235937](https://pubmed.ncbi.nlm.nih.gov/35235937/) | 2023 | Review | Hormone Research in Paediatrics | Updates pediatric bone disease treatment landscape including burosumab for XLH and novel agents for osteoporosis and achondroplasia |

### For Impaired Renal Function (Rank #2)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38195892](https://pubmed.ncbi.nlm.nih.gov/38195892/) | 2024 | Case Report | Calcified Tissue International | **Key case:** Successful burosumab treatment in a 61-year-old male with XLH and CKD Stage 3b. Phosphate normalization was achieved despite renal impairment. Establishes proof-of-concept but also highlights that this remains off-label and unstudied in formal trials |
| [32701599](https://pubmed.ncbi.nlm.nih.gov/32701599/) | 2020 | Review/Perspective | Current Opinion in Nephrology and Hypertension | Reviews burosumab mechanism in XLH and discusses FGF23's role in CKD-MBD; explicitly identifies CKD as a candidate population for FGF23 blockade research, with cautions |
| [36382755](https://pubmed.ncbi.nlm.nih.gov/36382755/) | 2022 | Review | Archives of Endocrinology and Metabolism | Reviews FGF23-driven hypophosphatemic disorders (XLH, oncogenic osteomalacia) and treatment advances; provides mechanistic framework linking phosphate regulation to renal function |
| [35103802](https://pubmed.ncbi.nlm.nih.gov/35103802/) | 2022 | Review | Zeitschrift fur Rheumatologie | Reviews tumor localization and management of tumor-induced osteomalacia (TIO) — FGF23-driven phosphate-wasting syndrome directly treated by burosumab; contextualizes FGF23 blockade across different disease etiologies |
| [31905439](https://pubmed.ncbi.nlm.nih.gov/31905439/) | 2019 | Review | Annals of Pediatric Endocrinology & Metabolism | Foundational review of skeletal mineralization mechanisms; explains how calcium and phosphate deficiency impair hydroxyapatite crystal formation — underpins rationale for phosphate restoration therapy |

---

## Singapore Market Information

Burosumab (Crysvita®) is **not registered** with the Health Sciences Authority (HSA) of Singapore. No product licenses are on record, and the drug is currently not commercially available in Singapore through standard channels.

> Internationally, burosumab has received approval from the U.S. FDA (April 2018), the European Medicines Agency (February 2018), and regulators in Japan, Canada, and other jurisdictions — for X-linked hypophosphatemia in adults and pediatric patients aged ≥1 year, and for tumor-induced osteomalacia (TIO) in adults. Singapore patients seeking access would currently require individual compassionate use or special access applications.

---

## Safety Considerations

Please refer to the Crysvita® international prescribing information (FDA label or EMA SmPC) for complete safety information, as no Singapore HSA product labeling is available.

> **Population-specific safety signal for CKD:** The mechanistic rationale for repurposing to renal osteodystrophy identifies a critical safety concern — FGF23 inhibition in CKD may worsen hyperphosphatemia and accelerate vascular calcification. Any clinical investigation in this population must include rigorous serum phosphate monitoring, vascular calcification assessment, and predefined stopping rules.

> **Hypocalcemic Rickets (Rank #9) — Contraindication Signal:** Burosumab should **not** be considered for hypocalcemic rickets (e.g., vitamin D deficiency, VDDR). The mechanistic basis is opposite: blocking FGF23 in a patient without FGF23 excess is not therapeutic and may impair 1,25(OH)₂D₃ synthesis, potentially worsening hypocalcemia. This is flagged as a contraindication signal in the prediction analysis.

---

## Conclusion and Next Steps

### Primary Recommendation (Renal Osteodystrophy, Rank #1)

**Decision: Hold**

**Rationale:**
Despite the highest TxGNN prediction score (96.93%), renal osteodystrophy has only L4 evidence — a single background review with no clinical trials. The mechanistic rationale is theoretically plausible but carries an inherent safety risk of worsening hyperphosphatemia in CKD, making premature advancement inappropriate.

---

### Secondary Recommendation (Bone Remodeling Disease, Rank #4)

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (NCT02526160, NCT02537431) directly demonstrate burosumab efficacy in FGF23-driven bone mineralization disorders — the highest evidence level (L1) in this dataset. This evidence base is the foundation of burosumab's existing global approvals for XLH and TIO, and supports expansion to related FGF23-driven bone remodeling indications.

---

**To proceed, the following is needed:**

- **Singapore HSA registration:** Initiate a submission for the existing XLH/TIO indications as the regulatory foundation; currently no local approval exists
- **MOA documentation (DG002):** Retrieve full mechanism of action data from DrugBank API to strengthen mechanistic analysis sections
- **Safety data (DG001):** Download and parse Crysvita® package insert PDF (from FDA or EMA sources) to populate key warnings, contraindications, and drug interaction data
- **CKD safety study design:** For the renal osteodystrophy research question, develop a dedicated Phase 1/2 protocol with serial serum phosphate, PTH, FGF23, and vascular calcification scoring at minimum 6-month intervals
- **Renal dosing investigation:** Current burosumab dosing is validated only in patients with normal-to-mildly impaired renal function; formal pharmacokinetic studies in CKD Stage 3b–4 patients are required before any expanded use
- **Orphan drug pathway assessment:** Evaluate Singapore's orphan drug incentive framework for any new indication submissions given the rare disease context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

