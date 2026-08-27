---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 606
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Acute Diarrhea to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is a well-established over-the-counter antidiarrheal agent that acts on intestinal opioid receptors to reduce gut motility, widely used for symptomatic relief of acute and chronic diarrhea.
The TxGNN model predicts it may be effective for **Acute Contagious Conjunctivitis**, however **no clinical trials and no relevant publications** currently support this direction.
The biological rationale connecting intestinal opioid receptors to ocular conjunctival disease is not established, and the high model score most likely reflects non-specific co-occurrence clustering in the knowledge graph rather than a true mechanistic link.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute diarrhea (symptomatic relief) |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on established pharmacological knowledge, Loperamide is a peripheral μ-opioid receptor agonist that acts specifically on the enteric nervous system. It slows intestinal peristalsis, reduces fluid and electrolyte secretion into the bowel lumen, and increases anal sphincter tone — all localised effects that do not cross the blood-brain barrier at therapeutic doses.

Acute contagious conjunctivitis is an inflammatory or infectious condition of the conjunctival membrane of the eye, driven by viral, bacterial, or allergic immune mechanisms. There is no established physiological pathway through which peripheral intestinal opioid receptor agonism would influence conjunctival immunity, tear film production, or ocular surface inflammatory responses. The repurposing rationale in the evidence pack explicitly identifies this as a likely **knowledge graph artefact** — the high TxGNN score is attributed to non-specific co-occurrence clustering between diarrhea-infection nodes rather than a genuine mechanistic signal.

In summary, the biological plausibility for this prediction is very low. The two disease domains (gastrointestinal motility disorders and ocular surface infections) are mechanistically disconnected, and the model score alone is insufficient grounds to pursue this indication without corroborating biological or clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Loperamide in acute contagious conjunctivitis.

> **Note:** Two clinical trials were retrieved in the database query for the related term "conjunctivitis" (NCT04185402, NCT06289647), but both study Azithromycin for trachoma elimination and have no relevance to Loperamide. They are excluded from this report.

---

## Literature Evidence

Currently no related literature available for Loperamide in acute contagious conjunctivitis.

---

## Singapore Market Information

Loperamide is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product licences or authorisation records were found.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Known signal of note (from Evidence Pack clinical data):** At **rank 10**, the evidence pack flags that high-dose Loperamide carries cardiac toxicity risk via hERG channel blockade. This is relevant context for any safety assessment of this drug. It is particularly notable for indication **Angelucci syndrome** (allergic conjunctivitis with cardiac palpitations), where Loperamide's cardiac risk profile makes it a contraindicated candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.97% for acute contagious conjunctivitis is high in absolute terms, but is assessed to be a knowledge graph artefact with no underlying biological mechanism connecting Loperamide's intestinal μ-opioid receptor activity to conjunctival disease. Evidence level is L5 (model prediction only) with zero supporting clinical trials or literature.

**To revisit this decision, the following would be needed:**

- Identification of a credible mechanistic hypothesis linking peripheral opioid receptor activity to conjunctival pathophysiology (e.g., mucosal immune cross-talk, shared neuropeptide signalling)
- At minimum one preclinical study (animal model or in vitro) demonstrating any ocular surface activity of Loperamide or closely related opioid receptor ligands
- Resolution of current data gaps: formal MOA documentation (DrugBank API query) and HSA/TFDA package insert warnings to enable basic safety screening

**Among the 10 predicted indications reviewed, the most scientifically credible candidate for further investigation is Rank 4: Gastroduodenitis** — where Loperamide's mechanism (reduced GI motility, mucosal protection via slowed luminal flow) has a plausible symptomatic link, and a 1986 Soviet clinical observation (PMID 3520142) provides a preliminary signal, albeit of uncertain methodological quality.

---

*⚠️ This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

