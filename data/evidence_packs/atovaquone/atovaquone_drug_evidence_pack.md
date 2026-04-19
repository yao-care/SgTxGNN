# Atovaquone 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Atovaquone | |
| DrugBank ID | DB01117 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | leprosy | 94.24% | L5 | 0 | 1 | S0 | Hold |
| 2 | nocardiosis | 90.90% | L4 | 0 | 9 | S1 | Hold |
| 3 | facial nerve palsy due to herpes zoster infection | 89.16% | L5 | 0 | 0 | S0 | Hold |
| 4 | acne (disease) | 88.00% | L5 | 0 | 0 | S0 | Hold |
| 5 | toxoplasmosis | 86.67% | L2 | 3 | 20 | S3 | Proceed with Guardrails |
| 6 | ocular toxoplasmosis | 85.27% | L3 | 1 | 19 | S2 | Proceed with Guardrails |
| 7 | creeping myiasis | 85.07% | L5 | 0 | 0 | S0 | Hold |
| 8 | furuncular myiasis | 85.07% | L5 | 0 | 0 | S0 | Hold |
| 9 | wound myiasis | 85.07% | L5 | 0 | 0 | S0 | Hold |
| 10 | myiasis | 82.88% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Atovaquone | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Atovaquone | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=leprosy | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Atovaquone, disease=leprosy | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Atovaquone, disease=leprosy | success | 1 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=nocardiosis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Atovaquone, disease=nocardiosis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Atovaquone, disease=nocardiosis | success | 9 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=facial nerve palsy due to herpes zoster infection | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Atovaquone, disease=facial nerve palsy due to herpes zoster infection | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Atovaquone, disease=facial nerve palsy due to herpes zoster infection | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=acne (disease) | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Atovaquone, disease=acne (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Atovaquone, disease=acne (disease) | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=toxoplasmosis | success | 3 |  |
| 16 | ictrp | 2026-03-10 | drug=Atovaquone, disease=toxoplasmosis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Atovaquone, disease=toxoplasmosis | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=ocular toxoplasmosis | success | 1 |  |
| 19 | ictrp | 2026-03-10 | drug=Atovaquone, disease=ocular toxoplasmosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Atovaquone, disease=ocular toxoplasmosis | success | 19 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=creeping myiasis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Atovaquone, disease=creeping myiasis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Atovaquone, disease=creeping myiasis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=furuncular myiasis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Atovaquone, disease=furuncular myiasis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Atovaquone, disease=furuncular myiasis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=wound myiasis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Atovaquone, disease=wound myiasis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Atovaquone, disease=wound myiasis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Atovaquone, disease=myiasis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Atovaquone, disease=myiasis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Atovaquone, disease=myiasis | success | 0 |  |