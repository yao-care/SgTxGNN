# Crizotinib 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Crizotinib | |
| DrugBank ID | DB08865 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | fibromatosis, gingival | 99.81% | L5 | 0 | 0 | S0 | Hold |
| 2 | fibroma of lung | 99.75% | L5 | 0 | 0 | S0 | Hold |
| 3 | hamartoma of lung | 99.75% | L4 | 0 | 1 | S0 | Hold |
| 4 | lung hilum carcinoma | 99.73% | L4 | 0 | 2 | S1 | Research Question |
| 5 | lung benign neoplasm | 99.73% | L3 | 0 | 20 | S1 | Research Question |
| 6 | lung germ cell tumor | 99.73% | L3 | 4 | 20 | S1 | Research Question |
| 7 | pulmonary sulcus neoplasm | 99.73% | L5 | 0 | 0 | S0 | Hold |
| 8 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 99.72% | L5 | 0 | 20 | S0 | Hold |
| 9 | junctional epidermolysis bullosa | 99.70% | L5 | 0 | 0 | S0 | Hold |
| 10 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 99.69% | L4 | 0 | 20 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Crizotinib | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Crizotinib | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=fibromatosis, gingival | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Crizotinib, disease=fibromatosis, gingival | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Crizotinib, disease=fibromatosis, gingival | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=fibroma of lung | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Crizotinib, disease=fibroma of lung | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Crizotinib, disease=fibroma of lung | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=hamartoma of lung | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Crizotinib, disease=hamartoma of lung | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Crizotinib, disease=hamartoma of lung | success | 1 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=lung hilum carcinoma | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Crizotinib, disease=lung hilum carcinoma | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Crizotinib, disease=lung hilum carcinoma | success | 2 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=lung benign neoplasm | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Crizotinib, disease=lung benign neoplasm | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Crizotinib, disease=lung benign neoplasm | success | 20 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=lung germ cell tumor | success | 4 |  |
| 19 | ictrp | 2026-03-09 | drug=Crizotinib, disease=lung germ cell tumor | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Crizotinib, disease=lung germ cell tumor | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=pulmonary sulcus neoplasm | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Crizotinib, disease=pulmonary sulcus neoplasm | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Crizotinib, disease=pulmonary sulcus neoplasm | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Crizotinib, disease=inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Crizotinib, disease=inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=junctional epidermolysis bullosa | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Crizotinib, disease=junctional epidermolysis bullosa | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Crizotinib, disease=junctional epidermolysis bullosa | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Crizotinib, disease=Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Crizotinib, disease=Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Crizotinib, disease=Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | success | 20 |  |