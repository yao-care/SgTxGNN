# Cilastatin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cilastatin | |
| DrugBank ID | DB01597 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | staphylococcus aureus infection | 99.94% | L2 | 3 | 20 | S2 | Research Question |
| 2 | chronic rhinosinusitis | 99.90% | L5 | 0 | 0 | S0 | Hold |
| 3 | chronic ethmoidal sinusitis | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 4 | sinusitis | 99.88% | L4 | 0 | 6 | S0 | Hold |
| 5 | paranasal sinus neoplasm (disease) | 99.86% | L5 | 0 | 0 | S0 | Hold |
| 6 | pneumonia | 99.81% | L1 | 18 | 20 | S3 | Proceed with Guardrails |
| 7 | paratyphoid fever | 99.65% | L5 | 0 | 0 | S0 | Hold |
| 8 | bronchitis | 99.65% | L3 | 0 | 13 | S1 | Research Question |
| 9 | diffuse scleroderma | 99.55% | L5 | 0 | 0 | S0 | Hold |
| 10 | salmonellosis | 99.43% | L3 | 0 | 9 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Cilastatin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Cilastatin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=staphylococcus aureus infection | success | 3 |  |
| 4 | ictrp | 2026-03-09 | drug=Cilastatin, disease=staphylococcus aureus infection | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Cilastatin, disease=staphylococcus aureus infection | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=chronic rhinosinusitis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Cilastatin, disease=chronic rhinosinusitis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Cilastatin, disease=chronic rhinosinusitis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Cilastatin, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Cilastatin, disease=chronic ethmoidal sinusitis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=sinusitis | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Cilastatin, disease=sinusitis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Cilastatin, disease=sinusitis | success | 6 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Cilastatin, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Cilastatin, disease=paranasal sinus neoplasm (disease) | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=pneumonia | success | 18 |  |
| 19 | ictrp | 2026-03-09 | drug=Cilastatin, disease=pneumonia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Cilastatin, disease=pneumonia | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=paratyphoid fever | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Cilastatin, disease=paratyphoid fever | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Cilastatin, disease=paratyphoid fever | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=bronchitis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Cilastatin, disease=bronchitis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Cilastatin, disease=bronchitis | success | 13 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=diffuse scleroderma | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Cilastatin, disease=diffuse scleroderma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Cilastatin, disease=diffuse scleroderma | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Cilastatin, disease=salmonellosis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Cilastatin, disease=salmonellosis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Cilastatin, disease=salmonellosis | success | 9 |  |