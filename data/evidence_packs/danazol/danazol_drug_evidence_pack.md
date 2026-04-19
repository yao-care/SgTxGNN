# Danazol 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Danazol | |
| DrugBank ID | DB01406 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | amenorrhea (disease) | 100.00% | L2 | 0 | 20 | S3 | Proceed with Guardrails |
| 2 | benign mammary dysplasia | 100.00% | L1 | 0 | 20 | S3 | Proceed with Guardrails |
| 3 | apocrine adenosis of breast | 100.00% | L4 | 0 | 3 | S1 | Research Question |
| 4 | blunt duct adenosis of breast | 100.00% | L5 | 0 | 0 | S0 | Hold |
| 5 | fat necrosis of breast | 100.00% | L5 | 0 | 0 | S0 | Hold |
| 6 | breast abscess | 100.00% | L4 | 0 | 3 | S1 | Research Question |
| 7 | lactation disease | 100.00% | L4 | 0 | 9 | S0 | Hold |
| 8 | breast adenosis | 100.00% | L3 | 0 | 19 | S2 | Research Question |
| 9 | vulvovaginitis | 99.96% | L5 | 0 | 1 | S0 | Hold |
| 10 | vulvitis | 99.95% | L5 | 0 | 1 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Danazol | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Danazol | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=amenorrhea (disease) | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Danazol, disease=amenorrhea (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Danazol, disease=amenorrhea (disease) | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=benign mammary dysplasia | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Danazol, disease=benign mammary dysplasia | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Danazol, disease=benign mammary dysplasia | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=apocrine adenosis of breast | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Danazol, disease=apocrine adenosis of breast | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Danazol, disease=apocrine adenosis of breast | success | 3 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=blunt duct adenosis of breast | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Danazol, disease=blunt duct adenosis of breast | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Danazol, disease=blunt duct adenosis of breast | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=fat necrosis of breast | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Danazol, disease=fat necrosis of breast | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Danazol, disease=fat necrosis of breast | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=breast abscess | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Danazol, disease=breast abscess | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Danazol, disease=breast abscess | success | 3 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=lactation disease | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Danazol, disease=lactation disease | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Danazol, disease=lactation disease | success | 9 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=breast adenosis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Danazol, disease=breast adenosis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Danazol, disease=breast adenosis | success | 19 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=vulvovaginitis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Danazol, disease=vulvovaginitis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Danazol, disease=vulvovaginitis | success | 1 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Danazol, disease=vulvitis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Danazol, disease=vulvitis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Danazol, disease=vulvitis | success | 1 |  |