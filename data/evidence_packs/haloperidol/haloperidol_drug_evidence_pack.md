# Haloperidol 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Haloperidol | |
| DrugBank ID | DB00502 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | congenital disorder of glycosylation with defective fucosylation | 99.91% | L5 | 0 | 0 | S0 | Hold |
| 2 | retinal dystrophy with or without extraocular anomalies | 99.91% | L5 | 0 | 16 | S0 | Hold |
| 3 | hydranencephaly (disease) | 99.90% | L5 | 0 | 0 | S0 | Hold |
| 4 | myopia X-linked | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 5 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 6 | myopia 26, X-linked, female-limited | 99.89% | L5 | 0 | 0 | S0 | Hold |
| 7 | syndromic myopia | 99.88% | L5 | 0 | 0 | S0 | Hold |
| 8 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.88% | L5 | 0 | 0 | S0 | Hold |
| 9 | atypical glycine encephalopathy | 99.87% | L5 | 0 | 0 | S0 | Hold |
| 10 | manic bipolar affective disorder | 99.83% | L1 | 9 | 20 | S3 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Haloperidol | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Haloperidol | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=congenital disorder of glycosylation with defective fucosylation | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Haloperidol, disease=congenital disorder of glycosylation with defective fucosylation | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Haloperidol, disease=congenital disorder of glycosylation with defective fucosylation | success | 0 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=retinal dystrophy with or without extraocular anomalies | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Haloperidol, disease=retinal dystrophy with or without extraocular anomalies | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Haloperidol, disease=retinal dystrophy with or without extraocular anomalies | success | 16 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=hydranencephaly (disease) | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Haloperidol, disease=hydranencephaly (disease) | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Haloperidol, disease=hydranencephaly (disease) | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=myopia X-linked | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Haloperidol, disease=myopia X-linked | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Haloperidol, disease=myopia X-linked | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=Charcot-Marie-Tooth disease, demyelinating, type 1G | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Haloperidol, disease=Charcot-Marie-Tooth disease, demyelinating, type 1G | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Haloperidol, disease=Charcot-Marie-Tooth disease, demyelinating, type 1G | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=myopia 26, X-linked, female-limited | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Haloperidol, disease=myopia 26, X-linked, female-limited | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Haloperidol, disease=myopia 26, X-linked, female-limited | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=syndromic myopia | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Haloperidol, disease=syndromic myopia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Haloperidol, disease=syndromic myopia | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Haloperidol, disease=polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Haloperidol, disease=polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=atypical glycine encephalopathy | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Haloperidol, disease=atypical glycine encephalopathy | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Haloperidol, disease=atypical glycine encephalopathy | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Haloperidol, disease=manic bipolar affective disorder | success | 9 |  |
| 31 | ictrp | 2026-03-09 | drug=Haloperidol, disease=manic bipolar affective disorder | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Haloperidol, disease=manic bipolar affective disorder | success | 20 |  |