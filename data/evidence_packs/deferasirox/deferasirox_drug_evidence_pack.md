# Deferasirox 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Deferasirox | |
| DrugBank ID | DB01609 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | HIV infectious disease | 99.40% | L4 | 0 | 2 | S1 | Research Question |
| 2 | chronic hepatitis C virus infection | 99.39% | L4 | 0 | 3 | S1 | Research Question |
| 3 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.23% | L5 | 0 | 0 | S0 | Hold |
| 4 | obsolete familial combined hyperlipidemia | 99.20% | L5 | 0 | 0 | S0 | Hold |
| 5 | dermatofibrosarcoma protuberans | 99.11% | L5 | 0 | 0 | S0 | Hold |
| 6 | simian immunodeficiency virus infection | 98.96% | L5 | 0 | 0 | S0 | Hold |
| 7 | feline acquired immunodeficiency syndrome | 98.96% | L5 | 0 | 0 | S0 | Hold |
| 8 | beta-thalassemia with other manifestations | 98.59% | L1 | 0 | 0 | S3 | Proceed with Guardrails |
| 9 | pyropoikilocytosis, hereditary | 98.55% | L5 | 0 | 0 | S0 | Hold |
| 10 | pyruvate kinase deficiency of red cells | 98.50% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Deferasirox | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Deferasirox | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=HIV infectious disease | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Deferasirox, disease=HIV infectious disease | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Deferasirox, disease=HIV infectious disease | success | 2 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=chronic hepatitis C virus infection | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Deferasirox, disease=chronic hepatitis C virus infection | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Deferasirox, disease=chronic hepatitis C virus infection | success | 3 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Deferasirox, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Deferasirox, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Deferasirox, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Deferasirox, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Deferasirox, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Deferasirox, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=simian immunodeficiency virus infection | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Deferasirox, disease=simian immunodeficiency virus infection | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Deferasirox, disease=simian immunodeficiency virus infection | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Deferasirox, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Deferasirox, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=beta-thalassemia with other manifestations | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Deferasirox, disease=beta-thalassemia with other manifestations | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Deferasirox, disease=beta-thalassemia with other manifestations | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=pyropoikilocytosis, hereditary | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Deferasirox, disease=pyropoikilocytosis, hereditary | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Deferasirox, disease=pyropoikilocytosis, hereditary | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Deferasirox, disease=pyruvate kinase deficiency of red cells | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Deferasirox, disease=pyruvate kinase deficiency of red cells | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Deferasirox, disease=pyruvate kinase deficiency of red cells | success | 0 |  |