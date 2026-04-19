# Glycine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Glycine | |
| DrugBank ID | DB00145 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | nasal cavity disease | 99.85% | pending | 1 | 2 | pending | pending |
| 2 | acute laryngopharyngitis | 99.84% | pending | 0 | 1 | pending | pending |
| 3 | faucial diphtheria | 97.40% | pending | 0 | 0 | pending | pending |
| 4 | cervical disc degenerative disorder | 97.28% | pending | 1 | 0 | pending | pending |
| 5 | dyspepsia | 96.42% | pending | 1 | 20 | pending | pending |
| 6 | non-syndromic esophageal malformation | 93.99% | pending | 0 | 0 | pending | pending |
| 7 | papillary conjunctivitis | 90.64% | pending | 0 | 0 | pending | pending |
| 8 | gastroparesis (disease) | 89.40% | pending | 0 | 0 | pending | pending |
| 9 | Ureaplasma urethritis | 89.30% | pending | 0 | 0 | pending | pending |
| 10 | gonococcal urethritis | 89.30% | pending | 0 | 0 | pending | pending |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Glycine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Glycine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=nasal cavity disease | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Glycine, disease=nasal cavity disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Glycine, disease=nasal cavity disease | success | 2 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=acute laryngopharyngitis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Glycine, disease=acute laryngopharyngitis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Glycine, disease=acute laryngopharyngitis | success | 1 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=faucial diphtheria | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Glycine, disease=faucial diphtheria | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Glycine, disease=faucial diphtheria | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=cervical disc degenerative disorder | success | 1 |  |
| 13 | ictrp | 2026-03-09 | drug=Glycine, disease=cervical disc degenerative disorder | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Glycine, disease=cervical disc degenerative disorder | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=dyspepsia | success | 1 |  |
| 16 | ictrp | 2026-03-09 | drug=Glycine, disease=dyspepsia | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Glycine, disease=dyspepsia | success | 20 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=non-syndromic esophageal malformation | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Glycine, disease=non-syndromic esophageal malformation | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Glycine, disease=non-syndromic esophageal malformation | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=papillary conjunctivitis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Glycine, disease=papillary conjunctivitis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Glycine, disease=papillary conjunctivitis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=gastroparesis (disease) | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Glycine, disease=gastroparesis (disease) | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Glycine, disease=gastroparesis (disease) | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=Ureaplasma urethritis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Glycine, disease=Ureaplasma urethritis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Glycine, disease=Ureaplasma urethritis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Glycine, disease=gonococcal urethritis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Glycine, disease=gonococcal urethritis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Glycine, disease=gonococcal urethritis | success | 0 |  |