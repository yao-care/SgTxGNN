# Insulin glargine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Insulin glargine | |
| DrugBank ID | DB00047 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | autoimmune oophoritis | 99.88% | L5 | 0 | 0 | S0 | Hold |
| 2 | thiamine-responsive dysfunction syndrome | 99.61% | L4 | 0 | 0 | S0 | Hold |
| 3 | focal stiff limb syndrome | 99.60% | L4 | 0 | 0 | S0 | Hold |
| 4 | classic stiff person syndrome | 99.60% | L4 | 0 | 0 | S1 | Research Question |
| 5 | opsismodysplasia | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 6 | pancreatic agenesis | 99.43% | L3 | 0 | 6 | S2 | Proceed with Guardrails |
| 7 | drug-induced localized lipodystrophy | 99.42% | L5 | 0 | 0 | S0 | Hold |
| 8 | centrifugal lipodystrophy | 99.39% | L5 | 0 | 0 | S0 | Hold |
| 9 | pressure-induced localized lipoatrophy | 99.38% | L5 | 0 | 0 | S0 | Hold |
| 10 | idiopathic localized lipodystrophy | 99.34% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Insulin glargine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Insulin glargine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=autoimmune oophoritis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=autoimmune oophoritis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=autoimmune oophoritis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=thiamine-responsive dysfunction syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=thiamine-responsive dysfunction syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=thiamine-responsive dysfunction syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=focal stiff limb syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=focal stiff limb syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=focal stiff limb syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=classic stiff person syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=classic stiff person syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=classic stiff person syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=opsismodysplasia | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=opsismodysplasia | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=opsismodysplasia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=pancreatic agenesis | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=pancreatic agenesis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=pancreatic agenesis | success | 6 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=drug-induced localized lipodystrophy | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=drug-induced localized lipodystrophy | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=drug-induced localized lipodystrophy | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=centrifugal lipodystrophy | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=centrifugal lipodystrophy | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=centrifugal lipodystrophy | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=pressure-induced localized lipoatrophy | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=pressure-induced localized lipoatrophy | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=pressure-induced localized lipoatrophy | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Insulin glargine, disease=idiopathic localized lipodystrophy | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Insulin glargine, disease=idiopathic localized lipodystrophy | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Insulin glargine, disease=idiopathic localized lipodystrophy | success | 0 |  |