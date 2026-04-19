# Acalabrutinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Acalabrutinib | |
| DrugBank ID | DB11703 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | lymphoma, non-Hodgkin, familial | 97.64% | L2 | 20 | 20 | S3 | Proceed with Guardrails |
| 2 | colon adenocarcinoma | 96.60% | L5 | 0 | 0 | S0 | Hold |
| 3 | small intestinal Burkitt lymphoma | 94.04% | L5 | 0 | 0 | S0 | Hold |
| 4 | small intestinal mucosa-associated lymphoid tissue lymphoma | 93.83% | L4 | 0 | 0 | S1 | Research Question |
| 5 | thyroid gland mucosa-associated lymphoid tissue lymphoma | 93.76% | L4 | 0 | 0 | S1 | Research Question |
| 6 | breast mucosa-associated lymphoid tissue lymphoma | 93.67% | L4 | 0 | 0 | S1 | Research Question |
| 7 | tonsillar lymphoma | 93.67% | L4 | 0 | 1 | S1 | Research Question |
| 8 | neoplasm of mature B-cells | 93.25% | L3 | 1 | 3 | S2 | Research Question |
| 9 | lymph node cancer | 92.30% | L2 | 11 | 10 | S3 | Proceed with Guardrails |
| 10 | polyclonal hypergammaglobulinemia | 92.29% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Acalabrutinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Acalabrutinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=lymphoma, non-Hodgkin, familial | success | 20 |  |
| 4 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=lymphoma, non-Hodgkin, familial | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=lymphoma, non-Hodgkin, familial | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=colon adenocarcinoma | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=colon adenocarcinoma | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=colon adenocarcinoma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=small intestinal Burkitt lymphoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=small intestinal Burkitt lymphoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=small intestinal Burkitt lymphoma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=small intestinal mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=small intestinal mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=small intestinal mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=thyroid gland mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=thyroid gland mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=thyroid gland mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=breast mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=breast mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=breast mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=tonsillar lymphoma | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=tonsillar lymphoma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=tonsillar lymphoma | success | 1 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=neoplasm of mature B-cells | success | 1 |  |
| 25 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=neoplasm of mature B-cells | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=neoplasm of mature B-cells | success | 3 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=lymph node cancer | success | 11 |  |
| 28 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=lymph node cancer | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=lymph node cancer | success | 10 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Acalabrutinib, disease=polyclonal hypergammaglobulinemia | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Acalabrutinib, disease=polyclonal hypergammaglobulinemia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Acalabrutinib, disease=polyclonal hypergammaglobulinemia | success | 0 |  |