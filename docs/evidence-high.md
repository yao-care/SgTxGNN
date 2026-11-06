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

Which of these drugs have trial evidence for their predicted new indication, and how many registered trials are cited? See [Singapore medicines with clinical-trial evidence for a new indication]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## What is High Evidence?

**L1-L2** evidence levels indicate predictions supported by:

| Level | Definition | Criteria |
|-------|------------|----------|
| **L1** | Multiple Phase 3 RCTs | ≥2 completed Phase 3 trials with positive results |
| **L2** | Single RCT or Phase 2 | 1 RCT or ≥2 Phase 2 trials |

These predictions have the strongest clinical foundation and can be prioritized for further evaluation.

---

## Drugs at L1–L2

Drugs on this site whose evidence level (shown at the top of each drug page) is L1 or L2. The score is the TxGNN model score of the drug's top-scoring predicted indication — a ranking value, not a probability. Open a drug page for the evidence behind each predicted indication.

<div id="high-evidence-list">
  Loading drugs...
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // 2026-11-06：/data/drugs-by-level.json 改由 scripts/generate_download_data.py 從本站公開藥物頁重產，
  // levels 依藥物頁頁首的證據等級分組（不含 noindex／轉址頁），藥物網址直接用檔內的 url。
  const base = '{{ "/" | relative_url }}'.replace(/\/$/, '');
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
  const LEVELS = ['L1', 'L2'];
  fetch('{{ "/data/drugs-by-level.json" | relative_url }}')
    .then(r => r.json())
    .then(data => {
      const container = document.getElementById('high-evidence-list');
      const rows = LEVELS.flatMap(lv => (data.levels && data.levels[lv]) || []);
      if (rows.length === 0) {
        container.innerHTML = '<p>No drugs at this evidence level.</p>';
        return;
      }
      container.innerHTML = `
        <p><em>${rows.length} drugs (${LEVELS.map(lv => lv + ': ' + (((data.levels || {})[lv]) || []).length).join(', ')}).</em></p>
        <table>
          <thead>
            <tr>
              <th>Drug</th>
              <th>Level</th>
              <th>Predicted indications</th>
              <th>Top-scoring predicted indication</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            ${rows.map(d => `
              <tr>
                <td><a href="${esc(base + d.url)}">${esc(d.drug_name)}</a></td>
                <td>${esc(d.evidence_level)}</td>
                <td>${esc(d.indication_count)}</td>
                <td>${esc(d.top_indication)}</td>
                <td>${typeof d.top_score === 'number' ? d.top_score.toFixed(4) : '—'}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      `;
    })
    .catch(err => {
      document.getElementById('high-evidence-list').innerHTML = '<p>Failed to load data.</p>';
    });
});
</script>

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
