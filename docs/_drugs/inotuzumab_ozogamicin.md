---
layout: default
title: Inotuzumab Ozogamicin
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Inotuzumab Ozogamicin
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

# Inotuzumab Ozogamicin: From B-Cell Precursor Acute Lymphoblastic Leukemia to Drug-Induced Osteoporosis

## One-Sentence Summary

Inotuzumab ozogamicin is an anti-CD22 antibody-drug conjugate (ADC) approved internationally for relapsed or refractory B-cell precursor acute lymphoblastic leukemia (ALL), and is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis** as its highest-ranked repurposing candidate (score: 98.24%),
however, with **0 clinical trials** and **0 directly relevant publications** supporting this direction, the evidence base remains at model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed or refractory B-cell precursor acute lymphoblastic leukemia (ALL) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 98.24% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Inotuzumab ozogamicin is a targeted antibody-drug conjugate composed of a humanized anti-CD22 IgG4 monoclonal antibody covalently linked to calicheamicin — a potent cytotoxic natural product that induces irreversible double-strand DNA breaks upon intracellular release. CD22 is a cell-surface glycoprotein expressed predominantly on mature B lymphocytes and on the blast cells of most B-cell precursor ALL patients. After the ADC binds to CD22 and is internalized, the calicheamicin payload is released, selectively killing CD22-expressing cells. This narrow mechanism of action is what makes the drug effective against B-cell malignancies.

Drug-induced osteoporosis, by contrast, is a metabolic bone disease driven by osteoclast/osteoblast imbalance, typically triggered by agents such as glucocorticoids, aromatase inhibitors, or androgen deprivation therapy. Its core pathophysiology revolves around RANKL/OPG signaling, vitamin D and calcium metabolism dysregulation, and direct suppression of osteoblast activity. There is no established direct link between the CD22 antigen or calicheamicin's DNA-damaging mechanism and bone remodeling pathways.

The high TxGNN knowledge graph score (98.24%) is most likely driven by indirect graph connectivity — for example, B cells are known to influence RANKL expression in the bone microenvironment, which in turn regulates osteoclastogenesis. While this indirect path exists biologically, it does not constitute a therapeutically actionable connection for an ADC targeting CD22. In practice, inotuzumab ozogamicin itself causes significant thrombocytopenia and hepatic sinusoidal obstruction syndrome, making safety in a non-oncology setting a further concern. This prediction should be considered a speculative, graph-topology artifact rather than a biologically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on Rank 5 (Breast Tumor Luminal A/B):** The evidence search for that indication retrieved 19 PubMed results; however, upon individual review, all publications relate to B-cell biology, hepatitis B vaccine studies, or unrelated topics. These represent keyword contamination (the letter "B" triggering B-cell–related literature) and contain no evidence supporting inotuzumab ozogamicin use in breast cancer.

---

## Singapore Market Information

Inotuzumab ozogamicin is **not registered** in Singapore. No marketing authorizations or product licenses were identified. Clinicians requiring access would need to pursue special access channels (e.g., clinical trial enrollment or compassionate use pathways), subject to HSA approval.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted cytotoxic — Antibody-Drug Conjugate (ADC); payload is calicheamicin, a DNA double-strand break inducer (enediyne class) |
| Myelosuppression Risk | **High** — Thrombocytopenia is a dose-limiting toxicity reported in >50% of patients in pivotal trials; neutropenia and febrile neutropenia are also common |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (monitor for thrombocytopenia and neutropenia), liver function tests with particular attention to sinusoidal obstruction syndrome (SOS/VOD), total bilirubin, renal function, coagulation profile |
| Handling Protection | Must follow cytotoxic/hazardous drug handling regulations; ADC preparation requires specialized pharmacy biosafety protocols (closed-system transfer devices recommended) |

---

## Safety Considerations

Please refer to the package insert for complete safety information. Given that inotuzumab ozogamicin itself causes dose-limiting thrombocytopenia and carries a black-box warning for hepatic sinusoidal obstruction syndrome (SOS/VOD) in international labeling, extrapolation to non-oncology indications such as drug-induced osteoporosis raises significant safety concerns that would need to be thoroughly characterized before any clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinically coherent mechanistic link between inotuzumab ozogamicin's anti-CD22 mode of action and the pathophysiology of drug-induced osteoporosis. All 10 TxGNN-predicted indications for this drug return an L5 evidence level (model prediction only, zero supporting trials or literature), and several predictions — including breast cancer subtypes, platelet disorders, pseudo-von Willebrand disease, and infectious bovine rhinotracheitis — exhibit clear mechanistic implausibility or fall entirely outside the scope of human oncology. The drug's known serious toxicities (thrombocytopenia, hepatotoxicity) further complicate any non-oncology repurposing scenario.

**To proceed, the following is needed:**

- **Mechanistic validation:** Identify a biologically plausible and testable hypothesis connecting CD22/B-cell biology to bone resorption (e.g., B-cell–mediated RANKL upregulation in steroid-induced osteoporosis models)
- **Preclinical proof-of-concept:** In vitro or in vivo studies demonstrating that anti-CD22 targeting reduces bone loss in drug-induced osteoporosis animal models
- **MOA data retrieval:** Query DrugBank API to obtain complete mechanism-of-action data for formal mechanistic analysis
- **Safety package review:** Obtain and parse the full prescribing information (package insert) to complete S1 safety screening, including warnings, contraindications, and special population data
- **Regulatory pathway assessment:** Evaluate feasibility of Singapore registration or compassionate use given current non-marketed status and the nature of the proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

