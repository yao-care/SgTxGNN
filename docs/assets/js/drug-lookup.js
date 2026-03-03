/**
 * SgTxGNN Drug Lookup Component
 * Fuzzy search for drugs and diseases
 */

(function() {
  'use strict';

  const CONFIG = window.SGTXGNN_CONFIG || {
    searchIndexUrl: '/data/search-index.json',
    drugsBaseUrl: '/drugs/'
  };

  let searchIndex = null;
  let fuse = null;

  // DOM elements
  const input = document.getElementById('lookup-input');
  const clearBtn = document.getElementById('lookup-clear');
  const searchBtn = document.getElementById('lookup-search');
  const resultsContainer = document.getElementById('lookup-results');
  const levelFilters = document.querySelectorAll('.level-filter');

  if (!input || !resultsContainer) {
    console.warn('Drug lookup elements not found');
    return;
  }

  // Load search index
  async function loadSearchIndex() {
    try {
      const response = await fetch(CONFIG.searchIndexUrl);
      const data = await response.json();
      searchIndex = data.entries;

      // Initialize Fuse.js
      fuse = new Fuse(searchIndex, {
        keys: ['drug', 'disease'],
        threshold: 0.3,
        includeScore: true,
        minMatchCharLength: 2
      });

      console.log(`Loaded ${searchIndex.length} search entries`);
    } catch (err) {
      console.error('Failed to load search index:', err);
      resultsContainer.innerHTML = '<p class="error">Failed to load search data.</p>';
    }
  }

  // Get selected evidence levels
  function getSelectedLevels() {
    const selected = [];
    levelFilters.forEach(filter => {
      if (filter.checked) {
        selected.push(filter.value);
      }
    });
    return selected;
  }

  // Map source to evidence level
  function sourceToLevel(source, score) {
    if (source === 'KG+DL') return 'L4';  // Dual validated
    if (score && score > 0.99) return 'L4';  // High confidence
    if (score && score > 0.95) return 'L5';
    return 'L5';
  }

  // Perform search
  function performSearch() {
    const query = input.value.trim();

    if (!query || query.length < 2) {
      resultsContainer.innerHTML = '<p class="hint">Enter at least 2 characters to search.</p>';
      return;
    }

    if (!fuse) {
      resultsContainer.innerHTML = '<p class="loading">Loading search index...</p>';
      return;
    }

    const results = fuse.search(query, { limit: 50 });
    const selectedLevels = getSelectedLevels();

    // Filter by evidence level
    const filtered = results.filter(r => {
      const level = sourceToLevel(r.item.source, r.item.score);
      return selectedLevels.includes(level);
    });

    if (filtered.length === 0) {
      resultsContainer.innerHTML = '<p class="no-results">No results found. Try different keywords or adjust filters.</p>';
      return;
    }

    // Group by drug
    const byDrug = {};
    filtered.forEach(r => {
      const drugId = r.item.drugbank_id;
      if (!byDrug[drugId]) {
        byDrug[drugId] = {
          drug: r.item.drug,
          drugbank_id: drugId,
          url: r.item.url,
          predictions: []
        };
      }
      byDrug[drugId].predictions.push({
        disease: r.item.disease,
        score: r.item.score,
        source: r.item.source
      });
    });

    // Render results
    const drugs = Object.values(byDrug).slice(0, 20);
    resultsContainer.innerHTML = `
      <div class="results-count">Found ${filtered.length} predictions in ${drugs.length} drugs</div>
      ${drugs.map(drug => `
        <div class="result-card">
          <a href="${drug.url}" class="drug-link">${drug.drug}</a>
          <span class="drug-id">${drug.drugbank_id}</span>
          <div class="predictions">
            ${drug.predictions.slice(0, 5).map(p => `
              <div class="prediction">
                <span class="disease">${p.disease}</span>
                ${p.score ? `<span class="score">${(p.score * 100).toFixed(1)}%</span>` : ''}
                <span class="source ${p.source.toLowerCase().replace('+', '-')}">${p.source}</span>
              </div>
            `).join('')}
            ${drug.predictions.length > 5 ? `<div class="more">+${drug.predictions.length - 5} more predictions</div>` : ''}
          </div>
        </div>
      `).join('')}
    `;
  }

  // Event listeners
  input.addEventListener('input', () => {
    clearBtn.style.display = input.value ? 'block' : 'none';
  });

  input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      performSearch();
    }
  });

  clearBtn.addEventListener('click', () => {
    input.value = '';
    clearBtn.style.display = 'none';
    resultsContainer.innerHTML = '';
  });

  searchBtn.addEventListener('click', performSearch);

  levelFilters.forEach(filter => {
    filter.addEventListener('change', performSearch);
  });

  // Add styles
  const style = document.createElement('style');
  style.textContent = `
    .drug-lookup-container {
      margin: 1.5rem 0;
    }
    .lookup-search-box {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }
    .lookup-input-wrapper {
      flex: 1;
      position: relative;
    }
    #lookup-input {
      width: 100%;
      padding: 0.75rem 2.5rem 0.75rem 0.75rem;
      font-size: 1rem;
      border: 2px solid #ddd;
      border-radius: 4px;
    }
    #lookup-input:focus {
      border-color: #1a5276;
      outline: none;
    }
    .lookup-clear-btn {
      position: absolute;
      right: 0.5rem;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      font-size: 1.2rem;
      cursor: pointer;
      color: #999;
    }
    .lookup-search-btn {
      padding: 0.75rem 1.5rem;
      background: #1a5276;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 600;
    }
    .lookup-search-btn:hover {
      background: #154360;
    }
    .lookup-filters {
      display: flex;
      gap: 1rem;
      font-size: 0.9rem;
    }
    .lookup-filters label {
      display: flex;
      align-items: center;
      gap: 0.25rem;
    }
    .lookup-results {
      margin-top: 1rem;
    }
    .results-count {
      font-size: 0.9rem;
      color: #666;
      margin-bottom: 1rem;
    }
    .result-card {
      padding: 1rem;
      background: #f8f9fa;
      border-radius: 8px;
      margin-bottom: 0.75rem;
      border-left: 3px solid #1a5276;
    }
    .drug-link {
      font-weight: 600;
      font-size: 1.1rem;
      color: #1a5276;
      text-decoration: none;
    }
    .drug-link:hover {
      text-decoration: underline;
    }
    .drug-id {
      font-size: 0.8rem;
      color: #999;
      margin-left: 0.5rem;
    }
    .predictions {
      margin-top: 0.75rem;
    }
    .prediction {
      display: flex;
      gap: 0.5rem;
      align-items: center;
      padding: 0.25rem 0;
      font-size: 0.9rem;
    }
    .disease {
      flex: 1;
    }
    .score {
      color: #666;
      font-size: 0.85rem;
    }
    .source {
      padding: 0.125rem 0.4rem;
      border-radius: 3px;
      font-size: 0.7rem;
      font-weight: 600;
    }
    .source.kg-dl {
      background: #2E7D32;
      color: white;
    }
    .source.dl {
      background: #1976D2;
      color: white;
    }
    .source.kg {
      background: #9E9E9E;
      color: white;
    }
    .more {
      font-size: 0.85rem;
      color: #666;
      font-style: italic;
      padding-top: 0.25rem;
    }
    .hint, .no-results, .loading, .error {
      padding: 1rem;
      text-align: center;
      color: #666;
    }
    .error {
      color: #c00;
    }
  `;
  document.head.appendChild(style);

  // Initialize
  loadSearchIndex();
})();
