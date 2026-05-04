---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Imiglucerase
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

---

## One-Sentence Summary

Imiglucerase (Cerezyme®) is a recombinant glucocerebrosidase enzyme replacement therapy (ERT) approved globally for Gaucher disease — the most common lysosomal storage disorder — but currently not marketed in Singapore.
TxGNN ranks Hurler syndrome as its top repurposing target (score 99.52%), supported by **0 clinical trials** and **2 publications**; however, the mechanistic link is absent, as Hurler syndrome requires alpha-L-iduronidase replacement, an entirely different enzyme.
The most evidence-supported prediction is **rank 6: lysosomal storage disease with skeletal involvement** (operationally equivalent to Gaucher disease with bone complications), backed by **2 completed clinical trials** and **20 publications**, with L1 evidence and a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gaucher disease (glucocerebrosidase deficiency; FDA-approved 1994, EMA-approved) |
| TxGNN Top Predicted Indication | Hurler syndrome (rank 1) |
| TxGNN Prediction Score | 99.52% (Hurler syndrome, rank 1) |
| Evidence Level | L4 (rank 1: Hurler syndrome) / L1 (rank 6: lysosomal storage disease with skeletal involvement) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (ranks 1–5, 7–10) / Proceed with Guardrails (rank 6) |

---

## Why is This Prediction Reasonable?

Imiglucerase is a recombinant form of human glucocerebrosidase (GBA), produced in Chinese hamster ovary cells and modified to expose mannose residues that direct the enzyme into macrophage lysosomes via mannose receptor-mediated endocytosis. In Gaucher disease, pathogenic GBA mutations cause glucocerebroside (glucosylceramide) to accumulate within lysosomes of macrophages throughout the liver, spleen, bone marrow, and — in neuropathic subtypes — the central nervous system. Intravenous biweekly administration of imiglucerase replenishes the deficient enzyme, progressively clearing the glycolipid substrate and reversing systemic manifestations including hepatosplenomegaly, anaemia, thrombocytopenia, and skeletal complications.

TxGNN's high scores for Hurler syndrome (MPS I), Scheie syndrome, Wolman disease, and cholesteryl ester storage disease reflect the knowledge graph's recognition that all lysosomal storage diseases share a common pathophysiological logic — an enzyme deficiency leads to substrate accumulation and progressive organ damage. This category-level similarity is a structural artifact of the knowledge graph, not a clinically actionable mechanistic link. **Hurler and Scheie syndromes require replacement of alpha-L-iduronidase (laronidase, Aldurazyme®), which is a completely different lysosomal enzyme from glucocerebrosidase.** Imiglucerase has no catalytic activity against the glycosaminoglycan substrates that accumulate in MPS I.

The most clinically coherent and evidence-supported TxGNN prediction is **rank 6: lysosomal storage disease with skeletal involvement**, which maps directly to the established, globally approved indication for imiglucerase. Multiple cohort studies, clinical trials, and long-term registries confirm that imiglucerase reduces bone marrow infiltration, bone pain, avascular necrosis risk, and improves quality of life in patients with skeletal Gaucher disease. The critical gap in Singapore is not efficacy uncertainty but the absence of local market authorisation, making this a market access question rather than a clinical evidence question.

---

## Clinical Trial Evidence

*Hurler syndrome (TxGNN rank 1):*

Currently no related clinical trials registered for imiglucerase in Hurler syndrome.

---

*Lysosomal storage disease with skeletal involvement (TxGNN rank 6 — highest evidence):*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04656600](https://clinicaltrials.gov/study/NCT04656600) | Phase 4 | Completed | 12 | Single-arm study of imiglucerase at maximum Chinese label dosage (60 U/kg IV biweekly) in Chinese patients with Gaucher disease type III; evaluated haematologic parameters, visceral manifestations, bone disease efficacy, and safety profile |
| [NCT01842841](https://clinicaltrials.gov/study/NCT01842841) | Phase 3 | Completed | 5 | Open-label extension of velaglucerase alfa ERT in Japanese patients with Gaucher disease; demonstrates class-level ERT efficacy for skeletal and haematologic manifestations in an Asian population (same enzyme class, different molecule, supports biological plausibility) |

---

## Literature Evidence

*Hurler syndrome (TxGNN rank 1) — 2 publications:*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Technical Study | PNAS | PET imaging applied to monitor ERT enzyme distribution across multiple LSDs including Gaucher, Fabry, **Hurler**, Hunter, and Pompe disease; imiglucerase cited as the prototype ERT — no therapeutic data specific to Hurler |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | Rev Med Interne | Review of ERT development for LSDs; describes imiglucerase as the ERT prototype and discusses distinct enzyme products required for Fabry, **Hurler**, Hunter, and Pompe — confirms different enzymes are needed for each disease |

*Lysosomal storage disease with skeletal involvement (TxGNN rank 6 — 20 publications, top 10 selected):*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17539908](https://pubmed.ncbi.nlm.nih.gov/17539908/) | 2007 | Cohort | Clinical Genetics | Imiglucerase (60 U/kg biweekly) significantly improved health-related quality of life in 32 treatment-naïve type 1 Gaucher patients with skeletal manifestations including bone pain, medullary infarctions, avascular necrosis, and lytic lesions |
| [8931951](https://pubmed.ncbi.nlm.nih.gov/8931951/) | 1996 | Clinical Trial | Blood Cells Mol Dis | Low-dose ERT produced objective bone improvement in 14 adult type 1 Gaucher patients with severe skeletal involvement over 2–4 years of treatment |
| [9453101](https://pubmed.ncbi.nlm.nih.gov/9453101/) | 1997 | Clinical Study | Skeletal Radiology | MRI-based assessment of bone marrow involvement and ERT response in type 1 Gaucher disease; MRI identified as most sensitive tool for monitoring skeletal treatment response |
| [22640238](https://pubmed.ncbi.nlm.nih.gov/22640238/) | 2012 | Cohort | Br J Haematology | ICGG Registry retrospective analysis (n=1,016 GD1 patients with intact spleen) examining characteristics associated with persistent thrombocytopenia after 4–5 years of continuous imiglucerase therapy |
| [18553043](https://pubmed.ncbi.nlm.nih.gov/18553043/) | 2008 | Case Series | Calcified Tissue Int | Bone metabolism laboratory parameters in 7 Gaucher patients consecutively switching from imiglucerase ERT to miglustat substrate reduction therapy; documents bone marker changes during treatment transition |
| [20055531](https://pubmed.ncbi.nlm.nih.gov/20055531/) | 2010 | Review | BioDrugs | Comprehensive review of imiglucerase: mechanism, dosing optimisation, clinical outcomes including bone improvements, and registry evidence from the ICGG international database |
| [27441734](https://pubmed.ncbi.nlm.nih.gov/27441734/) | 2016 | Biomarker Study | Am J Hematology | Plasma glucosylsphingosine (lyso-GL1) validated as key biomarker for Gaucher disease activity and ERT response in 169 GD1 patients; relevant for treatment monitoring |
| [34500086](https://pubmed.ncbi.nlm.nih.gov/34500086/) | 2021 | Cohort | Eur J Med Genetics | 16-year single-centre retrospective study of 38 Turkish children with GD1/GD3; imiglucerase ERT improved haematologic and visceral outcomes; characterises paediatric Asian/Middle Eastern population response |
| [25127542](https://pubmed.ncbi.nlm.nih.gov/25127542/) | 2014 | Cohort | Mol Genet Metab | Long-term ERT outcomes in Italian type 3 Gaucher cohort; ERT effective for systemic manifestations; CNS involvement not addressed due to blood-brain barrier limitation |
| [21889384](https://pubmed.ncbi.nlm.nih.gov/21889384/) | 2011 | Review | Mol Genet Metab | Comprehensive review of bone pathology in Gaucher disease and ERT response; discusses heterogeneity of skeletal involvement including osteonecrosis, marrow infiltration, and pathological fracture mechanisms |

---

## Singapore Market Information

No registered products found. Imiglucerase is **not currently authorised or marketed in Singapore** (0 HSA licences).

For patient access in Singapore, potential pathways include:

- **Named-patient / Special Access Route**: Application to HSA under the Special Access Route for unregistered therapeutic products
- **Institutional importation**: Licensed healthcare institutions (e.g., tertiary hospitals) may arrange direct importation
- **Manufacturer programme**: Contact Sanofi Genzyme for patient assistance or named-patient supply

---

## Safety Considerations

No warnings, contraindications, or drug interactions were retrieved in this evidence pack for imiglucerase.

Based on well-established clinical experience with intravenous ERT:

- **Infusion-related reactions** are the most commonly reported adverse events, occurring in approximately 13% of patients; symptoms include pruritus, flushing, urticaria, chest discomfort, and — rarely — anaphylaxis. Pre-medication with antihistamines or low-dose corticosteroids is recommended for patients who have experienced prior reactions.
- **Antibody formation**: A subset of patients develops IgG antibodies to imiglucerase; most remain asymptomatic, but monitoring is recommended, particularly in patients with persistent or worsening disease despite adequate dosing.

Please refer to the international Cerezyme® product insert for full prescribing information, including pregnancy, lactation, and renal/hepatic impairment guidance.

---

## Conclusion and Next Steps

**Decision: Hold (novel repurposing, ranks 1–5 and 7–10) / Proceed with Guardrails (rank 6: Gaucher disease with skeletal involvement)**

**Rationale:**
TxGNN's top nine unique predictions (Hurler syndrome through rank 10) are either mechanistically invalid — each requiring a different lysosomal enzyme unrelated to glucocerebrosidase — or entirely without supporting evidence. The one actionable TxGNN finding (rank 6) corresponds to imiglucerase's own established global indication and is supported by L1-level evidence including multiple cohort studies, Phase 3/4 trials, and long-term international registries. The barrier to use in Singapore is **market access**, not clinical uncertainty.

**To proceed (Gaucher disease with skeletal involvement, Singapore access), the following is needed:**

- **Market access**: Initiate HSA Special Access Route or institutional importation process; confirm whether the Ministry of Health rare disease funding framework covers imiglucerase
- **Safety documentation**: Obtain the full international Cerezyme® package insert and conduct a formal pharmacist-led safety review prior to any infusion
- **Baseline workup**: Establish pre-treatment assessment including CBC with differential, liver and spleen imaging (ultrasound/MRI), bone marrow MRI for skeletal disease burden, and plasma lyso-GL1 biomarker
- **Long-term monitoring plan**: Define CBC, organ imaging, and biomarker review intervals aligned with ICGG Registry protocols
- **For novel repurposing directions (ranks 1–5, 7–10)**: Mechanistic validation studies required before any clinical consideration; TxGNN scores reflect disease-category similarity, not enzyme-level specificity

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Clinicians should refer to the full product monograph and applicable regulatory guidance for patient care decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

