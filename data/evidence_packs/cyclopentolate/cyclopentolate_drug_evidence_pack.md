# Cyclopentolate 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cyclopentolate | |
| DrugBank ID | DB00979 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | cauda equina syndrome | 99.54% | L5 | 0 | 0 | S0 | Hold |
| 2 | obsolete neurogenic bladder (disease) | 99.40% | L5 | 0 | 0 | S0 | Research Question |
| 3 | irritable bowel syndrome | 99.27% | L5 | 0 | 0 | S0 | Research Question |
| 4 | acute laryngopharyngitis | 97.69% | L5 | 0 | 0 | S0 | Hold |
| 5 | pharyngitis | 97.59% | L5 | 0 | 0 | S0 | Hold |
| 6 | nasal cavity disease | 97.56% | L5 | 0 | 0 | S0 | Research Question |
| 7 | uveitis | 95.73% | L3 | 0 | 20 | S2 | Proceed with Guardrails |
| 8 | iris disease | 94.36% | L3 | 3 | 20 | S2 | Proceed with Guardrails |
| 9 | panuveitis (disease) | 93.38% | L4 | 0 | 13 | S1 | Research Question |
| 10 | ciliary body disease | 93.30% | L3 | 1 | 5 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Cyclopentolate | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Cyclopentolate | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=cauda equina syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=cauda equina syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=cauda equina syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=irritable bowel syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=irritable bowel syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=irritable bowel syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=acute laryngopharyngitis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=acute laryngopharyngitis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=acute laryngopharyngitis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=pharyngitis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=pharyngitis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=pharyngitis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=nasal cavity disease | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=nasal cavity disease | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=nasal cavity disease | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=uveitis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=uveitis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=uveitis | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=iris disease | success | 3 |  |
| 25 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=iris disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=iris disease | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=panuveitis (disease) | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=panuveitis (disease) | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=panuveitis (disease) | success | 13 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Cyclopentolate, disease=ciliary body disease | success | 1 |  |
| 31 | ictrp | 2026-03-10 | drug=Cyclopentolate, disease=ciliary body disease | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Cyclopentolate, disease=ciliary body disease | success | 5 |  |