---
layout: default
title: Famotidine
parent: 僅模型預測 (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
---

# Famotidine
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

# Famotidine: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Famotidine is a potent, highly selective histamine H2-receptor antagonist globally established for suppressing gastric acid secretion in peptic ulcer disease and related acid-mediated conditions, though it currently holds no Singapore regulatory registration.
The TxGNN model predicts it may be effective for **Duodenogastric Reflux**, with **0 clinical trials** and **2 publications** currently supporting this specific direction.
The prediction score of 99.99% reflects strong model confidence, though clinical evidence for this exact indication remains limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally established for peptic ulcer disease and gastric acid hypersecretion |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Famotidine is a highly selective antagonist of histamine H2 receptors located on the basolateral surface of gastric parietal cells. By competitively blocking these receptors, famotidine suppresses both basal and stimulated gastric acid secretion. On a weight-for-weight basis, it is approximately 20–50 times more potent than cimetidine and 8 times more potent than ranitidine, with a single bedtime dose (40 mg) providing 10–12 hours of sustained acid suppression. Detailed mechanism-of-action data from DrugBank was not retrievable in this Evidence Pack; the above reflects the drug's well-documented pharmacological class.

Duodenogastric reflux (DGR) is characterised by retrograde flow of bile acids, lysolecithin, and pancreatic enzymes from the duodenum into the stomach. Although impaired pyloric function is the primary anatomical driver, the acid environment of the stomach significantly amplifies mucosal injury caused by the mixed refluxate. By raising intragastric pH, famotidine reduces the corrosive acid component of this combined chemical insult, offering mechanistic rationale for mucosal protection even when the bile component persists.

Two published clinical studies directly address this link: one examines famotidine's effects on both gastroesophageal and duodeno-gastro-esophageal reflux in critically ill patients, exploring possible underlying mechanisms; the other evaluates H2-receptor antagonist therapy (famotidine 20 mg twice daily) in early-stage gastroduodenal reflux disease classified by the modified Savary-Miller scale. Both align with famotidine's established antisecretory profile and its broader role in managing acid-mediated upper gastrointestinal conditions.

---

## Clinical Trial Evidence

Currently no clinical trials specifically addressing duodenogastric reflux for famotidine are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Clinical study | World Journal of Gastroenterology | Investigated famotidine's effect on gastroesophageal reflux (GER) and duodeno-gastro-esophageal reflux (DGER) in critically ill patients; evaluated possible mechanisms and relevant contributing factors |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Clinical study | Experimental & Clinical Gastroenterology | Assessed famotidine 20 mg BID in early-stage gastroduodenal reflux disease (Savary-Miller grade 0–1) using combined clinical and endoscopic endpoints |

---

## Singapore Market Information

Famotidine currently has no registered products in Singapore. No authorization numbers or approved indication texts are available from local regulatory records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a near-perfect prediction score for famotidine in duodenogastric reflux, and the acid-suppression mechanism provides a plausible biological basis. However, the Singapore-specific clinical evidence base is minimal (2 observational studies, 0 registered trials), no Singapore registration exists, and the safety profile — warnings, contraindications, and drug interaction data — could not be populated from this Evidence Pack.

**To proceed, the following is needed:**
- Identify a Singapore HSA registration pathway, or establish whether the drug is available under an unregistered route (e.g., named-patient supply)
- Retrieve the official package insert to populate key warnings, contraindications, and drug-drug interaction data (resolves DG001)
- Query DrugBank API for full MOA details (resolves DG002)
- Identify or commission clinical studies with duodenogastric reflux as a primary endpoint, distinguishing famotidine's effect from PPIs on the bile-acid component of reflux
- Benchmark against current Singapore standard-of-care for DGR (proton pump inhibitors, ursodeoxycholic acid, prokinetics) to define where famotidine adds clinical value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

