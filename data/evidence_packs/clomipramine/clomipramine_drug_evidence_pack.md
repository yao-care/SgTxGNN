# Clomipramine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clomipramine | |
| DrugBank ID | DB01242 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | anxiety disorder | 99.93% | L1 | 18 | 20 | S3 | Proceed with Guardrails |
| 2 | benign paroxysmal torticollis of infancy | 99.90% | L5 | 0 | 0 | S0 | Hold |
| 3 | schizoid personality disorder | 99.90% | L5 | 0 | 1 | S0 | Hold |
| 4 | paranoid personality disorder | 99.90% | L5 | 0 | 2 | S0 | Hold |
| 5 | histrionic personality disorder (disease) | 99.90% | L5 | 0 | 0 | S0 | Hold |
| 6 | schizotypal personality disorder | 99.90% | L4 | 0 | 5 | S0 | Hold |
| 7 | agoraphobia | 99.87% | L2 | 0 | 20 | S2 | Research Question |
| 8 | major depressive disorder | 99.77% | L1 | 10 | 20 | S3 | Proceed with Guardrails |
| 9 | endogenous depression | 99.71% | L2 | 0 | 20 | S3 | Proceed with Guardrails |
| 10 | attention deficit-hyperactivity disorder | 99.58% | L2 | 0 | 20 | S2 | Research Question |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Clomipramine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Clomipramine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=anxiety disorder | success | 18 |  |
| 4 | ictrp | 2026-03-09 | drug=Clomipramine, disease=anxiety disorder | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Clomipramine, disease=anxiety disorder | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Clomipramine, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Clomipramine, disease=benign paroxysmal torticollis of infancy | success | 0 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=schizoid personality disorder | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Clomipramine, disease=schizoid personality disorder | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Clomipramine, disease=schizoid personality disorder | success | 1 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=paranoid personality disorder | success | 0 |  |
| 13 | ictrp | 2026-03-09 | drug=Clomipramine, disease=paranoid personality disorder | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Clomipramine, disease=paranoid personality disorder | success | 2 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=histrionic personality disorder (disease) | success | 0 |  |
| 16 | ictrp | 2026-03-09 | drug=Clomipramine, disease=histrionic personality disorder (disease) | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Clomipramine, disease=histrionic personality disorder (disease) | success | 0 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=schizotypal personality disorder | success | 0 |  |
| 19 | ictrp | 2026-03-09 | drug=Clomipramine, disease=schizotypal personality disorder | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Clomipramine, disease=schizotypal personality disorder | success | 5 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=agoraphobia | success | 0 |  |
| 22 | ictrp | 2026-03-09 | drug=Clomipramine, disease=agoraphobia | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Clomipramine, disease=agoraphobia | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=major depressive disorder | success | 10 |  |
| 25 | ictrp | 2026-03-09 | drug=Clomipramine, disease=major depressive disorder | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Clomipramine, disease=major depressive disorder | success | 20 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=endogenous depression | success | 0 |  |
| 28 | ictrp | 2026-03-09 | drug=Clomipramine, disease=endogenous depression | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Clomipramine, disease=endogenous depression | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Clomipramine, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Clomipramine, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Clomipramine, disease=attention deficit-hyperactivity disorder | success | 20 |  |