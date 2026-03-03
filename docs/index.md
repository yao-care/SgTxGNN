---
layout: default
title: Drug Repurposing Reports
nav_order: 1
description: "AI-powered drug repurposing predictions for Singapore HSA-approved medications. 745 drugs with clinical trial and literature evidence validation. L1-L5 evidence classification."
permalink: /
image: /assets/images/og-default.png
---

# Drug Repurposing: From Data to Evidence

<p class="key-answer" data-question="What is SgTxGNN Drug Repurposing Reports?">
<strong>SgTxGNN</strong> is a drug repurposing prediction platform based on Harvard's TxGNN model. We use AI to predict <strong>31,543</strong> drug repurposing candidates and provide evidence-based validation reports for <strong>745</strong> Singapore HSA-approved medications.
</p>

<div class="key-takeaway">
Not just "possibly effective" — we show you where the evidence is. L1-L5 evidence classification helps researchers quickly assess prediction credibility.
</div>

<p style="margin-top: 1.5rem;">
  <a href="{{ '/evidence-high' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #2E7D32; color: white; text-decoration: none; border-radius: 4px; font-weight: 600; margin-right: 0.5rem;">Browse High Evidence Drugs</a>
  <a href="{{ '/methodology' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #f5f5f5; color: #333; text-decoration: none; border-radius: 4px; font-weight: 500;">Learn Methodology</a>
</p>

---

## Drug Search

<p class="key-answer" data-question="How do I search for drug repurposing possibilities?">
Enter a <strong>drug name</strong> or <strong>disease name</strong> to search for repurposing possibilities and clinical evidence. Supports generic names, brand names, and disease keywords.
</p>

<div class="drug-lookup-container">
  <div class="lookup-search-box">
    <div class="lookup-input-wrapper">
      <input type="text" id="lookup-input" placeholder="Enter drug name or disease name..." autocomplete="off">
      <button id="lookup-clear" class="lookup-clear-btn" style="display: none;">✕</button>
    </div>
    <button id="lookup-search" class="lookup-search-btn">Search</button>
  </div>
  <div class="lookup-filters">
    <span class="filter-label">Evidence Level:</span>
    <label><input type="checkbox" class="level-filter" value="L1" checked> L1</label>
    <label><input type="checkbox" class="level-filter" value="L2" checked> L2</label>
    <label><input type="checkbox" class="level-filter" value="L3" checked> L3</label>
    <label><input type="checkbox" class="level-filter" value="L4"> L4</label>
    <label><input type="checkbox" class="level-filter" value="L5"> L5</label>
  </div>
  <div id="lookup-results" class="lookup-results"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0"></script>
<script>
  window.SGTXGNN_CONFIG = {
    searchIndexUrl: '{{ "/data/search-index.json" | relative_url }}',
    drugsBaseUrl: '{{ "/drugs/" | relative_url }}'
  };
</script>
<script src="{{ '/assets/js/drug-lookup.js' | relative_url }}"></script>

---

## What Makes Us Different

<p class="key-answer" data-question="How is SgTxGNN different from other prediction tools?">
Most drug repurposing tools only provide "possibly effective" scores. SgTxGNN integrates ClinicalTrials.gov, PubMed literature, drug interactions, and more — with L1-L5 evidence classification to show which predictions are worth pursuing.
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2E7D32;">
    <strong style="font-size: 1.1rem;">From Prediction to Evidence</strong><br>
    <span style="color: #666;">Each report integrates clinical trial IDs (NCT), literature indices (PMID), and Singapore HSA license information with complete evidence traceability.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1976D2;">
    <strong style="font-size: 1.1rem;">Five-Level Evidence Classification</strong><br>
    <span style="color: #666;">L1 (Multiple Phase 3 RCTs) to L5 (Model prediction only) with Go / Proceed / Hold recommendations for quick candidate screening.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #FB8C00;">
    <strong style="font-size: 1.1rem;">Singapore HSA Coverage</strong><br>
    <span style="color: #666;">Focused on HSA-registered medications covering 745 drugs and 4,589 predicted indications. Reports include Singapore license status.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #9B59B6;">
    <strong style="font-size: 1.1rem;">Dual Validation (KG+DL)</strong><br>
    <span style="color: #666;">1,217 predictions validated by both Knowledge Graph and Deep Learning methods, providing higher confidence for prioritization.</span>
  </div>
</div>

---

## Key Statistics

<style>
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}
.stat-card {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  text-align: center;
}
.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #1a5276;
}
.stat-label {
  font-size: 0.9rem;
  color: #666;
}
</style>

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-number">745</div>
    <div class="stat-label">Drugs Analyzed</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">31,543</div>
    <div class="stat-label">Repurposing Candidates</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">4,589</div>
    <div class="stat-label">Diseases Covered</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">1,217</div>
    <div class="stat-label">Dual Validated (KG+DL)</div>
  </div>
</div>

---

## Prediction Sources

| Source | Count | Description |
|--------|-------|-------------|
| **KG+DL** | 1,217 | Both Knowledge Graph and Deep Learning agree — highest confidence |
| **DL** | 27,883 | Deep Learning predictions with confidence scores |
| **KG** | 2,443 | Knowledge Graph predictions based on biological relationships |

---

## Quick Navigation

| Category | Description | Link |
|----------|-------------|------|
| **High Evidence** | L1-L2, prioritize for evaluation | [View Drugs]({{ '/evidence-high' | relative_url }}) |
| **Medium Evidence** | L3-L4, needs additional evidence | [View Drugs]({{ '/evidence-medium' | relative_url }}) |
| **Predictions Only** | L5, research direction reference | [View Drugs]({{ '/evidence-low' | relative_url }}) |
| **Full Drug List** | All 745 drugs (searchable) | [Drug List]({{ '/drugs' | relative_url }}) |
| **Methodology** | How predictions are made | [Methodology]({{ '/methodology' | relative_url }}) |
| **Downloads** | CSV / JSON formats | [Downloads]({{ '/downloads' | relative_url }}) |

---

## About This Project

<p class="key-answer" data-question="What technology does SgTxGNN use?">
This system uses Harvard Zitnik Lab's <a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> deep learning model published in <em>Nature Medicine</em> to predict potential new indications for Singapore HSA-approved medications.
</p>

<blockquote class="expert-quote">
"TxGNN is the first foundation model designed for clinician-centered drug repurposing, integrating knowledge graphs and deep learning to predict drug efficacy for rare diseases."
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

[Learn More]({{ '/about' | relative_url }}) | [View Methodology]({{ '/methodology' | relative_url }}) | [Data Sources]({{ '/sources' | relative_url }})

---

## Data Sources

<style>
.data-source-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 12px;
}
.data-source-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.25rem 1rem;
  background: white;
  border-radius: 10px;
  text-decoration: none;
  color: #333;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s, box-shadow 0.2s;
}
.data-source-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}
</style>

<div class="data-source-grid">
  <a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #A51C30;">TxGNN</strong>
    <small>Harvard Zitnik Lab</small>
  </a>
  <a href="https://clinicaltrials.gov/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #205493;">ClinicalTrials.gov</strong>
    <small>NIH Clinical Trials</small>
  </a>
  <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #326599;">PubMed</strong>
    <small>Biomedical Literature</small>
  </a>
  <a href="https://go.drugbank.com/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #E74C3C;">DrugBank</strong>
    <small>Drug Database</small>
  </a>
  <a href="https://www.hsa.gov.sg/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #00A651;">Singapore HSA</strong>
    <small>Health Sciences Authority</small>
  </a>
</div>

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research purposes only and <strong>does not constitute medical advice</strong>. Please follow physician instructions for medication use. Any drug repurposing decisions require complete clinical validation and regulatory approval.
<br><br>
<small>Last Review: 2026-03-03 | Reviewer: SgTxGNN Research Team</small>
</div>
