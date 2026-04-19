# Aspartic acid 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Aspartic acid | |
| DrugBank ID | DB00128 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | renal tubular acidosis | 99.47% | L4 | 1 | 10 | S1 | Research Question |
| 2 | esophageal varices with bleeding | 91.38% | L5 | 7 | 2 | S0 | Hold |
| 3 | esophageal varices without bleeding | 91.38% | L5 | 1 | 2 | S0 | Hold |
| 4 | dyspepsia | 89.95% | L4 | 36 | 8 | S1 | Research Question |
| 5 | renal hypomagnesemia | 82.74% | L4 | 0 | 5 | S1 | Research Question |
| 6 | Alstrom syndrome | 82.61% | L5 | 0 | 1 | S0 | Hold |
| 7 | hypophosphatemia (disease) | 82.60% | L5 | 34 | 5 | S0 | Hold |
| 8 | varicose disease | 81.60% | L5 | 5 | 4 | S0 | Hold |
| 9 | HELIX syndrome | 80.46% | L5 | 0 | 15 | S0 | Hold |
| 10 | Pendred syndrome | 79.37% | L5 | 0 | 1 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Aspartic acid | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Aspartic acid | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=renal tubular acidosis | success | 1 |  |
| 4 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=renal tubular acidosis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=renal tubular acidosis | success | 10 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=esophageal varices with bleeding | success | 7 |  |
| 7 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=esophageal varices with bleeding | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=esophageal varices with bleeding | success | 2 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=esophageal varices without bleeding | success | 1 |  |
| 10 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=esophageal varices without bleeding | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=esophageal varices without bleeding | success | 2 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=dyspepsia | success | 36 |  |
| 13 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=dyspepsia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=dyspepsia | success | 8 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=renal hypomagnesemia | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=renal hypomagnesemia | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=renal hypomagnesemia | success | 5 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=Alstrom syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=Alstrom syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=Alstrom syndrome | success | 1 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=hypophosphatemia (disease) | success | 34 |  |
| 22 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=hypophosphatemia (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=hypophosphatemia (disease) | success | 5 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=varicose disease | success | 5 |  |
| 25 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=varicose disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=varicose disease | success | 4 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=HELIX syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=HELIX syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=HELIX syndrome | success | 15 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Aspartic acid, disease=Pendred syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Aspartic acid, disease=Pendred syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Aspartic acid, disease=Pendred syndrome | success | 1 |  |