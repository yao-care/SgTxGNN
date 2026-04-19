# Deferiprone 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Deferiprone | |
| DrugBank ID | DB08826 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | hepatic porphyria | 99.20% | L4 | 0 | 2 | S1 | Research Question |
| 2 | hepatopulmonary syndrome | 99.20% | L5 | 0 | 0 | S0 | Hold |
| 3 | early-onset familial noncirrhotic portal hypertension | 99.20% | L5 | 0 | 0 | S0 | Hold |
| 4 | primitive portal vein thrombosis | 99.20% | L5 | 0 | 0 | S0 | Hold |
| 5 | hepatoportal sclerosis | 99.20% | L5 | 0 | 0 | S0 | Hold |
| 6 | idiopathic copper-associated cirrhosis | 99.20% | L5 | 0 | 0 | S0 | Hold |
| 7 | pyruvate kinase deficiency of red cells | 99.15% | L5 | 0 | 0 | S1 | Research Question |
| 8 | beta-thalassemia with other manifestations | 99.03% | L3 | 0 | 2 | S2 | Proceed with Guardrails |
| 9 | pyropoikilocytosis, hereditary | 99.02% | L5 | 0 | 0 | S1 | Research Question |
| 10 | partial deletion of the short arm of chromosome 16 | 98.92% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Deferiprone | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Deferiprone | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=hepatic porphyria | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Deferiprone, disease=hepatic porphyria | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Deferiprone, disease=hepatic porphyria | success | 2 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=hepatopulmonary syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Deferiprone, disease=hepatopulmonary syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Deferiprone, disease=hepatopulmonary syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=early-onset familial noncirrhotic portal hypertension | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Deferiprone, disease=early-onset familial noncirrhotic portal hypertension | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Deferiprone, disease=early-onset familial noncirrhotic portal hypertension | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=primitive portal vein thrombosis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Deferiprone, disease=primitive portal vein thrombosis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Deferiprone, disease=primitive portal vein thrombosis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=hepatoportal sclerosis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Deferiprone, disease=hepatoportal sclerosis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Deferiprone, disease=hepatoportal sclerosis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=idiopathic copper-associated cirrhosis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Deferiprone, disease=idiopathic copper-associated cirrhosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Deferiprone, disease=idiopathic copper-associated cirrhosis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=pyruvate kinase deficiency of red cells | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Deferiprone, disease=pyruvate kinase deficiency of red cells | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Deferiprone, disease=pyruvate kinase deficiency of red cells | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=beta-thalassemia with other manifestations | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Deferiprone, disease=beta-thalassemia with other manifestations | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Deferiprone, disease=beta-thalassemia with other manifestations | success | 2 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=pyropoikilocytosis, hereditary | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Deferiprone, disease=pyropoikilocytosis, hereditary | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Deferiprone, disease=pyropoikilocytosis, hereditary | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Deferiprone, disease=partial deletion of the short arm of chromosome 16 | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Deferiprone, disease=partial deletion of the short arm of chromosome 16 | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Deferiprone, disease=partial deletion of the short arm of chromosome 16 | success | 0 |  |