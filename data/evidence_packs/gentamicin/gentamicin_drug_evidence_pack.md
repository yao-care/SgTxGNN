# Gentamicin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Gentamicin | |
| DrugBank ID | DB00798 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | rheumatoid arthritis | 97.76% | L3 | 1 | 20 | S1 | Research Question |
| 2 | sclerosing cholangitis | 97.50% | L4 | 0 | 2 | S1 | Research Question |
| 3 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.32% | L5 | 0 | 0 | S0 | Hold |
| 4 | brachydactyly-syndactyly syndrome | 95.28% | L5 | 0 | 0 | S0 | Hold |
| 5 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 91.99% | L5 | 0 | 0 | S0 | Hold |
| 6 | brain small vessel disease 1 with or without ocular anomalies | 91.70% | L5 | 0 | 18 | S0 | Hold |
| 7 | osteoarthritis susceptibility | 90.62% | L4 | 0 | 1 | S0 | Hold |
| 8 | diabetic nephropathy | 89.92% | L5 | 0 | 19 | S0 | Hold |
| 9 | congenital hypotrichosis milia | 88.90% | L5 | 0 | 0 | S0 | Hold |
| 10 | unclassified myelodysplastic syndrome | 88.74% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Gentamicin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Gentamicin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=rheumatoid arthritis | success | 1 |  |
| 4 | ictrp | 2026-03-10 | drug=Gentamicin, disease=rheumatoid arthritis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Gentamicin, disease=rheumatoid arthritis | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=sclerosing cholangitis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Gentamicin, disease=sclerosing cholangitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Gentamicin, disease=sclerosing cholangitis | success | 2 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Gentamicin, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Gentamicin, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Gentamicin, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Gentamicin, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Gentamicin, disease=autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Gentamicin, disease=autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=brain small vessel disease 1 with or without ocular anomalies | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Gentamicin, disease=brain small vessel disease 1 with or without ocular anomalies | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Gentamicin, disease=brain small vessel disease 1 with or without ocular anomalies | success | 18 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=osteoarthritis susceptibility | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Gentamicin, disease=osteoarthritis susceptibility | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Gentamicin, disease=osteoarthritis susceptibility | success | 1 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=diabetic nephropathy | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Gentamicin, disease=diabetic nephropathy | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Gentamicin, disease=diabetic nephropathy | success | 19 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=congenital hypotrichosis milia | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Gentamicin, disease=congenital hypotrichosis milia | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Gentamicin, disease=congenital hypotrichosis milia | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Gentamicin, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Gentamicin, disease=unclassified myelodysplastic syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Gentamicin, disease=unclassified myelodysplastic syndrome | success | 0 |  |