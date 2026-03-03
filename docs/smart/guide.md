---
layout: default
title: User Guide
parent: SMART on FHIR
nav_order: 1
description: "User guide for SgTxGNN SMART on FHIR application"
permalink: /smart/guide/
---

# SMART App User Guide

A step-by-step guide for clinicians using the SgTxGNN SMART application.

---

## Getting Started

### Prerequisites

- Access to a SMART on FHIR enabled EHR system
- SgTxGNN app registered with your institution
- Valid user credentials for your EHR

### Launching the App

1. **From your EHR**: Look for "SgTxGNN" or "Drug Repurposing" in your app launcher
2. **Select a patient**: The app requires patient context
3. **Authorise**: Grant the app permission to read medication data
4. **View results**: See repurposing predictions for patient medications

---

## Understanding the Interface

### Patient Information Panel

Displays basic patient demographics loaded from the EHR:
- Patient name
- Date of birth
- Gender
- Patient ID

### Current Medications

Lists all active medications for the patient:
- Medication name
- Status (active, completed, etc.)
- **Has Insights** badge indicates repurposing predictions available

### Repurposing Insights

For medications with predictions:
- **Indication**: The predicted new use
- **Source**: Prediction method (KG, DL, or KG+DL)
- **Evidence Level**: L1-L5 classification

---

## Evidence Levels Explained

| Level | Meaning | Clinical Relevance |
|-------|---------|-------------------|
| **L1** | Multiple Phase 3 RCTs | Strong evidence, may support clinical use |
| **L2** | Single RCT or Phase 2 | Moderate evidence, consider with caution |
| **L3** | Observational studies | Emerging evidence, needs validation |
| **L4** | Preclinical/mechanistic | Early research stage |
| **L5** | Model prediction only | Research hypothesis |

### Special Indicators

- **KG+DL**: Prediction validated by both Knowledge Graph AND Deep Learning methods - higher confidence
- **High Score (>0.99)**: Very strong model confidence

---

## Best Practices

### Do

- Use predictions as research starting points
- Verify findings with current literature
- Discuss with colleagues and pharmacists
- Consider patient-specific factors

### Don't

- Make treatment decisions based solely on predictions
- Prescribe off-label without proper evaluation
- Ignore standard clinical guidelines
- Skip regulatory requirements

---

## Troubleshooting

### App won't launch

1. Check your network connection
2. Ensure you have a patient selected
3. Verify app is registered with your EHR
4. Contact your IT support

### No medications shown

1. Patient may have no active medications
2. Check patient has medication records in EHR
3. Verify app has permission to read MedicationRequest

### No predictions available

Not all medications have repurposing predictions. The app only shows results for:
- HSA-approved medications
- Drugs mapped to DrugBank identifiers
- Drugs included in TxGNN knowledge graph

---

## Privacy & Security

- **No data storage**: Patient data is never stored by SgTxGNN
- **In-browser processing**: All analysis happens locally
- **Encrypted connections**: HTTPS only
- **OAuth 2.0**: Industry-standard authentication

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
SgTxGNN predictions are for research purposes only and do not constitute medical advice. Always follow clinical guidelines and consult with healthcare professionals before making treatment decisions.
</div>
