---
layout: default
title: Alectinib
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# Alectinib: From ALK-Positive NSCLC to Fibromatosis, Gingival

## One-Sentence Summary

Alectinib is a second-generation, highly selective ALK (anaplastic lymphoma kinase) tyrosine kinase inhibitor, approved in multiple global jurisdictions for the treatment of ALK-positive non-small cell lung cancer (NSCLC), though it currently holds no market authorization in Singapore.
The TxGNN model ranks **Fibromatosis, Gingival** as its top new indication prediction, with a score of 99.97%.
However, **zero clinical trials and zero supporting publications** exist for this specific pairing, placing this prediction at the lowest possible evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Alectinib is a potent, orally bioavailable second-generation ALK inhibitor. It competitively occupies the ATP-binding pocket of the ALK kinase domain, blocking constitutively active ALK fusion oncoproteins (most commonly EML4-ALK) from driving downstream proliferation signalling via the RAS/MAPK, PI3K/AKT, and JAK/STAT pathways. Unlike its predecessor crizotinib, alectinib achieves robust CNS penetration and retains activity against most crizotinib-resistance mutations (e.g., L1196M, F1174L). Note: formal DrugBank MOA data was not retrieved in this evidence pack; the above reflects established published pharmacology.

Gingival fibromatosis is a rare benign fibrous overgrowth of the gingival tissue. It is driven predominantly by mutations in the **SOS1** or **HMGA2** genes (hereditary form) or triggered as a drug-induced reaction (e.g., phenytoin, calcium channel blockers, cyclosporine). There is currently no published evidence that ALK overexpression, amplification, or fusion genes play any role in its pathogenesis. The condition is not a proliferative malignancy in the oncological sense and does not involve tyrosine kinase-dependent signalling.

The TxGNN model's high prediction score for this indication most likely reflects **knowledge graph topology artefacts**: "fibroproliferative lesion" node clusters in the underlying knowledge graph may share graph-structural proximity to Alectinib's known disease nodes, generating an indirect, mechanistically unsupported association. Without any biological plausibility for ALK pathway involvement in gingival fibromatosis, this prediction should not be taken as evidence of a genuine repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Alectinib in fibromatosis, gingival.

---

## Literature Evidence

Currently no related literature available for Alectinib in fibromatosis, gingival.

---

## Singapore Market Information

Alectinib currently holds **no drug registrations** with the Health Sciences Authority (HSA) of Singapore. It is not marketed in Singapore as of the data cutoff date (2026-04-04).

Alectinib is approved in the United States (FDA, 2015/2017), European Union (EMA), Japan (PMDA), and Taiwan (TFDA) for ALK-positive NSCLC, but none of these authorisations extend to Singapore market registration. Any clinical use in Singapore would require special access pathways (e.g., HSA's Special Access Route).

---

## Cytotoxicity

Alectinib is an antineoplastic targeted therapy indicated for a malignant indication (ALK-positive NSCLC); the following cytotoxicity profile applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK tyrosine kinase inhibitor (non-conventional cytotoxic) |
| Myelosuppression Risk | Low (not a conventional cytotoxic agent; clinically significant myelosuppression is uncommon; anaemia reported in ~20% of patients but severe cases are rare) |
| Emetogenicity Classification | Minimal to low (oral TKI; nausea reported in ~14% but severe vomiting is uncommon) |
| Monitoring Items | Liver function (ALT, AST, total bilirubin) every 2 weeks for the first 3 months then monthly; CBC; renal function; serum creatine phosphokinase (CPK) for myalgia; body weight (unexplained weight gain reported in ~10%); heart rate (bradycardia risk) |
| Handling Protection | Standard cytotoxic handling precautions apply; oral capsule formulation reduces aerosolisation risk compared to intravenous agents |

---

## Safety Considerations

Formal TFDA/HSA package insert warnings and contraindications were not available in this evidence pack (Data Gap — Blocking severity). Please refer to the approved product package insert for complete safety information.

The following is noted from general published data:
- **Hepatotoxicity**: Grade 3–4 ALT/AST elevation occurs in approximately 3–5% of patients; liver function monitoring is essential.
- **Interstitial lung disease / pneumonitis**: Rare but potentially severe; requires prompt discontinuation.
- **Bradycardia**: Dose-dependent heart rate reduction; monitor in patients on concomitant antihypertensives or antiarrhythmics.
- **Photosensitivity**: Patients should avoid prolonged sun exposure and use sun protection.
- **CPK elevation and myalgia**: Reported in up to 30% of patients; monitor serum CPK.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no established biological link between ALK signalling and gingival fibromatosis, and zero clinical or preclinical data support this repurposing direction. The TxGNN high score reflects knowledge graph structural proximity rather than mechanistic plausibility, and pursuing this indication without any supporting evidence would not be a productive use of resources.

**To proceed, the following is needed:**
- Tissue profiling studies to determine whether ALK is expressed or rearranged in gingival fibromatosis specimens
- Preclinical (in vitro cell line or animal model) data demonstrating that ALK inhibition has any biological effect on gingival fibroblast proliferation
- Retrieval of the full DrugBank MOA entry and TFDA/HSA package insert to complete the safety assessment (currently Blocking data gaps)
- If ALK expression is confirmed in future tissue studies, escalate to L4 evidence stage and consider proof-of-concept preclinical work before any clinical translation

> **Note for reviewers:** Among the 10 TxGNN-predicted indications in this Evidence Pack, **Rank 6 (Lung Germ Cell Tumor / ALK-positive Neuroendocrine Tumours)** carries the strongest actual evidence (Evidence Level L3; 2 clinical trials, 16 publications including multiple case reports of objective response in ALK+ large-cell neuroendocrine carcinoma). If the goal is to identify the most actionable repurposing signal for Alectinib, that indication warrants a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

