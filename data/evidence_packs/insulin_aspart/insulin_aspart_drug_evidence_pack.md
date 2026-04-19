# Insulin aspart 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Insulin aspart | |
| DrugBank ID | DB01306 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | type 1 diabetes mellitus | 99.95% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 2 | autoimmune oophoritis | 99.92% | L5 | 0 | 0 | S0 | Hold |
| 3 | opsismodysplasia | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 4 | thiamine-responsive dysfunction syndrome | 99.57% | L5 | 0 | 0 | S0 | Hold |
| 5 | permanent neonatal diabetes mellitus | 99.55% | L4 | 0 | 1 | S1 | Research Question |
| 6 | focal stiff limb syndrome | 99.51% | L5 | 0 | 0 | S0 | Hold |
| 7 | classic stiff person syndrome | 99.51% | L5 | 0 | 0 | S0 | Hold |
| 8 | pancreatic agenesis | 99.44% | L4 | 0 | 2 | S1 | Research Question |
| 9 | drug-induced localized lipodystrophy | 99.35% | L5 | 0 | 0 | S0 | Hold |
| 10 | centrifugal lipodystrophy | 99.32% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Insulin aspart | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Insulin aspart | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=type 1 diabetes mellitus | success | 50 |  |
| 4 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=type 1 diabetes mellitus | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=type 1 diabetes mellitus | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=autoimmune oophoritis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=autoimmune oophoritis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=autoimmune oophoritis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=opsismodysplasia | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=opsismodysplasia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=opsismodysplasia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=thiamine-responsive dysfunction syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=thiamine-responsive dysfunction syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=thiamine-responsive dysfunction syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=permanent neonatal diabetes mellitus | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=permanent neonatal diabetes mellitus | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=permanent neonatal diabetes mellitus | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=focal stiff limb syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=focal stiff limb syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=focal stiff limb syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=classic stiff person syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=classic stiff person syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=classic stiff person syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=pancreatic agenesis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=pancreatic agenesis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=pancreatic agenesis | success | 2 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=drug-induced localized lipodystrophy | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=drug-induced localized lipodystrophy | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=drug-induced localized lipodystrophy | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Insulin aspart, disease=centrifugal lipodystrophy | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Insulin aspart, disease=centrifugal lipodystrophy | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Insulin aspart, disease=centrifugal lipodystrophy | success | 0 |  |