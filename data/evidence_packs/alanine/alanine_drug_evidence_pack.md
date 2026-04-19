# Alanine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Alanine | |
| DrugBank ID | DB00160 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | gastroparesis (disease) | 99.37% | L5 | 9 | 3 | S0 | Hold |
| 2 | obsolete vitamin D deficiency | 98.70% | L5 | 0 | 0 | S0 | Hold |
| 3 | dyspepsia | 98.37% | L5 | 33 | 20 | S0 | Hold |
| 4 | congenital prothrombin deficiency | 98.26% | L5 | 13 | 3 | S0 | Hold |
| 5 | hypophosphatemic rickets | 96.56% | L4 | 0 | 6 | S1 | Research Question |
| 6 | renal tubular acidosis | 96.41% | L4 | 1 | 20 | S1 | Research Question |
| 7 | sclerosing cholangitis | 96.34% | L5 | 27 | 20 | S0 | Hold |
| 8 | potassium deficiency disease | 95.85% | L5 | 50 | 20 | S0 | Hold |
| 9 | postmenopausal osteoporosis | 95.70% | L5 | 15 | 20 | S0 | Hold |
| 10 | albinism-deafness syndrome | 94.88% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Alanine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Alanine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=gastroparesis (disease) | success | 9 |  |
| 4 | ictrp | 2026-03-10 | drug=Alanine, disease=gastroparesis (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Alanine, disease=gastroparesis (disease) | success | 3 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Alanine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Alanine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=dyspepsia | success | 33 |  |
| 10 | ictrp | 2026-03-10 | drug=Alanine, disease=dyspepsia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Alanine, disease=dyspepsia | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=congenital prothrombin deficiency | success | 13 |  |
| 13 | ictrp | 2026-03-10 | drug=Alanine, disease=congenital prothrombin deficiency | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Alanine, disease=congenital prothrombin deficiency | success | 3 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=hypophosphatemic rickets | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Alanine, disease=hypophosphatemic rickets | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Alanine, disease=hypophosphatemic rickets | success | 6 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=renal tubular acidosis | success | 1 |  |
| 19 | ictrp | 2026-03-10 | drug=Alanine, disease=renal tubular acidosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Alanine, disease=renal tubular acidosis | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=sclerosing cholangitis | success | 27 |  |
| 22 | ictrp | 2026-03-10 | drug=Alanine, disease=sclerosing cholangitis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Alanine, disease=sclerosing cholangitis | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=potassium deficiency disease | success | 50 |  |
| 25 | ictrp | 2026-03-10 | drug=Alanine, disease=potassium deficiency disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Alanine, disease=potassium deficiency disease | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=postmenopausal osteoporosis | success | 15 |  |
| 28 | ictrp | 2026-03-10 | drug=Alanine, disease=postmenopausal osteoporosis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Alanine, disease=postmenopausal osteoporosis | success | 20 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Alanine, disease=albinism-deafness syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Alanine, disease=albinism-deafness syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Alanine, disease=albinism-deafness syndrome | success | 0 |  |