# Calcium gluconate 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Calcium gluconate | |
| DrugBank ID | DB11126 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | calcium-alkali syndrome | 98.88% | L5 | 42 | 0 | S0 | Hold |
| 2 | primary bone dysplasia with defective bone mineralization | 98.70% | L5 | 0 | 0 | S0 | Hold |
| 3 | dyspepsia | 90.12% | L4 | 32 | 2 | S0 | Hold |
| 4 | hypophosphatemia (disease) | 89.98% | L3 | 50 | 6 | S1 | Research Question |
| 5 | potassium deficiency disease | 84.52% | L4 | 50 | 3 | S0 | Hold |
| 6 | duodenal ulcer (disease) | 73.94% | L3 | 5 | 8 | S1 | Hold |
| 7 | duodenal obstruction | 72.96% | L5 | 1 | 1 | S0 | Hold |
| 8 | hyperlipidemia | 72.94% | L5 | 50 | 4 | S0 | Hold |
| 9 | urolithiasis | 72.90% | L4 | 50 | 20 | S0 | Hold |
| 10 | duodenogastric reflux | 70.51% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Calcium gluconate | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Calcium gluconate | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=calcium-alkali syndrome | success | 42 |  |
| 4 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=calcium-alkali syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=calcium-alkali syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=primary bone dysplasia with defective bone mineralization | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=primary bone dysplasia with defective bone mineralization | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=primary bone dysplasia with defective bone mineralization | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=dyspepsia | success | 32 |  |
| 10 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=dyspepsia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=dyspepsia | success | 2 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=hypophosphatemia (disease) | success | 50 |  |
| 13 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=hypophosphatemia (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=hypophosphatemia (disease) | success | 6 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=potassium deficiency disease | success | 50 |  |
| 16 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=potassium deficiency disease | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=potassium deficiency disease | success | 3 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=duodenal ulcer (disease) | success | 5 |  |
| 19 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=duodenal ulcer (disease) | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=duodenal ulcer (disease) | success | 8 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=duodenal obstruction | success | 1 |  |
| 22 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=duodenal obstruction | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=duodenal obstruction | success | 1 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=hyperlipidemia | success | 50 |  |
| 25 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=hyperlipidemia | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=hyperlipidemia | success | 4 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=urolithiasis | success | 50 |  |
| 28 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=urolithiasis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=urolithiasis | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Calcium gluconate, disease=duodenogastric reflux | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Calcium gluconate, disease=duodenogastric reflux | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Calcium gluconate, disease=duodenogastric reflux | success | 0 |  |