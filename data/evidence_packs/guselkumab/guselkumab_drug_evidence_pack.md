# Guselkumab 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Guselkumab | |
| DrugBank ID | DB11834 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | drug-induced osteoporosis | 99.84% | L5 | 0 | 0 | S0 | Hold |
| 2 | severe nonproliferative diabetic retinopathy | 99.80% | L5 | 0 | 0 | S0 | Hold |
| 3 | psoriasis | 99.75% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 4 | diabetic retinopathy | 99.74% | L5 | 0 | 0 | S0 | Hold |
| 5 | renal osteodystrophy | 99.73% | L5 | 0 | 0 | S0 | Hold |
| 6 | ulcerative colitis (disease) | 99.70% | L1 | 17 | 20 | S3 | Proceed with Guardrails |
| 7 | congenital hypotrichosis with juvenile macular dystrophy | 99.67% | L5 | 0 | 0 | S0 | Hold |
| 8 | primary release disorder of platelets | 99.61% | L5 | 0 | 0 | S0 | Hold |
| 9 | Glanzmann thrombasthenia | 99.60% | L5 | 0 | 0 | S0 | Hold |
| 10 | non-renal secondary hyperparathyroidism | 99.55% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Guselkumab | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Guselkumab | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=drug-induced osteoporosis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Guselkumab, disease=drug-induced osteoporosis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Guselkumab, disease=drug-induced osteoporosis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=severe nonproliferative diabetic retinopathy | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Guselkumab, disease=severe nonproliferative diabetic retinopathy | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Guselkumab, disease=severe nonproliferative diabetic retinopathy | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=psoriasis | success | 50 |  |
| 10 | ictrp | 2026-03-09 | drug=Guselkumab, disease=psoriasis | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Guselkumab, disease=psoriasis | success | 20 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=diabetic retinopathy | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Guselkumab, disease=diabetic retinopathy | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Guselkumab, disease=diabetic retinopathy | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=renal osteodystrophy | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Guselkumab, disease=renal osteodystrophy | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Guselkumab, disease=renal osteodystrophy | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=ulcerative colitis (disease) | success | 17 |  |
| 19 | ictrp | 2026-03-09 | drug=Guselkumab, disease=ulcerative colitis (disease) | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Guselkumab, disease=ulcerative colitis (disease) | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=congenital hypotrichosis with juvenile macular dystrophy | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Guselkumab, disease=congenital hypotrichosis with juvenile macular dystrophy | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Guselkumab, disease=congenital hypotrichosis with juvenile macular dystrophy | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=primary release disorder of platelets | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Guselkumab, disease=primary release disorder of platelets | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Guselkumab, disease=primary release disorder of platelets | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=Glanzmann thrombasthenia | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Guselkumab, disease=Glanzmann thrombasthenia | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Guselkumab, disease=Glanzmann thrombasthenia | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Guselkumab, disease=non-renal secondary hyperparathyroidism | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Guselkumab, disease=non-renal secondary hyperparathyroidism | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Guselkumab, disease=non-renal secondary hyperparathyroidism | success | 0 |  |