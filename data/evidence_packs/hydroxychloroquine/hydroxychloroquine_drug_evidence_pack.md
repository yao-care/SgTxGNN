# Hydroxychloroquine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Hydroxychloroquine | |
| DrugBank ID | DB01611 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | Quinquaud's folliculitis decalvans | 98.66% | L3 | 0 | 4 | S2 | Research Question |
| 2 | telogen effluvium | 98.55% | L5 | 0 | 1 | S0 | Hold |
| 3 | alopecia antibody deficiency | 98.53% | L5 | 0 | 1 | S0 | Hold |
| 4 | alopecia mucinosa | 98.47% | L3 | 0 | 5 | S2 | Research Question |
| 5 | hereditary hypotrichosis with recurrent skin vesicles | 98.40% | L5 | 0 | 0 | S0 | Hold |
| 6 | alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | 98.37% | L5 | 0 | 0 | S0 | Hold |
| 7 | alopecia areata | 98.21% | L3 | 7 | 19 | S2 | Research Question |
| 8 | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | 98.04% | L4 | 0 | 1 | S1 | Research Question |
| 9 | juvenile chronic polyarthritis | 97.75% | L3 | 0 | 19 | S2 | Proceed with Guardrails |
| 10 | rheumatoid nodulosis | 97.75% | L4 | 1 | 20 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Hydroxychloroquine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Hydroxychloroquine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=Quinquaud's folliculitis decalvans | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=Quinquaud's folliculitis decalvans | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=Quinquaud's folliculitis decalvans | success | 4 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=telogen effluvium | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=telogen effluvium | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=telogen effluvium | success | 1 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia antibody deficiency | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia antibody deficiency | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia antibody deficiency | success | 1 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia mucinosa | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia mucinosa | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia mucinosa | success | 5 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=hereditary hypotrichosis with recurrent skin vesicles | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=hereditary hypotrichosis with recurrent skin vesicles | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=hereditary hypotrichosis with recurrent skin vesicles | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia areata | success | 7 |  |
| 22 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia areata | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=alopecia areata | success | 19 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | success | 1 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=juvenile chronic polyarthritis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=juvenile chronic polyarthritis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=juvenile chronic polyarthritis | success | 19 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Hydroxychloroquine, disease=rheumatoid nodulosis | success | 1 |  |
| 31 | ictrp | 2026-03-10 | drug=Hydroxychloroquine, disease=rheumatoid nodulosis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Hydroxychloroquine, disease=rheumatoid nodulosis | success | 20 |  |