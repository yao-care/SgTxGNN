# Articaine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Articaine | |
| DrugBank ID | DB09009 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | gout | 99.58% | L5 | 0 | 0 | S0 | Hold |
| 2 | exostosis | 99.42% | L5 | 0 | 0 | S0 | Hold |
| 3 | allergic asthma | 99.38% | L5 | 0 | 3 | S0 | Hold |
| 4 | intrinsic asthma | 99.34% | L5 | 0 | 0 | S0 | Hold |
| 5 | exostoses, multiple, | 98.90% | pending | 0 | 0 | pending | pending |
| 6 | hypotrichosis simplex of the scalp | 98.62% | L5 | 0 | 0 | S0 | Hold |
| 7 | alopecia | 98.58% | L5 | 0 | 0 | S0 | Hold |
| 8 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 98.49% | L5 | 0 | 0 | S0 | Hold |
| 9 | brain small vessel disease 1 with or without ocular anomalies | 98.48% | L5 | 0 | 18 | S0 | Hold |
| 10 | congenital hypotrichosis milia | 98.44% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Articaine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Articaine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=gout | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Articaine, disease=gout | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Articaine, disease=gout | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=exostosis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Articaine, disease=exostosis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Articaine, disease=exostosis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=allergic asthma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Articaine, disease=allergic asthma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Articaine, disease=allergic asthma | success | 3 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=intrinsic asthma | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Articaine, disease=intrinsic asthma | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Articaine, disease=intrinsic asthma | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=exostoses, multiple, | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Articaine, disease=exostoses, multiple, | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Articaine, disease=exostoses, multiple, | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Articaine, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Articaine, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=alopecia | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Articaine, disease=alopecia | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Articaine, disease=alopecia | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Articaine, disease=autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Articaine, disease=autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=brain small vessel disease 1 with or without ocular anomalies | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Articaine, disease=brain small vessel disease 1 with or without ocular anomalies | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Articaine, disease=brain small vessel disease 1 with or without ocular anomalies | success | 18 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Articaine, disease=congenital hypotrichosis milia | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Articaine, disease=congenital hypotrichosis milia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Articaine, disease=congenital hypotrichosis milia | success | 0 |  |