# Azacitidine: From Myelodysplastic Syndromes to Bulbar Polio

## One-Sentence Summary

Azacitidine is a hypomethylating agent (HMA) established globally for treating myelodysplastic syndromes (MDS) and acute myeloid leukemia (AML), though it is not currently registered in Singapore.
The TxGNN model's top-ranked new indication is **Bulbar Polio**,
with **0 clinical trials** and **0 publications** supporting this direction — making this a model-only prediction most likely driven by knowledge-graph topology rather than pharmacological relevance.
Among all 10 predicted indications, haematological conditions — particularly **Aregenerative Anemia** (27 trials, 20 publications, L2) and **Unclassified MDS** (L3) — carry substantially stronger mechanistic and clinical support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Myelodysplastic syndromes (MDS), acute myeloid leukemia (AML) — globally approved, not registered in Singapore |
| Predicted New Indication (TxGNN #1) | Bulbar Polio |
| TxGNN Prediction Score | 98.59% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not provided in this evidence pack. Based on established pharmacology, Azacitidine is a pyrimidine nucleoside analogue that acts as a DNA methyltransferase (DNMT) inhibitor. After incorporation into replicating DNA, it covalently traps DNMT enzymes and causes progressive genome-wide demethylation. This reverses the aberrant epigenetic silencing of tumour suppressor genes and restores normal haematopoietic differentiation — the biological basis for its efficacy in clonal myeloid disorders such as MDS and AML.

Bulbar polio is an acute, life-threatening form of poliomyelitis in which poliovirus directly infects brainstem motor nuclei, causing cranial nerve palsy, respiratory failure, and dysphagia. Its pathophysiology is fundamentally viral-cytolytic and neuroinflammatory: poliovirus enters motor neurons via CD155 receptor binding, replicates intracellularly, and destroys the cells. There is no established epigenetic driver in bulbar polio that azacitidine's DNMT inhibition could plausibly address.

The TxGNN score of 98.59% for bulbar polio most likely reflects structural proximity between neurological disease nodes and haematology-drug nodes within the knowledge graph — not a pharmacological relationship. This is a well-documented limitation of graph neural network models, where topological closeness does not reliably indicate therapeutic relevance. This prediction is assessed as a **knowledge-graph topology artefact** and does not represent a credible repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Azacitidine in Bulbar Polio.

---

## Literature Evidence

Currently no related literature available for Azacitidine in Bulbar Polio.

---

## Singapore Market Information

Azacitidine is not registered in Singapore. No HSA marketing authorisations are on record.

> **Note:** Azacitidine (brand names Vidaza/Onureg) holds FDA approval (2004) and EMA approval for MDS, AML, and CMML in the United States and Europe respectively, but has not obtained Singapore HSA registration. Prescribing information and Singapore-specific safety data are therefore unavailable from this data pack.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Hypomethylating agent / Pyrimidine nucleoside analogue (antimetabolite class) |
| Myelosuppression Risk | **High** — Neutropenia, thrombocytopenia, and anaemia are the most frequent dose-limiting toxicities, occurring in the majority of patients after each treatment cycle; febrile neutropenia is a serious complication |
| Emetogenicity Classification | Low to moderate (per MASCC/ESMO antiemesis guidelines for subcutaneous/IV azacitidine) |
| Monitoring Items | CBC with differential (before each cycle and as clinically indicated); liver function tests (ALT, AST, total bilirubin); renal function (serum creatinine, BUN); serum electrolytes |
| Handling Protection | Cytotoxic precautions required: prepare in a biological safety cabinet; wear gloves, gown, and eye protection; follow institutional cytotoxic waste disposal protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Bulbar polio has no clinical, mechanistic, or epidemiological basis for azacitidine treatment, and the TxGNN #1 ranking reflects a knowledge-graph topology effect rather than a credible pharmacological hypothesis.

**To proceed with any azacitidine repurposing evaluation, the following is needed:**
- Redirect focus to haematological indications with established evidence (see full summary below)
- Obtain Singapore HSA prescribing information or the original product package insert to complete the safety and contraindication assessment (currently a blocking data gap)
- Confirm full mechanism of action from DrugBank (currently missing) to support mechanistic link analysis for actionable indications
- Assess regulatory pathway feasibility for Singapore HSA registration, as the drug is currently unregistered

---

## All Predicted Indications — Complete Summary

Ten indications were evaluated in this evidence pack. The table below provides a full prioritisation overview.

| Rank | Indication | TxGNN Score | Trials | Publications | Evidence Level | Recommendation |
|------|-----------|:-----------:|:------:|:------------:|:--------------:|:--------------:|
| 1 | Bulbar Polio | 98.59% | 0 | 0 | L5 | Hold |
| 2 | Refractory Cytopenia of Childhood | 98.20% | 1 | 5 | L3 | Proceed with Guardrails |
| 3 | Unclassified Myelodysplastic Syndrome | 98.10% | 1 | 8 | L3 | Proceed with Guardrails |
| 4 | Partial Deletion of Long Arm of Chr. 5 (del 5q) | 97.88% | 0 | 0 | Pending | Pending |
| 5 | Aregenerative Anemia | 97.88% | 27 | 20 | L2 | Proceed with Guardrails |
| 6 | Severe Congenital Hypochromic Anemia w/ Ringed Sideroblasts | 97.56% | 0 | 0 | L4 | Research Question |
| 7 | 5q35 Microduplication Syndrome | 97.48% | 0 | 0 | L5 | Hold |
| 8 | Neuralgic Amyotrophy | 96.20% | 0 | 0 | L5 | Hold |
| 9 | Amyotrophic Neuralgia | 95.87% | 0 | 0 | L5 | Hold |
| 10 | Familial Thrombocytosis | 93.09% | 0 | 0 | L5 | Hold |

### Priority Indication: Aregenerative Anemia (Rank 5, L2)

**Aregenerative Anemia** stands out as the most evidence-supported actionable indication with **27 clinical trials** and **20 publications**, including major Phase 2/3 studies (e.g., NCT00454480, N=2,000, elderly AML/high-risk MDS; NCT01928537, Phase 3 MDS with excess blasts; NCT02158936, Phase 3 eltrombopag + azacitidine). Azacitidine's demethylating mechanism directly addresses the haematopoietic stem cell dysfunction underlying MDS-associated aregenerative anaemia. A translational study ([PMID 34781359](https://pubmed.ncbi.nlm.nih.gov/34781359/)) further demonstrated direct azacitidine activity in X-linked sideroblastic anaemia via ALAS2 gene re-expression, extending the mechanistic argument to non-MDS causes of bone marrow failure. **Recommendation: advance this indication to detailed evaluation under "Proceed with Guardrails" at L2.**

**Unclassified MDS (Rank 3)** and **Refractory Cytopenia of Childhood (Rank 2)** are also worth co-evaluating — both fall within the MDS disease spectrum where azacitidine has the most established pharmacological rationale, and the AVIDA registry (PMID 24956145, N=421 including 86 unclassified MDS) provides real-world effectiveness data directly relevant to MDS-U.

Indications at ranks 7–9 (5q35 microduplication syndrome, neuralgic amyotrophy, amyotrophic neuralgia) are assessed as low-plausibility predictions with no supporting evidence and should not be pursued.

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.