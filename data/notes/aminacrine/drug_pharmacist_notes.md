# Aminacrine: From Topical Antiseptic to Paratyphoid Fever

## One-Sentence Summary

Aminacrine (9-aminoacridine) is an acridine-class compound historically used as a topical antiseptic and wound disinfectant.
The TxGNN model predicts it may be effective for **Paratyphoid Fever**,
with **0 clinical trials** and **0 publications** currently supporting this direction — placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical antiseptic / wound disinfection |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 98.26% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Aminacrine in the Evidence Pack. Based on known pharmacological information, Aminacrine is an acridine derivative that acts primarily as a topical antiseptic through DNA intercalation and disruption of microbial cell membranes. Its antibacterial activity is broad-spectrum but has historically been applied only to superficial wounds and skin infections, not systemic infections.

Paratyphoid fever is a systemic enteric infection caused by *Salmonella enterica* serovar Paratyphi (A, B, or C) — a Gram-negative facultative intracellular bacterium. While Aminacrine's acridine scaffold theoretically confers some activity against Gram-negative organisms, the mechanistic link is extremely weak: systemic salmonella infection requires bactericidal concentrations in the bloodstream, liver, and spleen, whereas Aminacrine has never been evaluated or formulated for systemic delivery.

The TxGNN model's high numerical score (98.26%) most likely reflects graph-level associations between acridine-class antibacterials and enteric bacterial disease nodes in the knowledge graph, rather than a direct mechanistic or clinical signal. The complete absence of supporting literature or trials across all 10 predicted indications suggests this is a model artefact driven by drug-class node proximity, not a genuine repurposing signal.

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
This prediction is supported exclusively by a TxGNN knowledge-graph score with zero clinical, preclinical, or mechanistic evidence for Aminacrine in any systemic infectious disease. Paratyphoid fever requires systemic antibiotic therapy (fluoroquinolones, third-generation cephalosporins, or azithromycin), and Aminacrine has no established systemic safety or pharmacokinetic profile to support such an application.

**To proceed, the following is needed:**

- **Establish basic MOA data**: Retrieve Aminacrine's mechanism of action from DrugBank (DB11561) to confirm whether any systemic antibacterial activity has been reported.
- **In vitro MIC data against *Salmonella* Paratyphi**: No in vitro susceptibility data exists; this is the minimum threshold before any further evaluation.
- **Systemic PK/PD profiling**: Aminacrine has only topical use data; oral or parenteral bioavailability, plasma half-life, and tissue distribution are unknown.
- **Regulatory status review**: Confirm whether Aminacrine holds any marketing authorisation globally (not just Singapore) and review associated labelling for systemic use warnings.
- **Knowledge graph audit**: Investigate whether the TxGNN prediction cluster (paratyphoid fever, sinusitis, epiglottitis, periapical diseases all scoring > 0.95) represents a true signal or a shared upstream disease node artefact, as the score distribution strongly suggests the latter.
- **Consider higher-ranked mechanistic candidates first**: Among the 10 predicted indications, apical periodontitis and paranasal sinus neoplasm carry marginally stronger mechanistic rationale and may be better starting points for hypothesis validation.

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*