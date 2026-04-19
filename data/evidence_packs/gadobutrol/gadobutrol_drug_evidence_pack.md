# Gadobutrol 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Gadobutrol | |
| DrugBank ID | DB06703 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | benign prostatic hyperplasia (disease) | 83.24% | L5 | 0 | 0 | S0 | Hold |
| 2 | peripheral arterial disease | 76.72% | L1 | 4 | 20 | S3 | Proceed with Guardrails |
| 3 | cauda equina syndrome | 75.23% | L5 | 0 | 0 | S0 | Hold |
| 4 | peripheral vascular disease | 74.39% | L1 | 5 | 20 | S3 | Proceed with Guardrails |
| 5 | strongyloidiasis | 73.13% | L5 | 0 | 0 | S0 | Hold |
| 6 | prostate calculus | 72.47% | L5 | 0 | 0 | S0 | Hold |
| 7 | obsolete neurogenic bladder (disease) | 71.93% | L5 | 0 | 0 | S0 | Hold |
| 8 | iritis (disease) | 71.23% | L5 | 0 | 0 | S0 | Hold |
| 9 | hypertrichosis (disease) | 70.84% | L5 | 0 | 0 | S0 | Hold |
| 10 | disease of orbital region | 70.62% | L3 | 2 | 0 | S2 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Gadobutrol | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Gadobutrol | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=benign prostatic hyperplasia (disease) | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=benign prostatic hyperplasia (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=benign prostatic hyperplasia (disease) | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=peripheral arterial disease | success | 4 |  |
| 7 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=peripheral arterial disease | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=peripheral arterial disease | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=cauda equina syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=cauda equina syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=cauda equina syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=peripheral vascular disease | success | 5 |  |
| 13 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=peripheral vascular disease | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=peripheral vascular disease | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=strongyloidiasis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=strongyloidiasis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=strongyloidiasis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=prostate calculus | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=prostate calculus | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=prostate calculus | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=iritis (disease) | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=iritis (disease) | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=iritis (disease) | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=hypertrichosis (disease) | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=hypertrichosis (disease) | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=hypertrichosis (disease) | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Gadobutrol, disease=disease of orbital region | success | 2 |  |
| 31 | ictrp | 2026-03-10 | drug=Gadobutrol, disease=disease of orbital region | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Gadobutrol, disease=disease of orbital region | success | 0 |  |