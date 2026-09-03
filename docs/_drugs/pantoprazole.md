---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 753
evidence_level: L5
indication_count: 10
---

# Pantoprazole
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

# Pantoprazole: From Gastroesophageal Reflux Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI), a drug class originally developed for gastroesophageal reflux disease (GERD) and other acid-related disorders.
The TxGNN model predicts it may also be effective for **Active Peptic Ulcer Disease**,
with **3 clinical trials** and **19 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastroesophageal reflux disease (GERD) / erosive esophagitis — based on known PPI drug class information; no Singapore license text is available for this drug |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this evidence pack. Based on known pharmacology, Pantoprazole belongs to the proton pump inhibitor (PPI) class. It accumulates in the acidic secretory canaliculus of the gastric parietal cell, where it is acid-activated and then irreversibly binds to the H+/K+-ATPase ("proton pump"), blocking the final common step of gastric acid secretion. This precise, acid-triggered mechanism is described in the supporting literature (e.g., PMID 8930575, PMID 19938880).

Gastric acid suppression is the pharmacological basis for both GERD/erosive esophagitis (the drug's established use) and peptic ulcer healing — active peptic ulcers heal when intragastric pH is raised and sustained above the threshold needed for mucosal repair, and PPIs are also the backbone of H. pylori eradication regimens, a leading cause of peptic ulcer disease. The two indications therefore share an identical underlying mechanism rather than requiring a novel biological hypothesis.

This mechanistic overlap explains why the TxGNN prediction is strongly supported by direct clinical evidence rather than being purely speculative: a completed Phase 3, multicenter, double-blind, active-controlled trial (NCT02084420) directly evaluated pantoprazole-based triple therapy for H. pylori eradication in gastric/duodenal ulcer patients, and numerous randomized trials in the literature (e.g., PMID 18824852, PMID 15244210, PMID 10632647) confirm efficacy of pantoprazole in peptic ulcer healing and bleeding-ulcer management.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, double-blind, active-controlled trial comparing Ilaprazole vs. Pantoprazole triple therapy for 7-day H. pylori eradication in gastric and/or duodenal ulcer patients. |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated the influence of PPIs (including pantoprazole) and statins on clopidogrel antiplatelet effect in patients undergoing PCI; primarily a drug-interaction/safety study rather than direct ulcer efficacy. |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Prospective study identifying risk factors for poor stigmata fading or early rebleeding after endoscopic hemostasis and high-dose PPI infusion, used to define second-look endoscopy selection criteria in bleeding peptic ulcer. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Prospective RCT comparing intermittent vs. continuous pantoprazole infusion for peptic ulcer bleeding; both reduced rebleeding risk after endoscopic therapy. |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | RCT | Hepato-gastroenterology | Compared lansoprazole and pantoprazole in treatment of active duodenal ulcer with H. pylori eradication. |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Alimentary Pharmacology & Therapeutics | Pantoprazole plus amoxicillin and either azithromycin or clarithromycin achieved effective H. pylori eradication in duodenal ulcer. |
| [8930575](https://pubmed.ncbi.nlm.nih.gov/8930575/) | 1996 | Pharmacology study | European Journal of Gastroenterology & Hepatology | Describes pantoprazole's precise, acid-activated, selective mechanism of H+/K+-ATPase inhibition — the mechanistic basis for its use across acid-related diseases. |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Review (Systematic Review/Meta-analysis) | American Journal of Gastroenterology | Network meta-analysis comparing P-CABs and PPIs for healing severe (Grade C/D) esophagitis, providing contemporary context for PPI efficacy in acid-related mucosal disease. |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clinical Drug Investigation | Overview of pantoprazole pharmacology; notes long duration of action and absence of identified drug-drug interactions across numerous interaction studies. |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | Reviews PPIs (including pantoprazole) as more effective than H2-receptor antagonists for acid-related diseases including peptic ulcer. |
| [8930576](https://pubmed.ncbi.nlm.nih.gov/8930576/) | 1996 | PK study | European Journal of Gastroenterology & Hepatology | Analyzes CYP450-mediated metabolism of lansoprazole, omeprazole, and pantoprazole and resulting drug-drug interaction potential. |
| [10983736](https://pubmed.ncbi.nlm.nih.gov/10983736/) | 2000 | Review | Drugs | Comparative review of esomeprazole noting pantoprazole's intragastric pH control in GORD trials. |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | Prospective RCT | Journal of Gastroenterology and Hepatology | Pantoprazole infusion as adjuvant therapy to endoscopic treatment in peptic ulcer bleeding improved outcomes vs. endoscopic therapy alone. |

## Singapore Market Information

Pantoprazole is currently **not marketed** in Singapore under this evidence pack (0 registrations on file); no license records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between pantoprazole's acid-suppressing action and peptic ulcer healing is direct and pharmacologically well-established, and this is reinforced by a completed Phase 3 RCT (NCT02084420) plus multiple supporting randomized trials, yielding an L1 evidence level. However, the drug is not currently marketed in Singapore and key drug-level safety data are missing, so guardrails are warranted before any local repositioning decision.

**To proceed, the following is needed:**
- HSA/regulatory-agency label warnings and contraindications (currently a blocking data gap — required before any S1 safety pre-assessment)
- Confirmed mechanism of action data from DrugBank API (currently a data gap affecting mechanistic-linkage analysis)
- A formal drug-drug interaction (DDI) review, since the current query returned no results
- Singapore-specific market authorization/registration data, given the drug is presently unmarketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

