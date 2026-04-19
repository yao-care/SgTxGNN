# Imipramine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Imipramine | |
| DrugBank ID | DB00458 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | attention deficit-hyperactivity disorder | 99.90% | L3 | 1 | 20 | S2 | Research Question |
| 2 | attention deficit hyperactivity disorder, inattentive type | 99.83% | L5 | 0 | 0 | S0 | Hold |
| 3 | faciodigitogenital syndrome | 99.80% | L5 | 0 | 0 | S0 | Hold |
| 4 | specific developmental disorder | 99.67% | L5 | 1 | 0 | S0 | Hold |
| 5 | chondromyxoid fibroma | 99.66% | L5 | 0 | 0 | S0 | Hold |
| 6 | benign paroxysmal torticollis of infancy | 99.21% | L5 | 0 | 0 | S0 | Hold |
| 7 | obsessive-compulsive disorder | 99.01% | L3 | 2 | 20 | S1 | Research Question |
| 8 | agoraphobia | 98.97% | L2 | 0 | 20 | S3 | Proceed with Guardrails |
| 9 | histrionic personality disorder (disease) | 98.61% | L4 | 0 | 1 | S0 | Hold |
| 10 | schizoid personality disorder | 98.61% | L4 | 0 | 1 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Imipramine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Imipramine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=attention deficit-hyperactivity disorder | success | 1 |  |
| 4 | ictrp | 2026-03-09 | drug=Imipramine, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Imipramine, disease=attention deficit-hyperactivity disorder | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Imipramine, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Imipramine, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=faciodigitogenital syndrome | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Imipramine, disease=faciodigitogenital syndrome | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Imipramine, disease=faciodigitogenital syndrome | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=specific developmental disorder | success | 1 |  |
| 13 | ictrp | 2026-03-09 | drug=Imipramine, disease=specific developmental disorder | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Imipramine, disease=specific developmental disorder | success | 0 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=chondromyxoid fibroma | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Imipramine, disease=chondromyxoid fibroma | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Imipramine, disease=chondromyxoid fibroma | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Imipramine, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Imipramine, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=obsessive-compulsive disorder | success | 2 |  |
| 22 | ictrp | 2026-03-09 | drug=Imipramine, disease=obsessive-compulsive disorder | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Imipramine, disease=obsessive-compulsive disorder | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=agoraphobia | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Imipramine, disease=agoraphobia | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Imipramine, disease=agoraphobia | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=histrionic personality disorder (disease) | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Imipramine, disease=histrionic personality disorder (disease) | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Imipramine, disease=histrionic personality disorder (disease) | success | 1 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Imipramine, disease=schizoid personality disorder | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Imipramine, disease=schizoid personality disorder | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Imipramine, disease=schizoid personality disorder | success | 1 |  |