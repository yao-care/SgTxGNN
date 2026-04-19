# Ambrisentan 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ambrisentan | |
| DrugBank ID | DB06403 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | pulmonary arteriovenous malformation (disease) | 99.41% | L4 | 0 | 1 | S0 | Hold |
| 2 | pulmonary arterial hypertension associated with congenital heart disease | 99.37% | L2 | 9 | 17 | S3 | Proceed with Guardrails |
| 3 | pulmonary arterial hypertension associated with connective tissue disease | 99.30% | L2 | 3 | 19 | S3 | Proceed with Guardrails |
| 4 | pulmonary arterial hypertension associated with chronic hemolytic anemia | 99.30% | L5 | 0 | 0 | S0 | Hold |
| 5 | pulmonary arterial hypertension associated with HIV infection | 99.30% | L1 | 1 | 4 | S3 | Proceed with Guardrails |
| 6 | pulmonary arterial hypertension associated with schistosomiasis | 99.30% | L5 | 0 | 0 | S0 | Hold |
| 7 | malformation syndrome with odontal and/or periodontal component | 99.19% | L5 | 0 | 20 | S0 | Hold |
| 8 | hypotrichosis simplex of the scalp | 99.15% | L5 | 0 | 0 | S0 | Hold |
| 9 | hypertrichosis (disease) | 99.14% | L5 | 0 | 0 | S0 | Hold |
| 10 | syndrome with a Dandy-Walker malformation as major feature | 99.12% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Ambrisentan | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Ambrisentan | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arteriovenous malformation (disease) | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arteriovenous malformation (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arteriovenous malformation (disease) | success | 1 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with congenital heart disease | success | 9 |  |
| 7 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with congenital heart disease | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with congenital heart disease | success | 17 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with connective tissue disease | success | 3 |  |
| 10 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with connective tissue disease | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with connective tissue disease | success | 19 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with chronic hemolytic anemia | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with chronic hemolytic anemia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with chronic hemolytic anemia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with HIV infection | success | 1 |  |
| 16 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with HIV infection | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with HIV infection | success | 4 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with schistosomiasis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with schistosomiasis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=pulmonary arterial hypertension associated with schistosomiasis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=malformation syndrome with odontal and/or periodontal component | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=malformation syndrome with odontal and/or periodontal component | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=malformation syndrome with odontal and/or periodontal component | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=hypertrichosis (disease) | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=hypertrichosis (disease) | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=hypertrichosis (disease) | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Ambrisentan, disease=syndrome with a Dandy-Walker malformation as major feature | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Ambrisentan, disease=syndrome with a Dandy-Walker malformation as major feature | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Ambrisentan, disease=syndrome with a Dandy-Walker malformation as major feature | success | 0 |  |