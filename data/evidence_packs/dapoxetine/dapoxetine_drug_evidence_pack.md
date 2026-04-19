# Dapoxetine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Dapoxetine | |
| DrugBank ID | DB04884 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | migraine disorder | 99.34% | L4 | 0 | 2 | S0 | Hold |
| 2 | dysthymic disorder | 99.14% | L4 | 0 | 0 | S0 | Hold |
| 3 | migraine with brainstem aura | 99.11% | L5 | 0 | 0 | S0 | Hold |
| 4 | migraine with or without aura, susceptibility to | 98.75% | L5 | 0 | 20 | S0 | Hold |
| 5 | neurotic disorder | 98.51% | L4 | 0 | 0 | S0 | Hold |
| 6 | atrophoderma vermiculata | 98.19% | L5 | 0 | 0 | S0 | Hold |
| 7 | ulerythema ophryogenesis | 97.59% | L5 | 0 | 0 | S0 | Hold |
| 8 | neurotic depression | 97.08% | L4 | 0 | 1 | S0 | Hold |
| 9 | melancholia | 97.02% | L4 | 0 | 1 | S0 | Hold |
| 10 | congenital isolated adrenocorticotropic hormone deficiency (disease) | 96.53% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Dapoxetine | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Dapoxetine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=migraine disorder | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=migraine disorder | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=migraine disorder | success | 2 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=dysthymic disorder | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=dysthymic disorder | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=dysthymic disorder | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=migraine with brainstem aura | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=migraine with brainstem aura | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=migraine with brainstem aura | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=migraine with or without aura, susceptibility to | success | 20 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=neurotic disorder | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=neurotic disorder | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=neurotic disorder | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=atrophoderma vermiculata | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=atrophoderma vermiculata | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=atrophoderma vermiculata | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=ulerythema ophryogenesis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=ulerythema ophryogenesis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=ulerythema ophryogenesis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=neurotic depression | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=neurotic depression | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=neurotic depression | success | 1 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=melancholia | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=melancholia | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=melancholia | success | 1 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Dapoxetine, disease=congenital isolated adrenocorticotropic hormone deficiency (disease) | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Dapoxetine, disease=congenital isolated adrenocorticotropic hormone deficiency (disease) | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Dapoxetine, disease=congenital isolated adrenocorticotropic hormone deficiency (disease) | success | 0 |  |