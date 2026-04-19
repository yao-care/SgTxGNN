# Alpelisib: From Advanced Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib (Piqray®, BYL719) is a selective PI3Kα inhibitor, globally approved for PIK3CA-mutated HR+/HER2- advanced or metastatic breast cancer, though it has not been registered in Singapore.
The TxGNN model predicts potential efficacy for **Pulmonary Hypertension** with a score of 99.03%, but the **1 clinical trial** and **2 publications** retrieved provide no direct therapeutic support — in fact, available evidence points to pulmonary adverse events rather than benefit.
At this stage, this prediction is considered a model-only signal requiring substantial mechanistic validation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | PIK3CA-mutated HR+/HER2- advanced or metastatic breast cancer (FDA/EMA approved; not registered in Singapore) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Alpelisib is a selective inhibitor of the class I phosphoinositide 3-kinase alpha (PI3Kα) catalytic subunit encoded by *PIK3CA*. By blocking PI3Kα, it suppresses the downstream PI3K/AKT/mTOR signaling cascade, which is critical for cell survival, growth, and proliferation in tumors harboring activating *PIK3CA* mutations. Its efficacy has been clinically validated in the Phase 3 SOLAR-1 trial (NCT02437318), which demonstrated significantly prolonged progression-free survival in PIK3CA-mutated HR+/HER2- advanced breast cancer.

The theoretical basis for a pulmonary hypertension (PH) indication rests on the known involvement of PI3K/AKT/mTOR signaling in pulmonary arterial smooth muscle cell (PASMC) hyperproliferation and vascular remodeling — the central pathological processes in pulmonary arterial hypertension (PAH). Inhibiting this pathway could, in principle, reduce the aberrant PASMC proliferation that drives disease progression.

However, the available evidence directly contradicts this hypothesis in the context of Alpelisib. First, the retrieved literature shows that alpelisib causes **interstitial lung disease (ILD) as an adverse event** in breast cancer patients, rather than demonstrating pulmonary benefit. Second, a preclinical mechanistic study found that PI3Kα pathway inhibition combined with doxorubicin leads to adverse biventricular atrophy and **right ventricular dysfunction** — the opposite of a therapeutic effect in PH. Furthermore, the PI3K isoforms most implicated in PAH pathobiology are PI3Kβ and PI3Kγ, not PI3Kα, making the isoform selectivity of alpelisib a poor match for this disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completed | 435 | Multinational retrospective cohort study of HR+/HER2- advanced breast cancer patients treated with ribociclib or alpelisib (2018–2021). No connection to pulmonary hypertension; enrolled only breast cancer patients. Relevance to this indication: none. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | J Oncol Pharm Pract | Alpelisib-induced interstitial lung disease (ILD) documented as a serious adverse event in an advanced breast cancer patient. Highlights pulmonary **toxicity risk** rather than any therapeutic role in pulmonary disease. |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical/Mechanistic | J Am Heart Assoc | PI3Kα pathway inhibition combined with doxorubicin produced biventricular atrophy and **right ventricular dysfunction** in preclinical cardiac models. Suggests alpelisib may exert adverse cardiopulmonary effects rather than benefit in pulmonary hypertension. |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Selective PI3Kα inhibitor (non-conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate (less prominent than conventional chemotherapy; neutropenia and anemia reported at lower rates) |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood glucose (hyperglycemia is the primary dose-limiting toxicity; diabetic and pre-diabetic patients at high risk), CBC with differential, liver function tests, renal function, skin and mucosal reactions (rash, stomatitis) |
| Handling Protection | Follow institutional cytotoxic/targeted oral agent handling procedures; standard precautions for oral antineoplastic drugs apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction reaches only L5 (model-only signal), and critically, the available literature indicates alpelisib is associated with **pulmonary adverse events (ILD)** and preclinical **cardiopulmonary harm** — directly contradicting any therapeutic application in pulmonary hypertension. The primary PI3K isoforms driving PAH pathobiology (PI3Kβ and PI3Kγ) are distinct from alpelisib's PI3Kα selectivity, further undermining biological plausibility.

**To proceed, the following is needed:**
- Dedicated PAH preclinical model studies with alpelisib to establish whether any therapeutic signal exists beyond model prediction
- Clarification of PI3K isoform contributions (α vs. β/γ) in PAH pathophysiology, and whether PI3Kα plays a meaningful independent role
- Resolution of the ILD and right ventricular dysfunction safety signal before any pulmonary indication is considered
- MOA data retrieval from DrugBank to complete the full mechanistic analysis
- TFDA/SmPC package insert review to characterize pulmonary-specific contraindications and warnings

> **Note:** Among the 10 predicted indications in this Evidence Pack, **Multiple Endocrine Neoplasia (MEN)** (Rank 10, score 98.38%, L3) carries a stronger mechanistic rationale — PIK3CA mutations are documented across MEN-associated endocrine tumors, and the SOLAR-1 Phase 3 trial establishes PI3Kα inhibition as a validated concept in PIK3CA-mutated solid tumors. That indication warrants separate evaluation as a Research Question.

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*