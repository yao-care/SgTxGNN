# Bendamustine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Bendamustine | |
| DrugBank ID | DB06769 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | mantle cell lymphoma | 99.63% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 2 | chronic myelogenous leukemia, BCR-ABL1 positive | 99.62% | L4 | 1 | 3 | S1 | Research Question |
| 3 | Hodgkins lymphoma | 99.55% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 4 | small intestinal Burkitt lymphoma | 99.40% | L4 | 3 | 0 | S0 | Hold |
| 5 | small intestinal mucosa-associated lymphoid tissue lymphoma | 99.35% | L4 | 3 | 1 | S0 | Hold |
| 6 | thyroid gland mucosa-associated lymphoid tissue lymphoma | 99.34% | L5 | 0 | 0 | S0 | Hold |
| 7 | breast mucosa-associated lymphoid tissue lymphoma | 99.34% | L5 | 0 | 2 | S0 | Hold |
| 8 | tonsillar lymphoma | 99.32% | L4 | 0 | 2 | S0 | Hold |
| 9 | MALT lymphoma | 99.21% | L1 | 29 | 20 | S3 | Proceed with Guardrails |
| 10 | relapsing-remitting multiple sclerosis | 99.21% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Bendamustine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Bendamustine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=mantle cell lymphoma | success | 50 |  |
| 4 | ictrp | 2026-03-09 | drug=Bendamustine, disease=mantle cell lymphoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Bendamustine, disease=mantle cell lymphoma | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=chronic myelogenous leukemia, BCR-ABL1 positive | success | 1 |  |
| 7 | ictrp | 2026-03-09 | drug=Bendamustine, disease=chronic myelogenous leukemia, BCR-ABL1 positive | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Bendamustine, disease=chronic myelogenous leukemia, BCR-ABL1 positive | success | 3 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=Hodgkins lymphoma | success | 50 |  |
| 10 | ictrp | 2026-03-09 | drug=Bendamustine, disease=Hodgkins lymphoma | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Bendamustine, disease=Hodgkins lymphoma | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=small intestinal Burkitt lymphoma | success | 3 |  |
| 13 | ictrp | 2026-03-09 | drug=Bendamustine, disease=small intestinal Burkitt lymphoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Bendamustine, disease=small intestinal Burkitt lymphoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=small intestinal mucosa-associated lymphoid tissue lymphoma | success | 3 |  |
| 16 | ictrp | 2026-03-09 | drug=Bendamustine, disease=small intestinal mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Bendamustine, disease=small intestinal mucosa-associated lymphoid tissue lymphoma | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=thyroid gland mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Bendamustine, disease=thyroid gland mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Bendamustine, disease=thyroid gland mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=breast mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Bendamustine, disease=breast mucosa-associated lymphoid tissue lymphoma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Bendamustine, disease=breast mucosa-associated lymphoid tissue lymphoma | success | 2 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=tonsillar lymphoma | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Bendamustine, disease=tonsillar lymphoma | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Bendamustine, disease=tonsillar lymphoma | success | 2 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=MALT lymphoma | success | 29 |  |
| 28 | ictrp | 2026-03-09 | drug=Bendamustine, disease=MALT lymphoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Bendamustine, disease=MALT lymphoma | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Bendamustine, disease=relapsing-remitting multiple sclerosis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Bendamustine, disease=relapsing-remitting multiple sclerosis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Bendamustine, disease=relapsing-remitting multiple sclerosis | success | 0 |  |