---
layout: default
title: App Integration Assessment
parent: SMART on FHIR
nav_order: 5
description: "Criteria for evaluating SMART app integration"
permalink: /smart/assessment/
---

# App Integration Assessment

Evaluation criteria for healthcare application integration.

---

## Assessment Framework

When evaluating SMART on FHIR apps for clinical use, consider these dimensions:

### 1. Clinical Utility

| Criterion | SgTxGNN Rating | Notes |
|-----------|----------------|-------|
| Clear use case | High | Drug repurposing research |
| Evidence-based | High | TxGNN published in Nature Medicine |
| Actionable insights | Medium | Research guidance, not clinical decisions |
| Workflow integration | High | Embeds in medication review |

### 2. Technical Quality

| Criterion | SgTxGNN Rating | Notes |
|-----------|----------------|-------|
| SMART compliance | Full | R4 compatible |
| Performance | Good | Lightweight, browser-based |
| Error handling | Good | Graceful degradation |
| Accessibility | Basic | WCAG 2.0 AA target |

### 3. Security & Privacy

| Criterion | SgTxGNN Rating | Notes |
|-----------|----------------|-------|
| Data minimisation | Excellent | No data storage |
| Encryption | Full | HTTPS only |
| Authentication | Standard | OAuth 2.0 + PKCE |
| Audit trail | Limited | Browser logs only |

### 4. Regulatory Compliance

| Criterion | SgTxGNN Status | Notes |
|-----------|----------------|-------|
| PDPA (Singapore) | Compliant | No personal data collected |
| Research use disclaimer | Present | All pages |
| Medical device classification | Not applicable | Information only |

---

## Risk Assessment

### Benefits

- Access to AI-driven drug repurposing insights
- Integration with clinical workflow
- No additional data collection
- Research support tool

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Misuse for clinical decisions | Low | High | Clear disclaimers |
| Data privacy concerns | Very Low | High | No data storage |
| Incorrect predictions | Medium | Medium | Evidence levels shown |
| System downtime | Low | Low | Static hosting |

---

## Institutional Checklist

Before deploying SgTxGNN:

### Technical

- [ ] EHR supports SMART on FHIR R4
- [ ] Network allows HTTPS to `sgtxgnn.yao.care`
- [ ] App registered with EHR vendor
- [ ] Tested in sandbox environment

### Clinical

- [ ] Clinical champion identified
- [ ] Use case approved by clinical informatics
- [ ] Training materials prepared
- [ ] Feedback mechanism established

### Administrative

- [ ] Privacy assessment completed
- [ ] Security review passed
- [ ] Terms of use accepted
- [ ] Support contacts documented

### Governance

- [ ] App reviewed by relevant committee
- [ ] Usage policies defined
- [ ] Review schedule established
- [ ] Incident response plan updated

---

## Ongoing Monitoring

### Metrics to Track

- Number of launches per month
- Error rates and types
- User feedback scores
- Clinical utility assessments

### Review Schedule

| Activity | Frequency |
|----------|-----------|
| Usage metrics review | Monthly |
| User satisfaction survey | Quarterly |
| Security assessment | Annually |
| Clinical utility evaluation | Annually |

---

## Contact

For assessment support or questions:
- [GitHub Issues](https://github.com/yao-care/SgTxGNN/issues)
- Documentation: [Technical Docs]({{ '/smart/technical/' | relative_url }})
