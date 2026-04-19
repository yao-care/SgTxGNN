# Iodixanol: From Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol (Visipaque) is a non-ionic, iso-osmolar iodinated contrast agent used in vascular and body cavity imaging — it is a diagnostic tool, not a conventional therapeutic drug.
The TxGNN model predicts it may be effective for **Osteoarthritis Susceptibility**, with **0 clinical trials** and **0 publications** directly supporting this therapeutic direction.
The evidence level is L5 (model prediction only), and the current recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iodinated contrast agent for medical imaging |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Iodixanol is a non-ionic, iso-osmolar (290 mOsm/kg) iodinated radiographic contrast agent — its "mechanism" is fundamentally physical rather than pharmacological. Iodine atoms absorb X-rays, providing contrast in imaging procedures. The drug has no established anti-inflammatory, chondroprotective, or disease-modifying pathway relevant to osteoarthritis or its genetic susceptibility.

The TxGNN knowledge graph most likely established a strong association between Iodixanol and osteoarthritis-related nodes because the drug is routinely used in musculoskeletal imaging — including arthrography, contrast-enhanced CT of joints, and cartilage composition assessment studies. This represents a co-occurrence pattern in the medical literature (imaging tool deployed alongside OA research), not a therapeutic mechanism. Second-ranked literature evidence (for the related "osteoarthritis" indication, rank 2) confirms this interpretation: all seven retrieved publications use Iodixanol as a diagnostic or biomechanical research tool — measuring solute transport across cartilage, assessing cartilage structure, or evaluating contrast safety in joint infiltration — not as a treatment.

"Osteoarthritis susceptibility" specifically refers to genetic or biological predisposition to developing OA, involving loci such as GDF5 and ALDH1A2. There is no known pharmacological interaction between Iodixanol and these susceptibility pathways. The high TxGNN score most likely reflects knowledge graph cluster effects within the musculoskeletal disease node group rather than any genuine drug-disease mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note:** For the closely related indication "osteoarthritis" (rank 2 prediction), 7 publications were retrieved — however, all use Iodixanol exclusively as a diagnostic imaging agent or research tool (solute transport studies, cartilage CT assessment), with no therapeutic intent. These do not constitute drug repurposing evidence.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Iodixanol is a diagnostic contrast agent with no established therapeutic mechanism relevant to osteoarthritis susceptibility or any of the 10 predicted musculoskeletal indications. The TxGNN high scores most likely reflect a systematic knowledge graph artefact: because Iodixanol is widely used in joint and bone imaging, the KG places it in close proximity to musculoskeletal disease nodes — creating the appearance of a drug-disease relationship where only a tool-disease co-occurrence exists. There is zero clinical trial evidence, zero therapeutic-intent literature, and no biological rationale supporting further development.

**To revisit this candidate, the following would be needed:**

- A mechanistic hypothesis explaining how Iodixanol could modify OA susceptibility beyond its contrast imaging role (none currently exists)
- Preclinical (in vitro / in vivo) data demonstrating any chondroprotective or disease-modifying effect
- Clarification of whether TxGNN scoring correctly distinguishes diagnostic co-occurrence from therapeutic signal — this case suggests a systematic recalibration may be warranted for contrast agents across the entire model output
- Singapore regulatory package insert to formally document contraindications and warnings (currently a blocking data gap)

> ⚠️ **Research Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.