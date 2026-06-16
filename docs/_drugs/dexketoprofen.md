---
layout: default
title: Dexketoprofen
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
---

# Dexketoprofen
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

# Dexketoprofen: From Acute Musculoskeletal Pain to Tendinitis

## One-Sentence Summary

Dexketoprofen is the pharmacologically active S-enantiomer of ketoprofen, a propionic acid-class NSAID approved in multiple markets (EU, Middle East) for mild to moderate acute pain including musculoskeletal conditions, dental pain, and dysmenorrhoea — but currently **not registered in Singapore**.
The TxGNN model identifies **Tendinitis** as its top-ranked repurposing candidate (score 99.90%), supported by **no registered clinical trials** and **1 publication** specifically addressing this direction.
Notably, **Migraine Disorder** (rank 6) emerges as a higher-evidence opportunity with **8 completed clinical trials** and **20 publications** (L1), warranting separate consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; approved in EU/other markets for acute pain (musculoskeletal, dental, dysmenorrhoea) |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, Dexketoprofen is a non-steroidal anti-inflammatory drug that inhibits both cyclooxygenase-1 (COX-1) and cyclooxygenase-2 (COX-2), thereby blocking the synthesis of prostaglandins and thromboxanes. As the S-enantiomer of ketoprofen, it retains full analgesic potency while offering a faster onset compared to the racemate, attributable to its more favourable pharmacokinetic profile.

Tendinitis is characterised by localised inflammatory pathology within tendon tissue, with prostaglandin E2 (PGE2) — generated via the COX-2 pathway — being the principal mediator of pain, oedema, and functional impairment. COX inhibition directly targets this mechanism, reducing local PGE2 production and interrupting the inflammatory cascade. The mechanistic rationale is therefore well-founded: NSAIDs represent standard of care for acute tendinitis, and Dexketoprofen's rapid absorption and short half-life make it well-suited for episodic, acute musculoskeletal presentations.

It is important to note that Dexketoprofen is already indicated for musculoskeletal pain in approved markets — tendinitis is clinically subsumed within that category. The TxGNN prediction may represent a formal disease-specific extension of an existing use rather than a wholly novel repurposing pathway. This contrasts with **Migraine Disorder** (rank 6), which represents a more pharmacologically distinct indication with substantially stronger clinical evidence (8 clinical trials, 20 publications, L1 level) and a more compelling case for active development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dexketoprofen specifically in tendinitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | RCT (IV Dexketoprofen vs IV Paracetamol) | The American Journal of Emergency Medicine | Compared intravenous dexketoprofen against paracetamol for non-traumatic musculoskeletal pain in the emergency department; tendinitis was among the included aetiologies. Both agents produced significant pain reduction on VAS; findings provide indirect support for Dexketoprofen's analgesic efficacy in tendon-related inflammation. |

---

## Singapore Market Information

Dexketoprofen (DrugBank ID: DB09214) is **not currently registered** with the Singapore Health Sciences Authority (HSA). No product authorisations, dosage forms, or approved indications are on record. Any clinical deployment in Singapore would require a full New Drug Application or a separate regulatory submission pathway.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
TxGNN assigns tendinitis as the highest-ranked prediction for Dexketoprofen (score 99.90%), and the COX-2/prostaglandin inhibition mechanism provides a sound pharmacological basis. However, dedicated clinical evidence for tendinitis specifically is limited to a single indirect RCT, no registered trials exist, and the drug is entirely absent from the Singapore market — all of which preclude a higher-stage recommendation at this time.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full mechanism of action from DrugBank API or the EMA/PMDA-approved product monograph to complete mechanistic analysis
- **Safety data**: Download and parse the TFDA or EMA package insert to identify key warnings, contraindications, and drug–drug interactions (currently all [Data Gap])
- **Dedicated clinical evidence**: Commission or identify prospective observational studies or RCTs specifically evaluating Dexketoprofen in tendinitis populations
- **Singapore regulatory pathway**: Assess feasibility and timeline for HSA product registration (New Drug Application)
- **Prioritisation review**: Consider reallocating development effort toward **Migraine Disorder** (rank 6, L1 evidence, "Proceed with Guardrails") and **Headache Disorder** (rank 7, L1 evidence), which present substantially more mature evidence bases and stronger near-term repurposing viability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

