# Acarbose 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Acarbose | |
| DrugBank ID | DB00284 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | focal stiff limb syndrome | 99.65% | L5 | 0 | 0 | S0 | Hold |
| 2 | classic stiff person syndrome | 99.65% | L5 | 0 | 0 | S0 | Hold |
| 3 | thiamine-responsive dysfunction syndrome | 99.62% | L5 | 0 | 0 | S0 | Hold |
| 4 | opsismodysplasia | 99.62% | L5 | 0 | 0 | S0 | Hold |
| 5 | drug-induced localized lipodystrophy | 99.24% | L5 | 0 | 0 | S0 | Hold |
| 6 | centrifugal lipodystrophy | 99.22% | L5 | 0 | 0 | S0 | Hold |
| 7 | pressure-induced localized lipoatrophy | 99.20% | L5 | 0 | 0 | S0 | Hold |
| 8 | idiopathic localized lipodystrophy | 99.17% | L5 | 0 | 0 | S0 | Hold |
| 9 | pancreatic agenesis | 99.16% | L4 | 0 | 11 | S0 | Hold |
| 10 | type 1 diabetes mellitus | 98.39% | L2 | 50 | 20 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Acarbose | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Acarbose | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=focal stiff limb syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Acarbose, disease=focal stiff limb syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Acarbose, disease=focal stiff limb syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=classic stiff person syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Acarbose, disease=classic stiff person syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Acarbose, disease=classic stiff person syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=thiamine-responsive dysfunction syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Acarbose, disease=thiamine-responsive dysfunction syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Acarbose, disease=thiamine-responsive dysfunction syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=opsismodysplasia | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Acarbose, disease=opsismodysplasia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Acarbose, disease=opsismodysplasia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=drug-induced localized lipodystrophy | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Acarbose, disease=drug-induced localized lipodystrophy | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Acarbose, disease=drug-induced localized lipodystrophy | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=centrifugal lipodystrophy | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Acarbose, disease=centrifugal lipodystrophy | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Acarbose, disease=centrifugal lipodystrophy | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=pressure-induced localized lipoatrophy | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Acarbose, disease=pressure-induced localized lipoatrophy | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Acarbose, disease=pressure-induced localized lipoatrophy | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=idiopathic localized lipodystrophy | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Acarbose, disease=idiopathic localized lipodystrophy | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Acarbose, disease=idiopathic localized lipodystrophy | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=pancreatic agenesis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Acarbose, disease=pancreatic agenesis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Acarbose, disease=pancreatic agenesis | success | 11 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Acarbose, disease=type 1 diabetes mellitus | success | 50 |  |
| 31 | ictrp | 2026-03-10 | drug=Acarbose, disease=type 1 diabetes mellitus | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Acarbose, disease=type 1 diabetes mellitus | success | 20 |  |