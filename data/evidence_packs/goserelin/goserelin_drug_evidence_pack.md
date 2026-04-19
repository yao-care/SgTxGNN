# Goserelin 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Goserelin | |
| DrugBank ID | DB00014 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | amenorrhea (disease) | 99.99% | L1 | 7 | 19 | S3 | Proceed with Guardrails |
| 2 | renal hypoplasia (disease) | 99.06% | L5 | 0 | 0 | S0 | Hold |
| 3 | renal hypoplasia, bilateral | 99.06% | L5 | 0 | 0 | S0 | Hold |
| 4 | cervix endometriosis | 98.75% | L4 | 0 | 2 | S1 | Research Question |
| 5 | gelatinous drop-like corneal dystrophy | 98.66% | L5 | 0 | 0 | S0 | Hold |
| 6 | duodenogastric reflux | 98.54% | L5 | 0 | 0 | S0 | Hold |
| 7 | endometriosis of rectovaginal septum and vagina | 98.46% | L4 | 0 | 1 | S1 | Research Question |
| 8 | endometriosis in cutaneous scar | 98.46% | L4 | 0 | 1 | S1 | Research Question |
| 9 | duodenal obstruction | 98.45% | L5 | 0 | 0 | S0 | Hold |
| 10 | duodenal ulcer (disease) | 98.24% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Goserelin | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Goserelin | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=amenorrhea (disease) | success | 7 |  |
| 4 | ictrp | 2026-03-09 | drug=Goserelin, disease=amenorrhea (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Goserelin, disease=amenorrhea (disease) | success | 19 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=renal hypoplasia (disease) | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Goserelin, disease=renal hypoplasia (disease) | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Goserelin, disease=renal hypoplasia (disease) | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=renal hypoplasia, bilateral | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Goserelin, disease=renal hypoplasia, bilateral | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Goserelin, disease=renal hypoplasia, bilateral | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=cervix endometriosis | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Goserelin, disease=cervix endometriosis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Goserelin, disease=cervix endometriosis | success | 2 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=gelatinous drop-like corneal dystrophy | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Goserelin, disease=gelatinous drop-like corneal dystrophy | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Goserelin, disease=gelatinous drop-like corneal dystrophy | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=duodenogastric reflux | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Goserelin, disease=duodenogastric reflux | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Goserelin, disease=duodenogastric reflux | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=endometriosis of rectovaginal septum and vagina | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Goserelin, disease=endometriosis of rectovaginal septum and vagina | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Goserelin, disease=endometriosis of rectovaginal septum and vagina | success | 1 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=endometriosis in cutaneous scar | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Goserelin, disease=endometriosis in cutaneous scar | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Goserelin, disease=endometriosis in cutaneous scar | success | 1 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=duodenal obstruction | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Goserelin, disease=duodenal obstruction | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Goserelin, disease=duodenal obstruction | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Goserelin, disease=duodenal ulcer (disease) | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Goserelin, disease=duodenal ulcer (disease) | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Goserelin, disease=duodenal ulcer (disease) | success | 0 |  |