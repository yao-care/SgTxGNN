# Amikacin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Amikacin | |
| DrugBank ID | DB00479 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | paratyphoid fever | 99.82% | L4 | 0 | 12 | S1 | Research Question |
| 2 | diffuse scleroderma | 99.82% | L5 | 0 | 0 | S0 | Hold |
| 3 | punctate epithelial keratoconjunctivitis | 99.80% | L5 | 0 | 0 | S0 | Hold |
| 4 | typhoid fever | 99.77% | L3 | 0 | 20 | S1 | Research Question |
| 5 | epiglottitis | 99.74% | L5 | 0 | 0 | S0 | Hold |
| 6 | salmonellosis | 99.74% | L3 | 0 | 20 | S1 | Research Question |
| 7 | congenital analbuminemia | 99.64% | L5 | 0 | 0 | S0 | Hold |
| 8 | polyclonal hyperviscosity syndrome | 99.62% | L5 | 0 | 0 | S0 | Hold |
| 9 | hyperamylasemia | 99.62% | L5 | 0 | 0 | S0 | Hold |
| 10 | meningococcemia | 99.58% | L4 | 0 | 3 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Amikacin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Amikacin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=paratyphoid fever | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Amikacin, disease=paratyphoid fever | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Amikacin, disease=paratyphoid fever | success | 12 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=diffuse scleroderma | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Amikacin, disease=diffuse scleroderma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Amikacin, disease=diffuse scleroderma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Amikacin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Amikacin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=typhoid fever | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Amikacin, disease=typhoid fever | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Amikacin, disease=typhoid fever | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=epiglottitis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Amikacin, disease=epiglottitis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Amikacin, disease=epiglottitis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=salmonellosis | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Amikacin, disease=salmonellosis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Amikacin, disease=salmonellosis | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=congenital analbuminemia | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Amikacin, disease=congenital analbuminemia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Amikacin, disease=congenital analbuminemia | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Amikacin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Amikacin, disease=polyclonal hyperviscosity syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=hyperamylasemia | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Amikacin, disease=hyperamylasemia | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Amikacin, disease=hyperamylasemia | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Amikacin, disease=meningococcemia | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Amikacin, disease=meningococcemia | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Amikacin, disease=meningococcemia | success | 3 |  |