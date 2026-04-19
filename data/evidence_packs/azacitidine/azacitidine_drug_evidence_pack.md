# Azacitidine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Azacitidine | |
| DrugBank ID | DB00928 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | bulbar polio | 98.59% | L5 | 0 | 0 | S0 | Hold |
| 2 | refractory cytopenia of childhood | 98.20% | L3 | 1 | 5 | S2 | Proceed with Guardrails |
| 3 | unclassified myelodysplastic syndrome | 98.10% | L3 | 1 | 8 | S2 | Proceed with Guardrails |
| 4 | partial deletion of the long arm of chromosome 5 | 97.88% | pending | 0 | 0 | pending | pending |
| 5 | aregenerative anemia | 97.88% | L2 | 27 | 20 | S2 | Proceed with Guardrails |
| 6 | severe congenital hypochromic anemia with ringed sideroblasts | 97.56% | L4 | 0 | 0 | S1 | Research Question |
| 7 | 5q35 microduplication syndrome | 97.48% | L5 | 0 | 0 | S0 | Hold |
| 8 | neuralgic amyotrophy | 96.20% | L5 | 0 | 0 | S0 | Hold |
| 9 | amyotrophic neuralgia | 95.87% | L5 | 0 | 0 | S0 | Hold |
| 10 | familial thrombocytosis | 93.09% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Azacitidine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Azacitidine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=bulbar polio | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Azacitidine, disease=bulbar polio | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Azacitidine, disease=bulbar polio | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=refractory cytopenia of childhood | success | 1 |  |
| 7 | ictrp | 2026-03-10 | drug=Azacitidine, disease=refractory cytopenia of childhood | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Azacitidine, disease=refractory cytopenia of childhood | success | 5 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=unclassified myelodysplastic syndrome | success | 1 |  |
| 10 | ictrp | 2026-03-10 | drug=Azacitidine, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Azacitidine, disease=unclassified myelodysplastic syndrome | success | 8 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=partial deletion of the long arm of chromosome 5 | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Azacitidine, disease=partial deletion of the long arm of chromosome 5 | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Azacitidine, disease=partial deletion of the long arm of chromosome 5 | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=aregenerative anemia | success | 27 |  |
| 16 | ictrp | 2026-03-10 | drug=Azacitidine, disease=aregenerative anemia | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Azacitidine, disease=aregenerative anemia | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=severe congenital hypochromic anemia with ringed sideroblasts | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Azacitidine, disease=severe congenital hypochromic anemia with ringed sideroblasts | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Azacitidine, disease=severe congenital hypochromic anemia with ringed sideroblasts | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=5q35 microduplication syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Azacitidine, disease=5q35 microduplication syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Azacitidine, disease=5q35 microduplication syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=neuralgic amyotrophy | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Azacitidine, disease=neuralgic amyotrophy | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Azacitidine, disease=neuralgic amyotrophy | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=amyotrophic neuralgia | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Azacitidine, disease=amyotrophic neuralgia | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Azacitidine, disease=amyotrophic neuralgia | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Azacitidine, disease=familial thrombocytosis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Azacitidine, disease=familial thrombocytosis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Azacitidine, disease=familial thrombocytosis | success | 0 |  |