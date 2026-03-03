---
layout: default
title: SMART on FHIR
nav_order: 9
has_children: true
description: "SgTxGNN SMART on FHIR integration for EHR systems"
permalink: /smart/
---

# SMART on FHIR Integration
{: .fs-9 }

Integrate drug repurposing insights into your EHR
{: .fs-6 .fw-300 }

---

## Overview

SgTxGNN provides SMART on FHIR applications that can be integrated into Electronic Health Record (EHR) systems. When a clinician views a patient's medications, the app displays potential repurposing insights based on TxGNN predictions.

---

## Available Apps

### Patient Medication Insights

Shows drug repurposing predictions for a patient's current medications.

- **Launch URL**: `https://sgtxgnn.yao.care/smart/launch.html`
- **App URL**: `https://sgtxgnn.yao.care/smart/app.html`
- **Scopes Required**: `launch patient/MedicationRequest.read patient/Patient.read`

---

## Integration Guide

### For EHR Administrators

1. **Register the App**
   - Client ID: `sgtxgnn-smart-app`
   - Redirect URI: `https://sgtxgnn.yao.care/smart/app.html`
   - Launch URI: `https://sgtxgnn.yao.care/smart/launch.html`

2. **Configure Scopes**
   ```
   launch
   patient/MedicationRequest.read
   patient/MedicationStatement.read
   patient/Patient.read
   patient/Condition.read
   ```

3. **Test with SMART Launcher**
   - Use [SMART App Launcher](https://launch.smarthealthit.org/) for testing
   - Select "Launch as Patient Standalone" or "Launch from EHR"

---

## FHIR API

### Capability Statement

```
GET https://sgtxgnn.yao.care/fhir/metadata
```

### Available Resources

| Resource | Description |
|----------|-------------|
| MedicationKnowledge | Drug information with repurposing metadata |
| ClinicalUseDefinition | Drug-indication predictions |

### Example Queries

```bash
# Get drug information
curl https://sgtxgnn.yao.care/fhir/MedicationKnowledge/db00945

# Get predictions for a drug
curl https://sgtxgnn.yao.care/fhir/ClinicalUseDefinition?subject=MedicationKnowledge/db00945
```

---

## Security

- All connections use HTTPS
- OAuth 2.0 with PKCE for authentication
- No patient data is stored by SgTxGNN
- Read-only access to patient medications

---

## Screenshots

*Coming soon*

---

## Support

For integration support, please contact us through [GitHub Issues](https://github.com/yao-care/SgTxGNN/issues).

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
SMART apps provide research information only and do not constitute clinical decision support. All treatment decisions should be made by qualified healthcare professionals.
</div>
