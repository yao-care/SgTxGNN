# Icodextrin: From Peritoneal Dialysis to Irritable Bowel Syndrome

## One-Sentence Summary

Icodextrin is a glucose polymer-based osmotic agent, primarily used as a peritoneal dialysis solution (e.g., Extraneal) to manage fluid overload in end-stage renal disease patients.
The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**,
however, **no clinical trials and no supporting publications** have been identified — this prediction is based solely on the model's knowledge graph inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peritoneal dialysis osmotic agent (fluid overload management in renal failure) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Icodextrin is a high-molecular-weight glucose polymer (starch-derived polysaccharide) that exerts its effect primarily through **colloidal osmotic pressure** rather than crystalloid osmosis. In the peritoneal cavity, it resists systemic absorption due to its large molecular size, sustaining ultrafiltration over long dwell times. Its primary established use is as an intraperitoneal dialysis solution.

The connection between Icodextrin and IBS is mechanistically tenuous. IBS pathophysiology involves altered gut motility, visceral hypersensitivity, and gut-brain axis dysregulation. Icodextrin, being a poorly absorbed polysaccharide when ingested orally, would behave analogously to a **FODMAP** (fermentable oligosaccharide) — a category of compounds that is well-established to **worsen** IBS symptoms by increasing intraluminal osmotic load and promoting bacterial fermentation with gas production. The intraperitoneal route (the only approved delivery route) has no established mechanistic pathway to address intestinal motility or visceral sensation.

The high TxGNN score most likely reflects **shared neighbourhood nodes in the knowledge graph** — both IBS and Icodextrin are associated with gastrointestinal and fluid-related biological entities — rather than a genuine pharmacological relationship. This prediction should be considered a probable **false positive** from the model.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Icodextrin is not currently registered with the Health Sciences Authority (HSA) in Singapore. No product authorisations are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | No registrations found |

> **Note:** Icodextrin-based peritoneal dialysis solutions (e.g., Extraneal by Baxter) are marketed in multiple countries including the US, EU, and Australia, but no HSA registration data was retrieved in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No key warnings, contraindications, or drug interaction data were available in this Evidence Pack. Full safety data including hypersensitivity reactions (including rare but serious maltose-mediated false glucose monitoring interference) should be obtained from the originator's SmPC/package insert before any further assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are rated L5 (model prediction only) with zero supporting clinical trials or publications, and the top prediction (IBS) has a mechanistic rationale that argues *against* therapeutic benefit rather than for it. The mechanistic link between an intraperitoneal osmotic agent and any of the predicted indications (IBS, esophageal malformation, C1 inhibitor deficiency, potassium deficiency, etc.) is either implausible or absent. Proceeding with development for any of these indications cannot be justified at this stage.

**To revisit this assessment, the following would be needed:**

- **MOA clarification**: Obtain full DrugBank pharmacology data for Icodextrin, including any known off-target molecular interactions that might support a new therapeutic hypothesis
- **Reformulation hypothesis**: If an oral formulation is being considered, dedicated preclinical studies would be required to establish gut epithelial interactions; note that current evidence suggests oral Icodextrin may *exacerbate* IBS symptoms
- **KG audit**: Review whether the TxGNN knowledge graph contains peritoneal dialysis–related IBS co-occurrence data that may be driving the high score as a non-causal confound
- **Alternative indication screening**: Consider screening Icodextrin against indications more mechanistically aligned with its known properties — e.g., post-surgical adhesion prevention (Adept formulation), or conditions benefiting from sustained intraperitoneal oncotic pressure
- **Singapore regulatory pathway**: If a valid new indication is identified through the above steps, HSA regulatory registration strategy should be developed from the ground up given zero existing local market presence