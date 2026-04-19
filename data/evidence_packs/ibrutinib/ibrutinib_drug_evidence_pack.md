# Ibrutinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ibrutinib | |
| DrugBank ID | DB09053 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | polyclonal hypergammaglobulinemia | 91.75% | L5 | 0 | 0 | S0 | Hold |
| 2 | monoclonal paraproteinemia disease | 91.16% | L1 | 13 | 20 | S3 | Proceed with Guardrails |
| 3 | thyroid gland mucosa-associated lymphoid tissue lymphoma | 88.43% | L5 | 0 | 0 | S0 | Hold |
| 4 | small intestinal mucosa-associated lymphoid tissue lymphoma | 88.36% | L4 | 1 | 0 | S0 | Hold |
| 5 | small intestinal Burkitt lymphoma | 88.32% | L4 | 1 | 0 | S0 | Hold |
| 6 | breast mucosa-associated lymphoid tissue lymphoma | 88.07% | L5 | 0 | 0 | S0 | Hold |
| 7 | tonsillar lymphoma | 88.05% | L5 | 0 | 0 | S0 | Hold |
| 8 | marginal zone lymphoma | 87.96% | L1 | 28 | 20 | S3 | Proceed with Guardrails |
| 9 | extracutaneous mastocytoma | 87.74% | L4 | 0 | 1 | S1 | Research Question |
| 10 | neoplasm of mature B-cells | 86.55% | L3 | 2 | 20 | S2 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Ibrutinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Ibrutinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=polyclonal hypergammaglobulinemia | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=polyclonal hypergammaglobulinemia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=polyclonal hypergammaglobulinemia | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=monoclonal paraproteinemia disease | success | 13 |  |
| 7 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=monoclonal paraproteinemia disease | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=monoclonal paraproteinemia disease | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=thyroid gland mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=thyroid gland mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=thyroid gland mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=small intestinal mucosa-associated lymphoid tissue lymphoma | success | 1 |  |
| 13 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=small intestinal mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=small intestinal mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=small intestinal Burkitt lymphoma | success | 1 |  |
| 16 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=small intestinal Burkitt lymphoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=small intestinal Burkitt lymphoma | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=breast mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=breast mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=breast mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=tonsillar lymphoma | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=tonsillar lymphoma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=tonsillar lymphoma | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=marginal zone lymphoma | success | 28 |  |
| 25 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=marginal zone lymphoma | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=marginal zone lymphoma | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=extracutaneous mastocytoma | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=extracutaneous mastocytoma | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=extracutaneous mastocytoma | success | 1 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Ibrutinib, disease=neoplasm of mature B-cells | success | 2 |  |
| 31 | ictrp | 2026-03-10 | drug=Ibrutinib, disease=neoplasm of mature B-cells | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Ibrutinib, disease=neoplasm of mature B-cells | success | 20 |  |