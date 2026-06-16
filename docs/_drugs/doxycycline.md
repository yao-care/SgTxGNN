---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
---

# Doxycycline
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

# Doxycycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a broad-spectrum tetracycline antibiotic used as first-line therapy for intracellular bacterial infections including *Chlamydia trachomatis*, tick-borne diseases (Lyme disease, Rocky Mountain spotted fever), and a range of gram-positive and gram-negative pathogens.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**, with **0 clinical trials** and **1 case series publication** currently available to support this direction.
The mechanistic link is indirect: Doxycycline eradicates the underlying chlamydial infection that triggers PEK as a post-infectious sequela, rather than treating PEK directly.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (broad-spectrum antibiotic; not registered in Singapore — no approved indication on record) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, Doxycycline is a tetracycline-class antibiotic that inhibits bacterial protein synthesis by binding to the 30S ribosomal subunit, thereby blocking aminoacyl-tRNA from attaching at the ribosomal acceptor site. Beyond its antimicrobial activity, Doxycycline also possesses anti-inflammatory properties through inhibition of matrix metalloproteinases (MMP-8 and MMP-9) and suppression of pro-inflammatory cytokines.

The TxGNN prediction for Punctate Epithelial Keratoconjunctivitis (PEK) is mechanistically grounded in Doxycycline's established role as the first-line oral treatment for *Chlamydia trachomatis* infection. Follicular conjunctivitis caused by *C. trachomatis* is a recognised antecedent of PEK: after resolution of the primary follicular infection, persistent superficial punctate corneal lesions can remain, representing a post-infectious sequela rather than an active bacterial disease. The logic of repurposing here is therefore indirect — Doxycycline clears the chlamydial trigger, which in turn allows PEK to resolve.

However, the available evidence does not demonstrate that Doxycycline acts on PEK as a primary therapeutic target. The sole publication (PMID 1424659, 1992) describes two cases of *C. trachomatis*-associated PEK where treatment was directed at the underlying chlamydial infection; the PEK itself was a residual finding after antibiotic resolution of the follicles. This is best classified as infection-sequela management rather than direct drug repurposing for PEK, which limits the strength of this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication (punctate epithelial keratoconjunctivitis + Doxycycline).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Series | Cornea | Two cases of *C. trachomatis* follicular conjunctivitis treated with oral tetracycline or doxycycline; after follicle resolution, both patients developed recurrent bilateral punctate epithelial keratitis with anterior stromal involvement, suggesting PEK as a post-infectious sequela rather than a primary doxycycline-responsive condition |

---

## Singapore Market Information

Doxycycline (DB00254) has **no registered products** in Singapore at the time of this evaluation. No licence records, dosage forms, or approved indications are available from the local regulatory database.

> Note: This finding may reflect a data gap in the regulatory dataset rather than true absence from the market. Independent verification against the current Health Sciences Authority (HSA) product listing is strongly recommended before drawing conclusions about market availability.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug–drug interaction data were retrieved for this evaluation.

> For general reference: Doxycycline is contraindicated in pregnant women (risk of foetal bone and tooth development impairment), in children under 8 years of age (permanent tooth discolouration), and in patients with known hypersensitivity to tetracyclines. Clinicians should verify these points against the current prescribing information and local regulatory guidance before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a near-perfect prediction score (99.94%), but the underlying evidence for Doxycycline in Punctate Epithelial Keratoconjunctivitis is limited to a single 1992 case series (n=2) in which PEK was treated indirectly via eradication of the triggering chlamydial infection — not as a direct target indication. No clinical trials have been registered for this specific combination. Until the mechanistic link is clarified and at least preliminary prospective data are available, proceeding to a clinical decision stage is premature.

**To proceed, the following is needed:**

- **Confirm disease definition**: Clarify whether the TxGNN model's "punctate epithelial keratoconjunctivitis" refers to chlamydial-associated PEK (infection-driven) or other aetiologies (e.g., dry eye, viral, toxic). The repurposing rationale differs substantially depending on aetiology.
- **MOA data**: Retrieve Doxycycline's full mechanism of action from DrugBank (DG002 remediation) to assess whether anti-inflammatory or MMP-inhibiting properties could have any direct role in corneal epithelial repair.
- **Singapore regulatory verification**: Confirm actual HSA registration status independently; zero-licence records may reflect a data extraction gap.
- **TFDA package insert warnings and contraindications**: Retrieve and parse the official prescribing information (DG001 remediation) to complete the S1 safety screening.
- **Prospective evidence**: Before progressing to S2, at minimum a small prospective case series or registry study in chlamydial PEK patients receiving doxycycline with quantified PEK outcomes is required to advance this from L4 to L3 evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

