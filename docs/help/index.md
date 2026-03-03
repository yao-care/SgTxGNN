---
layout: default
title: Help
nav_order: 10
has_children: true
description: "Documentation and guides for SgTxGNN"
permalink: /help/
---

# Help & Documentation
{: .fs-9 }

Guides, methodology, and project information
{: .fs-6 .fw-300 }

---

## Quick Links

| Resource | Description |
|----------|-------------|
| [Methodology]({{ '/methodology/' | relative_url }}) | How predictions are generated |
| [User Guide]({{ '/guide/' | relative_url }}) | How to use this platform |
| [About]({{ '/about/' | relative_url }}) | Project background and team |
| [Privacy Policy]({{ '/privacy-policy/' | relative_url }}) | Data handling and privacy |

---

## Frequently Asked Questions

### What is SgTxGNN?

SgTxGNN is a drug repurposing prediction platform for Singapore HSA-approved medications, based on Harvard's TxGNN model published in *Nature Medicine*.

### How accurate are the predictions?

Predictions should be viewed as research hypotheses. While TxGNN is validated on known drug-disease relationships, individual predictions require clinical validation before any therapeutic application.

### What do the evidence levels mean?

| Level | Meaning |
|-------|---------|
| L1 | Multiple Phase 3 RCTs support this use |
| L2 | Single RCT or Phase 2 evidence |
| L3 | Observational study evidence |
| L4 | Preclinical or mechanistic evidence |
| L5 | AI prediction only, no clinical evidence |

### What does KG+DL mean?

Predictions marked "KG+DL" are validated by both the Knowledge Graph method and the Deep Learning method, indicating higher confidence.

### Can I use this data for research?

Yes, SgTxGNN data is available for academic research with proper citation. See [Downloads]({{ '/resources/downloads/' | relative_url }}) for data files.

### How do I report an issue?

Please report issues via [GitHub Issues](https://github.com/yao-care/SgTxGNN/issues).

---

## Getting Started

### For Researchers

1. Browse [Drug Reports]({{ '/drugs/' | relative_url }}) for available drugs
2. Review [Methodology]({{ '/methodology/' | relative_url }}) to understand predictions
3. Download data from [Downloads]({{ '/resources/downloads/' | relative_url }})
4. Cite appropriately in publications

### For Clinicians

1. Search for drugs of interest
2. Review evidence levels and sources
3. Check [Safety Data]({{ '/safety/' | relative_url }}) for interactions
4. Remember: predictions are for research only

### For Developers

1. Review [FHIR API]({{ '/smart/fhir-api/' | relative_url }}) documentation
2. Test with [SMART App]({{ '/smart/' | relative_url }}) integration
3. Clone from [GitHub](https://github.com/yao-care/SgTxGNN)

---

## Contact

For questions or feedback:

- **GitHub Issues**: [Report a problem](https://github.com/yao-care/SgTxGNN/issues)
- **Discussions**: [Ask a question](https://github.com/yao-care/SgTxGNN/discussions)

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
SgTxGNN is for research purposes only and does not provide medical advice. Always consult healthcare professionals for treatment decisions.
</div>
