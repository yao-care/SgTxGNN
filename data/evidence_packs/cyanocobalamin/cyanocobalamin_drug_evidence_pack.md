# Cyanocobalamin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cyanocobalamin | |
| DrugBank ID | DB00115 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | biotin metabolic disease | 99.60% | L3 | 15 | 20 | S1 | Research Question |
| 2 | inborn error of biotin metabolism | 97.85% | L3 | 3 | 14 | S1 | Research Question |
| 3 | non-syndromic esophageal malformation | 97.67% | L5 | 1 | 0 | S0 | Hold |
| 4 | inflammatory myopathy with abundant macrophages | 97.64% | L5 | 0 | 0 | S0 | Hold |
| 5 | idiopathic eosinophilic myositis | 97.64% | L5 | 0 | 0 | S0 | Hold |
| 6 | immune-mediated necrotizing myopathy | 97.60% | L5 | 0 | 0 | S0 | Hold |
| 7 | antisynthetase syndrome | 97.49% | L5 | 0 | 0 | S0 | Hold |
| 8 | proteinuria | 97.31% | L3 | 9 | 20 | S2 | Proceed with Guardrails |
| 9 | focal myositis | 97.31% | L4 | 0 | 9 | S0 | Hold |
| 10 | primary CD59 deficiency | 97.09% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Cyanocobalamin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Cyanocobalamin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=biotin metabolic disease | success | 15 |  |
| 4 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=biotin metabolic disease | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=biotin metabolic disease | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=inborn error of biotin metabolism | success | 3 |  |
| 7 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=inborn error of biotin metabolism | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=inborn error of biotin metabolism | success | 14 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=non-syndromic esophageal malformation | success | 1 |  |
| 10 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=non-syndromic esophageal malformation | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=non-syndromic esophageal malformation | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=inflammatory myopathy with abundant macrophages | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=inflammatory myopathy with abundant macrophages | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=inflammatory myopathy with abundant macrophages | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=idiopathic eosinophilic myositis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=idiopathic eosinophilic myositis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=idiopathic eosinophilic myositis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=immune-mediated necrotizing myopathy | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=immune-mediated necrotizing myopathy | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=immune-mediated necrotizing myopathy | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=antisynthetase syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=antisynthetase syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=antisynthetase syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=proteinuria | success | 9 |  |
| 25 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=proteinuria | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=proteinuria | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=focal myositis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=focal myositis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=focal myositis | success | 9 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Cyanocobalamin, disease=primary CD59 deficiency | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Cyanocobalamin, disease=primary CD59 deficiency | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Cyanocobalamin, disease=primary CD59 deficiency | success | 0 |  |