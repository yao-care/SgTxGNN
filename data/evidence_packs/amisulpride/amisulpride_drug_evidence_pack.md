# Amisulpride 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Amisulpride | |
| DrugBank ID | DB06288 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | schizophrenia | 96.05% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 2 | retinal dystrophy with or without extraocular anomalies | 94.84% | L5 | 0 | 15 | S0 | Hold |
| 3 | myopia X-linked | 94.42% | L5 | 0 | 0 | S0 | Hold |
| 4 | hydranencephaly (disease) | 94.38% | L5 | 0 | 0 | S0 | Hold |
| 5 | psychotic disorder | 94.33% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 6 | syndromic myopia | 94.27% | L5 | 0 | 0 | S0 | Hold |
| 7 | myopia 26, X-linked, female-limited | 93.44% | L5 | 0 | 0 | S0 | Hold |
| 8 | dysthymic disorder | 93.42% | L1 | 0 | 20 | S3 | Proceed with Guardrails |
| 9 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 93.17% | L5 | 0 | 0 | S0 | Hold |
| 10 | anxiety disorder | 92.98% | L3 | 8 | 20 | S1 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-10 | drug=Amisulpride | not_found | 0 |  |
| 2 | drugbank | 2026-03-10 | drug=Amisulpride | success | 1 |  |
| 3 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=schizophrenia | success | 50 |  |
| 4 | ictrp | 2026-03-10 | drug=Amisulpride, disease=schizophrenia | success | 0 |  |
| 5 | pubmed | 2026-03-10 | drug=Amisulpride, disease=schizophrenia | success | 20 |  |
| 6 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=retinal dystrophy with or without extraocular anomalies | success | 0 |  |
| 7 | ictrp | 2026-03-10 | drug=Amisulpride, disease=retinal dystrophy with or without extraocular anomalies | success | 0 |  |
| 8 | pubmed | 2026-03-10 | drug=Amisulpride, disease=retinal dystrophy with or without extraocular anomalies | success | 15 |  |
| 9 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=myopia X-linked | success | 0 |  |
| 10 | ictrp | 2026-03-10 | drug=Amisulpride, disease=myopia X-linked | success | 0 |  |
| 11 | pubmed | 2026-03-10 | drug=Amisulpride, disease=myopia X-linked | success | 0 |  |
| 12 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=hydranencephaly (disease) | success | 0 |  |
| 13 | ictrp | 2026-03-10 | drug=Amisulpride, disease=hydranencephaly (disease) | success | 0 |  |
| 14 | pubmed | 2026-03-10 | drug=Amisulpride, disease=hydranencephaly (disease) | success | 0 |  |
| 15 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=psychotic disorder | success | 50 |  |
| 16 | ictrp | 2026-03-10 | drug=Amisulpride, disease=psychotic disorder | success | 0 |  |
| 17 | pubmed | 2026-03-10 | drug=Amisulpride, disease=psychotic disorder | success | 20 |  |
| 18 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=syndromic myopia | success | 0 |  |
| 19 | ictrp | 2026-03-10 | drug=Amisulpride, disease=syndromic myopia | success | 0 |  |
| 20 | pubmed | 2026-03-10 | drug=Amisulpride, disease=syndromic myopia | success | 0 |  |
| 21 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=myopia 26, X-linked, female-limited | success | 0 |  |
| 22 | ictrp | 2026-03-10 | drug=Amisulpride, disease=myopia 26, X-linked, female-limited | success | 0 |  |
| 23 | pubmed | 2026-03-10 | drug=Amisulpride, disease=myopia 26, X-linked, female-limited | success | 0 |  |
| 24 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=dysthymic disorder | success | 0 |  |
| 25 | ictrp | 2026-03-10 | drug=Amisulpride, disease=dysthymic disorder | success | 0 |  |
| 26 | pubmed | 2026-03-10 | drug=Amisulpride, disease=dysthymic disorder | success | 20 |  |
| 27 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | success | 0 |  |
| 28 | ictrp | 2026-03-10 | drug=Amisulpride, disease=polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | success | 0 |  |
| 29 | pubmed | 2026-03-10 | drug=Amisulpride, disease=polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | success | 0 |  |
| 30 | clinicaltrials | 2026-03-10 | drug=Amisulpride, disease=anxiety disorder | success | 8 |  |
| 31 | ictrp | 2026-03-10 | drug=Amisulpride, disease=anxiety disorder | success | 0 |  |
| 32 | pubmed | 2026-03-10 | drug=Amisulpride, disease=anxiety disorder | success | 20 |  |