---
layout: default
title: Privacy Policy
nav_order: 99
description: "SgTxGNN privacy policy"
permalink: /privacy-policy/
---

# Privacy Policy

Last updated: 5 November 2026

---

## Overview

SgTxGNN is a research platform providing drug repurposing predictions. We are committed to protecting your privacy and being transparent about our data practices.

---

## Information We Collect

### Website Analytics

We use Google Analytics 4, with analytics cookies set when a page loads, to understand how the website is used:
- Page views and navigation patterns
- Browser and device information
- Approximate geographic location (derived by Google Analytics)

We do **not** collect:
- Names, email addresses or account information (the site has no accounts or forms)
- Search terms, form contents or URL query strings (these are not sent to Google Analytics)

### SMART App Data

When using our SMART on FHIR application:
- Patient identity and EHR data are not sent to SgTxGNN's servers (this is a static site with no backend) and are not stored by SgTxGNN
- To match drug names, the app sends the medications' RxNorm codes (no patient identifiers) to the US National Library of Medicine's RxNav service; when you ask for clinical trials, the drug and indication names are sent to ClinicalTrials.gov
- Authentication is handled by your EHR system

---

## How We Use Information

Website analytics help us:
- Improve content and navigation
- Understand which drugs/predictions are most viewed
- Plan future features

---

## Data Sharing

We do **not**:
- Sell any data
- Share data with third parties for marketing
- Use data for any commercial purpose

We **may** share:
- Aggregated, anonymized usage statistics in research publications
- Open source code and datasets for research purposes

---

## Cookies

The only cookies on this website are the Google Analytics 4 analytics cookies (such as `_ga`), used for the usage statistics described above. They are set when a page loads. The site sets no cookies of its own for sessions or preferences.

---

## Third-Party Services

### GitHub Pages

This website is hosted on GitHub Pages. See [GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement).

### Resources loaded by the site

The pages load the following third-party resources, which may log access in accordance with their own privacy policies:

| Service | Purpose | Privacy policy |
|---------|---------|----------------|
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Visit statistics (pages viewed, referrer); uses analytics cookies. Search terms, form contents and URL query strings are not sent. | [Google Privacy Policy](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Script libraries: d3 charts on every page; Fuse.js name matching and the SMART on FHIR client on the SMART pages and in the home-page drug lookup | [jsDelivr Privacy Policy](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Clinical-trial lookup on the SMART pages: only when you ask for trials, the drug and indication names are sent to the ClinicalTrials.gov API | [NLM Web Policies](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | SMART app: the RxNorm codes of the medications read from your EHR are sent to the NLM RxNav API to look up ingredient names (no patient identifiers) | [NLM Web Policies](https://www.nlm.nih.gov/web_policies.html) |

---

## Your Rights

You have the right to:
- Access information about you
- Request deletion of any personal data
- Opt out of analytics

Contact us at [GitHub Issues](https://github.com/yao-care/SgTxGNN/issues) for any privacy-related requests.

---

## Research Use

This platform is intended for research purposes. By using SgTxGNN, you agree that:
- Predictions are not medical advice
- Data should not be used for direct clinical decisions
- Any research use should follow ethical guidelines

---

## Changes to This Policy

We may update this policy periodically. Changes will be posted on this page with an updated date.

---

## Contact

For privacy concerns, please contact us through:
- [GitHub Issues](https://github.com/yao-care/SgTxGNN/issues)

---

<div class="disclaimer">
<strong>Research Platform</strong><br>
SgTxGNN is a research tool. It does not collect or store personal health information. In the SMART app, patient data is processed in your browser to display predictions; only the medications' RxNorm codes (no patient identifiers) are sent to NLM RxNav, and the drug and indication names to ClinicalTrials.gov when you ask for trials.
</div>
