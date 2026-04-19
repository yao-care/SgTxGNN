# Hydrocortisone Acetate: From Topical Anti-inflammatory Use to Alopecia Areata

## One-Sentence Summary

Hydrocortisone acetate is the acetate ester form of hydrocortisone (cortisol), a well-established glucocorticoid used for mild-to-moderate inflammatory skin conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata** (圓禿),
with **1 completed Phase 3 clinical trial** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical anti-inflammatory (mild-to-moderate inflammatory skin conditions); no Singapore registration data available |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Hydrocortisone acetate is the acetate esterification of hydrocortisone (cortisol) — the primary endogenous glucocorticoid in humans. As a glucocorticoid receptor agonist (GRα), it inhibits NF-κB and AP-1 signalling pathways, suppresses pro-inflammatory cytokines including IL-2 and IFN-γ, and reduces local immune cell recruitment. The acetate ester form enhances percutaneous penetration and depot effect, making it particularly suitable for topical or intralesional administration.

Alopecia areata is a T-cell–mediated autoimmune disease in which CD8⁺ T cells breach the hair follicle's immune privilege zone — normally protected by low MHC-I expression and local immunosuppressive signals. This immune attack causes reversible hair follicle miniaturisation and hair loss. The mechanism of corticosteroids maps directly onto this pathology: by suppressing IL-2 and IFN-γ within the perifollicular microenvironment and restoring the immunosuppressive milieu, glucocorticoids can effectively re-establish follicular immune privilege.

Intralesional or topical hydrocortisone has been employed clinically in alopecia areata for decades — the 1973 literature (PMID 4755919) describes the use of intralesional hydrocortisone acetate suspension specifically for severe cases, and the completed Phase 3 trial (NCT01453686) directly compared hydrocortisone 1% cream against a higher-potency corticosteroid in paediatric alopecia areata. The mechanistic rationale is clear and direct, making this one of the more biologically plausible TxGNN predictions in this candidate set.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomised controlled trial comparing Clobetasol Propionate 0.05% cream versus Hydrocortisone 1% cream in children with alopecia areata. Hydrocortisone served as the active comparator, providing direct Phase 3 evidence of its clinical use in this indication. Sample size was modest (n=41); the trial formulation (1% cream) is a close comparator to hydrocortisone acetate but minor pharmacokinetic differences exist. |

> **Note:** In this trial, hydrocortisone 1% cream served as the comparator arm rather than the investigational drug. The evidence nonetheless establishes direct Phase 3 clinical use of hydrocortisone in paediatric alopecia areata.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | Clinical Study (Case Series) | Przeglad Dermatologiczny | Reports intralesional subcutaneous injection of hydrocortisone acetate suspension for severe forms of alopecia areata. This is the earliest direct clinical evidence using the specific acetate ester formulation (DB14539) in this indication. |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Review | MMW Münchener Medizinische Wochenschrift | Comprehensive review of topical therapy advances in skin diseases. Discusses comparative anti-inflammatory potency of hydrocortisone acetate versus newer corticosteroid esters, providing pharmacological context for its use in inflammatory dermatological conditions. |

---

## Singapore Market Information

Hydrocortisone acetate (DB14539) currently has **no registered products** in Singapore. There are no active licences on record.

> Pharmaceutical companies wishing to enter the Singapore market would need to submit a new drug application to the Health Sciences Authority (HSA).

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) for hydrocortisone acetate are not available in this Evidence Pack.

> Please refer to the package insert for complete safety information. For general glucocorticoid class effects, consult current dermatology guidelines — known class concerns include skin atrophy with prolonged topical use, HPA axis suppression (especially in children with extensive application), and secondary infection risk.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between hydrocortisone acetate and alopecia areata is direct and well-established — glucocorticoid-mediated restoration of follicular immune privilege is a primary therapeutic strategy in this disease. A completed Phase 3 RCT (NCT01453686, n=41) and 1973 case series using the acetate form specifically provide sufficient clinical grounding for L1 classification, despite the modest evidence base.

**To proceed, the following is needed:**

- **Singapore regulatory pathway confirmation:** Hydrocortisone acetate is currently not registered in Singapore; an HSA product registration submission is required before any clinical deployment
- **Formulation specification:** Clarify whether the intended route is topical cream, intralesional injection, or other; DB14539 (acetate ester) has distinct pharmacokinetic properties from hydrocortisone 1% cream used in NCT01453686 — bioequivalence data should be reviewed
- **Safety package completion:** Retrieve full prescribing information (package insert, contraindications, warnings) for the specific acetate formulation
- **Paediatric considerations:** The Phase 3 trial was conducted in children; if adult use is intended, age-specific dosing and safety data should be confirmed
- **MOA documentation:** Formal mechanism of action data from DrugBank or published sources should be retrieved to complete the pharmacological dossier
- **Comparative effectiveness context:** Stronger-potency corticosteroids (e.g., clobetasol, betamethasone) or intralesional triamcinolone are current standard-of-care in alopecia areata; a positioning rationale versus established treatments is needed