# Desogestrel 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Desogestrel | |
| DrugBank ID | DB00304 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | amenorrhea (disease) | 99.96% | L3 | 2 | 16 | S1 | Research Question |
| 2 | blunt duct adenosis of breast | 99.92% | L5 | 0 | 0 | S0 | Hold |
| 3 | apocrine adenosis of breast | 99.92% | L5 | 0 | 0 | S0 | Hold |
| 4 | acne (disease) | 99.91% | L2 | 1 | 20 | S2 | Proceed with Guardrails |
| 5 | breast abscess | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 6 | fat necrosis of breast | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 7 | lactation disease | 99.87% | L3 | 2 | 4 | S1 | Research Question |
| 8 | breast adenosis | 99.85% | L5 | 0 | 0 | S0 | Hold |
| 9 | primary ovarian failure | 99.72% | L5 | 0 | 0 | S0 | Hold |
| 10 | symptomatic form of fragile X syndrome in female carrier | 99.55% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Desogestrel | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Desogestrel | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=amenorrhea (disease) | success | 2 |  |
| 4 | ictrp | 2026-03-09 | drug=Desogestrel, disease=amenorrhea (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Desogestrel, disease=amenorrhea (disease) | success | 16 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=blunt duct adenosis of breast | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Desogestrel, disease=blunt duct adenosis of breast | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Desogestrel, disease=blunt duct adenosis of breast | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=apocrine adenosis of breast | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Desogestrel, disease=apocrine adenosis of breast | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Desogestrel, disease=apocrine adenosis of breast | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=acne (disease) | success | 1 |  |
| 13 | ictrp | 2026-03-09 | drug=Desogestrel, disease=acne (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Desogestrel, disease=acne (disease) | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=breast abscess | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Desogestrel, disease=breast abscess | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Desogestrel, disease=breast abscess | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=fat necrosis of breast | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Desogestrel, disease=fat necrosis of breast | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Desogestrel, disease=fat necrosis of breast | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=lactation disease | success | 2 |  |
| 22 | ictrp | 2026-03-09 | drug=Desogestrel, disease=lactation disease | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Desogestrel, disease=lactation disease | success | 4 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=breast adenosis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Desogestrel, disease=breast adenosis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Desogestrel, disease=breast adenosis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=primary ovarian failure | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Desogestrel, disease=primary ovarian failure | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Desogestrel, disease=primary ovarian failure | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Desogestrel, disease=symptomatic form of fragile X syndrome in female carrier | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Desogestrel, disease=symptomatic form of fragile X syndrome in female carrier | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Desogestrel, disease=symptomatic form of fragile X syndrome in female carrier | success | 0 |  |