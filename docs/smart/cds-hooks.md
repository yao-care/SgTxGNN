---
layout: default
title: CDS Hooks Architecture
parent: SMART on FHIR
nav_order: 11
description: "CDS Hooks architecture design for clinical decision support"
permalink: /smart/cds-hooks/
---

# CDS Hooks Architecture Design

Technical guide for implementing CDS Hooks services.

---

## What is CDS Hooks?

**CDS Hooks** is an HL7 specification for integrating Clinical Decision Support (CDS) services with EHR workflows. It provides:

- Standardised trigger points (hooks)
- Consistent request/response format
- EHR-agnostic architecture

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                     EHR System                          │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │ Order Entry │  │  Patient    │  │  Medication     │  │
│  │    Hook     │  │  View Hook  │  │  Prescribe Hook │  │
│  └──────┬──────┘  └──────┬──────┘  └────────┬────────┘  │
└─────────┼────────────────┼──────────────────┼───────────┘
          │                │                  │
          ▼                ▼                  ▼
┌─────────────────────────────────────────────────────────┐
│                  CDS Hooks Service                       │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │              Discovery Endpoint                  │    │
│  │              GET /cds-services                   │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │              Service Endpoints                   │    │
│  │     POST /cds-services/{service-id}              │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Standard Hooks

### patient-view

Triggered when a patient's record is opened.

```json
{
  "hook": "patient-view",
  "hookInstance": "uuid",
  "context": {
    "userId": "Practitioner/123",
    "patientId": "Patient/456"
  }
}
```

### order-select

Triggered when a clinician selects medications.

```json
{
  "hook": "order-select",
  "hookInstance": "uuid",
  "context": {
    "userId": "Practitioner/123",
    "patientId": "Patient/456",
    "selections": ["MedicationRequest/draft-123"],
    "draftOrders": {...}
  }
}
```

### order-sign

Triggered when signing orders.

```json
{
  "hook": "order-sign",
  "context": {
    "draftOrders": {...}
  }
}
```

---

## Service Discovery

### GET /cds-services

```json
{
  "services": [
    {
      "hook": "order-select",
      "title": "Drug Repurposing Insights",
      "description": "Shows potential new uses for selected medications",
      "id": "sgtxgnn-repurposing",
      "prefetch": {
        "patient": "Patient/{{context.patientId}}",
        "medications": "MedicationRequest?patient={{context.patientId}}"
      }
    }
  ]
}
```

---

## Response Cards

### Card Structure

```json
{
  "cards": [
    {
      "uuid": "card-uuid",
      "summary": "Brief message",
      "detail": "Detailed explanation",
      "indicator": "info|warning|critical",
      "source": {
        "label": "SgTxGNN",
        "url": "https://sgtxgnn.yao.care"
      },
      "suggestions": [...],
      "links": [...]
    }
  ]
}
```

### Indicator Values

| Indicator | Use Case |
|-----------|----------|
| `info` | Informational message |
| `warning` | Needs attention |
| `critical` | Requires action |

### Suggestions

```json
{
  "suggestions": [
    {
      "label": "Review repurposing evidence",
      "uuid": "suggestion-uuid",
      "actions": [
        {
          "type": "create",
          "description": "Create task to review",
          "resource": {...}
        }
      ]
    }
  ]
}
```

### Smart Links

```json
{
  "links": [
    {
      "label": "View drug details",
      "url": "https://sgtxgnn.yao.care/drugs/db00945",
      "type": "absolute"
    },
    {
      "label": "Launch SMART app",
      "url": "https://sgtxgnn.yao.care/smart/launch.html",
      "type": "smart",
      "appContext": "drug=DB00945"
    }
  ]
}
```

---

## Prefetch

### Purpose

Prefetch allows the CDS service to request needed data upfront, reducing latency.

### Template Syntax

```json
{
  "prefetch": {
    "patient": "Patient/{{context.patientId}}",
    "conditions": "Condition?patient={{context.patientId}}",
    "medications": "MedicationRequest?patient={{context.patientId}}&status=active"
  }
}
```

### Handling Missing Prefetch

If EHR doesn't support prefetch, service can query FHIR server:

```javascript
async function handleRequest(request) {
  const medications = request.prefetch?.medications
    || await fetchMedications(request.fhirServer, request.context.patientId);
  // Process medications...
}
```

---

## Implementation Example

### Node.js Service

```javascript
const express = require('express');
const app = express();

// Discovery
app.get('/cds-services', (req, res) => {
  res.json({
    services: [{
      hook: 'order-select',
      id: 'sgtxgnn-repurposing',
      title: 'Drug Repurposing Insights'
    }]
  });
});

// Service endpoint
app.post('/cds-services/sgtxgnn-repurposing', (req, res) => {
  const { context, prefetch } = req.body;

  // Analyse medications
  const cards = analyseForRepurposing(context.draftOrders);

  res.json({ cards });
});

app.listen(3000);
```

---

## Security

### Authentication

CDS Hooks supports OAuth 2.0 bearer tokens:

```http
Authorization: Bearer {access_token}
```

### CORS

Enable CORS for EHR integration:

```javascript
app.use(cors({
  origin: '*',
  methods: ['GET', 'POST', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));
```

---

## Resources

- [CDS Hooks Specification](https://cds-hooks.org/)
- [CDS Hooks Sandbox](https://sandbox.cds-hooks.org/)
- [HL7 CDS Hooks IG](https://www.hl7.org/fhir/us/cds-hooks/)
