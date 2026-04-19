# Clofarabine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clofarabine | |
| DrugBank ID | DB00631 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | myeloid leukemia | 99.88% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 2 | precursor lymphoblastic lymphoma/leukemia | 99.57% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 3 | ganglioneuroblastoma (disease) | 99.53% | L5 | 0 | 0 | S0 | Hold |
| 4 | neuroblastoma | 99.52% | L4 | 1 | 2 | S1 | Hold |
| 5 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.46% | L5 | 0 | 0 | S0 | Hold |
| 6 | retroperitoneal neoplasm | 99.44% | L5 | 0 | 0 | S0 | Hold |
| 7 | blast phase chronic myelogenous leukemia, BCR-ABL1 positive | 99.43% | L2 | 8 | 4 | S2 | Research Question |
| 8 | acute lymphoblastic leukemia | 99.31% | L1 | 50 | 18 | S3 | Proceed with Guardrails |
| 9 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 99.26% | L5 | 0 | 0 | S0 | Hold |
| 10 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.26% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Clofarabine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Clofarabine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=myeloid leukemia | success | 50 |  |
| 4 | ictrp | 2026-03-09 | drug=Clofarabine, disease=myeloid leukemia | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Clofarabine, disease=myeloid leukemia | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=precursor lymphoblastic lymphoma/leukemia | success | 50 |  |
| 7 | ictrp | 2026-03-09 | drug=Clofarabine, disease=precursor lymphoblastic lymphoma/leukemia | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Clofarabine, disease=precursor lymphoblastic lymphoma/leukemia | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Clofarabine, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Clofarabine, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=neuroblastoma | success | 1 |  |
| 13 | ictrp | 2026-03-09 | drug=Clofarabine, disease=neuroblastoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Clofarabine, disease=neuroblastoma | success | 2 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Clofarabine, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Clofarabine, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=retroperitoneal neoplasm | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Clofarabine, disease=retroperitoneal neoplasm | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Clofarabine, disease=retroperitoneal neoplasm | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=blast phase chronic myelogenous leukemia, BCR-ABL1 positive | success | 8 |  |
| 22 | ictrp | 2026-03-09 | drug=Clofarabine, disease=blast phase chronic myelogenous leukemia, BCR-ABL1 positive | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Clofarabine, disease=blast phase chronic myelogenous leukemia, BCR-ABL1 positive | success | 4 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=acute lymphoblastic leukemia | success | 50 |  |
| 25 | ictrp | 2026-03-09 | drug=Clofarabine, disease=acute lymphoblastic leukemia | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Clofarabine, disease=acute lymphoblastic leukemia | success | 18 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Clofarabine, disease=chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Clofarabine, disease=chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Clofarabine, disease=pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Clofarabine, disease=pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Clofarabine, disease=pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | success | 0 |  |