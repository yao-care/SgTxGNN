# Iron 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Iron | |
| DrugBank ID | DB01592 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | vitamin B12- and folate-independent constitutional megaloblastic anemia | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 2 | Plummer-Vinson syndrome | 99.89% | L3 | 0 | 19 | S3 | Proceed with Guardrails |
| 3 | non-syndromic esophageal malformation | 99.86% | L5 | 0 | 0 | S0 | Hold |
| 4 | biotin metabolic disease | 99.74% | L4 | 9 | 20 | S0 | Hold |
| 5 | vitamin deficiency disorder | 99.68% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 6 | esophageal disease | 99.42% | L3 | 35 | 20 | S2 | Research Question |
| 7 | injury | 98.56% | L4 | 50 | 20 | S1 | Research Question |
| 8 | florid cemento-osseous dysplasia | 98.04% | L5 | 0 | 0 | S0 | Hold |
| 9 | segmental odontomaxillary dysplasia | 98.04% | L5 | 0 | 0 | S0 | Hold |
| 10 | perinatal disease | 98.04% | L1 | 43 | 18 | S3 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Iron | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Iron | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Iron, disease=vitamin B12- and folate-independent constitutional megaloblastic anemia | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Iron, disease=vitamin B12- and folate-independent constitutional megaloblastic anemia | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Iron, disease=vitamin B12- and folate-independent constitutional megaloblastic anemia | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Iron, disease=Plummer-Vinson syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Iron, disease=Plummer-Vinson syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Iron, disease=Plummer-Vinson syndrome | success | 19 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Iron, disease=non-syndromic esophageal malformation | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Iron, disease=non-syndromic esophageal malformation | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Iron, disease=non-syndromic esophageal malformation | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Iron, disease=biotin metabolic disease | success | 9 |  |
| 13 | ictrp | 2026-03-09 | drug=Iron, disease=biotin metabolic disease | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Iron, disease=biotin metabolic disease | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Iron, disease=vitamin deficiency disorder | success | 50 |  |
| 16 | ictrp | 2026-03-09 | drug=Iron, disease=vitamin deficiency disorder | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Iron, disease=vitamin deficiency disorder | success | 20 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Iron, disease=esophageal disease | success | 35 |  |
| 19 | ictrp | 2026-03-09 | drug=Iron, disease=esophageal disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Iron, disease=esophageal disease | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Iron, disease=injury | success | 50 |  |
| 22 | ictrp | 2026-03-09 | drug=Iron, disease=injury | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Iron, disease=injury | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Iron, disease=florid cemento-osseous dysplasia | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Iron, disease=florid cemento-osseous dysplasia | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Iron, disease=florid cemento-osseous dysplasia | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Iron, disease=segmental odontomaxillary dysplasia | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Iron, disease=segmental odontomaxillary dysplasia | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Iron, disease=segmental odontomaxillary dysplasia | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Iron, disease=perinatal disease | success | 43 |  |
| 31 | ictrp | 2026-03-09 | drug=Iron, disease=perinatal disease | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Iron, disease=perinatal disease | success | 18 |  |