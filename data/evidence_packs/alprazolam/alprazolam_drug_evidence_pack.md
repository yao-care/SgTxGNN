# Alprazolam 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Alprazolam | |
| DrugBank ID | DB00404 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | insomnia (disease) | 99.81% | L3 | 7 | 18 | S2 | Proceed with Guardrails |
| 2 | benign paroxysmal torticollis of infancy | 99.61% | L5 | 0 | 0 | S0 | Hold |
| 3 | agoraphobia | 99.56% | L1 | 2 | 19 | S3 | Proceed with Guardrails |
| 4 | attention deficit-hyperactivity disorder | 98.95% | L4 | 0 | 5 | S0 | Hold |
| 5 | attention deficit hyperactivity disorder, inattentive type | 98.62% | L5 | 0 | 0 | S0 | Hold |
| 6 | obsessive-compulsive disorder | 98.24% | L4 | 0 | 20 | S1 | Hold |
| 7 | chondromyxoid fibroma | 98.12% | L5 | 0 | 0 | S0 | Hold |
| 8 | specific developmental disorder | 98.02% | L5 | 2 | 1 | S0 | Hold |
| 9 | faciodigitogenital syndrome | 97.95% | L5 | 0 | 0 | S0 | Hold |
| 10 | phobic disorder | 97.47% | L2 | 3 | 20 | S2 | Proceed with Guardrails |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Alprazolam | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Alprazolam | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=insomnia (disease) | success | 7 |  |
| 4 | ictrp | 2026-03-09 | drug=Alprazolam, disease=insomnia (disease) | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Alprazolam, disease=insomnia (disease) | success | 18 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Alprazolam, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Alprazolam, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=agoraphobia | success | 2 |  |
| 10 | ictrp | 2026-03-09 | drug=Alprazolam, disease=agoraphobia | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Alprazolam, disease=agoraphobia | success | 19 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Alprazolam, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Alprazolam, disease=attention deficit-hyperactivity disorder | success | 5 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Alprazolam, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Alprazolam, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=obsessive-compulsive disorder | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Alprazolam, disease=obsessive-compulsive disorder | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Alprazolam, disease=obsessive-compulsive disorder | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=chondromyxoid fibroma | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Alprazolam, disease=chondromyxoid fibroma | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Alprazolam, disease=chondromyxoid fibroma | success | 0 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=specific developmental disorder | success | 2 |  |
| 25 | ictrp | 2026-03-09 | drug=Alprazolam, disease=specific developmental disorder | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Alprazolam, disease=specific developmental disorder | success | 1 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=faciodigitogenital syndrome | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Alprazolam, disease=faciodigitogenital syndrome | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Alprazolam, disease=faciodigitogenital syndrome | success | 0 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Alprazolam, disease=phobic disorder | success | 3 |  |
| 31 | ictrp | 2026-03-09 | drug=Alprazolam, disease=phobic disorder | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Alprazolam, disease=phobic disorder | success | 20 |  |