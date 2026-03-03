---
layout: default
title: ClinicalTrials.gov API v2
parent: SMART on FHIR
nav_order: 8
description: "Technical notes on ClinicalTrials.gov API v2"
permalink: /smart/clinicaltrials-api/
---

# ClinicalTrials.gov API v2 Technical Notes

Working with the ClinicalTrials.gov API for drug repurposing evidence.

---

## Overview

The ClinicalTrials.gov API v2 provides access to clinical trial data for evidence collection. This document covers key technical aspects.

---

## Base URL

```
https://clinicaltrials.gov/api/v2
```

---

## Key Endpoints

### Studies Search

```http
GET /studies?query.intr={drug}&query.cond={disease}
```

### Study Details

```http
GET /studies/{nctId}
```

### Field Definitions

```http
GET /studies/fields
```

---

## Query Parameters

### Search Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `query.intr` | Intervention/treatment | `aspirin` |
| `query.cond` | Condition/disease | `alzheimer` |
| `query.term` | General search | `repurposing` |
| `filter.overallStatus` | Trial status | `COMPLETED` |

### Pagination

| Parameter | Description | Default |
|-----------|-------------|---------|
| `pageSize` | Results per page | 10 |
| `pageToken` | Next page token | - |

### Response Format

| Parameter | Options |
|-----------|---------|
| `format` | `json`, `csv` |
| `fields` | Comma-separated field list |

---

## Example Queries

### Search for Drug-Disease Trials

```bash
curl "https://clinicaltrials.gov/api/v2/studies?query.intr=metformin&query.cond=cancer&pageSize=10"
```

### Get Specific Trial

```bash
curl "https://clinicaltrials.gov/api/v2/studies/NCT12345678"
```

### Search with Filters

```bash
curl "https://clinicaltrials.gov/api/v2/studies?query.intr=aspirin&filter.overallStatus=COMPLETED&filter.phase=PHASE3"
```

---

## Response Structure

```json
{
  "studies": [
    {
      "protocolSection": {
        "identificationModule": {
          "nctId": "NCT12345678",
          "briefTitle": "Study Title"
        },
        "statusModule": {
          "overallStatus": "COMPLETED",
          "startDateStruct": {
            "date": "2020-01-15"
          }
        },
        "descriptionModule": {
          "briefSummary": "Study summary..."
        },
        "conditionsModule": {
          "conditions": ["Condition A", "Condition B"]
        },
        "interventionsModule": {
          "interventions": [
            {
              "type": "DRUG",
              "name": "Drug Name"
            }
          ]
        },
        "designModule": {
          "phases": ["PHASE3"],
          "studyType": "INTERVENTIONAL"
        }
      }
    }
  ],
  "nextPageToken": "xyz123"
}
```

---

## Useful Fields

### For Evidence Collection

| Field Path | Description |
|------------|-------------|
| `protocolSection.identificationModule.nctId` | Trial identifier |
| `protocolSection.statusModule.overallStatus` | Current status |
| `protocolSection.designModule.phases` | Trial phases |
| `protocolSection.designModule.enrollmentInfo.count` | Participant count |
| `resultsSection` | Trial results (if available) |

### Status Values

| Status | Description |
|--------|-------------|
| `RECRUITING` | Currently enrolling |
| `ACTIVE_NOT_RECRUITING` | Ongoing, not enrolling |
| `COMPLETED` | Finished |
| `TERMINATED` | Stopped early |
| `WITHDRAWN` | Never started |

---

## Rate Limits

- **Anonymous**: 3 requests/second
- **With API Key**: 10 requests/second

Request API key: [ClinicalTrials.gov Contact](https://clinicaltrials.gov/contact)

---

## Integration Tips

### Efficient Searching

1. Use specific intervention names
2. Filter by phase for higher evidence
3. Limit to completed trials for results
4. Use field selection to reduce response size

### Error Handling

```python
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.exceptions.Timeout:
    # Retry with exponential backoff
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 429:
        # Rate limited - wait and retry
```

---

## Resources

- [API Documentation](https://clinicaltrials.gov/data-api/api)
- [Data Dictionary](https://clinicaltrials.gov/data-api/about-api/study-data-structure)
- [API Support](https://clinicaltrials.gov/contact)
