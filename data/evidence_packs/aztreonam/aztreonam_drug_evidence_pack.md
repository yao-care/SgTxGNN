# Aztreonam 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Aztreonam | |
| DrugBank ID | DB00355 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | hyperamylasemia | 99.73% | L5 | 0 | 0 | S0 | Hold |
| 2 | polyclonal hyperviscosity syndrome | 99.73% | L5 | 0 | 0 | S0 | Hold |
| 3 | congenital analbuminemia | 99.69% | L5 | 0 | 0 | S0 | Hold |
| 4 | Ureaplasma urethritis | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 5 | gonococcal urethritis | 99.59% | L2 | 1 | 8 | S3 | Proceed with Guardrails |
| 6 | blood group incompatibility | 99.59% | L5 | 0 | 1 | S0 | Hold |
| 7 | premalignant hematological system disease | 99.54% | L5 | 0 | 0 | S0 | Hold |
| 8 | epiglottitis | 99.53% | L4 | 0 | 1 | S1 | Hold |
| 9 | monoclonal gammopathy | 99.50% | L5 | 0 | 0 | S0 | Hold |
| 10 | xanthogranulomatous pyelonephritis | 99.49% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Aztreonam | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Aztreonam | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=hyperamylasemia | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Aztreonam, disease=hyperamylasemia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Aztreonam, disease=hyperamylasemia | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Aztreonam, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Aztreonam, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=congenital analbuminemia | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Aztreonam, disease=congenital analbuminemia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Aztreonam, disease=congenital analbuminemia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=Ureaplasma urethritis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Aztreonam, disease=Ureaplasma urethritis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Aztreonam, disease=Ureaplasma urethritis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=gonococcal urethritis | success | 1 |  |
| 16 | ictrp | 2026-03-10 | drug=Aztreonam, disease=gonococcal urethritis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Aztreonam, disease=gonococcal urethritis | success | 8 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=blood group incompatibility | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Aztreonam, disease=blood group incompatibility | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Aztreonam, disease=blood group incompatibility | success | 1 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=premalignant hematological system disease | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Aztreonam, disease=premalignant hematological system disease | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Aztreonam, disease=premalignant hematological system disease | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=epiglottitis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Aztreonam, disease=epiglottitis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Aztreonam, disease=epiglottitis | success | 1 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=monoclonal gammopathy | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Aztreonam, disease=monoclonal gammopathy | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Aztreonam, disease=monoclonal gammopathy | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Aztreonam, disease=xanthogranulomatous pyelonephritis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Aztreonam, disease=xanthogranulomatous pyelonephritis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Aztreonam, disease=xanthogranulomatous pyelonephritis | success | 0 |  |