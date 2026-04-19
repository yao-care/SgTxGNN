# Cinacalcet 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Cinacalcet | |
| DrugBank ID | DB01012 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 98.48% | L5 | 0 | 0 | S0 | Hold |
| 2 | common cold | 95.39% | L5 | 0 | 0 | S0 | Hold |
| 3 | female breast carcinoma | 94.23% | L4 | 0 | 5 | S1 | Research Question |
| 4 | multiple endocrine neoplasia | 93.73% | L2 | 3 | 19 | S2 | Proceed with Guardrails |
| 5 | headache disorder | 93.08% | L5 | 0 | 0 | S0 | Hold |
| 6 | trigeminal autonomic cephalalgia | 92.16% | L5 | 0 | 0 | S0 | Hold |
| 7 | hypertrichosis (disease) | 91.66% | L5 | 0 | 0 | S0 | Hold |
| 8 | subarachnoid hemorrhage (disease) | 91.39% | L5 | 0 | 0 | S0 | Hold |
| 9 | pulmonary hypertension | 91.21% | L4 | 0 | 4 | S0 | Hold |
| 10 | obsolete familial combined hyperlipidemia | 90.80% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Cinacalcet | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Cinacalcet | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=common cold | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=common cold | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=common cold | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=female breast carcinoma | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=female breast carcinoma | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=female breast carcinoma | success | 5 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=multiple endocrine neoplasia | success | 3 |  |
| 13 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=multiple endocrine neoplasia | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=multiple endocrine neoplasia | success | 19 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=headache disorder | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=headache disorder | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=headache disorder | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=hypertrichosis (disease) | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=hypertrichosis (disease) | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=hypertrichosis (disease) | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=subarachnoid hemorrhage (disease) | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=subarachnoid hemorrhage (disease) | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=subarachnoid hemorrhage (disease) | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=pulmonary hypertension | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=pulmonary hypertension | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=pulmonary hypertension | success | 4 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Cinacalcet, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Cinacalcet, disease=obsolete familial combined hyperlipidemia | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Cinacalcet, disease=obsolete familial combined hyperlipidemia | success | 0 |  |