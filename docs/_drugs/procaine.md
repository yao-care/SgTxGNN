---
layout: default
title: Procaine
parent: 僅模型預測 (L5)
nav_order: 818
evidence_level: L5
indication_count: 10
---

# Procaine
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

# Procaine: From Unspecified Original Indication to Methemoglobinemia (Likely False-Positive Prediction)

## One-Sentence Summary

Procaine's original approved indication and mechanism of action are not available in this evidence pack (data gap). TxGNN's top-ranked prediction is **Methemoglobinemia**, but the supporting literature actually documents procaine as a **cause** of methemoglobinemia rather than a treatment for it — this is most likely a reversed-causality artifact, not a genuine repurposing signal. Of the 10 candidates reviewed, only two (fibromyalgia, tendinitis — ranks 7–8) show a biologically plausible treatment relationship, though evidence quality remains low (L3).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no Taiwan/Singapore license data, `original_indications` empty) |
| Predicted New Indication | Methemoglobinemia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`), and no approved indication is on file for Procaine in this jurisdiction.

More importantly, **this prediction does not appear mechanistically reasonable**. The literature retrieved for "methemoglobinemia" consistently describes procaine as an oxidizing agent that *causes* methemoglobinemia — through its metabolites, analogous to other aromatic-amine-type oxidants — rather than a drug used to *treat* it. Case reports (e.g. PMID 5529388, PMID 705003) and a cohort study (PMID 3691245) all frame procaine as the causal trigger, not the therapy.

This pattern is consistent with a known failure mode of knowledge-graph embedding models: a strong "drug–disease" association can be learned from literature co-occurrence without the model distinguishing *causes* from *treats*. TxGNN's high score (99.50%) here most likely reflects this causal-direction confusion rather than a genuine repurposing opportunity. The same caveat applies to rank 2 (methemoglobinemia, alpha type) and rank 5 (methemoglobin reductase deficiency), and a similar causal reversal is documented for rank 4 (anaphylaxis, where procaine/procaine-penicillin is the allergen, not the treatment).

Among the 10 candidates in this evidence pack, only **fibromyalgia** (rank 7, L3, historical trigger-point/intradermal procaine injections for fibrositis) and **tendinitis** (rank 8, L3, supported by a 2022 prospective cohort using 1% procaine for supraspinatus tendinopathy, plus a 2013 RCT of local-anesthetic vs. steroid injection for lateral epicondylitis) have a biologically coherent, direction-correct treatment rationale — local anesthetic infiltration for pain/spasm relief. These are worth separate evaluation but are **not** the top-ranked candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case Report | Acta physiologica latino americana | Reports methemoglobinemia caused by intravenous procaine — procaine as causal agent, not therapy. |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Unclassified | American Journal of Obstetrics and Gynecology | Studies placental passage of procaine and PABA; not related to methemoglobinemia treatment. |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | General review of rational local anaesthetic use; no methemoglobinemia-specific findings. |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case Report | Lancet | Methaemoglobinaemia following lignocaine (a related but different local anaesthetic, not procaine). |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Unclassified | Laval Medical | General overview article on local anaesthetics. |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Cohort | Zhonghua wai ke za zhi (Chinese Journal of Surgery) | Studies effect of intravenous procaine anesthesia on methemoglobin levels — procaine raises MetHb. |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Unclassified | Fundamental and Applied Toxicology | Discusses toxicologic interactions of organophosphate insecticides; only tangentially relevant. |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | Case Report | Revista Española de Anestesiología y Reanimación | Methemoglobinemia in a newborn after subcutaneous procaine (novocaine) infiltration during general anesthesia — again, procaine as cause. |

**Note:** All eight papers describe procaine as a *cause* of methemoglobinemia, not as a candidate treatment. This directly undermines the repurposing hypothesis for rank 1.

---

## Singapore Market Information

Procaine currently has **no product registrations on file** in Singapore (market status: Not Marketed, 0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Blocking data gap:** TFDA/HSA label warnings and contraindications for Procaine are not currently available in this evidence pack (`DG001`, severity: Blocking). This must be resolved before any S1 safety pre-evaluation can proceed. Drug-drug interaction search also returned no results (`query_status: not_found`, 0 interactions found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (methemoglobinemia) is most likely a reversed-causality artifact — all supporting literature shows procaine causing the condition, not treating it — so it does not represent a credible repurposing candidate. Combined with a blocking safety data gap (no TFDA/HSA label data) and zero current market presence in Singapore, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve `DG001`: obtain TFDA/HSA label warnings and contraindications (Blocking — required before any safety pre-evaluation)
- Resolve `DG002`: obtain Procaine's mechanism of action from DrugBank to properly assess mechanistic plausibility
- If pursuing repurposing research, redirect focus away from rank 1 (methemoglobinemia) and instead scope a research question around the two candidates with direction-correct, if still weak (L3), evidence: **fibromyalgia** (rank 7) and **tendinitis** (rank 8), both involving local-anesthetic infiltration for pain/spasm — noting most supporting studies used other local anesthetics (e.g. lidocaine) rather than procaine itself, so procaine-specific extrapolation still needs validation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

