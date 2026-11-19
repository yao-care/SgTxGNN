---
layout: default
title: Medium Evidence (L3-L4)
nav_order: 6
description: "76 medicines at evidence level L3–L4 on this site (Singapore), e.g. Acitretin, Alprazolam, Calcipotriol, with the main predicted new indication, local HSA registrations and review-log entries for each."
permalink: /evidence-medium/
---

# Medium Evidence Drugs (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
This page lists **{{ site.data.evidence_tier_facts.medium.count }}** of the **{{ site.data.drug_stats.total_drugs }}** medicines with a published report on this site ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Median share at L3–L4 across the 30 TxGNN sites: {{ site.data.evidence_tier_facts.medium.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}This site is above the median.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}This site is below the median.{% else %}This site is at the median.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
In the local data (HSA registrations), **{{ site.data.evidence_tier_facts.medium.with_current }}** of these medicines have at least one current entry, **{{ site.data.evidence_tier_facts.medium.none_current }}** have entries but none current, and **{{ site.data.evidence_tier_facts.medium.without_data }}** are not in the local data. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** have entries in the review log (corrections of registration facts on the drug page). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** have a predicted indication that no other TxGNN site lists for the same medicine.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

With entries but none current: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definitions of all levels: [Methodology]({{ '/methodology/' | relative_url }}).

<!-- tier-table:start all（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicine | Level | Main predicted new indication | HSA registrations: current / total | Review log | Only on this site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if true %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}yes ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->
<!-- tier-facts:end -->
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

{% comment %}2026-11-14：本等級藥物清單在建置時就輸出成 HTML（無 JS 也看得到、爬得到藥物頁連結）；口徑同 /data/drugs-by-level.json（公開藥物頁、依頁首等級）。下方 JS 載入後換成含最高分適應症的表。{%- endcomment -%}
{%- assign lv_levels = "L3,L4" | split: "," -%}
{%- assign lv_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" | sort: "title" -%}
{%- assign lv_drugs = "" | split: "" -%}
{%- for lv in lv_levels -%}{%- assign lv_part = lv_listed | where: "evidence_level", lv -%}{%- assign lv_drugs = lv_drugs | concat: lv_part -%}{%- endfor -%}
{%- assign lv_L3 = lv_drugs | where: "evidence_level", "L3" | size -%}
{%- assign lv_L4 = lv_drugs | where: "evidence_level", "L4" | size -%}
<div id="medium-level-list">
<p><em>{{ lv_drugs.size }} drugs (L3: {{ lv_L3 }}, L4: {{ lv_L4 }}).</em></p>
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
      // 讀不到 JSON 時保留建置時輸出的清單
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
