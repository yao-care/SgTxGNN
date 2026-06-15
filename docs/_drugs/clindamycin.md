---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Clindamycin
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

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic widely used to treat susceptible bacterial infections, including skin and soft tissue infections, anaerobic infections, bone and joint infections, and as a treatment component for toxoplasmosis.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis** with a very high prediction score of 99.97%; however, **no clinical trials** and **no directly relevant publications** currently support this direction, and the mechanistic rationale is weak.
Overall, this candidate package presents an L5-level evidence profile across all top predictions, warranting a firm Hold decision at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (skin/soft tissue, anaerobic, bone/joint, toxoplasmosis) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacology, Clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit. It is active against many gram-positive aerobic cocci (including *Staphylococcus aureus*), and a broad range of anaerobic organisms. It also has antiparasitic activity relevant to *Toxoplasma gondii* and *Plasmodium* species.

Punctate epithelial keratoconjunctivitis (PEK) is a multifactorial condition of the corneal and conjunctival surface epithelium. Its primary causes include dry eye syndrome, viral infection (notably adenovirus), drug toxicity, and chemical exposure — not bacterial infection. The mechanistic link between Clindamycin's antibacterial/antiparasitic action and the dominant pathophysiology of PEK is therefore weak. A secondary bacterial superinfection scenario could theoretically be considered, but no data supports this as a clinically meaningful treatment opportunity.

The notably high TxGNN score (0.9997, ranked #780 globally) is most likely an artefact of dense knowledge graph connectivity among corneal disease nodes, rather than true mechanistic signal. This interpretation is consistent with the complete absence of supporting clinical or preclinical evidence, and is explicitly flagged in the model's own repurposing rationale for this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature directly relevant to Clindamycin and punctate epithelial keratoconjunctivitis is available.

---

## Singapore Market Information

Clindamycin is currently **not registered** in Singapore. No product authorizations are on record, and no approved indication text is available from regulatory sources.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Package insert data (key warnings, contraindications) was identified as a blocking data gap (DG001) in this evidence pack. Retrieval from the HSA/TFDA official website via PDF parsing is required before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top 10 TxGNN predictions for Clindamycin carry L5 evidence (model prediction only), with no clinical trials and only indirect or veterinary literature retrieved. The highest-ranked prediction (punctate epithelial keratoconjunctivitis) lacks both mechanistic plausibility and any empirical support, and the drug is not registered in Singapore, making a regulatory pathway undefined at this time.

**To proceed, the following is needed:**

- **MOA data (DG002 — High):** Retrieve full DrugBank API record for DB01190 to confirm mechanism, categories, and known ophthalmic uses
- **Regulatory safety data (DG001 — Blocking):** Download and parse the HSA or TFDA package insert PDF for Clindamycin to establish key warnings and contraindications before any S1 safety screening
- **Singapore registration pathway:** Assess whether Clindamycin (oral, topical, or ophthalmic formulation) could be submitted for HSA registration, and identify any existing international approvals for ocular indications
- **Mechanistic feasibility review:** Before investing further resources, consider whether any of the 10 predicted indications has a plausible biological rationale — the current analysis suggests the exposure keratitis secondary infection scenario (Rank 2, L4) is the most defensible near-term candidate for further literature review, given known Clindamycin activity against *S. aureus* and *Bacillus cereus*
- **Ophthalmic formulation feasibility:** Determine whether a suitable topical ophthalmic formulation of Clindamycin exists or could be developed, as route compatibility is currently unresolved for all predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

