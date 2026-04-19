# Clotrimazole 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clotrimazole | |
| DrugBank ID | DB00257 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | acne (disease) | 99.86% | L4 | 1 | 0 | S0 | Hold |
| 2 | vulvovaginitis | 99.59% | L1 | 22 | 20 | S3 | Proceed with Guardrails |
| 3 | postmenopausal atrophic vaginitis | 99.46% | L4 | 1 | 0 | S0 | Hold |
| 4 | trichomonal vulvovaginitis | 98.99% | L3 | 4 | 20 | S2 | Research Question |
| 5 | tinea profunda | 98.76% | L4 | 0 | 4 | S0 | Hold |
| 6 | ectothrix infectious disease | 98.74% | L5 | 0 | 0 | S0 | Hold |
| 7 | Majocchi granuloma | 98.74% | L4 | 0 | 4 | S0 | Hold |
| 8 | endothrix infectious disease | 98.65% | L5 | 0 | 0 | S0 | Hold |
| 9 | superficial mycosis | 98.62% | L2 | 3 | 20 | S3 | Proceed with Guardrails |
| 10 | dermatophytosis of scalp or beard | 98.59% | L4 | 0 | 20 | S1 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Clotrimazole | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Clotrimazole | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=acne (disease) | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=acne (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=acne (disease) | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=vulvovaginitis | success | 22 |  |
| 7 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=vulvovaginitis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=vulvovaginitis | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=postmenopausal atrophic vaginitis | success | 1 |  |
| 10 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=postmenopausal atrophic vaginitis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=postmenopausal atrophic vaginitis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=trichomonal vulvovaginitis | success | 4 |  |
| 13 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=trichomonal vulvovaginitis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=trichomonal vulvovaginitis | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=tinea profunda | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=tinea profunda | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=tinea profunda | success | 4 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=ectothrix infectious disease | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=ectothrix infectious disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=ectothrix infectious disease | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=Majocchi granuloma | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=Majocchi granuloma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=Majocchi granuloma | success | 4 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=endothrix infectious disease | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=endothrix infectious disease | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=endothrix infectious disease | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=superficial mycosis | success | 3 |  |
| 28 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=superficial mycosis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=superficial mycosis | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Clotrimazole, disease=dermatophytosis of scalp or beard | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Clotrimazole, disease=dermatophytosis of scalp or beard | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Clotrimazole, disease=dermatophytosis of scalp or beard | success | 20 |  |