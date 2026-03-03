---
layout: default
title: Integration Resources
parent: SMART on FHIR
nav_order: 3
description: "Integration resources for EHR administrators"
permalink: /smart/integration/
---

# Integration Resources

Resources for EHR administrators integrating SgTxGNN.

---

## Registration Details

### App Configuration

| Parameter | Value |
|-----------|-------|
| **App Name** | SgTxGNN Drug Repurposing |
| **Publisher** | Yao.Care |
| **Launch URL** | `https://sgtxgnn.yao.care/smart/launch.html` |
| **Redirect URL** | `https://sgtxgnn.yao.care/smart/app.html` |
| **Logo URL** | `https://sgtxgnn.yao.care/assets/images/logo.png` |

### OAuth Configuration

| Parameter | Value |
|-----------|-------|
| **Auth Type** | Authorization Code with PKCE |
| **Token Endpoint Auth** | None (public client) |
| **Scopes** | `launch patient/MedicationRequest.read patient/MedicationStatement.read patient/Patient.read patient/Condition.read` |

---

## Supported EHR Systems

SgTxGNN has been tested with:

| EHR System | Status | Notes |
|------------|--------|-------|
| Epic | Compatible | Register via App Orchard |
| Cerner | Compatible | Register via CODE Program |
| SMART Sandbox | Tested | For development |

---

## Step-by-Step Integration

### 1. Review App Documentation

- Read the [Technical Documentation]({{ '/smart/technical/' | relative_url }})
- Review security and privacy policies
- Ensure compliance with institutional policies

### 2. Register the Application

Contact your EHR vendor's app marketplace:
- **Epic**: [App Orchard](https://apporchard.epic.com/)
- **Cerner**: [CODE Program](https://code.cerner.com/)
- **Other**: Contact vendor directly

### 3. Configure Permissions

Minimum required scopes:
```
launch
patient/MedicationRequest.read
patient/Patient.read
```

Optional scopes for enhanced features:
```
patient/MedicationStatement.read
patient/Condition.read
```

### 4. Test in Sandbox

Before production deployment:
1. Register in sandbox environment
2. Test with sample patients
3. Verify data flows correctly
4. Check error handling

### 5. Deploy to Production

After successful testing:
1. Submit for production approval
2. Configure user access
3. Train clinical staff
4. Monitor usage and feedback

---

## Security Requirements

### Network

- TLS 1.2 or higher required
- Allow outbound HTTPS to `sgtxgnn.yao.care`
- No inbound connections required

### Authentication

- OAuth 2.0 with PKCE
- Tokens expire after 1 hour
- Refresh tokens not required

### Data Handling

- No patient data stored externally
- All processing in user's browser
- Audit logging available on request

---

## Support

For integration assistance:
- **Email**: via GitHub Issues
- **Documentation**: [Technical Docs]({{ '/smart/technical/' | relative_url }})
- **GitHub**: [SgTxGNN Repository](https://github.com/yao-care/SgTxGNN)

---

## Compliance

### Certifications

- SMART on FHIR R4 compatible
- OAuth 2.0 compliant
- HTTPS only

### Data Protection

- No personal data collected
- No data stored on external servers
- Privacy by design architecture
