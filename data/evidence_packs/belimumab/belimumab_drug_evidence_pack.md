# Belimumab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Belimumab | |
| DrugBank ID | DB08879 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | primary release disorder of platelets | 99.96% | L5 | 1 | 0 | S0 | Hold |
| 2 | pseudo-von Willebrand disease | 99.96% | L5 | 0 | 0 | S0 | Hold |
| 3 | Glanzmann thrombasthenia | 99.88% | L5 | 0 | 0 | S0 | Hold |
| 4 | fetal and neonatal alloimmune thrombocytopenia | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 5 | severe nonproliferative diabetic retinopathy | 99.05% | L5 | 0 | 0 | S0 | Hold |
| 6 | autosomal dominant macrothrombocytopenia | 99.04% | L5 | 0 | 0 | S0 | Hold |
| 7 | granulomatous disease, chronic, autosomal recessive, 5 | 97.91% | L5 | 0 | 0 | S0 | Hold |
| 8 | anus disease | 97.89% | L5 | 0 | 0 | S0 | Hold |
| 9 | inflammatory bowel disease | 97.76% | L4 | 2 | 9 | S1 | Research Question |
| 10 | granulomatous disease with defect in neutrophil chemotaxis | 97.71% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Belimumab | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Belimumab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=primary release disorder of platelets | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Belimumab, disease=primary release disorder of platelets | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Belimumab, disease=primary release disorder of platelets | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=pseudo-von Willebrand disease | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Belimumab, disease=pseudo-von Willebrand disease | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Belimumab, disease=pseudo-von Willebrand disease | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=Glanzmann thrombasthenia | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Belimumab, disease=Glanzmann thrombasthenia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Belimumab, disease=Glanzmann thrombasthenia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=fetal and neonatal alloimmune thrombocytopenia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Belimumab, disease=fetal and neonatal alloimmune thrombocytopenia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Belimumab, disease=fetal and neonatal alloimmune thrombocytopenia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=severe nonproliferative diabetic retinopathy | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Belimumab, disease=severe nonproliferative diabetic retinopathy | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Belimumab, disease=severe nonproliferative diabetic retinopathy | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=autosomal dominant macrothrombocytopenia | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Belimumab, disease=autosomal dominant macrothrombocytopenia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Belimumab, disease=autosomal dominant macrothrombocytopenia | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=granulomatous disease, chronic, autosomal recessive, 5 | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Belimumab, disease=granulomatous disease, chronic, autosomal recessive, 5 | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Belimumab, disease=granulomatous disease, chronic, autosomal recessive, 5 | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=anus disease | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Belimumab, disease=anus disease | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Belimumab, disease=anus disease | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=inflammatory bowel disease | success | 2 |  |
| 28 | ictrp | 2026-03-09 | drug=Belimumab, disease=inflammatory bowel disease | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Belimumab, disease=inflammatory bowel disease | success | 9 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Belimumab, disease=granulomatous disease with defect in neutrophil chemotaxis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Belimumab, disease=granulomatous disease with defect in neutrophil chemotaxis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Belimumab, disease=granulomatous disease with defect in neutrophil chemotaxis | success | 0 |  |