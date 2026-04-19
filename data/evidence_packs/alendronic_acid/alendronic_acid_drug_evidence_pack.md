# Alendronic acid 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Alendronic acid | |
| DrugBank ID | DB00630 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | HIV infectious disease | 96.78% | L1 | 4 | 2 | S3 | Proceed with Guardrails |
| 2 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 95.23% | L5 | 0 | 0 | S0 | Hold |
| 3 | feline acquired immunodeficiency syndrome | 94.82% | L5 | 0 | 0 | S0 | Hold |
| 4 | simian immunodeficiency virus infection | 94.82% | L5 | 0 | 0 | S0 | Hold |
| 5 | deficiency anemia | 94.25% | L4 | 0 | 1 | S1 | Research Question |
| 6 | vitamin B12- and folate-independent constitutional megaloblastic anemia | 90.61% | L5 | 0 | 0 | S0 | Hold |
| 7 | Plummer-Vinson syndrome | 90.37% | L5 | 0 | 0 | S0 | Hold |
| 8 | osteomesopyknosis | 88.17% | L5 | 0 | 0 | S0 | Hold |
| 9 | obsolete familial combined hyperlipidemia | 86.32% | L5 | 0 | 0 | S0 | Hold |
| 10 | biotin metabolic disease | 86.15% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Alendronic acid | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Alendronic acid | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=HIV infectious disease | success | 4 |  |
| 4 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=HIV infectious disease | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=HIV infectious disease | success | 2 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=simian immunodeficiency virus infection | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=simian immunodeficiency virus infection | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=simian immunodeficiency virus infection | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=deficiency anemia | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=deficiency anemia | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=deficiency anemia | success | 1 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=vitamin B12- and folate-independent constitutional megaloblastic anemia | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=vitamin B12- and folate-independent constitutional megaloblastic anemia | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=vitamin B12- and folate-independent constitutional megaloblastic anemia | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=Plummer-Vinson syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=Plummer-Vinson syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=Plummer-Vinson syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=osteomesopyknosis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=osteomesopyknosis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=osteomesopyknosis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Alendronic acid, disease=biotin metabolic disease | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Alendronic acid, disease=biotin metabolic disease | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Alendronic acid, disease=biotin metabolic disease | success | 0 |  |