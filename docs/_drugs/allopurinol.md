---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout/Hyperuricemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a well-established xanthine oxidase (XO) inhibitor, approved worldwide for the treatment of gout and hyperuricemia by reducing uric acid production.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**,
with **0 clinical trials** and **2 publications** currently supporting this direction — both at the hypothesis or animal-study level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout / Hyperuricemia (xanthine oxidase inhibitor) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, Allopurinol is a xanthine oxidase (XO) inhibitor that blocks the conversion of hypoxanthine → xanthine → uric acid. Its primary clinical use is in gout and hyperuricemia. By reducing XO activity, it also attenuates reactive oxygen species (ROS) generation via the XO pathway, giving it secondary antioxidant properties.

The proposed bridge to hepatic porphyria rests on the heme biosynthesis pathway. Acute hepatic porphyrias are driven by overactivation of 5-aminolevulinate synthase 1 (ALAS1), which leads to accumulation of toxic porphyrin precursors (ALA and PBG). PMID 31443750 (Badawy, 2019) hypothesises that XO inhibitors — including Allopurinol — may indirectly downregulate ALAS1 by modulating the regulatory hepatic free-heme pool, since heme utilisation by tryptophan 2,3-dioxygenase (TDO) is thought to deplete the feedback-inhibitory heme pool. By sparing heme from TDO consumption, XO inhibition could theoretically restore negative feedback on ALAS1.

This mechanistic chain has biological plausibility but remains entirely at the hypothesis stage. No direct experimental or clinical evidence currently demonstrates that Allopurinol reduces ALAS1 activity or attenuates porphyric attacks in any in vitro, animal, or human study. The second supporting paper (PMID 1567472) examines carbamazepine's — not Allopurinol's — effects on haem metabolism, and is relevant only insofar as it characterises the same regulatory pathway. The overall rationale is speculative and requires experimental validation before advancing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Opinion | Medical Hypotheses | Proposes that XO inhibitors (including Allopurinol) may reduce ALAS1 activity by preserving the hepatic free-heme pool via inhibition of TDO-mediated heme utilisation; a theoretical therapy for acute hepatic porphyrias, unvalidated experimentally |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study | Biochemical Pharmacology | Demonstrates that acute carbamazepine administration exacerbates hepatic haem metabolism in rats by depleting the heme pool via tryptophan pyrrolase; contextually supports the regulatory heme feedback pathway but does not involve Allopurinol |

---

## Singapore Market Information

Allopurinol currently has **no registered products** in Singapore's HSA database. This drug is not marketed in Singapore under any authorisation number.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** A blocking data gap exists for this report. TFDA/HSA package insert warnings and contraindications have not been retrieved (Data Gap DG001, severity: Blocking). This prevents formal safety screening (Stage S1). Full safety evaluation — including Steven-Johnson Syndrome / DRESS risk (a well-known serious adverse effect of Allopurinol), renal dose-adjustment requirements, and drug interactions with azathioprine/mercaptopurine — must be completed before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only mechanistic support for Allopurinol in hepatic porphyria is a single hypothesis paper (2019) proposing an indirect pathway through TDO–heme pool regulation; no clinical trials exist, and no animal model studies directly test this hypothesis for Allopurinol. L4 evidence with a purely speculative mechanism does not justify advancing to a repurposing feasibility study at this stage.

**To proceed, the following is needed:**

- **Mechanism validation (Priority 1):** Conduct or identify in vitro / animal studies directly measuring Allopurinol's effect on ALAS1 activity and porphyrin precursor levels in hepatic porphyria models
- **MOA data retrieval (Data Gap DG002):** Query DrugBank API for complete pharmacological profile, including known off-target effects beyond XO inhibition
- **Safety package (Data Gap DG001 — Blocking):** Download and parse HSA/TFDA package insert PDF to extract warnings, contraindications, and DDI data; Allopurinol carries known risk of severe cutaneous adverse reactions (SCAR/DRESS), especially in HLA-B\*58:01 carriers prevalent in Asian populations
- **HLA-B\*58:01 pharmacogenomics assessment:** Given the Singapore/Asian patient context and the known SCAR risk, a pharmacogenomic risk statement is required before any clinical protocol design
- **Porphyria-specific DDI screen:** Several drugs known to trigger acute porphyric attacks overlap with Allopurinol co-medications; a dedicated DDI review for porphyria patients is needed
- **Feasibility review of existing porphyria therapies:** Compare against givosiran (approved siRNA therapy targeting ALAS1) to contextualise where Allopurinol might add value, if any
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

