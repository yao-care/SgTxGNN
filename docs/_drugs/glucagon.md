---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
---

# Glucagon
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

# Glucagon: From Severe Hypoglycemia to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon is a peptide hormone derived from the proglucagon gene, used as an emergency treatment for severe hypoglycemia, with no current registration in Singapore.
The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, supported by **2 directly relevant clinical trials** (including a completed Phase 1/2 trial with GLP-1 analog ROSE-010 in IBS-C patients) and **20 publications** — though the evidence body largely reflects GLP-1 receptor agonists rather than glucagon itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe hypoglycemia (emergency rescue use; no Singapore registration on record) |
| Predicted New Indication | Irritable Bowel Syndrome (IBS) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known information, Glucagon is a 29-amino acid peptide hormone encoded by the proglucagon gene — the same gene that encodes GLP-1 (glucagon-like peptide-1) and GLP-2. Glucagon is secreted by pancreatic alpha cells and is classically used to reverse severe hypoglycemia by stimulating hepatic glycogenolysis. Critically, glucagon receptors (GCGR) are also expressed on gastrointestinal smooth muscle, where glucagon produces a well-documented relaxant effect — a property already exploited clinically to reduce bowel motility before GI imaging procedures (e.g., colonoscopy premedication).

The mechanistic bridge to IBS lies within the proglucagon family. GLP-1, co-derived from the same precursor gene and secreted by intestinal L-cells in response to nutrients, binds GLP-1 receptors on enteric neurons and GI smooth muscle to inhibit the migrating motor complex, slow gastric emptying, and attenuate visceral pain hypersensitivity — all pathways directly implicated in IBS pathophysiology. A 2025 systematic review (PMID 40134805) confirmed that GLP-1 receptor agonists significantly improve IBS symptoms, while a 2017 clinical study (PMID 28215540) demonstrated that IBS-C patients have reduced circulating GLP-1 levels correlated with greater abdominal pain severity and confirmed GLP-1 receptor expression in the colon.

The highest-quality proof-of-concept comes from ROSE-010, a synthetic GLP-1 analog specifically evaluated in IBS-C (NCT01056107, Phase 1/2, n=52, completed), which demonstrated delayed gastric emptying and reduction in acute IBS pain attacks. While all existing clinical evidence targets GLP-1 analogs rather than native glucagon, the shared proglucagon ancestry and glucagon's established gastrointestinal smooth muscle relaxation activity provide a credible mechanistic rationale for further investigation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | GLP-1 receptor agonist ROSE-010 in female IBS-C patients: delayed gastric emptying of solids and enhanced gastric accommodation without retarding colonic transit. Provides the strongest proof-of-concept for proglucagon-family peptides in IBS. |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Mechanistic comparison of native GLP-1 vs. ROSE-010 on prandial motility of the stomach, duodenum, and jejunum in humans; confirmed GLP-1's inhibitory effect on upper GI motility via in vivo and in vitro muscle strip studies. |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | NA | Completed | 66 | Moderate vs. high-intensity exercise on gut dysbiosis and GLP-1 hormone in obese pre-diabetic IBS patients; GLP-1 measured as a key biomarker outcome. |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | NA | Completed | 37 | Colon-specific butyrate delivery in IBS patients; GLP-1 pathway implicated in mucosal disease resistance and colon health. |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | NA | Completed | 12 | FOS supplementation in idiopathic reactive hypoglycemia; glucagon measured as a metabolic counter-regulatory biomarker. |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | NA | Completed | 33 | Gut microbiota-targeted nutritional intervention during hypobaric hypoxia; GLP-1 measured as a secondary metabolic index alongside gut permeability markers. |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide (GLP-1 RA) in IPAA patients with chronic high bowel frequency; terminated early due to low enrollment, limiting conclusions. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review | Frontiers in Endocrinology | GLP-1 receptor agonists significantly improve IBS symptoms; GLP-1 and ROSE-010 inhibit the migrating motor complex and reduce GI motility, providing meta-analytic support for the GLP-1/proglucagon pathway in IBS. |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT Secondary Analysis | Scandinavian Journal of Gastroenterology | Cross-analysis of ROSE-010 RCT data identified patient subpopulations most responsive to GLP-1 RA treatment; demonstrated significant pain intensity reduction during IBS attacks. |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical Study | Neurogastroenterology & Motility | GLP-1 RA exendin-4 ameliorated GI dysfunction in Wistar Kyoto rat IBS model; implicates myenteric neuron activation in GLP-1's inhibitory effect on GI motility. |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Comprehensive review of GLP-1's role in IBS pathophysiology via L-cell secretion, gut permeability regulation, bile acid metabolism, and extrinsic/intrinsic gut neuron sensitization. |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Clinical Observational | Clinics and Research in Hepatology | Serum GLP-1 levels significantly decreased in IBS-C patients and inversely correlated with abdominal pain severity; GLP-1 receptor expression confirmed in colonic tissue. |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Clinical Study | Frontiers in Nutrition | Low FODMAP diet significantly increased circulating GLP-1 in IBS patients, suggesting GLP-1 upregulation as a shared mechanism underlying symptom improvement. |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Real-world Cohort | Annals of Gastroenterology | GLP-1 RA prescription and discontinuation patterns in IBS patients; real-world evidence on the incidence of GI adverse events in functional GI disorders. |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Experimental/Pilot | Advances in Experimental Medicine and Biology | Explored aerosolized GLP-1 as a non-invasive administration route for both diabetes mellitus and IBS; proposed inhaled delivery to bypass subcutaneous injection inconvenience. |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Review | Therapeutic Advances in Gastroenterology | Review of emerging IBS treatments; identified proglucagon-derived peptides as a promising emerging class, alongside 5-HT agents and antidepressants. |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opinion on Investigational Drugs | Novel investigational drugs for IBS-C including GLP-1 pathway agents; discusses pharmacokinetic profiling and safety considerations for new therapeutic candidates. |

---

## Singapore Market Information

Glucagon (DB00040) is currently **not registered or marketed in Singapore**. No product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings and contraindications data for this compound were not available in the current dataset (Data Gap DG001). Safety information should be obtained by downloading and parsing the Glucagon package insert from the relevant regulatory authority prior to any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A 2025 systematic review (PMID 40134805) and multiple supporting clinical and preclinical studies establish a credible evidence base for GLP-1 receptor agonists in IBS, and glucagon's well-documented GI smooth muscle relaxant effect — via GCGR expressed in intestinal smooth muscle — offers a biologically plausible direct mechanism distinct from, but complementary to, the GLP-1 pathway. However, all clinical evidence to date targets GLP-1 analogs (particularly ROSE-010) rather than native glucagon, the drug is not registered in Singapore, and essential safety data are absent from the current evidence pack.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Obtain and parse the Glucagon package insert from the relevant regulatory authority for key warnings, contraindications, and special population guidance (remediation for DG001)
- **Mechanism of action data (High priority):** Query DrugBank API for complete MOA, receptor binding profile, and pharmacodynamic data (remediation for DG002)
- **Formulation feasibility assessment:** Glucagon's very short plasma half-life (~3–6 minutes) and current parenteral-only administration are significant barriers to chronic IBS therapy; evaluate whether modified-release or alternative delivery formulations are viable
- **Translational study:** Commission a direct head-to-head study comparing native glucagon vs. GLP-1 RA efficacy in validated IBS animal models (e.g., Wistar Kyoto rat) to establish whether glucagon replicates GLP-1 RA effects
- **Regulatory pathway planning:** Since glucagon is unregistered in Singapore, a full regulatory strategy (new IND filing, clinical development plan) would be required before any clinical use in this new indication
- **Targeted clinical hypothesis:** Focus the IBS subtype most likely to benefit (IBS-C with visceral hypersensitivity) based on the mechanistic profile before broader IBS exploration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

