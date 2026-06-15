---
layout: default
title: Benzyl Benzoate
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
---

# Benzyl Benzoate
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

# Benzyl Benzoate: From Antiparasitic Use to Pharyngitis

## One-Sentence Summary

Benzyl benzoate is a well-established antiparasitic agent historically used topically to treat scabies and pediculosis; no formal original indications were captured in the current evidence pack due to data gaps.
The TxGNN model predicts it may be effective for **Pharyngitis** as the top-ranked indication,
with **0 clinical trials** and **0 publications** currently supporting this specific direction — making this a model-only prediction at this stage.

Notably, several downstream predictions (vulvovaginitis, vulvovaginal candidiasis, bacterial vaginosis, vulvitis, vaginitis) carry a "Research Question" recommendation based on benzyl benzoate's known antimicrobial and antiparasitic properties, representing a more pharmacologically coherent cluster for future investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; historically used as a scabicide/antiparasitic agent (scabies, pediculosis) |
| Predicted New Indication | Pharyngitis (Rank 1) |
| TxGNN Prediction Score | 88.66% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on known pharmacological information, benzyl benzoate is an ester of benzyl alcohol and benzoic acid, primarily recognised as a scabicide and pediculicide acting through neurotoxic effects on arthropod parasites (inhibition of octopaminergic neurotransmission). It also exhibits mild broad-spectrum antimicrobial and preservative properties, which have historically led to its inclusion as an excipient in various topical formulations including some oropharyngeal preparations.

The mechanistic link between benzyl benzoate and pharyngitis is, however, weak. Pharyngitis is predominantly caused by Group A Streptococcus or respiratory viruses, pathogens for which benzyl benzoate has no demonstrated targeted activity. The TxGNN model's high score (88.66%) for this indication most likely reflects topological proximity in the knowledge graph between benzyl benzoate nodes and mucosal infection-related disease nodes, rather than a genuine pharmacological relationship.

By contrast, the model's predictions for the vaginal/vulvar indication cluster (ranks 3, 5, 6, 8, 10) are pharmacologically more coherent: benzyl benzoate has documented in vitro activity against Trichomonas vaginalis, Candida albicans, and anaerobic bacteria — the primary pathogens underlying vaginitis, vulvovaginitis, bacterial vaginosis, and vulvovaginal candidiasis. These indications are better candidates for follow-up research, even though all currently sit at L5 evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Benzyl benzoate × Pharyngitis (or any of the top 10 predicted indications).

---

## Literature Evidence

No directly relevant literature was identified for the top predicted indication (pharyngitis).

For **vaginitis** (rank 3), one tangentially related publication was retrieved; however, its relevance to benzyl benzoate is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40190812](https://pubmed.ncbi.nlm.nih.gov/40190812/) | 2025 | Animal Study (Preclinical) | Drug Design, Development and Therapy | Investigates a progesterone microneedle patch for prevention of preterm birth in a mouse model via vaginal administration; does not study benzyl benzoate directly — relevance to benzyl benzoate repurposing is negligible |

---

## Singapore Market Information

Benzyl benzoate is **not currently registered** in Singapore. No product authorisations or licence records are available.

---

## Safety Considerations

Safety data for benzyl benzoate is not available in this evidence pack (key warnings, contraindications, and drug interaction data were not retrieved). Please refer to the package insert and current product monographs for full safety information.

Key data gaps requiring resolution before any clinical progression:
- TFDA/HSA package insert warnings and contraindications (currently blocking S1 safety review)
- Formal drug-drug interaction data

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication (pharyngitis) is an L5 prediction with no clinical trials, no literature support, and a mechanistic mismatch — benzyl benzoate's antiparasitic and mild antimicrobial profile does not align with the primary infectious aetiology of pharyngitis. The evidence base is insufficient to advance this candidate.

**A more productive research direction exists within this same prediction set:**
The vaginal/vulvar indication cluster (vulvovaginitis, vulvovaginal candidiasis, bacterial vaginosis, vaginitis, vulvitis — ranks 3, 5, 6, 8, 10) demonstrates stronger mechanistic coherence with benzyl benzoate's known pharmacology and should be prioritised for follow-up.

**To proceed with any indication, the following is needed:**

- **Safety baseline**: Retrieve and review TFDA/HSA package insert (blocking item — required before any further evaluation)
- **MOA confirmation**: Query DrugBank API for full mechanism of action, target binding data, and pharmacodynamic profile
- **In vitro screening (vaginal/vulvar cluster)**: Design MIC assays against Candida albicans, Trichomonas vaginalis, Gardnerella vaginalis, and anaerobic vaginal flora
- **Formulation assessment**: Evaluate feasibility of a topical vaginal delivery system (gel, suppository, or microneedle patch) given benzyl benzoate's chemical properties
- **Singapore regulatory pathway**: Confirm whether a pre-IND consultation or literature-bridging NDA pathway is applicable given the absence of local registration
- **Systematic literature review**: Conduct a structured search specifically for benzyl benzoate antimicrobial activity studies (broader than indication-specific queries) to supplement the current evidence gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

