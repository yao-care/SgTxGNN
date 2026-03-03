---
layout: default
title: "Understanding Evidence Levels"
date: 2026-03-02
categories: guide
description: "How to interpret L1-L5 evidence levels in SgTxGNN"
---

# Understanding Evidence Levels

SgTxGNN uses a five-level evidence classification system (L1-L5) to help researchers quickly assess the credibility of drug repurposing predictions.

## The Five Levels

### L1 - Multiple Phase 3 RCTs

The highest level of evidence. Predictions at this level are supported by:
- Two or more completed Phase 3 randomized controlled trials
- Consistent positive results across trials
- Large patient populations

**Recommendation**: Strong candidates for clinical evaluation

### L2 - Single RCT or Phase 2 Trials

Strong clinical evidence including:
- One completed Phase 3 RCT with positive results
- Multiple Phase 2 trials with consistent findings

**Recommendation**: Worth detailed feasibility assessment

### L3 - Observational Studies

Supported by real-world evidence:
- Cohort studies
- Case-control studies
- Registry data

**Recommendation**: Consider with additional investigation

### L4 - Preclinical/Mechanistic

Based on laboratory and mechanistic research:
- In vitro studies
- Animal models
- Pathway analysis

**Recommendation**: Explore as research hypothesis

### L5 - Prediction Only

AI prediction without clinical validation:
- TxGNN model prediction
- May be KG, DL, or KG+DL validated

**Recommendation**: Use as starting point for research

## Special Indicators

### KG+DL (Dual Validated)

Predictions that appear in both:
- Knowledge Graph analysis
- Deep Learning model

These have higher confidence due to convergent evidence from independent methods.

### High Score (>0.99)

Deep Learning predictions with confidence scores above 99% indicate very strong model certainty, though this doesn't guarantee clinical validity.

## How to Use This Information

1. **Prioritize L1-L2** for immediate clinical relevance
2. **Investigate L3-L4** for emerging opportunities
3. **Use L5 with KG+DL** as high-quality research hypotheses
4. **Always verify** with current literature and clinical judgment

---

*Remember: Evidence levels are guides, not guarantees. Clinical validation is always required.*
