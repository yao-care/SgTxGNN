---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 732
evidence_level: L5
indication_count: 10
---

# Omeprazole
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

# Omeprazole: From Peptic Ulcer Disease / GERD to Duodenogastric Reflux

## One-Sentence Summary

Omeprazole is a proton pump inhibitor (PPI) originally established for acid-related disorders such as peptic ulcer disease and gastroesophageal reflux disease (GERD).
The TxGNN model's top-ranked prediction points to **Duodenogastric Reflux**,
but the supporting evidence — **1 clinical trial** and **20 publications** — leans cautionary rather than confirmatory, since omeprazole targets acid, not the bile component that defines this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease / GERD (acid-related disorders) — inferred from PPI-class literature in this evidence pack; no Singapore license record available |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, omeprazole belongs to the proton pump inhibitor (PPI) class, irreversibly inhibiting the H⁺/K⁺-ATPase ("proton pump") of gastric parietal cells to suppress acid secretion. Its efficacy in peptic ulcer disease and GERD is well established, and the underlying mechanism is directly on the acid-secretion axis.

Duodenogastric reflux (DGR), however, is a mixed reflux condition involving both gastric acid **and** duodenal/biliary content. Because omeprazole only addresses the acid component, its applicability to DGR is mechanistically partial at best — the KG association likely arises from shared anatomical/keyword overlap ("gastric," "duodenal," "reflux") rather than a direct causal treatment relationship.

More importantly, several of the supporting literature entries raise a safety signal rather than a benefit signal: animal studies (PMID 10389684, PMID 33027361) suggest that gastric acid blockade with omeprazole may *promote* gastric carcinogenesis when combined with duodenogastric reflux, because prolonged elevation of intragastric pH can increase the cytotoxic potential of bile-containing refluxate on the foregut mucosa. This reframes the "prediction" as a research question about risk, not a straightforward repurposing opportunity.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | N/A | Completed | 157 | Evaluated endoscopic tri-modal imaging (NBI/AFI/WLI) to distinguish functional dyspepsia from reflux disease (acid or bile); a diagnostic-tool study, not a drug efficacy trial (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | RCT | Gut | Evaluated omeprazole 20 mg twice daily on duodenogastric and duodenogastro-oesophageal bile reflux in Barrett's oesophagus. |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Cohort | Scand J Gastroenterol | Long-term acid suppression raises intragastric pH, which can increase cytotoxicity of duodenal refluxate; recent work suggests omeprazole may reduce antral DGR. |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Cohort | J Pediatr Gastroenterol Nutr | Prospective study of PPI (omeprazole) therapy for oesophageal bile reflux in children. |
| [9841990](https://pubmed.ncbi.nlm.nih.gov/9841990/) | 1998 | Cohort | J Gastrointest Surg | Bilitec monitoring of bile reflux in benign vs. malignant Barrett's oesophagus; assessed effect of medical acid suppression and Nissen fundoplication. |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Animal | Dig Dis Sci | Rat model: gastric acid blockade with omeprazole promoted gastric carcinogenesis induced by duodenogastric reflux — key safety signal. |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Animal | Acta Cir Bras | Investigated whether omeprazole has a protective or promoting effect on gastric adenocarcinoma in rats with induced DGR. |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Review | Eur J Pediatr | Primary duodenogastric reflux in children/adolescents — rare disorder, atypical symptoms unresponsive to classical antacid therapy. |
| [11552908](https://pubmed.ncbi.nlm.nih.gov/11552908/) | 2001 | Cohort | Aliment Pharmacol Ther | PPI class (pantoprazole) effect on oesophageal motility and bile/acid reflux in oesophagitis patients — same-class indirect evidence. |
| [8076761](https://pubmed.ncbi.nlm.nih.gov/8076761/) | 1994 | Cohort | Gastroenterology | Examined relationship of pH, duodenogastroesophageal reflux, and bile acid concentration in producing oesophageal damage. |
| [21916229](https://pubmed.ncbi.nlm.nih.gov/21916229/) | 2011 | Cohort | Exp Clin Gastroenterol | Characteristics of DGR in duodenal ulcer patients and its dynamics after H. pylori eradication. |

## Singapore Market Information

No HSA/Singapore license records are present in this evidence pack (0 registrations; market status: not marketed). This reflects the data captured for this candidate, not necessarily global unavailability of generic omeprazole.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not available in this evidence pack; DDI query returned no results.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (duodenogastric reflux) is supported only by observational/animal-level evidence (L3) and a single non-therapeutic diagnostic trial. Critically, part of that evidence base flags a potential harm — long-term acid suppression combined with DGR may promote gastric carcinogenesis in animal models — rather than demonstrating benefit, and omeprazole's core mechanism does not address the bile component that defines DGR. A Blocking data gap (missing TFDA/HSA label warnings and contraindications) also prevents completion of the S1 safety screen. By contrast, a lower-ranked prediction in this same evidence pack — active peptic ulcer disease (L1, S3, Proceed with Guardrails) — reflects omeprazole's already-established, well-evidenced use rather than a genuinely new indication.

**To proceed, the following is needed:**
- Local package insert / label warnings and contraindications (resolves the Blocking data gap)
- Confirmed mechanism of action data via DrugBank API
- Drug-drug interaction data (current DDI query returned no results)
- A controlled clinical trial testing omeprazole specifically in DGR patients (current evidence is observational/animal only)
- A dedicated risk assessment of the acid-suppression + carcinogenesis signal before any further advancement of this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

