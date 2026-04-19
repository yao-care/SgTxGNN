# Clozapine 老藥新用分析報告

## 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物 (INN) | Clozapine | |
| DrugBank ID | DB00363 | |
| 中文商品名 | [Data Gap] | |
| 原核准適應症 | [Data Gap] | [來源：TFDA 許可證] |
| 原作用機轉 | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 未上市 | TFDA |

## 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 文獻 | 決策階段 | 開發建議 |
|------|-----------|-----------|---------|---------|------|---------|---------:|
| 1 | manic bipolar affective disorder | 99.95% | L2 | 6 | 20 | S2 | Proceed with Guardrails |
| 2 | Tourette syndrome | 99.91% | L4 | 0 | 20 | S1 | Research Question |
| 3 | trichotillomania | 99.90% | L5 | 0 | 0 | S0 | Hold |
| 4 | schizophreniform disorder | 99.69% | L2 | 6 | 20 | S2 | Proceed with Guardrails |
| 5 | bipolar disorder | 99.62% | L2 | 23 | 20 | S3 | Proceed with Guardrails |
| 6 | major affective disorder | 99.48% | L3 | 14 | 20 | S2 | Research Question |
| 7 | attention deficit-hyperactivity disorder | 99.31% | L5 | 1 | 20 | S0 | Hold |
| 8 | attention deficit hyperactivity disorder, inattentive type | 99.21% | L5 | 0 | 0 | S0 | Hold |
| 9 | psychotic disorder | 99.12% | L1 | 50 | 20 | S3 | Proceed with Guardrails |
| 10 | Malan overgrowth syndrome | 99.02% | L5 | 0 | 0 | S0 | Hold |

## 資料收集日誌
| # | 資料來源 | 查詢日期 | 查詢條件 | 結果狀態 | 筆數 | 備註 |
|---|---------|---------|---------|---------|------|------|
| 1 | ddi | 2026-03-09 | drug=Clozapine | not_found | 0 |  |
| 2 | drugbank | 2026-03-09 | drug=Clozapine | success | 1 |  |
| 3 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=manic bipolar affective disorder | success | 6 |  |
| 4 | ictrp | 2026-03-09 | drug=Clozapine, disease=manic bipolar affective disorder | success | 0 |  |
| 5 | pubmed | 2026-03-09 | drug=Clozapine, disease=manic bipolar affective disorder | success | 20 |  |
| 6 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=Tourette syndrome | success | 0 |  |
| 7 | ictrp | 2026-03-09 | drug=Clozapine, disease=Tourette syndrome | success | 0 |  |
| 8 | pubmed | 2026-03-09 | drug=Clozapine, disease=Tourette syndrome | success | 20 |  |
| 9 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=trichotillomania | success | 0 |  |
| 10 | ictrp | 2026-03-09 | drug=Clozapine, disease=trichotillomania | success | 0 |  |
| 11 | pubmed | 2026-03-09 | drug=Clozapine, disease=trichotillomania | success | 0 |  |
| 12 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=schizophreniform disorder | success | 6 |  |
| 13 | ictrp | 2026-03-09 | drug=Clozapine, disease=schizophreniform disorder | success | 0 |  |
| 14 | pubmed | 2026-03-09 | drug=Clozapine, disease=schizophreniform disorder | success | 20 |  |
| 15 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=bipolar disorder | success | 23 |  |
| 16 | ictrp | 2026-03-09 | drug=Clozapine, disease=bipolar disorder | success | 0 |  |
| 17 | pubmed | 2026-03-09 | drug=Clozapine, disease=bipolar disorder | success | 20 |  |
| 18 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=major affective disorder | success | 14 |  |
| 19 | ictrp | 2026-03-09 | drug=Clozapine, disease=major affective disorder | success | 0 |  |
| 20 | pubmed | 2026-03-09 | drug=Clozapine, disease=major affective disorder | success | 20 |  |
| 21 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=attention deficit-hyperactivity disorder | success | 1 |  |
| 22 | ictrp | 2026-03-09 | drug=Clozapine, disease=attention deficit-hyperactivity disorder | success | 0 |  |
| 23 | pubmed | 2026-03-09 | drug=Clozapine, disease=attention deficit-hyperactivity disorder | success | 20 |  |
| 24 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 25 | ictrp | 2026-03-09 | drug=Clozapine, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 26 | pubmed | 2026-03-09 | drug=Clozapine, disease=attention deficit hyperactivity disorder, inattentive type | success | 0 |  |
| 27 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=psychotic disorder | success | 50 |  |
| 28 | ictrp | 2026-03-09 | drug=Clozapine, disease=psychotic disorder | success | 0 |  |
| 29 | pubmed | 2026-03-09 | drug=Clozapine, disease=psychotic disorder | success | 20 |  |
| 30 | clinicaltrials | 2026-03-09 | drug=Clozapine, disease=Malan overgrowth syndrome | success | 0 |  |
| 31 | ictrp | 2026-03-09 | drug=Clozapine, disease=Malan overgrowth syndrome | success | 0 |  |
| 32 | pubmed | 2026-03-09 | drug=Clozapine, disease=Malan overgrowth syndrome | success | 0 |  |