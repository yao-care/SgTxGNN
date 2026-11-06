---
layout: default
title: Medium Evidence (L3-L4)
nav_order: 6
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

## Drugs at L3–L4

Drugs on this site whose evidence level (shown at the top of each drug page) is L3 or L4. The score is the TxGNN model score of the drug's top-scoring predicted indication — a ranking value, not a probability.

<div id="medium-level-list">
  Loading drugs...
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // 2026-11-06：/data/drugs-by-level.json 改由 scripts/generate_download_data.py 從本站公開藥物頁重產，
  // levels 依藥物頁頁首的證據等級分組（不含 noindex／轉址頁），藥物網址直接用檔內的 url。
  const base = '{{ "/" | relative_url }}'.replace(/\/$/, '');
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
  const LEVELS = ['L3', 'L4'];
  fetch('{{ "/data/drugs-by-level.json" | relative_url }}')
    .then(r => r.json())
    .then(data => {
      const container = document.getElementById('medium-level-list');
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
      document.getElementById('medium-level-list').innerHTML = '<p>Failed to load data.</p>';
    });
});
</script>

---

## High-Score Predictions (DL > 0.99, All Levels)

The highest-scoring predicted new indications across all evidence levels on this site's drug pages (the score is a ranking value, not a probability; the evidence level of each drug is on its page):

<div id="medium-evidence-list">
  Loading medium evidence drugs...
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // 2026-11-06：/data/drugs-by-level.json 改由 scripts/generate_download_data.py 從本站公開藥物頁重產；
  // high_score 每筆帶藥物頁 url，直接連到藥物頁（沒有 url 時只顯示名稱）。
  const base = '{{ "/" | relative_url }}'.replace(/\/$/, '');
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
  fetch('{{ "/data/drugs-by-level.json" | relative_url }}')
    .then(r => r.json())
    .then(data => {
      const drugLink = d => d.url ? `<a href="${esc(base + d.url)}">${esc(d.drug_name)}</a>` : esc(d.drug_name);
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
                <td>${drugLink(d)}</td>
                <td>${esc(d.disease_name)}</td>
                <td>${typeof d.score === 'number' ? d.score.toFixed(4) : '—'}</td>
                <td><span class="badge ${d.source === 'KG+DL' ? 'kgdl' : 'dl'}">${esc(d.source)}</span></td>
              </tr>
            `).join('')}
          </tbody>
        </table>
        <p><em>Showing top ${Math.min(50, highScore.length)} of ${(data.counts && data.counts.high_score) || highScore.length} predictions with score > 0.99.</em></p>
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
