# Glucagon 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Glucagon | |
| DrugBank ID | DB00040 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | irritable bowel syndrome | 99.24% | L3 | 11 | 20 | S1 | Research Question |
| 2 | cauda equina syndrome | 98.78% | L5 | 0 | 0 | S0 | Hold |
| 3 | obsolete neurogenic bladder (disease) | 97.28% | L5 | 0 | 0 | S0 | Hold |
| 4 | acute laryngopharyngitis | 94.48% | L5 | 0 | 0 | S0 | Hold |
| 5 | nasal cavity disease | 94.31% | L5 | 0 | 0 | S0 | Hold |
| 6 | pharyngitis | 93.78% | L5 | 0 | 7 | S0 | Hold |
| 7 | primary hereditary glaucoma | 91.02% | L5 | 0 | 0 | S0 | Hold |
| 8 | open-angle glaucoma | 90.16% | L4 | 0 | 9 | S1 | Research Question |
| 9 | filariasis | 90.01% | L5 | 0 | 1 | S0 | Hold |
| 10 | large intestine disease | 89.86% | L4 | 37 | 20 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Glucagon | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Glucagon | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=irritable bowel syndrome | success | 11 |  |
| 4 | ictrp | 2026-03-10 | drug=Glucagon, disease=irritable bowel syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Glucagon, disease=irritable bowel syndrome | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=cauda equina syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Glucagon, disease=cauda equina syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Glucagon, disease=cauda equina syndrome | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Glucagon, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Glucagon, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=acute laryngopharyngitis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Glucagon, disease=acute laryngopharyngitis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Glucagon, disease=acute laryngopharyngitis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=nasal cavity disease | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Glucagon, disease=nasal cavity disease | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Glucagon, disease=nasal cavity disease | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=pharyngitis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Glucagon, disease=pharyngitis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Glucagon, disease=pharyngitis | success | 7 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=primary hereditary glaucoma | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Glucagon, disease=primary hereditary glaucoma | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Glucagon, disease=primary hereditary glaucoma | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=open-angle glaucoma | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Glucagon, disease=open-angle glaucoma | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Glucagon, disease=open-angle glaucoma | success | 9 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=filariasis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Glucagon, disease=filariasis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Glucagon, disease=filariasis | success | 1 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Glucagon, disease=large intestine disease | success | 37 |  |
| 31 | ictrp | 2026-03-10 | drug=Glucagon, disease=large intestine disease | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Glucagon, disease=large intestine disease | success | 20 |  |