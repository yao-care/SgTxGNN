---
layout: default
title: Carboprost Tromethamine
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Carboprost Tromethamine
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

# Carboprost Tromethamine: From Postpartum Hemorrhage to Atypical Coarctation of Aorta

## One-Sentence Summary

Carboprost tromethamine (Hemabate) is a synthetic prostaglandin F2α (PGF2α) analogue established clinically as a uterotonic agent for treating postpartum haemorrhage and inducing uterine contractions. The TxGNN model predicts activity across **10 new indications**, with **Atypical Coarctation of Aorta** ranking first (score 99.99%), though the most mechanistically credible candidate is **Primary Hereditary Glaucoma** (rank 10, L4), where the PGF2α → FP receptor pathway overlaps with approved glaucoma drugs. For 9 of the 10 predicted indications, no supporting clinical trials or literature were identified, and several predictions are directly contradicted by known PGF2α pharmacology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Postpartum haemorrhage; uterine atony; pregnancy termination |
| Predicted New Indication (Rank 1) | Atypical Coarctation of Aorta |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data sources queried. Based on established pharmacological knowledge, carboprost tromethamine is a 15-methyl analogue of prostaglandin F2α that acts as a selective FP receptor agonist, stimulating smooth muscle contractions — particularly in the uterus. This accounts for its proven efficacy in controlling postpartum haemorrhage and terminating pregnancy.

The rank 1 prediction — atypical coarctation of aorta — represents a congenital structural defect requiring surgical or catheter-based correction. While PGE1 (alprostadil) is used in neonates to maintain ductus arteriosus patency, carboprost as a PGF2α analogue produces opposing vasoconstrictive effects. There is no mechanistic pathway connecting FP receptor activation to the treatment of aortic coarctation, and the TxGNN model's prediction most likely reflects indirect prostaglandin-class linkages in the knowledge graph (KG noise) rather than a genuine drug–disease relationship.

The most mechanistically credible prediction across all 10 candidates is **rank 10: Primary Hereditary Glaucoma (L4)**. PGF2α analogues — latanoprost, bimatoprost, travoprost, tafluprost — are established first-line treatments for open-angle glaucoma, working through FP receptor activation to increase uveoscleral aqueous outflow and reduce intraocular pressure (IOP). Carboprost shares this receptor binding profile and was explored historically as an IOP-lowering candidate in early ophthalmology research. This class-level indirect evidence elevates rank 10 to a legitimate research question, though significant formulation challenges and systemic safety risks (uterine contractions, bronchospasm) remain unresolved.

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Assessment |
|------|---------|-------------|----------------|----------|------------|
| 1 | Atypical coarctation of aorta | 99.99% | L5 | Hold | Structural defect; PGF2α mechanism is vasoconstrictive — opposing PGE1's role; KG noise |
| 2 | Aortic malformation | 99.98% | L5 | Hold | Structural congenital disease; no PGF2α treatment rationale |
| 3 | Migraine with brainstem aura | 99.97% | L5 | Hold | PGF2α agonism may aggravate central sensitisation; mechanism opposed to NSAID approach |
| 4 | Migraine disorder | 99.96% | L5 | Hold | Same mechanistic concern as rank 3; no clinical data |
| 5 | Pulmonary hypertension | 99.93% | L5 | Hold | ⚠️ **Safety contraindication**: carboprost causes pulmonary vasoconstriction and bronchospasm |
| 6 | Non-syndromic esophageal malformation | 99.92% | L5 | Hold | Congenital structural defect; no PGF2α mechanism |
| 7 | Kyphoscoliotic heart disease | 99.92% | L5 | Hold | Secondary cardiopulmonary disease from spinal deformity; pulmonary vasoconstriction risk |
| 8 | Amenorrhea | 99.89% | L5 | Hold | Partial mechanistic plausibility (PGF2α promotes luteolysis/menstruation); systemic side effects limit clinical feasibility; no data |
| 9 | Esophageal disease | 99.83% | L5 | Hold | PGE2/PGI2 protect GI mucosa but carboprost is FP-selective — wrong receptor subtype; KG generalisation noise |
| 10 | Primary hereditary glaucoma | 99.69% | L4 | Research Question | Best mechanistic rationale: PGF2α → FP receptor → uveoscleral drainage; class analogy with latanoprost/bimatoprost |

---

## Clinical Trial Evidence

No clinical trials directly evaluating carboprost tromethamine for any of the 10 predicted indications were identified across ClinicalTrials.gov and ICTRP. One trial surfaced in the aortic malformation search but is not relevant to drug repurposing:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04481503](https://clinicaltrials.gov/study/NCT04481503) | N/A | Completed | 150 | Observational echocardiography study characterising cardiac function during labour. Carboprost, if present, would appear only as a background uterotonic agent — it is not a study intervention and provides no evidence for treating aortic malformation. |

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## Singapore Market Information

Carboprost tromethamine is **not registered with HSA** in Singapore. There are no active marketing authorisations, and no dosage forms are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical safety signal — Pulmonary Hypertension (Rank 5):** The mechanistic review flags that carboprost tromethamine is known clinically to cause **pulmonary vasoconstriction and bronchospasm**. Obstetric clinical guidelines explicitly list pulmonary hypertension as a contraindication or high-caution situation for carboprost use. The rank 5 prediction (pulmonary hypertension) therefore represents a potential harm risk rather than a repurposing opportunity and should be documented as a known contraindication in any clinical summary involving this drug.

---

## Conclusion and Next Steps

**Decision: Hold (9 of 10 indications) / Research Question (Primary Hereditary Glaucoma)**

**Rationale:**
The large majority of TxGNN predictions for carboprost tromethamine reflect prostaglandin-class knowledge graph connectivity rather than genuine mechanistic pathways. PGF2α agonism is pharmacologically distinct from — and in multiple cases directly opposed to — the prostaglandin subtypes relevant to the predicted diseases (PGE1 for vascular patency, PGI2 for pulmonary arterial hypertension, COX inhibition for migraine). The single exception is primary hereditary glaucoma, where FP receptor activation has a well-established therapeutic role in IOP reduction through the same class of drugs (latanoprost, bimatoprost) already in clinical use. Carboprost is not marketed in Singapore, eliminating any regulatory shortcut. The rank 5 prediction (pulmonary hypertension) should be actively flagged as a contraindication rather than a target.

**To advance the Primary Hereditary Glaucoma research question, the following is needed:**
- MOA data retrieval from DrugBank API (currently a data gap)
- Systematic literature review of historical carboprost IOP-lowering studies (pre-latanoprost era pharmacology)
- Ocular formulation feasibility assessment: carboprost lacks the 17-phenyl and ester modifications that optimise corneal penetration and FP-receptor selectivity in approved glaucoma agents
- Expert ophthalmology pharmacology consultation on MYOC/CYP1B1 mutation phenotypes and whether uveoscleral drainage enhancement can overcome trabecular structural damage
- Systemic safety risk assessment: any topical ocular formulation must demonstrate absence of meaningful uterotonic and bronchoconstrictor systemic absorption

**For all remaining 9 indications:** No further evaluation is recommended at this stage.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

