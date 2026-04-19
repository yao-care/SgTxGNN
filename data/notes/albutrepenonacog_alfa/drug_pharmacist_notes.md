# Albutrepenonacog alfa: From Hemophilia B to Pseudo-von Willebrand Disease

## One-Sentence Summary

Albutrepenonacog alfa (rIX-FP) is a recombinant Factor IX albumin fusion protein designed to provide long-acting coagulation factor replacement for Hemophilia B (congenital Factor IX deficiency).
The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**,
however there are currently **0 clinical trials** and **0 publications** supporting this direction, and the mechanistic rationale is assessed as extremely weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia B (congenital Factor IX deficiency) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, Albutrepenonacog alfa is a recombinant human Factor IX fused to human serum albumin (rIX-FP), engineered to extend the circulating half-life of Factor IX to approximately 104 hours—roughly 5-fold longer than standard Factor IX concentrates. This enables once-weekly or less frequent prophylactic dosing in patients with Hemophilia B, where Factor IX activity is congenitally absent or severely reduced, impairing the intrinsic coagulation pathway (Xase complex: FIXa + FVIIIa → FXa).

Pseudo-von Willebrand disease (platelet-type vWD) is caused by a gain-of-function mutation in GPIbα on the platelet surface, which creates abnormally high affinity for von Willebrand Factor (vWF). This leads to spontaneous platelet-vWF binding, resulting in platelet aggregation and selective consumption of high-molecular-weight vWF multimers. The pathological mechanism operates entirely within the primary hemostasis axis (platelet/vWF interaction), and is structurally and functionally distinct from the coagulation cascade where Factor IX functions.

Mechanistic relevance is **extremely low**: supplementing Factor IX cannot correct GPIbα gain-of-function abnormalities, replace consumed vWF multimers, or prevent spontaneous platelet aggregation. The TxGNN model's high prediction score (99.94%) most likely reflects shared rare bleeding disorder ontology in the knowledge graph rather than true mechanistic or therapeutic overlap. Among all 10 predicted indications in this analysis, only **acquired coagulation factor deficiency** (Rank 7) carries a meaningful mechanistic link to Factor IX replacement therapy, as it may encompass acquired Factor IX deficiency (e.g., in systemic amyloidosis).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pseudo-von Willebrand disease.

---

## Literature Evidence

Currently no related literature available for pseudo-von Willebrand disease.

---

## Singapore Market Information

Albutrepenonacog alfa is currently **not registered** in Singapore. No HSA-authorised products containing this active substance have been identified. This drug is therefore not commercially available through standard regulatory channels in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.94%), pseudo-von Willebrand disease involves a primary hemostasis defect in GPIbα/vWF interaction that is mechanistically orthogonal to Factor IX replacement therapy; there is no clinical, preclinical, or biological rationale supporting this repurposing direction, and no supporting evidence exists.

**To proceed, the following is needed:**

- Obtain and review the full prescribing information (package insert) for Albutrepenonacog alfa (Idelvion, CSL Behring) to confirm the approved indication, key warnings, and contraindications — this is currently a **Blocking** data gap
- Retrieve the complete mechanism of action from DrugBank (DB13884) to enable formal mechanistic analysis — currently a **High** severity data gap
- Redirect repurposing evaluation to **Acquired Coagulation Factor Deficiency** (Rank 7), which has the strongest mechanistic justification among all predicted candidates, as acquired Factor IX deficiency (e.g., amyloidosis-associated) represents a direct biological parallel to the approved Hemophilia B indication
- Before any further evaluation of the remaining candidates, conduct a mechanistic triage review — note that **inherited thrombophilia** (Rank 10) and **thrombotic thrombocytopenic purpura** (Rank 8) represent potentially **contraindicated** directions where Factor IX supplementation could theoretically worsen thrombotic risk
- Register Albutrepenonacog alfa with HSA Singapore if the primary Hemophilia B indication is commercially relevant, as the drug is currently not marketed in Singapore