---
layout: default
title: Zinc Gluconate
parent: Low Evidence (L5)
nav_order: 1086
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Zinc Gluconate: predicted new indication Anemia of prematurity (evidence level L5). Approved use: Ascorbic acid deficiency"
---

# Zinc Gluconate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Zinc Gluconate: From Ascorbic Acid Deficiency (Scurvy) to Anemia of Prematurity

## One-Sentence Summary

Zinc gluconate is a zinc salt, and the knowledge graph used for this analysis lists ascorbic acid deficiency and scurvy as its original indications.
The TxGNN model predicts it may be effective for **anemia of prematurity**, but **no clinical trials and no publications** currently support this specific prediction.
The prediction rests on model output and a plausible biological link alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency; scurvy (from the knowledge graph). The Singapore licence record contains no approved indication text. |
| Predicted New Indication | Anemia of prematurity |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Zinc is an essential trace element that takes part in many enzyme systems. It also plays a role in erythropoiesis (red blood cell production) and iron metabolism, so a biological link to anemia is plausible.

The original indications (ascorbic acid deficiency and scurvy) are nutritional deficiency states. Anemia of prematurity is also a condition in which nutritional status and trace-element balance matter. This is where the model's prediction may come from, but the link has not been tested with studies.

There is also a safety concern. Excess zinc can induce copper deficiency, which causes anemia. This is a particular worry in preterm infants, who have limited copper stores. A case report in the literature compiled for the other predictions describes severe copper-deficiency anemia after prolonged high-dose zinc gluconate intake. The prediction is therefore biologically plausible but may be harmful in practice.

## Clinical Trial Evidence

Currently no related clinical trials registered for anemia of prematurity.

## Literature Evidence

Currently no related literature available for anemia of prematurity.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16768P | ZINC AGUETTANT CONCENTRATE FOR SOLUTION FOR INFUSION 1 MG/ML | Infusion, solution concentrate | Not stated in the licence record |

The only registered product is an injectable (infusion) formulation made by Laboratoire AGUETTANT.

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The knowledge graph lists drug-disease contraindication links with the following conditions:
  - Cardiovascular and immune: hypertension, rheumatoid arthritis, systemic lupus erythematosus (including paediatric), multiple sclerosis
  - Respiratory and allergic: asthma, allergic rhinitis, vasomotor rhinitis
  - Haematological and metal metabolism: blood coagulation disease, sickle cell anemia, hereditary persistence of fetal hemoglobin, hereditary hemochromatosis, hemosiderosis, iron metabolism disorders, Wilson disease
  - Other: primary hyperoxaluria, diarrheal disease, HIV infection and AIDS, leukemia

  These come from model data rather than the package insert and should be verified against the label.
- **Drug Interactions**: The interaction query returned 100 records. The ones listed here are mostly minor.
  - Moderate: alendronic acid, risedronic acid, ibandronate (bisphosphonates), tetracycline, baloxavir marboxil. These are likely chelation or absorption effects, so dosing separation may be needed.
  - Minor: immunosuppressants and biologics such as abatacept, adalimumab, azathioprine, baricitinib, belimumab, and corticosteroids such as hydrocortisone, dexamethasone, betamethasone and triamcinolone.
- **Signals from literature retrieved for other predictions**: Intranasal zinc gluconate has been linked to loss of smell (anosmia), and chronic excess zinc intake has been linked to copper-deficiency anemia. Neither is directly about the infusion product registered in Singapore, but both are relevant to any new use.

Package insert warnings were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the evidence is model output only (L5), with no trials or publications for anemia of prematurity. Zinc's known potential to cause copper-deficiency anemia is a specific concern in preterm infants. The drug is registered in Singapore only as an infusion, and no approved indication text is available.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- A targeted literature and trial search on zinc, copper balance and anemia in preterm infants
- Assessment of whether an infusion product is suitable for neonatal dosing, including a copper monitoring plan
- Review of the knowledge-graph contraindications, particularly the haematological and iron-metabolism conditions

---

### Other Predictions Reviewed

Other predictions ranked by the model had similarly limited support, and none changes the decision above.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Injury | 99.89% | L4 | Mostly animal studies on organ injury. The one Phase 3 trial (NCT06290219) tests platelet-rich plasma and hyaluronic acid, not zinc. |
| 3 | Cell proliferation disorder | 99.87% | L5 | Very broad category. The two papers are a mouse toxicity study and an in vitro disulfiram study. |
| 4 | Perinatal disease | 99.87% | L5 | Prediction only. |
| 5 | Segmental odontomaxillary dysplasia | 99.87% | L5 | Prediction only. |
| 6 | Florid cemento-osseous dysplasia | 99.87% | L5 | Prediction only. |
| 7 | Radiation or chemically induced disorder | 99.86% | L4 | Literature is mostly safety signals (anosmia, toxicity). |
| 8 | Disease by subcellular system affected | 99.86% | L5 | Ontology grouping term, not an actionable indication. |
| 9 | Iatrogenic disease | 99.85% | L5 | Prediction only. |
| 10 | Regional odontodysplasia | 99.85% | L5 | Prediction only. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

