---
layout: default
title: Ranitidine
parent: 僅模型預測 (L5)
nav_order: 844
evidence_level: L5
indication_count: 10
---

# Ranitidine
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

# Ranitidine: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Ranitidine is a histamine H2-receptor antagonist historically used to treat peptic ulcer disease and gastric hypersecretory conditions.
The TxGNN model's top prediction — **active peptic ulcer disease** — is essentially a rediscovery of the drug's own original approved use rather than a genuine new indication, and is supported by **1 clinical trial** and **20 publications**, though most were not run specifically to test this prediction.
Critically, ranitidine has been withdrawn from global markets (including no active Taiwan registration) since 2020 due to NDMA (a probable carcinogen) contamination, which overrides the otherwise strong efficacy evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease / gastric hypersecretory conditions (H2-receptor antagonist) — no active Taiwan license on file |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not marketed / withdrawn) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in DrugBank for this evidence pack. Based on known pharmacology, ranitidine is a competitive, selective histamine H2-receptor antagonist that blocks parietal cell H2 receptors, reducing basal and stimulated gastric acid secretion. This mechanism directly underlies its decades-long, well-established use in healing and preventing peptic ulcers.

The predicted indication, "active peptic ulcer disease," is mechanistically identical to the drug's known original use — both represent the same acid-related mucosal injury pathophysiology treated by the same acid-suppression mechanism. As the evidence pack itself notes for the closely related entry "peptic ulcer disease" (rank 7): *"TxGNN is 'rediscovering' an existing indication rather than proposing a true repurposing candidate."* This should be read as a validation signal for the model's pharmacological reasoning rather than a novel drug-repurposing opportunity.

The overriding consideration for this candidate is regulatory, not mechanistic: ranitidine was withdrawn worldwide starting in 2020 after N-nitrosodimethylamine (NDMA), a probable human carcinogen, was found to form in the product under normal storage conditions. This explains why Taiwan market status shows zero active registrations despite decades of proven efficacy — and it is the reason evidence strength alone cannot support a "Go" decision.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated the influence of statins and proton pump inhibitors (not ranitidine) on clopidogrel antiplatelet effects in PCI patients; ranitidine is not the study drug (relevance grade C — tangential). |

*Note: No trial in this evidence set directly tests ranitidine as a treatment specifically for "active peptic ulcer disease" as a repurposing hypothesis; broader peptic-ulcer-disease trials with ranitidine as comparator are listed under the closely related "peptic ulcer disease" entry (rank 7).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scand J Gastroenterol | Ranitidine 300 mg/day healed 91% of duodenal ulcers, 68% of prepyloric ulcers, and 81% of gastric corporeal ulcers at 4 weeks; maintenance therapy reduced relapse vs placebo. |
| [2491360](https://pubmed.ncbi.nlm.nih.gov/2491360/) | 1989 | RCT | J Gastroenterol Hepatol | Randomized double-blind trial (n=270) comparing omeprazole 10/20 mg vs ranitidine 150 mg bid for duodenal ulcer healing and relapse. |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | RCT | Am J Med | Multicenter, double-blind, randomized international study (n=1,031) comparing famotidine vs ranitidine for active duodenal ulcer healing. |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | RCT | Clin Ther | Multicenter study (n=160) comparing famotidine and ranitidine for active duodenal ulcer healing and 6-month maintenance, including NSAID/aspirin-related ulcers. |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intell Clin Pharm | Reviews ranitidine's approval for short-term treatment of active duodenal ulcers and gastric hypersecretory conditions; 4–10x more potent than cimetidine. |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepatogastroenterology | Reviews acid suppression as central to peptic ulcer pathogenesis and healing, contextualizing H2-antagonist efficacy including ranitidine. |
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | Comparative study | Klin Wochenschr | Compared nocturnal rioprostil (prostaglandin E1 analogue) vs ranitidine for duodenal ulcer healing. |
| [1717223](https://pubmed.ncbi.nlm.nih.gov/1717223/) | 1991 | Review | Drugs | Reviews roxatidine acetate, an H2-antagonist with pharmacodynamics/therapeutic potential compared against ranitidine-class agents in peptic ulcer disease. |
| [3527658](https://pubmed.ncbi.nlm.nih.gov/3527658/) | 1986 | Review | Drugs | Reviews omeprazole's pharmacodynamics and therapeutic potential in peptic ulcer disease and Zollinger-Ellison syndrome, benchmarked against H2-antagonists. |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Reviews nizatidine, an H2-receptor antagonist more potent than cimetidine, for peptic ulcer disease. |

---

## Singapore Market Information

Currently no registration records — `taiwan_regulatory.total_licenses = 0` and `market_status = 未上市 (not marketed)`. Ranitidine has been withdrawn worldwide since 2020 due to NDMA contamination, consistent with the absence of an active Taiwan license.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug-drug interactions) is available in this evidence pack — all fields are marked as data gaps, and the DDI lookup returned no results.

- **Regulatory safety flag (from evidence pack context):** Ranitidine products were withdrawn globally starting in 2020 after detection of NDMA, a probable human carcinogen, forming under normal storage/shelf-life conditions. This is the primary safety consideration for any repurposing evaluation of this drug, independent of the specific new indication.

Please refer to the original package insert (prior to withdrawal) or updated TFDA guidance for detailed prescribing safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction largely reconfirms ranitidine's known original indication rather than identifying a genuinely new therapeutic use, and — more decisively — the drug is not currently marketed in Taiwan and has been withdrawn globally due to NDMA carcinogenicity concerns, blocking any safety-stage (S1) advancement regardless of efficacy evidence strength.

**To proceed, the following is needed:**
- TFDA-approved label warnings/contraindications (currently a Blocking data gap — required before S1 safety evaluation can begin)
- Detailed DrugBank mechanism of action (MOA) data (High-severity data gap)
- Confirmation of whether an NDMA-free reformulation exists that could be considered for regulatory resubmission
- If pursuing genuinely novel candidates instead, prioritize lower-ranked, non-original indications (e.g., "gastroduodenitis," evidence level L2) with dedicated literature relevance grading, since much of the current literature classification remains "pending"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

