# Acyclovir 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Acyclovir | |
| DrugBank ID | DB00787 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | punctate epithelial keratoconjunctivitis | 99.67% | L4 | 0 | 2 | S1 | Research Question |
| 2 | common wart | 99.46% | L2 | 6 | 20 | S2 | Proceed with Guardrails |
| 3 | post-infectious neuralgia | 99.25% | L2 | 12 | 0 | S2 | Proceed with Guardrails |
| 4 | hepatitis C induced liver cirrhosis | 99.23% | L5 | 0 | 2 | S0 | Hold |
| 5 | eosinophilic pustular folliculitis | 99.22% | L5 | 0 | 1 | S0 | Hold |
| 6 | sequela of COVID-19 | 99.16% | L4 | 0 | 20 | S1 | Research Question |
| 7 | vulvovaginal candidiasis | 99.11% | L5 | 0 | 4 | S0 | Hold |
| 8 | papular urticaria | 99.09% | L5 | 0 | 0 | S0 | Hold |
| 9 | disease of orbital region | 99.08% | L2 | 50 | 3 | S3 | Proceed with Guardrails |
| 10 | epidemic keratoconjunctivitis | 99.07% | L4 | 0 | 7 | S1 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Acyclovir | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Acyclovir | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 4 | ictrp | 2026-03-09 | drug=Acyclovir, disease=punctate epithelial keratoconjunctivitis | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Acyclovir, disease=punctate epithelial keratoconjunctivitis | success | 2 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=common wart | success | 6 |  |
| 7 | ictrp | 2026-03-09 | drug=Acyclovir, disease=common wart | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Acyclovir, disease=common wart | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=post-infectious neuralgia | success | 12 |  |
| 10 | ictrp | 2026-03-09 | drug=Acyclovir, disease=post-infectious neuralgia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Acyclovir, disease=post-infectious neuralgia | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=hepatitis C induced liver cirrhosis | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Acyclovir, disease=hepatitis C induced liver cirrhosis | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Acyclovir, disease=hepatitis C induced liver cirrhosis | success | 2 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=eosinophilic pustular folliculitis | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Acyclovir, disease=eosinophilic pustular folliculitis | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Acyclovir, disease=eosinophilic pustular folliculitis | success | 1 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=sequela of COVID-19 | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Acyclovir, disease=sequela of COVID-19 | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Acyclovir, disease=sequela of COVID-19 | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=vulvovaginal candidiasis | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Acyclovir, disease=vulvovaginal candidiasis | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Acyclovir, disease=vulvovaginal candidiasis | success | 4 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=papular urticaria | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Acyclovir, disease=papular urticaria | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Acyclovir, disease=papular urticaria | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=disease of orbital region | success | 50 |  |
| 28 | ictrp | 2026-03-09 | drug=Acyclovir, disease=disease of orbital region | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Acyclovir, disease=disease of orbital region | success | 3 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Acyclovir, disease=epidemic keratoconjunctivitis | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Acyclovir, disease=epidemic keratoconjunctivitis | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Acyclovir, disease=epidemic keratoconjunctivitis | success | 7 |  |