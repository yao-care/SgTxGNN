# Iloprost 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Iloprost | |
| DrugBank ID | DB01088 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | hypotrichosis simplex of the scalp | 99.45% | L5 | 0 | 0 | S0 | Hold |
| 2 | congenital hypotrichosis milia | 99.33% | L5 | 0 | 0 | S0 | Hold |
| 3 | pulmonary arterial hypertension associated with congenital heart disease | 99.32% | L3 | 1 | 20 | S2 | Proceed with Guardrails |
| 4 | pulmonary arteriovenous malformation (disease) | 99.31% | L4 | 0 | 1 | S1 | Research Question |
| 5 | pulmonary arterial hypertension associated with schistosomiasis | 99.21% | L4 | 0 | 1 | S1 | Research Question |
| 6 | pulmonary arterial hypertension associated with connective tissue disease | 99.21% | L3 | 0 | 20 | S2 | Proceed with Guardrails |
| 7 | pulmonary arterial hypertension associated with HIV infection | 99.21% | L2 | 1 | 4 | S2 | Proceed with Guardrails |
| 8 | pulmonary arterial hypertension associated with chronic hemolytic anemia | 99.21% | L5 | 0 | 0 | S0 | Hold |
| 9 | diffuse alopecia areata | 99.10% | L5 | 0 | 0 | S0 | Hold |
| 10 | alopecia | 98.42% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Iloprost | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Iloprost | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Iloprost, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Iloprost, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=congenital hypotrichosis milia | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Iloprost, disease=congenital hypotrichosis milia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Iloprost, disease=congenital hypotrichosis milia | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with congenital heart disease | success | 1 |  |
| 10 | ictrp | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with congenital heart disease | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with congenital heart disease | success | 20 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=pulmonary arteriovenous malformation (disease) | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Iloprost, disease=pulmonary arteriovenous malformation (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Iloprost, disease=pulmonary arteriovenous malformation (disease) | success | 1 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with schistosomiasis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with schistosomiasis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with schistosomiasis | success | 1 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with connective tissue disease | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with connective tissue disease | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with connective tissue disease | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with HIV infection | success | 1 |  |
| 22 | ictrp | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with HIV infection | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with HIV infection | success | 4 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with chronic hemolytic anemia | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with chronic hemolytic anemia | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Iloprost, disease=pulmonary arterial hypertension associated with chronic hemolytic anemia | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=diffuse alopecia areata | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Iloprost, disease=diffuse alopecia areata | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Iloprost, disease=diffuse alopecia areata | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Iloprost, disease=alopecia | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Iloprost, disease=alopecia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Iloprost, disease=alopecia | success | 0 |  |