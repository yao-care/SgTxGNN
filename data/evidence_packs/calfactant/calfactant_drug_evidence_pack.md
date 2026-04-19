# Calfactant 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Calfactant | |
| DrugBank ID | DB06415 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | adult acute respiratory distress syndrome | 95.78% | L1 | 1 | 7 | S2 | Hold |
| 2 | neurolymphomatosis | 80.78% | L5 | 0 | 0 | S0 | Hold |
| 3 | pulmonary edema | 76.17% | L3 | 1 | 0 | S1 | Research Question |
| 4 | plasmacytoma | 73.72% | L5 | 0 | 0 | S0 | Hold |
| 5 | adult-onset myasthenia gravis | 73.55% | L5 | 0 | 0 | S0 | Hold |
| 6 | autoimmune disease of peripheral nervous system | 71.17% | L5 | 0 | 0 | S0 | Hold |
| 7 | atypical hemolytic-uremic syndrome with B factor anomaly | 70.76% | L5 | 0 | 0 | S0 | Hold |
| 8 | neonatal myasthenia gravis | 70.71% | L5 | 0 | 0 | S0 | Hold |
| 9 | disease of receptor activity | 70.46% | L5 | 0 | 0 | S0 | Hold |
| 10 | myasthenia gravis with thymus hyperplasia | 69.26% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Calfactant | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Calfactant | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=adult acute respiratory distress syndrome | success | 1 |  |
| 4 | ictrp | 2026-03-10 | drug=Calfactant, disease=adult acute respiratory distress syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Calfactant, disease=adult acute respiratory distress syndrome | success | 7 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=neurolymphomatosis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Calfactant, disease=neurolymphomatosis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Calfactant, disease=neurolymphomatosis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=pulmonary edema | success | 1 |  |
| 10 | ictrp | 2026-03-10 | drug=Calfactant, disease=pulmonary edema | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Calfactant, disease=pulmonary edema | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=plasmacytoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Calfactant, disease=plasmacytoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Calfactant, disease=plasmacytoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=adult-onset myasthenia gravis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Calfactant, disease=adult-onset myasthenia gravis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Calfactant, disease=adult-onset myasthenia gravis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=autoimmune disease of peripheral nervous system | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Calfactant, disease=autoimmune disease of peripheral nervous system | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Calfactant, disease=autoimmune disease of peripheral nervous system | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=atypical hemolytic-uremic syndrome with B factor anomaly | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Calfactant, disease=atypical hemolytic-uremic syndrome with B factor anomaly | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Calfactant, disease=atypical hemolytic-uremic syndrome with B factor anomaly | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=neonatal myasthenia gravis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Calfactant, disease=neonatal myasthenia gravis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Calfactant, disease=neonatal myasthenia gravis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=disease of receptor activity | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Calfactant, disease=disease of receptor activity | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Calfactant, disease=disease of receptor activity | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Calfactant, disease=myasthenia gravis with thymus hyperplasia | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Calfactant, disease=myasthenia gravis with thymus hyperplasia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Calfactant, disease=myasthenia gravis with thymus hyperplasia | success | 0 |  |