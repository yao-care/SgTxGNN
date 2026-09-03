---
layout: default
title: Trazodone
parent: 僅模型預測 (L5)
nav_order: 1006
evidence_level: L5
indication_count: 10
---

# Trazodone
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

# Trazodone: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Trazodone is a serotonin antagonist and reuptake inhibitor (SARI) originally approved for major depressive disorder. The TxGNN model predicts it may also be effective for **Obsessive-Compulsive Disorder (OCD)**, with **no registered clinical trials** but **20 publications** — including one placebo-controlled RCT — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (based on general pharmacological literature; no Singapore registration record available) |
| Predicted New Indication | Obsessive-Compulsive Disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (data gap). Based on the available literature, trazodone acts as a weak serotonin reuptake inhibitor (SERT) combined with 5-HT2A receptor antagonism (SARI class). Its efficacy in major depressive disorder is well established, and serotonergic modulation is mechanistically plausible for OCD, since OCD pathophysiology is strongly linked to serotonin dysregulation — the same rationale underlying the use of SSRIs and clomipramine as first-line OCD treatments.

However, trazodone's serotonin reuptake inhibition is considerably weaker than that of SSRIs, which remain the guideline first-line pharmacotherapy for OCD. The literature reflects this: most positive reports come from small open-label series or case reports, often in patients who failed clomipramine, with trazodone used as an adjunct or alternative rather than a primary agent. One controlled double-blind placebo trial exists, but results are limited in scale.

Overall, the mechanistic link is biologically reasonable but only moderately supported, and clinical evidence remains dated (predominantly 1980s–1990s) and low in methodological rigor by current standards.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | RCT | J Clin Psychopharmacol | Double-blind, placebo-controlled trial of trazodone in OCD patients; results modest compared to serotonin reuptake inhibitors. |
| [8993077](https://pubmed.ncbi.nlm.nih.gov/8993077/) | 1996 | Review | Psychopharmacol Bull | Discusses mono- and polypharmacotherapy of OCD; notes SRIs (not trazodone) as the primary FDA-approved class. |
| [8134850](https://pubmed.ncbi.nlm.nih.gov/8134850/) | 1994 | Review | South Med J | Reviews pharmacologic management of OCD, centered on serotonin/dopamine dysregulation hypothesis. |
| [8331098](https://pubmed.ncbi.nlm.nih.gov/8331098/) | 1993 | Review | J Clin Psychiatry | Reviews biological treatment strategies for treatment-resistant OCD, combining SRIs with adjunct agents. |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Review | Postgrad Med | General review of trazodone's approved and off-label uses, including psychiatric conditions beyond depression. |
| [26088119](https://pubmed.ncbi.nlm.nih.gov/26088119/) | 2015 | Review | Curr Pharm Des | Reviews off-label trazodone use, listing OCD among conditions with reported (non-approved) benefit. |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | Case Series/Open-label | Clin Neuropharmacol | Trazodone in 9 clomipramine-resistant OCD patients; mild but significant improvement, 3 strong responders. |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | Open-label (PET correlate) | Psychopathology | Trazodone response in OCD correlated with changes in caudate nucleus glucose metabolism on PET. |
| [6703152](https://pubmed.ncbi.nlm.nih.gov/6703152/) | 1984 | Case Report | Am J Psychiatry | Early case report describing trazodone use in OCD. |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | Case Report | J Nerv Ment Dis | Two cases of OCD with comorbid depression responding to trazodone. |

---

## Singapore Market Information

No Singapore (HSA) market authorization records are available for trazodone in this evidence pack. Market status is recorded as **Not Marketed**, with 0 registered licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are currently unavailable (data gap — flagged as **Blocking** in the evidence pack, pending TFDA/HSA label retrieval).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for trazodone in OCD is limited to one small placebo-controlled RCT plus older case reports/series (L3), the drug is not currently marketed in Singapore, and a blocking data gap exists for core safety information (warnings, contraindications, DDI), preventing a complete S1 safety assessment.

**To proceed, the following is needed:**
- Retrieve official package insert / regulatory label data for warnings and contraindications (resolve DG001)
- Confirm mechanism of action via DrugBank API (resolve DG002)
- Seek more recent or larger-scale controlled trials in OCD, given existing RCT evidence is from 1992
- Clarify Singapore registration pathway status, since the drug is currently not marketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

