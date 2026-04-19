# Atenolol 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Atenolol | |
| DrugBank ID | DB00335 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | posterolateral myocardial infarction | 99.87% | L4 | 0 | 0 | S1 | Research Question |
| 2 | posteroinferior myocardial infarction | 99.87% | L4 | 0 | 1 | S1 | Research Question |
| 3 | malignant renovascular hypertension | 99.85% | L4 | 0 | 1 | S0 | Hold |
| 4 | malignant hypertensive renal disease | 99.85% | L5 | 0 | 0 | S0 | Hold |
| 5 | pulmonary hypertension with unclear multifactorial mechanism | 99.84% | L5 | 0 | 0 | S0 | Hold |
| 6 | pulmonary hypertension owing to lung disease and/or hypoxia | 99.84% | L5 | 0 | 20 | S0 | Hold |
| 7 | septal myocardial infarction | 99.84% | L4 | 0 | 1 | S1 | Research Question |
| 8 | Braddock syndrome | 99.80% | L5 | 0 | 0 | S0 | Hold |
| 9 | chronic pulmonary heart disease | 99.04% | L3 | 1 | 15 | S2 | Proceed with Guardrails |
| 10 | primary hereditary glaucoma | 98.84% | L4 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Atenolol | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Atenolol | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=posterolateral myocardial infarction | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Atenolol, disease=posterolateral myocardial infarction | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Atenolol, disease=posterolateral myocardial infarction | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=posteroinferior myocardial infarction | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Atenolol, disease=posteroinferior myocardial infarction | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Atenolol, disease=posteroinferior myocardial infarction | success | 1 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=malignant renovascular hypertension | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Atenolol, disease=malignant renovascular hypertension | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Atenolol, disease=malignant renovascular hypertension | success | 1 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=malignant hypertensive renal disease | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Atenolol, disease=malignant hypertensive renal disease | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Atenolol, disease=malignant hypertensive renal disease | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Atenolol, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Atenolol, disease=pulmonary hypertension with unclear multifactorial mechanism | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Atenolol, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Atenolol, disease=pulmonary hypertension owing to lung disease and/or hypoxia | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=septal myocardial infarction | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Atenolol, disease=septal myocardial infarction | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Atenolol, disease=septal myocardial infarction | success | 1 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=Braddock syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Atenolol, disease=Braddock syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Atenolol, disease=Braddock syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=chronic pulmonary heart disease | success | 1 |  |
| 28 | ictrp | 2026-03-09 | drug=Atenolol, disease=chronic pulmonary heart disease | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Atenolol, disease=chronic pulmonary heart disease | success | 15 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Atenolol, disease=primary hereditary glaucoma | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Atenolol, disease=primary hereditary glaucoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Atenolol, disease=primary hereditary glaucoma | success | 0 |  |