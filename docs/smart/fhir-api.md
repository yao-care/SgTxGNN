---
layout: default
title: FHIR API Specification
parent: SMART on FHIR
nav_order: 6
description: "FHIR R4 API specification for SgTxGNN"
permalink: /smart/fhir-api/
---

# FHIR API Specification

Complete FHIR R4 API documentation for SgTxGNN.

---

## Base URL

```
https://sgtxgnn.yao.care/fhir
```

---

## CapabilityStatement

### Request

```http
GET /fhir/metadata
Accept: application/fhir+json
```

### Response

```json
{
  "resourceType": "CapabilityStatement",
  "status": "active",
  "date": "2026-03-01",
  "publisher": "Yao.Care",
  "kind": "instance",
  "fhirVersion": "4.0.1",
  "format": ["json"],
  "rest": [{
    "mode": "server",
    "resource": [
      {
        "type": "MedicationKnowledge",
        "profile": "http://hl7.org/fhir/StructureDefinition/MedicationKnowledge",
        "interaction": [{"code": "read"}, {"code": "search-type"}]
      },
      {
        "type": "ClinicalUseDefinition",
        "profile": "http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition",
        "interaction": [{"code": "read"}, {"code": "search-type"}]
      }
    ]
  }]
}
```

---

## MedicationKnowledge

Drug information with repurposing metadata.

### Read

```http
GET /fhir/MedicationKnowledge/{drugbank_id}
Accept: application/fhir+json
```

### Example

```http
GET /fhir/MedicationKnowledge/DB00945
```

### Response

```json
{
  "resourceType": "MedicationKnowledge",
  "id": "DB00945",
  "code": {
    "coding": [{
      "system": "https://www.drugbank.ca",
      "code": "DB00945",
      "display": "Aspirin"
    }]
  },
  "status": "active",
  "manufacturer": {
    "display": "Various"
  },
  "extension": [{
    "url": "https://sgtxgnn.yao.care/fhir/StructureDefinition/hsa-license",
    "valueString": "SIN12345P"
  }, {
    "url": "https://sgtxgnn.yao.care/fhir/StructureDefinition/prediction-count",
    "valueInteger": 42
  }]
}
```

---

## ClinicalUseDefinition

Drug repurposing predictions.

### Read

```http
GET /fhir/ClinicalUseDefinition/{id}
Accept: application/fhir+json
```

### Search by Drug

```http
GET /fhir/ClinicalUseDefinition?subject=MedicationKnowledge/{drugbank_id}
Accept: application/fhir+json
```

### Example

```http
GET /fhir/ClinicalUseDefinition/DB00945-alzheimer
```

### Response

```json
{
  "resourceType": "ClinicalUseDefinition",
  "id": "DB00945-alzheimer",
  "type": "indication",
  "subject": [{
    "reference": "MedicationKnowledge/DB00945"
  }],
  "indication": {
    "diseaseSymptomProcedure": {
      "concept": {
        "coding": [{
          "system": "http://snomed.info/sct",
          "code": "26929004",
          "display": "Alzheimer's disease"
        }],
        "text": "Alzheimer's disease"
      }
    }
  },
  "extension": [{
    "url": "https://sgtxgnn.yao.care/fhir/StructureDefinition/evidence-level",
    "valueCode": "L4"
  }, {
    "url": "https://sgtxgnn.yao.care/fhir/StructureDefinition/prediction-source",
    "valueCode": "KG+DL"
  }, {
    "url": "https://sgtxgnn.yao.care/fhir/StructureDefinition/txgnn-score",
    "valueDecimal": 0.9923
  }]
}
```

---

## Extension Definitions

### Evidence Level

```
URL: https://sgtxgnn.yao.care/fhir/StructureDefinition/evidence-level
Type: code
Values: L1, L2, L3, L4, L5
```

| Value | Description |
|-------|-------------|
| L1 | Multiple Phase 3 RCTs |
| L2 | Single RCT or Phase 2 |
| L3 | Observational studies |
| L4 | Preclinical/mechanistic |
| L5 | Model prediction only |

### Prediction Source

```
URL: https://sgtxgnn.yao.care/fhir/StructureDefinition/prediction-source
Type: code
Values: KG, DL, KG+DL
```

| Value | Description |
|-------|-------------|
| KG | Knowledge Graph only |
| DL | Deep Learning only |
| KG+DL | Both methods (higher confidence) |

### TxGNN Score

```
URL: https://sgtxgnn.yao.care/fhir/StructureDefinition/txgnn-score
Type: decimal
Range: 0.0 - 1.0
```

Deep learning confidence score.

---

## Error Responses

### 404 Not Found

```json
{
  "resourceType": "OperationOutcome",
  "issue": [{
    "severity": "error",
    "code": "not-found",
    "diagnostics": "Resource not found"
  }]
}
```

### 400 Bad Request

```json
{
  "resourceType": "OperationOutcome",
  "issue": [{
    "severity": "error",
    "code": "invalid",
    "diagnostics": "Invalid request parameters"
  }]
}
```

---

## Rate Limits

| Endpoint | Limit |
|----------|-------|
| Read operations | 100/minute |
| Search operations | 50/minute |

---

## CORS

Cross-Origin Resource Sharing is enabled for all origins:

```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Headers: Authorization, Content-Type, Accept
```
