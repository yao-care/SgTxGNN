# AMBROXOL HYDROCHLORIDE: Evaluation Incomplete — No Repurposing Predictions Available

## One-Sentence Summary

Ambroxol Hydrochloride is a mucolytic agent widely used to treat respiratory tract disorders involving excessive mucus production, such as bronchitis and COPD.
The TxGNN model did not return any predicted new indications for this drug in the current run,
and the evidence pack is missing key data required for a complete repurposing evaluation — including mechanism of action, safety warnings, and Singapore regulatory records.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data pack |
| Predicted New Indication | No predictions returned |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No predictions to evaluate |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug interaction data was found in the DDI query. Key warnings and contraindications were not available in this evidence pack. Please consult the official prescribing information before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned zero predicted indications for Ambroxol Hydrochloride, and the evidence pack contains two blocking data gaps — the Singapore (HSA) prescribing information and mechanism of action — which prevent even a baseline safety and mechanistic assessment. No evaluation can proceed without these inputs.

**To proceed, the following is needed:**

- **Predicted indications from TxGNN**: Re-run the KG + DL prediction pipeline with `AMBROXOL HYDROCHLORIDE` mapped to its correct DrugBank ID (DB06742). Verify that the drug node exists in `data/node.csv` and that mappings in `drugbank_mapper.py` cover the hydrochloride salt form.
- **DrugBank ID confirmation**: The `drugbank_id` field is null. Confirm the correct ID (likely DB06742 for ambroxol) and re-query DrugBank for MOA, categories, and toxicity data.
- **Singapore HSA package insert**: Download the prescribing information PDF from the HSA product listing to extract approved indications, key warnings, and contraindications (Data Gap DG001).
- **Singapore market registration check**: Ambroxol is available in many Asian markets; verify whether it is registered under a different INN spelling, brand name, or combination product (e.g., ambroxol + other agents) in the HSA database before confirming "Not marketed" status.
- **MOA data** (Data Gap DG002): Retrieve mechanism of action from DrugBank or ChEMBL to enable mechanistic plausibility analysis for any future predictions.