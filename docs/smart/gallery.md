---
layout: default
title: SMART App Gallery Reference
parent: SMART on FHIR
nav_order: 4
description: "Reference SMART apps and examples"
permalink: /smart/gallery/
---

# SMART App Gallery Reference

Examples and reference implementations for SMART on FHIR applications.

---

## Official Resources

### SMART App Gallery

The [SMART App Gallery](https://apps.smarthealthit.org/) showcases registered SMART on FHIR applications.

Key features:
- Searchable catalogue of healthcare apps
- Verified publisher information
- Compatibility details for different EHR systems

### Reference Apps

| App | Purpose | Source |
|-----|---------|--------|
| Growth Chart | Pediatric growth tracking | [GitHub](https://github.com/smart-on-fhir/growth-chart-app) |
| Cardiac Risk | ASCVD risk calculation | [GitHub](https://github.com/smart-on-fhir/cardiac-risk-app) |
| BP Centiles | Blood pressure percentiles | [GitHub](https://github.com/smart-on-fhir/bp-centiles-app) |

---

## Drug Information Apps

### Similar Applications

Applications with similar functionality to SgTxGNN:

| Application | Focus | EHR Support |
|-------------|-------|-------------|
| **MedlinePlus Connect** | Drug information | Epic, Cerner |
| **Lexicomp** | Drug interactions | Multiple |
| **UpToDate** | Clinical decision support | Multiple |

### How SgTxGNN Differs

SgTxGNN uniquely provides:
- AI-predicted drug repurposing candidates
- Dual validation (Knowledge Graph + Deep Learning)
- Singapore HSA-approved medication focus
- Evidence level classification (L1-L5)

---

## Implementation Patterns

### Launch Patterns

```javascript
// EHR Launch
FHIR.oauth2.authorize({
  client_id: "your-client-id",
  scope: "launch patient/MedicationRequest.read",
  redirect_uri: "https://yourapp.com/callback"
});

// Standalone Launch
FHIR.oauth2.authorize({
  client_id: "your-client-id",
  scope: "patient/MedicationRequest.read launch/patient",
  redirect_uri: "https://yourapp.com/callback",
  iss: "https://fhir.example.com"
});
```

### Data Fetching

```javascript
// After authorization
const client = await FHIR.oauth2.ready();

// Get patient
const patient = await client.patient.read();

// Get medications
const meds = await client.request(
  `MedicationRequest?patient=${patient.id}&status=active`
);
```

---

## Design Guidelines

### User Interface

Follow SMART on FHIR design recommendations:
- Responsive design for embedded frames
- Clear branding and attribution
- Accessible color contrast
- Loading states for async operations

### Performance

Best practices:
- Lazy load non-critical resources
- Cache static data
- Minimize API calls
- Use pagination for large datasets

---

## Resources

### Documentation

- [SMART on FHIR](https://smarthealthit.org/)
- [HL7 FHIR](https://www.hl7.org/fhir/)
- [FHIR Client JS](https://github.com/smart-on-fhir/client-js)

### Development Tools

- [SMART App Launcher](https://launch.smarthealthit.org/)
- [HAPI FHIR Server](https://hapifhir.io/)
- [Inferno Test Suite](https://inferno.healthit.gov/)
