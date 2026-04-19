# Human thrombin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Human thrombin | |
| DrugBank ID | DB11571 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | primary release disorder of platelets | 96.95% | pending | 13 | 20 | pending | pending |
| 2 | Glanzmann thrombasthenia | 96.64% | pending | 2 | 20 | pending | pending |
| 3 | pseudo-von Willebrand disease | 96.52% | pending | 0 | 2 | pending | pending |
| 4 | non-syndromic esophageal malformation | 91.68% | pending | 0 | 0 | pending | pending |
| 5 | hemorrhagic disorder due to a constitutional thrombocytopenia | 91.66% | pending | 0 | 3 | pending | pending |
| 6 | bleeding diathesis due to a collagen receptor defect | 91.55% | pending | 0 | 20 | pending | pending |
| 7 | Scott syndrome | 91.50% | pending | 2 | 20 | pending | pending |
| 8 | esophageal disease | 86.54% | pending | 10 | 20 | pending | pending |
| 9 | fetal and neonatal alloimmune thrombocytopenia | 86.21% | pending | 0 | 4 | pending | pending |
| 10 | platelet-type bleeding disorder | 86.13% | pending | 15 | 8 | pending | pending |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Human thrombin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Human thrombin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=primary release disorder of platelets | success | 13 |  |
| 4 | ictrp | 2026-03-10 | drug=Human thrombin, disease=primary release disorder of platelets | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Human thrombin, disease=primary release disorder of platelets | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=Glanzmann thrombasthenia | success | 2 |  |
| 7 | ictrp | 2026-03-10 | drug=Human thrombin, disease=Glanzmann thrombasthenia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Human thrombin, disease=Glanzmann thrombasthenia | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=pseudo-von Willebrand disease | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Human thrombin, disease=pseudo-von Willebrand disease | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Human thrombin, disease=pseudo-von Willebrand disease | success | 2 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=non-syndromic esophageal malformation | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Human thrombin, disease=non-syndromic esophageal malformation | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Human thrombin, disease=non-syndromic esophageal malformation | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=hemorrhagic disorder due to a constitutional thrombocytopenia | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Human thrombin, disease=hemorrhagic disorder due to a constitutional thrombocytopenia | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Human thrombin, disease=hemorrhagic disorder due to a constitutional thrombocytopenia | success | 3 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=bleeding diathesis due to a collagen receptor defect | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Human thrombin, disease=bleeding diathesis due to a collagen receptor defect | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Human thrombin, disease=bleeding diathesis due to a collagen receptor defect | success | 20 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=Scott syndrome | success | 2 |  |
| 22 | ictrp | 2026-03-10 | drug=Human thrombin, disease=Scott syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Human thrombin, disease=Scott syndrome | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=esophageal disease | success | 10 |  |
| 25 | ictrp | 2026-03-10 | drug=Human thrombin, disease=esophageal disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Human thrombin, disease=esophageal disease | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=fetal and neonatal alloimmune thrombocytopenia | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Human thrombin, disease=fetal and neonatal alloimmune thrombocytopenia | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Human thrombin, disease=fetal and neonatal alloimmune thrombocytopenia | success | 4 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Human thrombin, disease=platelet-type bleeding disorder | success | 15 |  |
| 31 | ictrp | 2026-03-10 | drug=Human thrombin, disease=platelet-type bleeding disorder | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Human thrombin, disease=platelet-type bleeding disorder | success | 8 |  |