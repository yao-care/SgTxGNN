---
layout: default
title: Low Evidence (L5)
nav_order: 5
description: "Drug repurposing candidates with prediction only (L5)"
permalink: /evidence-low/
---

# Prediction Only (L5)
{: .fs-9 }

AI predictions without clinical evidence
{: .fs-6 .fw-300 }

---

## What is L5 Evidence?

**L5** indicates predictions based solely on AI models without supporting clinical evidence:

| Level | Definition | Status |
|-------|------------|--------|
| **L5** | Prediction Only | No clinical trials or publications found |

These predictions represent research hypotheses that require validation.

---

## All Predictions by Source

<div id="low-evidence-stats">
  Loading prediction statistics...
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  fetch('{{ "/data/drugs-by-level.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('low-evidence-stats');

      container.innerHTML = `
        <table>
          <thead>
            <tr>
              <th>Source</th>
              <th>Count</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="badge kgdl">KG+DL</span></td>
              <td>${data.counts?.kgdl || 0}</td>
              <td>Validated by both methods - highest confidence</td>
            </tr>
            <tr>
              <td><span class="badge dl">DL</span></td>
              <td>${data.counts?.dl || 0}</td>
              <td>Deep learning prediction with confidence score</td>
            </tr>
            <tr>
              <td><span class="badge kg">KG</span></td>
              <td>${data.counts?.kg || 0}</td>
              <td>Knowledge graph prediction</td>
            </tr>
            <tr>
              <td><strong>Total</strong></td>
              <td><strong>${data.counts?.total || 0}</strong></td>
              <td></td>
            </tr>
          </tbody>
        </table>
      `;
    })
    .catch(err => {
      document.getElementById('low-evidence-stats').innerHTML = '<p>Failed to load data.</p>';
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
.badge.kg {
  background: #9E9E9E;
  color: white;
}
</style>

---

## How to Use L5 Predictions

L5 predictions can be valuable as:

1. **Research Hypotheses** - Starting points for new investigations
2. **Grant Applications** - Computational support for research proposals
3. **Literature Review Prompts** - Check if evidence has emerged since prediction
4. **Collaborative Opportunities** - Shared with research partners

---

## Caveats

- L5 does not mean "ineffective" - it means "not yet studied"
- Some L5 predictions may become L1-L4 as research progresses
- High DL scores in L5 may indicate promising unexplored areas

---

## Related Pages

- [High Evidence (L1-L2)]({{ '/evidence-high' | relative_url }})
- [Medium Evidence (L3-L4)]({{ '/evidence-medium' | relative_url }})
- [Full Drug List]({{ '/drugs' | relative_url }})
