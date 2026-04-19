# Acetylcysteine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Acetylcysteine | |
| DrugBank ID | DB06151 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | thrombotic disease | 99.96% | L1 | 9 | 20 | S3 | Proceed with Guardrails |
| 2 | closed-angle glaucoma | 99.95% | L5 | 0 | 0 | S0 | Hold |
| 3 | nasal cavity disease | 99.92% | L4 | 0 | 6 | S1 | Research Question |
| 4 | dry eye syndrome | 99.87% | L2 | 11 | 20 | S2 | Proceed with Guardrails |
| 5 | pharyngitis | 99.80% | L3 | 1 | 8 | S2 | Research Question |
| 6 | acute laryngopharyngitis | 99.79% | L5 | 0 | 0 | S0 | Hold |
| 7 | tracheal disease | 99.57% | L3 | 4 | 20 | S1 | Research Question |
| 8 | transient ischemic attack (disease) | 99.53% | L4 | 0 | 9 | S0 | Hold |
| 9 | laryngotracheitis | 99.34% | L5 | 0 | 0 | S0 | Hold |
| 10 | angle-closure glaucoma | 99.31% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Acetylcysteine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Acetylcysteine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=thrombotic disease | success | 9 |  |
| 4 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=thrombotic disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=thrombotic disease | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=closed-angle glaucoma | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=closed-angle glaucoma | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=closed-angle glaucoma | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=nasal cavity disease | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=nasal cavity disease | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=nasal cavity disease | success | 6 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=dry eye syndrome | success | 11 |  |
| 13 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=dry eye syndrome | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=dry eye syndrome | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=pharyngitis | success | 1 |  |
| 16 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=pharyngitis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=pharyngitis | success | 8 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=acute laryngopharyngitis | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=acute laryngopharyngitis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=acute laryngopharyngitis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=tracheal disease | success | 4 |  |
| 22 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=tracheal disease | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=tracheal disease | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=transient ischemic attack (disease) | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=transient ischemic attack (disease) | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=transient ischemic attack (disease) | success | 9 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=laryngotracheitis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=laryngotracheitis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=laryngotracheitis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Acetylcysteine, disease=angle-closure glaucoma | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Acetylcysteine, disease=angle-closure glaucoma | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Acetylcysteine, disease=angle-closure glaucoma | success | 0 |  |