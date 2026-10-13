---
layout: default
title: Leucovorin
parent: Low Evidence (L5)
nav_order: 591
evidence_level: L5
indication_count: 10
---

# Leucovorin
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

# Leucovorin: From Megaloblastic Anemia to Primary Hyperoxaluria

## One-Sentence Summary

Leucovorin (folinic acid) was originally used to treat megaloblastic anemia.
The TxGNN model predicts it may be effective for **primary hyperoxaluria**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Megaloblastic anemia |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, leucovorin is a reduced folate (a folic acid derivative) that can enter folate metabolism without needing the enzyme dihydrofolate reductase. Its efficacy in folate-related megaloblastic anemia is established, and it is widely used to rescue patients from antifolate toxicity.

The link to primary hyperoxaluria is weak. A plausible but unverified connection is that folate and one-carbon metabolism intersect with glyoxylate and oxalate pathways. However, primary hyperoxaluria is driven by enzyme defects (AGXT, GRHPR, HOGA1), and leucovorin has no established role in correcting them. The high score should be treated as a hypothesis, not as evidence of benefit.

Other predictions in the list vary in plausibility:
- **Congenital intrinsic factor deficiency** (score 99.34%) is the most biologically coherent. It causes B12 malabsorption and a folate-trap megaloblastic anemia, close to the original indication. Leucovorin could bypass the folate block, but it does not correct the B12 deficiency, and parenteral B12 remains standard treatment.
- **Inflammatory myopathies** (immune-mediated necrotizing myopathy, antisynthetase syndrome, focal myositis and others) likely score highly because leucovorin is used to rescue methotrexate toxicity in these patients. It is supportive care, not disease treatment.
- **Hereditary hemochromatosis, primary amyloidosis and acquired amyloid peripheral neuropathy** have no clear mechanistic link. These predictions may reflect shared annotations in the knowledge graph.

## Clinical Trial Evidence

Currently no clinical trials are registered for primary hyperoxaluria.

For reference, one trial was found for a lower-ranked prediction (primary amyloidosis). It is only indirectly related:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003331](https://clinicaltrials.gov/study/NCT00003331) | Phase 1 | Completed | 30 | Topotecan + 5-fluorouracil + leucovorin in advanced cancers. Leucovorin acts as a 5-FU modulator; the trial does not test amyloidosis. Relevance is low. |

## Literature Evidence

Currently no related literature is available for primary hyperoxaluria.

For reference, the following publications were retrieved for focal myositis (rank 8). All are indirect, since leucovorin appears only as rescue or supportive therapy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8393509](https://pubmed.ncbi.nlm.nih.gov/8393509/) | 1993 | RCT | Medicine | Retrospective review and randomized crossover trial of immunosuppressive therapy in inclusion body myositis |
| [9506565](https://pubmed.ncbi.nlm.nih.gov/9506565/) | 1998 | RCT | Arthritis and Rheumatism | Randomized crossover study of two cytotoxic regimens in refractory myositis |
| [32649847](https://pubmed.ncbi.nlm.nih.gov/32649847/) | 2021 | Case report | Immunological Medicine | Severe oral stomatitis from HSV-1 reactivation in a methotrexate-treated dermatomyositis patient; leucovorin given but stomatitis worsened |
| [25963703](https://pubmed.ncbi.nlm.nih.gov/25963703/) | 2015 | Case report | Gan to Kagaku Ryoho | Polymyositis associated with transverse colon cancer, responding to tumour resection and chemotherapy |
| [9787292](https://pubmed.ncbi.nlm.nih.gov/9787292/) | 1998 | Case report | Dtsch Med Wochenschr | Paraneoplastic orbital disease after leucovorin/5-FU chemotherapy for cardia carcinoma |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11058P | NYRIN INJECTION 50 mg/5 ml | Injection | Not specified |
| SIN10318P | NYRIN INJ. 15 mg/ml | Injection | Not specified |
| SIN11059P | NYRIN INJECTION 3 mg/ml | Injection | Not specified |
| SIN10357P | NYRIN TABLET 15 mg | Tablet | Not specified |

All four are single-ingredient products from Korea United Pharmaceutical Inc, and all are currently valid. Both injectable and oral forms are available.

## Cytotoxicity

Leucovorin is not an antineoplastic agent. It is a folate analogue used as a rescue agent and as a modulator of fluoropyrimidine chemotherapy. This section does not apply.

## Safety Considerations

- **Contraindications (from knowledge graph relationships, not label text)**: vitamin B12 deficiency and pernicious anemia. Leucovorin can correct the hematological picture while neurological damage from B12 deficiency progresses. This is directly relevant to the congenital intrinsic factor deficiency prediction.
- **Drug Interactions**: 100 interactions were identified in total. The main ones with a graded severity are:
  - Pancrelipase: Moderate
  - Sulfasalazine: Minor

  Most of the other listed interactions (for example calcitriol, pantoprazole, metformin, omeprazole, doxycycline and morphine) have no severity grading.

Please refer to the package insert for further safety information, including warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary hyperoxaluria rests on the model score alone (L5). No trials or literature exist, and there is no plausible mechanism by which leucovorin would correct the underlying enzyme defects. The package insert warnings and contraindications are also not yet available, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Download and review the HSA package insert for warnings, contraindications and approved indications (a blocking gap)
- Mechanism of action data from DrugBank
- A mechanistic or preclinical study linking folate metabolism to oxalate handling in primary hyperoxaluria
- Consideration of re-prioritising congenital intrinsic factor deficiency, which has the more coherent biological rationale, though it requires careful B12 co-management
- Route and formulation compatibility assessment for any new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

