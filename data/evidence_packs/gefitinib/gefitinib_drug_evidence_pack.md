# Gefitinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Gefitinib | |
| DrugBank ID | DB00317 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | fibromatosis, gingival | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 2 | fibroma of lung | 99.86% | L5 | 0 | 0 | S0 | Hold |
| 3 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 99.86% | L5 | 0 | 20 | S0 | Hold |
| 4 | hamartoma of lung | 99.86% | L5 | 0 | 0 | S0 | Hold |
| 5 | lung hilum carcinoma | 99.86% | L4 | 0 | 1 | S0 | Hold |
| 6 | lung benign neoplasm | 99.85% | L4 | 0 | 20 | S0 | Hold |
| 7 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 99.84% | L5 | 0 | 20 | S0 | Hold |
| 8 | pulmonary sulcus neoplasm | 99.84% | L4 | 0 | 2 | S0 | Research Question |
| 9 | lung germ cell tumor | 99.84% | L3 | 1 | 20 | S1 | Research Question |
| 10 | junctional epidermolysis bullosa | 99.84% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Gefitinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Gefitinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=fibromatosis, gingival | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Gefitinib, disease=fibromatosis, gingival | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Gefitinib, disease=fibromatosis, gingival | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=fibroma of lung | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Gefitinib, disease=fibroma of lung | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Gefitinib, disease=fibroma of lung | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Gefitinib, disease=inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Gefitinib, disease=inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=hamartoma of lung | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Gefitinib, disease=hamartoma of lung | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Gefitinib, disease=hamartoma of lung | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=lung hilum carcinoma | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Gefitinib, disease=lung hilum carcinoma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Gefitinib, disease=lung hilum carcinoma | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=lung benign neoplasm | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Gefitinib, disease=lung benign neoplasm | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Gefitinib, disease=lung benign neoplasm | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Gefitinib, disease=Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Gefitinib, disease=Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=pulmonary sulcus neoplasm | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Gefitinib, disease=pulmonary sulcus neoplasm | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Gefitinib, disease=pulmonary sulcus neoplasm | success | 2 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=lung germ cell tumor | success | 1 |  |
| 28 | ictrp | 2026-03-09 | drug=Gefitinib, disease=lung germ cell tumor | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Gefitinib, disease=lung germ cell tumor | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Gefitinib, disease=junctional epidermolysis bullosa | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Gefitinib, disease=junctional epidermolysis bullosa | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Gefitinib, disease=junctional epidermolysis bullosa | success | 0 |  |