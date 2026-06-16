---
layout: default
title: Dobutamine
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Acute Heart Failure to Alopecia

## One-Sentence Summary

Dobutamine is a synthetic catecholamine and β1 adrenergic receptor agonist, widely used as an intravenous inotropic agent for the acute management of decompensated heart failure and cardiogenic shock.
The TxGNN model predicts it may be effective for **Alopecia (hair loss)**, with **0 clinical trials** and **2 publications** retrieved — neither of which directly supports this indication.
The overall evidence base is at the lowest tier (L5), and the mechanistic rationale is absent; this prediction most likely reflects a knowledge graph artefact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute decompensated heart failure / cardiogenic shock (inotropic support) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on established pharmacological knowledge, Dobutamine is a synthetic catecholamine that acts primarily at β1 adrenergic receptors in the myocardium, increasing heart rate and contractile force to raise cardiac output. It is administered exclusively by continuous intravenous infusion in acute care settings. Its well-characterised cardiovascular mechanism has no known connection to hair follicle biology or the dermatological pathways involved in alopecia.

Alopecia encompasses a spectrum of conditions treated with topical or systemic agents targeting androgen signalling (e.g. finasteride, minoxidil) or autoimmune hair follicle destruction (e.g. JAK inhibitors such as baricitinib). The knowledge graph may have generated this prediction by linking dobutamine to minoxidil through shared "vasodilation" edges in the graph; however, minoxidil promotes hair growth via potassium channel opening (K⁺ channel opener), which is mechanistically entirely distinct from β1 adrenergic stimulation.

In short, there is no biologically plausible rationale supporting dobutamine as a treatment for alopecia. The two retrieved publications confirm this assessment: one describes dobutamine used for haemodynamic rescue in a cat suffering minoxidil-induced cardiotoxicity, and the other reports transient hair loss as a recovery-phase finding in a child with colchicine poisoning — neither publication addresses dobutamine as a hair-growth therapy in any way.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dobutamine and Alopecia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case Report (Animal) | Journal of Veterinary Cardiology | Dobutamine administered for haemodynamic rescue in a cat with minoxidil-induced congestive heart failure — not evidence for alopecia treatment; dobutamine is the rescue drug, minoxidil the cause |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | Case Report | Pediatric Emergency Care | Colchicine poisoning recovery phase associated with hair loss — dobutamine not mentioned in a therapeutic context; the hair loss is a toxicological sequela, not a treatment target |

> ⚠️ **Important:** Neither publication supports Dobutamine as a treatment for alopecia. Both were retrieved by keyword co-occurrence and are non-contributory to the repurposing hypothesis.

---

## Singapore Market Information

Dobutamine is currently **not registered** with the Health Sciences Authority (HSA) in Singapore. No active product licences were identified.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Full Prediction Summary (All 10 Indications)

All 10 TxGNN-predicted indications share the same **L5 evidence level** and **Hold** recommendation. The predictions cluster into two groups that expose a systematic pattern in the knowledge graph output:

| Rank | Predicted Indication | TxGNN Score | Clinical Trials | Literature | Key Mechanistic Concern |
|------|---------------------|-------------|-----------------|------------|-------------------------|
| 1 | Alopecia | 99.85% | 0 | 2 (non-contributory) | KG artefact — likely confusion with minoxidil via vasodilation node; no β1 link to hair biology |
| 2 | Hypotrichosis simplex of the scalp | 99.84% | 0 | 0 | Genetic disease (CDSN, LPAR6 mutations); no adrenergic mechanism |
| 3 | Congenital hypotrichosis milia | 99.83% | 0 | 0 | Genetic skin disorder; no β1 signalling connection |
| 4 | Diffuse alopecia areata | 99.82% | 0 | 0 | Autoimmune (JAK-STAT pathway); standard of care is JAK inhibitors |
| 5 | Open-angle glaucoma | 99.47% | 0 | 0 | **Reversed mechanism**: β-blockers lower IOP; β-agonist dobutamine would increase aqueous humour production and worsen glaucoma |
| 6 | Raynaud disease | 99.47% | 0 | 1 (irrelevant) | Weak β2 vasodilation hypothesis; IV-only route entirely unsuitable for chronic management of a peripheral vasospastic disorder |
| 7 | Primary hereditary glaucoma | 99.46% | 0 | 0 | Genetic (MYOC, OPTN mutations); same reversed mechanism risk as rank 5 |
| 8 | Headache disorder | 99.31% | 1* | 4 (non-contributory) | **Dobutamine causes headache as a known side effect** (PMID 9137218, n=3,011); drug is an aetiological agent, not a treatment |
| 9 | Hypertrichosis | 99.29% | 0 | 0 | Same hair-disorder KG artefact cluster; hypertrichosis is not a therapeutic target |
| 10 | Migraine disorder | 99.24% | 0 | 1 (in vitro animal) | **Reversed mechanism**: β-blockers (propranolol, metoprolol) prevent migraine; β-agonist use is pharmacologically contraindicated |

*NCT02607488 investigates lidocaine for post-bariatric bowel recovery — completely unrelated to dobutamine or headache; trial is also suspended.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Dobutamine carry zero clinical evidence (L5) and most are supported by mechanistic rationales that are either absent or pharmacologically reversed — meaning dobutamine would be expected to worsen, not treat, conditions such as glaucoma, migraine, and headache disorders. The prominent hair-disorder cluster (ranks 1–4, 9) almost certainly arises from a knowledge graph artefact in which dobutamine is connected to minoxidil via shared vasodilation edges, despite the two drugs having fundamentally different mechanisms of action.

**To proceed, the following is needed:**
- Retrieve Dobutamine's full mechanism of action data from DrugBank (DrugBank ID: DB00841) and TFDA package insert to formally document MOA and confirm the absence of secondary targets relevant to the predicted indications
- Conduct a knowledge graph audit to determine whether the dobutamine–minoxidil confounding edge is a systemic issue affecting other vasodilatory drugs in the pipeline
- No clinical development pathway is recommended for any of the 10 predicted indications based on current evidence; this candidate should be deprioritised in favour of drugs with mechanistically coherent predictions
- If Singapore registration is considered in the future for Dobutamine's established cardiac indication, an HSA licence application would be required from scratch given the current absence of registered products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

