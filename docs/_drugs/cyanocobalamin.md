---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Cyanocobalamin
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

# Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin is the synthetic form of Vitamin B12, classically used to treat vitamin B12 deficiency and megaloblastic anemia arising from dietary deficiency or malabsorption syndromes.
The TxGNN model predicts it may be effective for **Biotin Metabolic Disease**, with **15 clinical trials** and **20 publications** currently identified in support of this direction.
However, the majority of retrieved evidence is indirect — no trials directly test Cyanocobalamin as a therapeutic agent for biotin metabolic disease — placing the current evidence at **L3**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin B12 deficiency; megaloblastic anemia (not registered in Singapore — no approved indication on record) |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the formal drug record. Based on known biochemical information, Cyanocobalamin is a synthetic form of Vitamin B12 that is converted in the body to two active cofactors: adenosylcobalamin and methylcobalamin. Adenosylcobalamin drives the conversion of methylmalonyl-CoA to succinyl-CoA via the enzyme methylmalonyl-CoA mutase (MUT); methylcobalamin participates in remethylation of homocysteine to methionine. These reactions are central to propionate catabolism and one-carbon metabolism.

The mechanistic link to biotin metabolic disease rests on a shared metabolic node. Biotin is the obligatory cofactor for propionyl-CoA carboxylase (PCC), which converts propionyl-CoA to methylmalonyl-CoA — the direct substrate for the B12-dependent MUT enzyme. When biotin metabolism is disrupted (e.g., in biotinidase deficiency or holocarboxylase synthetase deficiency), PCC dysfunction causes propionyl-CoA accumulation and secondary impairment of the methylmalonyl-CoA pathway, which can reduce the efficiency of B12-dependent enzymatic steps downstream. A 2013 clinical review (PMID 23622402) explicitly groups cobalamin, folate, and biotin together as core cofactor interventions in vitamin-responsive inherited metabolic disorders, supporting the biological rationale for this prediction.

It is important to clarify, however, that Cyanocobalamin is not the primary treatment for biotin metabolic disease — biotin supplementation remains the first-line standard of care. B12 plays an adjunctive or secondary role in patients with combined or overlapping pathway dysfunction (e.g., methylmalonic acidemia with secondary propionate accumulation). The TxGNN prediction most likely captures metabolic network proximity rather than a direct, standalone therapeutic indication. Notably, one of the lower-ranked predictions — **proteinuria** (Rank 8) — carries a substantially stronger mechanistic link via Imerslund-Gräsbeck syndrome (CUBN mutations causing selective B12 malabsorption with proteinuria), and that indication has received a "Proceed with Guardrails" recommendation in this analysis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1,000 | Comparison of micronutrient-fortified food vs. milk (measuring serum B12 among other markers) in malnourished Guatemalan children; Phase 2 design with B12 as a key measured intervention component |
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | Completed | 33 | Phase 3 RCT of carglumic acid in propionic acidemia (PA) and methylmalonic acidemia (MMA) — both organic acidemias share the same propionate-biotin-B12 metabolic axis affected in biotin metabolic disease |
| [NCT05832190](https://clinicaltrials.gov/study/NCT05832190) | N/A | Terminated | 5 | Biotin + dietary fibre supplementation to correct gut microbiota before bariatric surgery; terminated early (only 5 enrolled), biotin was the primary micronutrient of interest |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | Cross-over RCT of Q10 ubiquinol + Vitamins B & E as metabolic support in autism and Phelan-McDermid syndrome; B vitamins used as part of a broader metabolic support package, not biotin-specific |
| [NCT03655223](https://clinicaltrials.gov/study/NCT03655223) | N/A | Enrolling by Invitation | 30,000 | Pre-symptomatic newborn screening framework for rare conditions including biotin metabolic disorders; infrastructure and identification study, not a therapeutic trial |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Universal genomic newborn screening (Baby Detect) covering 126 treatable genetic diseases including biotin metabolic disease; diagnostic platform study, no direct B12 intervention |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | B12-containing nutritional intervention targeting impaired methylation and antioxidant capacity in children with autism; indirect relevance via shared methylation pathway |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Clinical Review | Handbook of Clinical Neurology | Directly groups cobalamin, folate, and biotin as core cofactors in vitamin-responsive metabolic disorders; delineates inborn errors of cobalamin and biotin absorption, transport, and intracellular metabolism in children |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Molecular Sciences | Describes B12 as cofactor for synthesis of succinyl-CoA from methylmalonyl-CoA and biotin; reviews molecular mechanisms of B12 deficiency beyond classical hematological effects, with relevance to metabolic disease |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | Clinical Metabolic Study | Pediatric Research | In vivo propionate metabolism study in PA, MMA (4 of 8 patients B12-responsive), and multiple carboxylase deficiency; directly demonstrates B12 responsiveness in overlapping biotin-B12 metabolic disorders |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Clinical Review | Advances in Clinical Chemistry | Comprehensive review of vitamin-responsive inborn errors of metabolism; includes cofactor therapy with B12 and biotin in inherited amino acid and organic acid metabolic disorders |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Case Series | Pediatric Clinics of North America | Megavitamin-responsive aminoacidopathies; documents B-complex vitamin (including B12) efficacy in various inborn errors of metabolism, including enzyme activation by cofactor supplementation |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Reviews vitamins (including B12 and biotin) in metabolic diseases via three mechanisms: malabsorption, errors in vitamin metabolism, and vitamin-dependent apoenzyme syndromes |
| [7015958](https://pubmed.ncbi.nlm.nih.gov/7015958/) | 1980 | Review | Annals of the New York Academy of Sciences | Interactions among B-complex vitamins essential for metabolic and catabolic reactions; explains clinical aberrations in metabolic disease states through vitamin interrelationships |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | Experimental | The Journal of Endocrinology | B12-deficient rats show glucose intolerance, delayed peak insulin, and promoted ketogenesis; supports a broader metabolic role of B12 beyond classical hematological and neurological functions |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | Reviews vitamin dependency syndromes, including B12-dependent conditions; relevant to inherited enzyme deficiency states that overlap with biotin metabolism |
| [7004517](https://pubmed.ncbi.nlm.nih.gov/7004517/) | 1980 | Review | Birth Defects Original Article Series | Documents enzyme manipulation by megavitamin therapy; supports pharmacological-dose B12 use in inborn errors of metabolism as a cofactor-rescue strategy |

---

## Singapore Market Information

Cyanocobalamin is currently **not registered** with the Health Sciences Authority (HSA) in Singapore. No product licenses are on record in the database as of the data cutoff (2026-04-04).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns Cyanocobalamin a high predictive score for biotin metabolic disease (99.60%), grounded in a biologically plausible mechanistic overlap through the shared propionate-CoA metabolic pathway. However, no clinical trial directly evaluates Cyanocobalamin as a therapeutic agent for biotin metabolic disease, all retrieved trials are of low direct relevance (Grade C or indirect), and biotin supplementation — not B12 — remains the established standard of care for biotinidase and holocarboxylase synthetase deficiency.

**To proceed, the following is needed:**

- **Indication sub-type clarification**: Identify the specific biotin metabolic disease subtype (e.g., biotinidase deficiency vs. holocarboxylase synthetase deficiency vs. acquired biotin depletion) where adjunctive B12 therapy might offer measurable benefit
- **Prospective pilot data**: Design a case series or proof-of-concept study evaluating B12 supplementation outcomes in patients with confirmed biotin metabolic disease who also show signs of secondary propionyl-CoA pathway disruption
- **Formal MOA documentation**: Retrieve complete DrugBank mechanism of action data and pharmacokinetic profiling for Cyanocobalamin to enable a rigorous mechanistic analysis
- **Safety and labelling data**: Obtain formal package insert information (warnings, contraindications, drug interactions), which was unavailable in the current evidence pack
- **Singapore regulatory pathway**: Conduct an HSA regulatory feasibility assessment, as Cyanocobalamin is currently not marketed in Singapore; evaluate whether orphan drug designation or a compassionate use pathway would apply given the rare disease context
- **Consider prioritising the Proteinuria / Imerslund-Gräsbeck syndrome indication (Rank 8)**: This indication carries a far stronger direct mechanistic link (cubilin-mediated B12 absorption pathway), a 2023 systematic review (PMID 37710296), and has received a "Proceed with Guardrails" recommendation — it represents the more actionable drug repurposing opportunity for Cyanocobalamin in this analysis

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

