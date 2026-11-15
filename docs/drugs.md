---
layout: default
title: Drug List
nav_order: 4
description: "Complete list of Singapore HSA-approved drugs with repurposing predictions"
permalink: /drugs/
---
{%- comment -%}2026-10-27 build gate：站上各頁的藥物數讀 site.data.drug_stats；它和實際公開藥物頁數／等級分布不一致時，
故意 include 不存在的檔讓 Jekyll 建置失敗，錯誤訊息即修法。{%- endcomment -%}
{%- assign gate_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign gate_ds = site.data.drug_stats -%}
{%- assign gate_l1 = gate_listed | where: "evidence_level", "L1" | size -%}
{%- assign gate_l2 = gate_listed | where: "evidence_level", "L2" | size -%}
{%- assign gate_l3 = gate_listed | where: "evidence_level", "L3" | size -%}
{%- assign gate_l4 = gate_listed | where: "evidence_level", "L4" | size -%}
{%- assign gate_l5 = gate_listed | where: "evidence_level", "L5" | size -%}
{%- if gate_listed.size != gate_ds.total_drugs or gate_l1 != gate_ds.level_counts.L1 or gate_l2 != gate_ds.level_counts.L2 or gate_l3 != gate_ds.level_counts.L3 or gate_l4 != gate_ds.level_counts.L4 or gate_l5 != gate_ds.level_counts.L5 -%}
{% include ERROR-docs-data-drug_stats-json-out-of-sync--run-python3-scripts-generate_drug_stats-py.html %}
{%- endif %}

# Drug List
{: .fs-9 }

Browse all {{ site.data.site_stats.drugs }} drugs with repurposing predictions
{: .fs-6 .fw-300 }

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
This list is based on the registration data of [HSA](https://www.hsa.gov.sg/) (Singapore).

<!-- local-home:end -->

Shortlist: [Singapore medicines with clinical-trial evidence for a new indication]({{ '/clinical-trial-evidence/' | relative_url }}) (L1–L2, with the predicted indication and the number of registered trials cited).

## Search & Filter

<div class="drug-search-container">
  <input type="text" id="drug-search" placeholder="Search by drug name..." class="drug-search-input">
  <div class="drug-filters">
    <label>
      <input type="checkbox" id="filter-highscore"> High Score (>0.99)
    </label>
  </div>
</div>

{% comment %}2026-11-14：清單在建置時就輸出成 HTML（無 JS 也看得到、爬得到全部藥物頁連結）；下方 JS 只做搜尋／篩選並補上最高分。{%- endcomment -%}
{%- assign list_drugs = gate_listed | sort: "title" %}
<p id="drug-count" class="drug-count">Showing {{ list_drugs.size }} of {{ list_drugs.size }} drugs</p>

<div id="drug-list" class="drug-list">
{%- for drug in list_drugs %}
<div class="drug-card"><a href="{{ drug.url | relative_url }}" class="drug-name">{{ drug.title | escape }}</a><div class="drug-meta"><span class="drug-id">{{ drug.evidence_level | escape }}</span><span class="drug-predictions">{{ drug.indication_count | default: 0 }} predicted indications</span></div></div>
{%- endfor %}
</div>

<script>
// 2026-11-06：清單改讀 /data/drugs.json（只收公開藥物頁，等級＝頁首）與 /data/search-index.json（各藥預測適應症與分數）。
// 舊版讀 drugbank_id、prediction_count、has_kgdl、max_score，這幾個欄位 drugs.json 都沒有：清單顯示 undefined、
// 打字搜尋會出錯、「KG+DL Only」一勾就空白。公開資料沒有每個藥的 KG+DL 來源，所以拿掉那個篩選。
document.addEventListener('DOMContentLoaded', function() {
  const base = '{{ "/" | relative_url }}'.replace(/\/$/, '');
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
  Promise.all([
    fetch('{{ "/data/drugs.json" | relative_url }}').then(r => r.json()),
    fetch('{{ "/data/search-index.json" | relative_url }}').then(r => r.json()).catch(() => ({drugs: []}))
  ]).then(([data, index]) => {
    const top = {};
    (index.drugs || []).forEach(d => {
      top[d.slug] = Math.max(0, ...(d.indications || []).map(i => Number(i.score) || 0));
    });
    // Statistics 表「分數 > 0.99」列：只數 drugs.json 裡（公開藥物頁）的藥的預測。
    const listed = new Set((data.drugs || []).map(d => d.slug));
    const statHs = document.getElementById('stat-highscore-pairs');
    if (statHs && (index.drugs || []).length) {
      const n = (index.drugs || []).filter(d => listed.has(d.slug))
        .reduce((s, d) => s + (d.indications || []).filter(i => Number(i.score) > 99).length, 0);
      statHs.textContent = n.toLocaleString('en-US');
    }
    const all = (data.drugs || []).map(d => Object.assign({}, d, {top_score: top[d.slug] || 0}))
      .sort((a, b) => String(a.name).localeCompare(String(b.name)));
    const container = document.getElementById('drug-list');
    const counter = document.getElementById('drug-count');
    const searchInput = document.getElementById('drug-search');
    const filterHighscore = document.getElementById('filter-highscore');

    function renderDrugs(drugs) {
      counter.textContent = `Showing ${drugs.length} of ${all.length} drugs`;
      if (drugs.length === 0) {
        container.innerHTML = '<p class="no-results">No drugs found matching your criteria.</p>';
        return;
      }
      container.innerHTML = drugs.map(drug => `
          <div class="drug-card">
            <a href="${esc(base + drug.url)}" class="drug-name">${esc(drug.name)}</a>
            <div class="drug-meta">
              <span class="drug-id">${esc(drug.evidence_level)}</span>
              <span class="drug-predictions">${Number(drug.indication_count) || 0} predicted indications</span>
              ${drug.top_score > 0 ? `<span class="drug-score">top score ${drug.top_score.toFixed(2)}%</span>` : ''}
              ${drug.top_score > 99 ? '<span class="badge highscore">High Score</span>' : ''}
            </div>
          </div>
        `).join('');
    }

    function filterDrugs() {
      const query = searchInput.value.trim().toLowerCase();
      let filtered = all;
      if (query) {
        filtered = filtered.filter(d => String(d.name).toLowerCase().includes(query) || String(d.slug).includes(query));
      }
      if (filterHighscore.checked) {
        filtered = filtered.filter(d => d.top_score > 99);
      }
      renderDrugs(filtered);
    }

    searchInput.addEventListener('input', filterDrugs);
    filterHighscore.addEventListener('change', filterDrugs);
    filterHighscore.checked = false;
    renderDrugs(all);
  }).catch(err => {
    // 讀不到 JSON 時保留建置時輸出的清單
  });
});
</script>

<style>
.drug-search-container {
  margin-bottom: 1.5rem;
}
.drug-search-input {
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-bottom: 0.5rem;
}
.drug-filters {
  display: flex;
  gap: 1rem;
}
.drug-filters label {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.9rem;
}
.drug-list {
  display: grid;
  gap: 0.75rem;
}
.drug-card {
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 3px solid #1a5276;
}
.drug-name {
  font-weight: 600;
  font-size: 1.1rem;
  color: #1a5276;
  text-decoration: none;
}
.drug-name:hover {
  text-decoration: underline;
}
.drug-meta {
  margin-top: 0.5rem;
  display: flex;
  gap: 0.75rem;
  font-size: 0.85rem;
  color: #666;
}
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
.badge.highscore {
  background: #FB8C00;
  color: white;
}
.drug-count {
  font-size: 0.9rem;
  color: #666;
}
.no-results, .error {
  padding: 2rem;
  text-align: center;
  color: #666;
}
</style>

---

## Statistics

{%- comment -%}2026-11-06：數字改由資料算，口徑＝本站公開的藥物頁（同 docs/_data/drug_stats.json、/data/drugs.json）。
舊版寫死 31,543／1,217／6,361，是 2026-03 版 drugs-by-level.json 的全量預測（含沒有公開頁的藥、含 KG 已知用途），口徑不同；
該檔 2026-11-06 起由 scripts/generate_download_data.py 從公開藥物頁重產。
公開資料沒有每筆預測的 KG／DL 來源，所以拿掉 KG+DL 列。分數 > 0.99 這列由下方 JS 讀 /data/search-index.json 算。{%- endcomment -%}
{%- assign stat_pairs = 0 -%}
{%- for d in site.data.drug_stats.all_drugs -%}{%- assign stat_pairs = stat_pairs | plus: d.indication_count -%}{%- endfor -%}
{%- assign stat_with_pred = site.data.drug_stats.all_drugs | where_exp: "d", "d.indication_count > 0" | size -%}
{%- capture stat_pairs_fmt -%}{%- if stat_pairs >= 1000 -%}{{ stat_pairs | divided_by: 1000 }},{{ stat_pairs | modulo: 1000 | prepend: '00' | slice: -3, 3 }}{%- else -%}{{ stat_pairs }}{%- endif -%}{%- endcapture %}

| Metric | Value |
|--------|-------|
| Drugs with a public page on this site | {{ site.data.drug_stats.total_drugs }} |
| Of these, drugs with at least one predicted new indication | {{ stat_with_pred }} |
| Predicted new indications listed on these drug pages (drug–indication pairs) | {{ stat_pairs_fmt }} |
| Of these pairs, TxGNN model score above 0.99 | <span id="stat-highscore-pairs">—</span> |

---

## Download

- [drugs.json]({{ '/data/drugs.json' | relative_url }}) - JSON format
- [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) - CSV format
