---
layout: default
title: Progesterone
parent: 僅模型預測 (L5)
nav_order: 820
evidence_level: L5
indication_count: 10
---

# Progesterone
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

# Progesterone: From Hormone Therapy to Amenorrhea

## One-Sentence Summary

> Progesterone is an endogenous steroid hormone long used in reproductive endocrinology (luteal support, hormone replacement, progestin-challenge testing); however, this evidence pack has no recorded original indication text (data gap — original_indications is empty and requires manual verification against the actual package insert). The TxGNN model predicts efficacy for **Amenorrhea (disease)**, with **60 clinical trials** and **20 publications** identified — though most evidence reflects progesterone's already well-established, textbook role in diagnosing and managing secondary amenorrhea rather than a genuinely novel signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — Singapore license list is empty (0 records); `original_indications` is flagged as a data gap, not a confirmed absence of indication |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for this DrugBank record (DB00396) is not available in the evidence pack. Based on general pharmacological knowledge, progesterone is an endogenous steroid hormone acting on nuclear progesterone receptors (PR-A/PR-B) in the endometrium, myometrium, and along the hypothalamic-pituitary-ovarian (HPO) axis, where it modulates LH/FSH pulsatility and drives endometrial secretory transformation.

The evidence pack's own repurposing rationale notes: *"Progesterone/progestins are a standard diagnostic and therapeutic tool for secondary amenorrhea (progestin challenge test), acting directly on the endometrium and the HPO axis — the mechanism is well established, textbook-level knowledge."* This is an important caveat: because `original_indications` is empty (a data gap, not a true absence of approved use), the "amenorrhea" prediction likely represents the KG model correctly recovering an **already-known** clinical application of progesterone rather than identifying a truly novel repurposing opportunity. Manual verification against the actual approved package insert is recommended before treating this as new evidence.

That said, the mechanistic link is pharmacologically sound and is reinforced by the volume of clinical and literature evidence around progesterone/progestin use in amenorrhea-related conditions (hypothalamic amenorrhea, chemotherapy-induced amenorrhea, PCOS-related oligomenorrhea, and progestin-withdrawal bleeding protocols).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01185782](https://clinicaltrials.gov/study/NCT01185782) | Phase 3 | Completed | 300 | Comparative study of SJ-0021 vs. purified pituitary gonadotropin in subjects with Amenorrhea I or anovulatory cycles due to hypothalamic/pituitary dysfunction |
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | RCT of post-endometrial-ablation medroxyprogesterone acetate on amenorrhea rates in heavy menstrual bleeding |
| [NCT05312190](https://clinicaltrials.gov/study/NCT05312190) | N/A | Unknown | 330 | Multicenter RCT comparing Progesterone Capsules, a TCM formula, and their combination for menstrual disorders in adult women |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | RCT testing whether progesterone-induced endometrial withdrawal bleeding is necessary before ovulation induction in women with oligo-/amenorrhea |
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Phase 3 | Completed | 1,845 | Large placebo-controlled RCT of combined estradiol + progesterone for vasomotor symptoms in postmenopausal women with an intact uterus |
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Study of reproductive/endocrine function and estrogen therapy in adolescent athletes with exercise-associated amenorrhea |
| [NCT02744131](https://clinicaltrials.gov/study/NCT02744131) | N/A | Unknown | 100 | OCP vs. metformin in PCOS women; progesterone protocol used to induce withdrawal bleeding for amenorrhea >2 months |
| [NCT03309709](https://clinicaltrials.gov/study/NCT03309709) | Phase 3 | Unknown | 90 | RCT of subcutaneous progesterone (luteal-phase dosing) vs. watchful waiting for endometrial polyp regression in premenopausal women |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | Recruiting | 120 | RCT of transdermal estradiol with cyclic progesterone vs. placebo in hypoestrogenemic adolescents/young adults with eating-disorder-related amenorrhea |
| [NCT06533865](https://clinicaltrials.gov/study/NCT06533865) | Phase 3 | Recruiting | 114 | Romosozumab as adjunct to physiologic estrogen + cyclic progesterone replacement for low bone density in functional hypothalamic amenorrhea |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Reviews in Endocrine & Metabolic Disorders | Comprehensive review of diagnostic and therapeutic uses of oral micronized progesterone, including HPO-axis and endometrial mechanisms |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Review | Curr Probl Pediatr Adolesc Health Care | Review of amenorrhea etiology/management in adolescents, organized by HPO-axis dysfunction |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | American Family Physician | Classic clinical evaluation-of-amenorrhea reference, foundational to the progestin-challenge-test diagnostic approach |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Frontiers in Endocrinology | Review of premature ovarian insufficiency (POI) etiology, symptomatology, and hormone-replacement treatment options |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | Review | Southern Medical Journal | Current concepts in POI, including hormone replacement therapy and secondary amenorrhea management |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | Clinical management of postmenopausal vaginal bleeding, discussing estrogen/progesterone-driven endometrial atrophy |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecological Endocrinology | Neuroendocrine control of ovulation; HPO-axis failure as the mechanistic basis of anovulation/amenorrhea |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Reviews in Endocrine & Metabolic Disorders | Endocrine background of hormonal treatments for endometriosis, including progesterone-resistance mechanisms |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | Meta-analysis | Frontiers in Oncology | Meta-analysis of chemotherapy-induced amenorrhea risk factors and prognostic significance in premenopausal breast cancer |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Seminars in Reproductive Medicine | Review of intrauterine adhesions (Asherman's syndrome), spanning the spectrum from amenorrhea to normal menses |

---

## Singapore Market Information

Progesterone currently holds **no marketing authorization records** in Singapore under this evidence pack (0 licenses on file, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack — see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and well-established (progesterone's role in the HPO axis and endometrium), and is supported by two completed Phase 3 RCTs directly relevant to amenorrhea-related populations plus a broad base of supporting literature. However, this appears to largely reflect **already-known clinical use** rather than a novel indication, and two blocking/high-severity data gaps prevent a full safety assessment.

**To proceed, the following is needed:**
- **TFDA/HSA package insert warnings and contraindications (DG001, Blocking)** — required before any S1 safety screening can proceed; source: official regulatory label PDF
- **Confirmed mechanism-of-action and original approved indications (DG002, High)** — `original_indications` is empty and should not be read as "no indication"; verify via DrugBank API / package insert to determine whether "amenorrhea" is a genuinely new signal or an existing approved use
- **Drug-drug interaction data** — DDI query returned no results; a targeted interaction search is recommended before clinical guardrails can be finalized
- Manual clinical review to confirm whether trial evidence (e.g., NCT01185782, NCT02449161) applies to the specific amenorrhea subtype/etiology of interest, since the trials span hypothalamic, pituitary, and iatrogenic (ablation/chemotherapy) causes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

