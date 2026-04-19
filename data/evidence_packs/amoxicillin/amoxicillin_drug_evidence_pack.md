# Amoxicillin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Amoxicillin | |
| DrugBank ID | DB01060 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | polyclonal hyperviscosity syndrome | 99.63% | L5 | 0 | 0 | S0 | Hold |
| 2 | hyperamylasemia | 99.63% | L5 | 0 | 0 | S0 | Hold |
| 3 | congenital analbuminemia | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 4 | blood group incompatibility | 99.40% | L5 | 0 | 1 | S0 | Hold |
| 5 | premalignant hematological system disease | 99.29% | L5 | 0 | 0 | S0 | Hold |
| 6 | monoclonal gammopathy | 99.22% | L4 | 1 | 11 | S1 | Research Question |
| 7 | hematological disease associated with an acquired peripheral neuropathy | 99.14% | L5 | 0 | 0 | S0 | Hold |
| 8 | septicemic plague | 99.13% | L4 | 0 | 9 | S1 | Research Question |
| 9 | congenital hematological disorder | 98.70% | L4 | 1 | 4 | S0 | Hold |
| 10 | epiglottitis | 98.70% | L3 | 0 | 15 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Amoxicillin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Amoxicillin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=hyperamylasemia | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=hyperamylasemia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=hyperamylasemia | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=congenital analbuminemia | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=congenital analbuminemia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=congenital analbuminemia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=blood group incompatibility | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=blood group incompatibility | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=blood group incompatibility | success | 1 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=premalignant hematological system disease | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=premalignant hematological system disease | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=premalignant hematological system disease | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=monoclonal gammopathy | success | 1 |  |
| 19 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=monoclonal gammopathy | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=monoclonal gammopathy | success | 11 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=hematological disease associated with an acquired peripheral neuropathy | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=hematological disease associated with an acquired peripheral neuropathy | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=hematological disease associated with an acquired peripheral neuropathy | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=septicemic plague | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=septicemic plague | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=septicemic plague | success | 9 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=congenital hematological disorder | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=congenital hematological disorder | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=congenital hematological disorder | success | 4 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Amoxicillin, disease=epiglottitis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Amoxicillin, disease=epiglottitis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Amoxicillin, disease=epiglottitis | success | 15 |  |