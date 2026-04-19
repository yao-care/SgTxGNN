# Alverine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Alverine | |
| DrugBank ID | DB01616 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | dysthymic disorder | 99.83% | L5 | 0 | 0 | S0 | Hold |
| 2 | neurotic disorder | 99.59% | L5 | 0 | 0 | S0 | Hold |
| 3 | anxiety disorder | 99.45% | L4 | 1 | 1 | S1 | Research Question |
| 4 | migraine disorder | 99.25% | L5 | 0 | 0 | S0 | Hold |
| 5 | neurotic depression | 99.16% | L5 | 0 | 1 | S0 | Hold |
| 6 | melancholia | 99.14% | L5 | 0 | 1 | S0 | Hold |
| 7 | benign paroxysmal torticollis of infancy | 99.07% | L5 | 0 | 0 | S0 | Hold |
| 8 | agoraphobia | 99.06% | L5 | 0 | 0 | S0 | Hold |
| 9 | congenital isolated adrenocorticotropic hormone deficiency (disease) | 99.02% | L5 | 0 | 0 | S0 | Hold |
| 10 | migraine with brainstem aura | 98.95% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Alverine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Alverine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=dysthymic disorder | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Alverine, disease=dysthymic disorder | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Alverine, disease=dysthymic disorder | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=neurotic disorder | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Alverine, disease=neurotic disorder | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Alverine, disease=neurotic disorder | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=anxiety disorder | success | 1 |  |
| 10 | ictrp | 2026-03-09 | drug=Alverine, disease=anxiety disorder | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Alverine, disease=anxiety disorder | success | 1 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=migraine disorder | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Alverine, disease=migraine disorder | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Alverine, disease=migraine disorder | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=neurotic depression | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Alverine, disease=neurotic depression | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Alverine, disease=neurotic depression | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=melancholia | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Alverine, disease=melancholia | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Alverine, disease=melancholia | success | 1 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Alverine, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Alverine, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=agoraphobia | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Alverine, disease=agoraphobia | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Alverine, disease=agoraphobia | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=congenital isolated adrenocorticotropic hormone deficiency (disease) | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Alverine, disease=congenital isolated adrenocorticotropic hormone deficiency (disease) | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Alverine, disease=congenital isolated adrenocorticotropic hormone deficiency (disease) | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Alverine, disease=migraine with brainstem aura | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Alverine, disease=migraine with brainstem aura | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Alverine, disease=migraine with brainstem aura | success | 0 |  |