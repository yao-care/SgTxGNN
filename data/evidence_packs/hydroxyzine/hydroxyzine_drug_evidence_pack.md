# Hydroxyzine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Hydroxyzine | |
| DrugBank ID | DB00557 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | allergic urticaria | 99.77% | L2 | 1 | 20 | S3 | Proceed with Guardrails |
| 2 | rosacea conjunctivitis | 99.70% | L5 | 0 | 0 | S0 | Hold |
| 3 | cold urticaria | 99.66% | L3 | 1 | 20 | S2 | Proceed with Guardrails |
| 4 | recalcitrant atopic dermatitis | 99.36% | L5 | 0 | 0 | S0 | Hold |
| 5 | IgE responsiveness, atopic | 99.27% | L5 | 0 | 0 | S0 | Hold |
| 6 | nasal cavity disease | 98.75% | L4 | 1 | 3 | S1 | Research Question |
| 7 | acute laryngopharyngitis | 98.67% | L5 | 0 | 0 | S0 | Hold |
| 8 | parasitic conjunctivitis | 98.62% | L5 | 0 | 0 | S0 | Hold |
| 9 | chronic follicular conjunctivitis | 98.62% | L5 | 0 | 0 | S0 | Hold |
| 10 | serous conjunctivitis except viral | 98.62% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Hydroxyzine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Hydroxyzine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=allergic urticaria | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=allergic urticaria | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=allergic urticaria | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=rosacea conjunctivitis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=rosacea conjunctivitis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=rosacea conjunctivitis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=cold urticaria | success | 1 |  |
| 10 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=cold urticaria | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=cold urticaria | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=recalcitrant atopic dermatitis | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=recalcitrant atopic dermatitis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=recalcitrant atopic dermatitis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=IgE responsiveness, atopic | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=IgE responsiveness, atopic | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=IgE responsiveness, atopic | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=nasal cavity disease | success | 1 |  |
| 19 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=nasal cavity disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=nasal cavity disease | success | 3 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=acute laryngopharyngitis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=acute laryngopharyngitis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=acute laryngopharyngitis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=parasitic conjunctivitis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=parasitic conjunctivitis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=parasitic conjunctivitis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=chronic follicular conjunctivitis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=chronic follicular conjunctivitis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=chronic follicular conjunctivitis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Hydroxyzine, disease=serous conjunctivitis except viral | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Hydroxyzine, disease=serous conjunctivitis except viral | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Hydroxyzine, disease=serous conjunctivitis except viral | success | 0 |  |