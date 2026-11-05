---
layout: default
title: FHIR API Specification
parent: SMART on FHIR
nav_order: 6
description: "FHIR R4 API specification for SgTxGNN"
permalink: /smart/fhir-api/
---

# FHIR API Specification

FHIR R4 resources for SgTxGNN, published as static JSON files on GitHub Pages.

---

## Base URL

```
https://sgtxgnn.yao.care/fhir
```

The site is static: every resource is a file that can only be read (HTTP `GET`). Search queries such as `?subject=` or `?_id=` are not supported; use the file names below.

---

## File naming

| Resource | File | Example |
|----------|------|---------|
| CapabilityStatement | `/fhir/metadata` | [/fhir/metadata]({{ '/fhir/metadata' | relative_url }}) |
| MedicationKnowledge | `/fhir/MedicationKnowledge/{drug}.json` | `/fhir/MedicationKnowledge/amlodipine.json` |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/{drug}-{indication}.json` | `/fhir/ClinicalUseDefinition/amlodipine-brain-stem-infarction.json` |
| Bundle (all MedicationKnowledge) | `/fhir/Bundle/all-predictions.json` | [/fhir/Bundle/all-predictions.json]({{ '/fhir/Bundle/all-predictions.json' | relative_url }}) |

- `{drug}` is the drug's page slug, the same as in the drug report URL `/drugs/{drug}/` (lower case, words joined by `-`).
- `{indication}` is the predicted indication name in lower case with spaces and most punctuation turned into `-`; some names keep parentheses or `_`, e.g. `alanine-gastroparesis-(disease).json`. The full list of files is in the repository folder [`docs/fhir/ClinicalUseDefinition/`](https://github.com/yao-care/SgTxGNN/tree/main/docs/fhir/ClinicalUseDefinition).
- The resource `id` inside each file is the file name without `.json`.

---

## CapabilityStatement

```http
GET /fhir/metadata
```

Declares FHIR version `4.0.1` and `read` access to MedicationKnowledge and ClinicalUseDefinition.

---

## MedicationKnowledge

Drug information with the evidence level shown on the drug report.

### Read

```http
GET /fhir/MedicationKnowledge/{drug}.json
```

### Example

```http
GET /fhir/MedicationKnowledge/amlodipine.json
```

### Response

```json
{
  "resourceType": "MedicationKnowledge",
  "id": "amlodipine",
  "meta": {
    "profile": ["http://hl7.org/fhir/StructureDefinition/MedicationKnowledge"]
  },
  "status": "active",
  "code": {
    "coding": [{
      "system": "https://sgtxgnn.yao.care/drugs",
      "code": "amlodipine",
      "display": "AMLODIPINE"
    }],
    "text": "AMLODIPINE"
  },
  "intendedJurisdiction": [{
    "coding": [{
      "system": "urn:iso:std:iso:3166",
      "code": "SG",
      "display": "Singapore"
    }]
  }],
  "extension": [{
    "url": "https://sgtxgnn.yao.care/fhir/StructureDefinition/evidence-level",
    "valueCode": "L5"
  }]
}
```

---

## ClinicalUseDefinition

One file per predicted indication of a drug.

### Read

```http
GET /fhir/ClinicalUseDefinition/{drug}-{indication}.json
```

### Finding the predictions for a drug

There is no search endpoint. A drug's predicted indications are listed on its report (`/drugs/{drug}/`) and in [`/data/search-index.json`]({{ '/data/search-index.json' | relative_url }}); the matching files are the ones whose names start with `{drug}-` in [`docs/fhir/ClinicalUseDefinition/`](https://github.com/yao-care/SgTxGNN/tree/main/docs/fhir/ClinicalUseDefinition).

### Example

```http
GET /fhir/ClinicalUseDefinition/amlodipine-brain-stem-infarction.json
```

### Response

```json
{
  "resourceType": "ClinicalUseDefinition",
  "id": "amlodipine-brain-stem-infarction",
  "meta": {
    "profile": ["http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition"]
  },
  "type": "indication",
  "status": {
    "coding": [{
      "system": "http://hl7.org/fhir/publication-status",
      "code": "draft",
      "display": "Draft"
    }]
  },
  "subject": [{
    "reference": "MedicationKnowledge/amlodipine"
  }],
  "indication": {
    "diseaseSymptomProcedure": {
      "concept": {
        "text": "brain stem infarction"
      }
    }
  },
  "extension": [{
    "url": "https://sgtxgnn.yao.care/fhir/StructureDefinition/prediction-status",
    "valueCode": "predicted"
  }, {
    "url": "https://sgtxgnn.yao.care/fhir/StructureDefinition/evidence-level",
    "valueCode": "L5"
  }, {
    "url": "https://sgtxgnn.yao.care/fhir/StructureDefinition/txgnn-score",
    "valueDecimal": 0.9994
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

### Prediction Status

```
URL: https://sgtxgnn.yao.care/fhir/StructureDefinition/prediction-status
Type: code
Values: predicted
```

### TxGNN Score

```
URL: https://sgtxgnn.yao.care/fhir/StructureDefinition/txgnn-score
Type: decimal
Range: 0.0 - 1.0
```

Deep learning model score: a ranking value inside the model, not a probability.

---

## Errors

A file that does not exist returns HTTP `404` with the site's HTML "page not found" page, not a FHIR `OperationOutcome`.

---

## CORS

GitHub Pages sends `Access-Control-Allow-Origin: *`, so the files can be read from browser apps on other origins.
