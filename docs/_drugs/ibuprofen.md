---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ibuprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID), long established for pain relief, fever reduction, and management of inflammation across a broad range of musculoskeletal and systemic conditions.
The TxGNN model predicts it may have potential in **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare genetic skeletal developmental disorder,
however **no clinical trials or published literature** currently support this specific direction — placing this prediction at Evidence Level **L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain, fever, and inflammation (standard NSAID use; no Singapore HSA regulatory record retrieved) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed (no HSA registrations found) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

> **Note on market status:** The absence of Singapore HSA registrations for Ibuprofen is unexpected given its status as one of the most widely available OTC drugs globally. This likely reflects a data retrieval gap in the current regulatory query rather than a true absence from the Singapore market. Manual verification via the HSA product database is recommended.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Ibuprofen is a non-selective inhibitor of cyclooxygenase enzymes (COX-1 and COX-2), blocking the conversion of arachidonic acid to prostaglandins and thromboxanes. This results in reduced inflammation, analgesia, and antipyresis. Its broad use in musculoskeletal and joint-related pain conditions is why it plausibly appears in predictions involving bone and skeletal diseases.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare autosomal recessive skeletal disorder caused by loss-of-function mutations in the *GDF5/CDMP1* gene, resulting in disproportionate shortening of the middle and distal limb segments (radius, ulna, tibia, fibula). This is fundamentally a developmental genetic defect affecting cartilage and bone morphogenesis. While Ibuprofen's COX inhibition could theoretically provide symptomatic relief for secondary joint inflammation and pain in affected patients, it has no known mechanism to correct or compensate for the underlying genetic defect in BMP signalling. Any benefit would be purely supportive.

The high TxGNN prediction score (99.74%) most likely reflects a knowledge graph clustering effect: skeletal disease nodes are structurally similar in the graph, leading the model to score Ibuprofen highly across a broad cluster of rare skeletal conditions. This interpretation is strongly supported by the fact that 6 of the top 10 predicted indications are rare genetic skeletal dysplasias (brachyolmia, pseudoachondroplasia, brachydactyly-syndactyly syndrome, brachyolmia-amelogenesis imperfecta syndrome, acromesomelic dysplasia). These are likely systematic false positives driven by graph topology rather than specific drug-disease pharmacology.

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
This prediction sits at Evidence Level L5 — it is supported solely by the TxGNN knowledge graph model, with zero backing from clinical trials or published literature. The predicted indication is a rare, irreversible genetic skeletal disorder for which Ibuprofen lacks any disease-modifying mechanism; the high TxGNN score is most plausibly explained by graph clustering of skeletal disease nodes rather than true pharmacological relevance.

**To proceed, the following is needed:**

- **Retrieve MOA data from DrugBank** (DG002) to enable formal mechanistic analysis linking COX inhibition to skeletal disease biology
- **Verify Singapore HSA registration status** directly on the HSA product database — current data showing zero registrations is likely a retrieval gap for such a common drug
- **Retrieve package insert safety data** (DG001): warnings and contraindications are currently unavailable and required before any clinical use evaluation
- **Assess symptomatic use case separately**: if the research question is whether Ibuprofen can manage pain in patients with skeletal dysplasias (rather than modify disease), this is a lower-bar clinical question that could be addressed via observational case series, distinct from a formal repurposing programme
- **Consider deprioritising the skeletal dysplasia cluster** (ranks 1–4, 5–6): the systematic co-occurrence of rare bone disorders in the top predictions suggests a knowledge graph artifact; the predictions at rank 3 (myosclerosis) and rank 8 (hypotrichosis simplex of the scalp) carry relatively stronger mechanistic rationale and may be more worth investigating as exploratory research questions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

