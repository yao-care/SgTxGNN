---
layout: default
title: Bezafibrate
parent: Medium Evidence (L3-L4)
nav_order: 155
evidence_level: L3
indication_count: 10
---

# Bezafibrate
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Bezafibrate: From Hyperlipidemia to Hypoalphalipoproteinemia

## One-Sentence Summary

Bezafibrate is a fibrate lipid-lowering drug, marketed in Singapore as a 200 mg film-coated tablet.
The TxGNN model predicts it may help with **hypoalphalipoproteinemia** (persistently low HDL cholesterol).
No clinical trials are registered for this indication. Support comes from **3 publications**, all small or observational, and none proves benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia (established lipid-lowering use). The Singapore licence record does not state an indication. |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 98.54% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bezafibrate is a pan-PPAR (alpha/gamma/delta) agonist. Activating PPAR-alpha increases production of apolipoproteins A-I and A-II, the main protein components of HDL, and raises HDL cholesterol. It also lowers triglycerides through increased lipoprotein lipase activity and reduced apoC-III. So a link to low HDL states is biologically plausible.

Both hypoalphalipoproteinemia and the drug's established use are lipoprotein disorders. Low HDL is a recognized risk factor for coronary artery disease, and low HDL commonly accompanies raised triglycerides. Raising HDL, however, has not been shown to improve clinical outcomes in this setting.

The literature is mixed. One small study in coronary artery disease patients with isolated low HDL examined endothelial function during bezafibrate treatment. Two other papers describe *profound* HDL and apoA-I reductions when probucol was combined with a fibrate, which is a caution rather than support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11483875](https://pubmed.ncbi.nlm.nih.gov/11483875/) | 2001 | Clinical study (small) | J Cardiovasc Pharmacol | Endothelial dysfunction improved in coronary artery disease patients with isolated low HDL-C (<0.91 mM) treated with bezafibrate. The abstract is truncated, so detailed results are not visible. |
| [1575823](https://pubmed.ncbi.nlm.nih.gov/1575823/) | 1992 | Observational | Atherosclerosis | Studied how often primary hypoalphalipoproteinemia occurs in hypertriglyceridemic patients. Low HDL is often linked to disordered triglyceride metabolism. |
| [7567762](https://pubmed.ncbi.nlm.nih.gov/7567762/) | 1995 | Case report | Postgrad Med J | Two cases where probucol plus a fibrate (bezafibrate in one) caused very low HDL-C and apoA-I. This is an iatrogenic cause of low HDL. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10217P | ZAFIBRAL TABLET 200 mg (MEDOCHEMIE LTD, Central Factory) | Tablet, film coated (oral) | Not stated in the record |

---

## Safety Considerations

Please refer to the package insert for safety information. The HSA package insert warnings and contraindications were not available, and no drug interaction records were found.

Two signals from the retrieved literature and the evidence rationale:
- **Probucol combination**: Adding a fibrate such as bezafibrate to probucol can profoundly lower HDL-C and apoA-I (PMID 7567762). This works against the intended effect.
- **Statin combination**: Statin-fibrate combinations carry a myopathy risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug link is biologically plausible, but the evidence is thin: no registered trials, one small clinical study, one observational paper and one case report. HDL elevation has not been shown to improve outcomes, and the HSA safety data needed for screening are missing.

**To proceed, the following is needed:**
- HSA package insert warnings, contraindications and approved indications (safety screening is blocked without them)
- Mechanism of action data from DrugBank
- The full text of PMID 11483875 to confirm the design and results
- Any interventional trial of bezafibrate in isolated low HDL, with clinical or surrogate outcomes
- A statin/probucol co-medication risk plan and renal dose-adjustment guidance

**Note on other predictions:** *Hyperlipoproteinemia* (rank 8) has stronger support (L2, Proceed with Guardrails). It reflects the drug's established lipid-lowering use rather than a novel repurposing. *Familial hypercholesterolemia* (rank 7) is at L3, with add-on studies from the 1980s and 1990s. The remaining predictions have little or no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

