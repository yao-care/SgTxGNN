# Dasatinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dasatinib | |
| DrugBank ID | DB01254 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Ewing sarcoma | 99.90% | L2 | 3 | 9 | S2 | Research Question |
| 2 | myeloid leukemia | 99.68% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 3 | liposarcoma | 99.67% | L3 | 1 | 3 | S2 | Research Question |
| 4 | fibromatosis, gingival | 99.65% | L5 | 0 | 0 | S0 | Hold |
| 5 | dermatofibrosarcoma protuberans | 99.65% | L4 | 0 | 1 | S1 | Research Question |
| 6 | ovarian myxoid liposarcoma | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 7 | ganglioneuroblastoma (disease) | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 8 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 9 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 99.58% | L5 | 0 | 20 | S0 | Hold |
| 10 | hamartoma of lung | 99.56% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Dasatinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Dasatinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=Ewing sarcoma | success | 3 |  |
| 4 | ictrp | 2026-03-09 | drug=Dasatinib, disease=Ewing sarcoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Dasatinib, disease=Ewing sarcoma | success | 9 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=myeloid leukemia | success | 50 |  |
| 7 | ictrp | 2026-03-09 | drug=Dasatinib, disease=myeloid leukemia | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Dasatinib, disease=myeloid leukemia | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=liposarcoma | success | 1 |  |
| 10 | ictrp | 2026-03-09 | drug=Dasatinib, disease=liposarcoma | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Dasatinib, disease=liposarcoma | success | 3 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=fibromatosis, gingival | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Dasatinib, disease=fibromatosis, gingival | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Dasatinib, disease=fibromatosis, gingival | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Dasatinib, disease=dermatofibrosarcoma protuberans | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Dasatinib, disease=dermatofibrosarcoma protuberans | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Dasatinib, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Dasatinib, disease=ovarian myxoid liposarcoma | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Dasatinib, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Dasatinib, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Dasatinib, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Dasatinib, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Dasatinib, disease=inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Dasatinib, disease=inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Dasatinib, disease=hamartoma of lung | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Dasatinib, disease=hamartoma of lung | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Dasatinib, disease=hamartoma of lung | success | 0 |  |