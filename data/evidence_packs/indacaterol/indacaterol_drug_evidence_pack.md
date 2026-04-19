# Indacaterol 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Indacaterol | |
| DrugBank ID | DB05039 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 99.54% | L5 | 0 | 0 | S0 | Hold |
| 2 | headache disorder | 99.53% | L5 | 2 | 0 | S0 | Hold |
| 3 | trigeminal autonomic cephalalgia | 99.33% | L5 | 0 | 0 | S0 | Hold |
| 4 | paratenonitis | 99.26% | L5 | 0 | 0 | S0 | Hold |
| 5 | calcific tendinitis | 99.25% | L5 | 0 | 0 | S0 | Hold |
| 6 | hypertrichosis (disease) | 99.23% | L5 | 0 | 0 | S0 | Hold |
| 7 | bronchial disease | 99.18% | L1 | 37 | 20 | S3 | Proceed with Guardrails |
| 8 | myositis | 99.12% | L5 | 0 | 0 | S0 | Hold |
| 9 | anaphylaxis | 99.07% | L4 | 0 | 0 | S1 | Research Question |
| 10 | Ambras type hypertrichosis universalis congenita | 99.06% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Indacaterol | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Indacaterol | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 4 | ictrp | 2026-03-10 | drug=Indacaterol, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Indacaterol, disease=nephrogenic syndrome of inappropriate antidiuresis | success | 0 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=headache disorder | success | 2 |  |
| 7 | ictrp | 2026-03-10 | drug=Indacaterol, disease=headache disorder | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Indacaterol, disease=headache disorder | success | 0 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Indacaterol, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Indacaterol, disease=trigeminal autonomic cephalalgia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=paratenonitis | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Indacaterol, disease=paratenonitis | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Indacaterol, disease=paratenonitis | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=calcific tendinitis | success | 0 |  |
| 16 | ictrp | 2026-03-10 | drug=Indacaterol, disease=calcific tendinitis | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Indacaterol, disease=calcific tendinitis | success | 0 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=hypertrichosis (disease) | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Indacaterol, disease=hypertrichosis (disease) | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Indacaterol, disease=hypertrichosis (disease) | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=bronchial disease | success | 37 |  |
| 22 | ictrp | 2026-03-10 | drug=Indacaterol, disease=bronchial disease | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Indacaterol, disease=bronchial disease | success | 20 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=myositis | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Indacaterol, disease=myositis | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Indacaterol, disease=myositis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=anaphylaxis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Indacaterol, disease=anaphylaxis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Indacaterol, disease=anaphylaxis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Indacaterol, disease=Ambras type hypertrichosis universalis congenita | success | 0 |  |
| 31 | ictrp | 2026-03-10 | drug=Indacaterol, disease=Ambras type hypertrichosis universalis congenita | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Indacaterol, disease=Ambras type hypertrichosis universalis congenita | success | 0 |  |