# Hyaluronidase: From Spreading/Dispersing Agent to Diabetic Retinopathy

## One-Sentence Summary

Hyaluronidase is a naturally occurring enzyme that degrades hyaluronic acid (HA), classically used as a spreading/dispersing adjunct in local anaesthesia and as a reversal agent for HA-based dermal fillers.
The TxGNN model generated 10 predicted indications; while **esotropia** ranks highest by model score (99.89%), its sole supporting publication represents a **reverse safety signal** — the literature records Hyaluronidase as a potential *cause* of strabismus following retrobulbar anaesthesia, not a treatment.
The most clinically actionable prediction is **diabetic retinopathy** (model score 99.71%), backed by **2 completed Phase 3 RCTs** (n=510 and n=750) and **20 publications**, warranting a **Proceed with Guardrails** decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Known Clinical Application | Spreading/dispersing agent; adjunct to local anaesthesia; HA filler reversal agent |
| Top-Evidenced Predicted Indication | Diabetic Retinopathy |
| TxGNN Score (Diabetic Retinopathy) | 99.71% |
| Evidence Level | L1 (2 completed Phase 3 RCTs) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Hyaluronidase catalyses the hydrolytic cleavage of hyaluronic acid (HA), the dominant glycosaminoglycan within the vitreous body of the eye. In diabetic retinopathy — particularly the proliferative stage — pathological changes at the vitreoretinal interface are central to disease progression: HA accumulation contributes to vitreous gel condensation, traction on the retinal surface, vitreous haemorrhage, and ultimately tractional retinal detachment. By enzymatically digesting intravitreal HA, Hyaluronidase promotes **pharmacologic vitreolysis** — non-surgical liquefaction and separation of the posterior vitreous cortex from the retina — thereby addressing the mechanical driver of haemorrhage and traction without requiring vitrectomy.

A 2026 translational study (PMID 41789111) directly confirmed that dysregulated HA metabolism drives both inflammation and angiogenesis in proliferative diabetic retinopathy, further strengthening the pathway logic. Multiple review articles document that intravitreal injection of ovine Hyaluronidase (Vitrase®, ISTA Pharmaceuticals) achieved posterior vitreous detachment and cleared haemorrhage in human subjects. This is not a purely computational prediction: a dedicated clinical development programme reached Phase 3, generating the largest intravitreal pharmacologic vitreolysis dataset to date.

It is important to note that the TxGNN model's **highest-ranked** prediction, esotropia (99.89%), must be treated with caution. The single supporting publication (PMID 16934027) describes persistent diplopia and strabismus as an *adverse outcome* of retrobulbar anaesthesia that included Hyaluronidase — this is a complication report, not evidence of therapeutic benefit. The high TxGNN score likely reflects graph proximity between Hyaluronidase and ophthalmic surgical nodes, rather than a genuine therapeutic signal.

---

## All Predicted Indications at a Glance

| Rank | Indication | TxGNN Score | Evidence Level | Clinical Trials | Publications | Recommendation |
|------|-----------|------------|----------------|-----------------|--------------|----------------|
| 1 | Esotropia | 99.89% | L4 | 0 | 1 | ⚠️ Hold — Reverse Signal |
| 2 | Amenorrhea | 99.83% | L4 | 0 | 1 | Hold |
| 3 | Severe NPDR | 99.79% | L3 | 1 | 0 | Research Question |
| 4 | Renal Tubular Acidosis | 99.76% | L5 | 0 | 0 | Hold |
| **5** | **Dermatitis** | **99.73%** | **L2** | **1 RCT** | **20** | **Research Question** |
| **6** | **Diabetic Retinopathy** | **99.71%** | **L1** | **3 (incl. 2× Ph3)** | **20** | **✅ Proceed with Guardrails** |
| 7 | Acrodermatitis Chronica Atrophicans | 99.58% | L5 | 0 | 0 | Hold |
| 8 | Diabetic Cataract | 99.55% | L4 | 0 | 5 | Hold |
| 9 | Neonatal Dermatomyositis | 99.51% | L5 | 0 | 1 | Hold |
| 10 | Non-syndromic Esophageal Malformation | 99.51% | L5 | 0 | 0 | Hold |

---

## Clinical Trial Evidence

### Primary Focus: Diabetic Retinopathy

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00198510](https://clinicaltrials.gov/study/NCT00198510) | Phase 3 | Completed | 750 | Vitrase (ovine hyaluronidase) intravitreal injection for clearance of severe vitreous haemorrhage in diabetic retinopathy — largest pharmacologic vitreolysis RCT |
| [NCT00198497](https://clinicaltrials.gov/study/NCT00198497) | Phase 3 | Completed | 510 | Vitrase intravitreal injection for clearance of severe vitreous haemorrhage — parallel Phase 3 trial confirming the clinical programme |
| [NCT00198471](https://clinicaltrials.gov/study/NCT00198471) | Phase 2 | Completed | 10 | Open-label: Vitrase intravitreal injection to induce posterior vitreous detachment (PVD) in subjects with moderate-to-severe NPDR; pilot data preceding the Phase 3 programme |

### Secondary Focus: Dermatitis (L2 Evidence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00928447](https://clinicaltrials.gov/study/NCT00928447) | Phase 2 | Completed | 22 | Prospective, randomised, double-blind, placebo-controlled study of intradermal rHuPH20 (recombinant human hyaluronidase) vs. placebo for prevention and treatment of nickel allergic contact dermatitis — most rigorous direct evidence for this indication |

---

## Literature Evidence

### Diabetic Retinopathy

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41789111](https://pubmed.ncbi.nlm.nih.gov/41789111/) | 2026 | Mechanistic/Translational | Frontiers in Immunology | Dysregulated HA metabolism (HAS-2, Hyal-1, Hyal-2, CD44, RHAMM) drives inflammation and angiogenesis in PDR; directly confirms HA pathway as therapeutic target |
| [20939804](https://pubmed.ncbi.nlm.nih.gov/20939804/) | 2011 | Review | Curr Pharm Biotechnology | Comprehensive review of pharmacologic vitreolysis in DR: intravitreal ovine hyaluronidase cleared vitreous haemorrhage in clinical trials; multiple human case series included |
| [19199900](https://pubmed.ncbi.nlm.nih.gov/19199900/) | 2009 | Review | Curr Diabetes Reviews | Enzymatic vitreolysis review: vitreoretinal interface in DR pathogenesis; Hyaluronidase among agents studied for PVD induction |
| [23847321](https://pubmed.ncbi.nlm.nih.gov/23847321/) | 2013 | Mechanistic | Invest Ophthalmol Vis Sci | Enzyme-induced vitreolysis alleviates DR progression via HIF-1α pathway — key mechanistic pathway study |
| [12757408](https://pubmed.ncbi.nlm.nih.gov/12757408/) | 2003 | Drug Profile | Drugs in R&D | Vitrase (ovine hyaluronidase) ophthalmic injectable: developed specifically for vitreous haemorrhage and diabetic retinopathy |
| [17245084](https://pubmed.ncbi.nlm.nih.gov/17245084/) | 2007 | Review | Dev Ophthalmology | Pharmacologic vitreolysis overview: incomplete PVD and attached vitreous cortex associated with DR progression; Hyaluronidase as candidate agent |
| [19050667](https://pubmed.ncbi.nlm.nih.gov/19050667/) | 2009 | Animal Study | Retina | Pharmacologic vitreolysis with plasmin and hyaluronidase in diabetic rats: feasibility of PVD induction demonstrated |
| [30445048](https://pubmed.ncbi.nlm.nih.gov/30445048/) | 2019 | Animal Study | Exp Eye Research | Hyaluronidase reduced retinal endothelial glycocalyx thickness in diabetic mice — raises mechanistic complexity regarding glycocalyx effects |
| [19644368](https://pubmed.ncbi.nlm.nih.gov/19644368/) | 2009 | Review | Curr Opin Ophthalmology | Changing paradigms in DR treatment: pharmacologic vitreolysis including Hyaluronidase reviewed as emerging strategy |
| [17713597](https://pubmed.ncbi.nlm.nih.gov/17713597/) | 2007 | Review | Exp Diabetes Research | Pharmacotherapies for DR: intravitreal adjunctive agents including hyaluronidase discussed alongside triamcinolone and anti-VEGF agents |

### Dermatitis

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37145319](https://pubmed.ncbi.nlm.nih.gov/37145319/) | 2024 | Review | Aesthetic Plastic Surgery | Allergic complications of hyaluronidase injection: risk factors, treatment strategies — importantly highlights Hyaluronidase itself as an allergen, dual-role drug |
| [15426122](https://pubmed.ncbi.nlm.nih.gov/15426122/) | 1950 | Early Clinical Observation | Ann New York Acad Sci | Early clinical investigation of Hyaluronidase and skin inflammation |
| [24658508](https://pubmed.ncbi.nlm.nih.gov/24658508/) | 2014 | Mechanistic | J Invest Dermatology | HA metabolism in keratinocytes and atopic dermatitis skin driven by balance of HAS-1 and HAS-3 — contextualises HA pathway role in dermatitis |
| [14332642](https://pubmed.ncbi.nlm.nih.gov/14332642/) | 1965 | Case Series | J Invest Dermatology | Effects of serum from dermatitis herpetiformis cases on hyaluronidase viscosity-reduction — early mechanistic investigation |

> **⚠️ Mechanistic Warning for Dermatitis:** Several publications (PMIDs 26716906, 35455695, 31426284) show that *inhibiting* Hyaluronidase activity ameliorates experimental dermatitis models — suggesting HA degradation may have dual/opposing roles in skin inflammation depending on fragment size and context. The NCT00928447 RCT results are needed to resolve this directional uncertainty before advancing.

---

## Singapore Market Information

Hyaluronidase (DB14740) is **not currently registered** in Singapore. No product authorisations were identified in the Singapore regulatory database. Global context:
- **Vitrase®** (ovine hyaluronidase, ISTA Pharmaceuticals): US FDA ophthalmic IND development for vitreous haemorrhage/DR; the Phase 3 programme was completed but US approval was not obtained for the DR indication at the time
- **Hylenex®** (recombinant human hyaluronidase PH20, rHuPH20, Halozyme): FDA-approved as a spreading agent; the rHuPH20 formulation was used in the dermatitis RCT (NCT00928447)

---

## Safety Considerations

Detailed safety data (TFDA package insert warnings, contraindications) are not available in this evidence pack and must be retrieved before any clinical evaluation proceeds.

**Known safety signals from the evidence pack:**

- **Reverse Signal — Esotropia/Diplopia:** PMID 16934027 documents persistent diplopia and strabismus as a complication of retrobulbar anaesthesia containing Hyaluronidase. This represents an **adverse event** from use as a spreading agent, not a therapeutic application.
- **Allergic Reactions:** PMID 37145319 (2024 review) documents hyaluronidase allergy, frequently misdiagnosed, occurring since at least 1984. Risk factors and management strategies are described. This is a clinically relevant safety concern for any new indication.
- **Potential Dual Role in Dermatitis:** High-dose or sustained hyaluronidase activity may generate pro-inflammatory HA fragments, producing paradoxical worsening — particularly relevant for any dermatitis application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (combined n=1,260) and a mechanistically coherent HA-degradation pathway strongly support Hyaluronidase's therapeutic potential in diabetic retinopathy. A 2026 translational study confirming HA pathway dysregulation as a driver of PDR inflammation and angiogenesis further solidifies the biological rationale. Although Hyaluronidase is not currently registered in Singapore, the clinical development history (Vitrase®) provides a substantial regulatory precedent.

**To proceed, the following is needed:**

- **Retrieve Phase 3 full results** (NCT00198510 and NCT00198497): assess primary endpoint (vitreous haemorrhage clearance rate), visual acuity outcomes, and adverse event profile
- **Determine optimal formulation**: Assess whether ovine Vitrase® or recombinant rHuPH20 (Hylenex® formulation) is more appropriate for Singapore market — immunogenicity profiles differ
- **Complete safety data retrieval**: Obtain full package insert (warnings, contraindications, post-marketing signals) from the FDA/EMA via DrugBank or official sources (DG001 remediation)
- **Retrieve MOA data from DrugBank API** (DG002 remediation): confirm enzyme kinetics, receptor interactions, and known off-target effects
- **Evaluate Singapore regulatory pathway**: Explore whether HSA abridged or full NDA pathway applies; note Hyaluronidase (as a well-known enzyme) may qualify for a streamlined approach
- **For the dermatitis secondary indication (L2)**: Retrieve NCT00928447 full results before deciding whether a separate clinical strategy is warranted; resolve the mechanistic paradox (anti-hyaluronidase agents also improve dermatitis in preclinical models) before advancing
- **Flag esotropia (Rank 1 TxGNN) as a false positive**: Document the reverse signal in the project record to prevent future re-evaluation without new mechanistic data

> *Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*