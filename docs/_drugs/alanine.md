---
layout: default
title: Alanine
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Alanine
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

# Alanine: From Nutritional Amino Acid to Gastroparesis

## One-Sentence Summary

Alanine (L-丙胺酸) is an endogenous non-essential amino acid that participates in gluconeogenesis via the alanine-glucose cycle; it has no currently registered therapeutic indications in Singapore or Taiwan.
The TxGNN model predicts it may be relevant to **Gastroparesis**, with a prediction score of **99.37%**,
yet none of the **9 clinical trials** or **3 publications** retrieved directly involve Alanine as an intervention — all evidence relates to other gastroparesis drugs.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None (no approved therapeutic indications on record) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for Alanine in a therapeutic context. Based on known biochemistry, Alanine is a non-essential amino acid that functions as a key gluconeogenic precursor through the **alanine-glucose (Cahill) cycle**: skeletal muscle exports alanine to the liver during fasting, where it is converted to pyruvate and ultimately to glucose. This process is intimately linked to blood glucose homeostasis.

The rationale for the gastroparesis prediction, as noted in the Evidence Pack, is that **diabetic gastroparesis** is strongly associated with blood glucose fluctuations and autonomic neuropathy in the setting of diabetes. Since Alanine is central to the metabolic cross-talk between muscle and liver during glucose dysregulation, TxGNN's knowledge graph may have identified this metabolic adjacency. However, this mechanistic link is **highly indirect**: there is no established pathway by which exogenous Alanine supplementation would directly improve gastric motility, accelerate gastric emptying, or ameliorate gastroparetic symptoms.

Furthermore, Alanine is not marketed as a pharmaceutical product in Singapore (0 registered licenses), which means there is no established drug-product development basis. The high TxGNN score (rank 7,637 out of the full disease space) likely reflects broad metabolic node connectivity in the knowledge graph rather than a true pharmacological signal.

---

## Clinical Trial Evidence

All retrieved clinical trials were rated **Grade C** — none involve Alanine as the study intervention. They are listed here for completeness as the landscape of gastroparesis drug development.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01602549](https://clinicaltrials.gov/study/NCT01602549) | Phase 2 | Completed | 58 | GSK962040 (motilin receptor agonist) in Parkinson's disease patients with delayed gastric emptying — evaluates pharmacokinetics of L-DOPA |
| [NCT01262898](https://clinicaltrials.gov/study/NCT01262898) | Phase 2 | Completed | 79 | GSK962040 oral motilin agonist for diabetic gastroparesis (Type I/II), 28-day repeat dosing |
| [NCT03587142](https://clinicaltrials.gov/study/NCT03587142) | Phase 2 | Completed | 96 | Buspirone (anti-anxiety drug) for early satiety and gastroparesis symptoms — multicenter RCT (BESST trial) |
| [NCT03941288](https://clinicaltrials.gov/study/NCT03941288) | Phase 2 | Completed | 92 | Cannabidiol (CBD) for gastroparesis and functional dyspepsia — pharmacodynamics and pharmacogenetics |
| [NCT01934192](https://clinicaltrials.gov/study/NCT01934192) | Phase 2 | Terminated | 91 | GSK962040 for nutritional adequacy in critically ill patients (NUTRIATE study) — enteral nutrition support; terminated |
| [NCT02793154](https://clinicaltrials.gov/study/NCT02793154) | Phase 4 | Terminated | 4 | Albiglutide vs. exenatide on gastric myoelectrical activity in T2DM — terminated with only 4 subjects |
| [NCT01149369](https://clinicaltrials.gov/study/NCT01149369) | Phase 2 | Completed | 126 | Aprepitant (NK1 antagonist) for chronic nausea/vomiting of presumed gastric origin — multicenter RCT |
| [NCT06452966](https://clinicaltrials.gov/study/NCT06452966) | N/A | Recruiting | 350 | Traditional Chinese medicine interventions for organ failure in ICU patients — not gastroparesis-specific |
| [NCT07270939](https://clinicaltrials.gov/study/NCT07270939) | N/A | Not Yet Recruiting | 150 | Comparing 18/20/24-hour enteral nutrition feeding cycles in ICU patients |

> ⚠️ **Important**: None of the above trials use Alanine as the study drug. These represent the broader gastroparesis/gastric motility drug development landscape retrieved through the evidence search.

---

## Literature Evidence

All retrieved publications were rated as supporting background context only; none directly investigate Alanine as a therapeutic agent for gastroparesis.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Review | Advances in Renal Replacement Therapy | Gastrointestinal and hepatic disorders in end-stage renal disease; notes that gastroparesis is more prevalent in chronic renal failure — Alanine not mentioned as treatment |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | Review/Case Series | Diabetic Medicine | Diabetic hepatosclerosis as a hepatic microvascular complication of diabetes — contextual background only |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | Case Report | Cureus | Glycogen hepatopathy in Type 1 DM complicated by gastroparesis and DKA — gastroparesis mentioned as comorbidity, not treatment target |

> ⚠️ **Important**: None of the above publications evaluate Alanine as a treatment for gastroparesis. The literature was retrieved based on co-occurrence of search terms, not on direct mechanistic or clinical relevance.

---

## Singapore Market Information

Alanine (DrugBank ID: DB00160) has **no registered pharmaceutical products** in Singapore.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| — | No registered products | — | — |

> This drug has not been approved or registered as a pharmaceutical product in Singapore. Any clinical use would require regulatory authorization from scratch.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug interaction data were retrieved (query status: not found). No key warnings or contraindications data are available from the current evidence pack. As a naturally occurring amino acid, Alanine is generally considered safe at physiological concentrations, but pharmaceutical-grade dosing protocols, contraindications, and drug interaction profiles have not been established for therapeutic indications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Alanine is a naturally occurring amino acid with no approved therapeutic indications, no Singapore market presence, and no direct clinical evidence supporting its use for gastroparesis. All 9 clinical trials and 3 publications retrieved involve other drug interventions; the mechanistic link to gastroparesis is indirect (metabolic adjacency via the alanine-glucose cycle in diabetic contexts) rather than pharmacological. The TxGNN score reflects knowledge graph connectivity, not clinical efficacy.

**To proceed, the following is needed:**

- **Mechanistic proof-of-concept**: Preclinical studies demonstrating that exogenous Alanine supplementation can modulate gastric motility, gastric emptying rate, or enteric nervous system function in gastroparesis models
- **MOA characterization**: Formal DrugBank/literature review of any known effects of Alanine on gastrointestinal smooth muscle, autonomic signaling, or GLP-1/motilin pathways
- **Dose-response data**: Pharmacokinetic and pharmacodynamic studies establishing relevant therapeutic concentrations and routes of administration
- **Safety package**: Formal assessment of warnings, contraindications, and drug interactions for Alanine at pharmacological (non-nutritional) doses
- **Regulatory pathway clarification**: Consultation with Singapore HSA on the regulatory classification of amino acids when used as pharmaceutical agents (food supplement vs. drug)
- **Re-evaluation of prediction quality**: Consider whether high TxGNN scores for Alanine across metabolic disease nodes (ranks 1–10 span gastroparesis, vitamin D deficiency, dyspepsia, RTA, osteoporosis) indicate a genuine signal or systematic knowledge graph inflation due to Alanine's broad metabolic node connectivity

> **Note on alternate indications**: Among the top 10 predictions, **renal tubular acidosis** (Rank 6, L4 evidence) has the most biologically plausible mechanistic connection — direct studies document L-Alanine metabolism and transport in renal proximal tubules during metabolic acidosis (PMID 6410927, PMID 2051649). This indication warrants separate, dedicated evaluation before gastroparesis.

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

