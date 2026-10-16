---
layout: default
title: Polidocanol
parent: Low Evidence (L5)
nav_order: 805
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Polidocanol: predicted new indication Esophageal varices with bleeding (evidence level L5). Approved use: Varicose disease"
---

# Polidocanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Polidocanol: From Varicose Disease to Esophageal Varices with Bleeding

## One-Sentence Summary

Polidocanol is a sclerosing agent originally used to treat varicose disease (varicose veins).
The TxGNN model predicts it may be effective for **esophageal varices with bleeding**,
with **no registered clinical trials** but **20 publications** currently supporting this direction, including several randomized trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Varicose disease (the Singapore licence record contains no approved indication text) |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 (provisional; see note below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note: The L1 grade is inferred from publication titles and abstracts. The trial phase is not stated, and the full texts should be checked before it is relied on.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, polidocanol is a sclerosing agent that damages the vascular endothelium, leading to thrombosis and fibrosis of the treated vessel.

Varicose veins and esophageal varices are both abnormally dilated veins, and closing the affected vessel is the treatment goal in each. Polidocanol is already used in endoscopic injection sclerotherapy for esophageal and gastric varices, and as foam in balloon-occluded retrograde transvenous obliteration (BRTO) for gastric varices. This shared pathophysiology supports the model's prediction.

An important caveat is that sclerotherapy is now generally second-line to endoscopic band ligation. Strictures, ulceration and rebleeding are known risks.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 10 most relevant publications are listed below, with randomized trials first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9255525](https://pubmed.ncbi.nlm.nih.gov/9255525/) | 1997 | RCT | Endoscopy | Cyanoacrylate plus polidocanol, or polidocanol alone, in emergency and long-term management of bleeding esophageal varices in cirrhosis |
| [10385713](https://pubmed.ncbi.nlm.nih.gov/10385713/) | 1999 | RCT | Gastrointestinal Endoscopy | Band ligation alone vs. ligation plus sclerotherapy for bleeding esophageal varices |
| [2693076](https://pubmed.ncbi.nlm.nih.gov/2693076/) | 1989 | Randomized trial | Endoscopy | Ethanolamine vs. polidocanol: variceal eradication 81% vs. 64% (not significant) in 50 cirrhotic patients |
| [7942715](https://pubmed.ncbi.nlm.nih.gov/7942715/) | 1994 | Meta-analysis | Am J Gastroenterol | Whether prophylactic sclerotherapy improves survival in esophageal varices |
| [32517718](https://pubmed.ncbi.nlm.nih.gov/32517718/) | 2020 | Systematic review | BMC Gastroenterology | Pooled rebleeding risk after cyanoacrylate treatment of gastroesophageal varices |
| [29473522](https://pubmed.ncbi.nlm.nih.gov/29473522/) | 2017 | Review | Curr Clin Pharmacol | Evidence-based review of off-label polidocanol uses |
| [3069543](https://pubmed.ncbi.nlm.nih.gov/3069543/) | 1988 | Comparative study | Gastroenterol Clin Biol | Intravariceal polidocanol vs. perivariceal quinine-urea in 74 patients with bleeding varices |
| [10434360](https://pubmed.ncbi.nlm.nih.gov/10434360/) | 1999 | Comparative study | J UOEH | Ligation (101 patients) vs. paravariceal polidocanol sclerotherapy (40 patients); both controlled active bleeding, with rebleeding 29.6% (ligation) vs. 40.0% (sclerotherapy) |
| [36509625](https://pubmed.ncbi.nlm.nih.gov/36509625/) | 2023 | Cohort | Arch Pediatr | Polidocanol injection sclerotherapy for cardiac varices in children and adolescents |
| [6609102](https://pubmed.ncbi.nlm.nih.gov/6609102/) | 1984 | Cohort (adverse events) | Gut | Stricture or dysphagia in 20 of 34 patients (59%) after repeated 3% polidocanol sclerotherapy |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15433P | VARITHENA Polidocanol Injectable Foam 10 mg/mL | Injection | Not stated in the available record |

## Safety Considerations

- **Adverse events in the literature**: Esophageal stricture and dysphagia occurred in 59% of patients after repeated polidocanol sclerotherapy (PMID 6609102). Ulceration and rebleeding are also recognized risks.
- **Place in therapy**: Sclerotherapy is generally second-line to band ligation, and may aggravate portal hypertension by suppressing portosystemic shunts (PMID 2344911).

For other safety information, including warnings, contraindications and drug interactions, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomized and comparative studies support polidocanol sclerotherapy for bleeding esophageal varices, and the mechanism is the same as in its established use for varicose veins. However, no registered trials exist, the studies are mostly dated, and band ligation is now preferred. The use should therefore be limited to selected patients.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing
- Mechanism of action data from DrugBank
- Full-text review of the key randomized trials to confirm design, phase and the L1 grading
- Confirmation that the Singapore-registered product (an injectable foam) and its labelled indication suit endoscopic variceal use, since the current licence record states no approved indication
- A patient-selection and safety-monitoring plan, covering strictures, ulceration and rebleeding

**Other predicted indications:**
- *Esophageal varices without bleeding* (score 99.95%): Proceed with Guardrails. A meta-analysis of prophylactic sclerotherapy exists (PMID 7942715), but it is dated and not specific to polidocanol. Beta-blockers and band ligation have largely superseded this use, so it should be limited to patients who cannot use the standard options.
- *Eight other predictions* (for example immunoerythromyeloid hypoplasia, retinal and cone disorders, and monosomy X): Hold. They rest on model prediction alone, with no trials, no literature and no plausible mechanistic link to a local sclerosant.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

