# Afatinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Afatinib | |
| DrugBank ID | DB08916 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | HER2 positive breast carcinoma | 98.65% | L1 | 10 | 19 | S2 | Research Question |
| 2 | multiple endocrine neoplasia | 98.48% | L4 | 5 | 0 | S0 | Hold |
| 3 | progesterone-receptor negative breast cancer | 97.93% | L2 | 13 | 1 | S2 | Research Question |
| 4 | normal breast-like subtype of breast carcinoma | 97.89% | L5 | 0 | 0 | S0 | Hold |
| 5 | progesterone-receptor positive breast cancer | 97.89% | L4 | 0 | 3 | S0 | Hold |
| 6 | breast tumor luminal A or B | 97.87% | L5 | 0 | 19 | S0 | Hold |
| 7 | thrombocytopenia | 97.58% | L5 | 5 | 7 | S0 | Hold |
| 8 | marcothrombocytopenia with mitral valve insufficiency | 97.42% | L5 | 0 | 0 | S0 | Hold |
| 9 | hereditary thrombocytopenia with normal platelets | 97.39% | L5 | 0 | 0 | S0 | Hold |
| 10 | dense granule disease | 97.28% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Afatinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Afatinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=HER2 positive breast carcinoma | success | 10 |  |
| 4 | ictrp | 2026-03-10 | drug=Afatinib, disease=HER2 positive breast carcinoma | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Afatinib, disease=HER2 positive breast carcinoma | success | 19 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=multiple endocrine neoplasia | success | 5 |  |
| 7 | ictrp | 2026-03-10 | drug=Afatinib, disease=multiple endocrine neoplasia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Afatinib, disease=multiple endocrine neoplasia | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=progesterone-receptor negative breast cancer | success | 13 |  |
| 10 | ictrp | 2026-03-10 | drug=Afatinib, disease=progesterone-receptor negative breast cancer | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Afatinib, disease=progesterone-receptor negative breast cancer | success | 1 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=normal breast-like subtype of breast carcinoma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Afatinib, disease=normal breast-like subtype of breast carcinoma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Afatinib, disease=normal breast-like subtype of breast carcinoma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=progesterone-receptor positive breast cancer | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Afatinib, disease=progesterone-receptor positive breast cancer | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Afatinib, disease=progesterone-receptor positive breast cancer | success | 3 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=breast tumor luminal A or B | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Afatinib, disease=breast tumor luminal A or B | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Afatinib, disease=breast tumor luminal A or B | success | 19 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=thrombocytopenia | success | 5 |  |
| 22 | ictrp | 2026-03-10 | drug=Afatinib, disease=thrombocytopenia | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Afatinib, disease=thrombocytopenia | success | 7 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=marcothrombocytopenia with mitral valve insufficiency | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Afatinib, disease=marcothrombocytopenia with mitral valve insufficiency | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Afatinib, disease=marcothrombocytopenia with mitral valve insufficiency | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=hereditary thrombocytopenia with normal platelets | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Afatinib, disease=hereditary thrombocytopenia with normal platelets | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Afatinib, disease=hereditary thrombocytopenia with normal platelets | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Afatinib, disease=dense granule disease | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Afatinib, disease=dense granule disease | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Afatinib, disease=dense granule disease | success | 0 |  |