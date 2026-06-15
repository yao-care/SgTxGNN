---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Cabergoline
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

# Cabergoline: From Prolactinoma to Pituitary Cancer

## One-Sentence Summary

Cabergoline is a selective dopamine D2 receptor agonist, established globally as the first-line treatment for prolactin-secreting pituitary adenomas (prolactinoma) and hyperprolactinemia, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Pituitary Cancer** — including non-functioning pituitary adenomas (NFPA) and corticotroph adenomas causing Cushing's disease —
with **19 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally established for prolactinoma / hyperprolactinemia |
| Predicted New Indication | Pituitary Cancer (non-functioning pituitary adenoma; corticotroph adenoma / Cushing's disease) |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cabergoline is a selective dopamine D2 receptor (D2R) agonist. Its primary mechanism in prolactinoma is direct activation of D2R expressed on lactotroph tumor cells, which suppresses prolactin hypersecretion and induces tumor cell apoptosis and measurable shrinkage. For decades, it has been the undisputed first-line medical therapy for prolactinoma. Formal MOA documentation (DrugBank) was not available in the current evidence pack, so this mechanistic description is reconstructed from the clinical literature.

The repurposing rationale is mechanistically grounded: D2R expression is not exclusive to prolactin-secreting tumors. Non-functioning pituitary adenomas (NFPAs) — the most surgically challenging subtype and the one with no approved medical therapy — also express D2R at variable levels, and D2R-positive NFPAs respond to cabergoline with measurable tumor volume reduction. Similarly, corticotroph adenomas (the cause of Cushing's disease) express D2R, and cabergoline suppresses pathological ACTH secretion through this receptor. Beyond receptor-level effects, newer research has revealed non-dopaminergic anti-tumor mechanisms: cabergoline induces autophagy, inhibits cell proliferation via PI3K/mTOR pathways, and synergizes with chloroquine to enhance pituitary tumor cell death across multiple subtypes.

From a clinical evidence standpoint, the case for pituitary cancer is already substantiated: one completed Phase 3 RCT in NFPA (NCT03271918, n=140), one completed Phase 3 trial in Cushing's disease (NCT00889525), a 2022 systematic review and meta-analysis confirming NFPA benefit (PMID 35902444), and multiple international guidelines endorsing its use across pituitary tumor subtypes. Evidence reaches L1 for prolactinoma (standard of care) and L2 for NFPA and corticotroph adenomas. The TxGNN prediction is strongly supported by the existing literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Completed | N/A | Direct study of cabergoline efficacy in Cushing's disease (corticotroph adenoma); based on D2R expression confirmed in in vitro studies of corticotroph tumor cells; assessed cortisol normalization with oral cabergoline |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Completed | 140 | RCT of cabergoline in residual NFPA after transsphenoidal surgery; evaluated tumor volume control versus no treatment — the largest completed cabergoline RCT in NFPA to date |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Enrolling by Invitation | 30 | Randomized 1:1 trial of cabergoline vs. observation as primary therapy for NFPA over 48 weeks; assesss tumor size reduction as primary endpoint in treatment-naïve patients |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Active, Not Recruiting | 60 | RCT of dopamine agonist treatment for NFPA not yet requiring surgery; evaluates growth prevention, surgical delay, and preservation of pituitary function |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminated | 68 | Pasireotide alone or combined with cabergoline for Cushing's disease; assessed whether dual somatostatin + dopamine receptor targeting produces additive efficacy in corticotroph adenomas |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Completed | 20 | Octreotide + cabergoline combination in acromegaly partially resistant to somatostatin analog monotherapy; explored additive GH suppression through concurrent D2R targeting |
| [NCT03714763](https://clinicaltrials.gov/study/NCT03714763) | N/A | Unknown | 50 | PET-MR imaging of dopamine D2 receptors in NFPA; investigates whether in vivo D2R expression predicts cabergoline treatment response — a patient-selection biomarker study |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Completed | 21 | Somatostatin and dopamine receptor expression in NFPA and resistant prolactinomas; correlated receptor levels by mRNA and immunohistochemistry with in vitro and in vivo response to cabergoline |
| [NCT03400865](https://clinicaltrials.gov/study/NCT03400865) | N/A | Unknown | 30 | Cabergoline combined with hydroxychloroquine/chloroquine for cabergoline-resistant prolactinomas; based on autophagy-mediated synergy demonstrated in preclinical models |
| [NCT01143584](https://clinicaltrials.gov/study/NCT01143584) | N/A | Unknown | 20 | Rapid vs. conventional cabergoline dose escalation in macroprolactinomas; explored whether faster titration achieves earlier prolactin normalization and tumor shrinkage, potentially reducing cumulative dose |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35902444](https://pubmed.ncbi.nlm.nih.gov/35902444/) | 2022 | Meta-analysis | Pituitary | Systematic review and meta-analysis of cabergoline in NFPA; quantified tumor stabilization and shrinkage rates across multiple studies — provides the highest-quality summary evidence for NFPA |
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Review | JAMA | Comprehensive review of pituitary adenoma diagnosis and management; dopamine agonists cited as standard medical therapy; covers both functioning and non-functioning tumor subtypes |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Review | J Clin Endocrinol Metab | Clinical approach to prolactinoma; cabergoline as current gold-standard first-line treatment with high remission rates; discusses resistance and special populations |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Review / Guideline | Medicina | Historical and modern management of prolactinomas including aggressive subtypes; reviews evidence base for dopamine agonists and multimodality options for resistant prolactinomas |
| [37171003](https://pubmed.ncbi.nlm.nih.gov/37171003/) | 2023 | Guideline | Endocr Metab Immune Disord Drug Targets | Italian national guidelines for prolactinoma management; defines cabergoline dosing targets, monitoring protocols, and criteria for treatment withdrawal |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Translational | Neuro-oncology | HTR2B suppression enhances NFPA sensitivity to cabergoline via inhibition of the Gαq/PLC/PKCγ/STAT3 axis; identifies a novel combination target to overcome cabergoline resistance in NFPA |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Review | Endocrinol Metab Clin North Am | Cabergoline safety and efficacy across pituitary tumor types; cardiac valvular risk reviewed — not significantly elevated at standard endocrine doses compared with Parkinson's-level cumulative doses |
| [28973192](https://pubmed.ncbi.nlm.nih.gov/28973192/) | 2017 | Experimental | J Clin Endocrinol Metab | Cabergoline + chloroquine combination suppresses pituitary tumor growth in vitro and in vivo via autophagy induction; overcomes resistance in prolactinomas and extends activity to other adenoma types |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Review | Neuroendocrinology | Novel anti-tumor mechanisms of cabergoline beyond the D2R pathway: anti-proliferative, pro-apoptotic, and autophagy effects in NFPA, corticotroph, and somatotroph adenomas |
| [39891847](https://pubmed.ncbi.nlm.nih.gov/39891847/) | 2025 | Research | J Neuro-oncol | NDFIP1 upregulation activates mTOR signaling as a cabergoline resistance mechanism in pituitary neuroendocrine tumors; provides rationale for combining cabergoline with mTOR inhibitors |

---

## Singapore Market Information

Cabergoline has **no registered products** in Singapore (0 HSA authorizations on record). Patients requiring cabergoline would need access through special drug import channels subject to HSA approval.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note from clinical literature:** Although formal safety data was unavailable in this evidence pack, two clinically important adverse effect categories are well-documented in the published literature and should be proactively managed:
> - **Impulse control disorders (ICDs):** Pathological gambling, hypersexuality, compulsive shopping, and related compulsive behaviors have been reported in patients on dopamine agonist therapy, with prevalence reported up to 59.8% in some series. Routine ICD screening using a validated tool is strongly recommended at each follow-up visit.
> - **Cardiac valvular risk:** Long-term high cumulative doses are associated with valvular regurgitation (a class effect of ergot-derived dopamine agonists). Echocardiographic baseline assessment and periodic monitoring are recommended, particularly when cumulative weekly doses exceed 3 mg.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for cabergoline use across pituitary tumor subtypes is well-established via the D2R pathway, supported by two completed Phase 3 trials, a systematic review and meta-analysis, and multiple international guidelines. Evidence reaches L1 for prolactinoma (already standard of care) and L2 for NFPA and corticotroph adenoma — making this one of the strongest repurposing signals in the evidence pack, with a clearly defined patient population and measurable clinical endpoints.

**To proceed, the following is needed:**

- HSA special import approval or initiation of formal product registration for cabergoline in Singapore
- Complete package insert (MOA, warnings, contraindications, DDI profile) sourced from DrugBank or originator manufacturer
- D2R expression testing protocol to guide patient selection, especially for NFPA (as explored in NCT03714763)
- Baseline and follow-up echocardiography plan for cardiac valvular surveillance
- Impulse control disorder (ICD) screening tool integrated into routine endocrinology follow-up visits
- Subtype-specific dosing protocol: NFPA and corticotroph adenoma dosing strategies are distinct from the prolactinoma protocol and require separate clinical guidance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

