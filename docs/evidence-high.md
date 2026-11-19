---
layout: default
title: High Evidence (L1-L2)
nav_order: 5
description: "45 medicines at evidence level L1–L2 on this site (Singapore), e.g. Bendamustine, Busulfan, Clofarabine, with the main predicted new indication, local HSA registrations and review-log entries for each."
permalink: /evidence-high/
---

# High Evidence Drugs (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
This page lists **{{ site.data.evidence_tier_facts.high.count }}** of the **{{ site.data.drug_stats.total_drugs }}** medicines with a published report on this site ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Median share at L1–L2 across the 30 TxGNN sites: {{ site.data.evidence_tier_facts.high.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}This site is above the median.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}This site is below the median.{% else %}This site is at the median.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
In the local data (HSA registrations), **{{ site.data.evidence_tier_facts.high.with_current }}** of these medicines have at least one current entry, **{{ site.data.evidence_tier_facts.high.none_current }}** have entries but none current, and **{{ site.data.evidence_tier_facts.high.without_data }}** are not in the local data. **{{ site.data.evidence_tier_facts.high.with_reviews }}** have entries in the review log (corrections of registration facts on the drug page). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** have a predicted indication that no other TxGNN site lists for the same medicine.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

With entries but none current: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definitions of all levels: [Methodology]({{ '/methodology/' | relative_url }}).

<!-- tier-table:start all（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicine | Level | Main predicted new indication | HSA registrations: current / total | Review log | Only on this site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if true %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}yes ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->
<!-- tier-facts:end -->
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

{% comment %}2026-11-14：本等級藥物清單在建置時就輸出成 HTML（無 JS 也看得到、爬得到藥物頁連結）；口徑同 /data/drugs-by-level.json（公開藥物頁、依頁首等級）。下方 JS 載入後換成含最高分適應症的表。{%- endcomment -%}
{%- assign lv_levels = "L1,L2" | split: "," -%}
{%- assign lv_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" | sort: "title" -%}
{%- assign lv_drugs = "" | split: "" -%}
{%- for lv in lv_levels -%}{%- assign lv_part = lv_listed | where: "evidence_level", lv -%}{%- assign lv_drugs = lv_drugs | concat: lv_part -%}{%- endfor -%}
{%- assign lv_L1 = lv_drugs | where: "evidence_level", "L1" | size -%}
{%- assign lv_L2 = lv_drugs | where: "evidence_level", "L2" | size -%}
<div id="high-evidence-list">
<p><em>{{ lv_drugs.size }} drugs (L1: {{ lv_L1 }}, L2: {{ lv_L2 }}).</em></p>
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
      // 讀不到 JSON 時保留建置時輸出的清單
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
