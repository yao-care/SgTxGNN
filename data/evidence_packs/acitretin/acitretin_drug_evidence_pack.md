# Acitretin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Acitretin | |
| DrugBank ID | DB00459 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | acne (disease) | 99.94% | L4 | 1 | 18 | S1 | Research Question |
| 2 | pediatric systemic lupus erythematosus | 99.35% | L5 | 0 | 0 | S0 | Hold |
| 3 | fetal erythroblastosis | 99.28% | L5 | 0 | 0 | S0 | Hold |
| 4 | familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome | 99.10% | L5 | 0 | 0 | S0 | Hold |
| 5 | complement component 4a deficiency | 98.87% | L5 | 0 | 0 | S0 | Hold |
| 6 | subacute bacterial endocarditis | 98.46% | L5 | 0 | 0 | S0 | Hold |
| 7 | familial acanthosis nigricans | 98.43% | L5 | 0 | 0 | S0 | Research Question |
| 8 | prolapse of lacrimal gland | 98.42% | L5 | 0 | 0 | S0 | Hold |
| 9 | urticaria, familial localized heat | 98.36% | L5 | 0 | 0 | S0 | Hold |
| 10 | Sjogren syndrome | 98.34% | L4 | 0 | 5 | S1 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Acitretin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Acitretin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=acne (disease) | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Acitretin, disease=acne (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Acitretin, disease=acne (disease) | success | 18 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=pediatric systemic lupus erythematosus | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Acitretin, disease=pediatric systemic lupus erythematosus | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Acitretin, disease=pediatric systemic lupus erythematosus | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=fetal erythroblastosis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Acitretin, disease=fetal erythroblastosis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Acitretin, disease=fetal erythroblastosis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Acitretin, disease=familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Acitretin, disease=familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=complement component 4a deficiency | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Acitretin, disease=complement component 4a deficiency | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Acitretin, disease=complement component 4a deficiency | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=subacute bacterial endocarditis | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Acitretin, disease=subacute bacterial endocarditis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Acitretin, disease=subacute bacterial endocarditis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=familial acanthosis nigricans | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Acitretin, disease=familial acanthosis nigricans | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Acitretin, disease=familial acanthosis nigricans | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=prolapse of lacrimal gland | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Acitretin, disease=prolapse of lacrimal gland | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Acitretin, disease=prolapse of lacrimal gland | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=urticaria, familial localized heat | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Acitretin, disease=urticaria, familial localized heat | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Acitretin, disease=urticaria, familial localized heat | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Acitretin, disease=Sjogren syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Acitretin, disease=Sjogren syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Acitretin, disease=Sjogren syndrome | success | 5 |  |