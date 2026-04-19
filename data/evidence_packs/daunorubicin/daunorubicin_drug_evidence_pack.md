# Daunorubicin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Daunorubicin | |
| DrugBank ID | DB00694 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Hodgkins lymphoma | 99.81% | L3 | 50 | 20 | S2 | Research Question |
| 2 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.80% | L5 | 0 | 0 | S0 | Hold |
| 3 | ganglioneuroblastoma (disease) | 99.80% | L3 | 5 | 4 | S1 | Research Question |
| 4 | neuroblastoma | 99.78% | L3 | 49 | 20 | S2 | Research Question |
| 5 | ALK-positive large B-cell lymphoma | 99.78% | L3 | 4 | 10 | S1 | Research Question |
| 6 | adenosarcoma | 99.77% | L4 | 0 | 11 | S0 | Hold |
| 7 | retroperitoneal neoplasm | 99.77% | L3 | 5 | 20 | S1 | Research Question |
| 8 | small cell lung carcinoma | 99.76% | L3 | 31 | 20 | S2 | Research Question |
| 9 | primary pulmonary lymphoma | 99.76% | L3 | 17 | 20 | S1 | Research Question |
| 10 | pulmonary blastoma | 99.76% | L4 | 2 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Daunorubicin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Daunorubicin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=Hodgkins lymphoma | success | 50 |  |
| 4 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=Hodgkins lymphoma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=Hodgkins lymphoma | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=vertebral anomalies and variable endocrine and T-cell dysfunction | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=ganglioneuroblastoma (disease) | success | 5 |  |
| 10 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=ganglioneuroblastoma (disease) | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=ganglioneuroblastoma (disease) | success | 4 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=neuroblastoma | success | 49 |  |
| 13 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=neuroblastoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=neuroblastoma | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=ALK-positive large B-cell lymphoma | success | 4 |  |
| 16 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=ALK-positive large B-cell lymphoma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=ALK-positive large B-cell lymphoma | success | 10 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=adenosarcoma | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=adenosarcoma | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=adenosarcoma | success | 11 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=retroperitoneal neoplasm | success | 5 |  |
| 22 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=retroperitoneal neoplasm | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=retroperitoneal neoplasm | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=small cell lung carcinoma | success | 31 |  |
| 25 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=small cell lung carcinoma | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=small cell lung carcinoma | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=primary pulmonary lymphoma | success | 17 |  |
| 28 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=primary pulmonary lymphoma | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=primary pulmonary lymphoma | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Daunorubicin, disease=pulmonary blastoma | success | 2 |  |
| 31 | ictrp | 2026-03-09 | drug=Daunorubicin, disease=pulmonary blastoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Daunorubicin, disease=pulmonary blastoma | success | 0 |  |