# Dextromethorphan 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dextromethorphan | |
| DrugBank ID | DB00514 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | nasal cavity disease | 99.98% | L1 | 1 | 0 | S3 | Proceed with Guardrails |
| 2 | acute laryngopharyngitis | 99.98% | L4 | 0 | 0 | S1 | Research Question |
| 3 | faucial diphtheria | 99.36% | L5 | 0 | 0 | S0 | Hold |
| 4 | trigeminal autonomic cephalalgia | 99.32% | L5 | 0 | 0 | S0 | Hold |
| 5 | cervical disc degenerative disorder | 99.30% | L5 | 0 | 0 | S0 | Hold |
| 6 | allergic urticaria | 99.25% | L5 | 0 | 0 | S0 | Hold |
| 7 | tracheal disease | 98.59% | L4 | 0 | 2 | S1 | Research Question |
| 8 | massive neonatal aspiration syndrome | 97.84% | L5 | 0 | 0 | S0 | Hold |
| 9 | respiratory syncytial virus bronchiolitis | 97.65% | L5 | 0 | 0 | S0 | Hold |
| 10 | hantavirus infectious disease | 97.64% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Dextromethorphan | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Dextromethorphan | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=nasal cavity disease | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=nasal cavity disease | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=nasal cavity disease | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=acute laryngopharyngitis | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=acute laryngopharyngitis | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=acute laryngopharyngitis | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=faucial diphtheria | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=faucial diphtheria | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=faucial diphtheria | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=cervical disc degenerative disorder | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=cervical disc degenerative disorder | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=cervical disc degenerative disorder | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=allergic urticaria | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=allergic urticaria | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=allergic urticaria | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=tracheal disease | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=tracheal disease | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=tracheal disease | success | 2 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=massive neonatal aspiration syndrome | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=massive neonatal aspiration syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=massive neonatal aspiration syndrome | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=respiratory syncytial virus bronchiolitis | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=respiratory syncytial virus bronchiolitis | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=respiratory syncytial virus bronchiolitis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Dextromethorphan, disease=hantavirus infectious disease | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Dextromethorphan, disease=hantavirus infectious disease | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Dextromethorphan, disease=hantavirus infectious disease | success | 0 |  |