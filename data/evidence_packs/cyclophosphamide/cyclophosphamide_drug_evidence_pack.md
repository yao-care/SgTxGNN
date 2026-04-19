# Cyclophosphamide 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cyclophosphamide | |
| DrugBank ID | DB00531 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | myeloid leukemia | 99.47% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 2 | ganglioneuroblastoma (disease) | 99.43% | L2 | 6 | 8 | S2 | Research Question |
| 3 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.38% | L5 | 0 | 0 | S0 | Hold |
| 4 | retroperitoneal neoplasm | 99.37% | L3 | 1 | 20 | S1 | Research Question |
| 5 | lymph node cancer | 99.31% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 6 | lymphoma, non-Hodgkin, familial | 98.78% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 7 | acute lymphoblastic leukemia (disease) | 98.67% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 8 | myelodysplastic syndrome | 98.64% | L2 | 50 | 20 | S2 | Proceed with Guardrails |
| 9 | unclassified myelodysplastic syndrome | 98.64% | L3 | 0 | 2 | S1 | Research Question |
| 10 | refractory cytopenia of childhood | 98.59% | L2 | 9 | 11 | S2 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Cyclophosphamide | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Cyclophosphamide | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=myeloid leukemia | success | 50 |  |
| 4 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=myeloid leukemia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=myeloid leukemia | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=ganglioneuroblastoma (disease) | success | 6 |  |
| 7 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=ganglioneuroblastoma (disease) | success | 8 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=retroperitoneal neoplasm | success | 1 |  |
| 13 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=retroperitoneal neoplasm | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=retroperitoneal neoplasm | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=lymph node cancer | success | 50 |  |
| 16 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=lymph node cancer | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=lymph node cancer | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=lymphoma, non-Hodgkin, familial | success | 50 |  |
| 19 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=lymphoma, non-Hodgkin, familial | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=lymphoma, non-Hodgkin, familial | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=acute lymphoblastic leukemia (disease) | success | 50 |  |
| 22 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=acute lymphoblastic leukemia (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=acute lymphoblastic leukemia (disease) | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=myelodysplastic syndrome | success | 50 |  |
| 25 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=myelodysplastic syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=myelodysplastic syndrome | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=unclassified myelodysplastic syndrome | success | 2 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Cyclophosphamide, disease=refractory cytopenia of childhood | success | 9 |  |
| 31 | ictrp | 2026-03-10 | drug=Cyclophosphamide, disease=refractory cytopenia of childhood | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Cyclophosphamide, disease=refractory cytopenia of childhood | success | 11 |  |