---
layout: default
title: Low Evidence (L5)
nav_order: 7
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

## Drugs at L5

Drugs on this site whose evidence level (shown at the top of each drug page) is L5. The score is the TxGNN model score of the drug's top-scoring predicted indication — a ranking value, not a probability.

{% comment %}2026-11-14：本等級藥物清單在建置時就輸出成 HTML（無 JS 也看得到、爬得到藥物頁連結）；口徑同 /data/drugs-by-level.json（公開藥物頁、依頁首等級）。下方 JS 載入後換成含最高分適應症的表。{%- endcomment -%}
{%- assign lv_levels = "L5" | split: "," -%}
{%- assign lv_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" | sort: "title" -%}
{%- assign lv_drugs = "" | split: "" -%}
{%- for lv in lv_levels -%}{%- assign lv_part = lv_listed | where: "evidence_level", lv -%}{%- assign lv_drugs = lv_drugs | concat: lv_part -%}{%- endfor -%}
{%- assign lv_L5 = lv_drugs | where: "evidence_level", "L5" | size -%}
<div id="low-evidence-stats">
<p><em>{{ lv_drugs.size }} drugs (L5: {{ lv_L5 }}).</em></p>
<table>
<thead><tr><th>Drug</th><th>Level</th><th>Predicted indications</th></tr></thead>
<tbody>
{%- for d in lv_drugs %}
<tr><td><a href="{{ d.url | relative_url }}">{{ d.title | escape }}</a></td><td>{{ d.evidence_level | escape }}</td><td>{{ d.indication_count | default: 0 }}</td></tr>
{%- endfor %}
</tbody>
</table>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // 2026-11-06：/data/drugs-by-level.json 改由 scripts/generate_download_data.py 從本站公開藥物頁重產，
  // levels 依藥物頁頁首的證據等級分組（不含 noindex／轉址頁），藥物網址直接用檔內的 url。
  const base = '{{ "/" | relative_url }}'.replace(/\/$/, '');
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
  const LEVELS = ['L5'];
  fetch('{{ "/data/drugs-by-level.json" | relative_url }}')
    .then(r => r.json())
    .then(data => {
      const container = document.getElementById('low-evidence-stats');
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
      // 讀不到 JSON 時保留建置時輸出的清單
    });
});
</script>

<style>
#low-evidence-stats table { font-size: 0.875rem; }
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
