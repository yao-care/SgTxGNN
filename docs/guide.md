---
layout: default
title: Platform Guide
parent: Help
nav_order: 2
description: "How to read and use SgTxGNN validation reports"
permalink: /guide/
---

# User Guide
{: .fs-9 }

How to read and use validation reports
{: .fs-6 .fw-300 }

---

## Quick Start

### 1. Find a Drug of Interest

- Use the **search function** in the top right corner
- Or browse from the [Drug List](/drugs/)
- Or filter by [Evidence Level](/evidence-high/)

### 2. Check Evidence Level

Each drug has an evidence level (L1-L5):

| Level | Meaning | Confidence |
|:-----:|---------|:----------:|
| **L1** | Multiple large RCTs support | ⭐⭐⭐⭐⭐ |
| **L2** | Single RCT or multiple Phase 2 | ⭐⭐⭐⭐ |
| **L3** | Observational studies | ⭐⭐⭐ |
| **L4** | Preclinical/mechanistic studies | ⭐⭐ |
| **L5** | AI prediction only | ⭐ |

### 3. Read the Full Report

Reports contain detailed evidence analysis and recommendations.

---

## Report Structure

Each report contains the following sections:

### One-Sentence Summary

Quickly understand the core content:
- Original indication
- Predicted new indication
- How much evidence supports it

### Quick Overview Table

| Field | Description |
|-------|-------------|
| Original Indication | Drug's currently approved use |
| Predicted New Indication | TxGNN's predicted new use |
| TxGNN Prediction Score | AI confidence level (higher = more confident) |
| Evidence Level | L1-L5, see above |
| Singapore Registration | Whether registered with HSA |
| Recommendation | Go / Proceed / Consider / Explore / Hold |

### Why This Prediction Makes Sense

Explains the pharmacological mechanism:
- Drug's mechanism of action
- Why this mechanism might work for the new indication
- Relationship with original indication

### Clinical Trial Evidence

Lists relevant clinical trials:

| Field | Description |
|-------|-------------|
| Trial ID | ClinicalTrials.gov ID, clickable |
| Phase | Phase 1/2/3/4 |
| Status | Ongoing, Completed, Terminated, etc. |
| Enrollment | Number of participants |
| Key Findings | Trial results (if available) |

### Literature Evidence

Lists relevant academic literature:

| Field | Description |
|-------|-------------|
| PMID | PubMed ID, clickable |
| Year | Publication year |
| Type | Article type (journal article, review, etc.) |
| Journal | Publication journal |
| Key Findings | Main findings |

### Singapore Registration Info

Lists the drug's HSA registration:
- License number
- Product name (brand name)
- Dosage form
- Approved indications

### Safety Considerations

Highlights potential safety issues.

### Conclusion & Next Steps

Summarizes the recommendation and explains:
- Why this recommendation was made
- What's needed to proceed

---

## Decision Recommendations

| Decision | Meaning | Suggested Action |
|----------|---------|------------------|
| **Go** | Very strong evidence | Can proceed to detailed evaluation or trial planning |
| **Proceed** | Strong evidence | Worth further feasibility assessment |
| **Consider** | Some evidence | Can consider, but weigh risks |
| **Explore** | Worth exploring | Recommend gathering more data first |
| **Hold** | Insufficient evidence | Not recommended to proceed currently |

---

## Frequently Asked Questions

### Q: Can I use L1 drugs directly?

**Not necessarily.** L1 indicates strong clinical evidence supporting the prediction, but:
- Still need to confirm regulatory compliance
- Need to assess individual applicability
- Need to consider drug interactions

### Q: Are L5 drugs useless?

**Not necessarily.** L5 indicates lack of clinical evidence currently, but:
- May be an unexplored area
- AI predictions can serve as research hypothesis starting points
- Suitable for early research directions

### Q: Is a higher prediction score always better?

**Generally yes.** Prediction score reflects AI model confidence:
- Above 99.9%: Very confident
- 99.0-99.9%: Confident
- But high prediction score ≠ high clinical evidence

### Q: How often are reports updated?

Reports are currently **generated once** reflecting data at generation time. Future regular updates may be implemented.

### Q: Can this be used clinically?

**Absolutely not.** This report is for research reference only and does not constitute medical advice. Any clinical application requires:
- Complete clinical trial validation
- Regulatory approval
- Professional medical judgment

---

## Still Have Questions?

Please ask through [GitHub Issues](https://github.com/yao-care/SgTxGNN/issues).
