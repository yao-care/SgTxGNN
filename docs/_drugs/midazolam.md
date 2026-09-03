---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 665
evidence_level: L5
indication_count: 10
---

# Midazolam
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

# Midazolam: From Sedative/Anesthetic Use to Insomnia

## One-Sentence Summary

> Midazolam is a short-acting benzodiazepine GABA-A receptor agonist, most widely used clinically for procedural sedation, anesthesia induction, and peri-operative anxiolysis; detailed original-indication and mechanism-of-action data are not yet available in this evidence pack.
> The TxGNN model predicts it may be effective for **Insomnia**,
> with **32 clinical trials** and **11 publications** currently identified, though most trials use midazolam only as a comparator rather than as the primary study drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore HSA license/indication text on file (see Data Gap DG001/DG002) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available at the drug level (marked as a Data Gap). Based on known pharmacology cited in the evidence pack's repurposing rationale, midazolam is a benzodiazepine that acts at the GABA-A receptor benzodiazepine binding site, enhancing inhibitory GABAergic transmission and producing sedative/hypnotic effects — the same mechanism shared by benzodiazepines already approved for insomnia (e.g., triazolam, flurazepam).

Since the evidence pack contains no recorded original indication text for midazolam in this jurisdiction, a direct comparison between "original indication" and "insomnia" cannot be made from the structured data alone. However, the mechanistic overlap with approved hypnotic benzodiazepines directly supports biological plausibility for an insomnia indication.

A key caveat noted in the evidence pack: midazolam's short half-life carries risk of next-day rebound anxiety/insomnia and dependence, which limits its suitability for long-term chronic insomnia management even where acute hypnotic efficacy is demonstrated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Dexmedetomidine vs. midazolam sedation compared for postoperative sleep quality after TURP |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | Recruiting | 280 | Preoperative oral midazolam evaluated in patients with pre-existing sleep disturbance/anxiety undergoing colorectal surgery |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | NA | Terminated (N=5) | 5 | Direct comparison of dexmedetomidine vs. midazolam on sleep quality/quantity via 24-hour polysomnography in ICU patients |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated (N=6) | 6 | Polysomnographic comparison of α2-agonist vs. GABA-agonist (midazolam class) sedation on sleep stages |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unknown | 120 | Dexmedetomidine vs. midazolam sedation efficacy in critically ill ventilated children |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Phase 3 | Not yet recruiting | 195 | Oral melatonin vs. oral midazolam premedication; notes midazolam's sleep-inducing but non-ideal side-effect profile |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | NA | Completed | 23 | Transition from benzodiazepine (midazolam) to dexmedetomidine sedation near extubation in ICU |
| [NCT04149626](https://clinicaltrials.gov/study/NCT04149626) | Phase 2 | Unknown | 60 | Midazolam vs. dexmedetomidine vs. remifentanil sedation compared in orthopedic surgery under regional anesthesia |
| [NCT01050699](https://clinicaltrials.gov/study/NCT01050699) | Phase 4 | Completed | 90 | Sedation effects on sleep and inflammatory markers in critically ill ALI/ARDS patients (dexmedetomidine-focused, benzodiazepine comparator) |
| [NCT01791296](https://clinicaltrials.gov/study/NCT01791296) | Phase 4 | Completed | 100 | Sedation protocol effect on delirium incidence and sleep in critically ill patients (dexmedetomidine-focused) |

**Note:** Across the 32 trials returned for this indication, the large majority use midazolam only as an active comparator/control arm for another investigational agent (dexmedetomidine, ketamine, remimazolam) rather than testing midazolam as a primary insomnia treatment. Only a small subset directly assess midazolam's effect on sleep outcomes.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Midazolam 15mg vs. Vesparax in insomnia secondary to neuromuscular disease; midazolam was an efficient hypnotic, better tolerated, no hangover |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | 14-day multicenter RCT of flurazepam vs. midazolam on sleep, performance, and plasma levels in chronic insomniacs |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT | Arzneimittel-Forschung | Dose-finding study (10–30mg oral midazolam) in 75 hospitalized patients with mild-moderate insomnia; established optimal dose range |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Executive summary of the multicenter 14-day flurazepam/midazolam chronic insomnia trial |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatrica Scandinavica Suppl. | Clinical use of hypnotics including benzodiazepines across insomnia subtypes |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orvosi Hetilap | General review of insomnia pathophysiology and hyperarousal state (not midazolam-specific) |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Cohort | Journal of Clinical Medicine | Lemborexant (not midazolam) evaluated for insomnia/delirium prevention post-endoscopy; benzodiazepines noted as delirium-risk comparator class |
| [22729271](https://pubmed.ncbi.nlm.nih.gov/22729271/) | 2013 | Preclinical | Psychopharmacology | Zolpidem (not midazolam) effects on sedation/anxiety/memory in animal model |
| [36912148](https://pubmed.ncbi.nlm.nih.gov/36912148/) | 2024 | Review | American Journal of Hospice & Palliative Care | End-of-life symptom management case discussion (peripheral relevance) |
| [21396773](https://pubmed.ncbi.nlm.nih.gov/21396773/) | 2011 | Preclinical | Pain | GABAergic transmission changes underlying sleep disturbance in neuropathic pain mouse model (mechanistic, not midazolam-specific) |

**Note:** The four Tier-1 RCTs (PMID 6138072, 2121802, 6120704, 2229461) are the strongest evidence, but all date from 1981–1990, predate modern insomnia diagnostic/outcome standards, and were not designed for regulatory-grade efficacy claims.

---

## Singapore Market Information

Midazolam currently has **no HSA registration on file** in this evidence pack (market status: Not Marketed, 0 licenses). No product listing table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack — see DG001, a Blocking-severity gap requiring HSA/TFDA label retrieval before any S1 safety screening can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Four Tier-1 RCTs from the 1980s consistently show midazolam has hypnotic efficacy in insomnia, and the GABA-A mechanism is consistent with approved hypnotic benzodiazepines — supporting the L2 evidence level and S2 decision stage already assigned. However, the trials are decades old, mostly small, and the majority of the 32 registered clinical trials use midazolam only as a comparator arm rather than a primary insomnia treatment, so real-world efficacy/safety in a modern chronic-insomnia population remains unconfirmed. A related indication, **anxiety disorder** (rank 6, also L2/Proceed with Guardrails), is better supported by contemporary Phase 2–4 RCTs and may be a stronger near-term repurposing candidate; the other eight predicted indications (myofascial pain, OCD, tendinitis, etc.) currently rest on Hold due to L4–L5 evidence with no mechanistic or trial support specific to midazolam.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve TFDA/HSA package insert warnings and contraindications — required before S1 safety screening
- Resolve DG002 (High): confirm midazolam's mechanism of action via DrugBank API
- Clarify Singapore regulatory pathway, since the drug currently has zero HSA registrations
- Commission or identify a modern-era RCT (post-2000) evaluating midazolam specifically for insomnia, given the existing evidence base predates current diagnostic/outcome standards
- Assess dependence/rebound-insomnia risk data given midazolam's short half-life, particularly for any chronic (non-procedural) use case
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

