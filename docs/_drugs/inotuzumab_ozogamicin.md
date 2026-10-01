---
layout: default
title: Inotuzumab Ozogamicin
parent: Low Evidence (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
---

# Inotuzumab Ozogamicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Inotuzumab ozogamicin: From Relapsed/Refractory B-Cell Leukaemia to Drug-Induced Osteoporosis

## One-Sentence Summary

Inotuzumab ozogamicin is a CD22-directed antibody-drug conjugate with a calicheamicin DNA-cleaving payload. It is a B-cell-targeted cancer drug, and the local record does not state its approved indication.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction with no plausible biological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local HSA data. The drug is a CD22-directed agent for B-cell malignancy (relapsed/refractory CD22-positive B-cell precursor acute lymphoblastic leukaemia, from general knowledge, not from the Evidence Pack) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 98.24% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Inotuzumab ozogamicin is a CD22-directed antibody-drug conjugate. CD22 is expressed on B-lineage cells, and the calicheamicin payload cleaves DNA to kill the targeted cells.

The prediction is **not** mechanistically supported. Bone-forming or anti-resorptive activity has no support for this drug. A cytotoxic agent would more likely harm bone marrow and bone health than protect it. The high TxGNN score reflects graph proximity in the knowledge graph, not a biological mechanism.

The other top-ranked predictions show the same pattern. They include several breast cancer subtypes, diabetic retinopathy, platelet and von Willebrand-type bleeding disorders, and a veterinary disease (infectious bovine rhinotracheitis). None has clinical trials, and none has a CD22-based rationale. Some are also unsafe for this drug: its cytopenias could worsen bleeding disorders, and its hepatotoxicity is a poor trade-off in a non-life-threatening eye condition. The breast cancer subtypes lack CD22 expression. Overall, the predictions look like knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

For the lower-ranked prediction "breast tumor luminal A or B", 19 publications were retrieved. All were keyword false positives on "B" (B-cell biology, hepatitis B vaccines, B-cell lymphoma). None concerns breast cancer or bone health, and they do not support any predicted indication.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15747P | BESPONSA Powder for Concentrate for Solution for Infusion 1 mg/vial (Wyeth Pharmaceutical Division of Wyeth Holding LLC) | Powder, for solution | Not stated in the local record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic payload (calicheamicin, a DNA-cleaving agent) |
| Myelosuppression Risk | Cytopenias and thrombocytopenia are recognised main toxicities. Please refer to the package insert for incidence details |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with platelets, liver function (hepatotoxicity including veno-occlusive disease is a known risk) |
| Handling Protection | Follow local cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.
- **Other risks**: Known risks include hepatotoxicity (including veno-occlusive disease), cytopenias and thrombocytopenia.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score. There are no clinical trials or literature, and no plausible mechanism links a CD22-directed cytotoxic conjugate to osteoporosis. The drug's toxicity profile makes benefit-risk unfavourable for this indication.

**To proceed, the following is needed:**
- HSA package insert (warnings, contraindications, approved indication), which is required before any safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical signal linking the drug to bone metabolism. Without one, this candidate should not advance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

