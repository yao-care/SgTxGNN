# Hydrocortisone acetate 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Hydrocortisone acetate | |
| DrugBank ID | DB14539 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | alopecia areata | 99.94% | L1 | 1 | 2 | S3 | Proceed with Guardrails |
| 2 | telogen effluvium | 99.94% | L5 | 0 | 0 | S0 | Hold |
| 3 | alopecia mucinosa | 99.94% | L5 | 0 | 0 | S0 | Hold |
| 4 | Quinquaud's folliculitis decalvans | 99.93% | L5 | 0 | 0 | S0 | Hold |
| 5 | hereditary hypotrichosis with recurrent skin vesicles | 99.93% | L5 | 0 | 0 | S0 | Hold |
| 6 | alopecia antibody deficiency | 99.93% | L5 | 0 | 0 | S0 | Hold |
| 7 | alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | 99.92% | L5 | 0 | 0 | S0 | Hold |
| 8 | atrichia with papular lesions | 99.74% | L5 | 0 | 0 | S0 | Hold |
| 9 | seborrheic keratosis | 99.36% | L5 | 0 | 0 | S0 | Hold |
| 10 | idiopathic steroid-sensitive nephrotic syndrome | 99.31% | L4 | 0 | 0 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Hydrocortisone acetate | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Hydrocortisone acetate | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia areata | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia areata | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia areata | success | 2 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=telogen effluvium | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=telogen effluvium | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=telogen effluvium | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia mucinosa | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia mucinosa | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia mucinosa | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=Quinquaud's folliculitis decalvans | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=Quinquaud's folliculitis decalvans | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=Quinquaud's folliculitis decalvans | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=hereditary hypotrichosis with recurrent skin vesicles | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=hereditary hypotrichosis with recurrent skin vesicles | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=hereditary hypotrichosis with recurrent skin vesicles | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia antibody deficiency | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia antibody deficiency | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia antibody deficiency | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=atrichia with papular lesions | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=atrichia with papular lesions | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=atrichia with papular lesions | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=seborrheic keratosis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=seborrheic keratosis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=seborrheic keratosis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Hydrocortisone acetate, disease=idiopathic steroid-sensitive nephrotic syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Hydrocortisone acetate, disease=idiopathic steroid-sensitive nephrotic syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Hydrocortisone acetate, disease=idiopathic steroid-sensitive nephrotic syndrome | success | 0 |  |