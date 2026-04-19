# Isotretinoin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Isotretinoin | |
| DrugBank ID | DB00982 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | malignant renovascular hypertension | 99.01% | L5 | 0 | 0 | S0 | Hold |
| 2 | malignant hypertensive renal disease | 99.01% | L5 | 0 | 0 | S0 | Hold |
| 3 | pulmonary hypertension with unclear multifactorial mechanism | 98.89% | L5 | 0 | 0 | S0 | Hold |
| 4 | pulmonary hypertension owing to lung disease and/or hypoxia | 98.89% | L5 | 0 | 20 | S0 | Hold |
| 5 | Braddock syndrome | 98.66% | L5 | 0 | 0 | S0 | Hold |
| 6 | chronic pulmonary heart disease | 88.70% | L3 | 1 | 0 | S1 | Research Question |
| 7 | cholangiocarcinoma, susceptibility to | 61.91% | L5 | 0 | 0 | S0 | Hold |
| 8 | obsolete functional visual loss | 59.19% | L5 | 0 | 0 | S0 | Hold |
| 9 | mitral valve prolapse, myxomatous | 59.11% | L5 | 0 | 0 | S0 | Hold |
| 10 | ocular tuberculosis | 58.68% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Isotretinoin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Isotretinoin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=malignant renovascular hypertension | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=malignant renovascular hypertension | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=malignant renovascular hypertension | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=malignant hypertensive renal disease | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=malignant hypertensive renal disease | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=malignant hypertensive renal disease | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=Braddock syndrome | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=Braddock syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=Braddock syndrome | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=chronic pulmonary heart disease | success | 1 |  |
| 19 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=chronic pulmonary heart disease | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=chronic pulmonary heart disease | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=cholangiocarcinoma, susceptibility to | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=cholangiocarcinoma, susceptibility to | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=cholangiocarcinoma, susceptibility to | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=obsolete functional visual loss | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=obsolete functional visual loss | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=obsolete functional visual loss | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=mitral valve prolapse, myxomatous | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=mitral valve prolapse, myxomatous | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=mitral valve prolapse, myxomatous | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Isotretinoin, disease=ocular tuberculosis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Isotretinoin, disease=ocular tuberculosis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Isotretinoin, disease=ocular tuberculosis | success | 0 |  |