---
layout: default
title: Drug List
nav_order: 2
description: "Complete list of 745 Singapore HSA-approved drugs with repurposing predictions"
permalink: /drugs/
---

# Drug List
{: .fs-9 }

Browse all 745 drugs with repurposing predictions
{: .fs-6 .fw-300 }

---

## Search & Filter

<div class="drug-search-container">
  <input type="text" id="drug-search" placeholder="Search by drug name..." class="drug-search-input">
  <div class="drug-filters">
    <label>
      <input type="checkbox" id="filter-kgdl" checked> KG+DL Only
    </label>
    <label>
      <input type="checkbox" id="filter-highscore"> High Score (>0.99)
    </label>
  </div>
</div>

<div id="drug-list" class="drug-list">
  Loading drugs...
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  fetch('{{ "/data/drugs.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('drug-list');
      const searchInput = document.getElementById('drug-search');
      const filterKgdl = document.getElementById('filter-kgdl');
      const filterHighscore = document.getElementById('filter-highscore');

      function renderDrugs(drugs) {
        if (drugs.length === 0) {
          container.innerHTML = '<p class="no-results">No drugs found matching your criteria.</p>';
          return;
        }

        container.innerHTML = drugs.map(drug => `
          <div class="drug-card">
            <a href="${drug.url}" class="drug-name">${drug.name}</a>
            <div class="drug-meta">
              <span class="drug-id">${drug.drugbank_id}</span>
              <span class="drug-predictions">${drug.prediction_count} predictions</span>
              ${drug.has_kgdl ? '<span class="badge kgdl">KG+DL</span>' : ''}
              ${drug.max_score > 0.99 ? '<span class="badge highscore">High Score</span>' : ''}
            </div>
          </div>
        `).join('');
      }

      function filterDrugs() {
        const query = searchInput.value.toLowerCase();
        const kgdlOnly = filterKgdl.checked;
        const highscoreOnly = filterHighscore.checked;

        let filtered = data.drugs;

        if (query) {
          filtered = filtered.filter(d =>
            d.name.toLowerCase().includes(query) ||
            d.drugbank_id.toLowerCase().includes(query)
          );
        }

        if (kgdlOnly) {
          filtered = filtered.filter(d => d.has_kgdl);
        }

        if (highscoreOnly) {
          filtered = filtered.filter(d => d.max_score > 0.99);
        }

        renderDrugs(filtered);
      }

      searchInput.addEventListener('input', filterDrugs);
      filterKgdl.addEventListener('change', filterDrugs);
      filterHighscore.addEventListener('change', filterDrugs);

      // Initial render (no filters)
      filterKgdl.checked = false;
      filterHighscore.checked = false;
      renderDrugs(data.drugs);
    })
    .catch(err => {
      document.getElementById('drug-list').innerHTML = '<p class="error">Failed to load drug data.</p>';
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
.no-results, .error {
  padding: 2rem;
  text-align: center;
  color: #666;
}
</style>

---

## Statistics

| Metric | Value |
|--------|-------|
| Total Drugs | 745 |
| Total Predictions | 31,543 |
| KG+DL Validated | 1,217 |
| High Score (>0.99) | 6,361 |

---

## Download

- [drugs.json]({{ '/data/drugs.json' | relative_url }}) - JSON format
- [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) - CSV format
