# Calcium carbonate 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Calcium carbonate | |
| DrugBank ID | DB06724 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | calcium-alkali syndrome | 93.16% | L3 | 1 | 16 | S1 | Hold |
| 2 | primary bone dysplasia with defective bone mineralization | 93.08% | L5 | 0 | 0 | S0 | Hold |
| 3 | gout | 81.85% | L4 | 0 | 11 | S0 | Hold |
| 4 | hypophosphatemia (disease) | 73.02% | L4 | 2 | 20 | S1 | Hold |
| 5 | potassium deficiency disease | 71.92% | L5 | 3 | 4 | S0 | Hold |
| 6 | digitalis poisoning | 66.60% | L5 | 0 | 0 | S0 | Hold |
| 7 | gastroduodenitis | 65.78% | L3 | 0 | 12 | S2 | Proceed with Guardrails |
| 8 | hyperlipidemia | 64.56% | L3 | 2 | 20 | S1 | Research Question |
| 9 | peptic ulcer disease | 59.77% | L3 | 1 | 18 | S2 | Proceed with Guardrails |
| 10 | duodenogastric reflux | 59.38% | L4 | 0 | 1 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Calcium carbonate | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Calcium carbonate | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=calcium-alkali syndrome | success | 1 |  |
| 4 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=calcium-alkali syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=calcium-alkali syndrome | success | 16 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=primary bone dysplasia with defective bone mineralization | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=primary bone dysplasia with defective bone mineralization | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=primary bone dysplasia with defective bone mineralization | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=gout | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=gout | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=gout | success | 11 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=hypophosphatemia (disease) | success | 2 |  |
| 13 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=hypophosphatemia (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=hypophosphatemia (disease) | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=potassium deficiency disease | success | 3 |  |
| 16 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=potassium deficiency disease | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=potassium deficiency disease | success | 4 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=digitalis poisoning | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=digitalis poisoning | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=digitalis poisoning | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=gastroduodenitis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=gastroduodenitis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=gastroduodenitis | success | 12 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=hyperlipidemia | success | 2 |  |
| 25 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=hyperlipidemia | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=hyperlipidemia | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=peptic ulcer disease | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=peptic ulcer disease | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=peptic ulcer disease | success | 18 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Calcium carbonate, disease=duodenogastric reflux | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Calcium carbonate, disease=duodenogastric reflux | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Calcium carbonate, disease=duodenogastric reflux | success | 1 |  |