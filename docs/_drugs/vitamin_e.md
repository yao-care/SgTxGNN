---
layout: default
title: Vitamin E
parent: 僅模型預測 (L5)
nav_order: 1064
evidence_level: L5
indication_count: 10
---

# Vitamin E
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

# Vitamin E: From Vitamin E Deficiency to Inborn Disorder of Bilirubin Metabolism

## One-Sentence Summary

Vitamin E (DrugBank DB00163) is a fat-soluble antioxidant vitamin conventionally used for prevention and correction of vitamin E deficiency. The TxGNN model predicts it may be relevant to **Inborn Disorder of Bilirubin Metabolism**, but the supporting evidence is currently indirect — **3 clinical trials** (all low-relevance) and **2 older literature reports** were identified, none of which directly test vitamin E as a treatment for this disorder.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin E deficiency (nutritional/antioxidant supplement) — no local approved-label text available |
| Predicted New Indication | Inborn Disorder of Bilirubin Metabolism |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, Vitamin E is a fat-soluble antioxidant (tocopherol/tocotrienol class) that scavenges free radicals and protects cell membranes from lipid peroxidation; its role in treating overt vitamin E deficiency is well established.

Inborn disorders of bilirubin metabolism — such as Crigler-Najjar syndrome or progressive familial intrahepatic cholestasis (PFIC) — frequently involve chronic cholestasis, which impairs fat and fat-soluble vitamin absorption and commonly produces **secondary vitamin E deficiency**. Supplementation in these patients corrects the deficiency state and is standard supportive care, which is likely the biological signal driving this prediction.

However, correcting a secondary deficiency is mechanistically distinct from treating the underlying disorder of bilirubin metabolism itself. There is no evidence in the current pack that vitamin E modifies bilirubin conjugation, transport, or clearance pathways. The very high TxGNN score most plausibly reflects a "hepatobiliary disease" node co-occurrence effect in the knowledge graph rather than a direct causal treatment relationship — consistent with the L4/Hold assessment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06465810](https://clinicaltrials.gov/study/NCT06465810) | N/A | Recruiting | 1,850 | Multi-country observational registry (MaesTTRo) on ATTR amyloidosis natural history/treatment patterns; non-interventional, does not test vitamin E (Grade C relevance) |
| [NCT03115086](https://clinicaltrials.gov/study/NCT03115086) | N/A | Active, not recruiting | 55 | Post-marketing registry for Cholbam (cholic acid) in bile acid synthesis disorders; observational, not a vitamin E trial (Grade C relevance) |
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | Completed | 6 | Dose-escalation study of lomitapide (MTP inhibitor) in homozygous familial hypercholesterolemia; unrelated drug and indication (Grade C relevance) |

**Note:** None of the identified trials directly evaluate vitamin E for inborn disorders of bilirubin metabolism.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7915305](https://pubmed.ncbi.nlm.nih.gov/7915305/) | 1994 | Case report/Review | The Journal of Pediatrics | Describes 3β-hydroxy-C27-steroid dehydrogenase/isomerase deficiency as a cause of progressive intrahepatic cholestasis; does not address vitamin E treatment |
| [803225](https://pubmed.ncbi.nlm.nih.gov/803225/) | 1975 | Review | The New England Journal of Medicine | General review of neonatal nonhemolytic jaundice; no vitamin E intervention data |

**Note:** Both references are background disease-mechanism literature, not vitamin E efficacy studies.

---

## Singapore Market Information

Vitamin E has **0 registered licenses** and is currently **not marketed** in Singapore under this dataset. No product-level authorization records are available for tabulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA package insert warnings and contraindications are flagged as a Blocking data gap (DG001) requiring retrieval before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this indication is limited to mechanistic plausibility (correction of secondary vitamin E deficiency in cholestatic disease) plus a single TxGNN prediction; no clinical trial or literature evidence directly tests vitamin E as a treatment for the underlying bilirubin metabolism disorder, and the identified trials/literature are of low direct relevance (Grade C / Tier 3).

**To proceed, the following is needed:**
- TFDA/HSA package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Detailed mechanism of action data from DrugBank (DG002)
- Direct clinical evidence evaluating vitamin E specifically in inborn bilirubin metabolism disorders (e.g., Crigler-Najjar, PFIC), beyond correction of secondary deficiency
- Route compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

