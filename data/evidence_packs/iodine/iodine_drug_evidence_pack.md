# Iodine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Iodine | |
| DrugBank ID | DB05382 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Sjogren syndrome | 94.09% | L4 | 0 | 20 | S0 | Hold |
| 2 | prolapse of lacrimal gland | 93.64% | L5 | 0 | 0 | S0 | Hold |
| 3 | acne (disease) | 93.11% | L3 | 3 | 11 | S1 | Research Question |
| 4 | seborrheic keratosis | 91.41% | L4 | 1 | 2 | S0 | Hold |
| 5 | fetal erythroblastosis | 91.03% | L5 | 0 | 20 | S0 | Hold |
| 6 | recurrent corneal erosion | 90.66% | L4 | 0 | 1 | S0 | Hold |
| 7 | keratitis | 89.70% | L2 | 5 | 20 | S2 | Proceed with Guardrails |
| 8 | vulvar inverted follicular keratosis | 89.63% | L5 | 0 | 0 | S0 | Hold |
| 9 | peptic esophagitis | 89.39% | L4 | 1 | 6 | S0 | Hold |
| 10 | lacrimal gland neoplasm | 89.35% | L4 | 3 | 20 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Iodine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Iodine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=Sjogren syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Iodine, disease=Sjogren syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Iodine, disease=Sjogren syndrome | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=prolapse of lacrimal gland | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Iodine, disease=prolapse of lacrimal gland | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Iodine, disease=prolapse of lacrimal gland | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=acne (disease) | success | 3 |  |
| 10 | ictrp | 2026-03-10 | drug=Iodine, disease=acne (disease) | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Iodine, disease=acne (disease) | success | 11 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=seborrheic keratosis | success | 1 |  |
| 13 | ictrp | 2026-03-10 | drug=Iodine, disease=seborrheic keratosis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Iodine, disease=seborrheic keratosis | success | 2 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=fetal erythroblastosis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Iodine, disease=fetal erythroblastosis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Iodine, disease=fetal erythroblastosis | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=recurrent corneal erosion | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Iodine, disease=recurrent corneal erosion | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Iodine, disease=recurrent corneal erosion | success | 1 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=keratitis | success | 5 |  |
| 22 | ictrp | 2026-03-10 | drug=Iodine, disease=keratitis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Iodine, disease=keratitis | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=vulvar inverted follicular keratosis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Iodine, disease=vulvar inverted follicular keratosis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Iodine, disease=vulvar inverted follicular keratosis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=peptic esophagitis | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Iodine, disease=peptic esophagitis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Iodine, disease=peptic esophagitis | success | 6 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Iodine, disease=lacrimal gland neoplasm | success | 3 |  |
| 31 | ictrp | 2026-03-10 | drug=Iodine, disease=lacrimal gland neoplasm | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Iodine, disease=lacrimal gland neoplasm | success | 20 |  |