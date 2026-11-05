---
layout: default
title: HL7 PDDI-CDS IG
parent: SMART on FHIR
nav_order: 10
description: "HL7 Potential Drug-Drug Interaction CDS Implementation Guide"
permalink: /smart/pddi-cds/
---

# HL7 PDDI-CDS IG Technical Notes

Implementation notes for the HL7 Potential Drug-Drug Interaction Clinical Decision Support Implementation Guide.

---

## Overview

The **PDDI-CDS IG** (Potential Drug-Drug Interaction Clinical Decision Support Implementation Guide) provides a standardised approach for implementing DDI alerts in EHR systems.

---

## Key Concepts

### Interaction Severity

| Level | Description | Action |
|-------|-------------|--------|
| **Critical** | Life-threatening | Hard stop required |
| **Serious** | Significant harm possible | Warning with override |
| **Moderate** | Monitor recommended | Informational alert |
| **Minor** | Low clinical significance | Optional notification |

### Minimum Information Model

The IG defines minimum data elements:

```json
{
  "drugA": {
    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
    "code": "1191",
    "display": "aspirin"
  },
  "drugB": {
    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
    "code": "11289",
    "display": "warfarin"
  },
  "severity": "serious",
  "description": "Increased bleeding risk",
  "recommendation": "Monitor INR closely"
}
```

---

## CDS Hooks Integration

### Service Definition

```json
{
  "hook": "order-select",
  "title": "PDDI CDS Service",
  "description": "Checks for potential drug-drug interactions",
  "id": "pddi-cds-service",
  "prefetch": {
    "currentMedications": "MedicationRequest?patient={{context.patientId}}&status=active"
  }
}
```

### Request Format

```json
{
  "hookInstance": "uuid",
  "hook": "order-select",
  "context": {
    "patientId": "123",
    "draftOrders": {
      "resourceType": "Bundle",
      "entry": [
        {
          "resource": {
            "resourceType": "MedicationRequest",
            "medicationCodeableConcept": {
              "coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "1191", "display": "aspirin"}]
            }
          }
        }
      ]
    }
  },
  "prefetch": {
    "currentMedications": {
      "resourceType": "Bundle",
      "entry": [...]
    }
  }
}
```

### Response Format

```json
{
  "cards": [
    {
      "summary": "Potential interaction: Aspirin + Warfarin",
      "indicator": "warning",
      "detail": "Concurrent use increases bleeding risk",
      "source": {
        "label": "SgTxGNN DDI Database"
      },
      "suggestions": [
        {
          "label": "Monitor INR",
          "actions": []
        }
      ]
    }
  ]
}
```

---

## FHIR Resources

### DetectedIssue

For documenting identified DDIs:

```json
{
  "resourceType": "DetectedIssue",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
      "code": "DRG",
      "display": "Drug Interaction Alert"
    }]
  },
  "severity": "moderate",
  "patient": {"reference": "Patient/123"},
  "implicated": [
    {"reference": "MedicationRequest/456"},
    {"reference": "MedicationRequest/789"}
  ],
  "detail": "Aspirin may increase the anticoagulant effect of Warfarin"
}
```

---

## Implementation Considerations

### Performance

- Pre-compute common interactions
- Cache drug-drug pairs
- Use efficient lookup structures

### Alert Fatigue

Strategies to reduce alert fatigue:
1. Filter by clinical significance
2. Patient-specific filtering
3. Context-aware suppression
4. Tiered alerting

### Override Documentation

```json
{
  "resourceType": "DetectedIssue",
  "mitigation": [
    {
      "action": {
        "coding": [{
          "code": "override",
          "display": "Provider Override"
        }]
      },
      "author": {"reference": "Practitioner/abc"},
      "date": "2024-01-15"
    }
  ]
}
```

---

## SgTxGNN DDI Status

SgTxGNN does not check drug–drug interactions in the standalone page or the SMART app, and this static site has no CDS service and no interaction API. The drug reports include interaction notes built from the DDInter download files, with Guide to PHARMACOLOGY drug–target data; see [Drug-Drug Interactions]({{ '/safety/drug-interactions/' | relative_url }}).

---

## Resources

- [HL7 PDDI-CDS IG](https://www.hl7.org/fhir/us/pddi/)
- [CDS Hooks](https://cds-hooks.org/)
- [DDInter Database](http://ddinter.scbdd.com/)
