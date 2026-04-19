# Clarithromycin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clarithromycin | |
| DrugBank ID | DB01211 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | polyclonal hyperviscosity syndrome | 99.35% | L5 | 0 | 0 | S0 | Hold |
| 2 | hyperamylasemia | 99.35% | L5 | 0 | 1 | S0 | Hold |
| 3 | congenital analbuminemia | 99.21% | L5 | 0 | 0 | S0 | Hold |
| 4 | punctate epithelial keratoconjunctivitis | 99.11% | L4 | 0 | 1 | S1 | Research Question |
| 5 | blood group incompatibility | 99.07% | L5 | 0 | 0 | S0 | Hold |
| 6 | premalignant hematological system disease | 98.92% | L5 | 0 | 0 | S0 | Hold |
| 7 | monoclonal gammopathy | 98.81% | L2 | 1 | 20 | S3 | Proceed with Guardrails |
| 8 | septicemic plague | 98.70% | L5 | 0 | 3 | S0 | Hold |
| 9 | hematological disease associated with an acquired peripheral neuropathy | 98.69% | L5 | 0 | 0 | S0 | Hold |
| 10 | congenital hematological disorder | 98.32% | L5 | 0 | 1 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Clarithromycin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Clarithromycin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=hyperamylasemia | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=hyperamylasemia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=hyperamylasemia | success | 1 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=congenital analbuminemia | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=congenital analbuminemia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=congenital analbuminemia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=punctate epithelial keratoconjunctivitis | success | 1 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=blood group incompatibility | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=blood group incompatibility | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=blood group incompatibility | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=premalignant hematological system disease | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=premalignant hematological system disease | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=premalignant hematological system disease | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=monoclonal gammopathy | success | 1 |  |
| 22 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=monoclonal gammopathy | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=monoclonal gammopathy | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=septicemic plague | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=septicemic plague | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=septicemic plague | success | 3 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=hematological disease associated with an acquired peripheral neuropathy | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=hematological disease associated with an acquired peripheral neuropathy | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=hematological disease associated with an acquired peripheral neuropathy | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Clarithromycin, disease=congenital hematological disorder | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Clarithromycin, disease=congenital hematological disorder | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Clarithromycin, disease=congenital hematological disorder | success | 1 |  |