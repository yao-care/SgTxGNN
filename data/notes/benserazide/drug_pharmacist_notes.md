# Benserazide: From Parkinson's Disease (Adjunctive) to Congenital Hypotrichosis Milia

## One-Sentence Summary

Benserazide is a peripheral aromatic L-amino acid decarboxylase (AADC) inhibitor, used in combination with levodopa (e.g., Madopar®) to enhance central dopaminergic therapy in Parkinson's disease and related movement disorders.
The TxGNN model predicts it may be effective for **Congenital Hypotrichosis Milia**, with **0 clinical trials** and **0 publications** currently supporting this direction — representing the lowest possible evidence classification.
Across all 10 predicted indications, existing literature skews toward adverse signals rather than therapeutic evidence, warranting a full Hold recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; pharmacologically recognised as Parkinson's disease adjunct (peripheral AADC inhibitor in levodopa combinations) |
| Predicted New Indication | Congenital Hypotrichosis Milia |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Benserazide is a peripheral AADC inhibitor typically administered alongside levodopa. By blocking peripheral conversion of levodopa to dopamine, Benserazide increases the fraction of levodopa that crosses the blood–brain barrier, amplifying central dopaminergic effects in Parkinson's disease and related dopamine-deficient conditions.

Congenital hypotrichosis milia is a rare genetic disorder characterised by structural abnormalities of hair follicles present from birth. While the catecholamine/dopamine signalling pathway has a very weak and indirect role in hair follicle biology, whether peripheral AADC inhibition meaningfully affects congenital hair follicle development is entirely unknown. This disease category is driven by structural gene defects, not enzymatic dysregulation of the AADC pathway.

The mechanistic connection between Benserazide's AADC inhibition and congenital hypotrichosis is highly speculative. The elevated TxGNN prediction score most likely reflects topological proximity among hair disease nodes within the knowledge graph, rather than any genuine pharmacological relationship. No preclinical or clinical evidence supports this repurposing direction at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Benserazide holds no active drug registrations in Singapore (0 licenses). The drug is available in other markets exclusively as part of fixed-dose levodopa/benserazide combination products (e.g., Madopar® 125, Madopar® HBS). No standalone benserazide product is registered anywhere in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** A 1979 clinical observation (PMID 554794) directly documents that benserazide administration induced migraine attacks in migrainous women, independent of prolactin elevation. This constitutes a meaningful adverse signal relevant to any head pain–related predicted indication (ranks 7 and 9 in this Evidence Pack). Additionally, hair loss is a recognised side effect of levodopa/benserazide combination therapy — directly contradicting the predicted hair loss treatment indications (ranks 1–4). These adverse signals should be factored into any future safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are classified at Evidence Level L5 (model prediction only, no supporting studies), and the sparse literature identified across predictions is predominantly adverse signal — benserazide has been documented to *induce* migraine and *cause* alopecia as side effects — directly undermining the plausibility of the top-ranked predicted indications.

**To proceed, the following is needed:**

- **MOA data**: Retrieve benserazide mechanism-of-action details from DrugBank API (DG002 remediation) to establish any theoretical basis for hair follicle or oncology indications
- **Safety package**: Obtain Singapore HSA / TFDA package insert to formally assess warnings and contraindications (DG001 remediation; currently Blocking severity)
- **Preclinical validation**: Commission wet-laboratory studies examining AADC inhibition in hair follicle biology before advancing any hypotrichosis hypothesis
- **Oncology signal clarification**: The DHODH/pyrimidine synthesis mechanism proposed for small intestine and duodenum cancers (ranks 5–6) originates from external literature not included in this Evidence Pack; a targeted literature review (Li et al., 2019, *Nature Communications*) is needed to assess whether it extends beyond colorectal cancer models
- **Pheochromocytoma feasibility assessment**: AADC activity elevation in phaeochromocytoma is biochemically documented (PMID 3769207), but the clinical relevance of AADC inhibition as a therapeutic strategy against catecholamine-secreting tumours requires dedicated molecular pathology review before any research investment
- **Model audit**: The clustering of four hair disease indications at the top of the ranked list (ranks 1–4), combined with known adverse hair loss effects of benserazide, suggests possible systematic overprediction in this disease cluster by TxGNN; a knowledge graph topology audit is recommended