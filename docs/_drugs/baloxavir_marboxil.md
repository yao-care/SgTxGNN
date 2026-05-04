---
layout: default
title: Baloxavir Marboxil
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Baloxavir Marboxil
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

# Baloxavir marboxil: From Influenza to Hemophagocytic Syndrome Associated with an Infection

## One-Sentence Summary

Baloxavir marboxil (Xofluza®) is a cap-dependent endonuclease inhibitor originally developed and approved for the treatment of acute influenza A and B infection.
The TxGNN model predicts it may have activity against **hemophagocytic syndrome associated with an infection**,
with **0 clinical trials** and **0 publications** currently supporting this direction.
All 10 predicted indications carry an L5 evidence level, and the overall recommendation is **Hold** pending mechanistic and safety data acquisition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute influenza A and B (approved in Japan, USA, EU; not registered in Singapore) |
| Predicted New Indication | Hemophagocytic Syndrome Associated with an Infection |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Baloxavir marboxil is the prodrug of baloxavir acid — the active moiety that selectively inhibits the cap-dependent endonuclease activity of the influenza virus PA subunit. This blocks the "cap-snatching" step of viral mRNA synthesis and halts influenza replication with a single oral dose. It is the first-in-class antiviral of this mechanism, approved by Japan's PMDA (2018), the US FDA (2018), and EMA (2020) under the brand name Xofluza®.

The proposed mechanistic bridge to infection-associated hemophagocytic syndrome (HPS) is indirect: influenza virus is a well-recognised trigger of secondary HPS through the induction of an uncontrolled cytokine storm (IFN-γ, IL-6, IL-18 cascade), leading to unregulated macrophage and T-cell activation. In theory, by rapidly clearing influenza virus, Baloxavir could reduce the viral immunostimulatory burden that initiates this cascade — thereby diminishing the risk of virus-triggered HPS as a secondary consequence of antiviral treatment. This is an **adjunct or preventive effect**, not a direct treatment of HPS pathophysiology. Baloxavir has no known activity on IFN-γ signalling, perforin-granzyme pathways, or other HPS-specific immune mediators.

The TxGNN high-confidence score most likely reflects the knowledge graph's structural proximity between "influenza antiviral" and "virus-associated macrophage activation / HPS" nodes, rather than a direct pharmacological relationship. This is a biologically plausible but mechanistically unvalidated prediction — and the ranking of #11,683 across the full disease space further confirms it is not among the model's strongest candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Baloxavir marboxil has **no registered products in Singapore** (HSA). No authorization numbers, approved indications, or dosage form data are available from the local regulatory database. The drug is marketed in Japan (Xofluza®, Shionogi & Co.), the United States, and Europe, but has not been submitted for or granted HSA registration as of the data cutoff (2026-04-10).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, drug interactions) were not retrievable from available sources at the time of this report. DDI query returned no results. TFDA/HSA package insert has not been parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every one of the 10 TxGNN-predicted indications for Baloxavir marboxil carries an **L5 evidence level** — model prediction only, with zero supporting clinical trials and no directly relevant published literature. The top-ranked prediction (hemophagocytic syndrome associated with an infection) relies on a biologically indirect inference that does not translate into a viable therapeutic hypothesis without foundational preclinical data. Furthermore, the drug is not registered in Singapore, leaving critical safety and regulatory context absent.

**To proceed, the following is needed:**

- **Safety data acquisition**: Download and parse the Xofluza® package insert (Japan PMDA or US FDA label) to capture key warnings, contraindications, and drug–drug interactions — classified as a Blocking data gap in this pack
- **MOA confirmation**: Retrieve mechanism of action details from DrugBank (DB13997) to validate or refute the mechanistic link to the predicted indications
- **Preclinical feasibility assessment**: Review whether any in vitro or animal model data exist showing Baloxavir's effect on cytokine storm, macrophage activation, or HPS-like inflammatory cascades
- **Case series review**: Search for case reports of influenza-associated HPS where Baloxavir was used, to detect any signal of differential clinical outcomes versus oseltamivir
- **Consider alternative indications**: Examine TxGNN predictions more closely aligned with Baloxavir's established antiviral mechanism (e.g., influenza complications, post-viral syndromes) which may offer a stronger evidence base for repurposing investigation

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All predicted indications are computational hypotheses pending biological and clinical verification.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

