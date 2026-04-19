# Diltiazem 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Diltiazem | |
| DrugBank ID | DB00343 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | obsolete susceptibility to ischemic stroke | 99.08% | L5 | 0 | 0 | S0 | Hold |
| 2 | brain stem infarction | 98.23% | L5 | 0 | 0 | S0 | Hold |
| 3 | obsolete bundle branch block | 97.88% | L5 | 0 | 0 | S0 | Hold |
| 4 | cerebrovascular disorder | 97.63% | L3 | 6 | 20 | S2 | Research Question |
| 5 | pulmonary hypertension owing to lung disease and/or hypoxia | 97.19% | L4 | 0 | 20 | S1 | Hold |
| 6 | pulmonary hypertension with unclear multifactorial mechanism | 97.19% | L5 | 0 | 0 | S0 | Hold |
| 7 | malignant hypertensive renal disease | 97.16% | L5 | 0 | 0 | S0 | Research Question |
| 8 | malignant renovascular hypertension | 97.16% | L5 | 0 | 0 | S0 | Hold |
| 9 | ABri amyloidosis | 96.98% | L5 | 0 | 0 | S0 | Hold |
| 10 | Braddock syndrome | 96.70% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Diltiazem | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Diltiazem | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=obsolete susceptibility to ischemic stroke | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Diltiazem, disease=obsolete susceptibility to ischemic stroke | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Diltiazem, disease=obsolete susceptibility to ischemic stroke | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=brain stem infarction | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Diltiazem, disease=brain stem infarction | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Diltiazem, disease=brain stem infarction | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=obsolete bundle branch block | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Diltiazem, disease=obsolete bundle branch block | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Diltiazem, disease=obsolete bundle branch block | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=cerebrovascular disorder | success | 6 |  |
| 13 | ictrp | 2026-03-09 | drug=Diltiazem, disease=cerebrovascular disorder | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Diltiazem, disease=cerebrovascular disorder | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Diltiazem, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Diltiazem, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 20 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Diltiazem, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Diltiazem, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=malignant hypertensive renal disease | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Diltiazem, disease=malignant hypertensive renal disease | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Diltiazem, disease=malignant hypertensive renal disease | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=malignant renovascular hypertension | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Diltiazem, disease=malignant renovascular hypertension | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Diltiazem, disease=malignant renovascular hypertension | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=ABri amyloidosis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Diltiazem, disease=ABri amyloidosis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Diltiazem, disease=ABri amyloidosis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Diltiazem, disease=Braddock syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Diltiazem, disease=Braddock syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Diltiazem, disease=Braddock syndrome | success | 0 |  |