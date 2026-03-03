---
layout: default
title: Drug-Drug Interactions
parent: Safety Data
nav_order: 1
description: "Drug-drug interaction database"
permalink: /safety/drug-interactions/
---

# Drug-Drug Interactions

Potential interactions between medications in the SgTxGNN database.

---

## Overview

Drug-drug interactions (DDIs) occur when one medication affects the action of another. Understanding DDIs is crucial for:

- Safe prescribing
- Avoiding adverse effects
- Optimising therapeutic outcomes

---

## Search Interactions

*Interactive search coming soon*

For now, individual drug pages include interaction information. See the [Drug Reports]({{ '/drugs/' | relative_url }}) section.

---

## Interaction Categories

### By Mechanism

| Category | Description | Example |
|----------|-------------|---------|
| **Metabolic** | CYP450 enzyme interactions | Ketoconazole + Simvastatin |
| **Transport** | P-gp and transporter effects | Cyclosporine + Digoxin |
| **Receptor** | Competing at same receptors | Fluoxetine + Tramadol |
| **Additive** | Combined similar effects | NSAIDs + Anticoagulants |

### By Severity

| Level | Action Required |
|-------|-----------------|
| **Critical** | Combination generally contraindicated |
| **Serious** | Alternative recommended or close monitoring |
| **Moderate** | May require dose adjustment |
| **Minor** | Minimal clinical significance |

---

## Common High-Risk Interactions

### Anticoagulants

| Drug | Interacting Class | Effect |
|------|------------------|--------|
| Warfarin | NSAIDs | Increased bleeding risk |
| Warfarin | Antibiotics | INR changes |
| DOACs | P-gp inhibitors | Increased levels |

### Cardiovascular

| Drug | Interacting Drug | Effect |
|------|-----------------|--------|
| Statins | CYP3A4 inhibitors | Myopathy risk |
| Digoxin | Amiodarone | Toxicity risk |
| ACE inhibitors | Potassium supplements | Hyperkalaemia |

### CNS Medications

| Drug | Interacting Class | Effect |
|------|------------------|--------|
| SSRIs | MAOIs | Serotonin syndrome |
| Benzodiazepines | Opioids | Respiratory depression |
| Antipsychotics | QT-prolonging drugs | Arrhythmia risk |

---

## Interaction Mechanisms

### CYP450 System

Key enzymes and their clinical significance:

| Enzyme | Major Substrates | Notable Inhibitors |
|--------|-----------------|-------------------|
| CYP3A4 | Statins, Calcium channel blockers | Ketoconazole, Grapefruit |
| CYP2D6 | Codeine, Tamoxifen | Fluoxetine, Paroxetine |
| CYP2C9 | Warfarin, Phenytoin | Fluconazole |
| CYP2C19 | Clopidogrel, PPIs | Omeprazole |

### P-glycoprotein

| Effect | Clinical Consequence |
|--------|---------------------|
| Inhibition | Increased substrate absorption |
| Induction | Decreased substrate levels |

---

## Data Sources

| Source | Coverage |
|--------|----------|
| **DDInter** | 240,000+ interaction pairs |
| **DrugBank** | Mechanism-based interactions |
| **HSA Alerts** | Singapore-specific warnings |

---

## API Access

Query interactions programmatically:

```bash
# Check interaction between two drugs
curl "https://sgtxgnn.yao.care/api/ddi?drugA=DB00945&drugB=DB00374"
```

Response:
```json
{
  "drugA": "Aspirin",
  "drugB": "Warfarin",
  "interaction": true,
  "severity": "serious",
  "description": "Increased risk of bleeding",
  "mechanism": "Additive antiplatelet and anticoagulant effects"
}
```

---

<div class="disclaimer">
<strong>Clinical Use Warning</strong><br>
This database is for research purposes. Clinical decisions about drug combinations should involve pharmacist review and consideration of individual patient factors.
</div>
