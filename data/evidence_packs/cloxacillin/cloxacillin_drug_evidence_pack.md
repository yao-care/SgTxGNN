# Cloxacillin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cloxacillin | |
| DrugBank ID | DB01147 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | chronic rhinosinusitis | 98.31% | L5 | 0 | 0 | S0 | Hold |
| 2 | chronic ethmoidal sinusitis | 98.28% | L5 | 0 | 0 | S0 | Hold |
| 3 | paranasal sinus neoplasm (disease) | 98.17% | L5 | 0 | 0 | S0 | Hold |
| 4 | epiglottitis | 98.12% | L4 | 0 | 3 | S1 | Research Question |
| 5 | bacterial arthritis | 97.68% | L3 | 2 | 20 | S2 | Proceed with Guardrails |
| 6 | pneumonia | 97.22% | L4 | 2 | 20 | S1 | Research Question |
| 7 | laryngitis | 96.32% | L4 | 0 | 10 | S0 | Hold |
| 8 | celiac trunk compression syndrome | 95.93% | L5 | 0 | 0 | S0 | Hold |
| 9 | abdominal cystic lymphangioma | 95.93% | L5 | 0 | 0 | S0 | Hold |
| 10 | abdominal ectopic pregnancy | 95.93% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Cloxacillin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Cloxacillin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=chronic rhinosinusitis | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=chronic rhinosinusitis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=chronic rhinosinusitis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=epiglottitis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=epiglottitis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=epiglottitis | success | 3 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=bacterial arthritis | success | 2 |  |
| 16 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=bacterial arthritis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=bacterial arthritis | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=pneumonia | success | 2 |  |
| 19 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=pneumonia | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=pneumonia | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=laryngitis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=laryngitis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=laryngitis | success | 10 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=celiac trunk compression syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=celiac trunk compression syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=celiac trunk compression syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=abdominal cystic lymphangioma | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=abdominal cystic lymphangioma | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=abdominal cystic lymphangioma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Cloxacillin, disease=abdominal ectopic pregnancy | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Cloxacillin, disease=abdominal ectopic pregnancy | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Cloxacillin, disease=abdominal ectopic pregnancy | success | 0 |  |