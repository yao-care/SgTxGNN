# Ipratropium 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ipratropium | |
| DrugBank ID | DB00332 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | obstructive lung disease | 99.97% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 2 | nasal cavity disease | 99.86% | L3 | 0 | 1 | S2 | Proceed with Guardrails |
| 3 | pharyngitis | 99.85% | L4 | 3 | 5 | S1 | Research Question |
| 4 | acute laryngopharyngitis | 99.84% | L5 | 0 | 0 | S0 | Hold |
| 5 | respiratory malformation | 99.80% | L3 | 12 | 13 | S1 | Research Question |
| 6 | papillary conjunctivitis | 99.75% | L5 | 0 | 0 | S0 | Hold |
| 7 | Rienhoff syndrome | 99.69% | L5 | 0 | 0 | S0 | Hold |
| 8 | tracheal disease | 99.66% | L3 | 1 | 16 | S1 | Research Question |
| 9 | anaphylaxis | 99.38% | L4 | 0 | 10 | S1 | Research Question |
| 10 | food-dependent exercise-induced anaphylaxis | 99.36% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Ipratropium | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Ipratropium | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=obstructive lung disease | success | 50 |  |
| 4 | ictrp | 2026-03-09 | drug=Ipratropium, disease=obstructive lung disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Ipratropium, disease=obstructive lung disease | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=nasal cavity disease | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Ipratropium, disease=nasal cavity disease | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Ipratropium, disease=nasal cavity disease | success | 1 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=pharyngitis | success | 3 |  |
| 10 | ictrp | 2026-03-09 | drug=Ipratropium, disease=pharyngitis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Ipratropium, disease=pharyngitis | success | 5 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=acute laryngopharyngitis | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Ipratropium, disease=acute laryngopharyngitis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Ipratropium, disease=acute laryngopharyngitis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=respiratory malformation | success | 12 |  |
| 16 | ictrp | 2026-03-09 | drug=Ipratropium, disease=respiratory malformation | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Ipratropium, disease=respiratory malformation | success | 13 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=papillary conjunctivitis | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Ipratropium, disease=papillary conjunctivitis | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Ipratropium, disease=papillary conjunctivitis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=Rienhoff syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Ipratropium, disease=Rienhoff syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Ipratropium, disease=Rienhoff syndrome | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=tracheal disease | success | 1 |  |
| 25 | ictrp | 2026-03-09 | drug=Ipratropium, disease=tracheal disease | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Ipratropium, disease=tracheal disease | success | 16 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=anaphylaxis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Ipratropium, disease=anaphylaxis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Ipratropium, disease=anaphylaxis | success | 10 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Ipratropium, disease=food-dependent exercise-induced anaphylaxis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Ipratropium, disease=food-dependent exercise-induced anaphylaxis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Ipratropium, disease=food-dependent exercise-induced anaphylaxis | success | 0 |  |