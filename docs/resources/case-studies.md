---
layout: default
title: Research Cases
parent: Resources
nav_order: 3
description: "Example analyses and research tutorials"
permalink: /resources/case-studies/
---

# Research Cases

Example analyses demonstrating how to use SgTxGNN data for drug repurposing research.

---

## Case Study 1: Metformin Beyond Diabetes

### Background

Metformin is a first-line treatment for type 2 diabetes. SgTxGNN predictions suggest potential applications beyond glucose control.

### SgTxGNN Predictions

| Predicted Indication | Score | Source |
|---------------------|-------|--------|
| Polycystic ovary syndrome | 0.95 | KG+DL |
| Colorectal cancer prevention | 0.89 | DL |
| Anti-aging | 0.76 | DL |

### Evidence Review

**Polycystic Ovary Syndrome (PCOS)**
- Clinical trials: Multiple RCTs support metformin for PCOS
- Mechanism: Improves insulin sensitivity, reduces androgens
- Status: Already used off-label in many countries

**Cancer Prevention**
- Observational studies show reduced cancer risk in diabetic patients on metformin
- Mechanism: AMPK activation, mTOR inhibition
- Status: Active clinical trials ongoing

### Conclusion

This case demonstrates how TxGNN predictions align with emerging clinical evidence. Metformin's pleiotropic effects make it a strong repurposing candidate.

---

## Case Study 2: Aspirin for Neurodegenerative Disease

### Background

Aspirin is widely used for cardiovascular prevention. SgTxGNN suggests potential neurological applications.

### SgTxGNN Predictions

| Predicted Indication | Score | Source |
|---------------------|-------|--------|
| Alzheimer's disease | 0.82 | KG |
| Parkinson's disease | 0.71 | DL |

### Evidence Review

**Alzheimer's Disease**
- Mechanism: Anti-inflammatory effects, reduction of amyloid aggregation
- Clinical evidence: Mixed results in RCTs
- Current status: Not recommended for prevention

**Key Learning**

High prediction scores don't guarantee clinical efficacy. Multiple failed trials highlight the importance of rigorous validation.

### Conclusion

This case illustrates that even promising predictions require extensive validation. The gap between mechanistic plausibility and clinical benefit can be significant.

---

## Case Study 3: Statins for Infection

### Background

Statins are primarily used for cholesterol management. SgTxGNN identifies potential antimicrobial applications.

### SgTxGNN Predictions

| Predicted Indication | Score | Source |
|---------------------|-------|--------|
| Sepsis | 0.78 | KG+DL |
| Pneumonia outcomes | 0.72 | DL |

### Evidence Review

**Sepsis**
- Mechanism: Immunomodulatory effects
- Observational data: Reduced mortality in statin users
- RCT results: SAILS trial showed no benefit

**Research Implications**

1. Observational benefits may not translate to RCT success
2. Patient selection may be critical
3. Timing of initiation matters

### Conclusion

Demonstrates the complexity of translating predictions to clinical practice. Context and patient selection are crucial.

---

## Tutorial: Analysing a Drug

### Step 1: Find the Drug

```python
import pandas as pd

# Load predictions
predictions = pd.read_csv('unified_predictions.csv')

# Filter for drug of interest
drug_preds = predictions[predictions['drug_name'] == 'Aspirin']
print(f"Found {len(drug_preds)} predictions for Aspirin")
```

### Step 2: Review Predictions

```python
# Sort by confidence
drug_preds = drug_preds.sort_values('score', ascending=False)

# Show top predictions
print(drug_preds[['disease_name', 'score', 'source']].head(10))
```

### Step 3: Prioritise for Investigation

Focus on predictions that are:
- **High confidence**: Score > 0.9
- **Dual validated**: Source = KG+DL
- **Clinically plausible**: Has mechanistic rationale

### Step 4: Gather Evidence

For each high-priority prediction:
1. Search ClinicalTrials.gov for existing trials
2. Review PubMed for mechanistic literature
3. Check for safety concerns

---

## Best Practices

### For Researchers

1. **Start with high-confidence predictions**
2. **Verify mechanistic plausibility**
3. **Check for existing clinical evidence**
4. **Consider safety profile for new indication**
5. **Document your analysis process**

### For Clinicians

1. **Predictions are hypotheses, not recommendations**
2. **Always verify with current literature**
3. **Consider patient-specific factors**
4. **Follow established clinical guidelines**

---

## Submit Your Case Study

Have an interesting analysis to share?

1. Document your methodology
2. Include reproducible code
3. Submit via [GitHub Issues](https://github.com/yao-care/SgTxGNN/issues)

Selected case studies may be featured on this page.

---

<div class="disclaimer">
<strong>Educational Purpose</strong><br>
These case studies are for educational purposes only and do not constitute medical advice or treatment recommendations.
</div>
