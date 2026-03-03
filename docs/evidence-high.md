---
layout: default
title: High Evidence (L1-L2)
nav_order: 5
description: "Drug repurposing candidates with high evidence levels (L1-L2)"
permalink: /evidence-high/
---

# High Evidence Drugs (L1-L2)
{: .fs-9 }

Predictions with strong clinical trial support
{: .fs-6 .fw-300 }

---

## What is High Evidence?

**L1-L2** evidence levels indicate predictions supported by:

| Level | Definition | Criteria |
|-------|------------|----------|
| **L1** | Multiple Phase 3 RCTs | ≥2 completed Phase 3 trials with positive results |
| **L2** | Single RCT or Phase 2 | 1 RCT or ≥2 Phase 2 trials |

These predictions have the strongest clinical foundation and can be prioritized for further evaluation.

---

## KG+DL Dual Validated Predictions

The following predictions are validated by **both** Knowledge Graph and Deep Learning methods, providing the highest confidence:

<div id="high-evidence-list">
  Loading high evidence drugs...
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  fetch('{{ "/data/drugs-by-level.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('high-evidence-list');
      const highEvidence = data.kgdl_validated || [];

      if (highEvidence.length === 0) {
        container.innerHTML = '<p>No high evidence drugs found.</p>';
        return;
      }

      container.innerHTML = `
        <table>
          <thead>
            <tr>
              <th>Drug</th>
              <th>Predicted Indication</th>
              <th>Score</th>
              <th>Source</th>
            </tr>
          </thead>
          <tbody>
            ${highEvidence.slice(0, 50).map(d => `
              <tr>
                <td><a href="/drugs/${d.drugbank_id.toLowerCase()}/">${d.drug_name}</a></td>
                <td>${d.disease_name}</td>
                <td>${d.score ? d.score.toFixed(4) : 'N/A'}</td>
                <td><span class="badge kgdl">KG+DL</span></td>
              </tr>
            `).join('')}
          </tbody>
        </table>
        <p><em>Showing top 50 of ${highEvidence.length} KG+DL validated predictions.</em></p>
      `;
    })
    .catch(err => {
      document.getElementById('high-evidence-list').innerHTML = '<p>Failed to load data.</p>';
    });
});
</script>

<style>
.badge.kgdl {
  padding: 0.125rem 0.5rem;
  border-radius: 3px;
  font-size: 0.75rem;
  font-weight: 600;
  background: #2E7D32;
  color: white;
}
</style>

---

## Recommended Action

For L1-L2 drugs, we recommend:

1. **Review full report** - Check clinical trial details and literature
2. **Assess applicability** - Consider patient population and local context
3. **Evaluate safety** - Check drug interactions and contraindications
4. **Plan next steps** - Consider feasibility study or clinical protocol

---

## Related Pages

- [Medium Evidence (L3-L4)]({{ '/evidence-medium' | relative_url }})
- [Low Evidence (L5)]({{ '/evidence-low' | relative_url }})
- [Full Drug List]({{ '/drugs' | relative_url }})
