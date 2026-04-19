# Arginine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Arginine | |
| DrugBank ID | DB00125 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | gastroparesis (disease) | 99.42% | L4 | 1 | 10 | S1 | Research Question |
| 2 | congenital prothrombin deficiency | 98.92% | L5 | 2 | 5 | S0 | Hold |
| 3 | dyspepsia | 97.43% | L4 | 3 | 20 | S1 | Research Question |
| 4 | vitamin deficiency disorder | 96.92% | L5 | 6 | 20 | S0 | Hold |
| 5 | sclerosing cholangitis | 96.83% | L5 | 0 | 7 | S0 | Hold |
| 6 | obsolete vitamin D deficiency | 96.64% | L5 | 0 | 0 | S0 | Hold |
| 7 | biotin metabolic disease | 96.19% | L5 | 1 | 20 | S0 | Hold |
| 8 | hypophosphatemic rickets | 95.26% | L4 | 1 | 17 | S1 | Research Question |
| 9 | postgastrectomy syndrome | 93.74% | L4 | 0 | 3 | S0 | Hold |
| 10 | non-syndromic esophageal malformation | 93.41% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Arginine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Arginine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=gastroparesis (disease) | success | 1 |  |
| 4 | ictrp | 2026-03-10 | drug=Arginine, disease=gastroparesis (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Arginine, disease=gastroparesis (disease) | success | 10 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=congenital prothrombin deficiency | success | 2 |  |
| 7 | ictrp | 2026-03-10 | drug=Arginine, disease=congenital prothrombin deficiency | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Arginine, disease=congenital prothrombin deficiency | success | 5 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=dyspepsia | success | 3 |  |
| 10 | ictrp | 2026-03-10 | drug=Arginine, disease=dyspepsia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Arginine, disease=dyspepsia | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=vitamin deficiency disorder | success | 6 |  |
| 13 | ictrp | 2026-03-10 | drug=Arginine, disease=vitamin deficiency disorder | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Arginine, disease=vitamin deficiency disorder | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=sclerosing cholangitis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Arginine, disease=sclerosing cholangitis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Arginine, disease=sclerosing cholangitis | success | 7 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Arginine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Arginine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=biotin metabolic disease | success | 1 |  |
| 22 | ictrp | 2026-03-10 | drug=Arginine, disease=biotin metabolic disease | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Arginine, disease=biotin metabolic disease | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=hypophosphatemic rickets | success | 1 |  |
| 25 | ictrp | 2026-03-10 | drug=Arginine, disease=hypophosphatemic rickets | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Arginine, disease=hypophosphatemic rickets | success | 17 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=postgastrectomy syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Arginine, disease=postgastrectomy syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Arginine, disease=postgastrectomy syndrome | success | 3 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Arginine, disease=non-syndromic esophageal malformation | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Arginine, disease=non-syndromic esophageal malformation | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Arginine, disease=non-syndromic esophageal malformation | success | 0 |  |