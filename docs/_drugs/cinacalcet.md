---
layout: default
title: Cinacalcet
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Cinacalcet
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

# Cinacalcet: From Secondary Hyperparathyroidism to Multiple Endocrine Neoplasia

> ⚠️ **Research Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.

---

## One-Sentence Summary

Cinacalcet is a calcimimetic agent approved for managing secondary hyperparathyroidism (SHPT) in chronic kidney disease (CKD) patients on dialysis and hypercalcemia associated with parathyroid carcinoma.
The TxGNN model identified **10 potential new indications** across a multi-indication evaluation (candidate ID: TW-DB01012-multi); the most clinically actionable prediction is **Multiple Endocrine Neoplasia (MEN)**, supported by **3 clinical trials** (including 1 completed Phase 3) and **19 publications**.
Among all predicted indications, MEN reaches Evidence Level L2, warranting a "Proceed with Guardrails" recommendation, while the remaining 9 predictions are currently at L4–L5 with insufficient evidence to advance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Secondary hyperparathyroidism (CKD/hemodialysis patients); hypercalcemia in parathyroid carcinoma |
| Featured Predicted Indication | Multiple Endocrine Neoplasia (MEN) — highest-evidence prediction |
| TxGNN Prediction Score (MEN) | 93.73% (Rank #4 of all predictions) |
| Evidence Level | L2 (1 completed Phase 3 RCT in MEN1/MEN2A-associated primary HPT) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (for MEN); Hold (for all other predictions) |

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------------|---------------|----------------|
| 1 | Nephrogenic syndrome of inappropriate antidiuresis | 98.48% | L5 | Hold |
| 2 | Common cold | 95.39% | L5 | Hold |
| 3 | Female breast carcinoma | 94.23% | L4 | Research Question |
| **4** | **Multiple endocrine neoplasia** | **93.73%** | **L2** | **Proceed with Guardrails** |
| 5 | Headache disorder | 93.08% | L5 | Hold |
| 6 | Trigeminal autonomic cephalalgia | 92.16% | L5 | Hold |
| 7 | Hypertrichosis | 91.66% | L5 | Hold |
| 8 | Subarachnoid hemorrhage | 91.39% | L5 | Hold |
| 9 | Pulmonary hypertension | 91.21% | L4 | Hold |
| 10 | Familial combined hyperlipidemia (obsolete) | 90.80% | L5 | Hold |

---

## Why is the MEN Prediction Reasonable?

Cinacalcet acts as a **positive allosteric modulator of the calcium-sensing receptor (CaSR)** expressed on parathyroid chief cells. By increasing the receptor's sensitivity to extracellular calcium, it shifts the set-point for PTH secretion downward — meaning the parathyroid glands are "tricked" into secreting less PTH even at the same circulating calcium level. This mechanism is operative regardless of whether excess PTH secretion arises from CKD-driven SHPT or from genetically dysregulated parathyroid tissue.

Multiple Endocrine Neoplasia Type 1 (MEN1) is caused by germline inactivation of the *MEN1* tumour suppressor gene, and **primary hyperparathyroidism (PHPT)** is its most frequent and earliest manifestation — occurring in approximately 95% of MEN1 patients. Because MEN1-associated PHPT involves multiglandular parathyroid proliferation with high post-surgical recurrence rates, long-term medical management becomes particularly relevant. Cinacalcet's CaSR-mediated PTH suppression directly addresses the central pathophysiology (unregulated PTH hypersecretion and hypercalcaemia), making mechanistic extrapolation from its approved SHPT/parathyroid carcinoma indications highly logical.

Independent cohort studies from Italy (PMID 24285106; PMID 26224587), the US (PMID 20585352), and a completed Phase 3 trial (NCT00325104, n=25) have all demonstrated that cinacalcet normalises or substantially reduces serum calcium in MEN1 patients who are poor surgical candidates or who have recurrent disease. A French multicentre study further extended this to paediatric off-label use (PMID 36090548). While cinacalcet does not shrink parathyroid tumours and is therefore not curative, its established tolerability and mechanistic precision position it as a viable long-term bridge therapy or surgical alternative in this syndrome.

---

## Clinical Trial Evidence (MEN Indication)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00325104](https://clinicaltrials.gov/study/NCT00325104) | Phase 3 | Completed | 25 | Direct evaluation of cinacalcet in familial primary HPT associated with MEN1 and MEN2A — the highest-grade direct evidence for this repurposing indication |
| [NCT03123406](https://clinicaltrials.gov/study/NCT03123406) | Phase 4 | Completed | 750 | Large real-world Phase 4 study (n=750) of cinacalcet in CKD/hemodialysis SHPT patients; provides robust safety and iPTH/calcium/phosphorus control data applicable to HPT in general |
| [NCT04637360](https://clinicaltrials.gov/study/NCT04637360) | NA | Completed | 40 | Observational study of bone turnover markers and bone density under cinacalcet in dialysis patients — provides background on skeletal effects but low direct relevance to MEN |

---

## Literature Evidence (MEN Indication)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [24285106](https://pubmed.ncbi.nlm.nih.gov/24285106/) | 2013 | Cohort | Minerva Endocrinologica | Cinacalcet hydrochloride modified therapeutic strategy in 2 MEN1 PHPT patients, demonstrating calcium normalisation |
| [26224587](https://pubmed.ncbi.nlm.nih.gov/26224587/) | 2016 | Cohort | Endocrine | Prospective cohort confirming cinacalcet as medical alternative for MEN1-associated PHPT in patients ineligible for or refusing surgery |
| [22577108](https://pubmed.ncbi.nlm.nih.gov/22577108/) | 2012 | Cohort | European Journal of Endocrinology | Evaluated cinacalcet efficacy in MEN1 vs sporadic PHPT; also assessed impact of CaSR Arg990Gly polymorphism on treatment response |
| [35407574](https://pubmed.ncbi.nlm.nih.gov/35407574/) | 2022 | Systematic review | Journal of Clinical Medicine | Long-term follow-up of PHPT management in MEN1 at a single centre; contextualises cinacalcet within the broader MEN1 treatment algorithm |
| [20585352](https://pubmed.ncbi.nlm.nih.gov/20585352/) | 2010 | Prospective audit | International Journal of Endocrinology | Prospective 8-patient audit of cinacalcet in MEN1-associated HPT; supports its use as a medical alternative in complex patients with high surgical recurrence |
| [36090548](https://pubmed.ncbi.nlm.nih.gov/36090548/) | 2022 | Multicenter cohort | Frontiers in Pediatrics | French multicentre experience of off-label cinacalcet in paediatric PHPT; identifies risks (hypocalcaemia, QT prolongation) and dosing challenges in younger patients |
| [22104762](https://pubmed.ncbi.nlm.nih.gov/22104762/) | 2012 | Review | Journal of Endocrinological Investigation | Comprehensive review of cinacalcet in PHPT, including MEN1 patients, mild-to-moderate PHPT, and parathyroid carcinoma |
| [30736110](https://pubmed.ncbi.nlm.nih.gov/30736110/) | 2012 | Review | Expert Review of Endocrinology & Metabolism | Expert review covering cinacalcet as the primary non-surgical option in PHPT patients ineligible for or with failed parathyroidectomy, including MEN1 |
| [37893182](https://pubmed.ncbi.nlm.nih.gov/37893182/) | 2023 | Review | Biomedicines | Narrative review of paediatric parathyroid neuroendocrine neoplasia and PHPT (2020–2023); contextualises cinacalcet use in younger MEN populations |
| [37934711](https://pubmed.ncbi.nlm.nih.gov/37934711/) | 2023 | Case report | Clinical Nuclear Medicine | MEN1 patient on cinacalcet after total parathyroidectomy with autotransplantation, evaluated with 18F-fluorocholine PET/CT for recurrent hyperfunctioning tissue |

---

## Mechanistic Notes on Other Selected Predictions

### Female Breast Carcinoma (Rank 3 — Research Question, L4)
CaSR is highly expressed on breast epithelial cells and shows differential expression across breast cancer subtypes. Its activation suppresses PTHrP (parathyroid hormone-related protein) secretion from tumour cells, which theoretically reduces bone metastasis promotion. PMID 38780484 (2024, database analysis + experimental) identified CaSR as a potential biomarker in metastatic breast cancer. However, no clinical trial or study has directly tested cinacalcet as a breast cancer treatment — this remains an indirect mechanistic inference requiring dedicated preclinical investigation before clinical translation.

### Pulmonary Hypertension (Rank 9 — Hold, L4)
CaSR is expressed on pulmonary vascular smooth muscle cells and may modulate vascular tone. In CKD patients, elevated PTH promotes vascular calcification and may indirectly increase pulmonary vascular resistance. Cinacalcet's reduction of PTH and FGF23 could theoretically confer indirect cardiovascular protection (PMID 25498383). However, all available literature is mechanistic background research with no clinical data in PAH patients, and applicability to idiopathic pulmonary arterial hypertension is entirely unestablished.

### NSIAD, Common Cold, Headache, TAC, Hypertrichosis, Subarachnoid Haemorrhage, Familial Hyperlipidaemia (Ranks 1, 2, 5–8, 10 — Hold, L5)
These predictions lack any supporting clinical or preclinical evidence, and for most (common cold, hypertrichosis, familial hyperlipidaemia), no biologically plausible mechanistic link has been established. The TxGNN high scores likely reflect indirect knowledge graph associations or model noise. None are recommended for further evaluation at this stage.

---

## Singapore Market Information

Cinacalcet is **not registered in Singapore**. No licences, approved indications, or dosage forms are on record with the Health Sciences Authority (HSA).

| Item | Details |
|------|---------|
| HSA Registration Status | Not registered |
| Number of Authorisations | 0 |
| Available Dosage Forms | None on record |

> **For reference**, cinacalcet (Sensipar®/Mimpara®) is commercially available and approved in the US (FDA), EU (EMA), Japan (PMDA), and multiple other jurisdictions for SHPT in CKD-5D and hypercalcaemia in parathyroid carcinoma. Regulatory filing would be required before any use in Singapore.

---

## Safety Considerations

Detailed package insert warnings and contraindications for Singapore are not yet available (data gap). Drug interaction data was not retrieved from the query.

Please refer to the originator package insert (Sensipar®/Mimpara®) for complete safety information, including:
- Risk of hypocalcaemia (monitor corrected serum calcium)
- QT-interval prolongation risk (particularly relevant for paediatric populations — PMID 36090548)
- CYP3A4/CYP2D6 drug interactions (cinacalcet is a strong CYP2D6 inhibitor)
- Seizure risk in patients with history of seizure disorders
- Adynamic bone disease risk with over-suppression of PTH

---

## Conclusion and Next Steps

### Decision: Proceed with Guardrails *(for Multiple Endocrine Neoplasia)*

**Rationale:**
Cinacalcet's mechanism of action — positive allosteric modulation of CaSR to suppress PTH secretion — directly addresses the primary pathophysiology of MEN1-associated primary hyperparathyroidism. A completed Phase 3 trial (NCT00325104) and multiple independent cohort studies establish clinical proof-of-concept, and off-label use is already documented in clinical practice. Evidence Level L2 is sufficient to justify a structured evaluation for formalised repurposing.

**To proceed, the following is needed:**

- **Obtain full package insert (TFDA/FDA/EMA SmPC)** to complete safety profiling — this is currently the blocking data gap (DG001)
- **Confirm MOA data from DrugBank API** (DG002) to strengthen mechanistic documentation
- **HSA regulatory pathway assessment**: determine whether a new indication application or off-label use protocol is appropriate given Singapore's market absence
- **Design a prospective registry or cohort study** for MEN1 patients in Singapore/Asia-Pacific to generate region-specific pharmacokinetic and efficacy data
- **Paediatric safety protocol**: given the off-label paediatric use evidence and unique QT/hypocalcaemia risks, a dedicated monitoring plan for younger patients is essential
- **Clarify "curative vs. palliative" positioning**: cinacalcet controls biochemistry but does not cure MEN1; patient selection criteria (surgical candidates vs. non-candidates) must be defined prospectively

### Decision: Hold *(for all remaining 9 predicted indications)*

Insufficient mechanistic rationale and/or zero supporting evidence preclude further evaluation at this time. Re-assessment recommended if new preclinical data emerge for breast carcinoma or pulmonary hypertension targets.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

