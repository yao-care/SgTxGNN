# L-Lysine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | L-Lysine | |
| DrugBank ID | DB00123 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | gastroparesis (disease) | 99.77% | L5 | 0 | 1 | S0 | Hold |
| 2 | congenital prothrombin deficiency | 99.13% | L5 | 0 | 1 | S0 | Hold |
| 3 | obsolete vitamin D deficiency | 99.02% | L5 | 0 | 0 | S0 | Hold |
| 4 | dyspepsia | 98.68% | L4 | 1 | 4 | S0 | Hold |
| 5 | familial visceral myopathy | 98.37% | L5 | 0 | 0 | S0 | Hold |
| 6 | vitamin deficiency disorder | 98.21% | L4 | 3 | 18 | S1 | Research Question |
| 7 | hypophosphatemic rickets | 97.98% | L5 | 0 | 5 | S0 | Hold |
| 8 | renal tubular acidosis | 97.80% | L4 | 0 | 18 | S0 | Hold |
| 9 | biotin metabolic disease | 97.80% | L5 | 0 | 20 | S0 | Hold |
| 10 | postgastrectomy syndrome | 97.30% | L4 | 0 | 3 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=L-Lysine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=L-Lysine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=gastroparesis (disease) | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=L-Lysine, disease=gastroparesis (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=L-Lysine, disease=gastroparesis (disease) | success | 1 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=congenital prothrombin deficiency | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=L-Lysine, disease=congenital prothrombin deficiency | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=L-Lysine, disease=congenital prothrombin deficiency | success | 1 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=L-Lysine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=L-Lysine, disease=obsolete vitamin D deficiency | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=dyspepsia | success | 1 |  |
| 13 | ictrp | 2026-03-09 | drug=L-Lysine, disease=dyspepsia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=L-Lysine, disease=dyspepsia | success | 4 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=familial visceral myopathy | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=L-Lysine, disease=familial visceral myopathy | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=L-Lysine, disease=familial visceral myopathy | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=vitamin deficiency disorder | success | 3 |  |
| 19 | ictrp | 2026-03-09 | drug=L-Lysine, disease=vitamin deficiency disorder | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=L-Lysine, disease=vitamin deficiency disorder | success | 18 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=hypophosphatemic rickets | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=L-Lysine, disease=hypophosphatemic rickets | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=L-Lysine, disease=hypophosphatemic rickets | success | 5 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=renal tubular acidosis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=L-Lysine, disease=renal tubular acidosis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=L-Lysine, disease=renal tubular acidosis | success | 18 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=biotin metabolic disease | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=L-Lysine, disease=biotin metabolic disease | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=L-Lysine, disease=biotin metabolic disease | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=L-Lysine, disease=postgastrectomy syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=L-Lysine, disease=postgastrectomy syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=L-Lysine, disease=postgastrectomy syndrome | success | 3 |  |