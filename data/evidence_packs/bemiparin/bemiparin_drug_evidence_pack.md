# Bemiparin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Bemiparin | |
| DrugBank ID | DB09258 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | primary release disorder of platelets | 98.71% | L5 | 0 | 0 | S0 | Hold |
| 2 | Glanzmann thrombasthenia | 98.66% | L5 | 0 | 0 | S0 | Hold |
| 3 | pseudo-von Willebrand disease | 98.29% | L5 | 0 | 0 | S0 | Hold |
| 4 | hemorrhagic disorder due to a constitutional thrombocytopenia | 94.86% | L5 | 0 | 0 | S0 | Hold |
| 5 | bleeding diathesis due to a collagen receptor defect | 94.81% | L5 | 0 | 0 | S0 | Hold |
| 6 | Scott syndrome | 93.80% | L5 | 0 | 0 | S0 | Hold |
| 7 | fetal and neonatal alloimmune thrombocytopenia | 92.54% | L5 | 0 | 0 | S0 | Hold |
| 8 | platelet-type bleeding disorder | 90.24% | L5 | 1 | 0 | S0 | Hold |
| 9 | pulmonary embolism (disease) | 87.92% | L1 | 10 | 8 | S3 | Proceed with Guardrails |
| 10 | autosomal dominant macrothrombocytopenia | 87.21% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Bemiparin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Bemiparin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=primary release disorder of platelets | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Bemiparin, disease=primary release disorder of platelets | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Bemiparin, disease=primary release disorder of platelets | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=Glanzmann thrombasthenia | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Bemiparin, disease=Glanzmann thrombasthenia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Bemiparin, disease=Glanzmann thrombasthenia | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=pseudo-von Willebrand disease | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Bemiparin, disease=pseudo-von Willebrand disease | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Bemiparin, disease=pseudo-von Willebrand disease | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=hemorrhagic disorder due to a constitutional thrombocytopenia | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Bemiparin, disease=hemorrhagic disorder due to a constitutional thrombocytopenia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Bemiparin, disease=hemorrhagic disorder due to a constitutional thrombocytopenia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=bleeding diathesis due to a collagen receptor defect | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Bemiparin, disease=bleeding diathesis due to a collagen receptor defect | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Bemiparin, disease=bleeding diathesis due to a collagen receptor defect | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=Scott syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Bemiparin, disease=Scott syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Bemiparin, disease=Scott syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=fetal and neonatal alloimmune thrombocytopenia | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Bemiparin, disease=fetal and neonatal alloimmune thrombocytopenia | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Bemiparin, disease=fetal and neonatal alloimmune thrombocytopenia | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=platelet-type bleeding disorder | success | 1 |  |
| 25 | ictrp | 2026-03-10 | drug=Bemiparin, disease=platelet-type bleeding disorder | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Bemiparin, disease=platelet-type bleeding disorder | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=pulmonary embolism (disease) | success | 10 |  |
| 28 | ictrp | 2026-03-10 | drug=Bemiparin, disease=pulmonary embolism (disease) | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Bemiparin, disease=pulmonary embolism (disease) | success | 8 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Bemiparin, disease=autosomal dominant macrothrombocytopenia | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Bemiparin, disease=autosomal dominant macrothrombocytopenia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Bemiparin, disease=autosomal dominant macrothrombocytopenia | success | 0 |  |