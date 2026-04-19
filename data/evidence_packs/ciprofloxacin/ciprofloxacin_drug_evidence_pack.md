# Ciprofloxacin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ciprofloxacin | |
| DrugBank ID | DB00537 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | diffuse scleroderma | 99.87% | L4 | 0 | 2 | S1 | Research Question |
| 2 | polyclonal hyperviscosity syndrome | 99.87% | L5 | 0 | 0 | S0 | Hold |
| 3 | hyperamylasemia | 99.87% | L5 | 0 | 0 | S0 | Hold |
| 4 | congenital analbuminemia | 99.85% | L5 | 0 | 0 | S0 | Hold |
| 5 | blood group incompatibility | 99.78% | L5 | 0 | 3 | S0 | Hold |
| 6 | premalignant hematological system disease | 99.73% | L5 | 0 | 0 | S0 | Hold |
| 7 | punctate epithelial keratoconjunctivitis | 99.71% | L5 | 0 | 0 | S0 | Hold |
| 8 | monoclonal gammopathy | 99.71% | L3 | 1 | 20 | S2 | Proceed with Guardrails |
| 9 | hematological disease associated with an acquired peripheral neuropathy | 99.68% | L5 | 0 | 0 | S0 | Hold |
| 10 | septicemic plague | 99.64% | L2 | 1 | 19 | S3 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Ciprofloxacin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Ciprofloxacin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=diffuse scleroderma | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=diffuse scleroderma | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=diffuse scleroderma | success | 2 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=hyperamylasemia | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=hyperamylasemia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=hyperamylasemia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=congenital analbuminemia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=congenital analbuminemia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=congenital analbuminemia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=blood group incompatibility | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=blood group incompatibility | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=blood group incompatibility | success | 3 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=premalignant hematological system disease | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=premalignant hematological system disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=premalignant hematological system disease | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=monoclonal gammopathy | success | 1 |  |
| 25 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=monoclonal gammopathy | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=monoclonal gammopathy | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=hematological disease associated with an acquired peripheral neuropathy | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=hematological disease associated with an acquired peripheral neuropathy | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=hematological disease associated with an acquired peripheral neuropathy | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Ciprofloxacin, disease=septicemic plague | success | 1 |  |
| 31 | ictrp | 2026-03-09 | drug=Ciprofloxacin, disease=septicemic plague | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Ciprofloxacin, disease=septicemic plague | success | 19 |  |