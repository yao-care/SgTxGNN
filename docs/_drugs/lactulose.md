---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 568
evidence_level: L5
indication_count: 10
---

# Lactulose
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

Using the evidence pack data directly (no fabrication), I'm featuring the prediction with the strongest actual evidentiary support — **obstructive jaundice** (rank 3, L3 evidence: 1 completed trial + 20 publications) — rather than the top TxGNN-scored candidate (*acute urate nephropathy*, rank 1), because the pack's own mechanistic analysis flags rank 1 as very likely knowledge-graph noise (zero trials, zero literature, "Hold"). Presenting a report anchored on an unsupported top score would misrepresent the evidence.

---

# Lactulose: From Constipation / Hepatic Encephalopathy to Obstructive Jaundice

## One-Sentence Summary

Lactulose is a non-absorbable osmotic disaccharide with long-established use for **constipation** and **hepatic encephalopathy**. Among 10 TxGNN-predicted indications in this evidence pack, the one with genuine supporting evidence — rather than the highest raw model score — is **Obstructive Jaundice**, where lactulose's gut-acidifying, anti-endotoxin effect has been studied as a perioperative renal-protective adjunct. This direction is supported by **1 completed Phase 4 clinical study** and **20 relevant publications**, though no modern RCT confirms clinical benefit and the drug is not currently registered in Singapore.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation; Hepatic Encephalopathy (established pharmacological use — no Singapore regulatory filing exists to cite formal wording, see note below) |
| Predicted New Indication | Obstructive Jaundice |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

*Note: `taiwan_regulatory.licenses` is empty and `original_moa` is a documented data gap (DG002), so the "Original Indication" above reflects lactulose's globally recognized pharmacological classification rather than an HSA-approved label — this is corroborated within the evidence pack itself (e.g., PMID 9145459 describes lactulose's established role in hepatic encephalopathy).*

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for this candidate is currently a documented gap (DG002, High severity) and could not be retrieved from DrugBank. Based on well-established pharmacology, lactulose is a non-absorbable synthetic disaccharide that reaches the colon largely intact, where it is fermented by colonic bacteria to short-chain organic acids. This acidifies the colonic lumen, converts ammonia (NH₃) to the non-absorbable ammonium ion (NH₄⁺), and — of particular relevance here — has been reported to reduce colonic bacterial endotoxin production and gut-wall permeability.

Obstructive jaundice prevents bile salts from reaching the intestine, which is thought to promote small-intestinal bacterial overgrowth, increased gut permeability, and translocation of bacterial endotoxin into the portal and systemic circulation ("cholemic nephrosis" pathway). This endotoxemia is implicated in postoperative renal impairment and septic complications in these patients. Because lactulose's anti-endotoxin, gut-barrier-protective action is mechanistically positioned upstream of this pathway, several research groups from the 1980s–2000s tested it as a **preoperative adjunct** to reduce endotoxemia and postoperative renal dysfunction in obstructive jaundice patients — this is an indirect, gut–liver–kidney axis protective effect, not a direct treatment of the biliary obstruction itself.

It is important to note this is a supportive/preventive role alongside surgical decompression, not a stand-alone cure for obstructive jaundice, and the evidence base predates modern RCT standards.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01090193](https://clinicaltrials.gov/study/NCT01090193) | Phase 4 | Completed | 20 | Prospective study characterizing renal histopathological changes in patients with acute obstructive jaundice, examining cholemia/portal endotoxemia as drivers of kidney injury. Observational in design — does not directly test lactulose as an intervention. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3768644](https://pubmed.ncbi.nlm.nih.gov/3768644/) | 1986 | Clinical/Cohort study | The British Journal of Surgery | Prospective study of 24 surgical obstructive jaundice patients; oral lactulose (n=12) significantly reduced portal and systemic endotoxemia vs. untreated controls (P<0.05). |
| [2032107](https://pubmed.ncbi.nlm.nih.gov/2032107/) | 1991 | Multicentre cohort/RCT | The British Journal of Surgery | Randomized trial (n=102) comparing preoperative lactulose vs. sodium deoxycholate vs. no treatment for prevention of postoperative renal dysfunction in obstructive jaundice. |
| [17708248](https://pubmed.ncbi.nlm.nih.gov/17708248/) | 2007 | Cohort study | Hepato-Gastroenterology | Identifies endotoxemia-driven hemodynamic changes as predictors of mortality/morbidity in acute obstructive jaundice, framing the rationale for endotoxin-reducing preventive measures. |
| [29428098](https://pubmed.ncbi.nlm.nih.gov/29428098/) | 2018 | Review | Hepatobiliary & Pancreatic Diseases International | Reviews the pathophysiology and perioperative management of obstructive jaundice, including endotoxemia and renal complications. |
| [12957136](https://pubmed.ncbi.nlm.nih.gov/12957136/) | 2003 | Review / animal model | Journal of Surgical Research | Bile-duct-ligated rabbit model evaluating lactulose's role in preventing systemic endotoxemia following obstructive jaundice. |
| [9145459](https://pubmed.ncbi.nlm.nih.gov/9145459/) | 1997 | Review | Scandinavian Journal of Gastroenterology (Suppl.) | Confirms lactulose's established role in hepatic encephalopathy; notes a hypothesized reno-protective effect (via reduced endotoxinemia) in obstructive jaundice has **not** been conclusively demonstrated clinically. |
| [9174857](https://pubmed.ncbi.nlm.nih.gov/9174857/) | 1997 | Review | HPB Surgery | Reviews immune dysfunction and mediators contributing to perioperative complication risk (sepsis, renal/liver dysfunction) in obstructive jaundice. |
| [3283963](https://pubmed.ncbi.nlm.nih.gov/3283963/) | 1988 | Review | Surgery Annual | Reviews renal failure and other endotoxin-related complications in obstructive jaundice. |
| [2614579](https://pubmed.ncbi.nlm.nih.gov/2614579/) | 1989 | Review/cohort (rat model) | The Journal of Pathology | Bile-duct ligation rat study; lactulose (with polymyxin B/neomycin) did **not** prevent bile infarction or transaminase elevation — a negative/mixed finding for the anti-endotoxin hypothesis. |
| [12598962](https://pubmed.ncbi.nlm.nih.gov/12598962/) | 2002 | Animal study | Pediatric Surgery International | Rat study of melatonin and lactulose effects on liver and kidney histopathology in obstructive jaundice. |

## Safety Considerations

Please refer to the package insert for safety information. *(All safety fields — key warnings, contraindications, and drug interactions — are documented data gaps in this evidence pack; DG001, Blocking severity, flags that HSA/TFDA label warnings and contraindications must be sourced before any S1 safety review can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (endotoxin/gut-permeability reduction) is biologically plausible and supported by several small clinical and animal studies from 1986–2007, but there is no modern RCT confirming clinical benefit, findings are mixed (e.g., PMID 2614579 was negative), lactulose has no Singapore (HSA) registration, and both the formal mechanism-of-action data and safety/contraindication data are blocking gaps (DG001, DG002). This is insufficient to support a "Go" or "Proceed with Guardrails" decision at this time.

**To proceed, the following is needed:**
- HSA/TFDA package insert data — warnings, contraindications, and DDI profile (resolves blocking gap DG001)
- Confirmed DrugBank mechanism-of-action record (resolves DG002)
- A contemporary, adequately powered RCT testing lactulose specifically for reduction of postoperative renal dysfunction/endotoxemia in obstructive jaundice patients
- Reassessment of the discordant top-ranked TxGNN candidates (e.g., acute urate nephropathy, exercise-induced malignant hyperthermia) to determine whether they represent genuine signal or model artifact before any further investment in this drug-indication pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

