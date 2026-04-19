# Clindamycin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clindamycin | |
| DrugBank ID | DB01190 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | punctate epithelial keratoconjunctivitis | 99.97% | L5 | 0 | 0 | S0 | Hold |
| 2 | exposure keratitis | 99.80% | L4 | 0 | 4 | S1 | Hold |
| 3 | non-human animal disease | 99.69% | L5 | 0 | 2 | S0 | Hold |
| 4 | neurotrophic keratopathy | 99.49% | L5 | 0 | 0 | S0 | Hold |
| 5 | epidemic keratoconjunctivitis | 99.49% | L5 | 0 | 2 | S0 | Hold |
| 6 | postmenopausal atrophic vaginitis | 99.03% | L5 | 0 | 0 | S0 | Hold |
| 7 | superior limbic keratoconjunctivitis | 98.97% | L5 | 0 | 0 | S0 | Hold |
| 8 | visual snow syndrome | 98.28% | L5 | 0 | 0 | S0 | Hold |
| 9 | keratomalacia | 98.28% | L5 | 0 | 0 | S0 | Hold |
| 10 | ophthalmia nodosa | 98.28% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Clindamycin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Clindamycin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Clindamycin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Clindamycin, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=exposure keratitis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Clindamycin, disease=exposure keratitis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Clindamycin, disease=exposure keratitis | success | 4 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=non-human animal disease | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Clindamycin, disease=non-human animal disease | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Clindamycin, disease=non-human animal disease | success | 2 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=neurotrophic keratopathy | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Clindamycin, disease=neurotrophic keratopathy | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Clindamycin, disease=neurotrophic keratopathy | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=epidemic keratoconjunctivitis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Clindamycin, disease=epidemic keratoconjunctivitis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Clindamycin, disease=epidemic keratoconjunctivitis | success | 2 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=postmenopausal atrophic vaginitis | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Clindamycin, disease=postmenopausal atrophic vaginitis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Clindamycin, disease=postmenopausal atrophic vaginitis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=superior limbic keratoconjunctivitis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Clindamycin, disease=superior limbic keratoconjunctivitis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Clindamycin, disease=superior limbic keratoconjunctivitis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=visual snow syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Clindamycin, disease=visual snow syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Clindamycin, disease=visual snow syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=keratomalacia | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Clindamycin, disease=keratomalacia | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Clindamycin, disease=keratomalacia | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Clindamycin, disease=ophthalmia nodosa | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Clindamycin, disease=ophthalmia nodosa | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Clindamycin, disease=ophthalmia nodosa | success | 0 |  |