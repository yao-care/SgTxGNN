---
layout: default
title: Medium Evidence (L3-L4)
nav_order: 4
description: "Drug repurposing candidates with medium evidence levels (L3-L4)"
permalink: /evidence-medium/
---

# Medium Evidence Drugs (L3-L4)
{: .fs-9 }

Predictions with observational or preclinical support
{: .fs-6 .fw-300 }

---

## What is Medium Evidence?

**L3-L4** evidence levels indicate predictions supported by:

| Level | Definition | Evidence Type |
|-------|------------|---------------|
| **L3** | Observational Studies | Cohort or case-control studies |
| **L4** | Preclinical/Mechanistic | In vitro, animal studies, or mechanistic evidence |

These predictions have supporting evidence but need additional clinical validation.

---

## High-Score Predictions (DL > 0.99)

The following predictions have very high deep learning confidence scores:

<div id="medium-evidence-list">
  Loading medium evidence drugs...
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  fetch('{{ "/data/drugs-by-level.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('medium-evidence-list');
      const highScore = data.high_score || [];

      if (highScore.length === 0) {
        container.innerHTML = '<p>No high-score predictions found.</p>';
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
            ${highScore.slice(0, 50).map(d => `
              <tr>
                <td><a href="/drugs/${d.drugbank_id.toLowerCase()}/">${d.drug_name}</a></td>
                <td>${d.disease_name}</td>
                <td>${d.score.toFixed(4)}</td>
                <td><span class="badge ${d.source === 'KG+DL' ? 'kgdl' : 'dl'}">${d.source}</span></td>
              </tr>
            `).join('')}
          </tbody>
        </table>
        <p><em>Showing top 50 of ${highScore.length} high-score predictions (score > 0.99).</em></p>
      `;
    })
    .catch(err => {
      document.getElementById('medium-evidence-list').innerHTML = '<p>Failed to load data.</p>';
    });
});
</script>

<style>
.badge {
  padding: 0.125rem 0.5rem;
  border-radius: 3px;
  font-size: 0.75rem;
  font-weight: 600;
}
.badge.kgdl {
  background: #2E7D32;
  color: white;
}
.badge.dl {
  background: #1976D2;
  color: white;
}
</style>

---

## Recommended Action

For L3-L4 drugs, we recommend:

1. **Review mechanism** - Understand the biological rationale
2. **Check related trials** - Look for ongoing or planned studies
3. **Consider pilot study** - May warrant small-scale investigation
4. **Monitor literature** - Watch for new publications

---

## Related Pages

- [High Evidence (L1-L2)]({{ '/evidence-high' | relative_url }})
- [Low Evidence (L5)]({{ '/evidence-low' | relative_url }})
- [Full Drug List]({{ '/drugs' | relative_url }})
