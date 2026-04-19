# Calcium chloride 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Calcium chloride | |
| DrugBank ID | DB01164 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | dyspepsia | 97.47% | L5 | 10 | 5 | S0 | Hold |
| 2 | calcium-alkali syndrome | 96.05% | L4 | 20 | 3 | S0 | Hold |
| 3 | primary bone dysplasia with defective bone mineralization | 95.77% | L5 | 0 | 0 | S0 | Hold |
| 4 | gastroparesis (disease) | 93.86% | pending | 6 | 0 | pending | pending |
| 5 | gastroduodenitis | 93.02% | L4 | 0 | 2 | S0 | Hold |
| 6 | stomach disease | 91.54% | L4 | 50 | 20 | S1 | Research Question |
| 7 | congenital prothrombin deficiency | 85.98% | L4 | 3 | 0 | S1 | Research Question |
| 8 | hypophosphatemia (disease) | 83.94% | pending | 8 | 20 | pending | pending |
| 9 | esophageal varices without bleeding | 75.97% | L5 | 1 | 0 | S0 | Hold |
| 10 | esophageal varices with bleeding | 75.97% | L5 | 1 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Calcium chloride | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Calcium chloride | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=dyspepsia | success | 10 |  |
| 4 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=dyspepsia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=dyspepsia | success | 5 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=calcium-alkali syndrome | success | 20 |  |
| 7 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=calcium-alkali syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=calcium-alkali syndrome | success | 3 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=primary bone dysplasia with defective bone mineralization | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=primary bone dysplasia with defective bone mineralization | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=primary bone dysplasia with defective bone mineralization | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=gastroparesis (disease) | success | 6 |  |
| 13 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=gastroparesis (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=gastroparesis (disease) | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=gastroduodenitis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=gastroduodenitis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=gastroduodenitis | success | 2 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=stomach disease | success | 50 |  |
| 19 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=stomach disease | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=stomach disease | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=congenital prothrombin deficiency | success | 3 |  |
| 22 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=congenital prothrombin deficiency | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=congenital prothrombin deficiency | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=hypophosphatemia (disease) | success | 8 |  |
| 25 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=hypophosphatemia (disease) | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=hypophosphatemia (disease) | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=esophageal varices without bleeding | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=esophageal varices without bleeding | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=esophageal varices without bleeding | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Calcium chloride, disease=esophageal varices with bleeding | success | 1 |  |
| 31 | ictrp | 2026-03-10 | drug=Calcium chloride, disease=esophageal varices with bleeding | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Calcium chloride, disease=esophageal varices with bleeding | success | 0 |  |