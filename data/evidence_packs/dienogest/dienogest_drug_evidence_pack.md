# Dienogest 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dienogest | |
| DrugBank ID | DB09123 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | amenorrhea (disease) | 99.71% | L3 | 4 | 6 | S1 | Hold |
| 2 | primary ovarian failure | 99.69% | L4 | 1 | 0 | S0 | Hold |
| 3 | breast fibrocystic disease | 99.60% | L4 | 0 | 1 | S1 | Research Question |
| 4 | isolated growth hormone deficiency | 99.53% | L5 | 0 | 0 | S0 | Hold |
| 5 | symptomatic form of fragile X syndrome in female carrier | 99.46% | L5 | 0 | 0 | S0 | Hold |
| 6 | blepharophimosis-epicanthus inversus-ptosis | 99.46% | pending | 0 | 0 | pending | pending |
| 7 | hypogonadotropic hypogonadism with or without anosmia | 99.46% | L5 | 0 | 20 | S0 | Hold |
| 8 | partial trisomy/tetrasomy of the short arm of chromosome 5 | 99.43% | L5 | 0 | 0 | S0 | Hold |
| 9 | blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome | 99.43% | L5 | 0 | 0 | S0 | Hold |
| 10 | partial trisomy/tetrasomy of the short arm of chromosome 18 | 99.42% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Dienogest | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Dienogest | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=amenorrhea (disease) | success | 4 |  |
| 4 | ictrp | 2026-03-10 | drug=Dienogest, disease=amenorrhea (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Dienogest, disease=amenorrhea (disease) | success | 6 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=primary ovarian failure | success | 1 |  |
| 7 | ictrp | 2026-03-10 | drug=Dienogest, disease=primary ovarian failure | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Dienogest, disease=primary ovarian failure | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=breast fibrocystic disease | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Dienogest, disease=breast fibrocystic disease | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Dienogest, disease=breast fibrocystic disease | success | 1 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=isolated growth hormone deficiency | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Dienogest, disease=isolated growth hormone deficiency | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Dienogest, disease=isolated growth hormone deficiency | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=symptomatic form of fragile X syndrome in female carrier | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Dienogest, disease=symptomatic form of fragile X syndrome in female carrier | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Dienogest, disease=symptomatic form of fragile X syndrome in female carrier | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=blepharophimosis-epicanthus inversus-ptosis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Dienogest, disease=blepharophimosis-epicanthus inversus-ptosis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Dienogest, disease=blepharophimosis-epicanthus inversus-ptosis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=hypogonadotropic hypogonadism with or without anosmia | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Dienogest, disease=hypogonadotropic hypogonadism with or without anosmia | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Dienogest, disease=hypogonadotropic hypogonadism with or without anosmia | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=partial trisomy/tetrasomy of the short arm of chromosome 5 | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Dienogest, disease=partial trisomy/tetrasomy of the short arm of chromosome 5 | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Dienogest, disease=partial trisomy/tetrasomy of the short arm of chromosome 5 | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Dienogest, disease=blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Dienogest, disease=blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Dienogest, disease=partial trisomy/tetrasomy of the short arm of chromosome 18 | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Dienogest, disease=partial trisomy/tetrasomy of the short arm of chromosome 18 | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Dienogest, disease=partial trisomy/tetrasomy of the short arm of chromosome 18 | success | 0 |  |