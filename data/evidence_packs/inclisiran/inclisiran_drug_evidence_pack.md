# Inclisiran 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Inclisiran | |
| DrugBank ID | DB14901 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | potassium deficiency disease | 99.93% | L5 | 0 | 0 | S0 | Hold |
| 2 | esophageal disease | 99.87% | L5 | 0 | 0 | S0 | Hold |
| 3 | atypical coarctation of aorta | 99.86% | L5 | 0 | 0 | S0 | Hold |
| 4 | migraine disorder | 99.83% | L5 | 0 | 0 | S0 | Hold |
| 5 | non-syndromic esophageal malformation | 99.83% | L5 | 0 | 0 | S0 | Hold |
| 6 | migraine with brainstem aura | 99.78% | L5 | 0 | 0 | S0 | Hold |
| 7 | migraine with or without aura, susceptibility to | 99.78% | L4 | 0 | 20 | S1 | Research Question |
| 8 | aortic malformation | 99.76% | L3 | 2 | 0 | S2 | Proceed with Guardrails |
| 9 | esophageal ulcer | 99.73% | L5 | 0 | 0 | S0 | Hold |
| 10 | Raynaud disease | 99.73% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Inclisiran | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Inclisiran | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=potassium deficiency disease | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Inclisiran, disease=potassium deficiency disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Inclisiran, disease=potassium deficiency disease | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=esophageal disease | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Inclisiran, disease=esophageal disease | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Inclisiran, disease=esophageal disease | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=atypical coarctation of aorta | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Inclisiran, disease=atypical coarctation of aorta | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Inclisiran, disease=atypical coarctation of aorta | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=migraine disorder | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Inclisiran, disease=migraine disorder | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Inclisiran, disease=migraine disorder | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=non-syndromic esophageal malformation | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Inclisiran, disease=non-syndromic esophageal malformation | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Inclisiran, disease=non-syndromic esophageal malformation | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=migraine with brainstem aura | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Inclisiran, disease=migraine with brainstem aura | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Inclisiran, disease=migraine with brainstem aura | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Inclisiran, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Inclisiran, disease=migraine with or without aura, susceptibility to | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=aortic malformation | success | 2 |  |
| 25 | ictrp | 2026-03-09 | drug=Inclisiran, disease=aortic malformation | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Inclisiran, disease=aortic malformation | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=esophageal ulcer | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Inclisiran, disease=esophageal ulcer | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Inclisiran, disease=esophageal ulcer | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Inclisiran, disease=Raynaud disease | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Inclisiran, disease=Raynaud disease | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Inclisiran, disease=Raynaud disease | success | 0 |  |