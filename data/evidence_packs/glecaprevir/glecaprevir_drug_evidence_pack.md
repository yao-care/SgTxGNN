# Glecaprevir 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Glecaprevir | |
| DrugBank ID | DB13879 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | HIV infectious disease | 99.87% | L4 | 15 | 20 | S1 | Hold |
| 2 | hepatitis B virus infection | 99.87% | L4 | 14 | 19 | S1 | Hold |
| 3 | feline acquired immunodeficiency syndrome | 99.81% | L5 | 0 | 0 | S0 | Hold |
| 4 | simian immunodeficiency virus infection | 99.81% | L5 | 0 | 0 | S0 | Hold |
| 5 | hepatitis E virus infection | 99.80% | L5 | 6 | 0 | S0 | Research Question |
| 6 | hepatitis, viral, animal | 99.80% | L4 | 0 | 3 | S0 | Hold |
| 7 | hepatitis A virus infection | 99.80% | L5 | 50 | 0 | S0 | Hold |
| 8 | Omsk hemorrhagic fever | 99.79% | L5 | 0 | 0 | S0 | Hold |
| 9 | Kyasanur forest disease | 99.79% | L5 | 0 | 0 | S0 | Hold |
| 10 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.77% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Glecaprevir | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Glecaprevir | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=HIV infectious disease | success | 15 |  |
| 4 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=HIV infectious disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=HIV infectious disease | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=hepatitis B virus infection | success | 14 |  |
| 7 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=hepatitis B virus infection | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=hepatitis B virus infection | success | 19 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=simian immunodeficiency virus infection | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=simian immunodeficiency virus infection | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=simian immunodeficiency virus infection | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=hepatitis E virus infection | success | 6 |  |
| 16 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=hepatitis E virus infection | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=hepatitis E virus infection | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=hepatitis, viral, animal | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=hepatitis, viral, animal | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=hepatitis, viral, animal | success | 3 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=hepatitis A virus infection | success | 50 |  |
| 22 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=hepatitis A virus infection | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=hepatitis A virus infection | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=Omsk hemorrhagic fever | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=Omsk hemorrhagic fever | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=Omsk hemorrhagic fever | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=Kyasanur forest disease | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=Kyasanur forest disease | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=Kyasanur forest disease | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Glecaprevir, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Glecaprevir, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Glecaprevir, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |