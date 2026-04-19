# Idarubicin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Idarubicin | |
| DrugBank ID | DB01177 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | bulbar polio | 97.05% | L5 | 0 | 0 | S0 | Hold |
| 2 | 5q35 microduplication syndrome | 94.87% | L5 | 0 | 0 | S0 | Hold |
| 3 | neuralgic amyotrophy | 92.79% | L5 | 0 | 0 | S0 | Hold |
| 4 | amyotrophic neuralgia | 92.15% | L5 | 0 | 0 | S0 | Hold |
| 5 | familial thrombocytosis | 79.34% | L5 | 0 | 0 | S0 | Hold |
| 6 | reactive thrombocytosis | 79.15% | L5 | 0 | 0 | S0 | Hold |
| 7 | ganglioneuroblastoma (disease) | 78.40% | L4 | 0 | 0 | S1 | Research Question |
| 8 | retroperitoneal neoplasm | 77.40% | L4 | 0 | 1 | S1 | Research Question |
| 9 | vertebral anomalies and variable endocrine and T-cell dysfunction | 75.60% | L5 | 0 | 0 | S0 | Hold |
| 10 | obsolete Hodgkin's granuloma | 72.58% | L4 | 0 | 0 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Idarubicin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Idarubicin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=bulbar polio | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Idarubicin, disease=bulbar polio | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Idarubicin, disease=bulbar polio | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=5q35 microduplication syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Idarubicin, disease=5q35 microduplication syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Idarubicin, disease=5q35 microduplication syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=neuralgic amyotrophy | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Idarubicin, disease=neuralgic amyotrophy | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Idarubicin, disease=neuralgic amyotrophy | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=amyotrophic neuralgia | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Idarubicin, disease=amyotrophic neuralgia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Idarubicin, disease=amyotrophic neuralgia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=familial thrombocytosis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Idarubicin, disease=familial thrombocytosis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Idarubicin, disease=familial thrombocytosis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=reactive thrombocytosis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Idarubicin, disease=reactive thrombocytosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Idarubicin, disease=reactive thrombocytosis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Idarubicin, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Idarubicin, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=retroperitoneal neoplasm | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Idarubicin, disease=retroperitoneal neoplasm | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Idarubicin, disease=retroperitoneal neoplasm | success | 1 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Idarubicin, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Idarubicin, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Idarubicin, disease=obsolete Hodgkin's granuloma | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Idarubicin, disease=obsolete Hodgkin's granuloma | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Idarubicin, disease=obsolete Hodgkin's granuloma | success | 0 |  |