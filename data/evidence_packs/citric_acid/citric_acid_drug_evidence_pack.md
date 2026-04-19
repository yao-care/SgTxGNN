# Citric acid 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Citric acid | |
| DrugBank ID | DB04272 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | stomach disease | 99.74% | L4 | 29 | 20 | S0 | Hold |
| 2 | pharyngitis | 99.68% | L5 | 2 | 3 | S0 | Hold |
| 3 | acute laryngopharyngitis | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 4 | postgastrectomy syndrome | 99.58% | L5 | 0 | 0 | S0 | Hold |
| 5 | nasal cavity disease | 99.52% | L5 | 4 | 2 | S0 | Hold |
| 6 | papillary conjunctivitis | 99.24% | L5 | 0 | 0 | S0 | Hold |
| 7 | blepharoconjunctivitis | 99.14% | L5 | 0 | 0 | S0 | Hold |
| 8 | rhinitis | 99.07% | L4 | 2 | 20 | S1 | Research Question |
| 9 | thrombotic disease | 98.86% | L2 | 8 | 20 | S2 | Proceed with Guardrails |
| 10 | ulcerative blepharitis | 98.67% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Citric acid | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Citric acid | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=stomach disease | success | 29 |  |
| 4 | ictrp | 2026-03-09 | drug=Citric acid, disease=stomach disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Citric acid, disease=stomach disease | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=pharyngitis | success | 2 |  |
| 7 | ictrp | 2026-03-09 | drug=Citric acid, disease=pharyngitis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Citric acid, disease=pharyngitis | success | 3 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=acute laryngopharyngitis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Citric acid, disease=acute laryngopharyngitis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Citric acid, disease=acute laryngopharyngitis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=postgastrectomy syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Citric acid, disease=postgastrectomy syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Citric acid, disease=postgastrectomy syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=nasal cavity disease | success | 4 |  |
| 16 | ictrp | 2026-03-09 | drug=Citric acid, disease=nasal cavity disease | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Citric acid, disease=nasal cavity disease | success | 2 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=papillary conjunctivitis | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Citric acid, disease=papillary conjunctivitis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Citric acid, disease=papillary conjunctivitis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=blepharoconjunctivitis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Citric acid, disease=blepharoconjunctivitis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Citric acid, disease=blepharoconjunctivitis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=rhinitis | success | 2 |  |
| 25 | ictrp | 2026-03-09 | drug=Citric acid, disease=rhinitis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Citric acid, disease=rhinitis | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=thrombotic disease | success | 8 |  |
| 28 | ictrp | 2026-03-09 | drug=Citric acid, disease=thrombotic disease | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Citric acid, disease=thrombotic disease | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Citric acid, disease=ulcerative blepharitis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Citric acid, disease=ulcerative blepharitis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Citric acid, disease=ulcerative blepharitis | success | 0 |  |