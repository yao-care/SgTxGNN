---
layout: default
title: Safety Data
nav_order: 8
has_children: true
description: "Drug safety information including interactions and precautions"
permalink: /safety/
---

# Safety Data
{: .fs-9 }

Drug interactions and safety information
{: .fs-6 .fw-300 }

---

## Overview

SgTxGNN provides comprehensive safety data to support drug repurposing research. Before considering any off-label use, understanding potential interactions and contraindications is essential.

---

## Safety Categories

| Category | Description | Count |
|----------|-------------|-------|
| [Drug-Drug Interactions]({{ '/safety/drug-interactions/' | relative_url }}) | Interactions between medications | Coming soon |
| [Drug-Disease Precautions]({{ '/safety/drug-disease/' | relative_url }}) | Contraindicated conditions | Coming soon |
| [Drug-Food Interactions]({{ '/safety/drug-food/' | relative_url }}) | Food and beverage warnings | Coming soon |
| [Drug-Herb Interactions]({{ '/safety/drug-herb/' | relative_url }}) | Herbal supplement interactions | Coming soon |

---

## Why Safety Data Matters

Drug repurposing involves using approved medications for new indications. While these drugs have established safety profiles, new uses may:

- Require different dosing
- Involve new patient populations
- Create unexpected interactions
- Present different risk-benefit ratios

---

## Data Sources

Our safety data comes from:

| Source | Type |
|--------|------|
| **DDInter** | Drug-drug interactions database |
| **DrugBank** | Comprehensive drug information |
| **HSA** | Singapore regulatory safety data |
| **FDA** | Drug safety communications |

---

## Using Safety Data

### For Researchers

- Identify potential safety concerns early
- Design safer clinical trials
- Understand mechanistic interactions

### For Clinicians

- Review before off-label prescribing
- Consider patient-specific factors
- Document risk assessment

### Limitations

- Data may not be complete
- New interactions may not be included
- Individual patient factors vary
- Always verify with current sources

---

## Key Interaction Types

### Pharmacokinetic

How drugs affect each other's absorption, distribution, metabolism, or excretion:

- **CYP450 inhibition/induction**
- **P-glycoprotein interactions**
- **Protein binding displacement**

### Pharmacodynamic

How drugs interact at the effect level:

- **Additive effects**
- **Synergistic effects**
- **Antagonistic effects**

---

## Alert Levels

| Level | Icon | Meaning |
|-------|------|---------|
| **Critical** | | Avoid combination |
| **Serious** | | Use with caution |
| **Moderate** | | Monitor closely |
| **Minor** | | Be aware |

---

<div class="disclaimer">
<strong>Important Notice</strong><br>
Safety data is provided for research and educational purposes only. Clinical decisions must be made by qualified healthcare professionals considering individual patient factors. Report any suspected adverse reactions to HSA or your healthcare provider.
</div>
