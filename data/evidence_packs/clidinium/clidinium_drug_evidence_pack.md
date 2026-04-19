# Clidinium 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clidinium | |
| DrugBank ID | DB00771 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | cauda equina syndrome | 99.93% | L5 | 0 | 0 | S0 | Hold |
| 2 | obsolete neurogenic bladder (disease) | 99.91% | L4 | 0 | 0 | S1 | Research Question |
| 3 | gastroduodenitis | 99.89% | L4 | 0 | 2 | S1 | Research Question |
| 4 | peptic ulcer disease | 99.83% | L3 | 0 | 7 | S2 | Proceed with Guardrails |
| 5 | myasthenia gravis with thymus hyperplasia | 99.71% | L5 | 0 | 0 | S0 | Hold |
| 6 | myasthenia, limb-girdle, autoimmune | 99.68% | L5 | 0 | 0 | S0 | Hold |
| 7 | neonatal myasthenia gravis | 99.66% | L5 | 0 | 0 | S0 | Hold |
| 8 | autoimmune disease of peripheral nervous system | 99.63% | L5 | 0 | 0 | S0 | Hold |
| 9 | disease of receptor activity | 99.61% | L5 | 0 | 0 | S0 | Hold |
| 10 | large intestine disease | 99.16% | L4 | 0 | 1 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Clidinium | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Clidinium | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=cauda equina syndrome | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Clidinium, disease=cauda equina syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Clidinium, disease=cauda equina syndrome | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Clidinium, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Clidinium, disease=obsolete neurogenic bladder (disease) | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=gastroduodenitis | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Clidinium, disease=gastroduodenitis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Clidinium, disease=gastroduodenitis | success | 2 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=peptic ulcer disease | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Clidinium, disease=peptic ulcer disease | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Clidinium, disease=peptic ulcer disease | success | 7 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=myasthenia gravis with thymus hyperplasia | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Clidinium, disease=myasthenia gravis with thymus hyperplasia | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Clidinium, disease=myasthenia gravis with thymus hyperplasia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=myasthenia, limb-girdle, autoimmune | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Clidinium, disease=myasthenia, limb-girdle, autoimmune | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Clidinium, disease=myasthenia, limb-girdle, autoimmune | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=neonatal myasthenia gravis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Clidinium, disease=neonatal myasthenia gravis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Clidinium, disease=neonatal myasthenia gravis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=autoimmune disease of peripheral nervous system | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Clidinium, disease=autoimmune disease of peripheral nervous system | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Clidinium, disease=autoimmune disease of peripheral nervous system | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=disease of receptor activity | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Clidinium, disease=disease of receptor activity | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Clidinium, disease=disease of receptor activity | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Clidinium, disease=large intestine disease | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Clidinium, disease=large intestine disease | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Clidinium, disease=large intestine disease | success | 1 |  |