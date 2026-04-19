# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is a neurokinin-1 (NK1) receptor antagonist primarily used for the prevention of chemotherapy-induced nausea and vomiting (CINV) and postoperative nausea and vomiting (PONV). The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, a rare genetic disorder causing inappropriate water retention and hyponatremia. Currently, **no clinical trials** and **no published literature** support this specific application, making this an entirely model-driven hypothesis requiring substantial preclinical validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of chemotherapy-induced nausea and vomiting (CINV) and postoperative nausea and vomiting (PONV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Aprepitant is a selective NK1 (neurokinin-1) receptor antagonist that competitively blocks Substance P binding in central and peripheral neurons. Its proven efficacy in preventing CINV and PONV has been established through this Substance P / NK1 receptor pathway, particularly in the nucleus tractus solitarius and area postrema of the brainstem.

Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is a rare X-linked genetic disorder caused by gain-of-function mutations in the *AVPR2* gene encoding the renal vasopressin V2 receptor. Unlike SIADH, it presents with persistent hyponatremia and inappropriately concentrated urine in the absence of elevated arginine vasopressin (AVP). The underlying defect is constitutive receptor activation — a fundamentally different disease mechanism from neuropeptide-mediated signaling. The pharmacological link between NK1 antagonism and AVPR2 gain-of-function remains highly speculative, with no established pathway connecting Substance P signaling to V2 receptor constitutive activity.

The TxGNN model's high-confidence prediction for this pairing most likely reflects indirect topological proximity within the knowledge graph (e.g., shared disease ontology nodes or co-occurring drug targets) rather than a direct mechanistic connection. While NK1 receptors have been identified in renal tubular tissue and may play minor modulatory roles in sodium and water handling, there is currently no mechanistic chain linking NK1 blockade to the resolution of *AVPR2* constitutive activation. This prediction should be treated as a hypothesis-generating signal requiring dedicated preclinical investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Aprepitant has no registered products in Singapore. There are currently **0 active authorizations** on record, and the drug is classified as **not marketed** in this market.

> Note: Aprepitant (brand name Emend®) is approved by the US FDA and EMA for CINV/PONV prevention and is available in multiple markets, but no Singapore Health Sciences Authority (HSA) registration has been identified in this data set. Regulatory status should be independently verified via the HSA Product Register before any procurement or clinical planning.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on data gaps:** This evidence pack is missing two critical data elements that are required before any further evaluation can proceed:
> - **Package insert warnings and contraindications** (Severity: Blocking — needed for S1 safety screening)
> - **Mechanism of action detail** (Severity: High — needed for mechanistic relevance analysis)
>
> These gaps should be resolved by downloading the official product monograph from the US FDA, EMA, or TFDA before this candidate advances.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on TxGNN model inference. There are no registered clinical trials, no published literature linking Aprepitant to NSIAD, and no established mechanistic pathway connecting NK1 receptor antagonism to *AVPR2* gain-of-function mutations. The evidence level (L5) and the absence of a credible mechanistic rationale do not support further investment at this stage.

**Notable observation from the full prediction list:**
Among all 10 predicted indications, **subarachnoid hemorrhage (SAH)** (rank 9, score 99.85%) carries the most scientifically credible mechanistic rationale: Substance P is massively released following SAH and acts via NK1 receptors to drive cerebral vasospasm, neuroinflammation, and blood-brain barrier breakdown. Animal models have shown NK1 antagonists can attenuate post-SAH vasospasm. Aprepitant's established CNS penetrance makes it a pharmacologically eligible candidate. While SAH ranked lower in TxGNN score, it is the most scientifically compelling target in this list and may warrant prioritization for a dedicated literature and preclinical review.

**To proceed with any indication, the following is needed:**

- [ ] Resolve DG001: Obtain and review the full product monograph (warnings, contraindications, precautions) from an authorised regulatory source
- [ ] Resolve DG002: Confirm complete pharmacological MOA from DrugBank or primary literature
- [ ] Conduct drug-drug interaction profiling (current DDI data is empty)
- [ ] For NSIAD specifically: Commission a targeted literature search on NK1 receptor involvement in renal tubular water and sodium handling
- [ ] For NSIAD specifically: Evaluate feasibility of in vitro or animal model studies with *AVPR2* gain-of-function constructs
- [ ] Consider redirecting primary evaluation effort toward **subarachnoid hemorrhage** (rank 9), which has a substantially stronger mechanistic basis and represents a high unmet clinical need

---

*This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*