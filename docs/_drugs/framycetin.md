---
layout: default
title: Framycetin
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
---

# Framycetin
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

# Framycetin: From Topical Antibacterial Use to Sclerosing Cholangitis

## One-Sentence Summary

Framycetin (DrugBank DB00452) is an aminoglycoside antibiotic conventionally used as a topical anti-infective for skin, eye, and ear infections; no original systemic indication is recorded in this evidence pack. The TxGNN model's top-ranked prediction proposes potential relevance to **Sclerosing Cholangitis**, but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the link as mechanistically unsupported and possibly a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — Framycetin is a topically-used aminoglycoside antibiotic (no systemic indication data on file) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Framycetin is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, Framycetin belongs to the aminoglycoside class, sharing a 30S ribosomal protein-synthesis-inhibition mechanism with other agents in this class, and has historically been used as a **topical/local** antibacterial rather than a systemic agent.

The TxGNN model's top prediction — Sclerosing Cholangitis — is not well supported mechanistically. Sclerosing cholangitis is primarily an autoimmune/fibrotic biliary disease rather than one driven by typical bacterial infection, and aminoglycosides such as Framycetin have limited coverage against biliary anaerobes. The model's own generated rationale explicitly notes that there is **no mechanistic basis** for a therapeutic role of Framycetin in this indication, and suggests the high TxGNN score may reflect a **knowledge-graph linkage artifact** (e.g., indirect connections through other antibiotic–hepatobiliary disease nodes) rather than a genuine pharmacological signal.

Given this, the prediction should be treated as a hypothesis-generation output only, not as a candidate ready for clinical consideration. Other lower-ranked predictions in this evidence pack (e.g., gonococcal urethritis, xanthogranulomatous pyelonephritis) carry comparatively stronger class-effect mechanistic reasoning than the top-ranked hit, even though none currently have direct clinical or literature evidence for Framycetin itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Sclerosing Cholangitis.

---

## Literature Evidence

Currently no related literature available for Sclerosing Cholangitis.

---

## Singapore Market Information

Framycetin currently has no marketing authorization on file (market status: Not Marketed; 0 registrations recorded). No licensed product information is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (No drug interaction records were found, and no warning/contraindication text is currently available in this evidence pack; TFDA label warnings/contraindications are flagged as a Blocking data gap, DG001, pending retrieval.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Sclerosing Cholangitis) has no supporting clinical trials or literature, sits at Evidence Level L5 (model prediction only), and the model's own mechanistic rationale explicitly questions the biological plausibility of the link, suggesting a possible knowledge-graph artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve official label warnings/contraindications before any S1 safety screening can begin
- Resolve DG002 (High): obtain confirmed mechanism of action data from DrugBank to properly assess mechanistic plausibility
- If pursuing repurposing further, consider re-evaluating lower-ranked but mechanistically stronger candidates in this pack (e.g., gonococcal urethritis, xanthogranulomatous pyelonephritis) rather than the top TxGNN-ranked hit
- Original indication and formulation data for Framycetin (route of administration, approved local uses) should be sourced and confirmed, since none is currently present in the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

