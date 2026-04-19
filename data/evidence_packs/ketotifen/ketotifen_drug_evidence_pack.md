# Ketotifen 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ketotifen | |
| DrugBank ID | DB00920 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | allergic urticaria | 98.60% | L2 | 0 | 20 | S3 | Proceed with Guardrails |
| 2 | rosacea conjunctivitis | 97.10% | L5 | 0 | 0 | S0 | Hold |
| 3 | cold urticaria | 92.70% | L3 | 0 | 14 | S2 | Research Question |
| 4 | nasopharyngitis | 92.67% | L5 | 0 | 0 | S0 | Hold |
| 5 | recalcitrant atopic dermatitis | 84.33% | L5 | 0 | 0 | S0 | Hold |
| 6 | Angelucci syndrome | 83.52% | L5 | 0 | 0 | S0 | Hold |
| 7 | acute hemorrhagic conjunctivitis | 83.27% | L5 | 0 | 0 | S0 | Hold |
| 8 | pseudomembranous conjunctivitis | 82.78% | L5 | 0 | 0 | S0 | Hold |
| 9 | parasitic conjunctivitis | 82.56% | L5 | 0 | 0 | S0 | Hold |
| 10 | chronic follicular conjunctivitis | 82.56% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Ketotifen | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Ketotifen | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=allergic urticaria | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Ketotifen, disease=allergic urticaria | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Ketotifen, disease=allergic urticaria | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=rosacea conjunctivitis | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Ketotifen, disease=rosacea conjunctivitis | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Ketotifen, disease=rosacea conjunctivitis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=cold urticaria | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Ketotifen, disease=cold urticaria | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Ketotifen, disease=cold urticaria | success | 14 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=nasopharyngitis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Ketotifen, disease=nasopharyngitis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Ketotifen, disease=nasopharyngitis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=recalcitrant atopic dermatitis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Ketotifen, disease=recalcitrant atopic dermatitis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Ketotifen, disease=recalcitrant atopic dermatitis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=Angelucci syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Ketotifen, disease=Angelucci syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Ketotifen, disease=Angelucci syndrome | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=acute hemorrhagic conjunctivitis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Ketotifen, disease=acute hemorrhagic conjunctivitis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Ketotifen, disease=acute hemorrhagic conjunctivitis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=pseudomembranous conjunctivitis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Ketotifen, disease=pseudomembranous conjunctivitis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Ketotifen, disease=pseudomembranous conjunctivitis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=parasitic conjunctivitis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Ketotifen, disease=parasitic conjunctivitis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Ketotifen, disease=parasitic conjunctivitis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Ketotifen, disease=chronic follicular conjunctivitis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Ketotifen, disease=chronic follicular conjunctivitis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Ketotifen, disease=chronic follicular conjunctivitis | success | 0 |  |