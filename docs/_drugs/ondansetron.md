---
layout: default
title: Ondansetron
parent: 僅模型預測 (L5)
nav_order: 734
evidence_level: L5
indication_count: 10
---

# Ondansetron
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

# Ondansetron: From Nausea and Vomiting to Tourette Syndrome

## One-Sentence Summary

Ondansetron is a selective 5-HT3 receptor antagonist originally developed as an antiemetic for chemotherapy-, radiotherapy-, and anaesthesia-induced nausea and vomiting. The TxGNN model's evidence-supported prediction points to **Tourette syndrome**, backed by **1 completed Phase 4 clinical trial** and **10 relevant publications**, including two randomized controlled trials spanning 1999–2025. Note: TxGNN's single highest-scoring prediction (nephrogenic syndrome of inappropriate antidiuresis) carries no clinical trial or literature support and is treated here as a low-confidence model artifact rather than the report focus — this report evaluates the best-evidenced candidate instead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antiemetic for cancer chemotherapy-/radiotherapy- and anaesthesia-related nausea and vomiting |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 97.96% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not supplied for this evidence pack, but the literature captured in this pack confirms Ondansetron's established role: a selective 5-hydroxytryptamine-3 (5-HT3) receptor antagonist used clinically as an antiemetic for cancer-treatment-induced and anaesthesia-related nausea and vomiting (PMID 11474424).

The repurposing hypothesis for Tourette syndrome rests on the fact that 5-HT3 receptors modulate dopamine and glutamate release within the cortico-striatal-thalamic circuitry — the same circuitry implicated in tic generation. This is a biologically plausible mechanistic link, but it is not the primary dopamine D2-blockade pathway that underlies first-line TS pharmacotherapy, so the mechanism should be regarded as a secondary/modulatory hypothesis rather than a proven causal pathway.

This hypothesis is not purely computational: an open-label pilot (1999), a 3-week randomized double-blind placebo-controlled trial (2005), and a completed Phase 4 RCT with MRI-based brain connectivity endpoints (2017–2022, published 2025) have each tested ondansetron directly in Tourette/tic-spectrum populations, giving the prediction more grounding than a typical L5 model-only signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03239210](https://clinicaltrials.gov/study/NCT03239210) | Phase 4 | Completed | 110 | Randomized, placebo-controlled trial of 24 mg/day ondansetron for 4 weeks in patients with OCD and tic disorders (including Tourette syndrome), assessing symptom change and brain functioning via MRI at baseline and week 4. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39876680](https://pubmed.ncbi.nlm.nih.gov/39876680/) | 2025 | RCT | The American Journal of Psychiatry | High-dose ondansetron vs. placebo for 4 weeks reduced sensory-phenomena severity and modulated interoceptive-sensorimotor brain connectivity in OCD/Tourette's disorder. |
| [15816793](https://pubmed.ncbi.nlm.nih.gov/15816793/) | 2005 | RCT | The Journal of Clinical Psychiatry | 3-week randomized, double-blind, placebo-controlled study evaluating ondansetron efficacy specifically in Tourette's disorder. |
| [10565805](https://pubmed.ncbi.nlm.nih.gov/10565805/) | 1999 | Cohort (open-label) | International Clinical Psychopharmacology | Open-label pilot in 6 haloperidol-resistant Tourette's syndrome patients; ondansetron (8–16 mg) assessed via YGTSS, Y-BOCS, and TS-CGI scales. |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Review | Medicine | Narrative review of Phase III/IV pharmacological trials for Tourette syndrome across age groups, contextualizing ondansetron among emerging treatment options. |
| [21183132](https://pubmed.ncbi.nlm.nih.gov/21183132/) | 2010 | Review | Seminars in Pediatric Neurology | Summary of RCTs for Tourette syndrome and autism-related stereotypies (2005–2010), covering pharmacotherapeutic options including serotonergic agents. |
| [18184945](https://pubmed.ncbi.nlm.nih.gov/18184945/) | 2008 | Case report | Journal of Child Neurology | An 8-year-old boy with leukemia and Tourette syndrome given ondansetron for chemotherapy-induced nausea showed incidental relief of tic symptoms, which recurred on dose reduction. |
| [11474424](https://pubmed.ncbi.nlm.nih.gov/11474424/) | 2001 | Review | CNS Drug Reviews | Review of ondansetron's pharmacology as a 5-HT3 antagonist and its exploratory applications in CNS-related disorders. |
| [16314763](https://pubmed.ncbi.nlm.nih.gov/16314763/) | 2005 | Genetic association study | Psychiatric Genetics | HTR3A/HTR3B (5-HT3 receptor subunit) gene sequence variants were examined in Tourette syndrome patients; no association found, despite ondansetron's proposed use in GTS. |
| [21568361](https://pubmed.ncbi.nlm.nih.gov/21568361/) | 2011 | Review | Drugs | Review of shared features and potential treatments across OCD, impulse control disorders, and addiction — tangential context for tic-spectrum overlap. |
| [23126479](https://pubmed.ncbi.nlm.nih.gov/23126479/) | 2013 | Genetic study | Nordic Journal of Psychiatry | Investigated 5-HTR3A polymorphism and tardive dyskinesia in schizophrenia; references prior reports of ondansetron efficacy in Tourette syndrome as background. |

---

## Singapore Market Information

Ondansetron currently has no registered product licenses in this evidence pack (0 registrations; market status: Not Marketed). No local dossier, brand, or approved indication text is available for Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction records were returned for Ondansetron in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome hypothesis has meaningfully more support than a typical model-only prediction — a completed Phase 4 RCT plus a 25-year span of RCT, cohort, and case-report literature (L2 evidence) — but Ondansetron is not currently registered in Singapore, and local safety-label data (warnings/contraindications) is a **Blocking** data gap that prevents entry into the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- HSA/local package insert warnings, contraindications, and precautions (Blocking gap DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High-priority gap DG002)
- Drug-drug interaction data (current DDI query returned no results)
- A larger, adequately powered confirmatory RCT specifically in a Tourette syndrome population before considering guardrailed research use
- Clarification of Singapore registration pathway status, given the drug is currently unmarketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

