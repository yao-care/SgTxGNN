# Infliximab: From Autoimmune Inflammatory Disease to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Infliximab is a chimeric anti-TNF-α monoclonal antibody with established global approvals for rheumatoid arthritis, Crohn's disease, ankylosing spondylitis, psoriatic arthritis, ulcerative colitis, and plaque psoriasis, but is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, an ultra-rare congenital developmental disorder.
**No clinical trials or published literature** currently support this predicted direction, making this a model-only prediction with no supporting biological rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Globally approved for RA, Crohn's disease, ankylosing spondylitis, psoriatic arthritis, ulcerative colitis, and plaque psoriasis; not registered in Singapore |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 90.22% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not captured in this Evidence Pack. Based on widely established clinical pharmacology, Infliximab is a chimeric human-murine IgG1κ monoclonal antibody that binds with high affinity to both soluble and transmembrane forms of TNF-α, neutralizing its pro-inflammatory biological activity and preventing binding to TNF receptors. This mechanism underlies its efficacy across multiple TNF-α–driven autoimmune conditions.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is an ultra-rare congenital disorder caused by pathogenic variants in genes such as *ALDH18A1* and *PAX6*, leading to structural developmental defects manifest as ocular coloboma/microphthalmia combined with rhizomelic limb shortening. This is a structural embryonic dysplasia rooted in disrupted transcription factor and metabolic enzyme function during organogenesis—not an inflammatory or immune-mediated process.

The TxGNN score of 90.22% most likely reflects topological proximity within the knowledge graph (e.g., shared node neighbors through connective tissue or rare disease pathways) rather than any genuine biological link between TNF-α inhibition and this syndrome's pathogenesis. No known mechanistic connection exists between TNF-α signaling and *ALDH18A1*/*PAX6* developmental pathway dysfunction, and zero preclinical or clinical evidence currently supports this repurposing direction. This prediction should be interpreted as a knowledge graph topology artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Infliximab is currently not registered with Singapore's Health Sciences Authority (HSA). No marketing authorization licenses exist in the Singapore regulatory database at the time of this analysis (data cutoff: 2026-04-04).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| — | No registrations found | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a structural congenital developmental disorder with no established connection to TNF-α–mediated inflammation; the elevated TxGNN score reflects knowledge graph topology rather than biological plausibility, and zero supporting evidence exists at any level (L5).

**To proceed, the following is needed:**
- Preclinical mechanistic studies to investigate whether TNF-α signaling plays any role in *ALDH18A1* or *PAX6* developmental pathway regulation
- Infliximab full MOA documentation (source: DrugBank API) to identify any off-target activities theoretically relevant to structural dysplasias
- Singapore HSA regulatory submission data to clarify pathway for market access if future evidence emerges
- Reassessment using graph explainability tools (e.g., attention weights or edge attribution) to identify which KG edges are driving this high-score prediction