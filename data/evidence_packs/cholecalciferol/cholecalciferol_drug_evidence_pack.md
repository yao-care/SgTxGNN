# Cholecalciferol 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cholecalciferol | |
| DrugBank ID | DB00169 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | familial isolated hypoparathyroidism due to impaired PTH secretion | 99.79% | L4 | 0 | 0 | S0 | Hold |
| 2 | acromesomelic dysplasia, Campailla Martinelli type | 99.78% | L5 | 0 | 0 | S0 | Hold |
| 3 | craniofacial conodysplasia | 99.75% | L5 | 0 | 0 | S0 | Hold |
| 4 | Dahlberg-Borer-Newcomer syndrome | 99.73% | L5 | 0 | 20 | S0 | Hold |
| 5 | hypophosphatemic rickets | 99.20% | L3 | 50 | 20 | S1 | Research Question |
| 6 | renal osteodystrophy | 99.11% | L3 | 32 | 0 | S1 | Research Question |
| 7 | renal tubular acidosis | 99.06% | L3 | 2 | 20 | S1 | Research Question |
| 8 | hereditary hypophosphatemic rickets | 98.97% | L3 | 50 | 20 | S1 | Research Question |
| 9 | hypophosphatemia (disease) | 98.96% | L3 | 50 | 20 | S1 | Research Question |
| 10 | impaired renal function disease | 98.40% | L2 | 50 | 20 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Cholecalciferol | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Cholecalciferol | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=familial isolated hypoparathyroidism due to impaired PTH secretion | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=familial isolated hypoparathyroidism due to impaired PTH secretion | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=familial isolated hypoparathyroidism due to impaired PTH secretion | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=acromesomelic dysplasia, Campailla Martinelli type | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=acromesomelic dysplasia, Campailla Martinelli type | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=acromesomelic dysplasia, Campailla Martinelli type | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=craniofacial conodysplasia | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=craniofacial conodysplasia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=craniofacial conodysplasia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=Dahlberg-Borer-Newcomer syndrome | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=Dahlberg-Borer-Newcomer syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=Dahlberg-Borer-Newcomer syndrome | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=hypophosphatemic rickets | success | 50 |  |
| 16 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=hypophosphatemic rickets | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=hypophosphatemic rickets | success | 20 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=renal osteodystrophy | success | 32 |  |
| 19 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=renal osteodystrophy | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=renal osteodystrophy | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=renal tubular acidosis | success | 2 |  |
| 22 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=renal tubular acidosis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=renal tubular acidosis | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=hereditary hypophosphatemic rickets | success | 50 |  |
| 25 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=hereditary hypophosphatemic rickets | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=hereditary hypophosphatemic rickets | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=hypophosphatemia (disease) | success | 50 |  |
| 28 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=hypophosphatemia (disease) | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=hypophosphatemia (disease) | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Cholecalciferol, disease=impaired renal function disease | success | 50 |  |
| 31 | ictrp | 2026-03-09 | drug=Cholecalciferol, disease=impaired renal function disease | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Cholecalciferol, disease=impaired renal function disease | success | 20 |  |