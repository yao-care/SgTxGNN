---
layout: default
title: Cetylpyridinium
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Cetylpyridinium
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

# Cetylpyridinium: From Oral Antiseptic to Aphthous Stomatitis

## One-Sentence Summary

Cetylpyridinium (CPC) is a cationic quaternary ammonium antiseptic with decades of established use in oral hygiene products — mouthwashes, throat lozenges, and combination oral preparations — for its broad-spectrum antimicrobial action against oral pathogens. The TxGNN model predicts it may be effective for **Aphthous Stomatitis** (recurrent canker sores/RAS), supported by **1 indirect clinical trial** and **4 publications**, including one pilot study directly evaluating a CPC-containing combination product in oral mucosal inflammation. Among all 10 predicted indications in this multi-pack, aphthous stomatitis is the only one with clinical-level evidence (L3) and a "Proceed with Guardrails" recommendation; all other predictions are rated Hold (L5, no supporting evidence).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oral antiseptic for mouth and throat hygiene (no Singapore registration on file) |
| Predicted New Indication | Aphthous Stomatitis |
| TxGNN Prediction Score | 82.17% (rank 9 by score; note: top TxGNN score in this pack is 95.01% for fetal erythroblastosis — but that indication has no supporting evidence) |
| Evidence Level | L3 — combination product clinical trial + historical case series |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (aphthous stomatitis only); Hold for all other 9 predicted indications |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a high-severity data gap). Based on well-established pharmacology, Cetylpyridinium chloride (CPC) is a cationic surfactant that works by electrostatically binding to the negatively charged outer membranes of bacteria, fungi, and enveloped viruses, increasing membrane permeability and causing cell lysis. This broad-spectrum topical antimicrobial activity has been validated through decades of use in over-the-counter oral care products.

Recurrent aphthous stomatitis (RAS) involves painful oral mucosal ulcers driven by immune dysregulation and disrupted oral microbiome balance. Secondary bacterial colonisation of ulcer sites perpetuates inflammation and delays healing — a mechanism directly addressable by CPC. Beyond antimicrobial activity, quaternary ammonium compounds have documented local anti-inflammatory properties that may modulate the pro-inflammatory microenvironment at ulcer margins.

Crucially, the route of administration is already established: CPC is formulated as lozenges, rinses, and sprays for oral and oropharyngeal use. No systemic exposure is required. This dramatically lowers the translational hurdle compared to other predicted indications in this pack. PMID 31762696 provides the most direct evidence — a pilot clinical study of Lysozyme + CPC + Lidocaine for chemotherapy/radiotherapy-induced oral mucositis, a condition with substantial pathophysiological overlap with RAS.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04383236](https://clinicaltrials.gov/study/NCT04383236) | N/A | Completed | 120 | Randomised controlled trial of probiotic lozenges (not CPC directly) in adults and children with minor RAS. The lozenge delivery format and RAS outcome measures are directly transferable to CPC lozenge evaluation; provides disease-model reference. Indirect relevance to CPC — not counted in primary evidence chain. |

> No clinical trials evaluating CPC monotherapy for aphthous stomatitis were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31762696](https://pubmed.ncbi.nlm.nih.gov/31762696/) | 2019 | Clinical Trial (Combination Product) | Materia Socio-Medica | Pilot study evaluating Lysozyme + CPC + Lidocaine combination for chemotherapy/radiotherapy-induced oral mucositis. CPC is a named active component; findings demonstrate tolerability and therapeutic signal in oral mucosal inflammation — the closest available direct CPC evidence for an oral ulcerative condition. |
| [821708](https://pubmed.ncbi.nlm.nih.gov/821708/) | 1976 | Historical Case Series | Curr Ther Res Clin Exp | Cepacaine (CPC-containing lozenge formulation) evaluated for post-tonsillectomy pain, pharyngitis, and minor oral infections. Establishes CPC's historical clinical use at the oropharyngeal mucosa and its local anaesthetic-antiseptic synergy. |
| [46626](https://pubmed.ncbi.nlm.nih.gov/46626/) | 1975 | Historical Case Series | Therapie der Gegenwart | Treatment of inflammatory diseases of the mouth and pharynx using Imposit (CPC-containing product). Early clinical documentation of CPC's role in oral inflammatory conditions. |
| [4781108](https://pubmed.ncbi.nlm.nih.gov/4781108/) | 1973 | Historical Case Series | Die Medizinische Welt | Conservative therapy for inflammatory mouth and pharyngeal conditions; includes CPC-based formulation data in historical context alongside other antiseptic agents. |

---

## Singapore Market Information

Cetylpyridinium has **no registered products** in Singapore as of the data cut-off (2026-06-15). No authorization numbers, approved dosage forms, or indication texts are on record. Any future market entry would require a new product registration with HSA Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information. Singapore HSA package insert data and TFDA prescribing information were not available in the current evidence pack (flagged as a blocking data gap). No drug–drug interactions were identified in the DDI database query.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(aphthous stomatitis only; all other 9 predicted indications rated Hold)*

**Rationale:**
CPC has a biologically plausible and direct mechanism for aphthous stomatitis via oral mucosal antimicrobial action, an established oral topical delivery route, and published clinical data incorporating CPC in a related oral mucosal inflammatory condition. The evidence base is limited — historical case series and one indirect RCT — but sufficient to justify structured investigation before ruling out this indication.

**To proceed, the following is needed:**

- **Safety data (blocking):** Obtain and review Singapore HSA or TFDA package insert to extract approved warnings, contraindications, and handling precautions before any safety classification can be made
- **MOA confirmation (high priority):** Retrieve full DrugBank entry for DB11073 to confirm mechanism of action, pharmacodynamic targets, and any known interaction pathways
- **Dedicated clinical trial:** Design or identify a Phase 2 RCT of CPC monotherapy (lozenge or rinse) versus active comparator (e.g., chlorhexidine rinse or topical corticosteroid) in recurrent aphthous stomatitis using standardised endpoints (ulcer size, pain VAS, healing time)
- **Formulation strategy:** Define optimal CPC concentration and vehicle (lozenge vs. mouthwash vs. spray) for RAS endpoints, drawing on existing oral care product precedents
- **Singapore regulatory pathway:** Assess HSA registration feasibility and product classification (Class A/B/C cosmetic vs. therapeutic product) given zero existing local registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

