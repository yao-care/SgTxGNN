# Apixaban 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Apixaban | |
| DrugBank ID | DB06605 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | migraine disorder | 99.02% | L4 | 1 | 4 | S1 | Hold |
| 2 | migraine with or without aura, susceptibility to | 98.92% | L5 | 0 | 20 | S0 | Hold |
| 3 | leprosy | 98.90% | L5 | 0 | 1 | S0 | Hold |
| 4 | rheumatoid arthritis | 98.89% | L4 | 0 | 8 | S1 | Research Question |
| 5 | migraine with brainstem aura | 98.83% | L4 | 0 | 3 | S1 | Hold |
| 6 | Prinzmetal angina | 98.39% | L5 | 0 | 0 | S0 | Hold |
| 7 | brachydactyly-syndactyly syndrome | 98.18% | L5 | 0 | 0 | S0 | Hold |
| 8 | pulmonary hypertension | 98.13% | L3 | 8 | 19 | S2 | Research Question |
| 9 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 98.00% | L5 | 0 | 0 | S0 | Hold |
| 10 | kyphoscoliotic heart disease | 97.87% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Apixaban | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Apixaban | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=migraine disorder | success | 1 |  |
| 4 | ictrp | 2026-03-10 | drug=Apixaban, disease=migraine disorder | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Apixaban, disease=migraine disorder | success | 4 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Apixaban, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Apixaban, disease=migraine with or without aura, susceptibility to | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=leprosy | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Apixaban, disease=leprosy | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Apixaban, disease=leprosy | success | 1 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=rheumatoid arthritis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Apixaban, disease=rheumatoid arthritis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Apixaban, disease=rheumatoid arthritis | success | 8 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=migraine with brainstem aura | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Apixaban, disease=migraine with brainstem aura | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Apixaban, disease=migraine with brainstem aura | success | 3 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=Prinzmetal angina | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Apixaban, disease=Prinzmetal angina | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Apixaban, disease=Prinzmetal angina | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Apixaban, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Apixaban, disease=brachydactyly-syndactyly syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=pulmonary hypertension | success | 8 |  |
| 25 | ictrp | 2026-03-10 | drug=Apixaban, disease=pulmonary hypertension | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Apixaban, disease=pulmonary hypertension | success | 19 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Apixaban, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Apixaban, disease=colobomatous microphthalmia-rhizomelic dysplasia syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Apixaban, disease=kyphoscoliotic heart disease | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Apixaban, disease=kyphoscoliotic heart disease | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Apixaban, disease=kyphoscoliotic heart disease | success | 0 |  |