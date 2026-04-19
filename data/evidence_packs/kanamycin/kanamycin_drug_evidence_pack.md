# Kanamycin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Kanamycin | |
| DrugBank ID | DB01172 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | hyperamylasemia | 94.53% | L5 | 0 | 0 | S0 | Hold |
| 2 | polyclonal hyperviscosity syndrome | 94.53% | L5 | 0 | 0 | S0 | Hold |
| 3 | congenital analbuminemia | 93.90% | L5 | 0 | 0 | S0 | Hold |
| 4 | Ureaplasma urethritis | 92.88% | L4 | 0 | 1 | S0 | Hold |
| 5 | gonococcal urethritis | 92.88% | L3 | 0 | 20 | S2 | Research Question |
| 6 | blood group incompatibility | 91.89% | L5 | 0 | 1 | S0 | Hold |
| 7 | premalignant hematological system disease | 91.01% | L5 | 0 | 0 | S0 | Hold |
| 8 | uterine inflammatory disease | 90.81% | L3 | 2 | 4 | S1 | Research Question |
| 9 | xanthogranulomatous pyelonephritis | 90.66% | L5 | 0 | 0 | S0 | Hold |
| 10 | monoclonal gammopathy | 90.06% | L4 | 0 | 18 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Kanamycin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Kanamycin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=hyperamylasemia | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Kanamycin, disease=hyperamylasemia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Kanamycin, disease=hyperamylasemia | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Kanamycin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Kanamycin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=congenital analbuminemia | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Kanamycin, disease=congenital analbuminemia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Kanamycin, disease=congenital analbuminemia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=Ureaplasma urethritis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Kanamycin, disease=Ureaplasma urethritis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Kanamycin, disease=Ureaplasma urethritis | success | 1 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=gonococcal urethritis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Kanamycin, disease=gonococcal urethritis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Kanamycin, disease=gonococcal urethritis | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=blood group incompatibility | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Kanamycin, disease=blood group incompatibility | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Kanamycin, disease=blood group incompatibility | success | 1 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=premalignant hematological system disease | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Kanamycin, disease=premalignant hematological system disease | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Kanamycin, disease=premalignant hematological system disease | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=uterine inflammatory disease | success | 2 |  |
| 25 | ictrp | 2026-03-10 | drug=Kanamycin, disease=uterine inflammatory disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Kanamycin, disease=uterine inflammatory disease | success | 4 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=xanthogranulomatous pyelonephritis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Kanamycin, disease=xanthogranulomatous pyelonephritis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Kanamycin, disease=xanthogranulomatous pyelonephritis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Kanamycin, disease=monoclonal gammopathy | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Kanamycin, disease=monoclonal gammopathy | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Kanamycin, disease=monoclonal gammopathy | success | 18 |  |