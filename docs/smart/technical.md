---
layout: default
title: Technical Documentation
parent: SMART on FHIR
nav_order: 2
description: "Technical documentation for SgTxGNN SMART on FHIR integration"
permalink: /smart/technical/
---

# Technical Documentation

Technical specifications and implementation details for developers integrating SgTxGNN.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    EHR System                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │ FHIR Server │  │ Auth Server │  │ App Launcher    │  │
│  └──────┬──────┘  └──────┬──────┘  └────────┬────────┘  │
└─────────┼────────────────┼──────────────────┼───────────┘
          │                │                  │
          │ FHIR R4        │ OAuth 2.0        │ Launch
          │                │                  │
┌─────────▼────────────────▼──────────────────▼───────────┐
│                  SgTxGNN SMART App                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │ launch.html │─▶│  app.html   │◀─│ SgTxGNN FHIR    │  │
│  │ (OAuth)     │  │ (UI)        │  │ (Predictions)   │  │
│  └─────────────┘  └─────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## OAuth 2.0 Flow

### 1. Launch Request

EHR redirects to launch URL with parameters:
```
https://sgtxgnn.yao.care/smart/launch.html
  ?iss=https://ehr.example.com/fhir
  &launch=xyz123
```

### 2. Authorization

App requests authorization with scopes:
```javascript
FHIR.oauth2.authorize({
  client_id: "sgtxgnn-smart-app",
  scope: "launch patient/MedicationRequest.read patient/Patient.read patient/Condition.read",
  redirect_uri: "https://sgtxgnn.yao.care/smart/app.html",
  pkce: true
});
```

### 3. Token Exchange

After user authorisation, app receives access token and redirects to `app.html`.

### 4. FHIR Requests

App uses access token to query patient data:
```javascript
const client = await FHIR.oauth2.ready();
const patient = await client.patient.read();
const meds = await client.request(`MedicationRequest?patient=${patient.id}`);
```

---

## FHIR Resources

### CapabilityStatement

```
GET /fhir/metadata
Accept: application/fhir+json
```

### MedicationKnowledge

```
GET /fhir/MedicationKnowledge/{drugbank_id}
Accept: application/fhir+json
```

Example response:
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
  "status": "active"
}
```

### ClinicalUseDefinition

```
GET /fhir/ClinicalUseDefinition/{drugbank_id}-{disease_id}
Accept: application/fhir+json
```

---

## Integration Guide

### Step 1: Register App

Contact your EHR administrator with:

| Parameter | Value |
|-----------|-------|
| App Name | SgTxGNN Drug Repurposing |
| Launch URL | `https://sgtxgnn.yao.care/smart/launch.html` |
| Redirect URL | `https://sgtxgnn.yao.care/smart/app.html` |
| Scopes | `launch patient/MedicationRequest.read patient/Patient.read patient/Condition.read` |
| PKCE | Required |

### Step 2: Configure Client ID

After registration, update `launch.html` with your assigned `client_id`.

### Step 3: Test with SMART Launcher

Use [https://launch.smarthealthit.org](https://launch.smarthealthit.org) for testing.

---

## Security Considerations

### HTTPS Required

All endpoints use TLS 1.2+ encryption.

### CORS Policy

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Headers: Authorization, Content-Type
```

### No Data Retention

- Patient data processed in-browser only
- No server-side logging of patient information
- Session tokens expire after 1 hour

---

## Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | Supported |
| Firefox | 88+ | Supported |
| Safari | 14+ | Supported |
| Edge | 90+ | Supported |

---

## Error Handling

### Common Errors

| Error Code | Meaning | Resolution |
|------------|---------|------------|
| `invalid_scope` | Requested scope not allowed | Check scope configuration |
| `access_denied` | User denied authorization | Retry launch |
| `invalid_client` | Client ID not recognised | Verify registration |

### Debug Mode

Open browser developer tools to see:
- Network requests to FHIR server
- OAuth flow details
- Any JavaScript errors

---

## Support

- **GitHub Issues**: [SgTxGNN Issues](https://github.com/yao-care/SgTxGNN/issues)
- **Documentation**: [https://sgtxgnn.yao.care/smart/](https://sgtxgnn.yao.care/smart/)
