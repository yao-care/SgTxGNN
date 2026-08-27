---
layout: default
title: Metoclopramide
parent: 僅模型預測 (L5)
nav_order: 656
evidence_level: L5
indication_count: 10
---

# Metoclopramide
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

# Metoclopramide: From Antiemetic/Prokinetic Use to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a dopamine (D2) receptor antagonist historically used as a routine antiemetic and gastrointestinal prokinetic agent. The TxGNN model predicts it may be effective for **Gastric Ulcer (disease)**, with **2 clinical trials** and **20 publications** currently associated with this candidate — though, as detailed below, most of this evidence is indirect (adjunctive-use trials and older preclinical studies) rather than direct proof of ulcer-healing efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in this evidence pack — the drug has no Singapore marketing license on file. Literature within the pack (PMID 6336644) describes its historical use as a routine antiemetic and GI prokinetic agent. |
| Predicted New Indication | Gastric Ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002, requiring a DrugBank API lookup). Based on literature captured within the pack itself, metoclopramide is a dopamine antagonist that acts on the medullary chemoreceptor trigger zone (its antiemetic effect) and stimulates gastrointestinal smooth-muscle activity by antagonizing dopamine and augmenting acetylcholine release, thereby accelerating gastric emptying and upper-GI motility (Albibi & McCallum, 1983, PMID 6336644).

Gastric ulcer and metoclopramide's established uses share the same anatomical territory — the upper gastrointestinal tract — which likely drives the knowledge-graph association. However, the evidence pack's own mechanistic assessment is candid about a limitation: metoclopramide has **no acid-suppressing action**, and ulcer healing is conventionally acid-suppression- or mucosal-protection-driven. Most of the associated clinical trials and literature address *adjunctive* contexts — premedication before endoscopy in active upper GI bleeding (NCT05746377), or preoperative gastric-content clearance — rather than ulcer-healing efficacy per se. A handful of older animal studies (rats, guinea pigs, 1980s) do report an "ulcer-protective" effect independent of acid secretion, attributed to promotion of gastric drainage and reduced pyloric reflux (PMID 2730234, PMID 6436177), which offers a plausible but unconfirmed mechanistic thread.

In short, the mechanistic rationale is biologically plausible (motility-mediated mucosal protection) but indirect, and it has not been tested in a controlled clinical trial specifically designed to assess ulcer healing. The very high TxGNN score should be interpreted as reflecting strong topological/graph proximity to gastric-ulcer-related entities rather than confirmed causal therapeutic evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Tests metoclopramide as endoscopy premedication in upper GI bleeding, assessing whether it reduces need for repeat endoscopy/IR/surgery and improves mucosal visibility — an adjunctive-use trial, not an ulcer-healing trial. |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist-led prescribing-safety quality improvement program in Scottish primary care; not disease-specific and only tangentially relevant. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT | Yonsei Medical Journal | Double-blind RCT comparing IV metoclopramide + ranitidine vs. saline for reducing preoperative gastric contents before laparoscopic surgery — a peri-procedural motility endpoint, not ulcer treatment. |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | General review of drug treatments for gastric and duodenal ulcer (abstract not available). |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Annals of Internal Medicine | Describes metoclopramide's dopamine-antagonist pharmacology, its role as a routine antiemetic (including chemotherapy-induced nausea/vomiting), and its GI prokinetic effects via acetylcholine augmentation. |
| [797497](https://pubmed.ncbi.nlm.nih.gov/797497/) | 1976 | Review | Clinical Pharmacokinetics | General review of how disease states and drugs (including gastric ulcer) alter gastric emptying and drug absorption. |
| [11879596](https://pubmed.ncbi.nlm.nih.gov/11879596/) | 2002 | Review | Current Treatment Options in Gastroenterology | Review of functional (non-ulcer) dyspepsia management; prokinetics discussed as symptomatic options, not ulcer-specific therapy. |
| [6659560](https://pubmed.ncbi.nlm.nih.gov/6659560/) | 1983 | Review | Yale Journal of Biology and Medicine | Review of diabetic gastric dysfunction, noting reduced peptic ulcer frequency in diabetics — background context rather than direct evidence. |
| [18097282](https://pubmed.ncbi.nlm.nih.gov/18097282/) | 2008 | Review/Case Series | Journal of Clinical Gastroenterology | Review of GI involvement in systemic sclerosis, including delayed gastric emptying — background pathophysiology, not ulcer-treatment evidence. |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal Study | Archives Internationales de Pharmacodynamie et de Therapie | In aspirin-induced and pylorus-ligated rat models, metoclopramide (20–50 mg/kg) produced an ulcer-protective effect comparable in some respects to ranitidine, without a secretory (acid-suppressing) mechanism. |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal Study | Indian Journal of Physiology and Pharmacology | In guinea pigs, metoclopramide protected against several experimental gastric ulceration models without affecting gastric acid secretion, suggesting a gastric-drainage-mediated protective mechanism. |
| [28652516](https://pubmed.ncbi.nlm.nih.gov/28652516/) | 2017 | Animal Study | Journal of Smooth Muscle Research | Rat study of prokinetic drug effects on gastric emptying after artificial ulceration, examining regional differences by ulcer location. |

## Singapore Market Information

Metoclopramide currently has **no marketing authorization on file in Singapore** (`taiwan_regulatory.total_licenses = 0`, `market_status = 未上市/Not Marketed`). No product name, dosage form, or approved-indication text is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data are currently available in this evidence pack — retrieval of the local product label (warnings/contraindications) is flagged as a **Blocking** data gap (DG001), and the DDI query returned no results (`not_found`, 0 interactions), so absence of findings should not be read as absence of risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug has zero Singapore registrations and no available safety labeling (warnings/contraindications are a Blocking data gap that prevents even an initial S1 safety screen), and the mechanistic/clinical case for the top-ranked indication (gastric ulcer) is indirect — no completed RCT demonstrates ulcer-healing efficacy; supporting trials address adjunctive motility endpoints, and the strongest direct evidence is decades-old animal-model work. The evidence level (L3) and decision stage (S1, "Research Question") both indicate this is not yet actionable.

**To proceed, the following is needed:**
- Retrieve the TFDA/local product label for warnings and contraindications (Blocking gap, DG001) before any safety screening can proceed.
- Retrieve confirmed mechanism-of-action data from DrugBank API (High-priority gap, DG002).
- Re-verify the drug-drug interaction profile, since the current query returned no results rather than a confirmed "no interactions" finding.
- Commission or identify a study designed specifically to test ulcer-healing efficacy (not just gastric motility/emptying) to close the gap between the indirect mechanistic rationale and a genuine therapeutic claim.
- Clarify Singapore registration/route-of-administration status should repurposing be pursued locally, given the drug is not currently marketed there.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

