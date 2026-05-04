---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: From Herpes Virus Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Acyclovir is a well-established nucleoside analogue antiviral, primarily used for the treatment and suppression of infections caused by herpes simplex virus (HSV) and varicella-zoster virus (VZV).
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**, with **0 clinical trials** and **2 publications** currently available — both of which are indirect references that do not directly evaluate Acyclovir for this indication.
The mechanistic link is plausible when PEK is of herpetic origin, but direct clinical efficacy evidence is absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Herpes simplex and varicella-zoster virus infections |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current regulatory dataset. Based on established pharmacological knowledge, Acyclovir is a synthetic acyclic nucleoside analogue that requires activation by a virus-encoded thymidine kinase (TK) — present in HSV-1, HSV-2, and VZV, but absent in most other pathogens. Once phosphorylated to its active triphosphate form by a cascade of viral and cellular kinases, it competitively inhibits viral DNA polymerase and terminates chain elongation, halting viral replication with high selectivity.

Punctate epithelial keratoconjunctivitis refers to superficial lesions of the corneal and conjunctival epithelium that can result from multiple etiologies. HSV-1 is among the most common viral causes of ocular surface disease and can directly produce PEK as part of its clinical presentation. This provides a biologically coherent rationale for the TxGNN prediction: if the PEK is herpetic in origin, Acyclovir's established anti-HSV activity could plausibly suppress the causative virus and allow epithelial healing.

However, the two publications identified do not support this hypothesis directly. PMID 7825685 describes drug-induced corneal lipidosis in AIDS patients receiving treatment for opportunistic infections — it does not study Acyclovir for PEK. PMID 21934222 reports microsporidial keratoconjunctivitis, caused by an intracellular parasite that lacks thymidine kinase and is entirely unresponsive to Acyclovir. Both citations are coincidental co-occurrences in the literature rather than mechanistic or efficacy evidence. The prediction's high score most likely reflects strong graph-level connectivity between HSV/VZV and ocular surface pathology in the TxGNN knowledge graph, rather than a direct drug–disease relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Acyclovir in punctate epithelial keratoconjunctivitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case Series | American Journal of Ophthalmology | Two AIDS patients developed bilateral drug-induced corneal lipidosis during treatment for opportunistic infections; describes ocular surface toxicity, not Acyclovir efficacy in PEK |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case Series | Indian Journal of Pathology & Microbiology | Microsporidial keratoconjunctivitis in an eastern Indian cohort; caused by an intracellular parasite outside the spectrum of Acyclovir activity — not directly relevant |

---

## Singapore Market Information

Acyclovir currently holds **no registered products with HSA Singapore** (total authorizations: 0). No market authorization data is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.67%), the available evidence does not support pursuing this specific indication at this stage. The two identified publications are indirect references that provide no meaningful efficacy signal, and no clinical trials have evaluated Acyclovir for punctate epithelial keratoconjunctivitis. The therapeutic benefit of Acyclovir is strictly limited to HSV/VZV-mediated PEK, yet no data confirm the etiological fraction of PEK attributable to these pathogens in the target population.

**To proceed, the following is needed:**

- **Clarify PEK etiology profile**: Determine what proportion of PEK cases in the intended patient population is attributable to HSV-1 vs. adenovirus vs. other non-viral causes; Acyclovir can only benefit the herpetic subset
- **Retrieve DrugBank MOA data (DG002)**: Query DrugBank API to formally document mechanism of action for the evidence dossier
- **Obtain Singapore/Taiwan package insert (DG001)**: Download and parse full prescribing information (warnings, contraindications, interactions) before any safety evaluation can proceed — this is currently a Blocking gap
- **Targeted literature search**: Re-query PubMed with `"acyclovir" AND ("herpetic keratoconjunctivitis" OR "HSV epithelial keratitis" OR "herpes simplex keratitis")` to identify whether PEK has been assessed as a sub-endpoint in ocular herpes trials such as the Herpetic Eye Disease Study (HEDS, NCT00000138)
- **Consider indication reclassification**: If evidence from herpetic eye disease trials supports PEK as a measurable outcome, this indication may be more productively evaluated under **"Disease of Orbital Region"** (Rank 9 in this Evidence Pack), which already carries L2 evidence, Phase 4 trial data, and a "Proceed with Guardrails" recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

