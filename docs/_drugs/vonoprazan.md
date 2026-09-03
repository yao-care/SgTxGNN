---
layout: default
title: Vonoprazan
parent: 僅模型預測 (L5)
nav_order: 1065
evidence_level: L5
indication_count: 10
---

# Vonoprazan
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

# Vonoprazan: From Unregistered Status in Singapore to Active Peptic Ulcer Disease

## One-Sentence Summary

Vonoprazan is a first-in-class potassium-competitive acid blocker (P-CAB), approved overseas (e.g., Japan, as Takecab®) for gastric/duodenal ulcer, reflux esophagitis, and *H. pylori* eradication, but it currently holds **no registration in Singapore**. The TxGNN model's top-ranked prediction — **Active Peptic Ulcer Disease** — largely reconfirms this drug's core, already-established mechanism of action rather than identifying a genuinely novel use, with **2 clinical trials** and **17 publications** supporting the underlying pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; approved overseas (Japan) for gastric ulcer, duodenal ulcer, reflux esophagitis, and *H. pylori* eradication (as Takecab®) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, DrugBank's structured MOA field is not populated for this drug (Data Gap DG002). Based on the evidence pack's own repurposing rationale and the supporting literature, however, Vonoprazan's mechanism is well characterized: it is a **potassium-competitive acid blocker (P-CAB)** that directly and reversibly inhibits the H⁺/K⁺-ATPase proton pump on gastric parietal cells, producing faster, more potent, and more sustained acid suppression than conventional PPIs.

Critically, the evidence pack itself flags that this "predicted" indication is **not a speculative repurposing** — active peptic ulcer disease (gastric/duodenal ulcer, reflux esophagitis) is Vonoprazan's core, already-approved indication in markets such as Japan (marketed as Takecab® since 2015). The TxGNN prediction therefore functions less as a discovery of new biology and more as a **confirmation signal**, highlighting that Singapore's market lacks a registration for a mechanism-matched, globally validated indication.

Because acid suppression is the rate-limiting step in both ulcer healing and *H. pylori* eradication, the mechanistic fit between Vonoprazan's pharmacology and peptic ulcer disease is direct and non-inferential — unlike typical TxGNN cross-disease repurposing hypotheses that rely on indirect network relationships.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03214952](https://clinicaltrials.gov/study/NCT03214952) | N/A (Post-marketing surveillance) | Completed | 3,183 | Large real-world drug-use surveillance confirming safety and effectiveness of vonoprazan (Takecab) in gastric ulcer, duodenal ulcer, and reflux esophagitis |
| [NCT03116841](https://clinicaltrials.gov/study/NCT03116841) | Phase 4 | Completed | 3 | Exploratory study on vonoprazan's effect on sleep disturbance in reflux esophagitis patients; small sample, indirect relevance to ulcer disease itself |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28988197](https://pubmed.ncbi.nlm.nih.gov/28988197/) | 2018 | RCT | Gut | Vonoprazan non-inferior to lansoprazole for secondary prevention of NSAID-induced peptic ulcer, with confirmed long-term safety |
| [28267236](https://pubmed.ncbi.nlm.nih.gov/28267236/) | 2017 | RCT | Dig Endosc | Prospective RCT showing vonoprazan's healing effect on post-ESD artificial gastric ulcers |
| [39156336](https://pubmed.ncbi.nlm.nih.gov/39156336/) | 2024 | Review | Cureus | Comprehensive review of vonoprazan's efficacy and safety across GERD, peptic ulcer disease, and *H. pylori* infection |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review/Meta-analysis | Am J Gastroenterol | Network meta-analysis showing P-CABs (incl. vonoprazan) outperform PPIs in healing severe (Grade C/D) esophagitis |
| [26369775](https://pubmed.ncbi.nlm.nih.gov/26369775/) | 2016 | PK/PD Study | Clin Pharmacokinet | Foundational PK/PD profile confirming approved dosing for gastroduodenal ulcer, reflux esophagitis, and NSAID-ulcer prevention |
| [32998241](https://pubmed.ncbi.nlm.nih.gov/32998241/) | 2020 | Review | Pharmaceuticals (Basel) | Reviews vonoprazan's potential advantages over PPI-based regimens for *H. pylori* eradication and ulcer recurrence prevention |
| [36660052](https://pubmed.ncbi.nlm.nih.gov/36660052/) | 2023 | Review | JGH Open | Overview of *H. pylori* infection spectrum, from peptic ulcer disease to gastric cancer, and role of eradication therapy |
| [37066678](https://pubmed.ncbi.nlm.nih.gov/37066678/) | 2023 | PK/PD Study | Aliment Pharmacol Ther | Translational PK/PD analysis supporting optimal vonoprazan dosing for erosive esophagitis and *H. pylori* infection |
| [41472371](https://pubmed.ncbi.nlm.nih.gov/41472371/) | 2026 | Review | J Gastroenterol Hepatol | Discusses rising *H. pylori* antibiotic resistance in Asia-Pacific, relevant to acid-suppression-based eradication regimens |
| [41735211](https://pubmed.ncbi.nlm.nih.gov/41735211/) | 2026 | Systematic Review | Curr Top Med Chem | Broader review of peptic ulcer treatment landscape (2018–2024), contextualizing conventional vs. novel acid suppressants |

---

## Singapore Market Information

Currently no Singapore (HSA) registrations exist for this drug — `taiwan_regulatory.total_licenses = 0` and no license records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all currently marked as data gaps — notably DG001, a **Blocking** severity gap for local label warnings/contraindications, which must be resolved before any S1 safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Vonoprazan and active peptic ulcer disease is direct rather than speculative — this is the drug's globally established core indication (approved in Japan since 2015), supported by a large post-marketing surveillance study (n=3,183) and multiple RCTs/reviews (Evidence Level L1). However, the drug is **not registered in Singapore**, and critical local safety data (HSA label warnings/contraindications, DG001) is missing, which blocks a full safety pre-assessment.

**To proceed, the following is needed:**
- Local package insert / HSA label data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Formal DrugBank MOA record retrieval to close the mechanism-of-action data gap (DG002)
- Drug-drug interaction (DDI) profile — currently "not_found" in the evidence pack
- A regulatory filing strategy for Singapore market registration, given the drug's already-established efficacy/safety profile abroad
- For completeness, lower-confidence candidate indications (ranks 2–10, e.g., peptic ulcer perforation, gastrojejunal ulcer) remain at evidence levels L3–L5 and are not ready for action; they are noted here only as lower-priority research questions, not part of this recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

