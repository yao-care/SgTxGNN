---
layout: default
title: Pyridostigmine
parent: Medium Evidence (L3-L4)
nav_order: 834
evidence_level: L4
indication_count: 10
---

# Pyridostigmine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pyridostigmine: From Myasthenia Gravis (Symptomatic Therapy) to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Pyridostigmine is a reversible acetylcholinesterase inhibitor and a standard symptomatic therapy for myasthenia gravis.
The TxGNN model predicts it may be effective for **myasthenia gravis with thymus hyperplasia**, but this is a subtype of the drug's established use rather than a true repurposing.
Support is thin: **0 clinical trials** and **3 publications**, none of which tests pyridostigmine in this subtype.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myasthenia gravis (symptomatic therapy); the Singapore licence record does not state an indication |
| Predicted New Indication | Myasthenia gravis with thymus hyperplasia |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Pyridostigmine blocks the breakdown of acetylcholine, so more of it stays available at the neuromuscular junction. In myasthenia gravis, autoantibodies reduce the receptors that respond to acetylcholine, and boosting acetylcholine partly compensates. This is why the drug is a first-line symptomatic option in the disease.

The predicted indication is a subtype of the same disease, and thymic hyperplasia is a common feature of antibody-positive myasthenia gravis. The model's high score therefore mostly reflects that closeness rather than a new therapeutic idea. The supplied literature covers thymus hyperplasia and thymectomy outcomes, not pyridostigmine efficacy in this subtype.

One caution applies: MuSK-positive disease, which lacks the typical thymic changes, often responds poorly to acetylcholinesterase inhibitors.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Review | Molecular Medicine Reports | Genomic, phenotypic and epigenetic review of myasthenia gravis pathology, autoimmunity and weight management; no pyridostigmine-specific efficacy data |
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Cohort (retrospective) | Journal of Neurology | Two-year outcomes of thymectomy in 39 patients with non-thymomatous late-onset myasthenia gravis; studies surgery, not pyridostigmine |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case report | Neuromuscular Disorders | Dropped head syndrome in MuSK-positive myasthenia gravis with thymus hyperplasia; a single patient |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02898P | MESTINON TABLET 60 mg | Tablet, sugar coated (oral) | Not listed in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction restates the drug's established use in a narrower subtype, and no trial or paper evaluates pyridostigmine for it. The package-insert safety review is also still outstanding, which blocks progression.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications, which block the safety screening
- The Singapore-approved indication wording, to confirm whether this subtype is already covered
- Subtype-specific response data, including antibody status (AChR vs MuSK), since MuSK-positive disease may respond poorly
- Detailed mechanism of action data from DrugBank

**Other predictions in this pack (brief):**
- "Autoimmune disease of peripheral nervous system" (L3) could proceed with guardrails, limited to defined neuromuscular junction conditions. Its two registered trials are observational and do not test pyridostigmine.
- "Myasthenia, congenital, refractory to acetylcholinesterase inhibitors" conflicts with the disease definition, and acetylcholinesterase inhibitors can worsen slow-channel forms, so it should be held.
- Hypersplenism, atypical hemolytic-uremic syndrome and fetal akinesia deformation sequence have no plausible mechanistic link and should be held.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

