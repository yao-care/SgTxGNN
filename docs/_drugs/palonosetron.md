---
layout: default
title: Palonosetron
parent: Medium Evidence (L3-L4)
nav_order: 758
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Palonosetron: predicted new indication Migraine disorder (evidence level L4). Approved use: Not stated in the registration records compiled for this report (the…"
monitor_inn: "Palonosetron"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "headache disorder", "trigeminal autonomic cephalalgia", "open-angle glaucoma", "sciatic neuropathy", "primary hereditary glaucoma"]
---

# Palonosetron
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Palonosetron: From Chemotherapy-Induced Nausea and Vomiting to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Palonosetron is a 5-HT3 receptor antagonist marketed in Singapore as an antiemetic, used for the prevention of chemotherapy-induced nausea and vomiting (CINV).
The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials** and only **1 publication** (a case report describing palonosetron *causing* migraine-type headache) exist for this indication.
The prediction is therefore not supported by clinical evidence at present.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records compiled for this report (the registered products are antiemetics; CINV prevention is the known approved use) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, palonosetron is a 5-HT3 receptor antagonist. Its efficacy in preventing nausea and vomiting from chemotherapy is established, and mechanistically it may be relevant to migraine, because serotonin signalling is implicated in migraine pathophysiology and 5-HT3 antagonists have been explored in this area.

However, the evidence points the other way. The only retrieved publication for this indication (PMID 21132477) is a case report of palonosetron-**induced** migraine-type headache, which is an adverse-event signal rather than a therapeutic one. The high TxGNN score is a computational prediction, likely reflecting knowledge-graph proximity, and is not backed by clinical data.

Other top predictions (migraine with brainstem aura, trigeminal autonomic cephalalgia, headache disorder) appear to be extensions of the same graph proximity. Predictions such as atrophoderma vermiculata, ulerythema ophryogenesis, open-angle glaucoma and primary hereditary glaucoma have no identifiable mechanistic link and are likely graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case report | Can J Anaesth | Palonosetron-induced migraine-type headache; an adverse-event report, not evidence of benefit |

Related literature found for broader headache and migraine-susceptibility predictions concerns the approved antiemetic use or safety, not efficacy in migraine. Examples are CINV trials comparing palonosetron with ondansetron or oral with IV dosing (PMIDs 23354552, 26795844, 28941006), where headache appears only as a side effect. Another is a 2026 review of antiemetic-associated QT prolongation (PMID 42748473).

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16959P | PALONOSETRON-AFT Solution for Injection 0.25mg/5ml | Injection, solution | Not listed in the compiled data |
| SIN14038P | ALOXI® Solution for Injection 50mcg/ml | Injection, solution | Not listed in the compiled data |
| SIN16899P | Akynzeo® IV Concentrate for Solution for Infusion 235 mg/0.25 mg/vial | Infusion, solution concentrate | Not listed in the compiled data |
| SIN15031P | AKYNZEO Capsules 300mg/0.5mg | Capsule, gelatin coated | Not listed in the compiled data |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Examples of Major-level interactions include fentanyl, dextromethorphan, tramadol, alfentanil, almotriptan, sumatriptan, amiodarone, amisulpride, amitriptyline and anagrelide. Moderate-level examples include abiraterone, codeine, dihydrocodeine, famotidine, formoterol, adenosine, salbutamol, propofol and loperamide.
- **QT consideration**: A 2026 review identifies antiemetics as a class with QT-prolongation liability. This is relevant to any repurposing effort, especially alongside QT-prolonging co-medications such as amiodarone and amisulpride.
- **Headache**: Headache is reported as an adverse effect of palonosetron, which is directly relevant to a migraine indication.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trials exist, and the only direct literature reports palonosetron causing migraine-type headache. The evidence does not support moving forward, and the other predicted indications have even less support (L5, with no mechanistic rationale).

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) to assess the 5-HT3 link to migraine properly
- Package insert warnings and contraindications from HSA, which is a blocking gap for safety screening
- Approved indication text for the Singapore registrations
- A systematic review of 5-HT3 antagonists in migraine, plus any preclinical or early clinical data, including an assessment of headache as an adverse-event signal
- QT risk assessment and a DDI management plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

