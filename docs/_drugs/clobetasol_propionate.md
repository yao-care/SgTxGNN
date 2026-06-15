---
layout: default
title: Clobetasol Propionate
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Clobetasol Propionate
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

# Clobetasol Propionate: From Corticosteroid-Responsive Dermatoses to Psoriasis

## One-Sentence Summary

Clobetasol propionate is a superpotent Class I topical corticosteroid used internationally for various inflammatory skin conditions, but it is currently not registered in Singapore.
The TxGNN model generated 10 predicted indications; **psoriasis** carries by far the strongest evidence base — with **39 clinical trials** and **20 publications** — despite appearing at rank 10 by model score (96.30%), reflecting that the model prioritises novelty over established uses.
Given multiple completed Phase 3 and Phase 4 RCTs, psoriasis is the primary actionable candidate and is recommended to **Proceed with Guardrails**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; internationally recognised for corticosteroid-responsive inflammatory dermatoses |
| Predicted New Indication | Psoriasis (TxGNN Rank 10; Evidence Rank 1 among all predictions) |
| TxGNN Prediction Score | 96.30% |
| Evidence Level | L1 |
| Singapore Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN Ranking vs. Evidence Level:** The model's top-ranked prediction (Rank 1: vulvar inverted follicular keratosis, score 99.46%) has zero supporting trials or publications (L5, Hold). Psoriasis ranks 10th by model score but achieves L1 evidence — the highest among all 10 predictions. This report focuses on psoriasis as the most clinically actionable finding.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current DrugBank record. Based on published pharmacology, clobetasol propionate is the most potent of all commercially available topical steroids (Class I / superpotent). It binds glucocorticoid receptors in keratinocytes and immune cells, suppressing pro-inflammatory cytokine transcription via NF-κB pathway inhibition and phospholipase A2 blockade. This reduces the Th1/Th17 axis mediators — particularly IL-17A, IL-22, and TNF-α — while simultaneously inhibiting keratinocyte hyperproliferation and local vasodilation.

Psoriasis is a chronic immune-mediated skin disease driven by uncontrolled keratinocyte proliferation and Th17-axis inflammation. The same cytokine cascade that clobetasol suppresses — IL-17A, IL-22, TNF-α — constitutes the core pathology of plaque psoriasis. This mechanistic alignment is direct and highly specific, which explains why international guidelines (American Academy of Dermatology, British Association of Dermatologists, European Dermatology Forum) consistently designate superpotent topical corticosteroids as the first-line treatment for mild-to-moderate plaque psoriasis.

The absence of Singapore registration for clobetasol represents a market access gap rather than an evidence gap. The global body of evidence — comprising nearly 40 registered clinical trials and two decades of published reviews — firmly establishes clobetasol as a standard-of-care option. The TxGNN model's prediction, even at rank 10, confirms algorithmic support for a repurposing pathway in the Singapore context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01235442](https://clinicaltrials.gov/study/NCT01235442) | Phase 3 | Completed | 592 | Etanercept + short-course clobetasol propionate foam vs etanercept monotherapy in moderate-to-severe plaque psoriasis; primary endpoint PASI 75 at Week 12; largest direct RCT demonstrating add-on topical benefit |
| [NCT00438399](https://clinicaltrials.gov/study/NCT00438399) | Phase 3 | Completed | 219 | Clobetasol propionate shampoo 0.05% (Clobex®) preference vs three other topical corticosteroids in moderate-to-severe scalp psoriasis; Phase 3 head-to-head preference and efficacy data |
| [NCT00658788](https://clinicaltrials.gov/study/NCT00658788) | Phase 3 | Completed | 305 | Multicenter, open-label; consecutive clobetasol propionate 0.05% spray followed by calcitriol ointment for moderate-to-severe plaque psoriasis; safety and efficacy of sequential regimen |
| [NCT05706870](https://clinicaltrials.gov/study/NCT05706870) | Phase 2 | Completed | 190 | Multicenter, randomized, double-blind, placebo-controlled; GN-037 cream vs clobetasol 17-propionate vs placebo in mild-to-moderate plaque psoriasis; high-quality Phase 2 benchmark data |
| [NCT00733954](https://clinicaltrials.gov/study/NCT00733954) | Phase 4 | Completed | 250 | Clobetasol propionate spray vs clobetasol propionate ointment in moderate-to-severe stable plaque psoriasis; efficacy, safety, patient satisfaction, and duration of response compared |
| [NCT00437255](https://clinicaltrials.gov/study/NCT00437255) | Phase 4 | Completed | 122 | Clobetasol propionate spray vs Taclonex® ointment in stable plaque psoriasis; Overall Disease Severity and IGA assessed across multiple time points |
| [NCT00988637](https://clinicaltrials.gov/study/NCT00988637) | Phase 4 | Completed | 138 | Multicenter; two regimens combining clobetasol spray and calcitriol ointment for moderate plaque psoriasis; four-week safety and efficacy evaluation |
| [NCT00436540](https://clinicaltrials.gov/study/NCT00436540) | Phase 4 | Completed | 78 | Clobetasol propionate spray (Clobex®) vs clobetasol propionate foam (Olux®) in stable plaque psoriasis; formulation-level equivalence and patient preference |
| [NCT00842153](https://clinicaltrials.gov/study/NCT00842153) | Phase 4 | Completed | 58 | Clobetasol propionate vs vehicle in mild-to-moderate plaque-type psoriasis; direct placebo-controlled efficacy and safety confirmation |
| [NCT01043224](https://clinicaltrials.gov/study/NCT01043224) | Phase 1 | Completed | 24 | Psoriasis plaque test: clobetasol propionate + calcipotriol combination ointment vs each component alone vs vehicle; mechanistic anti-psoriatic effect and combination rationale |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [32308782](https://pubmed.ncbi.nlm.nih.gov/32308782/) | 2020 | Systematic Review | J Clin Aesthet Dermatol | Comprehensive review of topical corticosteroid therapy for psoriasis; discusses product selection tendencies, potency determinants, vehicle effects on penetration, and real-world clinical outcomes for clobetasol propionate |
| [18806904](https://pubmed.ncbi.nlm.nih.gov/18806904/) | 2008 | Review | Drugs of Today | Detailed review of clobetasol propionate's anti-inflammatory, immunosuppressive, and antimitotic mechanisms; confirms efficacy in psoriasis, atopic dermatitis, and vulvar lichen sclerosus; addresses symptomatic vs preventive use |
| [36745373](https://pubmed.ncbi.nlm.nih.gov/36745373/) | 2023 | RCT | J Drugs Dermatol | Investigator-initiated trial of halobetasol/tazarotene polymeric emulsion in palmoplantar psoriasis; provides comparative context for superpotent corticosteroid class in difficult-to-treat psoriasis subtypes |
| [35533304](https://pubmed.ncbi.nlm.nih.gov/35533304/) | 2022 | RCT | Skin Therapy Lett | Halobetasol propionate 0.01% lotion for plaque psoriasis; Phase 3 pivotal trial data showing treatment success (IGA 0/1 with ≥2-grade improvement) in over 30% of patients; class comparator for superpotent corticosteroids |
| [19824740](https://pubmed.ncbi.nlm.nih.gov/19824740/) | 2009 | Review | Am J Clin Dermatol | Comparison of clobetasol propionate spray, foam, lotion, and shampoo formulations for psoriasis; concludes newer vehicles provide equivalent efficacy and safety to traditional ointment with improved cosmetic acceptability |
| [16774104](https://pubmed.ncbi.nlm.nih.gov/16774104/) | 2006 | Clinical Comparative Study | J Drugs Dermatol | Clobetasol propionate is the most widely prescribed topical therapy for psoriasis in the US; reviews relative potency across vehicle types; challenges conventional assumption that ointments are universally more potent |
| [16086659](https://pubmed.ncbi.nlm.nih.gov/16086659/) | 2005 | Clinical Study | Expert Opin Pharmacother | Clobetasol propionate foam 0.05% for psoriasis, especially scalp-type; improved cosmetic profile increases patient adherence; foam demonstrates absorption advantage over solution in cadaver skin studies |
| [11705308](https://pubmed.ncbi.nlm.nih.gov/11705308/) | 2001 | Clinical Study | Am J Clin Dermatol | Clobetasol propionate foam 0.05% in moderate-to-severe scalp psoriasis showed significant improvement vs placebo across all symptom scores over 2 weeks; established foam formulation for psoriasis |
| [3528243](https://pubmed.ncbi.nlm.nih.gov/3528243/) | 1986 | Review | J Am Acad Dermatol | Landmark clinical review establishing clobetasol-17-propionate as the most potent available topical steroid; demonstrated superiority over Class II steroids in psoriasis; introduced intermittent pulsed-dosing rationale to extend remission |
| [39695818](https://pubmed.ncbi.nlm.nih.gov/39695818/) | 2024 | Case Report | J Med Case Reports | Iatrogenic Cushing's syndrome from topical clobetasol in a child with psoriasis; documents HPA axis suppression risk with extended use; important safety signal for paediatric prescribing |

---

## Singapore Market Information

Clobetasol propionate has no current registrations with the Health Sciences Authority (HSA) of Singapore. No active licences, approved product names, dosage forms, or approved indications are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | Not registered | — | — |

> Clobetasol propionate is approved and widely marketed in the US (FDA), EU (EMA), UK (MHRA), Japan (PMDA), and many Asia-Pacific markets for corticosteroid-responsive dermatoses including psoriasis. Its absence from Singapore's register represents a regulatory gap, not a scientific one.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Safety signal from evidence pack literature:** Long-term topical clobetasol propionate use in a paediatric psoriasis patient was associated with complicated iatrogenic Cushing's syndrome and HPA axis suppression (PMID [39695818](https://pubmed.ncbi.nlm.nih.gov/39695818/), 2024). This underscores the need for time-limited, pulsed dosing protocols — as established in the 1986 landmark review (PMID [3528243](https://pubmed.ncbi.nlm.nih.gov/3528243/)) — and monitoring in vulnerable populations. Full warnings and contraindications should be obtained from the originator package insert (e.g., FDA labelling for Clobex® or Olux-E®) before any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 and Phase 4 RCTs directly demonstrate clobetasol propionate's efficacy and safety profile in plaque psoriasis, and international dermatology guidelines universally recognise it as a first-line topical agent; the barrier to adoption in Singapore is regulatory access rather than evidentiary uncertainty.

**To proceed, the following is needed:**

- **Regulatory pathway:** File an HSA New Drug Application supported by existing Phase 3 RCT data (e.g., NCT01235442, NCT00438399, NCT00658788) and international reference approvals (FDA, EMA)
- **MOA documentation:** Query DrugBank API (DB01013) to formally document the mechanism of action for the evidence dossier
- **Safety review:** Obtain and parse the originator TFDA/FDA/EMA package insert to document official warnings, contraindications, and special population guidance (particularly paediatric, pregnancy, and large body surface area use)
- **Pharmacovigilance plan:** Address known risks — HPA axis suppression, skin atrophy with prolonged use, secondary infections, and paediatric Cushing's risk — with proposed monitoring parameters (morning cortisol, clinical skin assessment at follow-up)
- **Formulation strategy:** Determine which formulation(s) to register for Singapore (cream, ointment, foam, shampoo, spray) based on local prescribing needs and regulatory precedent
- **Dosing guidance:** Incorporate intermittent/pulsed dosing recommendations from evidence base to mitigate long-term corticosteroid adverse effects
- **YMYL disclaimer:** All patient-facing materials must include: "This prediction is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application."
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

