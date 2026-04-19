# Calcitriol 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Calcitriol | |
| DrugBank ID | DB00136 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | obsolete vitamin D deficiency | 99.96% | L4 | 0 | 0 | S1 | Research Question |
| 2 | renal tubular acidosis | 99.93% | L3 | 0 | 18 | S1 | Research Question |
| 3 | familial isolated hypoparathyroidism due to impaired PTH secretion | 99.81% | L4 | 0 | 0 | S1 | Research Question |
| 4 | acromesomelic dysplasia, Campailla Martinelli type | 99.79% | L5 | 0 | 0 | S0 | Hold |
| 5 | craniofacial conodysplasia | 99.78% | L5 | 0 | 0 | S0 | Hold |
| 6 | Dahlberg-Borer-Newcomer syndrome | 99.76% | L4 | 0 | 20 | S1 | Research Question |
| 7 | hereditary hypophosphatemic rickets | 99.28% | L2 | 7 | 20 | S2 | Proceed with Guardrails |
| 8 | hypophosphatemic rickets | 98.08% | L2 | 7 | 20 | S2 | Proceed with Guardrails |
| 9 | osteomalacia (disease) | 97.68% | L3 | 2 | 19 | S2 | Proceed with Guardrails |
| 10 | vitamin D-dependent rickets | 97.42% | L3 | 0 | 20 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Calcitriol | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Calcitriol | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=obsolete vitamin D deficiency | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Calcitriol, disease=obsolete vitamin D deficiency | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Calcitriol, disease=obsolete vitamin D deficiency | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=renal tubular acidosis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Calcitriol, disease=renal tubular acidosis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Calcitriol, disease=renal tubular acidosis | success | 18 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=familial isolated hypoparathyroidism due to impaired PTH secretion | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Calcitriol, disease=familial isolated hypoparathyroidism due to impaired PTH secretion | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Calcitriol, disease=familial isolated hypoparathyroidism due to impaired PTH secretion | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=acromesomelic dysplasia, Campailla Martinelli type | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Calcitriol, disease=acromesomelic dysplasia, Campailla Martinelli type | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Calcitriol, disease=acromesomelic dysplasia, Campailla Martinelli type | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=craniofacial conodysplasia | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Calcitriol, disease=craniofacial conodysplasia | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Calcitriol, disease=craniofacial conodysplasia | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=Dahlberg-Borer-Newcomer syndrome | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Calcitriol, disease=Dahlberg-Borer-Newcomer syndrome | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Calcitriol, disease=Dahlberg-Borer-Newcomer syndrome | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=hereditary hypophosphatemic rickets | success | 7 |  |
| 22 | ictrp | 2026-03-09 | drug=Calcitriol, disease=hereditary hypophosphatemic rickets | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Calcitriol, disease=hereditary hypophosphatemic rickets | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=hypophosphatemic rickets | success | 7 |  |
| 25 | ictrp | 2026-03-09 | drug=Calcitriol, disease=hypophosphatemic rickets | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Calcitriol, disease=hypophosphatemic rickets | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=osteomalacia (disease) | success | 2 |  |
| 28 | ictrp | 2026-03-09 | drug=Calcitriol, disease=osteomalacia (disease) | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Calcitriol, disease=osteomalacia (disease) | success | 19 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Calcitriol, disease=vitamin D-dependent rickets | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Calcitriol, disease=vitamin D-dependent rickets | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Calcitriol, disease=vitamin D-dependent rickets | success | 20 |  |