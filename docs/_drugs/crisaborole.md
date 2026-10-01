---
layout: default
title: Crisaborole
parent: Medium Evidence (L3-L4)
nav_order: 277
evidence_level: L4
indication_count: 10
---

# Crisaborole
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

# Crisaborole: From Atopic Dermatitis (Topical Use) to Exanthem

## One-Sentence Summary

Crisaborole is a topical PDE4 inhibitor ointment. Its known use is atopic dermatitis, although the Singapore registration data do not list an approved indication.
The TxGNN model predicts it may be effective for **Exanthem** (a broad term for skin rash), but only **3 loosely related clinical trials** and **no publications** currently support this direction.
The link is weak, and the score is probably driven by the drug's dermatitis association.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Singapore license data. Atopic dermatitis is the known labeled use. |
| Predicted New Indication | Exanthem (disease) |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Crisaborole is a topical PDE4 inhibitor. Blocking PDE4 raises intracellular cAMP and lowers pro-inflammatory cytokines (TNF-alpha, IL-4, IL-13, IL-31). This is the established mechanism in atopic dermatitis, so a nonspecific inflammatory rash is biologically plausible.

"Exanthem" is a broad, heterogeneous label rather than one defined disease. The trials linked to it concern eczema, dermatitis, or drug-induced skin toxicity, not a defined exanthematous disease. The high TxGNN score is therefore most likely explained by the dermatitis association. It is not independent evidence for exanthem.

The candidate list also shows that the strongest signal for this drug is atopic dermatitis (L1 evidence, two completed Phase 3 vehicle-controlled RCTs). That appears to be the drug's existing indication, not a true repurposing case.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06118047](https://clinicaltrials.gov/study/NCT06118047) | Phase 2 | Unknown | 33 | Single-arm study of crisaborole ointment twice daily for cetuximab-related skin toxicity in metastatic colorectal cancer. This is the closest match to a rash, but the target condition and design need manual verification. |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Rice-grain-sized skin microdevice that releases approved drugs into atopic dermatitis and psoriasis lesions. A delivery and pharmacology study, not an efficacy trial. |
| [NCT03409367](https://clinicaltrials.gov/study/NCT03409367) | N/A | Completed | 1260 | Community-based study of daily emollient use from birth to prevent eczema. It gives no efficacy evidence for crisaborole. |

## Literature Evidence

Currently no related literature available

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16613P | Staquis Ointment 2% w/w (Pharmacia & Upjohn Company LLC, a Pfizer subsidiary) | Ointment | Not listed in the registration data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For exanthem, the evidence is model prediction plus three trials that are unverified or off-target, and no literature was retrieved. This supports L4 at most. NCT06118047 is Phase 2 but has an unknown status and an unverified target condition, so it cannot support L2. The candidate that does have strong evidence is atopic dermatitis, and it appears to be the labeled use, so it should be handled as a label and registration question, not as repurposing.

**To proceed, the following is needed:**
- Verify the target condition, design, and results of NCT06118047 (cetuximab-related skin toxicity), and decide whether that narrower indication should replace the vague "exanthem" label.
- Obtain the Singapore package insert (approved indication, age limits, warnings, contraindications), since none of this is in the registration data.
- Fill in the original indication and mechanism of action from DrugBank.
- Confirm the Singapore approval status for atopic dermatitis before treating it as a separate opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

