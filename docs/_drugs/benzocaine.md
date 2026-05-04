---
layout: default
title: Benzocaine
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
---

# Benzocaine
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

# Benzocaine: From Topical Analgesia to Papillary Conjunctivitis

## One-Sentence Summary

Benzocaine is an ester-type topical local anesthetic widely available globally as an OTC product for mucosal pain relief, including sore throat lozenges (e.g., Cepacol, Chloraseptic), minor dental procedures, and skin preparations.
The TxGNN model predicts it may be effective for **Papillary Conjunctivitis**, with **0 clinical trials** and **0 publications** currently providing direct evidence for this direction — making this the lowest evidence tier (L5).
Notably, among all 10 predicted indications, **Acute Laryngopharyngitis** (rank 10) carries substantially stronger real-world evidence and a more mechanistically coherent rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical anesthesia — mucosal and skin pain relief (OTC; not registered in Singapore) |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on widely known pharmacology, Benzocaine is an ester-type local anesthetic that reversibly blocks voltage-gated sodium channels (Nav), inhibiting sensory nerve conduction and providing temporary analgesia at the application site. Its short duration of action and low systemic absorption make it suitable for topical mucosal use.

Papillary conjunctivitis is an inflammatory eye condition characterised by enlarged conjunctival papillae, typically driven by mast-cell and eosinophil-mediated hypersensitivity responses to allergens or mechanical stimuli (e.g., contact lens wear). The core pathology is immunological, not nociceptive. While Nav blockade could theoretically blunt superficial ocular discomfort transiently, it cannot reduce the allergic cascade, reverse papillae formation, or address the underlying cause.

Furthermore, the standard ophthalmic local anesthetics — proparacaine and tetracaine — have well-characterised corneal penetration profiles and established safety data. Benzocaine's corneal penetration is poor and its ophthalmic safety record is essentially absent. The TxGNN model's high prediction score for this indication likely reflects a broader clustering of mucosal/surface anesthetic applications across the knowledge graph, rather than any indication-specific mechanistic signal. Caution is warranted before interpreting this score as clinically actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Benzocaine in Papillary Conjunctivitis.

---

## Literature Evidence

Currently no related literature available for Benzocaine in Papillary Conjunctivitis.

---

## Singapore Market Information

Benzocaine is currently not registered in Singapore. No marketing authorisations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings and contraindications data are unavailable in this evidence pack (Data Gap: TFDA package insert not retrieved). Known safety signals for Benzocaine include the risk of **methemoglobinaemia** (particularly in infants and those with G6PD deficiency), **contact hypersensitivity** (Benzocaine is itself a common contact allergen in the ester-anesthetic class), and potential for mucosal toxicity with prolonged use. These gaps should be resolved before any clinical development or regulatory submission.

---

## Conclusion and Next Steps

**Decision: Hold** *(for Papillary Conjunctivitis)*

**Rationale:**
There is zero direct clinical or preclinical evidence for Benzocaine in papillary conjunctivitis, the mechanistic rationale is weak (Nav blockade does not address immune-mediated inflammation), and preferred ophthalmic anesthetics with established safety profiles already exist. Benzocaine is also not marketed in Singapore, adding a regulatory barrier.

**Broader repurposing perspective — a more actionable signal exists:**
Within the same TxGNN prediction set, **Acute Laryngopharyngitis (rank 10, score 96.63%, Evidence Level L3)** represents a substantially stronger repurposing candidate:
- Benzocaine is already marketed OTC in the US, UK, and Australia specifically for sore throat pain (Cepacol Ultra Sore Throat, Chloraseptic Lozenges), constituting large-scale real-world evidence.
- The mechanism is directly applicable: Nav blockade at pharyngeal sensory nerve endings relieves pain and irritation caused by acute laryngopharyngitis.
- The Singapore market gap (currently not registered) may represent a genuine commercial and patient-care opportunity via an OTC regulatory pathway.

**To proceed on any indication, the following is needed:**

- **MOA documentation:** Retrieve Benzocaine's full pharmacology and safety profile from DrugBank API (DG002 remediation)
- **Regulatory safety data:** Download and parse the package insert warnings and contraindications (DG001 remediation — Blocking severity)
- **Methemoglobinaemia risk assessment:** Quantify risk by patient population, dose, and route before any ophthalmic or expanded-use application
- **Ophthalmic formulation feasibility study (if pursuing conjunctivitis):** Corneal penetration data and ocular toxicology are prerequisites
- **OTC registration pathway for Acute Laryngopharyngitis:** Review HSA OTC approval requirements; benchmark against existing approved formulations in comparable regulatory environments (TGA, FDA)
- **Contact allergy risk stratification:** Relevant for any topical formulation given ester-class hypersensitivity profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

