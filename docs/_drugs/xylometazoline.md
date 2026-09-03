---
layout: default
title: Xylometazoline
parent: 僅模型預測 (L5)
nav_order: 1070
evidence_level: L5
indication_count: 10
---

# Xylometazoline
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

# Xylometazoline: From Nasal Decongestant (OTC) Use to Nasal Cavity Disease

## One-Sentence Summary

Xylometazoline is a topical α-adrenergic agonist already established as an over-the-counter nasal decongestant for nasal congestion/patency; no formal regulatory original-indication text is available in this evidence pack. The TxGNN model's top prediction — **Nasal Cavity Disease** — essentially confirms this existing pharmacological use rather than identifying a genuinely novel indication, and is supported by **2 clinical trials** (including 1 completed Phase 3 RCT) and **7 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No regulatory indication text available (drug not registered/marketed in Singapore); known established OTC use is nasal decongestion |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Xylometazoline is a local α-adrenergic receptor agonist. Its primary pharmacological action is direct vasoconstriction of nasal mucosal blood vessels, which reduces turbinate swelling and nasal airway resistance. This mechanism is the drug's core, well-established pharmacology — it is not a new mechanistic hypothesis but the same action already exploited in its conventional decongestant use.

Because the predicted indication "Nasal Cavity Disease" sits directly on this established mechanism, the evidence pack itself notes that this prediction is "effectively equivalent to the drug's existing clinical use for nasal patency/decongestion" — the mechanistic link is direct and unambiguous rather than a repurposing leap into a new organ system or pathology.

Consistent with this, the strongest supporting clinical trial (NCT06443255, completed Phase 3) directly compares a lidocaine/xylometazoline combination against cocaine and saline for intranasal analgesia/preparation — a use case squarely within the drug's known decongestant/vasoconstrictor role, further reinforcing that this is a validation of known pharmacology rather than a speculative new application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Blinded triple crossover study comparing cocaine, lidocaine/xylometazoline, and saline for intranasal analgesia prior to awake fiberoptic nasotracheal intubation in patients with anticipated difficult airway |
| [NCT05072392](https://clinicaltrials.gov/study/NCT05072392) | N/A | Unknown | 80 | Evaluated Foley catheter-assisted nasal intubation vs. conventional technique on nasal bleeding; xylometazoline used as pre-procedure decongestant adjunct |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24023995](https://pubmed.ncbi.nlm.nih.gov/24023995/) | 2013 | RCT | Korean J Anesthesiol | Prophylactic intranasal xylometazoline spray compared to epinephrine gauze packing for nasal cavity expansion prior to nasotracheal intubation |
| [24158493](https://pubmed.ncbi.nlm.nih.gov/24158493/) | 2013 | RCT | JAMA Otolaryngol Head Neck Surg | Randomized, double-blind, placebo-controlled trial of intranasal decongestant/local anesthetic in children before flexible nasendoscopy |
| [1281924](https://pubmed.ncbi.nlm.nih.gov/1281924/) | 1992 | Experimental study | Rhinology | Topical xylometazoline reduced nasal airway resistance asymmetry in healthy subjects and those with acute rhinitis |
| [22427029](https://pubmed.ncbi.nlm.nih.gov/22427029/) | 2013 | Prospective study | Eur Arch Otorhinolaryngol | Compared cotton pledget packing vs. topical decongestant spray for nasal preparation before endoscopy |
| [8740084](https://pubmed.ncbi.nlm.nih.gov/8740084/) | 1996 | RCT (comparator drug) | Arzneimittel-Forschung | Double-blind rhinomanometric study of a decongestant combination vs. xylometazoline and placebo on nasal resistance |
| [34783482](https://pubmed.ncbi.nlm.nih.gov/34783482/) | 2021 | Review | Vestnik Otorinolaringologii | Review of nasal mucosa changes in elderly patients and management of inflammatory nasal/paranasal sinus disease, including decongestant nasal sprays |
| [20632242](https://pubmed.ncbi.nlm.nih.gov/20632242/) | 2010 | Animal study | Pneumologie | Xylometazoline reduced pathologically elevated intranasal airway resistance by ~50% in brachycephalic dogs |

---

## Singapore Market Information

No marketing authorization records were found in Singapore — this evidence pack indicates the drug is currently **not registered/marketed** (0 licenses on file).

---

## Safety Considerations

**Literature-derived safety signal (relevant to overuse/misuse, not to the nasal cavity disease indication specifically):**
- Case reports link xylometazoline (and other topical decongestants) overuse to **hypertensive crisis with end-organ damage** ([PMID 21712403](https://pubmed.ncbi.nlm.nih.gov/21712403/)) and to **recurrent thunderclap headache from reversible cerebral vasoconstriction syndrome (RCVS)**, associated with rhinitis medicamentosa ([PMID 33168762](https://pubmed.ncbi.nlm.nih.gov/33168762/)).
- These signals arose from a separate predicted indication (headache disorder) in this evidence pack and indicate the opposite direction — chronic/excessive decongestant use as a potential **cause** of vascular headache rather than a treatment — and should inform duration-of-use guardrails.

Beyond this, no structured key warnings, contraindications, or DDI data were available in this evidence pack; please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction is supported by L2-level evidence, including one completed Phase 3 RCT and multiple mechanistically consistent studies, but it largely confirms the drug's already-known decongestant pharmacology rather than establishing a genuinely novel indication. The drug is also not currently marketed in Singapore, and core safety documentation (warnings, contraindications, DDI) is missing.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently blocking — DG001)
- Confirmed original mechanism of action and formally approved original indication text (DG002)
- Assessment of overuse-related risk (hypertensive crisis, RCVS/thunderclap headache) to inform dosing/duration guardrails
- Regulatory pathway assessment for market entry in Singapore, given zero current registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

