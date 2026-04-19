# Abiraterone 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Abiraterone | |
| DrugBank ID | DB05812 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | migraine disorder | 98.81% | L5 | 0 | 0 | S0 | Hold |
| 2 | migraine with or without aura, susceptibility to | 98.75% | L5 | 0 | 20 | S0 | Hold |
| 3 | migraine with brainstem aura | 98.61% | L5 | 0 | 0 | S0 | Hold |
| 4 | leprosy | 98.58% | L5 | 0 | 0 | S0 | Hold |
| 5 | pulmonary hypertension | 98.36% | L5 | 1 | 5 | S0 | Research Question |
| 6 | nephrogenic syndrome of inappropriate antidiuresis | 98.23% | L5 | 0 | 0 | S0 | Hold |
| 7 | rheumatoid arthritis | 98.13% | L5 | 0 | 0 | S0 | Hold |
| 8 | kyphoscoliotic heart disease | 98.11% | L5 | 0 | 0 | S0 | Hold |
| 9 | atrophoderma vermiculata | 97.66% | L5 | 0 | 0 | S0 | Hold |
| 10 | ulerythema ophryogenesis | 97.53% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Abiraterone | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Abiraterone | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=migraine disorder | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Abiraterone, disease=migraine disorder | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Abiraterone, disease=migraine disorder | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Abiraterone, disease=migraine with or without aura, susceptibility to | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Abiraterone, disease=migraine with or without aura, susceptibility to | success | 20 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=migraine with brainstem aura | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Abiraterone, disease=migraine with brainstem aura | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Abiraterone, disease=migraine with brainstem aura | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=leprosy | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Abiraterone, disease=leprosy | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Abiraterone, disease=leprosy | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=pulmonary hypertension | success | 1 |  |
| 16 | ictrp | 2026-03-10 | drug=Abiraterone, disease=pulmonary hypertension | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Abiraterone, disease=pulmonary hypertension | success | 5 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Abiraterone, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Abiraterone, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=rheumatoid arthritis | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Abiraterone, disease=rheumatoid arthritis | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Abiraterone, disease=rheumatoid arthritis | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=kyphoscoliotic heart disease | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Abiraterone, disease=kyphoscoliotic heart disease | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Abiraterone, disease=kyphoscoliotic heart disease | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=atrophoderma vermiculata | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Abiraterone, disease=atrophoderma vermiculata | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Abiraterone, disease=atrophoderma vermiculata | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Abiraterone, disease=ulerythema ophryogenesis | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Abiraterone, disease=ulerythema ophryogenesis | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Abiraterone, disease=ulerythema ophryogenesis | success | 0 |  |