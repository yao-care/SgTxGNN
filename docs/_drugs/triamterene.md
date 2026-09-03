---
layout: default
title: Triamterene
parent: 僅模型預測 (L5)
nav_order: 1011
evidence_level: L5
indication_count: 10
---

# Triamterene
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

# Triamterene: From Potassium-Sparing Diuretic Therapy to Potassium Deficiency Disease

## One-Sentence Summary

Triamterene is an ENaC-blocking, potassium-sparing diuretic classically used in combination with thiazide/loop diuretics to treat hypertension and oedema while preventing diuretic-induced hypokalemia. Among TxGNN's ten candidate predictions for this drug, only **Potassium Deficiency Disease** is backed by real drug-specific literature (10 publications, including case reports of Liddle's and Gitelman's syndrome successfully treated with triamterene), placing it at **Evidence Level L2** with a **Proceed with Guardrails** recommendation. The other, higher-scoring TxGNN predictions (e.g., malignant hypertensive renal disease, Braddock syndrome) have no supporting trials or literature and were explicitly flagged as clinically inappropriate or noise associations — a caveat detailed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in the Singapore regulatory database (drug not currently marketed); clinically established as a potassium-sparing diuretic used adjunctively with thiazide/loop diuretics for hypertension and oedema |
| Predicted New Indication | Potassium Deficiency Disease |
| TxGNN Prediction Score | 97.86% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available for this drug (data gap). However, the evidence pack's own mechanistic annotations confirm triamterene is an **epithelial sodium channel (ENaC) blocker** acting on the distal tubule/collecting duct, which reduces Na⁺–K⁺ exchange and thereby spares potassium — this is its core, well-established pharmacology.

This mechanism directly explains the link to the predicted indication: triamterene's established clinical role has never been as a standalone antihypertensive, but as an *adjunct* to kaliuretic diuretics (HCTZ, furosemide, etc.) specifically to **prevent or treat drug-induced hypokalemia**. The literature captured here supports this precise use-case, including case reports where triamterene successfully corrected hypokalemia in Liddle's syndrome and was reviewed as a first-line potassium-sparing agent alongside spironolactone and amiloride. In effect, TxGNN's prediction formalizes an already-recognized off-label/adjunct role into a distinct indication (potassium deficiency disease) rather than proposing a novel biological hypothesis.

**Important caveat on ranking:** TxGNN's five highest-scoring predictions for triamterene (malignant hypertensive renal disease, malignant renovascular hypertension, two pulmonary hypertension subtypes, and Braddock syndrome) all have **zero supporting trials or literature**, and the model's own rationale text explicitly argues that several represent *relative contraindications* (high hyperkalemia risk in renal impairment) or knowledge-graph co-occurrence noise rather than genuine repurposing signals. All were scored L5/Hold. Potassium Deficiency Disease, despite ranking 7th by raw TxGNN score, is the only candidate with a coherent, drug-specific evidence trail and is therefore the focus of this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8927344](https://pubmed.ncbi.nlm.nih.gov/8927344/) | 1996 | Drug-specific Review | Orvosi Hetilap | Reviews potassium-sparing diuretics (spironolactone, triamterene, amiloride); notes ability to prevent potassium loss and potentiate distal-tubule diuretics |
| [9630200](https://pubmed.ncbi.nlm.nih.gov/9630200/) | 1998 | Case Report | Internal Medicine (Tokyo) | 78-year-old woman with Liddle's syndrome (hypokalemia, low renin/aldosterone) successfully treated with triamterene |
| [6273144](https://pubmed.ncbi.nlm.nih.gov/6273144/) | 1981 | Case Report | Endocrinologia Japonica | Liddle's syndrome patient: plasma potassium and blood pressure normalized after triamterene administration |
| [16078592](https://pubmed.ncbi.nlm.nih.gov/16078592/) | 2005 | Case Report | J Sichuan University (Med) | Gitelman's syndrome presenting with severe hypokalemic periodic paralysis; managed with potassium-sparing therapy |
| [3543514](https://pubmed.ncbi.nlm.nih.gov/3543514/) | 1986 | Review | Magnesium | Reviews magnesium/potassium-sparing diuretic interactions and urinary potassium loss with diuretic therapy |
| [10528423](https://pubmed.ncbi.nlm.nih.gov/10528423/) | 1999 | Review | Annali Italiani di Medicina Interna | Magnesium deficiency and cardiovascular drug interactions; discusses diuretic-induced electrolyte loss |
| [5135405](https://pubmed.ncbi.nlm.nih.gov/5135405/) | 1971 | Experimental Study | Revue Canadienne de Biologie | Rat model: effect of antikaliuretic agents on cardiac lesions caused by potassium/magnesium deficiency |
| [9255135](https://pubmed.ncbi.nlm.nih.gov/9255135/) | 1997 | Review | Emerg Med Clin North Am | General review of weakness/neuromuscular disease workup, including electrolyte-related causes |
| [6032221](https://pubmed.ncbi.nlm.nih.gov/6032221/) | 1967 | Review | The Medical Letter | Brief drug review of furosemide (Lasix); limited direct relevance |
| [4861685](https://pubmed.ncbi.nlm.nih.gov/4861685/) | 1966 | Review | Der Internist | Pathogenesis and therapy of ascites in liver cirrhosis; general diuretic context |

---

## Singapore Market Information

Triamterene has no current market authorizations on record in Singapore (0 registrations; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were available in this evidence pack (flagged as a **Blocking** data gap for TFDA/HSA label warnings — see DG001). Given triamterene's known hyperkalemia risk, this gap must be closed before any clinical use is considered, particularly in patients with renal impairment or those on concomitant ACE inhibitors/ARBs/potassium supplements.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Potassium Deficiency Disease is mechanistically coherent with triamterene's established pharmacology and is supported by drug-specific case reports and reviews (L2), unlike the model's top-ranked but evidence-free predictions. However, all supporting literature is older (1966–2005), consists mainly of case reports rather than controlled trials, and the drug is not currently marketed or registered in Singapore.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/HSA label warnings and contraindications) before any safety evaluation
- Resolve DG002 (formal DrugBank MOA confirmation) to strengthen the mechanistic rationale
- Seek contemporary controlled evidence (beyond case reports) for potassium-sparing use as a primary indication rather than adjunct therapy
- Confirm hyperkalemia risk stratification and monitoring plan (renal function, serum potassium) given the drug's known contraindication in renal impairment
- Evaluate Singapore registration pathway, since the drug currently has zero local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

