# Bacitracin: From Topical Bacterial Infection to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a polypeptide antibiotic with established topical use against gram-positive bacterial infections, including minor skin wounds and ophthalmic infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
however this prediction is currently supported by **no clinical trials and no published literature**, representing a model-only hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical gram-positive bacterial infections (skin, ophthalmic) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query. Based on known pharmacological information, Bacitracin is a polypeptide antibiotic that disrupts bacterial cell wall synthesis by inhibiting the dephosphorylation of C55-isoprenyl pyrophosphate, a membrane-bound lipid carrier involved in peptidoglycan assembly. This mechanism is most effective against gram-positive bacteria such as *Staphylococcus aureus* and *Streptococcus* species, and is used almost exclusively as a topical agent due to systemic nephrotoxicity.

Punctate epithelial keratoconjunctivitis (PEK) is a superficial corneal and conjunctival inflammatory condition that can be caused by bacterial pathogens — most notably gram-positive cocci — as well as viral agents and mechanical irritants. The TxGNN model may have inferred this association from Bacitracin's established ophthalmic formulation profile: Bacitracin ophthalmic ointment is already a recognised vehicle for treating superficial bacterial ocular infections, and PEK can manifest as a bacterial complication.

However, the mechanistic link is indirect and highly conditional. Many cases of PEK are viral (adenovirus, HSV) or non-infectious in origin, where Bacitracin would offer no benefit. Furthermore, the complete absence of any clinical trial or published literature specifically connecting Bacitracin to PEK means this prediction cannot be advanced beyond a theoretical hypothesis. The high TxGNN score likely reflects the broader ophthalmic infection topology within the knowledge graph rather than a specific evidence-based association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Bacitracin is contraindicated for systemic or intravenous use due to significant nephrotoxicity. All clinical applications should be limited to topical routes (skin, ophthalmic). Detailed Singapore-specific warnings and contraindications were not available from the current data query and should be retrieved from the prescribing information prior to any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score to Bacitracin for punctate epithelial keratoconjunctivitis, but this is a model-only prediction (L5) with zero supporting clinical trials or literature. The biological plausibility is limited to bacterial-origin PEK, which represents only a subset of this condition. Additionally, Bacitracin is not registered in Singapore, further limiting its immediate translational relevance.

**To proceed, the following is needed:**

- Confirm the proportion of PEK cases attributable to gram-positive bacterial infection (to assess true mechanistic relevance)
- Conduct a scoping review of existing ophthalmic Bacitracin formulations and their efficacy for bacterial keratoconjunctivitis (broader category)
- Retrieve Bacitracin's full mechanism of action and toxicity data from DrugBank API (Data Gap DG002)
- Retrieve Singapore HSA / TFDA package insert for contraindications and warnings (Data Gap DG001)
- Consider whether **otitis externa** (Rank 4, Evidence Level L3, with 6 supporting publications including one controlled clinical comparison) may be a more tractable repurposing candidate to investigate first, given substantially stronger existing evidence