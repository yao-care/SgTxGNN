---
layout: default
title: Aprotinin
parent: Low Evidence (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Aprotinin
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

# Aprotinin: From Perioperative Bleeding Reduction in Cardiac Surgery to Primary Release Disorder of Platelets

## One-Sentence Summary

Aprotinin is a serine protease inhibitor and antifibrinolytic, originally used to reduce perioperative bleeding in cardiac surgery.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no aprotinin-specific clinical trials or publications** support this yet.
Only 2 indirect trials of other drugs in a similar surgical setting were retrieved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reduction of perioperative bleeding in cardiac surgery (taken from the evidence pack's rationale; the Singapore registration records contain no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 92.71% |
| Evidence Level | L4 (indirect context only; no aprotinin-specific study) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank record. Based on known information, aprotinin is a serine protease inhibitor that inhibits fibrinolysis, and its bleeding-reduction effect in cardiac surgery is the basis of its original use.

Primary release disorder of platelets is an acquired or inherited platelet function problem that leads to bleeding. A comparable clinical scenario is patients undergoing coronary artery bypass grafting (CABG) after recent clopidogrel exposure, whose platelets are pharmacologically inhibited and who bleed more. An antifibrinolytic could plausibly help reduce bleeding in that setting. This is the mechanistic link behind the prediction.

The link is still hypothetical. The two trials retrieved are in this surgical setting, but neither is shown to test aprotinin. The prediction score comes from knowledge-graph proximity, not from direct evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01596738](https://clinicaltrials.gov/study/NCT01596738) | Not applicable | Completed | 120 | Tranexamic acid (a different antifibrinolytic) in on-pump CABG patients with premature clopidogrel cessation. It aimed to reduce postoperative bleeding and transfusion. No aprotinin arm, so it gives only class-level indirect context. |
| [NCT00724880](https://clinicaltrials.gov/study/NCT00724880) | Phase 4 | Completed | 135 | Randomized study of how clopidogrel affects postoperative bleeding in CABG, and how long before surgery it should be stopped. The clinical scenario matches, but the title does not indicate an aprotinin intervention. |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN07805P | TRASYLOL INJECTION 500,000 kiu/50 ml | Injection | Bayer Pharma AG |
| SIN14719P | ARTISS Solutions for Sealant, Deep Frozen | Solution | Takeda Manufacturing Austria AG |
| SIN14707P | TISSEEL Fibrin Sealant VH S/D (Frozen) | Solution | Takeda Manufacturing Austria AG |

Approved indication text is not provided in these registration records.

---

## Safety Considerations

Please refer to the package insert for safety information.

The evidence pack notes that aprotinin's marketing history includes safety restrictions (renal and mortality signals). Any exploration of a new use should begin with a safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is a prediction only. There are no aprotinin-specific trials or publications for this indication, and the two retrieved trials do not test aprotinin. Aprotinin's history of renal and mortality safety signals, together with the missing package insert data, means the case is not ready to advance.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Aprotinin-specific clinical or observational evidence in platelet function disorders or clopidogrel-related surgical bleeding
- A formal safety review covering renal and mortality signals
- Route compatibility assessment (the injectable form is registered in Singapore; the other two registrations are sealant solutions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

