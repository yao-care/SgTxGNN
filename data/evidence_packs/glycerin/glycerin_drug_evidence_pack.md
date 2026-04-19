# Glycerin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Glycerin | |
| DrugBank ID | DB09462 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | cauda equina syndrome | 99.60% | L5 | 0 | 0 | S0 | Hold |
| 2 | open-angle glaucoma | 99.59% | L4 | 1 | 16 | S1 | Research Question |
| 3 | primary hereditary glaucoma | 99.56% | L5 | 0 | 0 | S0 | Hold |
| 4 | alopecia | 99.55% | L4 | 1 | 13 | S1 | Research Question |
| 5 | congenital hypotrichosis milia | 99.50% | L5 | 0 | 0 | S0 | Hold |
| 6 | irritable bowel syndrome | 99.49% | L5 | 1 | 0 | S0 | Hold |
| 7 | hypotrichosis simplex of the scalp | 99.47% | L5 | 0 | 0 | S0 | Hold |
| 8 | diffuse alopecia areata | 99.45% | L5 | 0 | 0 | S0 | Hold |
| 9 | migraine disorder | 99.27% | L5 | 0 | 0 | S0 | Hold |
| 10 | migraine with brainstem aura | 99.18% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Glycerin | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Glycerin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=cauda equina syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Glycerin, disease=cauda equina syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Glycerin, disease=cauda equina syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=open-angle glaucoma | success | 1 |  |
| 7 | ictrp | 2026-03-10 | drug=Glycerin, disease=open-angle glaucoma | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Glycerin, disease=open-angle glaucoma | success | 16 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=primary hereditary glaucoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Glycerin, disease=primary hereditary glaucoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Glycerin, disease=primary hereditary glaucoma | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=alopecia | success | 1 |  |
| 13 | ictrp | 2026-03-10 | drug=Glycerin, disease=alopecia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Glycerin, disease=alopecia | success | 13 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=congenital hypotrichosis milia | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Glycerin, disease=congenital hypotrichosis milia | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Glycerin, disease=congenital hypotrichosis milia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=irritable bowel syndrome | success | 1 |  |
| 19 | ictrp | 2026-03-10 | drug=Glycerin, disease=irritable bowel syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Glycerin, disease=irritable bowel syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Glycerin, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Glycerin, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=diffuse alopecia areata | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Glycerin, disease=diffuse alopecia areata | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Glycerin, disease=diffuse alopecia areata | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=migraine disorder | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Glycerin, disease=migraine disorder | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Glycerin, disease=migraine disorder | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Glycerin, disease=migraine with brainstem aura | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Glycerin, disease=migraine with brainstem aura | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Glycerin, disease=migraine with brainstem aura | success | 0 |  |