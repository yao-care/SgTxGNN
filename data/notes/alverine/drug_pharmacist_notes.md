# Alverine: From Irritable Bowel Syndrome to Dysthymic Disorder

## One-Sentence Summary

Alverine is an antispasmodic agent primarily used for irritable bowel syndrome (IBS) and gastrointestinal spasms, acting as a smooth muscle relaxant.
The TxGNN model predicts it may be effective for **Dysthymic Disorder** (persistent depressive disorder), achieving the highest prediction score (99.83%) in this analysis.
However, **no clinical trials and no direct publications** currently support this specific direction; the most evidence-supported indication in this prediction set is **anxiety disorder** (rank #3), backed by one preclinical animal study and one indirectly related clinical trial.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Irritable bowel syndrome (IBS) / Gastrointestinal spasms (antispasmodic) |
| Predicted New Indication | Dysthymic Disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Alverine is an antispasmodic agent whose primary action involves smooth muscle relaxation in the gastrointestinal tract, making it effective for IBS-related cramping and spasms. However, a 2014 preclinical study (PMID 25199966) demonstrated **anxiolytic-like effects of alverine citrate in mouse models**, proposing a serotonergic mechanism — specifically partial agonism or antagonism at the **5-HT1A receptor**. The 5-HT1A receptor is the primary pharmacological target of buspirone, a first-line anxiolytic, and plays a well-established role in the neurobiology of both anxiety and depressive spectrum disorders, including dysthymia.

The connection between IBS and psychiatric conditions is well-documented via the **gut-brain axis**: IBS patients have significantly elevated rates of comorbid anxiety and depression, including dysthymic disorder. Serotonin is a key neuromodulator in both GI motility and mood regulation, meaning a drug with dual peripheral (GI) and central (CNS) serotonergic activity could theoretically bridge these two domains. This mechanistic overlap likely drives the high TxGNN prediction score for dysthymia and related neuropsychiatric indications.

That said, the link between Alverine's antispasmodic use and dysthymic disorder remains **highly speculative**. The animal evidence for anxiolytic activity is preclinical only, and no human data exist for any psychiatric indication. The TxGNN model's high score for dysthymic disorder (rank #1) most likely reflects dense knowledge-graph connectivity through shared serotonergic pathway nodes, rather than direct biological validation. Researchers should treat this prediction as a hypothesis-generating signal requiring prospective experimental confirmation.

---

## Clinical Trial Evidence

Currently no clinical trials related to **dysthymic disorder** are registered for Alverine.

> **Note:** The only identified clinical trial in this evidence set, [NCT00934973](https://clinicaltrials.gov/study/NCT00934973), investigates Alverine in the context of **IBS** (not dysthymic disorder). It is listed here for reference as indirect contextual evidence:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00934973](https://clinicaltrials.gov/study/NCT00934973) | Phase 4 | Completed | 135 | Feasibility RCT comparing mebeverine (antispasmodic, same class as Alverine), methylcellulose, placebo, and a CBT-based self-management website for IBS in UK primary care. Primary endpoint was IBS symptoms; anxiety was a secondary or comorbidity observation. Evidence is **indirect** (different drug, IBS primary endpoint) and cannot support a dysthymic disorder indication. |

---

## Literature Evidence

Currently no direct publications linking Alverine to **dysthymic disorder** are available.

> **Note:** The following publication (identified for the anxiety disorder prediction, rank #3) provides the only direct preclinical evidence of CNS activity for Alverine and is the mechanistic basis for the entire psychiatric prediction cluster:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25199966](https://pubmed.ncbi.nlm.nih.gov/25199966/) | 2014 | Animal Study (Preclinical) | European Journal of Pharmacology | Alverine citrate demonstrated anxiolytic-like effects in experimental mouse models of anxiety. The proposed mechanism involves 5-HT1A receptor activity. This is the sole direct pharmacological evidence supporting any CNS/psychiatric application of Alverine. |
| [30087074](https://pubmed.ncbi.nlm.nih.gov/30087074/) | 2018 | Computational Biology | European Neuropsychopharmacology | Network-based drug repositioning study using protein-protein interaction networks to predict potential antidepressants from DrugBank compounds. Alverine was identified as a candidate based on network topology similarity to known antidepressants — not on direct biological validation. Supports the dysthymia/neurotic depression signal as a computational hypothesis only. |

---

## Singapore Market Information

Alverine is **not currently marketed in Singapore**. No Health Sciences Authority (HSA) product authorisations are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registrations found |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data, key warnings, or contraindication data were retrievable for Alverine in this evidence search.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model ranks dysthymic disorder as the top predicted indication for Alverine with a score of 99.83%, but this signal is currently supported by **model prediction only (L5)** — there are no clinical trials and no direct preclinical or clinical publications for this indication. The psychiatric prediction cluster (dysthymia, neurotic depression, anxiety disorder, agoraphobia) all appear to stem from the same hypothesised serotonergic mechanism, with only one mouse-model study (PMID 25199966) providing any biological foundation, and that study focused on anxiety — not dysthymia specifically.

**To proceed, the following is needed:**

- **Mechanism of action clarification**: Confirm whether Alverine has documented 5-HT1A agonist/antagonist activity (query DrugBank API and primary pharmacology literature; DrugBank ID: DB01616).
- **Step-wise psychiatric indication development**: Anxiety disorder (rank #3, evidence level L4) is the most appropriate first target, not dysthymic disorder. An investigator-initiated preclinical study (in vivo rodent model of chronic mild stress) should establish antidepressant activity before dysthymia is pursued.
- **Safety data retrieval**: Download and parse the Alverine package insert to extract warnings, contraindications, and hepatic/renal dosing considerations — currently a blocking data gap (DG001).
- **IBS–anxiety comorbidity trial design**: Reanalyse existing IBS clinical data (e.g., NCT00934973) for anxiety sub-scores to quantify the anxiolytic signal in humans before commissioning a de novo psychiatric RCT.
- **Singapore regulatory pathway assessment**: Since Alverine has no HSA registration, a full new drug application pathway would be required — significantly higher barrier than a line-extension strategy. Confirm whether Alverine is available in any regional markets (e.g., UK, France, India) that could support a bridging study strategy.