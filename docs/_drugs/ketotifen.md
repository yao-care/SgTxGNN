---
layout: default
title: Ketotifen
parent: 僅模型預測 (L5)
nav_order: 550
evidence_level: L5
indication_count: 10
---

# Ketotifen
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

# Ketotifen: From Bronchial Asthma / Allergic Disorders to Allergic Urticaria

## One-Sentence Summary

Ketotifen is a second-generation antihistamine and mast cell stabilizer with established use in bronchial asthma prophylaxis and allergic disorders. The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **0 registered clinical trials** but **20 published literature sources** — including at least 3 RCTs — currently supporting this direction. The mechanistic rationale is strong: urticaria is driven by the same IgE/mast cell/histamine axis that ketotifen is designed to suppress at both upstream and downstream levels.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bronchial asthma prophylaxis and allergic disorders (per established pharmacology; no Singapore regulatory record) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ketotifen is a benzocycloheptathiophene compound that exerts its effects through two complementary mechanisms: (1) competitive antagonism at histamine H1 receptors, and (2) stabilisation of mast cell membranes, thereby inhibiting the release of histamine, leukotrienes, and other inflammatory mediators triggered by IgE–FcεRI crosslinking. This dual action distinguishes it from pure H1 antagonists, which only block downstream receptor activation.

The mechanistic overlap with allergic urticaria is highly compelling. Urticaria's central pathophysiology is an allergen-driven sequence: IgE/FcεRI activation → mast cell degranulation → histamine and prostaglandin release → cutaneous microvascular dilatation and increased permeability → wheal-and-flare formation. Ketotifen interrupts this chain at two points simultaneously — it suppresses mast cell degranulation upstream *and* blocks H1 receptor activation downstream — offering a theoretically more complete pharmacological coverage than monotherapy with a conventional antihistamine. The mechanistic chain can be summarised as: **Allergen → IgE/FcεRI → [Ketotifen inhibits] mast cell degranulation → [Ketotifen blocks] H1R activation → suppressed vasodilation + reduced vascular permeability → symptom relief**.

In practice, multiple comparative clinical studies (including RCTs) and a long-standing body of literature have evaluated ketotifen specifically in chronic urticaria, cold urticaria, and allergic urticaria subtypes. A 1990 comprehensive pharmacology review (PMID 2226222) confirmed pronounced antihistaminic and antiallergic activity in allergic disorders, and a 2013 narrative review (PMID 24267353) described ketotifen as an underutilised option meriting "resurrection" in chronic urticaria management. TxGNN's high prediction score of 98.60% is consistent with this well-grounded mechanistic and empirical evidence base.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for Ketotifen in Allergic Urticaria.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9487221](https://pubmed.ncbi.nlm.nih.gov/9487221/) | 1998 | Clinical Trial (direct) | Archives of Dermatology | Direct clinical trial evaluating ketotifen in chronic urticaria |
| [19753736](https://pubmed.ncbi.nlm.nih.gov/19753736/) | 2002 | RCT (head-to-head) | J Dermatological Treatment | Compared levothyroxine vs ketotifen in chronic urticaria with thyroid autoimmunity; explores ketotifen as frontline antiurticarial therapy |
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | RCT (head-to-head) | Asian Pacific J Allergy Immunol | Double-blind crossover RCT comparing cyproheptadine vs ketotifen in cold urticaria in children; efficacy of ketotifen demonstrated |
| [24267353](https://pubmed.ncbi.nlm.nih.gov/24267353/) | 2013 | Narrative Review | Ann Allergy Asthma Immunol | "Ketotifen in the management of chronic urticaria: resurrection of an old drug" — advocates for ketotifen's underrecognised role in urticaria |
| [2226222](https://pubmed.ncbi.nlm.nih.gov/2226222/) | 1990 | Drug Review | Drugs | Comprehensive review: ketotifen reduces symptoms in ~70% of bronchial asthma patients; pronounced antihistaminic and antiallergic activity including urticaria-relevant effects |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Comparative Review | Drugs | Comparative review of second-generation antihistamines (including ketotifen) for urticaria and allergic disorders; evaluates sedation, efficacy and safety profiles |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Reviews efficacy and safety of first- and newer-generation antihistamines for allergic rhinitis and chronic idiopathic urticaria; guides pharmacy management |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Comprehensive urticaria treatment overview; nonsedating antihistamines as mainstay for chronic idiopathic urticaria; ketotifen discussed as treatment option |
| [2873823](https://pubmed.ncbi.nlm.nih.gov/2873823/) | 1986 | Cohort | Asian Pacific J Allergy Immunol | Observational study of 142 paediatric urticaria patients; ketotifen used among treatment options; characterises prevalence and causes |
| [15617665](https://pubmed.ncbi.nlm.nih.gov/15617665/) | 2004 | Case Series | Allergologia et Immunopathologia | Child with severe cold urticaria secondary to infectious mononucleosis treated with prophylactic ketotifen + cetirizine; ice cube test results documented |

---

## Singapore Market Information

Ketotifen is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product authorisations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Safety data (warnings, contraindications, drug interactions) were not available in this Evidence Pack. Retrieval of the full prescribing information from the originating manufacturer or an approved international regulatory source (e.g., EMA, Health Canada, or TGA) is required before clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for ketotifen in allergic urticaria is highly plausible and well-characterised — dual H1 antagonism and mast cell stabilisation directly target the central IgE/mast cell/histamine pathophysiology of urticaria. At least three RCTs and a substantial body of literature (20 publications) support its use in urticaria subtypes, yielding an L2 evidence classification. However, the absence of recent large-scale Phase 3 trials, no Singapore regulatory status, and incomplete safety data prevent an unconditional "Go" decision.

**To proceed, the following is needed:**

- **Safety dossier**: Retrieve full prescribing information (warnings, contraindications, drug interactions) from EMA, Health Canada, or TGA — required before any S1 safety assessment can be completed
- **MOA confirmation**: Obtain structured MOA data from DrugBank (DB00920) to formalise mechanism documentation
- **Singapore regulatory pathway**: Assess HSA registration requirements; determine whether existing approvals from reference agencies (e.g., EMA) can expedite local registration
- **Contemporary RCT data**: Conduct a targeted search for any post-2000 Phase 2/3 controlled trials of ketotifen in allergic urticaria to supplement older literature
- **Formulation strategy**: Confirm appropriate oral dosage form availability and supply chain for the Singapore market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

