# Ketamine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Ketamine | |
| DrugBank ID | DB01221 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | headache disorder | 99.33% | L2 | 39 | 19 | S2 | Proceed with Guardrails |
| 2 | trigeminal autonomic cephalalgia | 98.98% | L3 | 2 | 14 | S2 | Research Question |
| 3 | common cold | 98.98% | L5 | 1 | 14 | S0 | Hold |
| 4 | migraine disorder | 98.65% | L2 | 15 | 20 | S3 | Proceed with Guardrails |
| 5 | migraine with brainstem aura | 98.46% | L3 | 0 | 15 | S2 | Research Question |
| 6 | attention deficit-hyperactivity disorder | 98.38% | L5 | 2 | 19 | S0 | Hold |
| 7 | Tourette syndrome | 98.17% | L5 | 0 | 6 | S0 | Hold |
| 8 | myofascial pain syndrome | 97.84% | L3 | 11 | 8 | S1 | Research Question |
| 9 | trichotillomania | 97.64% | L4 | 1 | 0 | S0 | Hold |
| 10 | psychotic disorder | 97.47% | L4 | 50 | 20 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Ketamine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Ketamine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=headache disorder | success | 39 |  |
| 4 | ictrp | 2026-03-10 | drug=Ketamine, disease=headache disorder | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Ketamine, disease=headache disorder | success | 19 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=trigeminal autonomic cephalalgia | success | 2 |  |
| 7 | ictrp | 2026-03-10 | drug=Ketamine, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Ketamine, disease=trigeminal autonomic cephalalgia | success | 14 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=common cold | success | 1 |  |
| 10 | ictrp | 2026-03-10 | drug=Ketamine, disease=common cold | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Ketamine, disease=common cold | success | 14 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=migraine disorder | success | 15 |  |
| 13 | ictrp | 2026-03-10 | drug=Ketamine, disease=migraine disorder | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Ketamine, disease=migraine disorder | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=migraine with brainstem aura | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Ketamine, disease=migraine with brainstem aura | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Ketamine, disease=migraine with brainstem aura | success | 15 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=attention deficit-hyperactivity disorder | success | 2 |  |
| 19 | ictrp | 2026-03-10 | drug=Ketamine, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Ketamine, disease=attention deficit-hyperactivity disorder | success | 19 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=Tourette syndrome | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Ketamine, disease=Tourette syndrome | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Ketamine, disease=Tourette syndrome | success | 6 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=myofascial pain syndrome | success | 11 |  |
| 25 | ictrp | 2026-03-10 | drug=Ketamine, disease=myofascial pain syndrome | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Ketamine, disease=myofascial pain syndrome | success | 8 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=trichotillomania | success | 1 |  |
| 28 | ictrp | 2026-03-10 | drug=Ketamine, disease=trichotillomania | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Ketamine, disease=trichotillomania | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Ketamine, disease=psychotic disorder | success | 50 |  |
| 31 | ictrp | 2026-03-10 | drug=Ketamine, disease=psychotic disorder | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Ketamine, disease=psychotic disorder | success | 20 |  |