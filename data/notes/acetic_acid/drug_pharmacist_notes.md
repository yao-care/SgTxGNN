# Acetic Acid: From Antimicrobial Agent to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid (DB03166) is a broad-spectrum antimicrobial compound with a long history of use in wound irrigation, ear canal disinfection, and as a diagnostic reagent (visual inspection with acetic acid, VIA, for cervical lesion detection); no formal therapeutic indication is currently registered in Singapore.
The TxGNN model predicts it may be effective for **Post-Bacterial Disorder**, achieving a prediction score of **99.98%**.
However, supporting evidence is entirely model-based — **0 clinical trials** and **0 publications** directly study acetic acid for this indication, placing the recommendation firmly at **Hold** pending preclinical and mechanistic validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered therapeutic indication (used empirically as antimicrobial/antiseptic and diagnostic agent) |
| Predicted New Indication | Post-Bacterial Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for acetic acid (DB03166). Based on known information, acetic acid is a short-chain carboxylic acid whose primary pharmacological property is broad-spectrum antimicrobial activity. By lowering local pH below 4.5, it disrupts bacterial cell membrane integrity and inhibits essential enzymatic processes, which is why dilute acetic acid solutions have long been used in otitis externa irrigation and chronic wound management. It is also a naturally occurring short-chain fatty acid (SCFA) that, at physiological concentrations in the colon, participates in gut epithelial energy metabolism and immune modulation.

"Post-bacterial disorder" encompasses a heterogeneous group of sequelae arising after resolution of active bacterial infection — including post-infectious irritable bowel syndrome (PI-IBS), reactive arthritis, and dysbiosis-driven systemic inflammation. The theoretical bridge to acetic acid rests on its potential to (1) re-acidify the gut lumen and suppress residual pathobiont overgrowth, (2) restore SCFA-mediated epithelial barrier function disrupted during infection, and (3) exert mild anti-inflammatory signalling through SCFA receptors (GPR41/43). These are mechanistically plausible but entirely speculative links with no direct clinical validation in this indication.

The TxGNN graph neural network derives its high prediction score from structural and topological relationships within the drug–disease knowledge graph rather than from head-to-head experimental evidence. All 18 retrieved clinical trials involve unrelated interventions (microbiota transplantation, berberine, prebiotics, zinc supplementation) or use acetic acid solely as a diagnostic staining agent (VIA), not as a therapeutic compound. The "post-bacterial disorder" disease node itself is broad and heterogeneous, posing a significant challenge for clinical trial design.

---

## Clinical Trial Evidence

> **Note:** All 18 retrieved trials have a relevance grade of "C" — none directly test acetic acid as a therapeutic intervention for post-bacterial disorder. The trials below are listed for contextual awareness only; they involve different agents or use acetic acid solely as a diagnostic tool.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT04120259](https://clinicaltrials.gov/study/NCT04120259) | N/A | Completed | 126 | Apple cider vinegar (contains acetic acid) + metformin vs metformin alone in newly diagnosed Type 2 diabetes — metabolic indication, not post-bacterial disorder |
| [NCT07386795](https://clinicaltrials.gov/study/NCT07386795) | N/A | Not Yet Recruiting | 19 | Microbiota transplantation + prebiotics for functional constipation — gut microbiome relevance but no acetic acid involvement |
| [NCT04434365](https://clinicaltrials.gov/study/NCT04434365) | Phase 1/2 | Unknown | 24 | Berberine effects on gut microbiota and endothelial function in stable coronary artery disease — mechanistically adjacent but unrelated drug |
| [NCT02872675](https://clinicaltrials.gov/study/NCT02872675) | N/A | Completed | 17 | HOST-DM059 prebiotic supplementation on gut bacterial metabolites and systemic inflammation in adults with/without exercise-induced bronchoconstriction |
| [NCT04036318](https://clinicaltrials.gov/study/NCT04036318) | N/A | Completed | 3022 | Presumptive periodic treatment of STIs in high-risk populations in Tanzania — infection topic, but no acetic acid therapeutic use |
| [NCT05965440](https://clinicaltrials.gov/study/NCT05965440) | N/A | Completed | 50 | Dapagliflozin impact on intestinal microbiota in non-diabetic chronic renal failure — microbiome focus, unrelated drug |
| [NCT04657757](https://clinicaltrials.gov/study/NCT04657757) | N/A | Completed | 16 | Bacterial adhesion on implant restoration materials ex vivo — no acetic acid, diagnostic/materials science |
| [NCT04824261](https://clinicaltrials.gov/study/NCT04824261) | N/A | Unknown | 100 | 4% boric acid vs clotrimazole for otomycosis — acid-based antimicrobial comparator but different compound |
| [NCT03212729](https://clinicaltrials.gov/study/NCT03212729) | N/A | Completed | 10 | Antimicrobial photodynamic therapy as adjunct to endodontic treatment — physical therapy, no acetic acid |
| [NCT05275647](https://clinicaltrials.gov/study/NCT05275647) | Phase 2 | Unknown | 75 | Low energy shock wave + botulinum toxin A for refractory interstitial cystitis — post-infectious bladder sequelae context, but no acetic acid |

---

## Literature Evidence

Currently no related literature available for acetic acid specifically in post-bacterial disorder.

---

## Singapore Market Information

Acetic acid (DB03166) currently has **no registered products** in Singapore (HSA licenses = 0). It is not approved as a pharmaceutical product under any therapeutic indication in this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data gaps were identified: TFDA label warnings/contraindications (Blocking severity) and drug interaction profile were not retrievable in this Evidence Pack. Before any clinical or regulatory consideration, these must be obtained from the relevant regulatory authority and DrugBank API.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting acetic acid in post-bacterial disorder is entirely computational (L5) — the TxGNN model's high score reflects knowledge graph topology, not mechanistic or clinical validation. None of the 18 retrieved clinical trials directly investigate acetic acid therapeutically in this indication, and no supporting literature exists. Additionally, "post-bacterial disorder" as a disease category is insufficiently defined for clinical trial operationalisation.

**To proceed, the following is needed:**

- **Define the target indication precisely:** Specify which post-bacterial disorder subtype (e.g., PI-IBS, reactive arthritis, post-infectious dysbiosis) is the intended focus, as each has distinct pathophysiology
- **Obtain MOA data:** Query DrugBank API for acetic acid's pharmacodynamic and pharmacokinetic profile to establish or refute a mechanistic link
- **Retrieve safety data:** Download and parse TFDA/HSA package insert PDF to identify contraindications, key warnings, and drug interactions
- **Conduct preclinical assessment:** Identify or commission animal model studies demonstrating acetic acid activity in post-bacterial disease models before human studies are considered
- **Clarify formulation and route:** Determine what formulation (oral, topical, rectal) and dose would be pharmacologically relevant for the intended indication
- **Benchmark against tinea corporis (Rank 9):** Among all 10 predicted indications, tinea corporis is the only one reaching L4 evidence (with 1 RCT and multiple supporting publications including historical series on acetic acid in dermatophytosis), and may represent a more actionable repurposing candidate for near-term investigation

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*