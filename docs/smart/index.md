---
layout: default
title: SMART on FHIR
nav_order: 2
has_children: true
description: "SMART on FHIR integration for SgTxGNN drug repurposing predictions"
permalink: /smart/
---

# SMART on FHIR Integration
{: .fs-9 }

Integrate drug repurposing insights into your EHR
{: .fs-6 .fw-300 }

---

## What is SMART on FHIR?

**SMART on FHIR** (Substitutable Medical Applications, Reusable Technologies on Fast Healthcare Interoperability Resources) is a healthcare standard that enables third-party applications to integrate with EHR systems securely.

SgTxGNN provides a SMART app that allows clinicians to:
- View drug repurposing predictions for patient medications
- Access evidence levels and supporting literature
- Review drug interactions and safety information

---

## Quick Links

| Resource | Description |
|----------|-------------|
| [User Guide]({{ '/smart/guide/' | relative_url }}) | Step-by-step instructions for clinicians |
| [Technical Documentation]({{ '/smart/technical/' | relative_url }}) | API specifications and implementation details |
| [Integration Resources]({{ '/smart/integration/' | relative_url }}) | Resources for EHR administrators |
| [SMART App Gallery]({{ '/smart/gallery/' | relative_url }}) | Reference apps and examples |
| [App Assessment]({{ '/smart/assessment/' | relative_url }}) | Integration evaluation criteria |
| [FHIR API Specification]({{ '/smart/fhir-api/' | relative_url }}) | FHIR R4 endpoints and resources |

---

## Launch the App

### For Testing

Use the [SMART App Launcher](https://launch.smarthealthit.org/) with:

```
Launch URL: https://sgtxgnn.yao.care/smart/launch.html
FHIR Version: R4
```

### For Production

Register with your EHR administrator using:

| Parameter | Value |
|-----------|-------|
| App Name | SgTxGNN Drug Repurposing |
| Launch URL | `https://sgtxgnn.yao.care/smart/launch.html` |
| Redirect URL | `https://sgtxgnn.yao.care/smart/app.html` |
| FHIR Version | R4 |
| Scopes | `launch patient/MedicationRequest.read patient/Patient.read patient/Condition.read` |

---

## Key Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2E7D32;">
    <strong>Patient Context</strong><br>
    <span style="color: #666;">Automatically loads patient medications from EHR</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1976D2;">
    <strong>Evidence-Based</strong><br>
    <span style="color: #666;">Shows L1-L5 evidence levels for each prediction</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #FB8C00;">
    <strong>Dual Validation</strong><br>
    <span style="color: #666;">KG+DL validated predictions highlighted</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #9B59B6;">
    <strong>Privacy First</strong><br>
    <span style="color: #666;">All processing in-browser, no data stored</span>
  </div>
</div>

---

## FHIR Resources

SgTxGNN provides FHIR R4 resources:

| Resource | Endpoint | Description |
|----------|----------|-------------|
| CapabilityStatement | `/fhir/metadata` | Server capabilities |
| MedicationKnowledge | `/fhir/MedicationKnowledge/{id}` | Drug information |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/{id}` | Repurposing predictions |

---

## Technical Notes

Explore our technical documentation:

| Topic | Description |
|-------|-------------|
| [ClinicalTrials.gov API v2]({{ '/smart/clinicaltrials-api/' | relative_url }}) | Working with clinical trials data |
| [CQL Syntax Notes]({{ '/smart/cql-notes/' | relative_url }}) | Clinical Quality Language reference |
| [HL7 PDDI-CDS IG]({{ '/smart/pddi-cds/' | relative_url }}) | Drug-Drug Interaction CDS implementation |
| [CDS Hooks Architecture]({{ '/smart/cds-hooks/' | relative_url }}) | CDS Hooks service design |

---

<div class="disclaimer">
<strong>Research Use Only</strong><br>
This SMART app provides research information only. Drug repurposing predictions have not been clinically validated and should NOT be used for treatment decisions without consultation with qualified healthcare professionals.
</div>
