# Fusidic acid 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Fusidic acid | |
| DrugBank ID | DB02703 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | exposure keratitis | 99.95% | L4 | 0 | 1 | S1 | Research Question |
| 2 | non-human animal disease | 99.86% | L5 | 0 | 0 | S0 | Hold |
| 3 | otitis externa | 99.84% | L4 | 0 | 6 | S1 | Research Question |
| 4 | postinfectious vasculitis | 99.83% | L5 | 0 | 0 | S0 | Hold |
| 5 | post-bacterial disorder | 99.82% | L1 | 2 | 0 | S3 | Proceed with Guardrails |
| 6 | post-infectious syndrome | 99.82% | L5 | 0 | 0 | S0 | Hold |
| 7 | infective urethral stricture | 99.81% | L5 | 0 | 0 | S0 | Hold |
| 8 | Chagas cardiomyopathy | 99.80% | L5 | 0 | 0 | S0 | Hold |
| 9 | infection-related hemolytic uremic syndrome | 99.79% | L5 | 0 | 0 | S0 | Hold |
| 10 | parasitic eyelid infestation | 99.65% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Fusidic acid | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Fusidic acid | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=exposure keratitis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=exposure keratitis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=exposure keratitis | success | 1 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=non-human animal disease | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=non-human animal disease | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=non-human animal disease | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=otitis externa | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=otitis externa | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=otitis externa | success | 6 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=postinfectious vasculitis | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=postinfectious vasculitis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=postinfectious vasculitis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=post-bacterial disorder | success | 2 |  |
| 16 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=post-bacterial disorder | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=post-bacterial disorder | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=post-infectious syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=post-infectious syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=post-infectious syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=infective urethral stricture | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=infective urethral stricture | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=infective urethral stricture | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=Chagas cardiomyopathy | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=Chagas cardiomyopathy | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=Chagas cardiomyopathy | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=infection-related hemolytic uremic syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=infection-related hemolytic uremic syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=infection-related hemolytic uremic syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Fusidic acid, disease=parasitic eyelid infestation | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Fusidic acid, disease=parasitic eyelid infestation | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Fusidic acid, disease=parasitic eyelid infestation | success | 0 |  |