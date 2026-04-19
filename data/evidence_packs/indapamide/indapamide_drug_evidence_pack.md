# Indapamide 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Indapamide | |
| DrugBank ID | DB00808 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | chronic pulmonary heart disease | 92.97% | L4 | 0 | 3 | S1 | Hold |
| 2 | pulmonary hypertension with unclear multifactorial mechanism | 92.75% | L5 | 0 | 0 | S0 | Hold |
| 3 | pulmonary hypertension owing to lung disease and/or hypoxia | 92.75% | L5 | 0 | 20 | S0 | Hold |
| 4 | malignant hypertensive renal disease | 92.73% | L4 | 0 | 0 | S1 | Hold |
| 5 | malignant renovascular hypertension | 92.73% | L4 | 0 | 0 | S1 | Hold |
| 6 | acute pulmonary heart disease | 91.02% | L5 | 0 | 1 | S0 | Hold |
| 7 | Braddock syndrome | 90.42% | L5 | 0 | 0 | S0 | Hold |
| 8 | primary hereditary glaucoma | 84.53% | L5 | 0 | 0 | S0 | Hold |
| 9 | open-angle glaucoma | 79.64% | L4 | 0 | 1 | S0 | Hold |
| 10 | chronic kidney disease | 77.97% | L3 | 3 | 20 | S2 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Indapamide | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Indapamide | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=chronic pulmonary heart disease | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Indapamide, disease=chronic pulmonary heart disease | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Indapamide, disease=chronic pulmonary heart disease | success | 3 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Indapamide, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Indapamide, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Indapamide, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Indapamide, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=malignant hypertensive renal disease | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Indapamide, disease=malignant hypertensive renal disease | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Indapamide, disease=malignant hypertensive renal disease | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=malignant renovascular hypertension | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Indapamide, disease=malignant renovascular hypertension | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Indapamide, disease=malignant renovascular hypertension | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=acute pulmonary heart disease | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Indapamide, disease=acute pulmonary heart disease | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Indapamide, disease=acute pulmonary heart disease | success | 1 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=Braddock syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Indapamide, disease=Braddock syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Indapamide, disease=Braddock syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=primary hereditary glaucoma | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Indapamide, disease=primary hereditary glaucoma | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Indapamide, disease=primary hereditary glaucoma | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=open-angle glaucoma | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Indapamide, disease=open-angle glaucoma | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Indapamide, disease=open-angle glaucoma | success | 1 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Indapamide, disease=chronic kidney disease | success | 3 |  |
| 31 | ictrp | 2026-03-10 | drug=Indapamide, disease=chronic kidney disease | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Indapamide, disease=chronic kidney disease | success | 20 |  |