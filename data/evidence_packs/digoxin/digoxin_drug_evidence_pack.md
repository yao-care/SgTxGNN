# Digoxin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Digoxin | |
| DrugBank ID | DB00390 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Prinzmetal angina | 99.81% | L4 | 0 | 2 | S0 | Hold |
| 2 | duodenal obstruction | 99.70% | L5 | 0 | 1 | S0 | Hold |
| 3 | duodenal ulcer (disease) | 99.59% | L5 | 0 | 5 | S0 | Hold |
| 4 | duodenogastric reflux | 99.53% | L5 | 0 | 0 | S0 | Hold |
| 5 | obsolete susceptibility to ischemic stroke | 99.29% | L5 | 0 | 0 | S0 | Hold |
| 6 | hypoalphalipoproteinemia | 99.20% | L5 | 0 | 0 | S0 | Hold |
| 7 | homozygous familial hypercholesterolemia | 98.98% | L5 | 0 | 0 | S0 | Hold |
| 8 | nephrogenic syndrome of inappropriate antidiuresis | 98.83% | L5 | 0 | 0 | S0 | Hold |
| 9 | thrombotic disease | 98.75% | L4 | 2 | 0 | S0 | Hold |
| 10 | stroke disorder | 98.19% | L3 | 23 | 20 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Digoxin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Digoxin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=Prinzmetal angina | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Digoxin, disease=Prinzmetal angina | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Digoxin, disease=Prinzmetal angina | success | 2 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=duodenal obstruction | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Digoxin, disease=duodenal obstruction | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Digoxin, disease=duodenal obstruction | success | 1 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=duodenal ulcer (disease) | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Digoxin, disease=duodenal ulcer (disease) | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Digoxin, disease=duodenal ulcer (disease) | success | 5 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=duodenogastric reflux | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Digoxin, disease=duodenogastric reflux | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Digoxin, disease=duodenogastric reflux | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=obsolete susceptibility to ischemic stroke | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Digoxin, disease=obsolete susceptibility to ischemic stroke | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Digoxin, disease=obsolete susceptibility to ischemic stroke | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=hypoalphalipoproteinemia | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Digoxin, disease=hypoalphalipoproteinemia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Digoxin, disease=hypoalphalipoproteinemia | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=homozygous familial hypercholesterolemia | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Digoxin, disease=homozygous familial hypercholesterolemia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Digoxin, disease=homozygous familial hypercholesterolemia | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Digoxin, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Digoxin, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=thrombotic disease | success | 2 |  |
| 28 | ictrp | 2026-03-09 | drug=Digoxin, disease=thrombotic disease | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Digoxin, disease=thrombotic disease | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Digoxin, disease=stroke disorder | success | 23 |  |
| 31 | ictrp | 2026-03-09 | drug=Digoxin, disease=stroke disorder | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Digoxin, disease=stroke disorder | success | 20 |  |