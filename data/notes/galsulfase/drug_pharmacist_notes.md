# Galsulfase: From Mucopolysaccharidosis VI to Ptosis-Strabismus-Ectopic Pupils Syndrome

## One-Sentence Summary

Galsulfase (brand name: Naglazyme) is a recombinant enzyme replacement therapy (ERT) approved for Mucopolysaccharidosis Type VI (MPS VI, Maroteaux-Lamy syndrome), a rare lysosomal storage disorder caused by deficiency of the enzyme N-acetylgalactosamine-4-sulfatase (ARSB).
The TxGNN model predicts it may be effective for **Ptosis-Strabismus-Ectopic Pupils Syndrome**, yet currently there are **no clinical trials** and **no publications** supporting this specific direction.
The mechanistic rationale is weak, and this prediction warrants a Hold decision pending further biological justification.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucopolysaccharidosis VI (MPS VI / Maroteaux-Lamy syndrome) |
| Predicted New Indication | Ptosis-Strabismus-Ectopic Pupils Syndrome |
| TxGNN Prediction Score | 97.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on publicly known information, Galsulfase is a recombinant form of arylsulfatase B (ARSB, also known as N-acetylgalactosamine-4-sulfatase), the lysosomal enzyme that is deficient in MPS VI patients. By replacing this enzyme intravenously, Galsulfase enables the breakdown of dermatan sulfate — a glycosaminoglycan (GAG) that otherwise accumulates in tissues throughout the body, causing progressive multisystem organ damage. Its clinical efficacy in MPS VI has been established through controlled trials leading to FDA and EMA approval.

Ptosis-strabismus-ectopic pupils syndrome is a rare congenital disorder characterised by structural and neuromuscular abnormalities of the eye: drooping upper eyelids (ptosis), ocular misalignment (strabismus), and abnormally positioned pupils (ectopic pupils). These features arise from developmental defects — abnormal neural crest cell migration, extraocular muscle maldevelopment, or sphincter pupillae structural anomalies — rather than from the lysosomal accumulation of GAG substrates.

The TxGNN model's high score (97.89%) most likely reflects an indirect statistical association in the knowledge graph: MPS VI patients do develop secondary ocular manifestations (e.g., corneal clouding, glaucoma, and periorbital soft tissue deposition), which co-occur with Galsulfase treatment records. This creates a graph-level link between Galsulfase and eye conditions in general. However, this represents co-occurrence rather than mechanistic relevance — the structural deficits that define ptosis-strabismus-ectopic pupils syndrome are not caused by ARSB deficiency and cannot be reversed by enzyme replacement. There is no known biological pathway connecting dermatan sulfate catabolism to the correction of congenital ocular structural anomalies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is classified as L5 — TxGNN model prediction only, with zero clinical trials, zero supporting publications, and no credible mechanistic link between Galsulfase's ARSB enzyme replacement action (targeting dermatan sulfate catabolism) and the developmental-structural pathophysiology of ptosis-strabismus-ectopic pupils syndrome. The high model score most likely reflects indirect graph associations from MPS VI ocular co-morbidities, not a genuine drug–disease causal relationship.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve full DrugBank entry for DB01279 to formally document ARSB substrate specificity and confirm the absence of any pleiotropic mechanism relevant to ocular structural development
- **Package insert review**: Obtain the Naglazyme SmPC/PI to document approved warnings, contraindications, and infusion-related adverse events
- **Biological hypothesis generation**: A biologically plausible hypothesis must be articulated before any further investigation — e.g., whether excess dermatan sulfate in MPS VI could secondarily impair extraocular muscle development or neural crest migration in a way that resembles the target syndrome
- **Broader candidate review**: Among the 10 TxGNN predictions evaluated, Scheie syndrome (rank 10; MPS I) is biologically closer to MPS VI and supported by 4 ERT-related review publications (PMIDs: 22210671, 21211680, 20040314, 20040319) — this candidate merits a separate, focused assessment as a higher-priority repurposing signal than rank 1

> **Research disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.