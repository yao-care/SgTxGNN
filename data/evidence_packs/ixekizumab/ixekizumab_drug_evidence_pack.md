# Ixekizumab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ixekizumab | |
| DrugBank ID | DB11569 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | rheumatoid vasculitis | 97.53% | L4 | 1 | 0 | S1 | Research Question |
| 2 | acute lymphoblastic/lymphocytic leukemia | 97.35% | L5 | 0 | 0 | S0 | Hold |
| 3 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 97.07% | L5 | 0 | 0 | S0 | Hold |
| 4 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 97.07% | L5 | 0 | 0 | S0 | Hold |
| 5 | hypermobility of coccyx | 96.87% | L5 | 0 | 0 | S0 | Hold |
| 6 | inflammatory spondylopathy | 96.77% | L1 | 26 | 20 | S3 | Proceed with Guardrails |
| 7 | Kummell disease | 96.70% | L5 | 0 | 0 | S0 | Hold |
| 8 | polyarticular juvenile rheumatoid arthritis | 96.42% | L5 | 0 | 0 | S0 | Hold |
| 9 | vertebral disease | 95.13% | L1 | 4 | 20 | S3 | Proceed with Guardrails |
| 10 | fibromatosis, gingival | 92.21% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Ixekizumab | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Ixekizumab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=rheumatoid vasculitis | success | 1 |  |
| 4 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=rheumatoid vasculitis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=rheumatoid vasculitis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=acute lymphoblastic/lymphocytic leukemia | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=acute lymphoblastic/lymphocytic leukemia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=acute lymphoblastic/lymphocytic leukemia | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=hypermobility of coccyx | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=hypermobility of coccyx | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=hypermobility of coccyx | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=inflammatory spondylopathy | success | 26 |  |
| 19 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=inflammatory spondylopathy | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=inflammatory spondylopathy | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=Kummell disease | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=Kummell disease | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=Kummell disease | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=polyarticular juvenile rheumatoid arthritis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=polyarticular juvenile rheumatoid arthritis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=polyarticular juvenile rheumatoid arthritis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=vertebral disease | success | 4 |  |
| 28 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=vertebral disease | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=vertebral disease | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Ixekizumab, disease=fibromatosis, gingival | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Ixekizumab, disease=fibromatosis, gingival | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Ixekizumab, disease=fibromatosis, gingival | success | 0 |  |