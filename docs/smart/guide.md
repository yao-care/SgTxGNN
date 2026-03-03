---
layout: default
title: SMART App Guide
parent: SMART on FHIR
nav_order: 1
description: "How to use the SgTxGNN SMART app"
permalink: /smart/guide/
---

# SMART App User Guide

## For Clinicians

### Launching the App

1. Open a patient's chart in your EHR
2. Navigate to the "Apps" or "SMART Apps" section
3. Select "SgTxGNN Drug Repurposing"
4. The app will load with the patient's medications

### Understanding the Display

The app shows:

- **Patient medications** - Current prescriptions from the EHR
- **Repurposing insights** - AI predictions for potential new uses
- **Confidence indicators** - KG+DL means higher confidence

### Interpreting Results

| Badge | Meaning |
|-------|---------|
| **KG+DL** | Validated by both knowledge graph and deep learning |
| **High Score** | Deep learning confidence > 99% |
| **L1-L2** | Strong clinical evidence available |

### Important Notes

- Predictions are for **research purposes only**
- Always verify with current literature
- Discuss with colleagues before clinical application
- Report any issues via the feedback button

---

## For Developers

### Testing the App

Use the SMART App Launcher for testing:

1. Go to [launch.smarthealthit.org](https://launch.smarthealthit.org/)
2. Enter Launch URL: `https://sgtxgnn.yao.care/smart/launch.html`
3. Select a test patient
4. Click "Launch"

### Debugging

Open browser developer tools to see:
- FHIR requests and responses
- Authentication flow
- Any error messages

### Customization

The app can be customized for your institution:
- Branding and colors
- Additional data sources
- Custom filtering rules

Contact us for customization options.
