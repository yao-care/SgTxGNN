# Cysteine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cysteine | |
| DrugBank ID | DB00151 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | dry eye syndrome | 99.98% | L2 | 7 | 20 | S2 | Proceed with Guardrails |
| 2 | closed-angle glaucoma | 99.95% | L5 | 0 | 5 | S0 | Hold |
| 3 | nasal cavity disease | 99.88% | L3 | 1 | 16 | S1 | Research Question |
| 4 | acute laryngopharyngitis | 99.79% | L5 | 0 | 0 | S0 | Hold |
| 5 | pharyngitis | 99.78% | L3 | 1 | 20 | S1 | Research Question |
| 6 | exercise-induced malignant hyperthermia | 99.26% | L5 | 0 | 1 | S0 | Hold |
| 7 | angle-closure glaucoma | 99.06% | L5 | 0 | 5 | S0 | Hold |
| 8 | excretory apparatus of the lacrimal system anomaly | 98.72% | L5 | 0 | 0 | S0 | Hold |
| 9 | tracheal disease | 98.68% | L2 | 5 | 20 | S2 | Proceed with Guardrails |
| 10 | nasolacrimal duct disease | 98.66% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Cysteine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Cysteine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=dry eye syndrome | success | 7 |  |
| 4 | ictrp | 2026-03-09 | drug=Cysteine, disease=dry eye syndrome | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Cysteine, disease=dry eye syndrome | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=closed-angle glaucoma | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Cysteine, disease=closed-angle glaucoma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Cysteine, disease=closed-angle glaucoma | success | 5 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=nasal cavity disease | success | 1 |  |
| 10 | ictrp | 2026-03-09 | drug=Cysteine, disease=nasal cavity disease | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Cysteine, disease=nasal cavity disease | success | 16 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=acute laryngopharyngitis | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Cysteine, disease=acute laryngopharyngitis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Cysteine, disease=acute laryngopharyngitis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=pharyngitis | success | 1 |  |
| 16 | ictrp | 2026-03-09 | drug=Cysteine, disease=pharyngitis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Cysteine, disease=pharyngitis | success | 20 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=exercise-induced malignant hyperthermia | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Cysteine, disease=exercise-induced malignant hyperthermia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Cysteine, disease=exercise-induced malignant hyperthermia | success | 1 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=angle-closure glaucoma | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Cysteine, disease=angle-closure glaucoma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Cysteine, disease=angle-closure glaucoma | success | 5 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=excretory apparatus of the lacrimal system anomaly | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Cysteine, disease=excretory apparatus of the lacrimal system anomaly | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Cysteine, disease=excretory apparatus of the lacrimal system anomaly | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=tracheal disease | success | 5 |  |
| 28 | ictrp | 2026-03-09 | drug=Cysteine, disease=tracheal disease | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Cysteine, disease=tracheal disease | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Cysteine, disease=nasolacrimal duct disease | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Cysteine, disease=nasolacrimal duct disease | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Cysteine, disease=nasolacrimal duct disease | success | 0 |  |