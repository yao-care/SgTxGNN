---
layout: default
title: Cyproterone Acetate
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 10
---

# Cyproterone Acetate
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

# Cyproterone Acetate: From Hyperandrogenism to Migraine Disorder

## One-Sentence Summary

Cyproterone acetate (CPA) is a synthetic antiandrogen and potent progestogen internationally established for hyperandrogenism, hirsutism, and polycystic ovary syndrome (PCOS); in high doses it is used for hormonal suppression in prostate cancer. The TxGNN model predicts it may have relevance for **Migraine Disorder** — the highest-ranked of 10 new predicted indications — supported by **no clinical trials** and only **3 publications** providing indirect mechanistic evidence. Across the full landscape of 10 predictions, only **amenorrhea/PCOS-related menstrual disorders (Rank 8)** reaches actionable evidence (L3, 4 trials, 14 publications); five other predictions are **active safety contraindications** where CPA would cause harm rather than benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; internationally approved for hyperandrogenism and PCOS-related conditions (EU: Diane-35, Androcur) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 (mechanism/review literature only; no clinical trials) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cyproterone acetate is a synthetic steroidal compound with dual activity: it competitively blocks androgen receptors and suppresses gonadotropin (LH/FSH) secretion, thereby reducing testosterone production. Beyond its classical hormonal role, CPA engages the neurosteroid axis — progesterone is metabolised downstream to allopregnanolone, a potent positive allosteric modulator of GABA-A receptors. PMID 14670648 (Gruber & Huber, 2003) specifically documents that CPA interacts with GABA-A receptor subtypes, stimulates dopamine release in striatal tissue, modulates GnRH release from hypothalamic neurons, and binds opioid receptors — all pathways that have been implicated in migraine pathophysiology.

The hormone-migraine connection is well-established in clinical observation. Menstrual migraine is closely linked to the perimenstrual drop in progesterone and the consequent fall in allopregnanolone, which destabilises GABA-A receptor-mediated inhibition and lowers the threshold for trigeminal vascular activation and cortical spreading depression. CPA's progestogenic potency could theoretically buffer this hormonal instability and maintain steadier GABA-A tone. PMID 12390622 (Facchinetti et al., 2002) demonstrates that different hormone replacement regimens have meaningfully different effects on migraine course in postmenopausal women, confirming that the type and stability of progestogenic exposure matters for migraine frequency.

Despite this biological rationale, the evidence remains entirely indirect. None of the 3 available publications directly tested CPA as a migraine treatment. Furthermore, a critical safety boundary must be respected: for patients with **migraine with aura** — including brainstem aura (formerly basilar-type migraine) — combined hormonal preparations containing CPA are classified as WHO Medical Eligibility Criteria Category 4 (absolute contraindication) due to significantly elevated ischaemic stroke risk. Any future investigation must strictly exclude this patient subgroup.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [14670648](https://pubmed.ncbi.nlm.nih.gov/14670648/) | 2003 | Review | *Maturitas* | CPA activates GABA-A receptor subtypes via C21-steroid pathway, stimulates dopaminergic and opioid systems; provides mechanistic basis for CNS effects relevant to migraine |
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Observational/Clinical | *Headache* | Three HRT schemes produce significantly different migraine outcomes in postmenopausal women, establishing that progestogen type and dose affects migraine course |
| [10857213](https://pubmed.ncbi.nlm.nih.gov/10857213/) | 2000 | Retrospective (Adverse Effects) | *Zentralblatt für Gynäkologie* | Long-term safety analysis of CPA-containing therapy in 2,506 patients (7,971 patient-years); no migraine efficacy data — included as background safety context only |

---

## Singapore Market Information

Cyproterone acetate is **not registered with the Health Sciences Authority (HSA) of Singapore** and holds no product licences. There are no authorisation numbers, approved dosage forms, or official approved indications to record. The drug is authorised in multiple other jurisdictions — notably the EU (Diane-35 for hyperandrogenism; Androcur for prostate cancer suppression) — but currently has no regulatory pathway in Singapore.

---

## All Predicted Indications at a Glance

This is a multi-indication evidence pack. The following table summarises all 10 TxGNN predictions for cyproterone acetate:

| Rank | Indication | Score | Evidence | Trials | Publications | Decision |
|------|-----------|-------|----------|--------|-------------|---------|
| 1 | Migraine Disorder | 99.66% | L4 | 0 | 3 | Hold — Research Question |
| 2 | Migraine with Brainstem Aura | 99.58% | L5 | 0 | 2 | ⛔ **Safety Alert** — Absolute contraindication for hormonal contraceptives; stroke risk |
| 3 | Prinzmetal Angina | 99.52% | L5 | 0 | 0 | Hold — No evidence, tenuous mechanistic link |
| 4 | Antithrombin Deficiency Type 2 | 99.48% | L5 | 0 | 0 | ⛔ **Safety Alert** — CPA raises VTE risk; lethal in AT-deficient patients |
| 5 | Heparin Cofactor 2 Deficiency | 99.45% | L5 | 0 | 0 | ⛔ **Safety Alert** — CPA procoagulant effects directly contraindicated |
| 6 | Factor V Excess with Spontaneous Thrombosis | 99.45% | L5 | 0 | 0 | ⛔ **Safety Alert** — CPA + Factor V interaction multiplies VTE risk |
| 7 | Migraine with/without Aura (susceptibility) | 99.34% | L4 | 0 | 20* | Hold — Most literature is epilepsy-focused, not migraine |
| **8** | **Amenorrhea / PCOS-related Menstrual Disorders** | **99.28%** | **L3** | **4** | **14** | ✅ **Proceed with Guardrails** |
| 9 | Breast Fibrocystic Disease | 99.15% | L4 | 0 | 4 | Hold — Research Question; antiandrogenic mechanism plausible |
| 10 | Thrombophilia | 99.03% | L5 | 0 | 18 | ⛔ **Model False Positive** — All 18 papers document CPA *causing* thrombosis |

> \* Rank 7 literature (20 publications) is overwhelmingly epilepsy-focused; only PMID 33856647 directly addresses migraine-epilepsy shared mechanisms.

**Critical Interpretation Note:** Ranks 2, 4, 5, 6, and 10 are not repurposing opportunities — they are pharmacological contraindications. Rank 10 (thrombophilia) is a likely TxGNN graph false positive: the model appears to have learned drug-disease co-occurrence from pharmacovigilance reports documenting CPA *as a cause* of thrombosis, misidentifying this signal as a potential therapeutic relationship.

---

## Safety Considerations

Formal package insert data (warnings, contraindications) is unavailable for Singapore as this drug holds no HSA registration. Based on the pharmacovigilance literature retrieved in this evidence pack, the following safety signals are directly evidenced:

- **Venous Thromboembolism Risk**: CPA-containing oral contraceptives reduce Protein S levels (24–38%), increase endogenous thrombin potential, and activate the coagulation cascade (PMID 15550051, 18064335, 18067603). In women carrying Factor V Leiden, the interaction with CPA multiplies VTE risk substantially (PMID 29614525, 32342502).
- **Cerebral Venous Sinus Thrombosis**: Case reports associate CPA-containing contraceptives with CVST in women of childbearing age (PMID 40704263).
- **Stroke Risk in Migraine with Aura**: Combined hormonal preparations are WHO MEC Category 4 for any migraine with aura. Literature (PMID 25227335, 30389542) confirms this prohibition applies to CPA-containing products.
- **Thrombophilia Interaction**: Patients with inherited thrombophilia (Factor V Leiden, Protein C deficiency, antithrombin deficiency) face significantly amplified VTE risk with CPA use (PMID 36634704, 19340712).

For complete safety information including hepatotoxicity, meningioma risk with prolonged high-dose use, and considerations in gender-affirming therapy, refer to the EMA-approved Diane-35 and Androcur Summary of Product Characteristics.

---

## Conclusion and Next Steps

**Decision: Hold** *(for Migraine Disorder — the top TxGNN prediction)*

**Rationale:**
The mechanistic hypothesis connecting CPA to migraine via the progesterone–allopregnanolone–GABA-A pathway is biologically coherent, but entirely speculative at this stage. With zero clinical trials and only 3 indirect publications, there is insufficient evidence to justify clinical development investment. Patient safety concerns — particularly the stroke contraindication in migraine with aura — further limit the eligible population and raise the bar for investigation.

---

**Priority Redirection — Amenorrhea/PCOS (Rank 8): Proceed with Guardrails**

The most actionable finding in this pack is not the top TxGNN prediction but **Rank 8 (amenorrhea/PCOS-related menstrual disorders)**, which has genuine clinical traction:
- CPA+EE (Diane-35/Dianette) has EU regulatory approval for hyperandrogenism-related menstrual irregularity
- 4 clinical trials (including NCT01103518 — Phase IV, direct EE+CPA comparison) and 14 publications support this use
- This represents a credible **HSA registration opportunity** for an indication with established international precedent

---

**To proceed with the Migraine Disorder research question, the following is needed:**

- Retrieve CPA mechanism of action data from DrugBank API (addresses Data Gap DG002)
- Obtain EMA package insert warnings and contraindications (addresses Data Gap DG001) and map to Singapore clinical context
- Commission a focused preclinical study examining CPA's effect on cortical spreading depression threshold in migraine animal models
- Define strict patient eligibility criteria: exclude migraine with aura, active thrombophilia, smoking, cardiovascular risk factors
- Evaluate progestogen-only CPA formulations (without oestrogen component) to separate efficacy signal from known EE-related VTE risk

**To expedite the Amenorrhea/PCOS evaluation (Rank 8):**

- Obtain and review the EMA benefit-risk assessment basis for Diane-35 PCOS indication
- Map existing EU clinical trial data (NCT01103518, NCT04831151, NCT02744131) to HSA new drug application requirements
- Develop a VTE risk management plan as a condition of any regulatory submission, given the drug's established procoagulant profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

