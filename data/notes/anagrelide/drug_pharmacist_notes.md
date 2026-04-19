# Anagrelide: From Essential Thrombocythemia to Reactive Thrombocytosis

## One-Sentence Summary

Anagrelide is a platelet-reducing agent established for the treatment of essential thrombocythemia (ET), a clonal myeloproliferative neoplasm characterised by persistently elevated platelet counts.
The TxGNN model predicts it may be effective for **Reactive Thrombocytosis**, with **0 clinical trials** and **10 publications** currently supporting this direction.
The available evidence, however, largely discusses Anagrelide in the context of clonal (not reactive) thrombocytosis, and the evidence base does not yet justify advancing this repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Essential Thrombocythemia (myeloproliferative neoplasm) |
| Predicted New Indication | Reactive Thrombocytosis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on information from the retrieved literature, Anagrelide is believed to act primarily through inhibition of phosphodiesterase 3 (PDE3), which elevates intracellular cyclic AMP (cAMP) levels and subsequently blocks the late-stage maturation of megakaryocytes — the precursor cells that produce platelets. The net result is a reduction in circulating platelet count, which is why it is used in clonal thrombocytosis disorders such as essential thrombocythemia.

The biological connection to reactive thrombocytosis rests on the observation that both conditions share the phenotype of an elevated platelet count. If Anagrelide can suppress megakaryocyte maturation irrespective of the underlying driver, it could theoretically reduce platelet counts in secondary (reactive) thrombocytosis as well. TxGNN likely captured this phenotypic overlap through shared knowledge-graph nodes linking the drug to elevated platelet biology.

However, the clinical rationale for this repurposing is weak. Reactive thrombocytosis is a secondary condition caused by an underlying trigger — infection, inflammation, iron deficiency, or post-surgical states — and resolves upon treatment of the root cause. Platelet function is typically normal, so the thrombotic risk that justifies cytoreductive therapy in ET is absent. Anagrelide carries meaningful cardiovascular risks (arrhythmia, fluid retention, palpitations), making its risk-benefit profile difficult to justify in a self-limiting, lower-risk condition. This mechanistic mismatch is the primary reason the decision is **Hold**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Anagrelide in Reactive Thrombocytosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Narrative Review | Expert Review of Anticancer Therapy | Profiles Anagrelide (Agrylin) as a treatment option for clonal thrombocytosis; contrasts clonal vs reactive thrombocytosis and notes that reactive forms do not require therapeutic intervention |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Critical Review | Leukemia & Lymphoma | Critical appraisal of Anagrelide efficacy in ET; reinforces that cytoreductive therapy targets clonal thrombocytosis only, not reactive forms |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Medical Journal of Australia | ET diagnosis and management review; highlights that diagnosis depends on exclusion of reactive thrombocytosis; platelet-lowering therapy discussed |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective Cohort | Pediatric Blood & Cancer | Retrospective analysis of 12 paediatric cases; distinguishes essential from reactive thrombocythemia in children; reinforces differential diagnosis |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leukemia Research | Case-based review of thrombocytapheresis in myeloproliferative neoplasms with extreme thrombocytosis; Anagrelide cited as standard medical cytoreduction |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | American Journal of the Medical Sciences | Overview of thrombocytosis clinical spectrum; describes cytokine regulation of megakaryocyte production; differentiates pseudothrombocytosis, reactive, and clonal forms |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case Report | European Journal of Case Reports in Internal Medicine | Reports acute myocardial infarction in an ET patient on Anagrelide; highlights cardiovascular safety concerns of Anagrelide therapy |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Japanese Journal of Clinical Hematology | Reviews ET diagnosis and treatment in a Japanese context; lists Anagrelide alongside hydroxyurea and interferon-alpha for megakaryocyte suppression |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case Report | Srpski Arhiv Za Celokupno Lekarstvo | Case of ET co-existing with ankylosing spondylitis (which causes reactive thrombocytosis); managed with Anagrelide; illustrates diagnostic complexity |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case Report | Medicine | Reports digital replantation in a post-splenectomy thrombocytosis patient; discusses management of reactive thrombocytosis in a surgical setting |

---

## Singapore Market Information

Anagrelide is currently **not registered** in Singapore. No product licences are on record.

---

## Safety Considerations

Detailed package insert warnings and contraindications are not available in this Evidence Pack. Based on the retrieved case literature, the following safety signal has been identified:

- **Cardiovascular Risk**: A 2024 case report (PMID 38455691) documents acute myocardial infarction in an ET patient treated with Anagrelide, consistent with the known risk of arrhythmia, tachycardia, and fluid retention associated with PDE3 inhibition. This is particularly relevant when evaluating use in populations without high-thrombosis-risk clonal disease.

Please refer to the approved package insert (e.g., Agrylin® prescribing information) for complete warnings, contraindications, and drug interaction data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While reactive thrombocytosis and essential thrombocythemia share an elevated platelet count phenotype, reactive thrombocytosis is a self-limiting secondary condition with normal platelet function and low inherent thrombotic risk — the very risk that justifies Anagrelide's use in ET. The cardiovascular toxicity profile of Anagrelide (arrhythmia, fluid retention, risk of MI) creates an unfavourable risk-benefit balance in a condition that typically resolves with treatment of the underlying cause. All 10 retrieved publications discuss Anagrelide in the context of clonal, not reactive, thrombocytosis; none present evidence of benefit in the reactive setting.

**To proceed, the following would be needed:**

- **Establish the clinical unmet need**: Identify a reactive thrombocytosis subpopulation where platelet reduction is genuinely indicated (e.g., extremely high counts with symptomatic thrombotic risk unresponsive to root-cause treatment)
- **Mechanistic data (MOA)**: Obtain full DrugBank/prescribing information MOA to confirm PDE3 inhibition pathway relevance in reactive contexts
- **Prospective safety data**: At minimum, a pharmacovigilance review of any off-label use cases in reactive thrombocytosis
- **Regulatory baseline**: Retrieve full Singapore/TFDA package insert to complete the safety and contraindication profile before any clinical evaluation