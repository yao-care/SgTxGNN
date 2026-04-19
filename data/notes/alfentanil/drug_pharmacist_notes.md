# Alfentanil: From Anaesthesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Alfentanil is an ultra-short-acting μ-opioid receptor agonist administered intravenously as an analgesic adjunct during general anaesthesia and procedural sedation.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
yet **no clinical trials and no publications** currently support this direction — evidence sits at the lowest possible tier.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Intravenous analgesia and anaesthesia adjunct (opioid analgesic) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on established pharmacology, Alfentanil is a potent, ultra-short-acting μ-opioid receptor agonist (redistribution half-life ~1 min) administered intravenously for the induction and maintenance of anaesthesia as well as procedural analgesia. Its primary mechanism involves binding to μ-opioid receptors in the central nervous system — particularly in the spinal dorsal horn, brainstem, and periaqueductal grey — to suppress nociceptive transmission and produce sedation.

NSIAD is a channelopathy caused by gain-of-function mutations in the *AVPR2* gene (arginine vasopressin receptor type 2), resulting in constitutive receptor activation independent of vasopressin binding. This leads to inappropriate water retention, euvolaemic hyponatraemia, and can be clinically indistinguishable from SIADH except that it does not respond to V2-receptor antagonists (vaptans). The disease driver is a permanently activated AVPR2 receptor, not a pain-signalling or opioid-receptor pathway.

While opioid receptor agonism is known to modulate ADH secretion indirectly through hypothalamic pathways, this effect is entirely upstream of the constitutively active AVPR2 mutation and cannot antagonise or correct the underlying receptor dysfunction. The TxGNN high score (99.51%) most likely reflects indirect graph traversals between water-electrolyte imbalance nodes and CNS pharmacology nodes in the knowledge graph rather than a biologically coherent mechanism. Mechanistic plausibility for this specific repurposing prediction is assessed as very low.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Alfentanil is not registered in Singapore. No regulatory authorisation records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on the TxGNN model score (L5 evidence); there are no clinical trials, no published literature, and no established mechanistic pathway linking μ-opioid receptor agonism to the AVPR2 gain-of-function mutations that drive NSIAD.

**To proceed, the following is needed:**
- Preclinical evidence (in vitro or animal models) demonstrating any functional interaction between opioid signalling and AVPR2 constitutive activity
- A coherent mechanistic hypothesis explaining how Alfentanil could modulate NSIAD pathophysiology beyond indirect ADH modulation
- Mechanism of action data from DrugBank (Data Gap DG002)
- Singapore package insert and warnings review to complete the safety profile (Data Gap DG001)
- Expert pharmacologist and nephrologist review before any further development of this candidate