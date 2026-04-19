# Isosorbide dinitrate 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Isosorbide dinitrate | |
| DrugBank ID | DB00883 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | alopecia | 99.99% | L5 | 0 | 0 | S0 | Hold |
| 2 | congenital hypotrichosis milia | 99.99% | L5 | 0 | 0 | S0 | Hold |
| 3 | hypotrichosis simplex of the scalp | 99.99% | L5 | 0 | 0 | S0 | Hold |
| 4 | pulmonary hypertension | 99.98% | L3 | 0 | 20 | S2 | Research Question |
| 5 | diffuse alopecia areata | 99.98% | L5 | 0 | 0 | S0 | Hold |
| 6 | vascular disease | 99.97% | L1 | 49 | 20 | S3 | Proceed with Guardrails |
| 7 | hypertrichosis (disease) | 99.97% | L5 | 0 | 0 | S0 | Hold |
| 8 | kyphoscoliotic heart disease | 99.96% | L5 | 0 | 0 | S0 | Hold |
| 9 | visceral calciphylaxis | 99.96% | L5 | 0 | 0 | S0 | Hold |
| 10 | venous thoracic outlet syndrome | 99.95% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Isosorbide dinitrate | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Isosorbide dinitrate | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=alopecia | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=alopecia | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=alopecia | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=congenital hypotrichosis milia | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=congenital hypotrichosis milia | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=congenital hypotrichosis milia | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=hypotrichosis simplex of the scalp | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=pulmonary hypertension | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=pulmonary hypertension | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=pulmonary hypertension | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=diffuse alopecia areata | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=diffuse alopecia areata | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=diffuse alopecia areata | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=vascular disease | success | 49 |  |
| 19 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=vascular disease | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=vascular disease | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=hypertrichosis (disease) | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=hypertrichosis (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=hypertrichosis (disease) | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=kyphoscoliotic heart disease | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=kyphoscoliotic heart disease | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=kyphoscoliotic heart disease | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=visceral calciphylaxis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=visceral calciphylaxis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=visceral calciphylaxis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Isosorbide dinitrate, disease=venous thoracic outlet syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Isosorbide dinitrate, disease=venous thoracic outlet syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Isosorbide dinitrate, disease=venous thoracic outlet syndrome | success | 0 |  |