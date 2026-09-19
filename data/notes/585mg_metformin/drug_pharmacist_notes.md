# Metformin: Data Quality Issue — Drug Repurposing Analysis Pending

## One-Sentence Summary

This candidate drug record contains an anomalous INN field "585MG METFORMIN)" which includes a dosage value and extraneous parenthesis, indicating data corruption prior to pipeline entry. The TxGNN model returned no predicted new indications, and no matching Singapore HSA registration exists, precluding completion of a full drug repurposing assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unobtainable |
| Predicted New Indication | None |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model record only; no linked research) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The TxGNN model returned no predicted indications, precluding mechanism of action correlation.

Query logs demonstrate successful DrugBank retrieval of 1 result (`result_status: success`), indicating that the underlying drug is identifiable in DrugBank and likely corresponds to metformin (biguanide oral antihyperglycaemic agent). However, the admixture of the dosage string "585MG" and extraneous closing parenthesis ")" in the INN field prevented the normalizer and DrugBank mapping pipeline from correctly identifying the drug ID, resulting in both KG and DL prediction steps failing to generate candidate indications.

This problem represents an **upstream data quality issue** and should be remedied at the data-cleaning layer followed by Evidence Pack pipeline re-execution, not at the reporting layer.

---

## Clinical Trial Evidence

No relevant clinical trials are currently available (because predicted indications are absent, corresponding trial queries cannot be executed).

---

## Literature Evidence

No relevant literature is currently available (because predicted indications are absent, corresponding literature queries cannot be executed).

---

## Singapore Market Information

No Singapore HSA registration record exists for this candidate drug.

> **Note:** Metformin is a globally widespread first-line agent for type 2 diabetes mellitus, and Singapore should have a corresponding HSA entry. The anomalous INN field may account for retrieval failure; requerying the HSA database with the correct drug name "metformin" is recommended.

---

## Safety Considerations

See package insert for warnings and precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug INN field "585MG METFORMIN)" is anomalous, causing failure across three processes: prediction pipeline, regulatory retrieval, and safety extraction. This Evidence Pack lacks assessable content.

**To proceed, the following is needed:**

- **Correct the INN field**: Amend "585MG METFORMIN)" to the standard INN "metformin"; trace the data source (original HSA data or preprocessing script) to audit parsing logic and prevent recurrence
- **Obtain DrugBank ID**: DrugBank retrieval has returned 1 result; extract the correct `DB:XXXXXX` ID from that result and populate the Evidence Pack
- **Re-run KG + DL prediction**: Execute `run_kg_prediction.py` with the correct drug ID to obtain the TxGNN indication candidate list
- **Requery HSA registration data**: Requery Singapore HSA registration with "metformin" as key to complete the regulatory section
- **Supplement safety data**: Retrieve Singapore product information leaflet PDF, parse warnings, contraindications, and MOA (to address DG001 and DG002 data gaps)
