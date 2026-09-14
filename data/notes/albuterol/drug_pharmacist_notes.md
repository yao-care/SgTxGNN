# Albuterol: Repurposing Evaluation Incomplete — No Predictions Available

## One-Sentence Summary

Albuterol (international nonproprietary name; known as salbutamol in many markets) is a short-acting beta-2 adrenergic agonist widely used for bronchospasm and asthma.
However, the TxGNN pipeline returned **no predicted new indications** for this candidate, and critical data fields — including mechanism of action, safety warnings, and Singapore regulatory records — could not be retrieved.
**This report serves as a data-gap notice; a full repurposing evaluation cannot be completed until the gaps below are resolved.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model produced no output) |
| Singapore Market Status | Not marketed (per query result) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No predicted indication is available in this Evidence Pack; therefore, a mechanism-to-indication bridge analysis cannot be performed.

Additionally, detailed mechanism of action data was not retrieved during this pipeline run. Based on publicly available pharmacological knowledge, albuterol is a selective beta-2 adrenoceptor agonist that relaxes bronchial smooth muscle, but this background context alone is insufficient to anchor a repurposing hypothesis without a TxGNN-scored candidate indication to evaluate.

---

## Singapore Market Information

No Singapore (HSA) drug registrations were found for "ALBUTEROL" in this query. This may reflect a nomenclature mismatch — albuterol is listed as **salbutamol** in most international pharmacopoeias and regulatory databases outside North America. A re-query using "SALBUTAMOL" is recommended before drawing conclusions about local market status.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline returned no candidate indications, and two blocking data gaps (TFDA/HSA package insert warnings and mechanism of action) remain unresolved. There is no actionable repurposing hypothesis to evaluate at this stage.

**To proceed, the following is needed:**

- **Re-query with correct INN**: Re-run the full pipeline using **"SALBUTAMOL"** (the WHO-INN) instead of "ALBUTEROL" to retrieve HSA registrations, TFDA package insert data, and TxGNN predictions correctly.
- **Retrieve MOA from DrugBank**: The DrugBank query returned 1 result (query log ID 2); extract the mechanism of action, pharmacological category, and drug interactions from that record.
- **Retrieve safety data**: Download and parse the TFDA package insert PDF to populate key warnings and contraindications (resolves DG001 — currently Blocking severity).
- **Re-run TxGNN prediction**: Once the drug is correctly identified and mapped, re-execute the KG and DL prediction steps to generate scored candidate indications.
- **Confirm Singapore market status**: After re-querying with "SALBUTAMOL", confirm HSA registration count and approved indications to assess local regulatory baseline.