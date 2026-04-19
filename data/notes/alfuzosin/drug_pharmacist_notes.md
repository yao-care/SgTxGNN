# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective α1-adrenergic receptor antagonist, primarily used to treat benign prostatic hyperplasia (BPH) and hypertension.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita** — a rare genetic condition causing excessive whole-body hair growth —
however, **no clinical trials and no supporting publications** exist for this direction, and the underlying mechanistic rationale is considered weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) / Hypertension (no Singapore registration data available) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on known pharmacological information, Alfuzosin is a selective α1-adrenergic receptor antagonist (alpha-1 blocker). Its established efficacy in benign prostatic hyperplasia relies on relaxing smooth muscle in the prostate and bladder neck, thereby relieving urinary obstruction. It also has a role in hypertension management through peripheral vascular smooth muscle relaxation.

The proposed mechanistic bridge to hair disorders rests on the observation that α1-adrenergic receptors are expressed in the **arrector pili muscles** of hair follicles. Theoretically, blocking α1 signalling could influence the hair follicle cycle. However, Ambras type hypertrichosis universalis congenita is caused by mutations in the **TRPS1 gene** — a zinc-finger transcription factor governing hair follicle development — which has no established direct relationship with adrenergic signalling pathways. The TxGNN model's high confidence score (99.999%) most likely arises from indirect traversal paths within the knowledge graph (e.g., hair disorder nodes connecting through shared adrenergic-related intermediaries) rather than from a genuine therapeutic biology, and should be regarded as **model noise**.

A critical red flag further undermines this prediction: **hypertrichosis (excessive hair growth) has been reported as an adverse effect of Alfuzosin** in clinical use. This suggests that α1 blockade may actively *promote* rather than suppress hair growth, creating a direct pharmacological contradiction with the proposed repurposing rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Alfuzosin is currently **not registered in Singapore**. No marketing authorizations were found in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence supporting Alfuzosin for Ambras type hypertrichosis universalis congenita. The condition is driven by a specific genetic mutation (TRPS1) with no known mechanistic connection to α1-adrenergic blockade, and the paradox that hypertrichosis is itself a reported adverse effect of this drug makes the repurposing rationale logically inconsistent.

**To proceed, the following would be needed:**
- Verified MOA data from DrugBank confirming any hair follicle biology involvement
- Preclinical evidence (e.g., in vitro or animal model data) demonstrating that α1-adrenergic blockade influences TRPS1-associated hair growth pathways
- Resolution of the pharmacological paradox: Alfuzosin causes hypertrichosis as a side effect — any proposed mechanism for treating hypertrichosis must address this contradiction directly
- Singapore HSA package insert data to complete safety screening (currently blocking Step S1 safety assessment)
- If the broader TxGNN candidate list is being reviewed, note that **allergic urticaria** (rank 7) and **persistent fetal circulation syndrome** (rank 8) carry more mechanistically coherent rationales and are classified as "Research Question" rather than "Hold" — these may be more productive targets for hypothesis generation