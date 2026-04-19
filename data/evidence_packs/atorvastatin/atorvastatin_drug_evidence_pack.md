# Atorvastatin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Atorvastatin | |
| DrugBank ID | DB01076 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | familial hypercholesterolemia | 99.42% | L1 | 34 | 19 | S3 | Proceed with Guardrails |
| 2 | HIV infectious disease | 99.31% | L2 | 22 | 20 | S2 | Research Question |
| 3 | brain stem infarction | 99.31% | L3 | 2 | 5 | S2 | Research Question |
| 4 | cholesterol-ester transfer protein deficiency | 99.25% | L4 | 0 | 5 | S0 | Hold |
| 5 | hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | 99.20% | L5 | 0 | 3 | S0 | Hold |
| 6 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.13% | L5 | 0 | 0 | S0 | Hold |
| 7 | hypoalphalipoproteinemia | 98.99% | L3 | 1 | 3 | S1 | Hold |
| 8 | hypercholesterolemia, autosomal dominant | 98.93% | L1 | 30 | 20 | S3 | Proceed with Guardrails |
| 9 | feline acquired immunodeficiency syndrome | 98.92% | L5 | 0 | 0 | S0 | Hold |
| 10 | simian immunodeficiency virus infection | 98.92% | L5 | 0 | 1 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Atorvastatin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Atorvastatin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=familial hypercholesterolemia | success | 34 |  |
| 4 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=familial hypercholesterolemia | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=familial hypercholesterolemia | success | 19 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=HIV infectious disease | success | 22 |  |
| 7 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=HIV infectious disease | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=HIV infectious disease | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=brain stem infarction | success | 2 |  |
| 10 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=brain stem infarction | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=brain stem infarction | success | 5 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=cholesterol-ester transfer protein deficiency | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=cholesterol-ester transfer protein deficiency | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=cholesterol-ester transfer protein deficiency | success | 5 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | success | 3 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=hypoalphalipoproteinemia | success | 1 |  |
| 22 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=hypoalphalipoproteinemia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=hypoalphalipoproteinemia | success | 3 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=hypercholesterolemia, autosomal dominant | success | 30 |  |
| 25 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=hypercholesterolemia, autosomal dominant | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=hypercholesterolemia, autosomal dominant | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=feline acquired immunodeficiency syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Atorvastatin, disease=simian immunodeficiency virus infection | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Atorvastatin, disease=simian immunodeficiency virus infection | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Atorvastatin, disease=simian immunodeficiency virus infection | success | 1 |  |